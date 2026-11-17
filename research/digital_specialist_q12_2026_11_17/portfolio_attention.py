"""Exact synthetic two-service portfolio optimization.

A fully qualified flexible fleet competes with dedicated task capacity, with or
without a digital coordination investment. Shared supervisor attention is a
separate physical constraint. Python 3.10+, standard library only.

Run: python portfolio_attention.py --output results.json
"""
from __future__ import annotations
from dataclasses import dataclass, replace
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
import argparse, json


@dataclass(frozen=True)
class Policy:
    name: str
    cap_a: F
    cap_b: F
    cap_total: F
    attention_a: F
    attention_b: F
    cost: F
    overhead_a: F = F(0)
    overhead_b: F = F(0)
    eligible_a: bool = True
    eligible_b: bool = True
    rights: bool = True

    def __post_init__(self):
        vals=(self.cap_a,self.cap_b,self.cap_total,self.attention_a,
              self.attention_b,self.cost,self.overhead_a,self.overhead_b)
        if min(vals)<0: raise ValueError('Capacities, costs and attention must be nonnegative')


@dataclass(frozen=True)
class Optimum:
    q_a: F
    q_b: F
    surplus: F


def optimize(d_a: F, d_b: F, b: F, H: F, p: Policy) -> Optimum:
    """Exact argmax of separable strictly concave quadratic on polytope.

    Constraints A*q_a+B*q_b <= C. For a strictly concave differentiable
    objective over a nonempty compact 2D polygon, the optimum is interior,
    in the relative interior of one binding line, or at a vertex. Enumerates
    precisely those candidates using rationals; no discretization/gridding.
    """
    if b<=0 or H<0: raise ValueError('Require b>0 and H>=0')
    ca = p.cap_a if p.eligible_a else F(0)
    cb = p.cap_b if p.eligible_b else F(0)
    lines=[(F(-1),F(0),F(0)),(F(0),F(-1),F(0)),
           (F(1),F(0),ca),(F(0),F(1),cb),
           (F(1),F(1),p.cap_total),
           (p.attention_a,p.attention_b,H)]
    ma,mb=d_a-p.overhead_a,d_b-p.overhead_b
    candidates=[(F(0),F(0)),(ma/b,mb/b)]
    # Each line's unconstrained optimum, projected onto the line.
    for a,c,k in lines:
        norm=a*a+c*c
        if norm:
            multiplier=(a*ma+c*mb-b*k)/norm
            candidates.append(((ma-multiplier*a)/b,(mb-multiplier*c)/b))
    # All intersections of two nonparallel supporting lines.
    for (a,c,k),(u,v,w) in combinations(lines,2):
        det=a*v-c*u
        if det:
            candidates.append(((k*v-c*w)/det,(a*w-k*u)/det))
    def feasible(x,y): return all(a*x+c*y<=k for a,c,k in lines)
    def surplus(x,y): return ma*x+mb*y-b*(x*x+y*y)/2
    valid=[(surplus(x,y),x,y) for x,y in candidates if feasible(x,y)]
    assert valid, 'zero output must always be feasible'
    # Ties choose smaller q_A then smaller q_B for reproducibility.
    value,x,y=max(valid,key=lambda z:(z[0],-z[1],-z[2]))
    return Optimum(x,y,value)


@dataclass(frozen=True)
class Environment:
    d_low: F = F(3)
    d_high: F = F(5)
    b: F = F(2)
    capture: F = F(4,5)
    H: F = F(1)
    synchrony: F = F(0)
    budget: F = F(3)

    def __post_init__(self):
        if self.d_high<self.d_low or self.b<=0 or self.H<0 or self.budget<0:
            raise ValueError('Bad demand, curvature, attention or cash')
        if not (0<=self.synchrony<=1 and 0<=self.capture<=1):
            raise ValueError('Synchrony and provider capture are in [0,1]')


FLEX=Policy('qualified_flexible',F(2),F(2),F(2),F(1,2),F(1,2),F(43,20),F(1,10),F(1,10))
DEDICATED=Policy('dedicated_uncoordinated',F(1),F(1),F(2),F(3,4),F(3,4),F(19,10))
COORDINATED=Policy('dedicated_digital',F(1),F(1),F(2),F(2,5),F(2,5),F(43,20))
POLICIES=(FLEX,DEDICATED,COORDINATED)


def states(env:Environment):
    l,h=env.d_low,env.d_high
    s=env.synchrony
    return [('HH',h,h,s/2),('LL',l,l,s/2),
            ('HL',h,l,(1-s)/2),('LH',l,h,(1-s)/2)]


def expected_surplus(env:Environment, p:Policy):
    return sum((prob*optimize(a,b,env.b,env.H,p).surplus
                for _,a,b,prob in states(env)),F(0))


def value(env:Environment,p:Policy):
    if not p.rights or p.cost>env.budget: return None
    return env.capture*expected_surplus(env,p)-p.cost


def compare(env:Environment, policies=POLICIES):
    vs={p.name:value(env,p) for p in policies}
    feasible=[(v,p.name) for p in policies if (v:=vs[p.name]) is not None]
    if not feasible: return {'winner':None,'values':vs}
    # On equal values retain coordinated dedicated, then uncoordinated, before new flexible hardware.
    preference={'dedicated_digital':2,'dedicated_uncoordinated':1,'qualified_flexible':0}
    winner=max(feasible,key=lambda z:(z[0],preference.get(z[1],-1)))[1]
    return {'winner':winner,'values':vs}


def full_capacity_difference(env:Environment):
    """Q11 extension: valid only when F and D fully use 2 and remain interior.

    With H>=max(2*hF,2*hD), and demand conditions detailed in NOTE, the
    difference between flexible and digitally coordinated dedicated profit
    equals the cross-task reallocation dividend, less embodiment overhead and
    net capital cost. It is NOT the generic optimizer for smaller H.
    """
    assert FLEX.attention_a==FLEX.attention_b and COORDINATED.attention_a==COORDINATED.attention_b
    if env.H<max(FLEX.attention_a*FLEX.cap_total,COORDINATED.attention_a*COORDINATED.cap_total):
        raise ValueError('Attention may be binding; use exact optimizer')
    if not (env.d_low-FLEX.overhead_a>=env.b*FLEX.cap_total/2
            and env.d_high-env.d_low<env.b*FLEX.cap_total):
        raise ValueError('Not in stated binding/interior regime')
    delta=env.d_high-env.d_low
    k=FLEX.cap_total
    return (env.capture*((1-env.synchrony)*delta*delta/(4*env.b)
                         -FLEX.overhead_a*k)
            -(FLEX.cost-COORDINATED.cost))


def fraction_json(z):
    if isinstance(z,F): return {'exact':str(z),'decimal':float(z)}
    if isinstance(z,dict):return {k:fraction_json(v) for k,v in z.items()}
    if isinstance(z,(list,tuple)):return [fraction_json(x) for x in z]
    if hasattr(z,'__dataclass_fields__'):return fraction_json(vars(z))
    return z


def results():
    base=Environment()
    out={}
    for tag,env in [('anti_correlated',base),
                    ('synchronous',replace(base,synchrony=F(1))),
                    ('switch_threshold',replace(base,synchrony=F(3,5))),
                    ('tight_attention',replace(base,H=F(4,5))),
                    ('low_cash',replace(base,budget=F(2))),
                    ('weak_capture',replace(base,capture=F(1,10)))]:
        c=compare(env)
        out[tag]={'environment':env,'comparison':c,
                  'state_allocation':{p.name:{state:optimize(a,b,env.b,env.H,p)
                                               for state,a,b,pr in states(env)}
                                      for p in POLICIES}}
        if env.H>=1: out[tag]['closed_form_F_minus_D']=full_capacity_difference(env)
    out['rights_gate_no_digital']=compare(base,(FLEX,DEDICATED,replace(COORDINATED,rights=False)))
    out['eligibility_gate_flex_B']=compare(base,(replace(FLEX,eligible_b=False),DEDICATED,COORDINATED))
    out['lambdas']={str(F(i,10)):compare(replace(base,synchrony=F(i,10))) for i in range(11)}
    return fraction_json(dict(status='Synthetic exact fractional arithmetic, not calibration',
                              policy_definitions=POLICIES,cases=out))


if __name__=='__main__':
    p=argparse.ArgumentParser()
    p.add_argument('--output',type=Path,default=Path(__file__).with_name('results.json'))
    args=p.parse_args()
    args.output.write_text(json.dumps(results(),indent=2,sort_keys=True)+'\n')
    print(f'Wrote {args.output}')
