#!/usr/bin/env python3
"""Independent exact Fraction audit of synthetic source-mixture production interaction."""
from fractions import Fraction as Q
from itertools import product

BASE = {0:Q(20,10),1:Q(21,10),2:Q(21,10),3:Q(25,10),
        4:Q(21,10),5:Q(25,10),6:Q(25,10)}

def world(full):
    return {**BASE, 7:Q(full,10)}

def mobius(v, t):
    return sum((-1)**(t.bit_count()-s.bit_count())*v[s]
               for s in range(8) if s&t==s)

def monotone(v):
    return all(v[s]<=v[t] for s in range(8) for t in range(8) if s&t==s)

checks = 0
for s,e in product(range(25,36), repeat=2):
    a,b=world(s),world(e)
    assert monotone(a) and monotone(b)
    assert mobius(a,7) == Q(s-32,10)
    assert mobius(a,7)-mobius(b,7) == Q(s-e,10)
    checks += 3
assert world(35)[7]-world(27)[7] == Q(8,10)
assert mobius({s:Q(8) if s==7 else Q(0) for s in range(8)},7)==8
assert mobius({s:Q(min(2,s.bit_count())) for s in range(8)},7)==-1
p=[Q(3,6),Q(2,6),Q(1,6)]
q=[Q(2,6)]*3
d=[Q(3),Q(0),Q(-3)]
assert sum(x*y for x,y in zip(p,d))==1
assert sum(x*y for x,y in zip(q,d))==0
print({"passed": True, "independent_fraction_assertions":checks+5,"worlds":121})
