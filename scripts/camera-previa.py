import json, subprocess, sys
import numpy as np, cv2
from PIL import Image, ImageDraw, ImageFont
B='G:/App Corte Cenas/Output/Nia Liston The Merciless Maiden/S01E08'
T=json.loads(open(sys.argv[2],encoding='utf-8').read())
W,H=1280,720; CW=int(H*9/16)
def bez(t,p=(0,0,0.052,0.964)):
    # cubic-bezier ease (x1,y1,x2,y2): resolve x->y por busca
    x1,y1,x2,y2=p
    lo,hi=0.0,1.0
    for _ in range(40):
        m=(lo+hi)/2; x=3*(1-m)**2*m*x1+3*(1-m)*m*m*x2+m**3
        lo,hi=(m,hi) if x<t else (lo,m)
    m=(lo+hi)/2; return 3*(1-m)**2*m*y1+3*(1-m)*m*m*y2+m**3
f=ImageFont.truetype('arialbd.ttf',15); TW,TH=150,267
rows=[]
for c,s,ent,dur,a,b,nota in T:
    row=Image.new('RGB',(4*(TW+4),TH+40),'black')
    for i,u in enumerate([0,0.15,0.5,1.0]):
        t=ent+u*dur*0.97
        r=subprocess.run(['ffmpeg','-v','error','-ss',f'{t:.2f}','-i',f'{B}/shots/{s}.mp4','-frames:v','1','-vf',f'scale={W}:{H}','-f','rawvideo','-pix_fmt','bgr24','-'],capture_output=True)
        while len(r.stdout)!=W*H*3 and t>0.05:
            t-=0.1; r=subprocess.run(['ffmpeg','-v','error','-ss',f'{t:.2f}','-i',f'{B}/shots/{s}.mp4','-frames:v','1','-vf',f'scale={W}:{H}','-f','rawvideo','-pix_fmt','bgr24','-'],capture_output=True)
        fr=np.frombuffer(r.stdout,np.uint8).reshape(H,W,3)
        cx=a+(b-a)*bez(u); x0=int(min(max(cx*W-CW/2,0),W-CW))
        im=Image.fromarray(cv2.cvtColor(fr[:,x0:x0+CW],cv2.COLOR_BGR2RGB)).resize((TW,TH))
        row.paste(im,(i*(TW+4),0))
    d=ImageDraw.Draw(row); d.text((3,TH+2),f"c{c} {s} entrada {ent} camera {a}->{b}",fill=(255,230,0),font=f); d.text((3,TH+20),nota,fill='white',font=f)
    rows.append(row)
rw,rh=rows[0].size
sh=Image.new('RGB',(2*(rw+10),((len(rows)+1)//2)*(rh+6)),(20,20,20))
for j,r in enumerate(rows): sh.paste(r,((j%2)*(rw+10),(j//2)*(rh+6)))
sh.save(sys.argv[1],quality=85)
