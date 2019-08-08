import random

score=0
c=['\x1b[A', '\x1b[B', '\x1b[D', '\x1b[C']
com=["\x1b[A","\x1b[B","\x1b[C","\x1b[D"]
co="^[[A^[[B^[[C^[[D"
#c=[0,0,0,0]
q=["up:","down:","right:","left:"]
b1=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
b2=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

def out():
 print "SCORE:",score
 print ("+"+"-"*7)*4+"+"
 for i in range(4):
  for j in range(4):
   print "| ",
   if b1[i][j]!=0:
    print b1[i][j],
   print "\t",
  print "|"+"\n"+("+"+"-"*7)*4+"+"

def copy(l):
  for i in range(0,4):
   for j in range(0,4):
    if l==1:
     b2[i][j]=b1[j][i]
    if l==2:
     b1[i][j]=b2[j][i]

def move(k,d,n):
 c=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
 global score,b1,b2
 if d==0:
  for i in range(0,4):
   l=[0,0,0,0]
   a=k
   for j in range((3-3*n)/2,(3+5*n)/2,n):
    if 0<=a-n<=3:
     if b2[i][j]==l[a-n]:
      l[a-n]=b2[i][j]*2
      score+=l[a-n]
      continue
    if b2[i][j]!=0:
     l[a]=b2[i][j]
     a+=n
   c[i]=l
  if b2[:]==c[:]:
   return True
  b2=c[:]
  copy(2)

 elif d==1:
  for i in range(0,4):
   l=[0,0,0,0]
   a=k
   for j in range((3-3*n)/2,(3+5*n)/2,n):
    if 0<=a-n<=3:
     if b1[i][j]==l[a-n]:
      l[a-n]=b1[i][j]*2
      score+=l[a-n]
      continue
    if b1[i][j]!=0:
     l[a]=b1[i][j]
     a+=n
   c[i]=l
  if b1[:]==c[:]:
   return True
  b1=c[:]
  copy(1)

def rand():
 b=[]
 for i in range(4):
  for j in range(4):
   if b1[i][j]==0:
    b.append([i,j])
 if b==[]:
  return True
 r=random.randint(0,len(b)-1)
 b1[b[r][0]][b[r][1]]=(random.randint(1,4)/4+1)*2
 copy(1)
 return False

def main():
 rand()
 while 1:
  flag=rand()
  out()
  if flag:
   print "YOU LOSE"
   break
  flag=True
  while flag:
   while 1:
    d=raw_input("Input:")
    if d in c:
     break
    elif d=="\x1b":
     break
    print "INVALID INPUT"
   if d=="\x1b":
    break
   d=c.index(d)
   flag=move((d)%2*3,d/2,(d+1)%2*2-1)
  if d=="\x1b":
   print "EXIT"
   break

main()
