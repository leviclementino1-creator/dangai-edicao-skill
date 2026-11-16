# python janela-cena.py <projeto.dangai> <saida> <cenas 1,2,3> [planos.json {id,s,e}]
import json, subprocess, sys
from io import BytesIO
from PIL import Image, ImageDraw, ImageFont
p = json.load(open(sys.argv[1], encoding='utf8')); saida = sys.argv[2]; quais=[int(x) for x in sys.argv[3].split(',')]
P = {x['id']:x for x in json.load(open(sys.argv[4] if len(sys.argv)>4 else 'G:/ClaudeEditor/_capturas/e2e-apo/planos.json',encoding='utf8'))}
f = ImageFont.truetype('arialbd.ttf', 16); TW, TH = 288, 162
linhas=[]
for n in quais:
    s=p['plan']['scenes'][n-1]; img=p['images'][s['imageIndex']]; d=s['end']-s['start']; ss=s.get('sourceStart',0) or 0
    pid=img['fileName'][:-4]; L=P[pid]['e']-P[pid]['s']; fx=img.get('focusX',.5)
    ts=[ss+0.05, ss+d*0.5, ss+d-0.08] + [L*k/4 for k in range(1,4)]
    row=Image.new('RGB',(TW*6+20,TH+22),(15,15,15)); dr=ImageDraw.Draw(row)
    for j,t in enumerate(ts):
        r=subprocess.run(['ffmpeg','-v','error','-ss',f'{max(t,0):.3f}','-i',img['path'],'-frames:v','1','-vf',f'scale={TW}:{TH}','-f','image2pipe','-vcodec','png','-'],capture_output=True)
        if not r.stdout: continue
        im=Image.open(BytesIO(r.stdout)).convert('RGB'); x=j*TW+(20 if j>=3 else 0); row.paste(im,(x,0))
        cw=TH*9/16; x0=x+fx*(TW-cw)
        if j<3: ImageDraw.Draw(row).rectangle((x0,0,x0+cw,TH-1),outline='yellow',width=2)
        dr.text((x+3,TH+2),f't{t:.1f}',fill='cyan' if j>=3 else 'white',font=f)
    dr.text((3,3),f'#{n} {pid} d{d:.1f} clip{L:.1f} fx{fx:.2f} in{ss:.1f}',fill='yellow',font=f,stroke_width=2,stroke_fill='black')
    linhas.append(row)
for k in range(0,len(linhas),9):
    g=linhas[k:k+9]; out=Image.new('RGB',(g[0].width,sum(r.height+4 for r in g))); y=0
    for r in g: out.paste(r,(0,y)); y+=r.height+4
    out.save(f'{saida}_{k//9+1}.jpg',quality=85)
