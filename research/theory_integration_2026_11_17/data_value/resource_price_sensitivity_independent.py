#!/usr/bin/env python3
"""Exact rational diagnostic for conditional outside-resource opportunity bounds.
Not measured robot or customer data."""
from fractions import Fraction as F
from itertools import product
import json

p=[F(1,2),F(1,4),F(1,4)]

def refinement(l1,l2,l3):
    d=[F(1,2)-l1,-F(1,4)-l2,l3]
    pos=sum((p[i]*max(d[i],0) for i in range(3)),F(0))
    neg=sum((-p[i]*min(d[i],0) for i in range(3)),F(0))
    return min(pos,neg)

def analytic(e):
    return (min(F(1,16),max(F(0),F(1,8)-e/F(2))),
            min(F(3,16),F(5,32)+e/F(2)))

rows=[]
allchecks=0
for k in range(9):
    e=F(k,32)
    vals=[]
    grid=[F(j,32) for j in range(17)]
    for a,b,c in product(grid, repeat=3):
        if max(a,b,c)-min(a,b,c) <= 2*e:
            vals.append(refinement(a,b,c))
    lo,hi=analytic(e)
    assert min(vals)==lo,(e,min(vals),lo)
    assert max(vals)==hi,(e,max(vals),hi)
    rows.append({'epsilon':str(e),'min':str(lo),'max':str(hi),'feasible_grid_laws':len(vals)})
    allchecks+=len(vals)
# Stable-basis fails if objective net customer contribution is report-dependent.
# With one variable x in [0,1], and objective c_y*x for c_y>0,
# optimal x=1 in all worlds but capacity shadow price is c_y.
assert F(1,2) != F(1,4)
# Basis switching despite identical objective (slot x+z<=1, x<=d, rewards x + 0.7z).
# If d=.2, optimal (x,z)=(.2,.8) and slot shadow .7; if d=1.2, (1,0) and shadow 1.
assert F(1,5)+F(7,10)*F(4,5)==F(19,25)
assert F(1,1)>F(19,25)
print(json.dumps({'case':'shared-outside-opportunity approximate invariance',
                  'assumptions':'lambda_y in [0,1/2], max pairwise spread <=2epsilon; unchanged original signed A/B rewards, predecision report probabilities, fixed learner and legally permitted network menu',
                  'exact_grid_laws_evaluated':allchecks,'rows':rows,
                  'status':'exact enumeration corroborates analytic constructive endpoints; synthetic only'},indent=2))
