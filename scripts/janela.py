import json, subprocess, sys
from io import BytesIO
from PIL import Image, ImageDraw, ImageFont
p = json.load(open(sys.argv[1], encoding='utf8')); saida = sys.argv[2]
try: fonte = ImageFont.truetype('arialbd.ttf', 15)
except Exception: fonte = ImageFont.load_default()
TW, TH = 320, 180
tiles = []
for k, s in enumerate(p['plan']['scenes']):
    img = p['images'][s['imageIndex']]; d = s['end'] - s['start']; ss = s.get('sourceStart', 0) or 0
    t = ss + min(d, 1.0) * 0.5
    r = subprocess.run(['ffmpeg','-v','error','-ss',f'{t:.3f}','-i',img['path'],'-frames:v','1','-vf',f'scale={TW}:{TH}','-f','image2pipe','-vcodec','png','-'],capture_output=True)
    im = Image.open(BytesIO(r.stdout)).convert('RGB') if r.stdout else Image.new('RGB', (TW, TH))
    cw = TH * 9 / 16; x0 = img.get('focusX', 0.5) * (TW - cw)
    dr = ImageDraw.Draw(im)
    dr.rectangle([x0, 0, x0 + cw, TH - 1], outline=(255, 40, 120), width=3)
    dr.line([x0 + cw / 2, 0, x0 + cw / 2, 12], fill=(255, 40, 120), width=2)
    dr.rectangle([0, TH - 20, TW, TH], fill=(0, 0, 0))
    dr.text((4, TH - 19), f"#{k+1} {img['fileName'][:4]} fx{img.get('focusX',0.5):.2f} {d:.1f}s", fill='white', font=fonte)
    tiles.append(im)
cols = 6
for parte in range(0, len(tiles), 30):
    g = tiles[parte:parte + 30]; rows = (len(g) + cols - 1) // cols
    out = Image.new('RGB', (cols * (TW + 4), rows * (TH + 4)))
    for i, t in enumerate(g): out.paste(t, ((i % cols) * (TW + 4), (i // cols) * (TH + 4)))
    out.save(f'{saida}_{parte//30+1}.jpg', quality=82)
print('ok')
