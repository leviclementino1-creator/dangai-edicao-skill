import json, os
from PIL import Image, ImageDraw, ImageFont
F = json.load(open('frases.json', encoding='utf8')); P = json.load(open('planos.json', encoding='utf8'))
por = {p['id']: p for p in P}
try: fonte = ImageFont.truetype('arial.ttf', 15); fb = ImageFont.truetype('arialbd.ttf', 17)
except Exception: fonte = fb = ImageFont.load_default()
TW, TH = 240, 135
def cands(f):
    ids = []
    def add(i):
        if i in por and i not in ids: ids.append(i)
    for a in f['app']:
        for i in a['planos']: add(i)
    for c in f['fita']:
        for i in c['planos']: add(i)
    janelas = [(e['t0'], e['t1']) for e in f['eventos'] if e['t0'] is not None]
    if f['cue']: janelas.append((f['cue']['t'] - 8, f['cue']['t'] + 8))
    for p in P:
        if any(p['s'] < b and p['e'] > a for a, b in janelas): add(p['id'])
    return ids[:35]
def folha(fs, saida):
    blocos = []
    for f in fs:
        ids = cands(f); app = {i for a in f['app'] for i in a['planos']}; fita = {i for c in f['fita'] for i in c['planos']}
        cols = 7; rows = (len(ids) + cols - 1) // cols
        im = Image.new('RGB', (cols * TW, 70 + rows * (TH + 20)), (18, 18, 18)); d = ImageDraw.Draw(im)
        d.text((6, 4), f"{f['id']} [{f['secao']}] {f['dur']:.1f}s  {f['texto'][:110]}", fill='white', font=fb)
        d.text((6, 28), (f['texto'][110:220]), fill='white', font=fb)
        d.text((6, 50), 'evento: ' + '; '.join((e['resumo'] or '')[:70] for e in f['eventos']), fill=(170, 170, 170), font=fonte)
        for k, i in enumerate(ids):
            p = por[i]; x = (k % cols) * TW; y = 70 + (k // cols) * (TH + 20)
            try: t = Image.open(p['kf']).convert('RGB').resize((TW - 4, TH - 4))
            except Exception: continue
            im.paste(t, (x + 2, y + 2))
            cor = (255, 60, 120) if i in app else ((80, 180, 255) if i in fita else None)
            if cor: d.rectangle([x, y, x + TW - 1, y + TH - 1], outline=cor, width=4)
            d.text((x + 4, y + TH + 1), f"{i} {p['e']-p['s']:.1f}s {p['s']:.0f}s {'/'.join(n[:6] for n in p['pers'][:2])}", fill='white', font=fonte)
        blocos.append(im)
    W = max(b.width for b in blocos); H = sum(b.height for b in blocos)
    out = Image.new('RGB', (W, H), (0, 0, 0)); y = 0
    for b in blocos: out.paste(b, (0, y)); y += b.height
    out.save(saida, quality=80)
for k in range(0, len(F), 2):
    folha(F[k:k + 2], f'folhas/f{k:02d}.jpg')
print('ok')
