from fractions import Fraction as F
from itertools import combinations
# Independently check the two economically relevant counterexamples.
masks=[(0,1),(1,2),(0,2)]
for a,b in combinations(masks,2):
    assert set(a).intersection(b)
assert not set.intersection(*(set(x) for x in masks))
assert F(1)-F(2,3)==F(1,3)
worlds=[(0,0),(0,1),(1,0),(1,1)]
def report_value(signal):
    cells={}
    for x,y in worlds:
        cells.setdefault(signal(x,y),[]).append((x,y))
    return sum(max(sum(int((x^y)==a) for x,y in cell) for a in [0,1]) for cell in cells.values())*F(1,4)
assert report_value(lambda x,y:0)==F(1,2)
assert report_value(lambda x,y:x)==F(1,2)
assert report_value(lambda x,y:y)==F(1,2)
assert report_value(lambda x,y:(x,y))==F(1)
print("exact Fraction checks passed: triple 1/3 regret and XOR 0,0,1/2 information gains")
