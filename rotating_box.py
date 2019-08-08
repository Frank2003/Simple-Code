from Tkinter import *
from math import sin,cos
from time import sleep
w,h=300,300
groups=[[0,2,6,4],[4,6,7,5],[5,7,3,1],[1,3,2,0]]
cord=[[-100,-100,-100],[-100,-100,100],[-100,100,-100],[-100,100,100],\
      [100,-100,-100],[100,-100,100],[100,100,-100],[100,100,100]]
colours=["red","green","blue","yellow"]
t=Tk()
ca=Canvas(t,width=w,height=h)
ca.pack()
def plus(cord):
  result=[]
  for i in cord:
    result.append([i[0]+w/2,i[1]+w/2])
  return result

def light(cord,zplane,dotcord):
  result=[]
  [xdot,ydot,zdot]=dotcord
  for [x,y,z] in cord:
    result.append([(zdot-zplane)/(zdot-z)*(xdot-x)+xdot,\
                   (zdot-zplane)/(zdot-z)*(ydot-y)+ydot,zplane])
  return result

def group(cord):
  result=[]
  for i in groups:
    temp=[]
    for j in i:
      temp.append(cord[j])
    result.append(temp)
  return result

def rotate(deg,cord,axis):
  newcord=[]
  if axis=="x":
    for [x,y,z] in cord:
      y,z=y*cos(deg)-z*sin(deg),y*sin(deg)+z*cos(deg)
      newcord.append([x,y,z])
  if axis=="y":
    for [x,y,z] in cord:
      x,z=x*cos(deg)-z*sin(deg),x*sin(deg)+z*cos(deg)
      newcord.append([x,y,z])
  if axis=="z":
    for [x,y,z] in cord:
      x,y=x*cos(deg)-y*sin(deg),x*sin(deg)+y*cos(deg)
      newcord.append([x,y,z])
  return newcord

while 1:
  #print cord
  '''
  id=[0,0,0,0]
  display=group(plus(cord))
  for i in range(4):
    id[i]=ca.create_polygon(display[i],fill="",outline="black")
  cord=rotate(0.01,cord,"x")
  cord=rotate(0.02,cord,"y")
  cord=rotate(0.03,cord,"z")
  t.update()
  #t.update_idletasks()
  #sleep(0.5)
  for i in id:
    ca.delete(i)
  '''
  id=[0,0,0,0]
  display=group(plus(light(cord,-100,(0,0,-500))))
  cord=rotate(0.01,cord,"z")
  cord=rotate(0.01,cord,"x")
  cord=rotate(0.02,cord,"y")
  for i in range(4):
    id[i]=ca.create_polygon(display[i],fill="",outline="black")
  t.update()
  for i in id:
    ca.delete(i)
  #'''
