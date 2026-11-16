"""Exact, synthetic two-period diagnostic; not an empirical enterprise engine."""
from dataclasses import dataclass, replace
from fractions import Fraction as Q
from pathlib import Path
import hashlib
import json
import math


@dataclass(frozen=True)
class Application:
    name: str
    cash: Q
    a: Q
    cost: Q


def service(a, cost, capacity, b=Q(2), outside=Q(0), capture=Q(4, 5)):
    a, cost, capacity, b, outside, capture = map(
        Q, (a, cost, capacity, b, outside, capture))
    if capacity < 0 or b <= 0 or outside < 0 or not 0 <= capture <= 1:
        raise ValueError("Invalid service domain")
    q = min(capacity, max(Q(0), (a-cost)/b))
    gross = (a-cost)*q-b*q*q/2
    # If the alternative dominates, no robotic service is purchased.
    if gross < outside:
        return dict(q=Q(0), gross=gross, surplus=Q(0), provider=Q(0),
                    customer=outside, fee=Q(0), resource=Q(0), revenue=Q(0))
    surplus = gross-outside
    resource = cost*q
    fee = resource+capture*surplus
    revenue = a*q-b*q*q/2
    return dict(q=q, gross=gross, surplus=surplus, provider=capture*surplus,
                customer=revenue-fee, fee=fee, resource=resource, revenue=revenue)


def choices(app, credit=Q(0), initial=Q(0), investment=Q(3), capacity=Q(1),
            increment=Q(1), b=Q(2), capture=Q(4, 5), outside=Q(0)):
    credit, initial, investment, capacity, increment = map(
        Q, (credit, initial, investment, capacity, increment))
    if min(credit, initial, investment, capacity, increment, app.cash) < 0:
        raise ValueError("Nonnegative resources required")
    result = []
    for expand in (False, True):
        spend = investment if expand else Q(0)
        loan = max(Q(0), spend-initial-app.cash)
        s = service(app.a, app.cost, capacity+increment*expand, b, outside, capture)
        after_investment = initial+app.cash+loan-spend
        terminal = after_investment+s['provider']-loan
        feasible = loan <= credit and terminal >= 0
        result.append(dict(application=app.name, expand=expand, loan=loan,
                           investment=spend, after_investment=after_investment,
                           terminal=terminal, value=terminal-initial,
                           feasible=feasible, service=s))
    return result


def best(apps, **kwargs):
    candidates = [c for app in apps for c in choices(app, **kwargs) if c['feasible']]
    return max(candidates, key=lambda c: c['value'])


def source_output(m, competence=1.8, coordination=.75, phi=1.75):
    return m*competence*math.exp(phi*m/(1+m))*(1+m)**(coordination-1)


def rationalize(obj):
    if isinstance(obj, Q):
        return str(obj)
    if isinstance(obj, dict):
        return {k: rationalize(v) for k, v in obj.items()}
    if isinstance(obj, (list, tuple)):
        return [rationalize(v) for v in obj]
    return obj


def build():
    h = Application('H', Q(8), Q(8), Q(4))
    low = Application('L', Q(2), Q(12), Q(2))
    worlds = {
        'no_credit': ([h, low], Q(0)),
        'bridge_credit': ([h, low], Q(1)),
        'no_learning': ([h, replace(low, cost=Q(4))], Q(1)),
        'no_access': ([h, replace(low, a=Q(8))], Q(1)),
    }
    root = Path(__file__).resolve().parents[1]
    return rationalize({
        'status': 'synthetic exact diagnostic; no calibration or novelty claim',
        'units': 'normalized service and currency; two windows; beta=1',
        'parameters': dict(b=Q(2), capacity=Q(1), increment=Q(1),
                           investment=Q(3), capture=Q(4, 5), initial=Q(0), outside=Q(0)),
        'worlds': {name: {
            'credit': credit,
            'applications': [vars(a) for a in apps],
            'choices': [c for a in apps for c in choices(a, credit=credit)],
            'best': best(apps, credit=credit),
        } for name, (apps, credit) in worlds.items()},
        'source_example': {
            'optimal_continuous_size': 6,
            'six_coders': source_output(6),
            'twelve_coders_one_firm': source_output(12),
            'twelve_coders_two_firms': 2*source_output(6),
            'meaning': 'Selected source arithmetic, not equilibrium replication',
        },
        'source_sha256': {
            p: hashlib.sha256((root/p).read_bytes()).hexdigest()
            for p in ('model/theory_deployment.py', 'research/theory/deployment_investment.md',
                      'research/theory/organizing_intelligence.md')
        },
    })


if __name__ == '__main__':
    path = Path(__file__).resolve().parent/'results/theory_deployment.json'
    path.write_text(json.dumps(build(), indent=2, sort_keys=True)+'\n')
    print(path)
