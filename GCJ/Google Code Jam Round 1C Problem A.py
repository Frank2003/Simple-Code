#!/usr/bin/python
from math import pi
import sys
fp = file(sys.argv[1])
for case in range(int(fp.next())):
    (N,K) = fp.next().split()
    N,K=int(N),int(K)
    pancakes=[]
    for i in range(N):
        (radii,height)=fp.next().split()
        pancakes.append([int(radii),int(height)])
    pancakes.sort(reverse=True)
    pancakes_height=[2*i[1]*i[0]*pi for i in pancakes]
    res=0
    for i in range(len(pancakes)-K+1):
        radii=pancakes[i][0]
        height=sum(sorted(pancakes_height[i+1:])[::-1][0:K-1]+[pancakes_height[i]])
        res=max(res,(radii**2)*pi+height)
    print "Case #%d: %.9f" % (case+1, res)
fp.close()
