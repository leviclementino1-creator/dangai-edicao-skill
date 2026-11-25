import json, glob, os
from PIL import Image, ImageDraw, ImageFont

B = 'G:/App Corte Cenas/Output/Nia Liston The Merciless Maiden/S01E08'
S = r'C:\Users\levic\AppData\Local\Temp\claude\f78c88a91d52f2f5\e6c6941a-74d2-41c1-9f4c-718121aa3fe8\scratchpad\nia\ep'
os.makedirs(S, exist_ok=True)
shots = json.load(open(B + '/metadata/shots.json', encoding='utf-8'))
proj = glob.glob('G:/Dangai Recap/Biblioteca/_projetos/Nia Liston The Merciless S01E08 - 2026-11-24 13h15/*.dangai')[0]
p = json.load(open(proj, encoding='utf-8'))
usados = {}
for n, s in enumerate(p['plan']['scenes'], 1):
    usados.setdefault(p['images'][s['imageIndex']]['fileName'][:4], []).append(n)
f = ImageFont.truetype('arialbd.ttf', 15)
TW, TH, COLS, ROWS = 256, 144, 8, 7
per = COLS * ROWS
for k in range(0, len(shots), per):
    sheet = Image.new('RGB', (COLS * TW, ROWS * (TH + 20)), 'black')
    for j, sh in enumerate(shots[k:k + per]):
        im = Image.open(f"{B}/keyframes/{sh['shot_id']}_1.jpg").convert('RGB').resize((TW, TH))
        x, y = (j % COLS) * TW, (j // COLS) * (TH + 20)
        sheet.paste(im, (x, y))
        d = ImageDraw.Draw(sheet)
        m, s_ = divmod(int(sh['start']), 60)
        u = usados.get(sh['shot_id'])
        txt = f"{sh['shot_id']} {m}:{s_:02d} {sh['duration']:.1f}s" + (f" USEI c{','.join(map(str, u))}" if u else '')
        d.rectangle([x, y + TH, x + TW, y + TH + 20], fill=(150, 0, 60) if u else (0, 0, 0))
        d.text((x + 3, y + TH + 2), txt, fill='white', font=f)
    sheet.save(f'{S}/ep{k // per + 1}.jpg', quality=82)
print(len(shots), 'shots', (len(shots) + per - 1) // per, 'folhas')
