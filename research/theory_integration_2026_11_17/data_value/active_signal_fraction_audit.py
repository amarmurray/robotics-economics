"""Independent rational policy-enumeration audit of synthetic active-signal example.
No field calibration. Enumerates four lawful report-contingent actions rather than
using the positive-part sufficient-moment expression in the JavaScript model.
"""
from fractions import Fraction as F
from itertools import product

def atoms(kind, world, perfect):
    out = []
    for z in (0, 1):
        qs = (0, 1) if kind == "P" else (1,)
        for q in qs:
            for y in ((z,) if perfect else (0, 1)):
                p = F(1, 2) * (F(1, 2) if kind == "P" else 1) * (1 if perfect else F(1, 2))
                free = z if kind == "P" or world == "I" else 1-z
                out.append((p, q, y, z, free))
    return out

def optimized(kind, world, perfect):
    a = atoms(kind, world, perfect)
    vals=[]
    for policy in product((0,1), repeat=2):
        # A certified target T is reserved only if q=1 and policy[y] chooses T.
        v=sum(p*(4*b*f if q and policy[y] else 2) for p,q,y,b,f in a)
        vals.append(v)
    return max(vals)

def check():
    vals={(k,w,p):optimized(k,w,p) for k,w,p in product(("P","D"),("I","II"),(False,True))}
    assert vals["P","I",False]==F(2)
    assert vals["P","I",True]==F(5,2)
    assert vals["D","I",False]==F(2)
    assert vals["D","I",True]==F(3)
    assert vals["D","II",False]==F(2)
    assert vals["D","II",True]==F(2)
    assert vals["P","I",False]+F(1,2)==F(5,2)
    assert vals["D","I",True]-F(1,4)==F(11,4)
    assert vals["D","II",True]-F(1,4)==F(7,4)
    assert vals["D","I",True]-vals["D","I",False]-vals["P","I",True]+vals["P","I",False]==F(1,2)
    assert vals["D","II",True]-vals["D","II",False]-vals["P","I",True]+vals["P","I",False]==-F(1,2)
    return vals

if __name__=="__main__":
    result=check()
    for key,value in sorted(result.items()): print(key, str(value))
    print("PASS: independent exact rational policy enumeration, 8 combinations")
