"""Fixed-bundle funding cuts and exact two-payer synthetic decisions."""
from fractions import Fraction as Q
from itertools import product
from pathlib import Path
import hashlib
import json

from model.theory_deployment import rationalize, service


def funding_cuts(cash, obligations, edges):
    cash, obligations = tuple(map(Q, cash)), tuple(map(Q, obligations))
    n = len(cash)
    if n != len(obligations) or any(x < 0 for x in cash+obligations):
        raise ValueError('Invalid payer resources')
    if any(a == b or not (0 <= a < n and 0 <= b < n) or Q(t) < 0
           for (a, b), t in edges.items()):
        raise ValueError('Invalid directed payment capacity')
    cuts = []
    for mask in range(1, 1 << n):
        payers = tuple(i for i in range(n) if mask & (1 << i))
        needed = sum((obligations[i] for i in payers), Q(0))
        available = sum((cash[i] for i in payers), Q(0))
        incoming = sum((Q(t) for (a, b), t in edges.items()
                        if a not in payers and b in payers), Q(0))
        cuts.append(dict(payers=payers, needed=needed, cash=available,
                         incoming=incoming, slack=available+incoming-needed))
    return cuts


def funded(cash, obligations, edges):
    return all(c['slack'] >= 0 for c in funding_cuts(cash, obligations, edges))


def project_choices(name, cash, tau, a=Q(10)):
    cash, tau = tuple(map(Q, cash)), Q(tau)
    customer = service(a, 2, 2, capture=Q(5, 6))
    result = []
    for qualify, commission in product((False, True), repeat=2):
        obligations = (Q(2)*qualify, Q(2)*commission)
        cuts = funding_cuts(cash, obligations, {(0, 1): tau})
        feasible = all(c['slack'] >= 0 for c in cuts)
        transfer = max(Q(0), obligations[1]-cash[1])
        after = (cash[0]-transfer-obligations[0], cash[1]+transfer-obligations[1])
        complete = qualify and commission
        profits = (customer['provider']/2,)*2 if complete else (Q(0), Q(0))
        terminal = tuple(after[i]+profits[i] for i in range(2))
        result.append(dict(deployment=name, qualify=qualify, commission=commission,
                           feasible=feasible, cuts=cuts, transfer=transfer,
                           obligations=obligations, after=after, profits=profits,
                           terminal=terminal, value=sum(terminal),
                           note='Infeasible candidates are arithmetic diagnostics, not executions'))
    return result


def build():
    worlds = {}
    for label, tau in [('no_transfer', Q(0)), ('below_boundary', Q(999, 1000)),
                       ('at_boundary', Q(1)), ('above_boundary', Q(2))]:
        options = project_choices('H', (5, 1), tau)+project_choices('L', (2, 2), tau)
        worlds[label] = dict(tau=tau, options=options,
                             best=max((x for x in options if x['feasible']), key=lambda x:x['value']))
    root = Path(__file__).resolve().parents[1]
    return rationalize(dict(
        status='Synthetic fixed-engineering diagnostic; standard flow theorem, no novelty claim',
        units='Normalized currency and accepted service, two windows, no discount or interest',
        input=dict(cash_H=(5, 1), cash_L=(2, 2), obligations=(2, 2),
                   a=10, b=2, cost=2, capacity=2, capture=Q(5, 6)),
        phase=dict(demand_intercept_bounds=(0,12), transfer_capacity_bounds=(0,2),
                   funding_threshold=Q(2)-Q(1),
                   investment_demand_threshold=Q(2)+Q(2)*Q(2)/2+Q(4)/(Q(5,6)*2),
                   deployment_demand_threshold=Q(2)+Q(2)*Q(2)/2+Q(6)/(Q(5,6)*2),
                   equality_note='Funding equality is feasible; demand equalities give the stated policy ties'),
        customer_contract=service(10, 2, 2, capture=Q(5, 6)), worlds=worlds,
        source_sha256={p:hashlib.sha256((root/p).read_bytes()).hexdigest() for p in (
            'model/qualification_finance.py', 'model/theory_deployment.py',
            'scripts/plot_qualification_finance.py',
            'research/theory/qualification_finance.md')}))


if __name__ == '__main__':
    p = Path(__file__).resolve().parent/'results/qualification_finance.json'
    p.write_text(json.dumps(build(), indent=2, sort_keys=True)+'\n')
    print(p)
