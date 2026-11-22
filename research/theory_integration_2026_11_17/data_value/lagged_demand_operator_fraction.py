"""Independent exact-rational audit of finite lagged paid-service constructions."""
from fractions import Fraction as F
from itertools import product

checks=0

def compositions(n,k):
    if k==1:
        yield (n,)
    else:
        for x in range(n+1):
            for suffix in compositions(n-x,k-1):
                yield (x,)+suffix

# Distinct representation from main JavaScript: direct set operations on 8 event cells.
strata={}
for p in compositions(6,8):
    q=sum(p[i] for i in range(8) if (i//4)%2)
    a=sum(p[i] for i in range(8) if (i//2)%2)
    b=sum(p[i] for i in range(8) if i%2)
    s=sum(p[i] for i in range(8) if (i//4)%2 and not (i//2)%2 and i%2)
    v=sum(p[i]*(4*((i//2)%2)+3*int(bool((i//4)%2 and i%2 and not (i//2)%2))) for i in range(8))
    assert v==4*a+3*s
    low=max(0,q+b-a-6); high=min(q,b,6-a)
    assert low<=s<=high
    key=(q,a,b)
    vals=strata.setdefault(key,[]); vals.append(s)
    checks+=2
for (q,a,b),v in strata.items():
    assert min(v)==max(0,q+b-a-6) and max(v)==min(q,b,6-a)
    checks+=1

# Recovery association: direct Fractions for date-2 received payments.
for j,expected_delta in [(F(0),F(1,8)),(F(5,32),-F(1,32)),(F(1,4),-F(1,8))]:
    q=F(5,8); h=F(1,4)
    table={"Q_and_H":j,"Q_only":q-j,"H_only":h-j,"neither":1-q-h+j}
    assert all(x>=0 for x in table.values()) and sum(table.values())==1
    future=table['neither']+table['Q_only']*2
    delta=F(3,4)+future-(F(1)+F(1))
    assert delta==expected_delta
    checks+=2

p0=sum((F(s,4)-F(1,8))/2 for s in range(2))
assert p0==0
p_stag=p0+sum(F(1,2)*max(1-s,s) for s in range(2))
p_sync=p0+sum(F(1,2)*(s) for s in range(2))
d=sum(F(1,8)*((1 if a else int(q and b))) for q,a,b in product(range(2),repeat=3))-F(1,16)
e=F(1,2)+F(1,2)-F(3,8)
assert (p_stag,p_sync,d,e)==(F(1),F(1,2),F(9,16),F(5,8))
checks+=2
print({'independent_fraction_assertions':checks,'three_way_marginal_strata':len(strata), 'synthetic_values':[str(x) for x in (p_stag,p_sync,d,e)], 'dispatch_deltas':['1/8','-1/32','-1/8']})
