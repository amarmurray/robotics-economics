"""Independent exact-rational audit of synthetic queue-duration and buyer-path transfer."""
from fractions import Fraction as F
from itertools import permutations
from collections import Counter
paths=((0,0),(1,0),(0,1),(1,1))
def cost(d,u): return (u[0] if d<=1 else 0)+(u[1] if d<=2 else 0)
results=[]
checks=0
for i,j in permutations(range(4),2):
    durations=tuple(1 if k==i else (2 if k==j else 3) for k in range(4))
    assert Counter(durations)=={1:1,2:1,3:2};checks+=1
    assert all(int(d<=1)<=int(d<=2) for d in durations);checks+=1
    q=sum(F(cost(d,u),4) for d,u in zip(durations,paths))
    P=max(F(6),F(6)-F(1,4)+q)
    results.append((q,P))
    assert F(6)<=P<=F(13,2);checks+=1
assert len(results)==12;checks+=1
assert min(x for x,_ in results)==0;checks+=1
assert max(x for x,_ in results)==F(3,4);checks+=1
assert min(y for _,y in results)==6;checks+=1
assert max(y for _,y in results)==F(13,2);checks+=1
G=F(6)+F(1)-F(7,10)
E=F(6)+F(1)-F(13,20)
assert G==F(63,10) and E==F(127,20);checks+=1
assert F(13,2)>E>G>F(6);checks+=1
for short_on in (0,1):
    orders=((1,0),(0,1))
    q=sum(F(cost(1 if k==short_on else 3,u),2) for k,u in enumerate(orders))
    assert q==F(1,2);checks+=1
print({"audit":"independent Fraction","assignment_cases":len(results),"checks":checks,
       "gain_range":tuple(map(str,(min(x for x,_ in results),max(x for x,_ in results)))),
       "P_range":tuple(map(str,(min(y for _,y in results),max(y for _,y in results)))),
       "G":str(G),"E":str(E),"conserved_gain":"1/2"})
