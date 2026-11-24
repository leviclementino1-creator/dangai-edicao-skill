import json, subprocess, sys
import numpy as np
sys.path.insert(0, r'G:\ClaudeEditor\dangai\modulos\recap\motor')
from app.matching.face_detector import AnimeFaceDetector

proj, S = sys.argv[1], sys.argv[2]
p = json.load(open(proj, encoding='utf8'))
rend = {r['cena']: r for r in json.load(open(S + '/render.json'))}
det = AnimeFaceDetector()
W, H = 640, 360


def quadro(path, t):
    r = subprocess.run(['ffmpeg', '-v', 'error', '-ss', f'{t:.3f}', '-i', path, '-frames:v', '1', '-vf', f'scale={W}:{H}',
                        '-f', 'rawvideo', '-pix_fmt', 'bgr24', '-'], capture_output=True)
    if len(r.stdout) != W * H * 3:
        return np.zeros((H, W, 3), np.uint8)
    return np.frombuffer(r.stdout, np.uint8).reshape(H, W, 3).copy()


for k, s in enumerate(p['plan']['scenes']):
    r = rend[k + 1]
    if r['camera'] or r['cx_render'][1] is None:
        continue
    im = p['images'][s['imageIndex']]
    ss = s.get('sourceStart') or 0
    d = s['end'] - s['start']
    t = ss + d / 2
    bx = det.detect_batch([quadro(im['path'], t)], min_size=24, max_ratio=0.99)[0]
    fx = im.get('focusX', .5)
    win = 0.158 + fx * 0.684
    caras = [round((x + w / 2) / W, 3) for (x, y, w, h) in bx]
    prev = [round(0.5 + (c - win) / 0.316, 3) for c in caras]
    # foco que centralizaria o maior rosto
    if bx:
        x, y, w, h = max(bx, key=lambda q: q[2] * q[3])
        c = (x + w / 2) / W
        certo = round(min(1, max(0, (c - 0.158) / 0.684)), 3)
    else:
        certo = None
    print(f"cena {k+1:2d} {im['fileName'][:4]} entrada {ss:5.2f} fx {fx:.3f} | rosto fonte {caras} -> previsto no 9:16 {prev} | medido no render {r['cx_render'][1]} | fx certo {certo}")
