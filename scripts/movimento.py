# python movimento.py <projeto.dangai> : movimento medio dentro do recorte 9:16 de cada cena
import json, subprocess, sys
import numpy as np
p = json.load(open(sys.argv[1], encoding='utf8'))
def mov(path, ss, d, fx):
    r = subprocess.run(['ffmpeg','-v','error','-ss',f'{ss:.3f}','-t',f'{max(d,0.2):.3f}','-i',path,'-vf',f'fps=8,crop=ih*9/16:ih:{fx}*(iw-ih*9/16):0,scale=54:96,format=gray','-f','rawvideo','-'],capture_output=True)
    a = np.frombuffer(r.stdout, np.uint8)
    n = a.size // (54*96)
    if n < 2: return 0.0
    a = a[:n*54*96].reshape(n,96,54).astype(np.float32)
    return float(np.abs(np.diff(a,axis=0)).mean())
out = []
for k, s in enumerate(p['plan']['scenes']):
    img = p['images'][s['imageIndex']]; d = s['end'] - s['start']; ss = s.get('sourceStart', 0) or 0
    m = mov(img['path'], ss, d, img.get('focusX', .5))
    out.append((k+1, img['fileName'][:4], round(d,2), round(m,2)))
for o in sorted(out, key=lambda x: x[3]): print(*o)
