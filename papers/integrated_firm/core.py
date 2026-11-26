#!/usr/bin/env python3
"""A finite, jointly optimized recursive robotic firm.

Synthetic technology; Python standard library only. Money is in half-unit ticks.
The finite benchmark uses beta=1: retained cash and dividends telescope exactly.
All end-period uncertainty is observed; a latent transfer regime has a Bayesian belief.
"""
from __future__ import annotations

from dataclasses import dataclass, asdict, replace
from functools import lru_cache
from itertools import product
from math import gcd, ceil
import argparse
import json
import time


@dataclass(frozen=True)
class State:
    arm: int = 1
    mobile: int = 0
    reference: int = 0
    physical_model: int = 0
    digital_model: int = 0
    physical_data: int = 1
    digital_data: int = 0
    procedure: int = 0
    internal_lab: int = 1
    cash: int = 12
    odds_one: int = 3
    odds_zero: int = 2
    market: int = 0


@dataclass(frozen=True)
class Config:
    human_capacity: int = 4
    compute_capacity: int = 7
    wage: int = 2
    token_price: int = 1
    rights_fee: int = 1
    rights_mask: int = 3
    arm_parts: int = 6
    mobile_parts: int = 8
    reference_parts: int = 3
    lab_entry: int = 4
    lab_exit: int = 1
    lab_overhead: int = 1
    outside_training_fee: int = 5
    outside_research_fee: int = 6
    outside_audit_fee: int = 3
    exact_audit_fee: int = 6
    direct_data_fee: int = 6
    method_license_fee: int = 10
    coordination_tokens: int = 1
    training_tokens: int = 2
    procedure_tokens: int = 3
    research_human: int = 1
    # End-market willingness to pay; rows are the two public demand states.
    demand_intercepts: tuple = ((14, 8), (10, 12))
    market_persistence: float = .75
    allow_training: bool = True
    allow_procedure: bool = True
    allow_build: bool = True
    allow_boundary: bool = True
    allow_outside: bool = True
    max_procedure: int = 2
    diagnostic_collection: bool = True


@dataclass(frozen=True)
class Production:
    physical: int
    digital: int
    arm_jobs: int
    mobile_jobs: int
    digital_agent_jobs: int
    physical_version: int
    digital_version: int
    agent_copies: int
    human: int
    tokens: int
    revenue: int
    p_case_physical: float
    p_case_digital: float


@dataclass(frozen=True)
class Research:
    name: str
    method: int
    human: int
    tokens: int
    fee: int
    # Report laws under H=1 and H=0. None is a deterministic operation.
    success_one: float | None = None
    success_zero: float | None = None
    effect: str = "none"


@dataclass(frozen=True)
class Action:
    production: Production
    research: Research
    build: str
    next_lab: int
    retain_physical: int
    retain_digital: int
    human: int
    tokens: int
    outlay: int


def normalize(a, b):
    if a == 0:
        return 0, 1
    if b == 0:
        return 1, 0
    d = gcd(a, b)
    return a // d, b // d


def bayes(a, b, one, zero, success):
    # All channel probabilities in this benchmark are quarters or halves.
    l1 = round(4 * (one if success else 1 - one))
    l0 = round(4 * (zero if success else 1 - zero))
    return normalize(a * l1, b * l0)


class Firm:
    def __init__(self, config=Config()):
        self.c = config
        assert 0<=config.max_procedure<=2
        assert 0<=config.market_persistence<=1
        assert config.arm_parts+config.wage+config.token_price>1
        assert config.mobile_parts+config.wage+config.token_price>2
        assert config.reference_parts+config.wage>1
        self.policy = {}
        self.stats = {"states": 0, "actions_evaluated": 0, "transition_equivalent_pruned": 0}

    def price(self, market, physical, quantity):
        if quantity == 0:
            return 0
        intercept = self.c.demand_intercepts[market][0 if physical else 1]
        return intercept - 2 * quantity

    @lru_cache(None)
    def productions(self, arm, mobile, mp, md, market, last=False):
        """Qualified complete-service recipes include reserved human recovery.

        Copies are chosen at the smallest count supporting the chosen automated jobs;
        additional identical idle copies only consume resources and are dominated.
        Older qualified model versions remain in the operating menu.
        """
        out = []
        for yp, yd, ra, rb, rd in product(range(3), range(3), range(arm+1), range(mobile+1), range(3)):
            if ra + rb > yp or rd > yd:
                continue
            p_versions = (mp,) if last and ra + rb else range(mp+1) if ra+rb else (0,)
            d_versions = (md,) if last and ra+rb+rd else range(md+1) if ra+rb+rd else (0,)
            for ep, ed in product(p_versions, d_versions):
                human = 3*(yp-ra-rb) + 2*(yd-rd) + ra*max(0, 2-ep) + rb*max(0, 1-ep) + rd*max(0, 1-ed)
                copies = ceil((ra+rb+rd)/(1+int(ed==2)))
                tokens = copies + self.c.coordination_tokens*copies*(copies-1)//2
                tokens += (ra+rb)*(2 if ep==0 else 1) + rd*(2 if ed==0 else 1)
                if human > self.c.human_capacity or tokens > self.c.compute_capacity:
                    continue
                revenue = yp*self.price(market, True, yp) + yd*self.price(market, False, yd)
                # Conditional independent opportunities for a first usable family.
                # Archives are retained and nonrival; duplicates do not add another bit.
                p_p = 1-(1-(.75-.25*ep))**ra * (1-(.75-.25*ep)/2)**rb * (.85**(yp-ra-rb))
                p_d = 1-(1-(.75-.25*ed))**rd * (.85**(yd-rd))
                out.append(Production(yp,yd,ra,rb,rd,ep,ed,copies,human,tokens,revenue,p_p,p_d))
        return tuple(out)

    @lru_cache(None)
    def researches(self, mp, md, dp, dd, psi, lab, reference, a, b, last):
        out = [Research("none",0,0,0,0)]
        if last:
            return tuple(out)
        internal = bool(lab)
        if self.c.allow_training:
            for target, level in (("physical",mp),("digital",md)):
                for source, present in (("physical",dp),("digital",dd)):
                    if not present:
                        continue
                    if level >= 2 and source == target:
                        continue
                    effect = target if level < 2 else "probe_"+target
                    for method in range(psi+1):
                        good = (2+method)/4
                        bad = good if source==target else .25
                        if internal:
                            out.append(Research("train_"+source+"_to_"+target,method,1,self.c.training_tokens,0,good,bad,effect))
                        if self.c.allow_outside:
                            out.append(Research("contract_train_"+source+"_to_"+target,method,1,0,self.c.outside_training_fee,good,bad,effect))
        if self.c.allow_procedure and psi < self.c.max_procedure and (dp or dd):
            for method in range(psi+1):
                q = .25 + .25*method + .25*int(dp and dd)
                if internal:
                    out.append(Research("develop_procedure",method,1,self.c.procedure_tokens,0,q,q,"procedure"))
                if self.c.allow_outside:
                    out.append(Research("contract_develop_procedure",method,1,0,self.c.outside_research_fee,q,q,"procedure"))
            if self.c.allow_outside:
                out.append(Research("license_procedure",0,1,0,self.c.method_license_fee,None,None,"procedure"))
        if a and b:
            good = 1.0 if reference else .75
            if internal:
                out.append(Research("audit_transfer",0,1,1,0,good,1-good,"belief"))
            if self.c.allow_outside:
                out.append(Research("contract_audit",0,1,0,self.c.outside_audit_fee,good,1-good,"belief"))
                out.append(Research("exact_outside_audit",0,1,0,self.c.exact_audit_fee,1,0,"belief"))
        if self.c.allow_outside:
            if not dp:
                out.append(Research("buy_physical_reference",0,1,0,self.c.direct_data_fee,None,None,"data_physical"))
            if not dd:
                out.append(Research("buy_digital_reference",0,1,0,self.c.direct_data_fee,None,None,"data_digital"))
        # A separately stated technology regime can automate admitted research
        # workflows. Compute/provider payments still enter the same budget.
        return tuple(replace(r,human=self.c.research_human) if r.name!='none' else r for r in out)

    def actions(self, s, t):
        last = t==1
        builds = [("none",0,0,0)]
        if self.c.allow_build and not last:
            if not s.arm: builds.append(("arm",1,1,self.c.arm_parts))
            if not s.mobile: builds.append(("mobile",1,1,self.c.mobile_parts))
            if not s.reference: builds.append(("reference",1,0,self.c.reference_parts))
        scopes = (s.internal_lab,) if last or not self.c.allow_boundary else (s.internal_lab,1-s.internal_lab)
        rs = self.researches(s.physical_model,s.digital_model,s.physical_data,s.digital_data,s.procedure,s.internal_lab,s.reference,s.odds_one,s.odds_zero,last)
        prods = self.productions(s.arm,s.mobile,s.physical_model,s.digital_model,s.market,last)
        overhead = self.c.lab_overhead*s.internal_lab
        for p in prods:
            if self.c.wage*p.human+self.c.token_price*p.tokens+overhead > s.cash:
                continue
            rp = (0,1) if not last and self.c.diagnostic_collection and not s.physical_data and p.physical and self.c.rights_mask&1 else (0,)
            rd = (0,1) if not last and self.c.diagnostic_collection and not s.digital_data and p.digital and self.c.rights_mask&2 else (0,)
            for r, build, lab, retain_p, retain_d in product(rs,builds,scopes,rp,rd):
                name,bh,bt,parts = build
                human = p.human+r.human+bh
                tokens = p.tokens+r.tokens+bt
                if human > self.c.human_capacity or tokens > self.c.compute_capacity:
                    continue
                switch = 0 if lab==s.internal_lab else self.c.lab_entry if lab else self.c.lab_exit
                outlay = self.c.wage*human+self.c.token_price*tokens+parts+r.fee+overhead+switch+self.c.rights_fee*(retain_p+retain_d)
                if outlay > s.cash:
                    continue
                yield Action(p,r,name,lab,retain_p,retain_d,human,tokens,outlay)
        # Idle closure is always available, not just to an insolvent state.
        # It forgoes current service/research and releases the lab next period.
        if s.internal_lab:
            p=Production(0,0,0,0,0,0,0,0,0,0,0,0.,0.)
            yield Action(p,Research("idle_close",0,0,0,0),"none",0,0,0,0,0,0)

    def transition(self, s, act, t, rival_output=(0,0)):
        """Complete joint law, including publicly observed qualification reports."""
        p, r = act.production, act.research
        revenue = p.revenue
        if rival_output != (0,0):
            revenue = p.physical*self.price(s.market,True,p.physical+rival_output[0])
            revenue += p.digital*self.price(s.market,False,p.digital+rival_output[1])
        cash = s.cash-act.outlay+revenue
        assert cash >= 0  # Customers pay after the working-capital commitment.
        base = replace(s,arm=s.arm+int(act.build=="arm"), mobile=s.mobile+int(act.build=="mobile"),
                       reference=s.reference+int(act.build=="reference"), internal_lab=act.next_lab,cash=cash)
        if r.success_one is None:
            research_outcomes = ((1.,True,s.odds_one,s.odds_zero),)
        else:
            belief=s.odds_one/(s.odds_one+s.odds_zero)
            prob=belief*r.success_one+(1-belief)*r.success_zero
            research_outcomes=[]
            for success,weight in ((True,prob),(False,1-prob)):
                if weight>1e-15:
                    a,b=bayes(s.odds_one,s.odds_zero,r.success_one,r.success_zero,success)
                    research_outcomes.append((weight,success,a,b))
        pp = p.p_case_physical if act.retain_physical else 0.
        pd = p.p_case_digital if act.retain_digital else 0.
        data_p=((0,1-pp),(1,pp)) if 0<pp<1 else ((int(pp==1),1.),)
        data_d=((0,1-pd),(1,pd)) if 0<pd<1 else ((int(pd==1),1.),)
        markets=((s.market,1.),) if t==1 else ((s.market,self.c.market_persistence),(1-s.market,1-self.c.market_persistence))
        outcomes={}
        for (weight,success,a,b),(newp,wp),(newd,wd),(market,wm) in product(research_outcomes,data_p,data_d,markets):
            if weight*wp*wd*wm==0:
                continue
            st=replace(base, physical_model=s.physical_model+int(success and r.effect=="physical"),
                       digital_model=s.digital_model+int(success and r.effect=="digital"),
                       procedure=s.procedure+int(success and r.effect=="procedure"),
                       physical_data=max(s.physical_data,newp,int(r.effect=="data_physical")),
                       digital_data=max(s.digital_data,newd,int(r.effect=="data_digital")),
                       odds_one=a,odds_zero=b,market=market)
            outcomes[st]=outcomes.get(st,0.)+weight*wp*wd*wm
        assert abs(sum(outcomes.values())-1)<1e-12
        return tuple((prob,st) for st,prob in outcomes.items())

    @staticmethod
    def terminal(s):
        return s.cash+s.arm+2*s.mobile+s.reference

    def equivalence_key(self, s, act, t):
        """Only collapse literally identical joint next-state distributions."""
        return frozenset((st,prob) for prob,st in self.transition(s,act,t))

    @lru_cache(None)
    def last_choice(self, arm,mobile,mp,md,lab,cash,market):
        s=State(arm=arm,mobile=mobile,physical_model=mp,digital_model=md,internal_lab=lab,cash=cash,market=market)
        best=float('-inf')
        chosen=None
        for act in self.actions(s,1):
            value=act.production.revenue-act.outlay
            if value>best+1e-10:
                best,chosen=value,act
        return best,chosen

    @lru_cache(None)
    def value(self, s, t):
        self.stats['states']+=1
        if t==0:
            return float(self.terminal(s))
        if t==1:
            # No more learning or construction can pay before the horizon ends.
            cap=self.c.wage*self.c.human_capacity+self.c.token_price*self.c.compute_capacity+self.c.lab_overhead
            margin,act=self.last_choice(s.arm,s.mobile,s.physical_model,s.digital_model,s.internal_lab,min(s.cash,cap),s.market)
            self.policy[(s,t)]=act
            return self.terminal(s)+margin
        best=float('-inf')
        best_action=None
        seen=set()
        for act in self.actions(s,t):
            # Exact single-firm horizon dominance, not a global menu deletion:
            # these changes cannot reach accepted service before liquidation.
            # Keep them in actions() for competitive commitment comparisons.
            if t==2 and (act.research.effect in ('procedure','belief','data_physical','data_digital','probe_physical','probe_digital')
                         or act.retain_physical or act.retain_digital):
                continue
            if t<=3 and act.build=='reference':
                continue
            self.stats['actions_evaluated']+=1
            if t==1:
                val=self.terminal(s)+act.production.revenue-act.outlay
            else:
                outcomes=self.transition(s,act,t)
                key=frozenset((st,pr) for pr,st in outcomes)
                if key in seen:
                    self.stats['transition_equivalent_pruned']+=1
                    continue
                seen.add(key)
                val=sum(pr*self.value(st,t-1) for pr,st in outcomes)
            if val>best+1e-10:
                best,best_action=val,act
        assert best_action is not None, (s,t)
        self.policy[(s,t)]=best_action
        return best

    def distribution(self, initial, horizon):
        self.value(initial,horizon)
        dist={initial:1.}
        rows=[]
        fields=('physical','digital','agent_copies','human','tokens','outlay','revenue')
        for t in range(horizon,0,-1):
            row={key:0. for key in fields}
            row.update({'step':horizon-t,'operating_human':0.,'operating_tokens':0.,'training':0.,'procedure_research':0.,'hardware_starts':0.,'reference_starts':0.,'internal_lab':0.,'cash_start':0.,'procedure_stock':0.})
            nxt={}
            for s,pr in dist.items():
                act=self.policy[(s,t)]
                for key in fields:
                    value=getattr(act,key) if hasattr(act,key) else getattr(act.production,key)
                    row[key]+=pr*value
                row['operating_human']+=pr*act.production.human
                row['operating_tokens']+=pr*act.production.tokens
                row['training']+=pr*('train_' in act.research.name)
                row['procedure_research']+=pr*('procedure' in act.research.name)
                row['hardware_starts']+=pr*(act.build in ('arm','mobile'))
                row['reference_starts']+=pr*(act.build=='reference')
                row['internal_lab']+=pr*s.internal_lab
                row['cash_start']+=pr*s.cash
                row['procedure_stock']+=pr*s.procedure
                for ps,st in self.transition(s,act,t):
                    nxt[st]=nxt.get(st,0.)+pr*ps
            rows.append(row)
            dist=nxt
        terminal=sum(pr*self.terminal(s) for s,pr in dist.items())
        assert abs(terminal-self.value(initial,horizon))<1e-8
        return rows, {'value':terminal,'expected_cash':sum(pr*s.cash for s,pr in dist.items()),
                      'expected_salvage':sum(pr*(s.arm+2*s.mobile+s.reference) for s,pr in dist.items()),
                      'prob_procedure_2':sum(pr for s,pr in dist.items() if s.procedure==2),
                      'expected_physical_model':sum(pr*s.physical_model for s,pr in dist.items()),
                      'expected_digital_model':sum(pr*s.digital_model for s,pr in dist.items()),
                      'expected_robot_stock':sum(pr*(s.arm+s.mobile) for s,pr in dist.items())}


def solve(horizon=3, config=Config(), initial=State()):
    started=time.time()
    f=Firm(config)
    val=f.value(initial,horizon)
    path,terminal=f.distribution(initial,horizon)
    return {'horizon':horizon,'parameters':asdict(config),'initial':asdict(initial),
            'value_including_initial_cash_and_terminal_salvage':val,
            'net_of_initial_cash_including_salvage':val-initial.cash,
            'net_cash_generation':terminal['expected_cash']-initial.cash,
            'first_action':asdict(f.policy[(initial,horizon)]),'expected_path':path,'terminal':terminal,
            'stats':f.stats,'elapsed_seconds':time.time()-started}


if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--horizon',type=int,default=2)
    parser.add_argument('--output')
    args=parser.parse_args()
    result=solve(args.horizon)
    encoded=json.dumps(result,indent=2)
    if args.output:
        with open(args.output,'w') as f:f.write(encoded+'\n')
    print(encoded)
