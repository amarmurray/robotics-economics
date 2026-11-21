# Independent standard-library exact-rational verification for identification hierarchy.
# Run with python identification_hierarchy_independent.py
from fractions import Fraction as F
from itertools import product

common = [(u, u, u, u) for u in (0,1)]
parity = [(u,1-u,1-u,u) for u in (0,1)]
def E(law,fn): return sum((F(fn(r),len(law)) for r in law),F(0))
def interaction(r): return r[3]-r[1]-r[2]+r[0]
for law in (common,parity):
    assert all(E(law,lambda r,j=j: r[j]) == F(1,2) for j in range(4))
    assert E(law,interaction)==0
assert set(map(interaction,common))=={0}
assert set(map(interaction,parity))=={-2,2}
# Assignment-positivity identity checked for every potential four-arm binary pattern
for outcomes in product((0,1),repeat=4):
    for arm in range(4):
        lhs = sum(F((1 if assigned==arm else 0)*outcomes[arm],4)*4 for assigned in range(4))
        assert lhs == outcomes[arm]

joint = (((0,0),(1,1)),((0,1),(1,0)))
values=[]
for law in joint:
    pa,pb,h = E(law,lambda r:r[0]),E(law,lambda r:r[1]),E(law,lambda r:r[0]*r[1])
    assert (pa,pb)==(F(1,2),F(1,2))
    values.append((h,12*h-1,8*h-1))
assert values==[(F(1,2),F(5),F(3)),(F(0),F(-1),F(-1))]
assert values[0][1]>4>values[1][1]
assert values[0][2]>1>values[1][2]
assert max(F(0),F(1,2)+F(1,2)-1)==0
assert min(F(1,2),F(1,2))==F(1,2)
print('Independent Python Fraction verification passed: all 16 potential four-arm binary types, 64 assignment checks, two data/qualification joint worlds, exact value/rank reversals.')
