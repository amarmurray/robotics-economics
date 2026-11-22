"""Independent rational audit of the synthetic menu-information result; no field data."""
from fractions import Fraction as F
from itertools import combinations
PAY = {'idle': (F(0),F(0)), 'oldA': (F(1),F(0)),
       'oldB': (F(0),F(1)), 'learnedB': (F(0),F(1)),
       'learnedUniversal': (F(3,4),F(3,4))}
def value(menu, signal):
    if signal:
        return sum((max(PAY[a][z] for a in menu) for z in range(2)),F(0))/2
    return max(sum(PAY[a])/2 for a in menu)
def interaction(old,new):
    return (value(new,True)-value(new,False))-(value(old,True)-value(old,False))
a=['idle','oldA']; b=a+['learnedB']
c=['idle','oldA','oldB']; d=c+['learnedUniversal']
assert [value(a,False),value(a,True),value(b,False),value(b,True)]==[F(1,2),F(1,2),F(1,2),F(1)]
assert [value(c,False),value(c,True),value(d,False),value(d,True)]==[F(1,2),F(1),F(3,4),F(1)]
assert interaction(a,b)==F(1,2) and interaction(c,d)==-F(1,4)
checks=3; count=0; signs={-1:0,0:0,1:0}
keys=['idle','oldA','oldB','learnedUniversal']
for old_bits in range(1,16):
 for new_bits in range(1,16):
  if old_bits & new_bits != old_bits or old_bits==new_bits: continue
  old=[keys[i] for i in range(4) if old_bits>>i&1]
  new=[keys[i] for i in range(4) if new_bits>>i&1]
  v0=value(old,False); v1=value(old,True); w0=value(new,False); w1=value(new,True)
  assert w0>=v0 and w1>=v1 and v1>=v0 and w1>=w0
  assert interaction(old,new)==(w1-v1)-(w0-v0)
  delta=interaction(old,new); signs[(delta>0)-(delta<0)]+=1
  checks+=2; count+=1
assert count==50
# Bayesian Jensen-gap zero iff one common Bayes optimal action at all support points.
def argmax(menu,z):
 m=max(PAY[a][z] for a in menu)
 return {a for a in menu if PAY[a][z]==m}
assert argmax(a,0)&argmax(a,1)
assert not(argmax(b,0)&argmax(b,1))
checks+=2
print('INDEPENDENT_RATIONAL_AUDIT_OK',{'checks':checks,'nested':count,'interaction_signs':signs,
                                    'positive':str(interaction(a,b)), 'negative':str(interaction(c,d))})
