"""Q4 exact finite-source supervision benchmark; Python >=3.10, stdlib only.

Synthetic stationary CTMC: each *working* robot asks for intervention at rate
lambda, each of c supervisors resolves at exponential rate mu; interrupted
robots cannot create new requests. The stationary mean is an expected rate,
not a finite-window service guarantee, observed fleet uptime or queue tail.
"""
from __future__ import annotations
from dataclasses import dataclass, replace
from fractions import Fraction as F
from itertools import product
import json


def stationary(n: int, arrival: F, resolution: F, supervisors: int=1) -> tuple[F, ...]:
    """Exact stationary fractions indexed by number of interrupted robots."""
    if not isinstance(n, int) or n < 0 or not isinstance(supervisors, int) or supervisors < 1:
        raise ValueError('Require n>=0 integer and supervisors>=1 integer')
    if arrival < 0 or resolution <= 0:
        raise ValueError('Require arrival>=0 and resolution>0')
    w = [F(1)]
    for k in range(1, n + 1):
        w.append(w[-1] * (n - k + 1) * arrival / (min(k, supervisors)*resolution))
    z = sum(w)
    return tuple(x/z for x in w)


def effective_capacity(n: int, arrival: F, resolution: F=F(1),
                       supervisors: int=1, rate: F=F(1)) -> F:
    """Long-run output capacity per unit time, in accepted-output units/time."""
    if rate < 0:
        raise ValueError('Rate must be nonnegative')
    pi=stationary(n,arrival,resolution,supervisors)
    active = F(n) - sum(F(k)*v for k,v in enumerate(pi))
    return rate*active


@dataclass(frozen=True)
class Market:
    a: F
    b: F
    resource_cost: F
    outside_profit: F=F(0)
    capture: F=F(4,5)

    def __post_init__(self):
        if self.b <= 0 or min(self.resource_cost, self.outside_profit) < 0:
            raise ValueError('Require b>0, nonnegative cost/outside')
        if not 0 <= self.capture <= 1:
            raise ValueError('Invalid capture share')

    def outcome(self, capacity: F) -> tuple[F,F,F]:
        """Adopted q, provider operating profit, customer's operating profit.

        Revenue aq-bq^2/2; cost c*q, plus an explicit outside option.
        This is customer monopoly quantity, not industry competition.
        """
        if capacity < 0: raise ValueError('Negative qualified capacity')
        q = min(capacity, max(F(0), (self.a-self.resource_cost)/self.b))
        gross = (self.a-self.resource_cost)*q - self.b*q*q/2
        if gross <= self.outside_profit:
            return F(0),F(0),self.outside_profit
        incremental = gross-self.outside_profit
        return q,self.capture*incremental,self.outside_profit+(F(1)-self.capture)*incremental


@dataclass(frozen=True)
class Operations:
    robots: int=4
    incident_rate: F=F(1,2)
    repair_rate: F=F(1)
    supervisors: int=1
    work_rate: F=F(1)
    digital_rate_factor: F=F(1,2)  # target arrival multiplier with digital triage
    hardware_cost: F=F(3)
    digital_cost: F=F(3)
    supervisor_cost: F=F(5)
    budget: F=F(6)

    def __post_init__(self):
        stationary(self.robots,self.incident_rate,self.repair_rate,self.supervisors)
        if self.work_rate <= 0 or not 0 < self.digital_rate_factor <= 1:
            raise ValueError('Require positive work rate and digital factor in (0,1]')
        if min(self.hardware_cost, self.digital_cost, self.supervisor_cost, self.budget) < 0:
            raise ValueError('Costs/budget must be nonnegative')


@dataclass(frozen=True)
class Choice:
    hardware: int
    digital: int
    additional_supervisor: int
    outlay: F
    effective_capacity: F
    quantity: F
    provider_operating_profit: F
    customer_operating_profit: F
    gain: F


def enumerate_choices(ops: Operations, market: Market) -> list[Choice]:
    baseline=effective_capacity(ops.robots,ops.incident_rate,ops.repair_rate,
                                ops.supervisors,ops.work_rate)
    prior=market.outcome(baseline)[1]
    out=[]
    for hardware,digital,added in product((0,1),repeat=3):
        outlay=hardware*ops.hardware_cost+digital*ops.digital_cost+added*ops.supervisor_cost
        if outlay>ops.budget: continue
        K=effective_capacity(ops.robots+hardware,ops.incident_rate*(ops.digital_rate_factor if digital else 1),
                             ops.repair_rate,ops.supervisors+added,ops.work_rate)
        q,provider,customer=market.outcome(K)
        out.append(Choice(hardware,digital,added,outlay,K,q,provider,customer,
                          provider-prior-outlay))
    return out


def optimal(ops: Operations, market: Market) -> Choice:
    """Maximum incremental private value; ties prefer retained capital."""
    return max(enumerate_choices(ops,market), key=lambda d:(d.gain,-d.outlay,-d.hardware,-d.digital,-d.additional_supervisor))


def cross_effects(ops: Operations, market: Market) -> dict:
    """Interaction from hardware + digital; cost terms cancel if additive."""
    if ops.budget < ops.hardware_cost+ops.digital_cost:
        ops=replace(ops,budget=ops.hardware_cost+ops.digital_cost)
    rows={(d.hardware,d.digital):d for d in enumerate_choices(ops,market) if d.additional_supervisor==0}
    h=rows[1,0];d=rows[0,1];both=rows[1,1];base=rows[0,0]
    return dict(physical=both.effective_capacity-d.effective_capacity-h.effective_capacity+base.effective_capacity,
                operating=both.provider_operating_profit-d.provider_operating_profit-h.provider_operating_profit+base.provider_operating_profit,
                private=both.gain-d.gain-h.gain+base.gain)


def binding_interaction_threshold(ops: Operations, market: Market) -> tuple[F, F, F]:
    """Return capacity cross, demand-margin threshold and max required binding margin.

    For provider profit rho * ((a-c)K-b*K^2/2-Pi0) with adoption and
    capacity binding at all four regimes, joint cross-effect changes sign
    when d=(b/2)*cross(K^2)/cross(K), assuming cross(K)>0.
    This is NOT applicable if demand saturates or an outside option binds.
    """
    K0=effective_capacity(ops.robots,ops.incident_rate,ops.repair_rate,ops.supervisors,ops.work_rate)
    KH=effective_capacity(ops.robots+1,ops.incident_rate,ops.repair_rate,ops.supervisors,ops.work_rate)
    KD=effective_capacity(ops.robots,ops.incident_rate*ops.digital_rate_factor,ops.repair_rate,ops.supervisors,ops.work_rate)
    KHD=effective_capacity(ops.robots+1,ops.incident_rate*ops.digital_rate_factor,ops.repair_rate,ops.supervisors,ops.work_rate)
    cross=KHD-KD-KH+K0
    if cross <= 0:
        raise ValueError('Positive physical complementarity required for this threshold')
    sqcross=KHD*KHD-KD*KD-KH*KH+K0*K0
    return cross,market.b*sqcross/(2*cross), market.b*max(K0,KH,KD,KHD)


def exact_results():
    base=Operations()
    deep=Market(F(18),F(2),F(2),F(5))
    scenarios={
      'low_incident':(replace(base,incident_rate=F(1,10)),deep),
      'high_incident':(base,deep),
      'deep_demand_saturated':(base,Market(F(5),F(2),F(2),F(0))),
      'higher_supervision_cost':(replace(base,supervisor_cost=F(10)),deep),
      'digital_inactive':(replace(base,digital_rate_factor=F(1)),deep),
      'customer_retains_most_value':(base,replace(deep,capture=F(1,10))),
    }
    comparison={key:dict(best=optimal(o,m),alternatives=enumerate_choices(o,m)) for key,(o,m) in scenarios.items()}
    complementary=Operations(robots=3,incident_rate=F(1,2),budget=F(6))
    low_d=Market(F(31,4),F(2),F(2),F(0)) # d=23/4, all four capacities binding
    high_d=Market(F(10),F(2),F(2),F(0)) # d=8, all four capacities binding
    return dict(classification='exact synthetic CTMC & customer demand; not calibrated',
      mechanism='fleet hardware, digital intervention reduction, extra human supervisor versus funds',
      scenarios=comparison,
      interaction=dict(low_demand=cross_effects(complementary,low_d),high_demand=cross_effects(complementary,high_d), binding_threshold=binding_interaction_threshold(complementary,low_d)),
      ceiling_examples={str(n):effective_capacity(n,F(1,2)) for n in (4,8,12,24,48)},
      zero_incident=effective_capacity(5,F(0)),
      current_source='Serve Robotics 2025 10-K; Agility FAQ; Hoque et al PMLR 2022')


def encode(v):
    if isinstance(v,F):return {'fraction':str(v),'float':float(v)}
    if hasattr(v,'__dataclass_fields__'):return {k:encode(x) for k,x in v.__dict__.items()}
    if isinstance(v,dict):return {str(k):encode(x) for k,x in v.items()}
    if isinstance(v,(tuple,list)):return [encode(x) for x in v]
    return v


if __name__=='__main__':
    from pathlib import Path
    import argparse
    parser=argparse.ArgumentParser()
    parser.add_argument('--output',type=Path,default=Path(__file__).with_name('results.json'))
    args=parser.parse_args()
    args.output.write_text(json.dumps(encode(exact_results()),indent=2,sort_keys=True)+'\n')
    print(args.output)
