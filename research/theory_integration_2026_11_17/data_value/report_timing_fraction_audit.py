"""Independent Fraction audit of lawful report timing under one network factor.
Synthetic original-buyer normalized net contributions only; no robot evidence.
Run with: python report_timing_fraction_audit.py
"""
from fractions import Fraction as F
from json import dumps
P=((F(2),F(4)),(F(3,2),F(5)))
E=((F(19,10),F(39,10)),(F(11,5),F(9,2)))
def values(p,q):
    w=lambda z,y:(p if z else 1-p)*(q if z==y else 1-q)
    stage=lambda row,y:sum(w(z,y)*row[z] for z in (0,1))
    pre=sum(max(stage(row,y) for row in P+E) for y in (0,1))
    post=max(sum(max(stage(row,y) for row in arm) for y in (0,1)) for arm in (P,E))
    none=max(max((1-p)*row[0]+p*row[1] for row in arm) for arm in (P,E))
    return pre,post,none
checked=0
for d in range(1,17):
    for n in range(d+1):
        for m in range(2,13):
            for k in range((m+1)//2,m+1):
                pre,post,none=values(F(n,d),F(k,m))
                assert pre>=post>=none
                checked+=1
assert values(F(1,2),F(3,4))==(F(69,20),F(67,20),F(67,20))
assert values(F(1,4),F(3,4))==(F(111,40),)*3
assert values(F(1,2),F(7,12))==(F(67,20),)*3
assert values(F(1,2),F(1))==(F(18,5),F(7,2),F(67,20))
for m in range(2,49):
    for k in range((m+1)//2,m+1):
        q=F(k,m)
        pre,post,none=values(F(1,2),q)
        assert pre==max(F(67,20),F(3)+F(3,5)*q)
        assert post==max(F(67,20),F(11,4)+F(3,4)*q)
print(dumps({"independent_fraction_configurations":checked,
  "early":str(values(F(1,2),F(3,4))[0]),
  "no":str(values(F(1,2),F(3,4))[2]),
  "robust_lower_factor":str(values(F(1,4),F(3,4))[0])},indent=2))
