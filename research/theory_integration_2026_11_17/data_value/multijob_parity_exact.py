#!/usr/bin/env python3
"""Exact, synthetic finite-policy multi-job queue / common law test. No real robot data.

All amounts are normalized NET original-buyer production increments relative to
three old-R dates; this is not money or an empirical estimate.
Run: python3 multijob_parity_exact.py --output multijob_parity_exact_results.json
"""
from __future__ import annotations
from fractions import Fraction as F
from itertools import product, combinations
from pathlib import Path
import json
import argparse

ATOMS = tuple(product((0, 1), repeat=3))  # J: learner incident, H: other-site incident, Y: date-4 original buyer order
POLICIES = ('R_after_P', 'T_wait', 'T_serve')
COST_P = F(1, 8)
SAFE_QUALIFIED_ORDER = F(7, 8) * F(1, 2)  # independent R-action Q and buyer order; date-4 worker is free
G_VALUE = F(5, 8) - F(1, 4)  # licensed grounding; qualified original order probability and cost
E_VALUE = F(7, 8) - F(15, 32)  # extra chassis and independent operator capacity, qualified original buyer order


def law(t: F):
    assert 0 <= t <= 1
    return {atom: t / 4 if sum(atom) % 2 == 0 else (1 - t) / 4 for atom in ATOMS}


def realized_increment(policy: str, atom):
    """Nonanticipative policy's expected-after-R pilot surplus on each latent atom.

    In R_after_P, the complete R-action buyer/qualification product has
    conditional expectation 7/16 under its independent, identically distributed
    exogenous subtable, and old safe t2/t3/t4 service is preserved.
    For T_*: J and H arrive AFTER t2 dispatch, each consumes 1 worker job.
    At date 3 worker clears one outstanding job; a site-2 target if served
    admits another job K=1 AFTER date-3 service. Original Y only arrives at t4.
    """
    j, h, y = atom
    if policy == 'R_after_P':
        # One background incident H clears by t4; the site-3 R-action paid
        # eligibility law is independently specified and identical in both worlds.
        b3 = h
        b4 = max(0, b3 - 1)
        assert b4 == 0
        return -COST_P + SAFE_QUALIFIED_ORDER
    assert policy in ('T_wait', 'T_serve')
    b3 = j + h
    serve_site2 = policy == 'T_serve' and b3 == 0  # t3 order X3=1, Q3=1
    new_k = int(serve_site2)
    b4 = max(0, b3 - 1) + new_k  # CONSERVATION; no independent t4 free-worker coin
    paid_site2_gain = F(1, 2) if serve_site2 else F(0)
    paid_site3_gain = F(y) if b4 == 0 else F(0)  # Q4=1 under T; original Y not seen at t3
    return -COST_P + paid_site2_gain + paid_site3_gain


def value(policy, t):
    return sum((p * realized_increment(policy, atom) for atom, p in law(t).items()), F())


def oracle_p(t):
    return max(value(pi, t) for pi in POLICIES)


def frac(x):
    return str(x.numerator) if x.denominator == 1 else f'{x.numerator}/{x.denominator}'


def run():
    n_checks = 0
    n_grid = 0
    extreme = {}
    for step in range(0, 257):
        t = F(step, 256)
        n_grid += 1
        p = law(t)
        assert sum(p.values()) == 1
        n_checks += 1
        for idx in range(3):
            assert sum(w for a, w in p.items() if a[idx] == 1) == F(1, 2)
            n_checks += 1
        for i, j in combinations(range(3), 2):
            for x, y in product((0, 1), repeat=2):
                assert sum(w for a, w in p.items() if a[i] == x and a[j] == y) == F(1, 4)
                n_checks += 1
        assert sum(w for (j, h, y), w in p.items() if j == 0 and h == 0 and y == 1) == (1 - t) / 4
        n_checks += 1
        assert value('R_after_P', t) == F(5, 16)
        assert value('T_wait', t) == F(1, 8) + t / 4
        assert value('T_serve', t) == t / 2
        n_checks += 3
        assert oracle_p(t) == max(F(5, 16), t / 2)
        n_checks += 1
        # Explicit whole-program values: safe baseline six, G=6+3/8, E=6+13/32.
        assert G_VALUE == F(3, 8) and E_VALUE == F(13, 32)
        assert min(F(5, 16), t / 2) <= oracle_p(t) <= F(1, 2)
        n_checks += 2
        if t in (F(0), F(1, 2), F(5, 8), F(13, 16), F(1)):
            extreme[frac(t)] = {
                'P_increment': frac(oracle_p(t)),
                'G_increment': frac(G_VALUE),
                'E_increment': frac(E_VALUE),
                'P_minus_E': frac(oracle_p(t)-E_VALUE),
                'P_policy_values': {k: frac(value(k, t)) for k in POLICIES},
            }
    assert oracle_p(F(0)) - E_VALUE == -F(3, 32)
    assert oracle_p(F(1)) - E_VALUE == F(3, 32)
    assert oracle_p(F(13, 16)) == E_VALUE
    assert oracle_p(F(5, 8)) == value('R_after_P', F(5, 8)) == value('T_serve', F(5, 8))
    assert value('T_wait', F(1, 2)) == value('T_serve', F(1, 2))
    n_checks += 5
    # Any mixture over the three P policies is <= 5/16 at theta=0,
    # and the pure R_after_P policy achieves 5/16 for all theta.
    assert max(value(k, F(0)) for k in POLICIES) == F(5, 16)
    assert all(value('R_after_P', F(step, 256)) == F(5, 16) for step in range(257))
    n_checks += 2
    assert oracle_p(F(0)) < G_VALUE < E_VALUE < oracle_p(F(1))
    n_checks += 1
    output = {
        'scope': 'conditional synthetic four-date P/G/E comparison; NOT measured robotics return',
        'units': 'normalized full-program accepted customer-production net surplus, relative to baseline 6',
        'latent_bits': ['J_t2_T_incident','H_t2_other_site_incident','Y_t4_original_buyer_order'],
        'law': 'P(J=j,H=h,Y=y)=theta/4 if (j+h+y) even, else (1-theta)/4, theta in [0,1]',
        'pairwise_data': 'All three one-bit marginals fair; all three pairwise bit tables exactly 1/4 per cell for every theta',
        'worker': 'B3=J+H under T; B4=max(0,B3-1)+K, where K=1 only if T_serve at B3=0',
        'policy_increment_formulas': {'P_R_after_pilot': '5/16', 'P_T_wait': '1/8+theta/4', 'P_T_serve': 'theta/2', 'P_oracle': 'max(5/16,theta/2)', 'G':'3/8','E':'13/32'},
        'partial_identification_oracle_P_minus_E': ['-3/32', '+3/32'],
        'robust_fixed_P_without_precommit_report': '5/16 (R_after_P); cannot claim theta-dependent oracle value',
        'robust_E': '13/32, therefore exceeds robust P by 3/32',
        'minimum_theta_for_P_oracle_over_E': 'strictly greater than 13/16',
        'triple_event_P(J=0,H=0,Y=1)': '(1-theta)/4; not identified by any pairwise moments',
        'snapshots': extreme,
        'fraction_grid_points': n_grid,
        'assertions': n_checks,
        'negative_results': ['t2 T_wait never globally optimal when free R_after_P remains available', 'P site-3 technical qualification under T is fixed at 1 across worlds', 'Even fully observed pairwise incident and order tables cannot rank programs'],
        'limitations': ['all payoffs, action kernels and legal rights stipulated', 'independent R/G/E buyer and qualification subtable assumed', 'no real original-buyer offers/cleared settlements', 'not a new general data scaling law', 'not complete repository CI']
    }
    return output


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--output')
    args = parser.parse_args()
    results = run()
    payload = json.dumps(results, indent=2, sort_keys=True) + '\n'
    if args.output:
        Path(args.output).write_text(payload, encoding='utf8')
    else:
        print(payload)
