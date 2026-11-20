#!/usr/bin/env python3
"""Exact rational checks for the regime-conditioned source/grounding/embodiment option.
Synthetic complete-policy contributions; NOT empirical robotics estimates or safety approval.
"""
from fractions import Fraction as F
from itertools import product
import json


def direct_value(q, x, alpha):
    """Joint-qualified histories only: flexible versus pre-report embodiment lock."""
    rows = [(alpha*x, (1-alpha)*(q-x)), ((1-alpha)*x, alpha*(q-x))]
    flex = sum(max(2*(a+b),4*a,4*b) for a,b in rows)
    locked_a = sum(max(2*(a+b),4*a) for a,b in rows)
    locked_b = sum(max(2*(a+b),4*b) for a,b in rows)
    return flex, max(locked_a, locked_b)


def switching_premium(q, x, alpha):
    return max(F(0), (2*alpha-1)*q-2*abs(x-q/2))


def sharp_bounds(q, pi, alpha):
    lo = max(F(0),pi+q-1)
    hi = min(pi,q)
    center=q/2
    closest=min(max(center,lo),hi)
    farthest=max(abs(lo-center),abs(hi-center))
    bottom=max(F(0),(2*alpha-1)*q-2*farthest)
    top=switching_premium(q,closest,alpha)
    return lo,hi,bottom,top


def check():
    checks=0
    alphas=[F(1,2),F(3,5),F(3,4),F(9,10),F(1)]
    for pi_num,q_num in product(range(21), repeat=2):
        pi,q=F(pi_num,20),F(q_num,20)
        lo,hi,_,_=sharp_bounds(q,pi,F(3,4))
        for alpha in alphas:
            l,u,lower,upper=sharp_bounds(q,pi,alpha)
            assert (l,u)==(lo,hi)
            xs=set([l,u,min(max(q/2,l),u)])
            # Include all rational grid allocations of regime A to jointly qualified histories.
            xs.update(F(z,20) for z in range(21) if l<=F(z,20)<=u)
            for x in xs:
                fv,lv=direct_value(q,x,alpha)
                direct=fv-lv
                assert direct == switching_premium(q,x,alpha), (pi,q,x,alpha,direct)
                assert lower<=direct<=upper, (pi,q,x,alpha,lower,direct,upper)
                checks+=2
            assert min(switching_premium(q,x,alpha) for x in (l,u))==lower
            assert switching_premium(q,min(max(q/2,l),u),alpha)==upper
            checks+=2
    samples=[(F(1,2),F(2,5),F(3,4),F(1,5)),
             (F(1,2),F(2,5),F(3,4),F(7,20)),
             (F(1,2),F(4,5),F(3,4),F(2,5)),
             (F(1,2),F(4,5),F(3,4),F(3,10))]
    result=[]
    for pi,q,alpha,x in samples:
        l,u,lower,upper=sharp_bounds(q,pi,alpha)
        fv,lv=direct_value(q,x,alpha)
        result.append({'pi':str(pi),'q':str(q),'alpha':str(alpha),'x':str(x),
                       'F_joint_history':str(fv),'L_joint_history':str(lv),
                       'flexibility_premium':str(fv-lv),'sharp_range':[str(lower),str(upper)],
                       'admissible_x':[str(l),str(u)]})
    return {'kind':'synthetic_exact_rational_audit','assertions':checks,'examples':result,
            'safety_approval':False,'original_customer_receipts':False,
            'empirical_transfer_measurement':False,'scientific_novelty_claim':False}

if __name__=='__main__':
    print(json.dumps(check(),indent=2))
