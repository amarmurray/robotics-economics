"""Q8: exact discrete customer-acceptance economics for multi-case workflows.

Synthetic benchmark with accepted bundles, not a measured warehouse model.
Python standard library, Python >=3.10. No external dependencies.
"""
from __future__ import annotations
from dataclasses import dataclass, replace
from fractions import Fraction as F
from functools import reduce
from operator import mul
from math import sqrt
import json
from pathlib import Path


def frechet_bounds(successes: tuple[F, ...]) -> tuple[F, F]:
    """Sharp bounds for intersection probability with arbitrary dependence."""
    if not successes or any(x < 0 or x > 1 for x in successes):
        raise ValueError('Require at least one success probability in [0,1]')
    return max(F(0), sum(successes, F(0)) - (len(successes)-1)), min(successes)


def independent_success(successes: tuple[F, ...]) -> F:
    frechet_bounds(successes)
    return reduce(mul, successes, F(1))


@dataclass(frozen=True)
class Market:
    intercept: F = F(10)
    curvature: F = F(2)
    per_attempt_cost: F = F(1)
    manual_completion_cost: F = F(2)
    attempts_capacity: F = F(4)
    outside_profit: F = F(16)
    capture: F = F(1)
    qualification_cost: F = F(2)

    def __post_init__(self):
        if self.curvature <= 0 or self.attempts_capacity < 0:
            raise ValueError('Positive demand curvature and nonnegative capacity required')
        if min(self.per_attempt_cost, self.manual_completion_cost,
               self.outside_profit, self.qualification_cost) < 0:
            raise ValueError('Costs and outside profit must be nonnegative')
        if not F(0) <= self.capture <= F(1):
            raise ValueError('Capture must be in [0,1]')


@dataclass(frozen=True)
class Outcome:
    acceptance: F
    attempts: F
    expected_accepted: F
    gross_customer_provider_profit: F
    incremental_surplus: F
    provider_before_qualification: F
    provider_after_qualification_if_enter: F
    enter: bool


def evaluate(accepted_probability: F, market: Market = Market()) -> Outcome:
    """Optimize attempts with expected complete-service acceptance probability.

    Each attempted bundle costs c regardless of success; expected failed
    bundles also incur manual completion h. Expected accepted quantity q=g*A;
    customer revenue R(q)=a*q-b*q^2/2 is an aggregate expected-quantity
    demand approximation, not E[R(random Q)] under quantity uncertainty.
    Qualification is a t=0 fixed cost paid only if entrant chooses entry.
    """
    g = accepted_probability
    if g < 0 or g > 1:
        raise ValueError('Acceptance must be in [0,1]')
    m = market
    coefficient = (m.intercept + m.manual_completion_cost)*g - (m.per_attempt_cost+m.manual_completion_cost)
    if g == 0 or coefficient <= 0:
        attempts = F(0)
    else:
        attempts = min(m.attempts_capacity, coefficient/(m.curvature*g*g))
    q = g*attempts
    gross = m.intercept*q - m.curvature*q*q/2 - m.per_attempt_cost*attempts - m.manual_completion_cost*(attempts-q)
    assert gross >= 0
    increment = max(F(0), gross-m.outside_profit)
    provider = m.capture*increment
    after = provider-m.qualification_cost
    # No-entry is a genuine alternative; zero gain favors no entry.
    return Outcome(g,attempts,q,gross,increment,provider,after,after > 0)


def closed_form_capacity_root(m: Market = Market()) -> float:
    """Smaller acceptance root if the investment comparison binds at A=K.

    Only a diagnostic root; must separately check g in [0,1], A*(g)=K,
    positive participation, and the direction of the inequality.
    """
    K=float(m.attempts_capacity)
    if not K or m.capture <= 0:
        raise ValueError('Root needs positive capacity and capture')
    a=float(m.intercept); b=float(m.curvature)
    c=float(m.per_attempt_cost); h=float(m.manual_completion_cost)
    required=float(m.outside_profit+m.qualification_cost/m.capture)
    # (a+h)*K*g-(c+h)*K - (b/2)*K^2*g^2 = required
    disc=(a+h)**2-2*b*K*((c+h)+required/K)
    if disc<0:
        raise ValueError('No real capacity-binding root')
    return ((a+h)-sqrt(disc))/(b*K)


def results():
    s=(F(19,20),)*3
    lo, hi=frechet_bounds(s)
    indep=independent_success(s)
    m=Market()
    scenarios={'disjoint_failures_lower_bound':lo,'independent_failures':indep,
               'coincident_failures_upper_bound':hi,'single_pick_accepted':F(19,20)}
    o={k:evaluate(v,m).__dict__ for k,v in scenarios.items()}
    def val(x):
        if isinstance(x,F):return {'fraction':str(x),'decimal':float(x)}
        if isinstance(x,dict):return {k:val(v) for k,v in x.items()}
        if isinstance(x,(tuple,list)):return [val(v) for v in x]
        return x
    d={'status':'Synthetic service-bundle example; not a calibrated robotics estimate',
       'component_marginals':list(s),'acceptance_bounds':(lo,hi),
       'independence_assumption':indep,'capacity_binding_lower_root':closed_form_capacity_root(m),
       'cases':o,'higher_demand_order':evaluate(indep,replace(m,intercept=F(12))).__dict__,
       'no_manual_rework_order':evaluate(indep,replace(m,manual_completion_cost=F(0))).__dict__}
    return val(d)


if __name__=='__main__':
    path=Path(__file__).with_name('results.json')
    path.write_text(json.dumps(results(),indent=2,sort_keys=True)+'\n')
    print(f'Wrote {path}')
