"""Exact-fraction analytical replication of Q5 hypothetical thresholds; not empirical calibration."""
from fractions import Fraction as Q
def profit(a,b,c,outside,rho,cap):
    q=min(cap,max(Q(0),(a-c)/b))
    return rho*max(Q(0),(a-c)*q-b*q*q/2-outside)
def threshold(x,k=Q(1),ls=Q(2)):
    return Q(3)+Q(2)*(1+2)/2+(9-k*ls*x-(6-k*x)+2)/(Q(4,5))
def paths(k):
    A=profit(Q(10),Q(2),Q(3),Q(4),Q(4,5),Q(2))
    B=profit(Q(22),Q(2),Q(3),Q(3),Q(4,5),Q(2))
    cash=Q(18)-12+A
    entry=13-4*k
    direct=B-13
    seeded=2*A+B-12-entry
    return direct,seeded,cash>=entry
def check():
    assert threshold(0)==Q(49,4)
    assert threshold(2)==Q(39,4)
    assert threshold(2,Q(0))==Q(49,4)
    assert threshold(2,Q(1),Q(1,2))==Q(27,2)
    assert profit(Q(10),Q(2),Q(3),Q(4),Q(4,5),Q(2))==Q(24,5)
    assert profit(Q(22),Q(2),Q(3),Q(3),Q(4,5),Q(2))==Q(124,5)
    assert paths(Q(0))==(Q(59,5),Q(47,5),False)
    assert paths(Q(1))==(Q(59,5),Q(67,5),True)
    assert paths(Q(3,5))==(Q(59,5),Q(59,5),True)
    assert paths(Q(11,20))[2]
    assert not paths(Q(1,2))[2]
    print("11 exact-fraction checks passed; private threshold 3/5, financing threshold 11/20")
if __name__=="__main__":check()
