# python ranking-animacao.py <pasta do episodio com shots/> [min_seg] [saida.json]
# Mede o movimento (diferenca media entre quadros) de TODOS os planos do episodio e lista os mais animados.
# Rode ANTES de escolher as cenas: o gancho e as cenas de poder saem do topo desta lista.
import cv2, glob, os, sys, numpy as np, json
res=[]
for f in sorted(glob.glob(os.path.join(sys.argv[1],'shots','*.mp4'))):
    c=cv2.VideoCapture(f); n=int(c.get(7)); fps=c.get(5) or 24
    prev=None; d=[]; i=0
    while True:
        ok=c.grab()
        if not ok: break
        if i%2==0:
            ok,fr=c.retrieve()
            g=cv2.cvtColor(cv2.resize(fr,(160,90)),cv2.COLOR_BGR2GRAY).astype(np.float32)
            if prev is not None: d.append(float(np.abs(g-prev).mean()))
            prev=g
        i+=1
    res.append((os.path.basename(f)[:4], round(n/fps,2), round(float(np.median(d)) if d else 0,1)))
if len(sys.argv)>3: json.dump(res,open(sys.argv[3],'w'))  # 3o arg = json de saida (fora da Biblioteca: ela e so leitura)
res=[r for r in res if r[1]>=(float(sys.argv[2]) if len(sys.argv)>2 else 0.6)]
res.sort(key=lambda r:-r[2])
print('plano, duracao, movimento (>25 = muito animado)')
for r in res[:60]: print(*r)
