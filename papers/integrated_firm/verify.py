#!/usr/bin/env python3
"""Independent physical/cash ledger and latent-world replay for core.py.

The checker reconstructs costs, report laws and state changes; it does not call
Firm.transition. Exact planning remains supplied by Firm.value. No simulation
sampling error is used to excuse an accounting discrepancy.
"""
from dataclasses import asdict
from fractions import Fraction
from itertools import product
from math import ceil, isclose
import json
from core import State, Config, Firm

def research_law(s, act):
    name, m = act.research.name, act.research.method
    if 'train_' in name:
        source, target = name.split('train_',1)[1].split('_to_')
        return ((2+m)/4, (2+m)/4 if source==target else .25)
    if name in ('develop_procedure','contract_develop_procedure'):
        q=.25+.25*m+.25*int(s.physical_data and s.digital_data)
        return q,q
    if name in ('audit_transfer','contract_audit'):
        q=1. if s.reference else .75
        return q,1-q
    if name=='exact_outside_audit':
        return 1.,0.
    return None

def check_action(c,s,a):
    p,r=a.production,a.research
    if r.name=='idle_close':
        assert (a.human,a.tokens,a.outlay,p.physical,p.digital,a.next_lab)==(0,0,0,0,0,0)
        return 0
    auto=p.arm_jobs+p.mobile_jobs
    h=3*(p.physical-auto)+2*(p.digital-p.digital_agent_jobs)
    h+=p.arm_jobs*max(0,2-p.physical_version)+p.mobile_jobs*max(0,1-p.physical_version)
    h+=p.digital_agent_jobs*max(0,1-p.digital_version)
    copies=ceil((auto+p.digital_agent_jobs)/(1+int(p.digital_version==2)))
    tokens=copies+c.coordination_tokens*copies*(copies-1)//2
    tokens+=auto*(2 if p.physical_version==0 else 1)+p.digital_agent_jobs*(2 if p.digital_version==0 else 1)
    assert (h,tokens,copies)==(p.human,p.tokens,p.agent_copies)
    assert p.arm_jobs<=s.arm and p.mobile_jobs<=s.mobile
    assert p.physical_version<=s.physical_model and p.digital_version<=s.digital_model
    # Research bundles, including contracted provider resources charged once.
    rh=0 if r.name=='none' else c.research_human
    rt=rf=0
    if r.name.startswith('contract_train_'):rf=c.outside_training_fee
    elif r.name.startswith('train_'):rt=c.training_tokens
    elif r.name=='develop_procedure':rt=c.procedure_tokens
    elif r.name=='contract_develop_procedure':rf=c.outside_research_fee
    elif r.name=='license_procedure':rf=c.method_license_fee
    elif r.name=='audit_transfer':rt=1
    elif r.name=='contract_audit':rf=c.outside_audit_fee
    elif r.name=='exact_outside_audit':rf=c.exact_audit_fee
    elif r.name.startswith('buy_'):rf=c.direct_data_fee
    assert (rh,rt,rf)==(r.human,r.tokens,r.fee)
    assert research_law(s,a)==(None if r.success_one is None else (r.success_one,r.success_zero))
    bh=int(a.build!='none');bt=int(a.build in ('arm','mobile'))
    parts={'none':0,'arm':c.arm_parts,'mobile':c.mobile_parts,'reference':c.reference_parts}[a.build]
    totalh=h+rh+bh; totalt=tokens+rt+bt
    switch=0 if a.next_lab==s.internal_lab else c.lab_entry if a.next_lab else c.lab_exit
    cost=c.wage*totalh+c.token_price*totalt+parts+rf+c.lab_overhead*s.internal_lab+switch
    cost+=c.rights_fee*(a.retain_physical+a.retain_digital)
    assert (totalh,totalt,cost)==(a.human,a.tokens,a.outlay)
    assert totalh<=c.human_capacity and totalt<=c.compute_capacity and cost<=s.cash
    revenue=sum(q*(c.demand_intercepts[s.market][j]-2*q) for j,q in enumerate((p.physical,p.digital)))
    assert revenue==p.revenue
    return revenue

def independent_transitions(c,s,a,t,true_h):
    revenue=check_action(c,s,a)
    law=research_law(s,a)
    if law is None:
        observations=[(True,1.)]
    else:
        q=law[0] if true_h else law[1]
        observations=[(v,p) for v,p in ((True,q),(False,1-q)) if p>0]
    p=a.production
    pp=0. if not a.retain_physical else 1-(1-(.75-.25*p.physical_version))**p.arm_jobs*(1-(.75-.25*p.physical_version)/2)**p.mobile_jobs*.85**(p.physical-p.arm_jobs-p.mobile_jobs)
    pd=0. if not a.retain_digital else 1-(1-(.75-.25*p.digital_version))**p.digital_agent_jobs*.85**(p.digital-p.digital_agent_jobs)
    data_p=[(v,pr) for v,pr in ((0,1-pp),(1,pp)) if pr>0]
    data_d=[(v,pr) for v,pr in ((0,1-pd),(1,pd)) if pr>0]
    markets=[(s.market,1.)] if t==1 else [(s.market,c.market_persistence),(1-s.market,1-c.market_persistence)]
    for (success,po),(np,wp),(nd,wd),(market,wm) in product(observations,data_p,data_d,markets):
        if po*wp*wd*wm==0:
            continue
        st=asdict(s)
        st['cash']=s.cash-a.outlay+revenue
        st['arm']+=int(a.build=='arm')
        st['mobile']+=int(a.build=='mobile')
        st['reference']+=int(a.build=='reference')
        st['internal_lab']=a.next_lab
        st['market']=market
        if law is not None:
            prior=Fraction(s.odds_one,s.odds_one+s.odds_zero)
            l1=Fraction(law[0] if success else 1-law[0])
            l0=Fraction(law[1] if success else 1-law[1])
            posterior=prior*l1/(prior*l1+(1-prior)*l0)
            st['odds_one']=posterior.numerator
            st['odds_zero']=posterior.denominator-posterior.numerator
        if success:
            if a.research.effect=='physical':st['physical_model']+=1
            if a.research.effect=='digital':st['digital_model']+=1
            if a.research.effect=='procedure':st['procedure']+=1
        st['physical_data']=max(s.physical_data,np,int(a.research.effect=='data_physical'))
        st['digital_data']=max(s.digital_data,nd,int(a.research.effect=='data_digital'))
        yield po*wp*wd*wm,State(**st)

def potential(s):
    return 7*s.physical_model+3*s.digital_model+5*s.procedure+2*(s.physical_data+s.digital_data)

def replay(f,initial,horizon):
    value=f.value(initial,horizon)
    p=initial.odds_one/(initial.odds_one+initial.odds_zero)
    dist={(1,initial):p,(0,initial):1-p}
    expected_profit=shaping=0.
    visited=set()
    for t in range(horizon,0,-1):
        nxt={}
        for (h,s),weight in dist.items():
            if weight==0:continue
            a=f.policy[(s,t)]
            visited.add((s,t))
            revenue=check_action(f.c,s,a)
            expected_profit+=weight*(revenue-a.outlay)
            transitions=list(independent_transitions(f.c,s,a,t,h))
            assert abs(sum(pr for pr,_ in transitions)-1)<1e-12
            for pr,st in transitions:
                nxt[(h,st)]=nxt.get((h,st),0)+weight*pr
                shaping+=weight*pr*(potential(st)-potential(s))
        dist=nxt
        # The observed posterior must agree with the independently propagated
        # mass over the common latent regime, including adaptive selection.
        masses={}
        for (h,s),w in dist.items():
            den,num=masses.get(s,(0.,0.))
            masses[s]=(den+w,num+w*h)
        for s,(den,num) in masses.items():
            assert abs(num/den-s.odds_one/(s.odds_one+s.odds_zero))<1e-10
    wealth=sum(w*(s.cash+s.arm+2*s.mobile+s.reference) for (h,s),w in dist.items())
    cash=sum(w*s.cash for (h,s),w in dist.items())
    final_potential=sum(w*potential(s) for (h,s),w in dist.items())
    assert abs(wealth-value)<1e-8
    assert abs(cash-initial.cash-expected_profit)<1e-8
    assert abs(shaping-(final_potential-potential(initial)))<1e-8
    return {'bellman_value':value,'independent_hidden_world_value':wealth,
            'absolute_discrepancy':abs(wealth-value),
            'net_cash_generation':expected_profit,
            'cash_ledger_discrepancy':abs(cash-initial.cash-expected_profit),
            'shaping_telescoping_discrepancy':abs(shaping-final_potential+potential(initial)),
            'unadjusted_potential_windfall':shaping,
            'selected_public_state_periods_checked':len(visited)}

def channel_checks(c=Config()):
    f=Firm(c)
    cases=[State(),State(cash=25,digital_data=1,physical_model=1,digital_model=1,procedure=1,mobile=1,reference=1),
           State(cash=30,physical_model=2,digital_model=2,procedure=2,mobile=1,odds_one=1,odds_zero=0),
           State(cash=0)]
    checked=0
    for s in cases:
        p=s.odds_one/(s.odds_one+s.odds_zero)
        for a in f.actions(s,3):
            truth={}
            for h,ph in ((1,p),(0,1-p)):
                if ph==0:continue
                for pr,st in independent_transitions(c,s,a,3,h):
                    truth[st]=truth.get(st,0)+ph*pr
            stated={st:pr for pr,st in f.transition(s,a,3)}
            assert truth.keys()==stated.keys()
            assert max(abs(truth[st]-stated[st]) for st in truth)<1e-12
            assert abs(sum(pr*st.odds_one/(st.odds_one+st.odds_zero) for st,pr in truth.items())-p)<1e-12
            checked+=1
    return {'joint_kernels_independently_reconstructed':checked,'posterior_martingale':'passed'}

def run():
    results={'channels':channel_checks(),'replays':{}}
    for h in (2,4):
        f=Firm()
        results['replays'][str(h)]=replay(f,State(),h)
    f=Firm()
    baseline=f.value(State(),3)
    monotone={}
    for key in ('cash','physical_model','digital_model','physical_data','digital_data','procedure','mobile','reference'):
        base=asdict(State())
        if key=='physical_data':base[key]=0;low=State(**base);high=State()
        else:low=State();base[key]+=1;high=State(**base)
        gain=f.value(high,3)-f.value(low,3)
        assert gain>=-1e-8
        monotone[key]=gain
    results['free_optional_endowment_value_changes_t3']=monotone
    return results

if __name__=='__main__':
    results=run()
    with open('verification_results.json','w') as out:json.dump(results,out,indent=2);out.write('\n')
    print(json.dumps(results,indent=2))

