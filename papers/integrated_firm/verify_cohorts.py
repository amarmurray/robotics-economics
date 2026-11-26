#!/usr/bin/env python3
"""Rational-arithmetic reconstruction of the staged successor model."""
from fractions import Fraction as F
from functools import lru_cache
from itertools import product
from math import ceil
import json
from cohorts import run

def operating_margin(md,z):
    best=-1000
    for qp,qd,ra,rd in product(range(3),range(3),range(2),range(3)):
        if ra>qp or rd>qd:continue
        for version in range(md+1):
            human=3*(qp-ra)+2*(qd-rd)+2*ra+rd*max(0,1-version)
            copies=ra+rd  # This checker only needs digital versions zero and one.
            tokens=copies+copies*(copies-1)//2+2*ra+rd*(2 if version==0 else 1)
            if human>4 or tokens>7:continue
            prices=((14,8),(10,12))[z]
            margin=qp*(prices[0]-2*qp)+qd*(prices[1]-2*qd)-2*human-tokens
            best=max(best,margin)
    return best

def run_checks():
    actual=run()
    raw=[[operating_margin(md,z) for z in (0,1)] for md in (0,1)]
    assert raw==[[7,8],[10,13]]
    gain=4*8-2*(1-F(1,2)**8)
    assert gain==F(str(actual['recipient']['derived_gain']))
    @lru_cache(None)
    def value(r,n,psi,cap):
        if r==0 or n==0:return F(0)
        vals=[F(0)]
        for m in range(psi+1):
            a=F(2+m,4)
            for cost in (5,8):
                vals.append(-cost+a*(gain+value(r-1,n-1,psi,cap))+(1-a)*value(r-1,n,psi,cap))
            if psi<cap:
                p=F(2+m,4)
                for cost in (6,9):
                    vals.append(-cost+p*value(r-1,n,psi+1,cap)+(1-p)*value(r-1,n,psi,cap))
        if psi<cap:vals.append(-13+value(r-1,n,psi+1,cap))
        return max(vals)
    out={'independent_operating_margins':raw,'exact_derived_gain':str(gain),'cases':{}}
    for key,r in actual['cases'].items():
        exact=value(r['research_windows'],r['targets'],0,r['procedure_cap'])
        error=abs(float(exact)-r['incremental_value'])
        assert error<1e-9
        assert abs(r['probability_procedure_2']-r['probability_second_procedure_developed']-r['probability_second_procedure_licensed'])<1e-10
        out['cases'][key]={'exact_value':str(exact),'absolute_discrepancy':error}
    return out

if __name__=='__main__':
    r=run_checks()
    with open('cohort_verification.json','w') as out:json.dump(r,out,indent=2);out.write('\n')
    print(json.dumps(r,indent=2))

