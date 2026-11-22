#!/usr/bin/env python3
"""Independent exact conditional production checker; synthetic only."""
from fractions import Fraction as F
from itertools import combinations
from math import comb

S = ("00", "10", "01", "11")
def compositions(k, n):
    if k == 1:
        yield (n,)
        return
    for first in range(n + 1):
        for rest in compositions(k - 1, n - first):
            yield (first,) + rest

checks = cases = 0
for masses in compositions(8, 4):
    table = {(s, h): F(masses[2*i+h], 4) for i, s in enumerate(S) for h in (0, 1)}
    h = sum(table[s, 1] for s in S)
    free_singleton = sum(table[s, 0] for s in ("10", "01"))
    direct = sum(table[s, k] * (F(9,2) if k else (F(25,4) if s in ("10", "01") else F(5))) for s in S for k in (0, 1))
    analytic = F(5) - F(1,2)*h + F(5,4)*free_singleton
    assert direct == analytic
    checks += 1
    b = F(7,4) + direct
    r = F(7)
    j = (F(6) + max(r,b)) / 2
    derived = F(13,2) + F(1,2)*max(F(0), -F(1,4)-F(1,2)*h+F(5,4)*free_singleton)
    assert j == derived and j >= F(13,2)
    checks += 2
    singleton = sum(table[s,k] for s in ("10","01") for k in (0,1))
    assert max(F(0), singleton-h) <= free_singleton <= min(singleton, 1-h)
    checks += 1
    cases += 1
assert cases == comb(4+8-1,8-1)
checks += 1
out = {}
for label,busy in (("diversified", ("00","11")),("synchronized",("10","01"))):
    table = {(s,h): F(1,4) if (h == int(s in busy)) else F(0) for s in S for h in (0,1)}
    h = sum(table[s,1] for s in S)
    p = sum(table[s,0] for s in ("10","01"))
    expected_b = F(7,4) + sum(table[s,k]*(F(9,2) if k else (F(25,4) if s in ("10","01") else F(5))) for s in S for k in (0,1))
    j = (F(6)+max(F(7),expected_b))/2
    out[label] = (str(h),str(p),str(expected_b),str(j))
assert out["diversified"] == ("1/2","1/2","57/8","105/16")
assert out["synchronized"] == ("1/2","0","13/2","13/2")
assert F(13,2) < F(209,32) < F(105,16)
checks += 3
print({"compositions":cases,"checks":checks,"worlds":out,"embodiment":"209/32"})
