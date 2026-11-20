"""Folhas do RECONHECER NA MAO: uma linha por grupo de rostos (ate 8) com a key, as cenas e o
palpite do motor; e uma folha do elenco (foto + indice + nome) para dar nome a cada grupo.
uso: python folha-grupos.py <pasta do reconhecer.mjs>   ->  <pasta>/folha_N.jpg e <pasta>/elenco.jpg
"""
import json, os, sys
from PIL import Image, ImageDraw, ImageFont

pasta = sys.argv[1]
d = json.load(open(os.path.join(pasta, 'grupos.json'), encoding='utf8'))
try:
    f = ImageFont.truetype('arialbd.ttf', 15)
except Exception:
    f = ImageFont.load_default()
T = 110  # lado de cada rosto
POR_FOLHA = 12
grupos = d['grupos']
for n in range(0, len(grupos), POR_FOLHA):
    lote = grupos[n:n + POR_FOLHA]
    out = Image.new('RGB', (300 + 8 * (T + 4), len(lote) * (T + 6)), (18, 18, 18))
    dr = ImageDraw.Draw(out)
    for r, g in enumerate(lote):
        y = r * (T + 6)
        palp = g['sugestao']['nome'] if g.get('sugestao') else '-'
        sug = ', '.join(s['nome'] for s in g.get('sugestoes', [])[:2])
        dr.text((6, y + 6), f"g{g['key']}  {g['cenas']} cenas", fill=(255, 220, 0), font=f)
        dr.text((6, y + 28), ('JA TEM NOME: ' if g['conhecido'] else 'palpite: ') + palp[:28], fill=(255, 255, 255), font=f)
        dr.text((6, y + 50), sug[:34], fill=(170, 170, 170), font=f)
        if g['figurante']:
            dr.text((6, y + 72), 'figurante', fill=(255, 90, 90), font=f)
        for i in range(g['rostos']):
            arq = os.path.join(pasta, f"g{g['key']}_{i}.jpg")
            if os.path.exists(arq):
                out.paste(Image.open(arq).convert('RGB').resize((T, T)), (300 + i * (T + 4), y))
    out.save(os.path.join(pasta, f'folha_{n // POR_FOLHA + 1}.jpg'), quality=85)
el = d.get('elenco', [])
if el:
    C = 8
    W = 150
    out = Image.new('RGB', (C * W, ((len(el) + C - 1) // C) * (W + 40)), (18, 18, 18))
    dr = ImageDraw.Draw(out)
    for k, e in enumerate(el):
        x, y = (k % C) * W, (k // C) * (W + 40)
        arq = os.path.join(pasta, 'elenco', f"{e['i']}.jpg")
        if os.path.exists(arq):
            out.paste(Image.open(arq).convert('RGB').resize((W - 10, W - 10)), (x + 5, y))
        dr.text((x + 5, y + W - 8), e['nome'][:20], fill=(255, 255, 255), font=f)
        dr.text((x + 5, y + W + 10), e['nome'][20:40], fill=(255, 255, 255), font=f)
    out.save(os.path.join(pasta, 'elenco.jpg'), quality=85)
print('ok', len(grupos), 'grupos,', len(el), 'no elenco')
