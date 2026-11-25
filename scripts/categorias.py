import json, glob, os, sys
from PIL import Image, ImageDraw, ImageFont

B = 'G:/App Corte Cenas/Output/Nia Liston The Merciless Maiden/S01E08'
S = sys.argv[1]
os.makedirs(S, exist_ok=True)
shots = {s['shot_id']: s for s in json.load(open(B + '/metadata/shots.json', encoding='utf-8'))}
proj = glob.glob('G:/Dangai Recap/Biblioteca/_projetos/Nia Liston The Merciless S01E08 - 2026-11-24 13h15/*.dangai')[0]
p = json.load(open(proj, encoding='utf-8'))
usados = {}
for n, s in enumerate(p['plan']['scenes'], 1):
    usados.setdefault(p['images'][s['imageIndex']]['fileName'][:4], []).append(n)
CATS = json.loads(open(sys.argv[2], encoding='utf-8').read())
f = ImageFont.truetype('arialbd.ttf', 17)
TW, TH = 320, 180
for nome, lista in CATS.items():
    per = 4 * 6  # 4 colunas x 6 linhas, 1 quadro (o do meio) maior
    for parte in range(0, len(lista), per):
        sub = lista[parte:parte + per]
        W2, H2 = 400, 225
        sheet = Image.new('RGB', (4 * W2, ((len(sub) + 3) // 4) * (H2 + 24)), 'black')
        d = ImageDraw.Draw(sheet)
        for j, (sid, nota) in enumerate(sub):
            sh = shots[sid]
            im = Image.open(f"{B}/keyframes/{sid}_1.jpg").convert('RGB').resize((W2, H2))
            x, y = (j % 4) * W2, (j // 4) * (H2 + 24)
            sheet.paste(im, (x, y))
            m, s_ = divmod(int(sh['start']), 60)
            u = usados.get(sid)
            d.rectangle([x, y + H2, x + W2, y + H2 + 24], fill=(150, 0, 60) if u else (0, 90, 40))
            d.text((x + 4, y + H2 + 3), f"{sid} {m}:{s_:02d} {sh['duration']:.1f}s " + (f"JA USEI (c{','.join(map(str, u))})" if u else f"NOVA - {nota}"), fill='white', font=f)
        sheet.save(f'{S}/{nome}{"" if parte == 0 else parte // per + 1}.jpg', quality=85)
        print(nome, len(sub))
