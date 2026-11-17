"""Q9: exact two-state complete-service validation versus incumbent expansion.

Synthetic model, not calibrated data. Python >=3.10, standard library only.
Run: python value_of_evidence.py (writes results.json beside script).
"""
from __future__ import annotations
from dataclasses import dataclass, replace
from fractions import Fraction as F
from math import comb
from pathlib import Path
import json


@dataclass(frozen=True)
class Market:
    intercept: F = F(10)
    curvature: F = F(2)
    cost_per_attempt: F = F(1)
    repair_cost_per_failure: F = F(2)
    capacity: F = F(4)
    outside_profit: F = F(16)
    capture: F = F(1)
    investment: F = F(2)

    def __post_init__(self):
        if self.curvature <= 0 or self.capacity < 0:
            raise ValueError('Demand curvature positive and capacity nonnegative')
        if min(self.cost_per_attempt, self.repair_cost_per_failure,
               self.outside_profit, self.investment) < 0:
            raise ValueError('No negative resource or qualification cost')
        if not F(0) <= self.capture <= F(1):
            raise ValueError('Capture fraction out of bounds')

    def value(self, g: F) -> F:
        """Provider incremental operating profit net of full fixed investment.

        Deterministic fluid expected-output revenue from Q8; not E[R(Q)]
        for stochastic output. Includes customer outside option, free no-entry.
        """
        if not F(0) <= g <= F(1):
            raise ValueError('Completion probability out of bounds')
        linear = (self.intercept+self.repair_cost_per_failure)*g - (self.cost_per_attempt+self.repair_cost_per_failure)
        attempts = F(0) if g == 0 or linear <= 0 else min(self.capacity, linear/(self.curvature*g*g))
        q = g*attempts
        gross = self.intercept*q-self.curvature*q*q/2 - self.cost_per_attempt*attempts - self.repair_cost_per_failure*(attempts-q)
        surplus = max(F(0),gross-self.outside_profit)
        return self.capture*surplus-self.investment


@dataclass(frozen=True)
class Design:
    high_g: F = F(19,20)
    low_g: F = F(17,20)
    prior_high: F = F(1,2)
    budget: F = F(21,10)
    incumbent_investment: F = F(1)
    incumbent_operating_increment: F = F(13,10)
    trial_cost: F = F(1,100)
    fixed_trial_cost: F = F(0)
    market: Market = Market()

    def __post_init__(self):
        if not F(0) < self.low_g < self.high_g < F(1):
            raise ValueError('Two distinguishable interior completion states required')
        if not F(0) <= self.prior_high <= F(1):
            raise ValueError('Invalid prior')
        if min(self.budget,self.incumbent_investment,self.incumbent_operating_increment,
               self.trial_cost,self.fixed_trial_cost) < 0:
            raise ValueError('Negative budget/expense')

    @property
    def incumbent_value(self) -> F:
        return self.incumbent_operating_increment-self.incumbent_investment

    def cost_of_test(self,n:int) -> F:
        if type(n) is not int or n < 0:
            raise ValueError('n must be a nonnegative integer')
        return F(0) if n == 0 else self.fixed_trial_cost+self.trial_cost*n


def binomial_probability(n:int,s:int,g:F) -> F:
    if type(n) is not int or type(s) is not int or n < 0 or not 0 <= s <= n or not 0 <= g <= 1:
        raise ValueError('Invalid binomial inputs')
    return F(comb(n,s))*g**s*(F(1)-g)**(n-s)


def policy(n:int,d:Design=Design()):
    """Return exact preposterior expected value of observing n complete trials.

    Testing is pure information: it does not alter policy quality, service
    capacity or qualification costs. A cash outlay at t=0 reduces the budget
    available for the irreversible decision at t=1. Benefits are t=2 valued
    with a common unit discount factor. Retained cash is implicit (net value).
    """
    cost=d.cost_of_test(n)
    if cost > d.budget:
        return None
    liquid=d.budget-cost
    vh=d.market.value(d.high_g)
    vl=d.market.value(d.low_g)
    ja=d.incumbent_value
    allowed_a=liquid >= d.incumbent_investment
    allowed_b=liquid >= d.market.investment
    expected=F(0)
    branches=[]
    for s in range(n+1):
        wh=d.prior_high*binomial_probability(n,s,d.high_g)
        wl=(F(1)-d.prior_high)*binomial_probability(n,s,d.low_g)
        prob=wh+wl
        assert prob >= 0
        choices={'retain':F(0)}
        if allowed_a:choices['incumbent']=ja*prob
        if allowed_b:choices['new_service']=vh*wh+vl*wl
        # deterministic tie: retain, incumbent, then new service
        action=max(choices,key=lambda key:(choices[key],-['retain','incumbent','new_service'].index(key)))
        contribution=choices[action]
        expected+=contribution
        branches.append((s,prob,action,contribution))
    assert sum((x[1] for x in branches),F(0)) == 1
    return {'n':n,'test_cost':cost,'budget_after_test':liquid,
            'gross':expected,'net':expected-cost,
            'branches':branches,'new_service_available':allowed_b}


def optimize(max_n:int=40,d:Design=Design()):
    if type(max_n) is not int or max_n<0:
        raise ValueError('max_n invalid')
    feasible=[policy(n,d) for n in range(max_n+1)]
    feasible=[r for r in feasible if r is not None]
    # ties select the fewer trials
    return max(feasible,key=lambda r:(r['net'],-r['n']))


def information_without_budget_gate(n:int,d:Design=Design()) -> F:
    """EVSI before cost relative to prior best, holding both actions feasible."""
    ample=replace(d,budget=d.budget+d.market.investment+d.incumbent_investment+d.cost_of_test(n))
    r=policy(n,ample)
    baseline=policy(0,ample)
    return r['gross']-baseline['gross']


def results():
    d=Design()
    cases={
        'base':d,
        'just_funded_no_test':replace(d,budget=F(2)),
        'cash_2_05':replace(d,budget=F(41,20)),
        'higher_demand':replace(d,market=replace(d.market,intercept=F(12))),
        'low_capture':replace(d,market=replace(d.market,capture=F(1,2))),
        'indistinguishable_states':replace(d,high_g=F(19,20),low_g=F(189,200)),
    }
    def enc(x):
        if isinstance(x,F):return {'fraction':str(x),'decimal':float(x)}
        if isinstance(x,dict):return {k:enc(v) for k,v in x.items()}
        if isinstance(x,(list,tuple)):return [enc(v) for v in x]
        return x
    out={'status':'Synthetic two-state VOI and capital allocation; no estimated failure rates or financial returns',
         'base_state_values':{'high':d.market.value(d.high_g),'low':d.market.value(d.low_g),
                              'incumbent':d.incumbent_value},
         'posterior_entry_threshold':(d.incumbent_value-d.market.value(d.low_g))/(d.market.value(d.high_g)-d.market.value(d.low_g)),
         'gross_EVSI':{str(n):information_without_budget_gate(n,d) for n in (0,1,2,3,5,8,10,20,40)},
         'cases':{name:{'design':{'budget':p.budget,'capture':p.market.capture,'intercept':p.market.intercept,
                                  'high_g':p.high_g,'low_g':p.low_g},
                        'best':{k:v for k,v in optimize(40,p).items() if k!='branches'},
                        'no_test_net':policy(0,p)['net']} for name,p in cases.items()},
         'base_eight_trial_actions':[(s,pr,a) for s,pr,a,_ in policy(8,d)['branches']]}
    return enc(out)

if __name__=='__main__':
    out=Path(__file__).with_name('results.json')
    out.write_text(json.dumps(results(),indent=2,sort_keys=True)+'\n')
    print(f'Wrote {out}')
