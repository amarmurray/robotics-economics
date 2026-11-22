# Independent exact arithmetic; run: python endogenous_acquisition_fraction_independent.py
from fractions import Fraction as F
def payoff(theta, action):
    if action == "R": return F(1,2)
    if action == "E": return F(7,8)
    return F(int(theta == action))
def W(alpha, menu, usable=True):
    return sum(max(sum(F(1,2)*((alpha if sig == theta else 1-alpha) if usable else 1)*payoff(theta, act) for theta in ("A","B")) for act in menu)
               for sig in (("A","B") if usable else ("missing",)))
p=F(1,4)+W(F(3,4),("R","A","B"))
d=-F(1,8)+W(F(1),("R","A","B"))
e=-F(1,16)+W(F(1,2),("R","E"),False)
assert (p,d,e)==(F(1),F(7,8),F(13,16))
assert W(F(1),("R","A"))-F(1,8)==F(5,8)
assert W(F(1),("R","A","B"),False)==F(1,2)
for k in range(9):
    r=F(k,16)
    assert (r+W(F(3,4),("R","A","B"))>=d)==(r>=F(1,8))
for a in range(4,9):
    for b in range(a,9):
        for menu in (("R",),("R","A"),("R","A","B")):
            assert W(F(b,8),menu)>=W(F(a,8),menu)
assert W(F(3,4),("R","A","B"))-W(F(1,2),("R","A","B"))-W(F(3,4),("R",))+W(F(1,2),("R",))==F(1,4)
print("Independent Fraction checks passed: P=1 D=7/8 E=13/16; transfer-menu interaction=1/4")
