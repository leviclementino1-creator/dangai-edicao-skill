# python folha-final.py <projeto.dangai> <saida>  -> <saida>_1.jpg, _2.jpg...
# Todas as cenas como o Dangai mostra: recorte 9:16 pelo focusX (ou pela camera livre) com o zoom
# do efeito, no 1o e no ultimo quadro de cada cena. Conferencia final antes de entregar.
import json, subprocess, sys
from io import BytesIO
from PIL import Image, ImageDraw, ImageFont
p = json.load(open(sys.argv[1], encoding='utf8'))
try: f = ImageFont.truetype('arialbd.ttf', 13)
except Exception: f = ImageFont.load_default()
W, H = 96, 170
def q(path, t):
    for k in range(5):
        r = subprocess.run(['ffmpeg','-v','error','-ss',f'{max(t-0.15*k,0):.3f}','-i',path,'-frames:v','1','-vf','scale=-2:540','-f','image2pipe','-vcodec','png','-'], capture_output=True)
        if r.stdout: return Image.open(BytesIO(r.stdout)).convert('RGB')
    return Image.new('RGB', (960, 540))
def recorte(im, cx, esc):
    w, h = im.size; cw = h*9/16; x0 = max(0, min(w-cw, cx*w-cw/2)); c = im.crop((int(x0), 0, int(x0+cw), h))
    if esc > 1:
        cw2, ch2 = c.width/esc, c.height/esc
        c = c.crop((int((c.width-cw2)/2), int((c.height-ch2)/2), int((c.width+cw2)/2), int((c.height+ch2)/2)))
    return c.resize((W, H))
tiles = []
for k, s in enumerate(p['plan']['scenes']):
    img = p['images'][s['imageIndex']]; d = s['end']-s['start']; ss = s.get('sourceStart', 0) or 0; cam = s.get('camera')
    t = Image.new('RGB', (W*2+4, H+16), (20, 20, 20))
    for j, (tt, fr) in enumerate([(ss+0.04, 0.0), (ss+d-0.06, 1.0)]):
        im = q(img['path'], tt)
        if cam:
            c = cam['from'] if j == 0 else cam['to']; cx = 0.5-c['x']/100; esc = c['scale']
        else:
            cx = 0.158+img.get('focusX', .5)*0.684; e = s.get('effect'); i = s.get('intensity', 0.1)
            esc = 1+i*fr if e == 'zoom-in' else (1+i*(1-fr) if e == 'zoom-out' else 1+i)
        t.paste(recorte(im, cx, esc), (j*(W+4), 0))
    ImageDraw.Draw(t).text((2, H+1), f"#{k+1} {img['fileName'][:4]}{' grid' if s.get('imageIndexB') is not None else ''}", fill='white', font=f)
    tiles.append(t)
c = 10
for g in range(0, len(tiles), 25):
    gr = tiles[g:g+25]; out = Image.new('RGB', (c*(gr[0].width+5), ((len(gr)+c-1)//c)*(gr[0].height+5)))
    for i, t in enumerate(gr): out.paste(t, ((i % c)*(t.width+5), (i//c)*(t.height+5)))
    out.save(f'{sys.argv[2]}_{g//25+1}.jpg', quality=85)
print('ok', len(tiles))
