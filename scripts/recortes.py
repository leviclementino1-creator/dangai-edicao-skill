import json, subprocess, sys, numpy as np
from PIL import Image, ImageDraw, ImageFont
p = json.load(open(sys.argv[1], encoding='utf8'))
saida = sys.argv[2]
try: fonte = ImageFont.truetype('arialbd.ttf', 14)
except Exception: fonte = ImageFont.load_default()
W, H = 108, 192
def quadro(path, t):
    r = subprocess.run(['ffmpeg','-v','error','-ss',f'{max(t,0):.3f}','-i',path,'-frames:v','1','-vf','scale=640:-2','-f','image2pipe','-vcodec','png','-'],capture_output=True)
    from io import BytesIO
    return Image.open(BytesIO(r.stdout)).convert('RGB') if r.stdout else None
def recorte(im, fx, fy):
    w, h = im.size; cw = h * 9 / 16
    if cw > w: cw = w
    x0 = fx * (w - cw)
    return im.crop((int(x0), 0, int(x0 + cw), h)).resize((W, H))
cenas = p['plan']['scenes']; imgs = p['images']
tiles = []
for k, s in enumerate(cenas):
    img = imgs[s['imageIndex']]; d = s['end'] - s['start']; ss = s.get('sourceStart', 0) or 0
    pid = img['fileName'].replace('.mp4', '')
    par = []
    for t in (ss + 0.05, ss + max(d - 0.1, 0.05)):
        im = quadro(img['path'], t)
        par.append(recorte(im, img.get('focusX', 0.5), img.get('focusY', 0.5)) if im else Image.new('RGB', (W, H)))
    t = Image.new('RGB', (W * 2 + 4, H + 36), (20, 20, 20)); t.paste(par[0], (0, 0)); t.paste(par[1], (W + 4, 0))
    dr = ImageDraw.Draw(t)
    dr.text((2, H + 2), f"#{k+1} {pid} {d:.1f}s", fill='white', font=fonte)
    dr.text((2, H + 18), f"fx{img.get('focusX',0.5):.2f} in{ss:.1f} {'A' if img.get('focusAuto') else 'M'}", fill=(180, 180, 180), font=fonte)
    tiles.append(t)
cols = 10
for parte in range(0, len(tiles), 30):
    grupo = tiles[parte:parte + 30]
    rows = (len(grupo) + cols - 1) // cols
    tw, th = grupo[0].size
    out = Image.new('RGB', (cols * (tw + 6), rows * (th + 6)), (0, 0, 0))
    for i, t in enumerate(grupo): out.paste(t, ((i % cols) * (tw + 6), (i // cols) * (th + 6)))
    out.save(f'{saida}_{parte//30+1}.jpg', quality=82)
print('ok', len(tiles))
