"""Independent exact-Fraction check of the Nov21 synthetic source/grounding/embodiment example."""
from fractions import Fraction as Q
from itertools import product
P = [Q(2,5), Q(1,2), Q(1,2), Q(3,5)]
LO = [max(Q(0), 2*p-1) for p in P]
HI = P
mins, maxs, n = None, None, 0
for q0,q1,q2,q3 in product(*(range(int(20*l),int(20*h)+1) for l,h in zip(LO,HI))):
    x=Q(q3-q1-q2+q0,20)
    mins=x if mins is None else min(mins,x)
    maxs=x if maxs is None else max(maxs,x)
    n+=1
assert n==9801 and mins==Q(-4,5) and maxs==Q(1)

def vals(q11):
    q=[Q(1,5),Q(1,4),Q(1,4),q11]
    gross=[4*p+8*qq for p,qq in zip(P,q)]
    c=[Q(0),Q(1,2),Q(1,2),Q(1)]
    choices={str(i):gross[i]-c[i] for i in range(4)}
    choices.update({f'E{i}':max(gross[i],Q(5))-c[i]-1 for i in range(4)})
    return gross,choices
for q11,winner,gross11,delta in [
    (Q(1,2),'3',Q(32,5),Q(8,5)),
    (Q(1,5),'E0',Q(4),Q(-4,5))]:
    gross, choices=vals(q11)
    assert gross[3]==gross11
    assert gross[3]-gross[1]-gross[2]+gross[0]==delta
    assert max(choices,key=choices.get)==winner
    print(q11, 'best:',winner,'net:',choices[winner])
for q11ticks in range(4,13):
    _,choices=vals(Q(q11ticks,20))
    winner=max(choices,key=choices.get)
    assert winner==('3' if q11ticks>=7 else 'E0'),(q11ticks,winner)
assert Q(13,40) == (Q(4)+Q(1)-Q(12,5))/8
print('independent Fraction checks passed:', n, 'Fréchet grids; cross interval',mins,maxs,'; threshold 13/40')

