import random

def gcm(a,b):
    assert a>0,b>0
    while b>0:
        a,b=b,a%b
    return a

def lcm(a,b):
    assert a>0,b>0
    return a*b/gcm(a,b)

def isprime(n):
    if n<=1:
        return False
    if n==2:
        return True
    elif n%2==0:
      return False
    else:
        for i in range(3,int((n**0.5)+3),2):
            if n%i==0:
                return False
    return True

def isbigprime(n):
    for i in range(2,50):
        if pow(i,n-1,n) != 1:
            return False
    return True

def ranprime(lmin,lmax,t):
    r=random.randint(lmin,lmax)*2+1
    if isbigprime(r):
        return r
    else:
        return ranprime(lmin,lmax,t-1)

def ranp(a,b,c,d):
    r=random.randint(a,b)
    if gcm(r,d)==1:
        return r
    else:
        return ranp(a,b,c-1,d)

def gete(e1,ab):
    k=1
    while 1:
        if (ab*k+1)%e1==0:
            return (ab*k+1)/e1
        k+=1

def setup():
 a=ranprime(10000,100000,100)
 b=ranprime(10000,100000,100)
 l=(a-1)*(b-1)
 e1=ranp(10000,10000000,1000,l)
 e2=gete(e1,l)
 A=1234
 B=pow(A,e1,a*b)
 C=pow(B,e2,a*b)
 print e1,e2,a*b,B

while 1:
    setup()
