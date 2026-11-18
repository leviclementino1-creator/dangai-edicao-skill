# Nitidez (variancia do Laplaciano) DENTRO da janela 9:16 de cada cena, comparada com o clipe inteiro.
# uso: python nitidez.py <projeto.dangai>   -> lista as cenas com trecho borrado (< 45% do mais nitido
# do clipe): foco mudando no comeco, fade, pan borrado. Conserto: entrada (sourceStart) depois do borrao.
import json, subprocess, sys
import numpy as np, cv2
p = json.load(open(sys.argv[1], encoding='utf8'))
W,H=480,270
def nit(path,t,fx):
    r=subprocess.run(['ffmpeg','-v','error','-ss',f'{t:.3f}','-i',path,'-frames:v','1','-vf',f'scale={W}:{H}','-f','rawvideo','-pix_fmt','gray','-'],capture_output=True)
    if len(r.stdout)!=W*H: return None
    g=np.frombuffer(r.stdout,np.uint8).reshape(H,W)
    cx=0.158+fx*0.684; x0=int((cx-0.158)*W); g=g[:,max(0,x0):x0+int(0.316*W)]
    return cv2.Laplacian(g,cv2.CV_64F).var()
def dur(path):
    r=subprocess.run(['ffmpeg','-hide_banner','-i',path],capture_output=True,text=True)
    import re; m=re.search(r'Duration: (\d+):(\d+):([\d.]+)',r.stderr); return int(m[1])*3600+int(m[2])*60+float(m[3])
for k,s in enumerate(p['plan']['scenes']):
    im=p['images'][s['imageIndex']]; ss=s.get('sourceStart') or 0; d=s['end']-s['start']; fx=im.get('focusX',.5)
    D=dur(im['path'])
    cena=[nit(im['path'],ss+d*f,fx) for f in (0.02,0.5,0.95)]
    clipe=[nit(im['path'],D*f,fx) for f in (0.1,0.3,0.5,0.7,0.9)]
    mx=max(v for v in clipe+cena if v)
    mn=min(v for v in cena if v is not None)
    if mn < 0.45*mx: print(k+1, im['fileName'][:4], 'cena',[round(v or 0) for v in cena],'clipe',[round(v or 0) for v in clipe], f'entrada {ss} dur {d:.2f} clip {D:.2f}')
