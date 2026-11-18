import json, subprocess, sys
import numpy as np, cv2
# Detector de rostos do motor do recap. Rodar com o python do motor-runtime, de dentro da pasta do motor:
#   cd <repo>/modulos/recap/motor && %LOCALAPPDATA%\Dangai\recap\motor-runtime\venv\Scripts\python.exe rostos-cenas.py <projeto.dangai> <pasta_saida>
# Sai: <pasta>/faces.json (rostos de cada cena em 3 instantes: [cx, cy, w, h] em fracao do quadro) e fc_N.jpg
# (quadro do meio com os rostos em verde e a janela 9:16 em rosa).
import os
sys.path.insert(0, os.environ.get('DANGAI_MOTOR', r'G:\ClaudeEditor\dangai\modulos\recap\motor'))
from app.matching.face_detector import AnimeFaceDetector
from PIL import Image, ImageDraw, ImageFont
proj, S = sys.argv[1], sys.argv[2]
p = json.load(open(proj, encoding='utf8'))
det = AnimeFaceDetector()
W, H = 640, 360
def quadro(path, t):
    r = subprocess.run(['ffmpeg','-v','error','-ss',f'{t:.3f}','-i',path,'-frames:v','1','-vf',f'scale={W}:{H}','-f','rawvideo','-pix_fmt','bgr24','-'], capture_output=True)
    if len(r.stdout) != W*H*3: return None
    return np.frombuffer(r.stdout, np.uint8).reshape(H, W, 3).copy()
res = []
tiles = []
fonte = ImageFont.truetype('arialbd.ttf', 16)
for k, s in enumerate(p['plan']['scenes']):
    im = p['images'][s['imageIndex']]; ss = s.get('sourceStart') or 0; d = s['end'] - s['start']
    ts = [ss + 0.05, ss + d/2, ss + max(0.05, d - 0.08)]
    fr = [quadro(im['path'], t) for t in ts]
    boxes = det.detect_batch(fr, min_size=24, max_ratio=0.99)
    mid = fr[1] if fr[1] is not None else np.zeros((H,W,3),np.uint8)
    faces = [[(x+w/2)/W, (y+h/2)/H, w/W, h/H] for (x,y,w,h) in boxes[1]]
    todas = [[[(x+w/2)/W, w/W, h/H] for (x,y,w,h) in b] for b in boxes]
    res.append({'cena': k+1, 'arquivo': im['fileName'][:4], 'fx': im.get('focusX', .5), 'meio': faces, 'tres': todas})
    pil = Image.fromarray(cv2.cvtColor(mid, cv2.COLOR_BGR2RGB)); dr = ImageDraw.Draw(pil)
    for j,(x,y,w,h) in enumerate(boxes[1]):
        dr.rectangle([x,y,x+w,y+h], outline=(0,255,0), width=3); dr.text((x+3,y+3), str(j), fill=(0,255,0), font=fonte)
    fx = im.get('focusX', .5); cw = H*9/16; x0 = fx*(W-cw)
    dr.rectangle([x0,0,x0+cw,H-1], outline=(255,40,120), width=3)
    dr.line([x0+cw/2,0,x0+cw/2,H], fill=(255,40,120), width=1)
    dr.rectangle([0,H-22,W,H], fill=(0,0,0)); dr.text((4,H-21), f"#{k+1} {im['fileName'][:4]} fx{fx:.2f}", fill='white', font=fonte)
    tiles.append(pil.resize((320,180)))
json.dump(res, open(S+'/faces.json','w'), indent=0)
for parte in range(0, len(tiles), 25):
    g = tiles[parte:parte+25]; rows = (len(g)+4)//5
    out = Image.new('RGB', (5*324, rows*184))
    for i,t in enumerate(g): out.paste(t, ((i%5)*324, (i//5)*184))
    out.save(f'{S}/fc_{parte//25+1}.jpg', quality=85)
print('ok')
