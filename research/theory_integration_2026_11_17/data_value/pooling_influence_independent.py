"""Independent exact arithmetic audit of synthetic pooled-transfer certificate."""
from fractions import Fraction as F
from itertools import product

def mobius_three(values):
    return sum((-1) ** (3 - mask.bit_count()) * values[mask] for mask in range(8))

def order_two_contrast(values):
    return values[3]+values[5]+values[6]-values[1]-values[2]-values[4]+values[0]

base_s=[F(550+120*m.bit_count(),1000) for m in range(8)]
base_e=[F(150+120*m.bit_count(),1000) for m in range(8)]
sg=[x+F(1,100)*(-1)**(3-m.bit_count()) for m,x in enumerate(base_s)]
e=[x-F(1,100)*(-1)**(3-m.bit_count()) for m,x in enumerate(base_e)]
D=[x-y for x,y in zip(sg,e)]
assert order_two_contrast(D)==F(13,50)
assert D[7]==F(21,50)
assert mobius_three(sg)-mobius_three(e)==F(4,25)
assert D[7]-order_two_contrast(D)==F(4,25)
assert order_two_contrast(D)-F(4,25)==F(1,10)>0
assert all(v[b]>=v[a] for v in [sg,e] for a,b in product(range(8),repeat=2) if a & b == a)
S2=base_s.copy();E2=base_e.copy();S2[7]+=F(1,100);E2[7]-=F(1,100)
D2=[x-y for x,y in zip(S2,E2)]
assert D2[7]==F(21,50)
assert order_two_contrast(D2)==F(2,5)
assert D2[7]-order_two_contrast(D2)==F(1,50)
assert 1-(1-F(1,100))*(1-F(1,50))==F(149,5000)
local=[F(300+100*m.bit_count(),1000) for m in range(8)]
triple=local.copy();triple[7]+=F(1,10)
assert all(triple[m]==local[m] for m in range(7))
assert mobius_three(triple)-mobius_three(local)==F(1,10)
assert all(triple[b]>=triple[a] for a,b in product(range(8),repeat=2) if a&b==a)
checks=0
for bs,be in product(range(0,21,5),repeat=2):
    for sgSigns in product((-1,1),repeat=8):
        s=[base_s[m]+F(bs*sgSigns[m],1000) for m in range(8)]
        t=[base_e[m]-F(be*((-1)**(3-m.bit_count())),1000) for m in range(8)]
        if not all(0<=x<=1 for x in s+t): continue
        difference=[x-y for x,y in zip(s,t)]
        assert abs(difference[7]-order_two_contrast(difference))<=F(8*(bs+be),1000)
        checks+=1
print({"independent_exact_checks":checks+14,"general_lower_bound":"1/10","generic_tail":"4/25","activation_tail":"1/50","two_step_mismatch":"149/5000","triple_only_falsifier":"1/10"})
