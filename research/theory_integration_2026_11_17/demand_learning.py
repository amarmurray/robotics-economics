"""Exact closed-form stationary qualification choice in a concave accepted-service economy.

All parameters synthetic; no robot/vendor calibration. This extends the
production/receivables theoretical framework with priced endogenous A output.
Requires m >= d*K, so accepted A is capacity-constrained at u=0.
"""
from dataclasses import dataclass, replace
from math import sqrt, isclose
import json


@dataclass(frozen=True)
class Economy:
    m: float = 4.0             # retained marginal contribution before demand curvature
    d: float = 4.0             # decreasing marginal customer value / capture
    K: float = 1.0             # qualified A capacity at zero learning
    eta: float = 0.0           # retained capacity fraction at full shared learning
    c: float = 1.0             # B learning operating cost per effort-time
    hazard: float = 2.0        # B qualification hazard per effort-time
    rho: float = 1.0           # discount hazard (positive)
    W: float = 4.0             # after-qualification provider net cash flow
    q_floor: float = 0.0       # contractual minimum accepted A output during B learning
    mu: float = 1.0            # specialist qualification hazard, A undisplaced
    c_sp: float = 1.2          # specialist ongoing development/facility rental

    def __post_init__(self):
        if self.K <= 0 or self.d <= 0 or self.rho <= 0 or self.c < 0 or self.hazard < 0 or self.mu <= 0 or self.c_sp < 0:
            raise ValueError('invalid positive/nonnegative parameter')
        if self.m < self.d*self.K or not 0 <= self.eta <= 1 or not 0 <= self.q_floor <= self.K:
            raise ValueError('requires capacity-constrained A demand and admissible qualification/SLA')


def scalars(e: Economy):
    delta = 1-e.eta
    return (e.m*e.K-e.d*e.K**2/2,
            e.K*delta*(e.m-e.d*e.K),
            e.d*e.K**2*delta**2/2)


def max_effort(e: Economy):
    if e.eta == 1:
        return 1.0
    return min(1.0, max(0.0, (1-e.q_floor/e.K)/(1-e.eta)))


def output(e: Economy, u: float):
    if not 0<=u<=max_effort(e)+1e-12:
        raise ValueError('effort violates technical or customer constraint')
    return e.K*(1-(1-e.eta)*u)


def net_a(e: Economy, u: float):
    q = output(e,u)
    return e.m*q-e.d*q*q/2


def shared_value(e: Economy,u: float):
    return (net_a(e,u)-e.c*u+e.hazard*u*e.W/e.rho)/(e.rho+e.hazard*u)


def optimal_shared(e: Economy):
    g0,L,h=scalars(e)
    A=e.hazard*(e.W-g0)-e.rho*(e.c+L)
    cap=max_effort(e)
    if cap==0 or A<=0:
        u=0.0
    elif h==0:
        u=cap
    else:
        # Derivative numerator A-2*rho*h*u-hazard*h*u**2 decreases in u.
        if A >= 2*e.rho*h*cap+e.hazard*h*cap**2:
            u=cap
        else:
            u=(sqrt(e.rho**2+e.hazard*A/h)-e.rho)/e.hazard
    return {'u':u,'value':shared_value(e,u),'no_learning':g0/e.rho,
            'cap':cap,'marginal_at_zero':A,'g0':g0,'L':L,'h':h}


def specialist(e: Economy):
    g0=scalars(e)[0]
    learning=(g0-e.c_sp+e.mu*e.W/e.rho)/(e.rho+e.mu)
    return {'value':max(g0/e.rho,learning),'learn':learning>g0/e.rho}


def penalty_optimized(e: Economy, sla_min: float, penalty: float):
    """Optimal stationary effort if failing an A-output SLA incurs a per-time
    penalty until B qualification (rather than being contractually prohibited).
    The SLA threshold is on accepted complete A service, NOT robot cycles.
    """
    if not 0<=sla_min<=e.K or penalty<0:
        raise ValueError('invalid service threshold or penalty')
    cap=max_effort(e)
    g0,L,h=scalars(e)
    threshold=(1-sla_min/e.K)/(1-e.eta) if e.eta<1 else float('inf')
    no_breach_cap=min(cap,threshold)
    def candidate_at(max_u, p):
        A=e.hazard*(e.W-g0)-e.rho*(e.c+L)+e.hazard*p
        if A<=0: u=0.
        elif h==0: u=max_u
        elif A>=2*e.rho*h*max_u+e.hazard*h*max_u**2: u=max_u
        else: u=(sqrt(e.rho**2+e.hazard*A/h)-e.rho)/e.hazard
        return u
    u0=candidate_at(no_breach_cap,0.)
    best=(shared_value(e,u0),u0,False)
    if threshold<cap:
        u1=max(threshold,candidate_at(cap,penalty))
        # Strictly breaching is required to incur this penalty; if candidate
        # is exactly threshold, no-breach candidate weakly dominates.
        if u1>threshold+1e-13:
            v=shared_value(e,u1)-penalty/(e.rho+e.hazard*u1)
            if v>best[0]: best=(v,u1,True)
    return {'value':best[0], 'u':best[1], 'breaches_sla':best[2]}


def financially_sustainable_effort(e: Economy):
    """Long-run cash-funded effort share with immediate actual receipts,
    divisible shared production and no terminal-qualification premium.
    This is an average-rate bound, *not* the optimal discounted controller.
    """
    g0,L,h=scalars(e)
    if e.c==0: return max_effort(e)
    if h==0:
        root=g0/(L+e.c)
    else:
        root=2*g0/(L+e.c+sqrt((L+e.c)**2+4*h*g0))
        # stable quadratic formula: root = 2*g0/(B+sqrt(B²+4*h*g0))
    return max(0.0,min(max_effort(e),root))


def discrete_shared_value(e:Economy,u:float,dt:float):
    from math import exp
    if dt<=0: raise ValueError('positive dt')
    p=-__import__('math').expm1(-e.hazard*u*dt)
    discount=exp(-e.rho*dt)
    flow=(net_a(e,u)-e.c*u)*dt
    return (flow+discount*p*e.W/e.rho)/(1-discount*(1-p))


def examples():
    e=Economy()
    scenarios={'base':e,'contract_floor':replace(e,q_floor=.9),
               'higher_incumbent_demand':replace(e,m=6,W=6)}
    ret={}
    for k,v in scenarios.items():
        shared=optimal_shared(v); sp=specialist(v)
        ret[k]={'params':vars(v),'shared':shared,'specialist':sp,
                'winner':'shared' if shared['value']>sp['value']+1e-12 else 'specialist',
                'sustainable_duty':financially_sustainable_effort(v)}
    return ret


if __name__=='__main__':
    print(json.dumps(examples(),indent=2,sort_keys=True))
