import random

def rand(l):
    r=""
    for i in range(l):
        r=r+chr(random.randint(33,127))
    return r

def char(a):
    c=""
    while a:
        c=c+chr(a%96+32)
        a/=96
    return c

def plus(a,b):
    c=0
    t=0
    while t<len(a):
        c+=(ord(a[t])+ord(b[t%len(b)])-64)%96*(96**t)
        t+=1
    return c

def minus(a,b):
    c=0
    t=0
    while t<len(a):
        c+=(ord(a[t])-ord(b[t%len(b)]))%96*(96**t)
        t+=1
    return c

a="Hello!"
key=rand(len(a))
b=char(plus(a,key))
print key,b
