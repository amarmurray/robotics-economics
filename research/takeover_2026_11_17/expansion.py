"""Exact, synthetic investment benchmark; Python 3.10+, standard library only.

Reuses the existing theory's quadratic customer revenue and two-part tariff.
No empirical calibration, continuous execution, or novelty claim is implied.
Run: python expansion.py --output results.json
"""
from __future__ import annotations
from dataclasses import dataclass, replace
from fractions import Fraction as F
from itertools import product
import argparse
import json
from pathlib import Path


@dataclass(frozen=True)
class Market:
    a: F
    b: F
    c: F
    outside_profit: F = F(0)
    capture: F = F(4, 5)

    def __post_init__(self):
        if self.b <= 0 or self.c < 0 or self.outside_profit < 0:
            raise ValueError('Require b>0 and nonnegative costs/outside profit')
        if not 0 <= self.capture <= 1:
            raise ValueError('Capture share must be in [0,1]')

    def service(self, capacity: F) -> tuple[F, F, F]:
        """Return adopted quantity, provider profit, customer profit.

        Customer uses its outside option unless robotic gross operating profit
        exceeds that option. Zero surplus uses the outside option (tie rule).
        Full resource cost is reimbursed contemporaneously; no working-capital
        gap or customer liquidity constraint is modeled in this benchmark.
        """
        if capacity < 0:
            raise ValueError('Capacity cannot be negative')
        q = min(capacity, max(F(0), (self.a - self.c) / self.b))
        gross = (self.a - self.c) * q - self.b * q * q / 2
        surplus = gross - self.outside_profit
        if surplus <= 0:
            return F(0), F(0), self.outside_profit
        return q, self.capture * surplus, self.outside_profit + (1-self.capture)*surplus


@dataclass(frozen=True)
class Technology:
    unit_a: F = F(6)
    unit_b: F = F(3)
    qualification_base: F = F(8)
    qualification_floor: F = F(2)
    transfer: F = F(6)
    tooling_cost: F = F(2)
    tooling_saving_a: F = F(2)
    tooling_saving_b: F = F(1)
    salvage_share: F = F(0)
    installed_a: int = 1

    def __post_init__(self):
        if self.unit_a <= self.tooling_saving_a or self.unit_b <= self.tooling_saving_b:
            raise ValueError('New-unit acquisition costs must stay positive')
        if min(self.qualification_floor, self.transfer, self.tooling_cost,
               self.tooling_saving_a, self.tooling_saving_b) < 0:
            raise ValueError('Costs and savings cannot be negative')
        if self.qualification_base < self.qualification_floor or self.installed_a < 0:
            raise ValueError('Invalid qualification floor or initial fleet')
        if not 0 <= self.salvage_share < 1:
            raise ValueError('Salvage share must be in [0,1)')

    def qualification(self, experience: F) -> F:
        if experience < 0:
            raise ValueError('Experience cannot be negative')
        return max(self.qualification_floor, self.qualification_base - self.transfer*experience)


@dataclass(frozen=True)
class Decision:
    new_a: int
    new_b: int
    tooling: bool
    investment: F
    quantity_a: F
    quantity_b: F
    operating_profit: F
    salvage: F
    gain: F


def optimize(budget: F, experience: F, market_a: Market, market_b: Market,
             tech: Technology = Technology(), allow_tooling: bool = False,
             allow_new: bool = True) -> Decision:
    """Globally enumerate this finite deterministic decision problem.

    Gain is incremental provider value versus keeping the installed A fleet.
    Full upfront acquisition spending is constrained by budget. Unspent cash
    is retained, and new-asset terminal value is included separately.
    Each new unit supplies one qualified accepted-service capacity unit.
    """
    if budget < 0:
        raise ValueError('Budget cannot be negative')
    tech.qualification(experience)  # validate even if no new configuration
    baseline = market_a.service(F(tech.installed_a))[1]
    best = None
    for tool in (False, True) if allow_tooling else (False,):
        ka = tech.unit_a - int(tool)*tech.tooling_saving_a
        kb = tech.unit_b - int(tool)*tech.tooling_saving_b
        for na, nb in product(range(int(budget/ka)+1),
                              range(int(budget/kb)+1) if allow_new else (0,)):
            investment = int(tool)*tech.tooling_cost + ka*na + kb*nb
            if nb:
                investment += tech.qualification(experience)
            if investment > budget:
                continue
            qa, pa, _ = market_a.service(F(tech.installed_a+na))
            qb, pb, _ = market_b.service(F(nb))
            salvage = tech.salvage_share*(ka*na+kb*nb)
            candidate = Decision(na, nb, tool, investment, qa, qb, pa+pb,
                                 salvage, pa+pb-baseline-investment+salvage)
            # At exact value ties prefer less spending, then fewer new units,
            # then no tooling; never silently force adoption at indifference.
            key = lambda d: (d.gain, -d.investment, -d.new_b, -d.new_a, -int(d.tooling))
            if best is None or key(candidate) > key(best):
                best = candidate
    assert best is not None  # retaining the old fleet is always feasible
    return best


A = Market(F(18), F(2), F(2), F(10))
B_LOW = Market(F(12), F(2), F(2), F(2))
B_HIGH = replace(B_LOW, a=F(20))
SOURCES = {
    'cash_rich': (Market(F(13), F(2), F(2)), F(0)),
    'transfer_rich': (Market(F(21,2), F(2), F(2)), F(1)),
}


def choose_source(market_b: Market = B_HIGH, tech: Technology = Technology(),
                  allow_tooling: bool = False, allow_new: bool = True,
                  initial_cash: F = F(4)):
    rows = {}
    for name, (market, target_experience_per_output) in SOURCES.items():
        q0, collected_cash, _ = market.service(F(1))
        experience = target_experience_per_output*q0
        d = optimize(initial_cash+collected_cash, experience, A, market_b,
                     tech, allow_tooling, allow_new)
        rows[name] = dict(source_quantity=q0, source_cash=collected_cash,
                          target_experience=experience,
                          budget=initial_cash+collected_cash,
                          decision=d, added_value=collected_cash+d.gain)
    winner = max(rows, key=lambda name: rows[name]['added_value'])
    return dict(winner=winner, paths=rows)


def incumbent_gain(budget: F, tech: Technology = Technology()) -> F:
    return optimize(budget, F(1), A, B_LOW, tech, allow_new=False).gain


def jsonable(x):
    if isinstance(x, F):
        return {'exact': str(x), 'decimal': float(x)}
    if hasattr(x, '__dataclass_fields__'):
        return {k: jsonable(v) for k, v in x.__dict__.items()}
    if isinstance(x, dict):
        return {str(k): jsonable(v) for k, v in x.items()}
    if isinstance(x, (tuple, list)):
        return [jsonable(v) for v in x]
    return x


def results():
    tech = Technology()
    cases = {
        'base': choose_source(),
        'no_transfer': choose_source(tech=replace(tech, transfer=F(0))),
        'weaker_target_demand': choose_source(market_b=B_LOW),
        'fixed_embodiment': choose_source(allow_new=False),
        'manufacturing_tooling_available': choose_source(allow_tooling=True),
        'salvage_25_percent': choose_source(tech=replace(tech, salvage_share=F(1,4))),
        'ample_initial_cash': choose_source(initial_cash=F(100)),
    }
    return jsonable(dict(
        status='Synthetic exact benchmark, not empirical estimates or a novelty claim',
        market_a=A, market_b_base=B_HIGH, market_b_low=B_LOW, technology=tech,
        source_definitions=SOURCES, source_comparisons=cases,
        nonmonotone_entry={str(b): optimize(F(b), F(1), A, B_LOW) for b in (5,6,11)},
        mechanism='Full-value comparison of deployment, expansion, qualification, tooling and retained cash',
    ))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=Path(__file__).with_name('results.json'))
    args = parser.parse_args()
    args.output.write_text(json.dumps(results(), indent=2, sort_keys=True)+'\n')
    print(f'Wrote {args.output}')
