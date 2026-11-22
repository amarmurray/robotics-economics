from fractions import Fraction as F

# Independent exact enumeration of common complete potential histories.
# Conditional G even-parity and odd-parity masses vary without changing pairs.
def calculate(t):
    law = []
    for q in range(2):
      for d in range(2):
       for f in range(2):
        gmass = F(1,4)-t if (q+d+f)%2 == 0 else t
        for x in range(2):
         for z in range(2):
          for jp in range(2):
           m = gmass/F(8)
           old = F(z)
           P = old if x == 0 else F(1,2)+F(1-jp)
           G = old if x == 0 else F(f)*(F(9,2) if q*d else old)
           law.append((m,old,P,G,q,d,f,z))
    assert sum(v[0] for v in law)==1
    old = sum(m*o for m,o,*_ in law)
    P = sum(m*p for m,o,p,*_ in law)
    G = sum(m*g for m,o,p,g,*_ in law)-F(1,16)
    assert (old,P,G)==(F(1,2),F(3,4),F(5,16)+2*t)
    for bit in range(3):
        assert sum(v[0] for v in law if v[4+bit])==F(1,2)
    for a,b in ((0,1),(0,2),(1,2)):
        assert sum(v[0] for v in law if v[4+a] and v[4+b])==F(1,4)
    assert sum(v[0] for v in law if v[4] and v[5] and v[6])==t
    assert sum(v[0] for v in law if v[7])==F(1,2)
    return old,P,G

def main():
    for k in range(33):calculate(F(k,128))
    assert calculate(F(0))==(F(1,2),F(3,4),F(5,16))
    assert calculate(F(1,4))==(F(1,2),F(3,4),F(13,16))
    assert max(F(3,4),F(13,16))-F(3,4)==F(1,16)
    assert max(F(3,4),F(5,16))-F(3,4)==0
    assert F(1,8)*(F(3,4)-F(5,16))==F(7,128)
    assert F(7,8)*(F(13,16)-F(3,4))==F(7,128)
    assert (F(3,4)+F(13,16))/2-F(3,4)==F(1,32)
    print("33 finite laws, exact rational checks passed.")
    print("P=3/4; G_cal=5/16+2t; E=23/32; report value=1/32.")

if __name__=="__main__":main()
