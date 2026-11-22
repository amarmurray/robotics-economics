#!/usr/bin/env python3
"""Exact finite synthetic original-buyer/queue model. No field estimates."""
from fractions import Fraction as F
from itertools import product
import json

COUNT=0
def ck(test, label):
    global COUNT
    COUNT += 1
    assert test, label

def law(b):
    # Pairwise independent fair binary H,Y,Z, with triple b = Pr(H=0,Y=1,Z=1).
    tau = b-F(1,8)
    out={(h,y,z):F(1,8)+tau*((-1)**(h+y+z)) for h,y,z in product(range(2), repeat=3)}
    return out

def totals(p, bonus=F(1,2)):
    a=sum(w for (h,y,z),w in p.items() if h==0 and y==1)
    b=sum(w for (h,y,z),w in p.items() if h==0 and y==1 and z==1)
    z=sum(w for (h,y,zz),w in p.items() if zz==1)
    pr=z
    pt=z+F(3,4)*a-b
    popt=max(pr,pt)
    grounded=z+bonus*b-F(1,32)
    e=F(9,16)
    return a,b,z,pr,pt,popt,grounded,e

records=[]
for idx in range(257):
    b=F(idx,1024) # 0 through 1/4
    p=law(b)
    ck(all(w>=0 for w in p.values()),'nonnegative')
    ck(sum(p.values())==1,'total mass')
    for pair in [(0,1),(0,2),(1,2)]:
        for x in product(range(2),repeat=2):
            ck(sum(v for k,v in p.items() if k[pair[0]]==x[0] and k[pair[1]]==x[1])==F(1,4),'pairwise fair')
    a,bb,z,pr,pt,popt,g,e=totals(p)
    ck(a==F(1,4) and bb==b and z==F(1,2),'moments')
    ck(pr==F(1,2),'retained')
    ck(pt==F(11,16)-b,'t2 serve')
    ck(popt==F(1,2)+max(F(0),F(3,16)-b),'optional P')
    ck(g==F(15,32)+b/2,'grounded')
    ck(e==F(9,16),'embodiment')
    ck(pt-pr == F(1,4)*(F(3,4)-b/a),'conditional T-R')
    if idx in [0,160,256]:records.append({'b':str(b),'P':str(popt),'G':str(g),'E':str(e),'winner':('P' if popt>g and popt>e else 'G' if g>popt and g>e else 'E' if e>popt and e>g else 'tie')})

# Exact piecewise rank thresholds and sharp contrast bounds over the whole common-law b segment
ck(totals(law(F(0)))[5:]==(F(11,16),F(15,32),F(9,16)),'endpoint lower')
ck(totals(law(F(1,4)))[5:]==(F(1,2),F(19,32),F(9,16)),'endpoint upper')
ck(totals(law(F(5,32)))[5]==F(17,32),'middle P')
ck(totals(law(F(5,32)))[6]==F(35,64),'middle G')
ck(totals(law(F(5,32)))[7]==F(9,16),'middle E')
# P>E iff b<1/8. G>E iff b>3/16. E wins strictly between.
for b in [F(0),F(1,16),F(1,8),F(5,32),F(3,16),F(1,4)]:
    p=totals(law(b)); P,G,E=p[5:]
    ck((P>E)==(b<F(1,8)),'P/E boundary')
    ck((G>E)==(b>F(3,16)),'G/E boundary')

# Legal no-action-support counterworld: exactly the same fully audited H,Y,Z at b=1/4
# but G-target terminal value uplift coefficient k is not known.
b=F(1,4)
g0=totals(law(b),F(0))[6]
g1=totals(law(b),F(1,2))[6]
ck(g0==F(15,32) and g1==F(19,32),'grounding reward unobserved')
ck(g0<F(9,16)<g1,'audit cannot identify untried grounded value')

# Equal-prior illustrative preinvestment report about the law's b, one report per world.
bset=[F(0),F(1,8),F(1,4)]
with_report=sum(max(totals(law(b))[5:]) for b in bset)/3
# Commitment before report: select one whole P policy, G, or E against same prior.
no_report=max(sum(totals(law(b))[i] for b in bset)/3 for i in [3,4,6,7])
ck(with_report==F(59,96),'information observed early')
ck(no_report==F(9,16),'commitment before report')
ck(with_report-no_report==F(5,96),'net report ceiling')
mid_report=max(sum(totals(law(b))[5] for b in bset)/3, sum(totals(law(b))[6] for b in bset)/3, F(9,16))
ck(mid_report==F(7,12),'after program before dispatch')
ck(with_report-mid_report==F(1,32),'program timing option')
ck(mid_report-no_report==F(1,48),'dispatch timing option')
print(json.dumps({'model':'synthetic global parity history and conserved 2-window queue','assertions':COUNT,'laws':257,'sample_worlds':records,'early_perfect_b_report':str(with_report),'no_precommitment_report':str(no_report),'perfect_report_gross_value':str(with_report-no_report),'intermediate_report':str(mid_report),'program_timing_value':str(with_report-mid_report),'dispatch_timing_value':str(mid_report-no_report),'grounding_support_zero_worlds':[str(g0),str(g1)],'empirical_data':False},indent=2))
