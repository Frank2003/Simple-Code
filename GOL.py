#GAME OF LIFE
import time,random
'''
b=["00000",\
   "00100",\
   "00010",\
   "01110",\
   "00000"]
'''
show=["#","."]
live=[2,3]
born=[3,6]
neigh=[[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]
xmax=55
ymax=180
b=[]
for i in range(xmax):
    s=""
    for j in range(ymax):
        s=s+str(random.randint(0,1))
    b.append(s)
wait=0
'''
def g(x,y):
    l=len(b[0])
    b_=["0"*(l+2)]
    for i in b:
        b_.append("0"+i+"0")
    b_.append("0"*(l+2))
    return sum([b_[x][y],b_[x+1][y],b_[x+2][y],b_[x][y+1],b_[x+2][y+1],b_[x][y+2],b_[x+1][y+2],b_[x+2][y+2]])
'''
def g(x,y):
    s=0
    for i in neigh:
        s+=int(b[(x+i[0])%xmax][(y+i[1])%ymax])
    return s

def p(b):
    for l in b:
        s=""
        for i in l:
            s=s+show[int(i)]
        print s

while 1:
    p(b)
    if b == ["0"*ymax]*xmax:
        break
    n=b[:]
    for i in range(xmax):
        for j in range(ymax):
            a=g(i,j)
            if b[i][j]=="1" and a in live:
                continue
            elif b[i][j]=="1":
                n[i]=n[i][:j]+"0"+n[i][j+1:]
            if b[i][j]=="0" and a in born:
                n[i]=n[i][:j]+"1"+n[i][j+1:]
    b=n[:]
    time.sleep(wait)
    print
