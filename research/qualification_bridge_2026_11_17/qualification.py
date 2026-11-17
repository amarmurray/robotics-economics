"""Conditional qualification-cost model. No fitted parameters or safety certification.

Python 3.10+, standard library. All demonstration values are synthetic.
Minimize sum(w*x) with sum(floor + (initial-floor)*exp(-rate*x)) <= epsilon.
The constraint is a sufficient union-bound service rule, not an independence claim.
"""
from __future__ import annotations
from dataclasses import dataclass, asdict
from math import exp, log, isfinite, ceil, inf
from pathlib import Path
import argparse
import json


@dataclass(frozen=True)
class Component:
    name: str
    initial: float
    floor: float = 0.0
    rate: float = 1.0
    cost: float = 1.0

    def __post_init__(self):
        if not all(isfinite(v) for v in (self.initial, self.floor, self.rate, self.cost)):
            raise ValueError('Parameters must be finite')
        if not 0 <= self.floor <= self.initial <= 1 or self.rate <= 0 or self.cost <= 0:
            raise ValueError('Require 0<=floor<=initial<=1, rate>0, cost>0')


@dataclass(frozen=True)
class Qualification:
    feasible: bool
    effort: tuple[float, ...]
    residual: tuple[float, ...]
    adaptation_cost: float | None
    verification_cost: float
    total_cost: float | None
    multiplier: float | None
    status: str


def qualify(components: tuple[Component, ...], epsilon: float,
            verification_cost: float = 0.0) -> Qualification:
    """Solve the convex program by its unique positive dual root when needed.

    Returns infeasible when irreducible floors rule out finite effort under
    this conservative criterion. This is not a physical impossibility theorem.
    Zero effort still pays the stated verification/setup cost.
    """
    if not components or not isfinite(epsilon) or not 0 < epsilon < 1:
        raise ValueError('Need components and epsilon in (0,1)')
    if not isfinite(verification_cost) or verification_cost < 0:
        raise ValueError('Verification cost must be finite and nonnegative')
    floors = sum(c.floor for c in components)
    initial = tuple(c.initial for c in components)
    if sum(initial) <= epsilon:
        return Qualification(True, (0.0,)*len(components), initial, 0.0,
                             verification_cost, verification_cost, 0.0, 'no_adaptation')
    allowance = epsilon-floors
    if allowance <= 0:
        return Qualification(False, (), initial, None, verification_cost, None,
                             None, 'floor_blocks_finite_certificate')
    amplitudes = tuple(c.initial-c.floor for c in components)
    weights = tuple(c.cost/c.rate for c in components)

    def remaining(lam: float) -> tuple[float, ...]:
        return tuple(min(a, k/lam) if a else 0.0 for a, k in zip(amplitudes, weights))

    hi = 1.0
    for _ in range(1024):
        if sum(remaining(hi)) <= allowance:
            break
        hi *= 2
        if not isfinite(hi):
            raise ArithmeticError('Dual bracket exceeds floating-point range')
    else:
        raise ArithmeticError('Could not bracket dual root')
    lo = 0.0
    for _ in range(160):
        mid = (lo+hi)/2
        if mid == lo or mid == hi:
            break
        if sum(remaining(mid)) > allowance:
            lo = mid
        else:
            hi = mid
    delta = remaining(hi)  # feasible side of root
    effort = tuple(log(a/d)/c.rate if a else 0.0
                   for a,d,c in zip(amplitudes,delta,components))
    residual = tuple(c.floor+d for c,d in zip(components,delta))
    cost = sum(c.cost*x for c,x in zip(components,effort))
    return Qualification(True, effort, residual, cost, verification_cost,
                         cost+verification_cost, hi, 'optimized')


def fixed_failure_budgets(components: tuple[Component, ...], budgets: tuple[float, ...]) -> float:
    """Cost under separately stipulated failure ceilings, for a comparator."""
    if len(components) != len(budgets) or any(not 0 < d < 1 for d in budgets):
        raise ValueError('Invalid component budgets')
    total = 0.0
    for c,d in zip(components,budgets):
        if c.initial <= d:
            continue
        if d <= c.floor:
            return inf
        total += c.cost/c.rate*log((c.initial-c.floor)/(d-c.floor))
    return total


def zero_failure_trials(required_success: float, alpha: float = .05) -> int:
    """Fixed-n one-sided binomial zero-failure bound, iid held-out trials only.

    Not a mandatory industry standard. No optional stopping or repeated testing.
    """
    if not 0 < required_success < 1 or not 0 < alpha < 1:
        raise ValueError('Probabilities must be in (0,1)')
    n = max(1, ceil(log(alpha)/log(required_success)))
    while alpha**(1/n) < required_success:
        n += 1
    while n > 1 and alpha**(1/(n-1)) >= required_success:
        n -= 1
    return n


PROFILES = {
    'score_rich': (Component('easy', .002), Component('hard', .12, cost=8)),
    'bottleneck_rich': (Component('easy', .08), Component('hard', .05, cost=8)),
}


def experiment() -> dict:
    rows = {}
    for name, profile in PROFILES.items():
        answer = qualify(profile,.02,2)
        rows[name] = dict(components=[asdict(c) for c in profile],
                          mean_component_success=1-sum(c.initial for c in profile)/len(profile),
                          qualification=asdict(answer),
                          fixed_equal_budget_cost=fixed_failure_budgets(profile,(.01,.01)))
    blocked = (Component('first', .1, .015), Component('second', .1, .01))
    return dict(status='Synthetic analytical benchmark; not calibrated service reliability',
                epsilon=.02, profiles=rows,
                floor_example=asdict(qualify(blocked,.02,2)),
                verification={str(p):zero_failure_trials(p) for p in (.9,.95,.99,.999)})


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,default=Path(__file__).with_name('qualification_results.json'))
    args=parser.parse_args()
    args.output.write_text(json.dumps(experiment(),indent=2,sort_keys=True,allow_nan=False)+'\n')
    print(args.output)
