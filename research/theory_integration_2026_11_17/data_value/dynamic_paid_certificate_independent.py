"""Independent exact-rational spot checks for dynamic_paid_certificate.js.
No external robot/customer measurements, access or claims of novelty.
Run: python dynamic_paid_certificate_independent.py
"""
from fractions import Fraction as F
from itertools import product

def value(p, q, r, c, d, rights=True):
    return p * (1 + (max(F(0), q-c) if rights else 0)) + (1-p) * max(F(0),r-d)

p, q, r = F(2,5), F(4,5), F(1,2)
c, d, e = F(3,20), F(1,20), F(19,20)
assert value(p,q,r,c,d) == F(93,100)
assert value(p,q,r,c,d,False) == F(67,100)
assert value(p,F(9,10),r,c,d) == F(97,100)
assert value(p,F(17,20),r,c,d) == e
policy_values = [p*(1+(q-c if learn else 0))+(1-p)*((r-d) if rescue else 0)
                 for learn,rescue in product([False,True], repeat=2)]
assert max(policy_values) == value(p,q,r,c,d)
p0,p1 = F(8,20),F(12,20)
q0,q1 = F(10,20),F(16,20)
cross = value(p1,q1,r,c,d)-value(p1,q0,r,c,d)-value(p0,q1,r,c,d)+value(p0,q0,r,c,d)
assert cross == (p1-p0)*(q1-q0) == F(3,50)
s = lambda a: value(p0,a,r,F(0),d)
sub = s(F(16,20))-s(F(16,20))-s(F(16,20))+s(F(0))
assert sub == -F(8,25)
assert max(value(F(1,2),0,0,0,0),value(0,1,0,0,0)) == F(1,2)
assert value(F(1,2),1,0,0,0) == 1
print("PASS: 9 independent exact rational identities (no field data)")
