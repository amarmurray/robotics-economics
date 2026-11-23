from fractions import Fraction as F
from itertools import product
checks=0
for k in range(9):
 p=F(k,8); law={(x,h,y):(p if (x+h+y)%2==0 else 1-p)/4 for x,h,y in product(range(2),repeat=3)}
 a=sum(w*(2+6*x) for (x,h,y),w in law.items()); g=sum(w*max(2+6*x, 2+4*h*y) for (x,h,y),w in law.items())-F(1,2)
 assert a==5 and g==F(9,2)+p; checks+=2
 for x in range(2):
  for h in range(2):
   assert sum(w for (i,j,y),w in law.items() if i==x and j==h)==F(1,4);checks+=1
 for delta in [F(-1,4),F(0),F(1,4)]:
  for alpha0,alpha1 in product([F(-1),F(0),F(1)],repeat=2):
   aa=sum(w*(2+6*x+(alpha1 if x else alpha0)) for (x,h,y),w in law.items())
   gg=sum(w*(2+6*x+(alpha1 if x else alpha0)+((4+delta) if x==0 and h*y else 0)) for (x,h,y),w in law.items())-F(1,2)
   assert gg-aa==-F(1,2)+(4+delta)*p/4;checks+=1
   if k>=7:
    assert gg-aa-F(1,4)>=F(9,128);checks+=1
print('Independent exact fraction checks:',checks)
