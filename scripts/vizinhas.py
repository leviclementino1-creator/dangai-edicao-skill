import json, subprocess, io, sys
from PIL import Image
import numpy as np
c = json.load(open(sys.argv[1], encoding='utf8'))
def q(p, t):
    b = subprocess.run(['ffmpeg', '-v', 'error', '-ss', f'{t:.2f}', '-i', p, '-frames:v', '1', '-vf', 'scale=64:36', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-'], capture_output=True).stdout
    return np.frombuffer(b, np.uint8).reshape(36, 64, 3).astype(float) if len(b) == 64*36*3 else None
prev = None
for x in c:
    p = x['clipe'].replace(chr(92), '/'); e = x['entrada']; d = x['duracao']
    a = q(p, e + 0.05); b = q(p, e + max(0.05, d - 0.1))
    if prev is not None and a is not None and prev[1] is not None:
        dif = np.abs(prev[1] - a).mean()
        hist = sum(np.abs(np.histogram(prev[1][..., k], 16, (0, 255))[0] - np.histogram(a[..., k], 16, (0, 255))[0]).sum() for k in range(3)) / (64*36*3)
        flag = 'IGUAL?' if dif < 25 or hist < 0.25 else ''
        print(prev[0], '->', x['cena'], prev[2], p[-8:-4], round(dif, 1), round(hist, 2), flag)
    prev = (x['cena'], b if b is not None else a, p[-8:-4])
