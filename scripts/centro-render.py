import json, subprocess, sys, os
import numpy as np, cv2
sys.path.insert(0, r'G:\ClaudeEditor\dangai\modulos\recap\motor')
from app.matching.face_detector import AnimeFaceDetector
from PIL import Image, ImageDraw, ImageFont

proj, video, S = sys.argv[1], sys.argv[2], sys.argv[3]
os.makedirs(S, exist_ok=True)
p = json.load(open(proj, encoding='utf8'))
det = AnimeFaceDetector()
W, H = 360, 640
fonte = ImageFont.truetype('arialbd.ttf', 18)


def quadro(t):
    r = subprocess.run(['ffmpeg', '-v', 'error', '-ss', f'{t:.3f}', '-i', video, '-frames:v', '1', '-vf', f'scale={W}:{H}',
                        '-f', 'rawvideo', '-pix_fmt', 'bgr24', '-'], capture_output=True)
    if len(r.stdout) != W * H * 3:
        return None
    return np.frombuffer(r.stdout, np.uint8).reshape(H, W, 3).copy()


res, tiles = [], []
for k, s in enumerate(p['plan']['scenes']):
    im = p['images'][s['imageIndex']]
    a, b = s['start'], s['end']
    ts = [a + 0.12, (a + b) / 2, b - 0.12]
    fr = [quadro(t) for t in ts]
    ok = [f if f is not None else np.zeros((H, W, 3), np.uint8) for f in fr]
    boxes = det.detect_batch(ok, min_size=30, max_ratio=0.99)
    med = []
    for bx in boxes:
        if len(bx):
            x, y, w, h = max(bx, key=lambda q: q[2] * q[3])
            med.append(round((x + w / 2) / W, 3))
        else:
            med.append(None)
    res.append({'cena': k + 1, 'clipe': im['fileName'][:4], 'fx': round(im.get('focusX', .5), 3),
                'camera': bool(s.get('camera')), 'efeito': s.get('effect'), 'zoomFixo': s.get('escala'),
                'grid': s.get('imageIndexB') is not None, 'cx_render': med})
    row = []
    for f, bx in zip(ok, boxes):
        pil = Image.fromarray(cv2.cvtColor(f, cv2.COLOR_BGR2RGB)); dr = ImageDraw.Draw(pil)
        dr.line([W / 2, 0, W / 2, H], fill=(255, 40, 120), width=2)
        for (x, y, w, h) in bx:
            dr.rectangle([x, y, x + w, y + h], outline=(0, 255, 0), width=3)
        row.append(pil.resize((180, 320)))
    t = Image.new('RGB', (540, 345), 'black')
    for j, r_ in enumerate(row):
        t.paste(r_, (j * 180, 0))
    ImageDraw.Draw(t).text((4, 322), f"#{k+1} {im['fileName'][:4]} fx{im.get('focusX', .5):.2f} {'CAM' if s.get('camera') else ''} {med}", fill='white', font=fonte)
    tiles.append(t)
json.dump(res, open(S + '/render.json', 'w'), indent=0)
for parte in range(0, len(tiles), 12):
    folha = Image.new('RGB', (540 * 3, 345 * 4), 'black')
    for j, t in enumerate(tiles[parte:parte + 12]):
        folha.paste(t, ((j % 3) * 540, (j // 3) * 345))
    folha.save(f'{S}/folha{parte // 12 + 1}.jpg', quality=85)
for r in res:
    print(r)
