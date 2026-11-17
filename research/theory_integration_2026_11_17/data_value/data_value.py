"""Data transfer into an optimized production-value table.

Conditional theory, not empirical calibration. Qualification outcomes are
independent conditional on a fixed data/learning configuration in this module.
Uses Python 3.10+ standard library. See DATA_VALUE_THEORY.md for proofs.
"""
from __future__ import annotations

from dataclasses import dataclass
from itertools import product
from math import exp, expm1, isfinite, log1p, sqrt
from pathlib import Path
import argparse
import json


def probability(mask: int, p: tuple[float, ...], excluded: tuple[int, ...] = ()) -> float:
    ans = 1.0
    for i, pi in enumerate(p):
        if i not in excluded:
            ans *= pi if mask & (1 << i) else 1 - pi
    return ans


def expected_value(p: tuple[float, ...], values: tuple[float, ...]) -> float:
    if len(values) != 2 ** len(p) or any(not 0 <= x <= 1 for x in p):
        raise ValueError('One finite value per subset and probabilities in [0,1] required')
    if any(not isfinite(x) for x in values):
        raise ValueError('Values must be finite')
    return sum(probability(mask, p) * v for mask, v in enumerate(values))


def expected_difference(p: tuple[float, ...], values: tuple[float, ...],
                        indices: tuple[int, ...]) -> float:
    """Expected mixed set difference over qualifications outside indices."""
    if len(set(indices)) != len(indices) or not indices or any(i < 0 or i >= len(p) for i in indices):
        raise ValueError('Distinct valid difference indices required')
    flags = sum(1 << i for i in indices)
    answer = 0.0
    for base in range(len(values)):
        if base & flags:
            continue
        difference = 0.0
        for bits in product((0, 1), repeat=len(indices)):
            mask = base | sum(bit << i for bit, i in zip(bits, indices))
            difference += (-1) ** (len(indices) - sum(bits)) * values[mask]
        answer += probability(base, p, indices) * difference
    return answer


@dataclass(frozen=True)
class DataProduction:
    """Rows = qualifications; columns = data sources. Values index bit masks.

    transfer entries are hypothetical marginal effective-exposure rates, not
    source volume shares, data prices, or estimated robot transfer coefficients.
    """
    transfer: tuple[tuple[float, ...], ...]
    baseline: tuple[float, ...]
    values: tuple[float, ...]

    def __post_init__(self):
        m = len(self.transfer)
        if not m or not self.transfer[0] or len(self.baseline) != m or len(self.values) != 2 ** m:
            raise ValueError('Inconsistent dimensions')
        n = len(self.transfer[0])
        if any(len(row) != n for row in self.transfer):
            raise ValueError('Rectangular transfer matrix required')
        inputs = self.baseline + tuple(x for row in self.transfer for x in row)
        if any(not isfinite(x) or x < 0 for x in inputs):
            raise ValueError('Nonnegative finite exposures/transfer required')
        if any(not isfinite(x) for x in self.values):
            raise ValueError('Finite production values required')

    def probabilities(self, data: tuple[float, ...]) -> tuple[float, ...]:
        if len(data) != len(self.transfer[0]) or any(not isfinite(x) or x < 0 for x in data):
            raise ValueError('Nonnegative source exposures of the right dimension required')
        return tuple(-expm1(-d - sum(t*x for t, x in zip(row, data)))
                     for row, d in zip(self.transfer, self.baseline))

    def value(self, data: tuple[float, ...]) -> float:
        return expected_value(self.probabilities(data), self.values)

    def derivatives(self, data: tuple[float, ...]) -> dict:
        p = self.probabilities(data)
        q = tuple(1-x for x in p)
        m, n = len(p), len(data)
        marginal = [expected_difference(p, self.values, (i,)) for i in range(m)]
        interactions = [[0.0 if i == j else expected_difference(p, self.values, (i,j))
                         for j in range(m)] for i in range(m)]
        gradient = [sum(self.transfer[i][s]*q[i]*marginal[i] for i in range(m)) for s in range(n)]
        curvature, complement, exhaustion = [], [], []
        for s in range(n):
            cr, co, ex = [], [], []
            for t in range(n):
                shared = -sum(self.transfer[i][s]*self.transfer[i][t]*q[i]*marginal[i]
                              for i in range(m))
                production = sum(self.transfer[i][s]*self.transfer[j][t]*q[i]*q[j]*interactions[i][j]
                                 for i in range(m) for j in range(m) if i != j)
                cr.append(shared+production); co.append(production); ex.append(shared)
            curvature.append(cr); complement.append(co); exhaustion.append(ex)
        return dict(probabilities=p, conditional_capability_values=marginal,
                    gradient=gradient, hessian=curvature,
                    production_interactions=complement, same_capability_exhaustion=exhaustion)


def _validate_mix(budget: float, transfer: float, incumbent: float, joint: float, kind: str):
    if (not all(isfinite(x) for x in (budget,transfer,incumbent,joint))
        or min(budget,incumbent,joint) < 0 or not 0 <= transfer <= 1
        or kind not in ('exponential','rational')):
        raise ValueError('Invalid mixture parameters')


def mix_value(x: float, budget: float, transfer: float, incumbent: float,
              joint: float, kind: str = 'exponential') -> dict:
    _validate_mix(budget,transfer,incumbent,joint,kind)
    if not 0 <= x <= budget:
        raise ValueError('Source-one exposure must lie in [0,budget]')
    z1 = x + transfer*(budget-x)
    z2 = transfer*x + budget-x
    curve = (lambda z: -expm1(-z)) if kind == 'exponential' else (lambda z: z/(1+z))
    p1, p2 = curve(z1), curve(z2)
    return dict(x=x, y=budget-x, probabilities=[p1,p2],
                value=incumbent*p1+joint*p1*p2, mean_qualification_score=(p1+p2)/2)


def optimal_mix(budget: float, transfer: float, incumbent: float,
                joint: float, kind: str = 'exponential') -> dict:
    """Closed-form GLOBAL optimum for the stated fixed equal-cost budget model."""
    _validate_mix(budget,transfer,incumbent,joint,kind)
    if budget == 0 or transfer == 1 or incumbent == joint == 0:
        x = budget/2  # explicit indifference tie convention
    elif joint == 0:
        x = budget
    elif kind == 'exponential':
        x = min(budget, max(0.0, budget/2 + log1p(incumbent/joint)/(2*(1-transfer))))
    else:
        h = 2+(1+transfer)*budget
        b = joint*(1-1/h)
        a = incumbent+b
        target_z1 = h*sqrt(a)/(sqrt(a)+sqrt(b))-1
        x = min(budget,max(0.0,(target_z1-transfer*budget)/(1-transfer)))
    return mix_value(x,budget,transfer,incumbent,joint,kind)


def grounding_value(source: float, grounding: float, reward: float=1.0) -> dict:
    """Alternative TECHNICAL complementarity, not a production-complement assumption."""
    if min(source,grounding,reward) < 0 or not all(isfinite(x) for x in (source,grounding,reward)):
        raise ValueError('Nonnegative finite inputs required')
    z=source*grounding
    return dict(value=reward*(-expm1(-z)), mixed_derivative=reward*exp(-z)*(1-z))


def results() -> dict:
    model=DataProduction(((1.0,0.25),(0.25,1.0)),(0.0,0.0),(0.0,3.0,0.0,9.0))
    return {
        'status':'Conditional analytical models; all quantities synthetic normalized units',
        'baseline': {'transfer':model.transfer,'baseline':model.baseline,'value_table':model.values,
                     'at_data_0_7_0_4':model.derivatives((0.7,0.4))},
        'demand_conditioned_mixtures': {
            kind: {str((u,v)):optimal_mix(2.0,0.25,u,v,kind)
                   for u,v in ((0.0,6.0),(3.0,6.0),(12.0,3.0))}
            for kind in ('exponential','rational')},
        'greater_transfer_can_concentrate_acquisition': {
            str(e):optimal_mix(2.0,e,3.0,6.0) for e in (0.0,0.25,0.5,0.75,0.9,1.0)},
        'score_vs_value': {'economic':optimal_mix(2.0,0.25,12.0,3.0),
                           'balanced':mix_value(1.0,2.0,0.25,12.0,3.0)},
        'technical_grounding_complement': {
            'early':grounding_value(0.25,0.5), 'late':grounding_value(2.0,1.0)},
        'dependence_warning': {'marginals':[0.5,0.5],
                               'joint_reward':1.0,'independent_value':0.25,
                               'shared_success_value':0.5,'mutually_exclusive_value':0.0}}


if __name__ == '__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,default=Path(__file__).with_name('results.json'))
    args=parser.parse_args()
    args.output.write_text(json.dumps(results(),sort_keys=True,indent=2)+'\n',encoding='utf-8')
    print(f'Wrote {args.output}')
