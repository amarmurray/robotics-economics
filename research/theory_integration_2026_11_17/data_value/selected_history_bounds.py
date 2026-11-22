#!/usr/bin/env python3
"""Exact synthetic selected-history audit for multi-job qualified paid production.
No field data. Python 3 stdlib only. Runs without external deps.
"""
from fractions import Fraction as F
from itertools import product
import json, argparse

CHECKS=0
def check(test, msg):
    global CHECKS
    assert test, msg
    CHECKS += 1

BITS=list(product((0,1),repeat=3))
QUEUE_ONE=((0,1),(1,0))

def true_parity(theta):
    assert 0<=theta<=1
    return {(j,h,y):(theta if (j+h+y)%2==0 else 1-theta)/4 for j,h,y in BITS}

def observed_mask(theta):
    """Observable (J,H,S,S*Y): equal logged positive/negative 1/32 in queue-one strata.
    S=0 hides Y, all other strata wholly censored. Missing mass varies with theta.
    """
    law=true_parity(theta)
    obs={}
    for j,h in product((0,1),repeat=2):
        if (j,h) not in QUEUE_ONE:
            obs[(j,h,0,None)]=sum(law[j,h,y] for y in (0,1))
            continue
        for y in (0,1):
            logged=F(1,32)
            check(logged <= law[j,h,y],f'complete-case infeasible {theta} {(j,h,y)}')
            obs[(j,h,1,y)]=logged
        obs[(j,h,0,None)]=sum(law[j,h,y] for y in (0,1))-F(1,16)
    return obs

def full_payoffs(law):
    p00=sum(law[0,0,y] for y in (0,1))
    q0=law[0,0,1]
    q1=law[0,1,1]+law[1,0,1]
    # All returns incremental above safe baseline six; one P purchase cost 1/8.
    r=F(5,16)
    wait=-F(1,8)+q0+q1
    serve=-F(1,8)+F(1,2)*p00+q1
    return {'R':r,'T_wait':wait,'T_serve':serve,'P_oracle':max(r,wait,serve),
            'p00':p00,'q0':q0,'q1':q1}

def fmt(f): return f'{f.numerator}/{f.denominator}' if f.denominator!=1 else str(f.numerator)

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--output',default='selected_history_bounds_results.json')
    args=parser.parse_args()
    first=None; n=0
    lower=F(1,8); upper=F(7,8)
    for t in range(1,8*16): # rational grid from 1/128 to 127/128, restrict feasible region
        theta=F(t,128)
        if not lower<=theta<=upper: continue
        law=true_parity(theta)
        check(sum(law.values())==1,'normalization')
        for j in (0,1):check(sum(law[j,h,y] for h,y in product((0,1),repeat=2))==F(1,2),'J marginal')
        for h in (0,1):check(sum(law[j,h,y] for j,y in product((0,1),repeat=2))==F(1,2),'H marginal')
        for y in (0,1):check(sum(law[j,h,y] for j,h in product((0,1),repeat=2))==F(1,2),'Y marginal')
        for j,h in product((0,1),repeat=2):check(sum(law[j,h,y] for y in (0,1))==F(1,4),'JH table')
        for j,y in product((0,1),repeat=2):check(sum(law[j,h,y] for h in (0,1))==F(1,4),'JY table')
        for h,y in product((0,1),repeat=2):check(sum(law[j,h,y] for j in (0,1))==F(1,4),'HY table')
        obs=observed_mask(theta)
        check(sum(obs.values())==1,'observable mass')
        if first is None: first=obs
        check(obs==first,'two observationally equivalent worlds')
        p=full_payoffs(law)
        check(p['p00']==F(1,4),'physical queue free mass')
        check(p['q0']==(1-theta)/4,'unseen Y queue-zero mass')
        check(p['q1']==theta/2,'Y order at queue-one')
        check(p['T_wait']==F(1,8)+theta/4,'T wait')
        check(p['T_serve']==theta/2,'T serve')
        check(p['P_oracle']==max(F(5,16),theta/2),'whole program')
        # Under this family T_wait never beats both safe R and T_serve.
        check(p['T_wait']<=max(p['R'],p['T_serve']),'unused contingent policy')
        n+=1
    check(n==97,'grid coverage 1/8 to 7/8 inclusive')
    lo=full_payoffs(true_parity(lower));hi=full_payoffs(true_parity(upper))
    check(lo['P_oracle']==F(5,16),'lower P endpoint')
    check(hi['P_oracle']==F(7,16),'upper P endpoint')
    check(lo['P_oracle']<F(13,32)<hi['P_oracle'],'investment reversal')
    check(lo['P_oracle']<F(3,8)<hi['P_oracle'],'grounding reversal')
    check(F(13,32)<F(7,16),'E below high P')
    # With informative complete registries, p00,q0,q1 suffice for all three P policy payoffs.
    # Without the pairwise/parity restriction only the cell-specific logged bounds are sharp.
    # For both queue-one strata, observed Y=1 is 1/32 and unlogged mass 3/16.
    check(lower==4*F(1,32),'sharp theta lower')
    check(upper==4*(F(1,32)+F(3,16)),'sharp theta upper')
    e=F(13,32);g=F(3,8)
    result={'scope':'synthetic, identified only conditional on complete fair pairwise tables and a specified selection/masking mechanism',
            'case_count':n,'exact_checks':CHECKS,'theta_bounds':[fmt(lower),fmt(upper)],
            'q1_bounds':[fmt(lower/2),fmt(upper/2)],
            'P_increment_bounds':[fmt(lo['P_oracle']),fmt(hi['P_oracle'])],
            'G_increment':fmt(g),'E_increment':fmt(e),
            'observed_queue_one_per_jh':{'logged_positive':fmt(F(1,32)),
                                        'logged_negative':fmt(F(1,32)),
                                        'unlogged':fmt(F(3,16))},
            'selected_positive_rate_given_logged_and_queue_one':fmt(F(1,2)),
            'decision_threshold_theta_P_gt_E':fmt(F(13,16)),
            'endpoint_P_minus_E':[fmt(lo['P_oracle']-e),fmt(hi['P_oracle']-e)],
            'worker_conservation':'B3=J+H; B4=max(0,B3-1)+K, where K=1 only after actual T service at B3=0',
            'real_field_data':False,'scientific_novelty_claimed':False}
    with open(args.output,'w',encoding='utf-8') as f:json.dump(result,f,indent=2,sort_keys=True);f.write('\n')
    print(json.dumps(result,indent=2,sort_keys=True))
if __name__=='__main__':main()
