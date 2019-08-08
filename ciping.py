txt=open("bible.txt","r").read().lower()
wanted=[chr(a) for a in range(97,124)]+[" "]
c=""
d={}
l=[]
for i in txt:
    c=c+i if i in wanted else c
for i in c.split():
    d[i]=d.get(i,0)+1
for i in d:
    l.append((d[i],i))
l.sort(reverse=True)
print "The Top Hundred Common Words:"
for i in range(100):
    print "No.%d (%d times): %s "%((i+1,)+l[i])
