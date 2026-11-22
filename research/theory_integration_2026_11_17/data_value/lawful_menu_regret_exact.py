#!/usr/bin/env python3
"""Exact synthetic two-demand-state, two-action paid Q-support regret checks.
No field robotics, customer or settlement data are used.
"""
import json
from fractions import Fraction as F
from itertools import combinations_with_replacement

checks = 0

def check(condition, detail):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(detail)

def regret(d1, d2, p):
    mean = p*d1 + (1-p)*d2
    return p*max(F(0),d1) + (1-p)*max(F(0),d2) - max(F(0),mean)

def sharp(lo1,hi1,lo2,hi2,p):
    # Exact rectangular identified regret envelope for two actions, two demand states.
    upper = max(min(p*max(F(0),hi1), (1-p)*max(F(0),-lo2)),
                min(p*max(F(0),-lo1), (1-p)*max(F(0),hi2)))
    if hi1>=0 and hi2>=0 or lo1<=0 and lo2<=0:
        lower = F(0)
    elif lo1>0 and hi2<0:
        lower = min(p*lo1,(1-p)*(-hi2))
    elif lo2>0 and hi1<0:
        lower = min(p*(-hi1),(1-p)*lo2)
    else:
        raise AssertionError('unclassified intervals')
    return lower, upper

def s(x): return f'{x.numerator}/{x.denominator}'

values=[F(i) for i in (-2,-1,0,1,2)]
intervals=list(combinations_with_replacement(values,2))
cases=0
for (l1,u1) in intervals:
    for (l2,u2) in intervals:
        for p in (F(1,4),F(1,2),F(3,4)):
            lo,hi=sharp(l1,u1,l2,u2,p)
            candidates1={l1,u1} | ({F(0)} if l1<=0<=u1 else set())
            candidates2={l2,u2} | ({F(0)} if l2<=0<=u2 else set())
            direct=[regret(x,y,p) for x in candidates1 for y in candidates2]
            check(lo==min(direct),f'lo {(l1,u1,l2,u2,p)}')
            check(hi==max(direct),f'hi {(l1,u1,l2,u2,p)}')
            check(lo>=0 and lo<=hi,'regret order')
            cases+=1

# When R={a=(1,0)} and new b=(0,q), the omitted original-buyer
# paid-service response q is not learned from task-level qualification.
p=F(1,2)
loss_interval = sharp(F(-1),F(-1),F(0),F(1),p)
check(loss_interval==(F(0),F(1,2)),'sharp buyer report regret')
q_grid={F(i,10) for i in range(11)} | {F(3,5)}
for q in sorted(q_grid):
    no_signal=max(F(1,2),q/2)
    with_signal=(1+q)/2
    q_loss=with_signal-no_signal
    check(q_loss==q/2,'identity: incremental value of report for S')
    check(q_loss==regret(F(-1),q,p),'same regret')
    S_net=no_signal-F(1,10)
    G_net=F(1,2)-F(1,20)
    SG_net=with_signal-F(3,20)
    E_net=F(3,4)-F(1,10)
    check(SG_net-E_net==q/2-F(3,10),'SG-E identity')
    check(SG_net>E_net if q>F(3,5) else SG_net<=E_net,'synthetic decision boundary')
    check(S_net==F(2,5) and G_net==F(9,20) and E_net==F(13,20),'fixed alternatives')

# A pure legal support graph forbids actions, rather than assigning them Q=0.
# Nonempty common action intersection is required to act without observing state.
A0={'idle','old_A'}; A1={'idle','old_A','learned_B'}
C=A0&A1
check(C==A0,'legal menu intersection')
# Robust common supported paid-option witness under interval-valid bounds.
lower={'A':{'idle':F(0),'old_A':F(3,4),'learned_B':F(0)},
       'B':{'idle':F(0),'old_A':F(3,4),'learned_B':F(0)}}
upper={'A':{'idle':F(0),'old_A':F(3,4),'learned_B':F(1,2)},
       'B':{'idle':F(0),'old_A':F(3,4),'learned_B':F(1,2)}}
check(all(lower[z]['old_A']>=max(upper[z].values()) for z in lower),'common robust paid witness')

report={
 'status':'synthetic exact arithmetic only',
 'theorem':'sharp two-demand, two-common-action box-identified buyer-information regret',
 'interval_grid_cases':cases,'checks':checks,
 'unit_grid':{'interval_endpoints':[-2,-1,0,1,2],'p':['1/4','1/2','3/4']},
 'missing_original_buyer_paid_q':{'support':['0','1'],'buyer_report_value_range':[s(x) for x in loss_interval],
  'SG_minus_E_net_range':['-3/10','1/5'],'switch_condition':'q > 3/5 (synthetic only)',
  'S_net':'2/5','G_net':'9/20','E_net':'13/20'},
 'real_R_S_G_SG_E_paid_panel':False,'approved_lawful_physical_comparison':False,
 'verified_full_horizon_Q_ceilings':False,'nov22_scientific_gate_passed':False
}
if __name__=='__main__':
    print(json.dumps(report,sort_keys=True,indent=2))
