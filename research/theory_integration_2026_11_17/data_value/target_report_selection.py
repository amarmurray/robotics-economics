"""Conditional exact diagnostic for production-selected target reports.
All numbers synthetic. It does not contain real robotics/customer observations.
"""
from fractions import Fraction as F
from itertools import product
from math import log, sqrt
import json

A = {'F': (F(0),F(0)), 'S': (F(3,4),F(3,4)),
     'G': (F(3),F(-1)), 'T': (F(4),F(-6))}
P = (F(1,2), F(1,2))
QH = F(3,5)

def value(rule, qh, ql):
    high, low = rule
    return sum((P[z]*(q*A[high][z]+(1-q)*A[low][z])
                for z,q in enumerate((qh,ql))), F(0))

def opt(qh, ql):
    out = [(value(r,qh,ql),r) for r in product(A,A)]
    top = max(x[0] for x in out)
    return top, [r for v,r in out if v==top]

assert opt(QH,F(2,5))[0]==F(43,40)
assert ('G','S') in opt(QH,F(2,5))[1]
assert opt(QH,F(3,5))[0]==F(1)
assert ('G','G') in opt(QH,F(3,5))[1]
assert value(('G','S'),QH,F(2,5))==F(43,40)
assert value(('G','S'),QH,F(3,5))==F(9,10)
assert value(('G','G'),QH,F(2,5))==F(1)
assert value(('G','G'),QH,F(3,5))==F(1)
# Two observationally identical worlds: selected high share a=q*rho_h=2/5.
worlds=[(F(2,5),F(1)),(F(3,5),F(2,3))]
assert all(q*r==F(2,5) for q,r in worlds)
assert all((1-q*r)==F(3,5) for q,r in worlds)
assert opt(QH,worlds[0][0])[0]!=opt(QH,worlds[1][0])[0]
# Sharp partial set with known a,b but arbitrary selection.
a,b=F(2,5),F(0)
assert (a,1-b)==(F(2,5),F(1))
# Under conditional high inclusion in [2/3,1], the row is in [2/5,3/5].
assert (a/F(1),a/F(2,3)) == (F(2,5), F(3,5))
# A min-max saddle: at ql=3/5 any report policy <= constant G=1.
assert max(value(r,QH,F(3,5)) for r in product(A,A))==F(1)
assert min(value(('G','G'),QH,q) for q in [F(2,5),F(3,5)])==F(1)
# A fixed unconditional accepted order distribution with uncertain p and q:
# |V(p,q)-V(p',q')| <= (M-m)TV(p,p') + sum p'_z R_z |q_z-q'_z|.
# Tested on rational grids, not claimed as proof.
span=max(v for row in A.values() for v in row)-min(v for row in A.values() for v in row)
ranges=[max(row[z] for row in A.values())-min(row[z] for row in A.values()) for z in range(2)]
nchecks=0
for high,low in product(A,A):
  rule=(high,low)
  for p in [F(1,4),F(1,2),F(3,4)]:
   for p2 in [F(1,4),F(1,2),F(3,4)]:
    for ql in [F(2,5),F(1,2),F(3,5)]:
     for ql2 in [F(2,5),F(1,2),F(3,5)]:
      def v(p,q):
       return p*(QH*A[high][0]+(1-QH)*A[low][0])+(1-p)*(q*A[high][1]+(1-q)*A[low][1])
      lhs=abs(v(p,ql)-v(p2,ql2))
      rhs=span*abs(p-p2)+(1-p2)*ranges[1]*abs(ql-ql2)
      assert lhs<=rhs,(rule,p,p2,ql,ql2,lhs,rhs)
      nchecks+=1

n=1000; m=2; delta=.05
radius=sqrt(log(4*m/delta)/(2*n))
result={
 'description':'Synthetic whole-order source/grounding policy target report selection, no robot or customer calibration',
 'observable_selected_high_share':'2/5',
 'worlds':[{'target_low_report_probability':str(q),'high_report_selection_probability':str(r),
            'observable_selected_share':str(q*r), 'optimized_full_service_value':str(opt(QH,q)[0])}
           for q,r in worlds],
 'unknown_propensity_identified_low_row':['2/5','1'],
 'bounded_high_selection_[2/3,1]_low_row':['2/5','3/5'],
 'robust_qualified_production_with_bounded_propensity':'1',
 'perfectly_identified_low_row_2/5_production':'43/40',
 'selected_only_H=400_L=0_N=1000_95pct_outer_row':[max(0,400/n-radius),min(1,1-0/n+radius)],
 'independent_demand_sensitivity_grid_checks':nchecks,
 'method':'exact rational policy enumeration, saddle, observational equivalence, and independent grid check; no general proof from numerical tests'
}
print(json.dumps(result,indent=2))
