import json, subprocess, sys
import numpy as np, cv2
sys.path.insert(0, r'G:\ClaudeEditor\dangai\modulos\recap\motor')
from app.matching.face_detector import AnimeFaceDetector
from PIL import Image, ImageDraw, ImageFont

B = 'G:/App Corte Cenas/Output/Nia Liston The Merciless Maiden/S01E08'
OUT = sys.argv[1]
T = json.loads(open(sys.argv[2], encoding='utf-8').read())  # [[cena, shot, nota, fx_manual|null], ...]
det = AnimeFaceDetector()
W, H = 1280, 720


def quadro(path, t):
    r = subprocess.run(['ffmpeg', '-v', 'error', '-ss', f'{t:.3f}', '-i', path, '-frames:v', '1', '-vf', f'scale={W}:{H}',
                       '-f', 'rawvideo', '-pix_fmt', 'bgr24', '-'], capture_output=True)
    if len(r.stdout) != W * H * 3:
        return None
    return np.frombuffer(r.stdout, np.uint8).reshape(H, W, 3).copy()


def dur(path):
    r = subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', path], capture_output=True, text=True)
    return float(r.stdout.strip() or 1)


f = ImageFont.truetype('arialbd.ttf', 15)
CW = int(H * 9 / 16)  # 405
TW, TH = 162, 288
tiles = []
for cena, shot, nota, fxm in T:
    p = f'{B}/shots/{shot}.mp4'
    d = dur(p)
    ts = [0.08, d / 2, max(0.08, d - 0.12)]
    fr = [quadro(p, t) for t in ts]
    fr = [x if x is not None else np.zeros((H, W, 3), np.uint8) for x in fr]
    boxes = det.detect_batch([cv2.resize(x, (640, 360)) for x in fr], min_size=24, max_ratio=0.99)
    allb = [b for bx in boxes for b in bx]
    if fxm is not None:
        fx = fxm
    elif allb:
        x, y, w, h = max(allb, key=lambda q: q[2] * q[3])
        cx = (x + w / 2) / 640
        fx = min(1, max(0, (cx - 0.158) / 0.684))
    else:
        fx = 0.5
    x0 = int(fx * (W - CW))
    row = Image.new('RGB', (3 * TW + 8, TH + 40), 'black')
    for i, x in enumerate(fr):
        crop = cv2.cvtColor(x[:, x0:x0 + CW], cv2.COLOR_BGR2RGB)
        im = Image.fromarray(crop).resize((TW, TH))
        dd = ImageDraw.Draw(im); dd.line([TW / 2, 0, TW / 2, TH], fill=(255, 40, 120), width=1)
        row.paste(im, (i * (TW + 4), 0))
    ImageDraw.Draw(row).text((3, TH + 2), f"c{cena} {shot} fx{fx:.2f} {d:.1f}s", fill=(255, 230, 0), font=f)
    ImageDraw.Draw(row).text((3, TH + 20), nota[:52], fill='white', font=f)
    tiles.append(row)
    print(cena, shot, round(fx, 3), round(d, 2), 'rostos' if allb else 'sem rosto')
cols = 3
rw, rh = tiles[0].size
sheet = Image.new('RGB', (cols * (rw + 12), ((len(tiles) + cols - 1) // cols) * (rh + 8)), (20, 20, 20))
for j, t in enumerate(tiles):
    sheet.paste(t, ((j % cols) * (rw + 12), (j // cols) * (rh + 8)))
sheet.save(OUT, quality=85)
