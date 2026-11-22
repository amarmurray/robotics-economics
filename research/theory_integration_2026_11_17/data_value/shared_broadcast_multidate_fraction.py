"""Independent rational audit: joint 32-state, date-1 adaptive B/R, date-2 one-worker dispatch."""
from fractions import Fraction as F
from itertools import combinations_with_replacement

def value(weights):
    n=sum(weights)
    direct=[]
    for mask in range(4):
        t=F(0)
        for i,k in enumerate(weights):
            L=(i>>4)&1;W=(i>>3)&1;S1=(i>>2)&1;S2=(i>>1)&1;free=i&1
            pilot=L and ((mask>>W)&1)
            t+=k*((F(3,4) if pilot else F(2))+(F(4) if pilot and free and (S1 or S2) else F(2)))
        direct.append(t/n)
    m=[0,0];p=[0,0]
    for i,k in enumerate(weights):
        L=(i>>4)&1;W=(i>>3)&1;S1=(i>>2)&1;S2=(i>>1)&1;free=i&1
        if L:
            m[W]+=k
            if free and (S1 or S2):p[W]+=k
    formula=F(4)+sum((max(F(0),2*p[w]-F(5,4)*m[w]) for w in range(2)),F(0))/n
    return max(direct),formula

cases=0
for i in range(32):
    w=[0]*32;w[i]=1
    assert value(w)[0]==value(w)[1];cases+=1
for i,j in combinations_with_replacement(range(32),2):
    w=[0]*32;w[i]+=1;w[j]+=1
    assert value(w)[0]==value(w)[1];cases+=1

def make(kind):
    w=[0]*32;w[1]=64
    pairs={(1,1):2,(1,0):1,(0,1):1} if kind=="diversified" else {(1,1):3,(0,0):1}
    for (a,b),n in pairs.items():
        for free,freq in [(0,1),(1,3)]:
            w[16+4*a+2*b+free]+=4*n*freq
    assert sum(w)==128
    return w

div=value(make("diversified"));sync=value(make("synchronized"));E=F(65,16)
assert div==(F(33,8),F(33,8)) and sync==(F(4),F(4))
assert sync[0]<E<div[0]
print({"independent_fraction_cases":cases,"diversified":str(div[0]),"synchronized":str(sync[0]),"embodiment":str(E)})
