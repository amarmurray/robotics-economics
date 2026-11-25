import numpy as np
Q=np.arange(1,13)
G=np.array([1-(1-theta)**Q for theta in (.06,.12)])
M=Q*(16-Q)
B=.9
def solve(v):
    a=(M+v*G).max(axis=1)
    outside=max(76,v-20)
    d=0
    for _ in range(1000):
        t=np.maximum(a+B*np.array([.25,.95])*d,outside+B*np.array([0,.65])*d)
        u=t[1]-t[0]
        if abs(d-u)<1e-12: break
        d=u
    gap=a-outside+B*np.array([.25,.30])*d
    return gap,d,tuple('A' if x>0 else ('C' if v<96 else 'B') for x in gap)
prev=None
for v in range(401):
    gap,d,act=solve(v)
    if act!=prev or v in [15,25,100,140,160,190,200,250,320]:
        print(v,act,gap,d)
    prev=act
