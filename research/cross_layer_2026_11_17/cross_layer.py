"""Q7: exact synthetic manufacturer–field–customer learning and capital allocation.

Reuses the quadratic final-demand and surplus-share benchmark. The three stocks
are independent primitives. No observed robotic cost or transfer coefficients.
Python 3.10+ standard library. Run python cross_layer.py.
"""
from dataclasses import dataclass
from fractions import Fraction as F

import json
from pathlib import Path


@dataclass(frozen=True)
class Market:
    a: F
    b: F = F(2)
    c: F = F(3)
    outside: F = F(2)
    capture: F = F(4, 5)

    def service(self, capacity: F) -> tuple[F, F, F]:
        if self.b <= 0 or capacity < 0 or not F(0) <= self.capture <= F(1) or self.outside < 0:
            raise ValueError("invalid market")
        q = min(capacity, max(F(0), (self.a - self.c) / self.b))
        gross = (self.a - self.c) * q - self.b * q * q / 2
        if gross <= self.outside:
            return F(0), F(0), self.outside
        surplus = gross - self.outside
        return q, self.capture * surplus, self.outside + (1-self.capture)*surplus


@dataclass(frozen=True)
class Source:
    name: str
    source_intercept: F
    manufacturer_experience: F
    field_experience: F
    customer_access: F

    def cash(self) -> F:
        # Actual current net provider receipts, not a bonus assigned to data.
        return Market(self.source_intercept, c=F(2), outside=F(0)).service(F(1))[1]


SOURCES = (
    Source("factory", F(37, 4), F(2), F(0), F(0)),
    Source("field", F(8), F(0), F(2), F(1)),
    Source("hybrid", F(27, 4), F(1), F(1), F(2)),
    Source("none", F(2), F(0), F(0), F(0)),
)


@dataclass(frozen=True)
class Contracts:
    pass_through: F = F(1)
    field_reuse_right: F = F(1)
    access_effect: F = F(2)
    target_base_intercept: F = F(12)

    def __post_init__(self):
        if not F(0) <= self.pass_through <= F(1):
            raise ValueError("invalid pass-through fraction")
        if not F(0) <= self.field_reuse_right <= F(1) or self.access_effect < 0 or self.target_base_intercept < 0:
            raise ValueError("invalid reuse/access fraction")


@dataclass(frozen=True)
class Outcome:
    source: str
    current_cash: F
    investment_budget: F
    manufacturer_experience: F
    field_experience: F
    customer_access: F
    target_price: F
    target_resource_cost: F
    target_qualification: F
    target_investment: F
    potential_target_quantity: F
    target_provider_profit: F
    target_customer_profit: F
    action: str
    provider_gain: F
    provider_total: F
    supplier_margin_on_target: F
    terminal_cash: F


def evaluate(source: Source, contracts: Contracts = Contracts(), *, initial_cash: F = F(7)) -> Outcome:
    """Fixed incumbent option vs one S investment, exact fractions.

    The existing-fleet expansion is a separate alternative with cost six and
    an incremental provider profit of 52/5, hence net 22/5. It is available
    from the same starting resources, but cannot coexist with S in this
    deliberately one-investment first benchmark.
    """
    if initial_cash < 0:
        raise ValueError("negative starting cash")
    m = source.cash()
    budget = initial_cash + m
    X, L, C = source.manufacturer_experience, source.field_experience, source.customer_access
    price = F(8) - F(3) * contracts.pass_through * X
    real_cost = F(7) - F(3) * X
    qual = F(7) - F(3) * contracts.field_reuse_right * L
    investment = price + qual
    target_market = Market(contracts.target_base_intercept + contracts.access_effect * C)
    prospective_q, target_profit, customer_profit = target_market.service(F(2))
    incumbent_gain = F(22, 5)
    choices = [("retain", F(0), F(0))]
    if budget >= F(6):
        choices.append(("expand_incumbent", incumbent_gain, F(6)))
    if budget >= investment:
        choices.append(("enter_specialist", target_profit-investment, investment))
    # Prefer incumbent over speculative specialist at exact ties.
    action, gain, spending = max(choices, key=lambda x: (x[1], -int(x[0] == "enter_specialist"), -x[2]))
    supplier = F(1) + F(3) * (F(1) - contracts.pass_through) * X if action == "enter_specialist" else F(0)
    terminal_cash = budget-spending + (target_profit if action == "enter_specialist" else F(52, 5) if action == "expand_incumbent" else F(0))
    return Outcome(source.name, m, budget, X, L, C, price, real_cost,
                   qual, investment, prospective_q, target_profit, customer_profit, action,
                   gain, m + gain, supplier, terminal_cash)


def portfolio(contracts: Contracts = Contracts(), *, initial_cash: F = F(7)) -> tuple[str, dict[str, Outcome]]:
    outcomes = {s.name: evaluate(s, contracts, initial_cash=initial_cash) for s in SOURCES}
    # Exact preference ties favor current-cash-rich source to avoid forced data bets.
    best = max(SOURCES, key=lambda s: (outcomes[s.name].provider_total, outcomes[s.name].current_cash))
    return best.name, outcomes


def _jsonable(obj):
    if isinstance(obj, F):
        return {"exact": str(obj), "decimal": float(obj)}
    if hasattr(obj, "__dataclass_fields__"):
        return {k: _jsonable(v) for k, v in vars(obj).items()}
    if isinstance(obj, dict):
        return {k: _jsonable(v) for k, v in obj.items()}
    if isinstance(obj, (list, tuple)):
        return [_jsonable(i) for i in obj]
    return obj


def run():
    cases = {
        "all_channels": Contracts(),
        "no_manufacturer_pass_through": Contracts(pass_through=F(0)),
        "no_field_reuse_right": Contracts(field_reuse_right=F(0)),
        "no_customer_access_effect": Contracts(access_effect=F(0)),
        "joint_rights_near_boundary": Contracts(pass_through=F(4, 5), field_reuse_right=F(1)),
        "joint_rights_just_above_boundary": Contracts(pass_through=F(81, 100), field_reuse_right=F(1)),
        "joint_rights_financeable_not_preferred": Contracts(pass_through=F(7, 10), field_reuse_right=F(1)),
    }
    return {
        "claim_status": "Synthetic conditional analytical results; no calibration or novelty claim",
        "inputs": _jsonable({"initial_cash": F(7), "sources": SOURCES, "contracts": cases}),
        "cases": {name: _jsonable({"winner": portfolio(c)[0], "outcomes": portfolio(c)[1]}) for name,c in cases.items()},
        "target_demand_grid": [
            _jsonable({"base_intercept": F(a), "winner": portfolio(Contracts(target_base_intercept=F(a)))[0],
                       "hybrid_action": portfolio(Contracts(target_base_intercept=F(a)))[1]["hybrid"].action,
                       "hybrid_potential_output": portfolio(Contracts(target_base_intercept=F(a)))[1]["hybrid"].potential_target_quantity})
            for a in range(0, 19)
        ],
        "supplier_pass_through_grid": [
            _jsonable({"kappa": F(i,100), "winner": portfolio(Contracts(pass_through=F(i,100)))[0],
                       "specialist_supplier_margin":portfolio(Contracts(pass_through=F(i,100)))[1]["hybrid"].supplier_margin_on_target})
            for i in range(0,101)
        ],
    }


if __name__ == "__main__":
    target = Path(__file__).with_name("results.json")
    target.write_text(json.dumps(run(), indent=2, sort_keys=True) + "\n")
    print("Wrote", target)

