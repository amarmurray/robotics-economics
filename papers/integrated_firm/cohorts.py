#!/usr/bin/env python3
"""Successor procedures with many recipient tasks, valued by core production.

A dated research window precedes L operating periods in independent local end
markets. Installed equipment is fixed during this restriction; research and all
operating outlays are prefunded by an explicit sufficient cash bound. No interim
research credit is spendable cash. Its additive G is derived from actual optimal
accepted-service recipes in core.py, not assigned as a continuation coefficient.
"""
from dataclasses import asdict
from functools import lru_cache
import json
from core import Firm,State,Config

def recipient_value(periods=8,c=Config()):
    f=Firm(c)
    profits={}
    plans={}
    for md in (0,1):
        profits[md]=[]
        plans[md]=[]
        for market in (0,1):
            s=State(cash=100,internal_lab=0,digital_model=md,market=market)
            a=f.last_choice(s.arm,s.mobile,s.physical_model,s.digital_model,0,100,market)[1]
            profits[md].append(a.production.revenue-a.outlay)
            plans[md].append(asdict(a.production))
    dist=[1.,0.]
    total=[0.,0.]
    for _ in range(periods):
        for md in (0,1):total[md]+=sum(dist[z]*profits[md][z] for z in (0,1))
        stay=c.market_persistence
        dist=[dist[0]*stay+dist[1]*(1-stay),dist[1]*stay+dist[0]*(1-stay)]
    return {'operating_periods':periods,'current_profit_by_model_and_market':profits,
            'accepted_service_recipes':plans,'total_unqualified_profit':total[0],
            'total_qualified_profit':total[1],'derived_gain':total[1]-total[0]}

class Cohorts:
    def __init__(self,gain,cap=2,c=Config()):
        self.G=gain;self.cap=cap;self.c=c;self.policy={}
        # Research uses a reserved lab in this restriction. Each active window
        # pays the same overhead as the parent technology; stopping is free.
        self.training_cost=c.wage*c.research_human+c.token_price*c.training_tokens+c.lab_overhead
        self.procedure_cost=c.wage*c.research_human+c.token_price*c.procedure_tokens+c.lab_overhead
        self.contract_training=c.wage*c.research_human+c.outside_training_fee+c.lab_overhead
        self.contract_procedure=c.wage*c.research_human+c.outside_research_fee+c.lab_overhead
        self.license_cost=c.wage*c.research_human+c.method_license_fee+c.lab_overhead

    def actions(self,n,psi):
        out=[('stop',0.,0.,'none')]
        if n:
            # Both inherited archives exist; each target has its own qualified
            # execution model, so successes are not copies of the same discovery.
            for m in range(psi+1):
                out.append(('train_'+str(m),self.training_cost,(2+m)/4,'target'))
                out.append(('contract_train_'+str(m),self.contract_training,(2+m)/4,'target'))
                if psi<self.cap:
                    q=.5+.25*m
                    out.append(('develop_'+str(m),self.procedure_cost,q,'procedure'))
                    out.append(('contract_develop_'+str(m),self.contract_procedure,q,'procedure'))
            if psi<self.cap:
                out.append(('license',self.license_cost,1.,'procedure'))
        return out

    @lru_cache(None)
    def value(self,r,n,psi):
        if r==0 or n==0:return 0.
        candidates=[]
        for name,cost,p,effect in self.actions(n,psi):
            if name=='stop':v=0.
            elif effect=='target':
                v=-cost+p*(self.G+self.value(r-1,n-1,psi))+(1-p)*self.value(r-1,n,psi)
            else:
                v=-cost+p*self.value(r-1,n,psi+1)+(1-p)*self.value(r-1,n,psi)
            candidates.append((v,(name,cost,p,effect)))
        v,a=max(candidates,key=lambda x:x[0])
        self.policy[r,n,psi]=a
        return v

    def solve(self,windows,targets,initial_procedure=0):
        v=self.value(windows,targets,initial_procedure)
        dist={(targets,initial_procedure):1.}
        spent=0.;steps=[];second_by_development=0.;second_by_license=0.
        for r in range(windows,0,-1):
            nxt={};row={'research_step':windows-r,'training':0.,'procedure_development':0.,'licenses':0.,'outlay':0.}
            for (n,psi),w in dist.items():
                if n==0:a=('stop',0.,0.,'none')
                else:a=self.policy[r,n,psi]
                name,cost,p,effect=a
                row['outlay']+=w*cost;spent+=w*cost
                if effect=='target':row['training']+=w
                if effect=='procedure':
                    row['procedure_development']+=w*(name!='license')
                    row['licenses']+=w*(name=='license')
                    if psi==1:
                        second_by_development+=w*p*(name!='license')
                        second_by_license+=w*p*(name=='license')
                if name=='stop':branches=[(1.,(n,psi))]
                elif effect=='target':branches=[(p,(n-1,psi)),(1-p,(n,psi))]
                else:branches=[(p,(n,psi+1)),(1-p,(n,psi))]
                for pr,st in branches:
                    if pr:nxt[st]=nxt.get(st,0.)+w*pr
            dist=nxt;steps.append(row)
        qualified=sum(w*(targets-n) for (n,psi),w in dist.items())
        probability_2=sum(w for (n,psi),w in dist.items() if psi==2)
        assert abs(v-(qualified*self.G-spent))<1e-8
        # Safe sufficient prefunding: every date's largest research invoice,
        # then every local operating pool, without relying on receipts.
        max_research=max(self.training_cost,self.procedure_cost,self.contract_training,self.contract_procedure,self.license_cost)
        return {'research_windows':windows,'targets':targets,'procedure_cap':self.cap,
                'initial_procedure':initial_procedure,'derived_gain_per_qualification':self.G,
                'incremental_value':v,'first_action':self.policy.get((windows,targets,initial_procedure),('stop',0,0,'none'))[0],
                'expected_qualified_targets':qualified,'expected_research_outlay':spent,
                'probability_procedure_2':probability_2,
                'probability_second_procedure_developed':second_by_development,
                'probability_second_procedure_licensed':second_by_license,
                'research_prefunding_bound':windows*max_research,'expected_path':steps,
                'terminal_distribution':[{'remaining_targets':n,'procedure':psi,'probability':w} for (n,psi),w in sorted(dist.items())],
                'cash_profit_identity_error':abs(v-qualified*self.G+spent)}

def run():
    recipient=recipient_value()
    result={'recipient':recipient,'cases':{}}
    for targets,windows in ((2,16),(4,16),(8,16),(12,16),(8,10),(8,20)):
        for cap in (0,1,2):
            key='N'+str(targets)+'_R'+str(windows)+'_cap'+str(cap)
            r=Cohorts(recipient['derived_gain'],cap).solve(windows,targets)
            r['operating_prefunding_bound']=targets*recipient['operating_periods']*(Config().wage*Config().human_capacity+Config().token_price*Config().compute_capacity)
            result['cases'][key]=r
    return result

if __name__=='__main__':
    result=run()
    with open('cohort_results.json','w') as out:json.dump(result,out,indent=2);out.write('\n')
    for k,r in result['cases'].items():
        print(k,r['incremental_value'],r['first_action'],r['probability_procedure_2'],r['expected_qualified_targets'])

