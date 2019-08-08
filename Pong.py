from Tkinter import *
from time import *
from random import *

def ranum():
 chr="0123456789abcdef"
 r="#"
 for i in range(0,6):
  r=r+chr[randint(0,15)]
 return r

def move(event):
 global vx
 pvx=vx
 if event.keysym=="Right":
  vx+=3
 if event.keysym=="Left":
  vx-=3
 #if (vx-pvx)/3 == pvx**0:
 # vx=vx-pvx

def game():
 global sid,ca,ax,ay,vx,score,px
 ca.delete(sid)
 score=0
 sid=ca.create_text(250,50,text="Score",font=("Helvetica",30))
 t.update()
 count()
 ca.move(id,-ax,-ay)
 ca.move(pid,250-px,0)
 score=0
 x=3.5
 y=3.5
 px=250
 vx=0
 ax=0
 ay=0
 while 1:
  sleep(0.01)
  ca.move(id,x,y)
  ca.bind_all("<KeyPress-Left>",move)
  ca.bind_all("<KeyPress-Right>",move)
  ax+=x
  ay+=y
  x*=1.001
  y*=1.001
  ca.move(pid,vx,0)
  px+=vx
  vx*=0.98
  if ax>=480 or ax<=0:
   x=-x
   ca.itemconfig(id,fill=ranum())
  if ay<=0:
   y=-y
   ca.itemconfig(id,fill=ranum())
  if ay>=480:
   break
  if px>=500:
   ca.move(pid,500-px,0)
   px=500
   vx=0
  if px<=0:
   ca.move(pid,0-px,0)
   px=0
   vx=0
  if 395>=ay>=375 and px-60<=ax+10<=px+60 and y>0:
   y=-y
   x+=vx/2.0
   score+=1
   ca.itemconfig(pid,fill=ranum())
   ca.itemconfig(id,fill=ranum())
   ca.itemconfig(sid,text=str(score))
  t.update()

def count():
 ssid=ca.create_text(250,250,text=str(0),font=("Helvetica",90))
 for i in range(3,0,-1):
  ca.itemconfig(ssid,text=str(i))
  t.update()
  sleep(1)
 ca.delete(ssid)

t=Tk()
t.title("PONGGG!!!!")
b=Button(t,text="Start",command=game)
b.pack()
t.update()
ca=Canvas(t,width=500,height=500)
ca.pack()
score=0
vx=0
ax,ay=0,0
px=250

id=ca.create_oval(0,0,20,20,fill="#0000ff",outline="#000000")
pid=ca.create_rectangle(200,395,300,405,fill="#00ff00",outline="#000000")
sid=ca.create_text(250,50,text="Score",font=("Helvetica",30))
t.mainloop()
