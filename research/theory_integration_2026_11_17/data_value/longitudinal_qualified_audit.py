#!/usr/bin/env python3
"""Exact synthetic 3-date qualified paid-service, learner and queue audit.
No empirical observations, customer prices or robotics claims. Python >=3.9.
"""
from fractions import Fraction as F
from itertools import product
from math import comb
import json

ARMS = ('P', 'G', 'E')  # source pilot, licensed grounding, independent embodiment
POLICIES = ('retain', 'adaptive', 'probe')
ALLOWED = {'P': ('retain', 'adaptive'), 'G': POLICIES, 'E': ('retain', 'adaptive')}
# Legal scope: P production-only; G has licensed deliberate validation;
# E adds an independent resource but has no deliberate target-probe right.
# Non-G program trials require an AUDITED original buyer and qualified learner;
# the logged action cannot know an unaudited offer ex ante.
PAIRS = tuple(product((0, 1), repeat=2))
COST = {'P': F(1, 8), 'G': F(1, 5), 'E': F(1, 4)}

def pre(a, z, w):
    return (z if a == 'P' else 1, w if a == 'P' else 0,
            z if a == 'P' else w)  # learner L, first job J1, original buyer Y1

def action(k, a, z, w):
    L, J1, Y1 = pre(a, z, w)
    if k == 'retain': return 'R'
    if k == 'probe': return 'T' if not J1 else 'R'
    return 'T' if L and not J1 and Y1 else 'R'

def production(a, b, z, w):
    L, J1, Y1 = pre(a, z, w)
    assert b == 'R' or J1 == 0  # connected worker physically available
    # T can create learner qualification and follow-on original customer demand.
    J2 = int(b == 'T' and z == 0 and w == 1 and a != 'E')
    Q3 = int(bool(L or (b == 'T' and w == 0)))
    Y3 = int(bool((z or w or (b == 'T' and w == 0)) if a != 'G'
                  else (w or (b == 'T' and z == 0))))
    early = F(1, 2) if b == 'T' and L and Y1 else F(0)
    later = F(1) if Q3 and Y3 and not J2 else F(0)
    return early + later - COST[a], J2

def report1(j): return F(1, 4) if j else F(1, 2)
def report2(j): return F(1, 4) if j else F(1, 2)
def choose_t(arm, s1, y1, j1, l):
    if j1: return F(0)
    if arm != "G" and not (s1 and y1 and l): return F(0)
    return F(3,4) if s1 and y1 else F(1,4)

def evaluate(a, policy, law):
    """Return exact true, IPW and optimally no-need-to-audit terminal-zero value."""
    truth = weighted = efficient = m1 = m2 = naive_mass = naive_sum = F(0)
    for (z, w), pzw in zip(PAIRS, law):
        if not pzw: continue
        target = action(policy, a, z, w)
        v, _ = production(a, target, z, w)
        truth += pzw * v
        L, J1, Y1 = pre(a, z, w)
        rho1 = report1(J1)
        for s1 in (0, 1):
            ps1 = rho1 if s1 else 1-rho1
            et = choose_t(a, s1, Y1, J1, L)
            for b in ('R', 'T'):
                eb = et if b == 'T' else 1-et
                if not eb: continue
                value, J2 = production(a, b, z, w)
                rho2 = report2(J2)
                for s2 in (0, 1):
                    ps2 = rho2 if s2 else 1-rho2
                    log_p = pzw * F(1, 3) * ps1 * eb * ps2
                    if s1 and s2 and b == target:
                        est = value/(F(1, 3)*rho1*eb*rho2)
                        weighted += log_p*est
                        m1 += log_p*est**2
                        naive_sum += log_p*value
                        naive_mass += log_p
                    if s1 and b == target and (s2 or J2):
                        # On J2=1, t3 paid service=0 by known queue constraint.
                        # Y3 need not be reported to score *this* finite horizon.
                        factor = F(1) if J2 else rho2
                        est2 = value/(F(1, 3)*rho1*eb*factor)
                        efficient += log_p*est2
                        m2 += log_p*est2**2
    assert truth == weighted == efficient
    assert m2 <= m1
    return dict(true=truth, ipw=weighted, reduced=efficient,
                naive=naive_sum/naive_mass if naive_mass else None,
                second_moment=m1, reduced_second_moment=m2)

def fmt(f):return None if f is None else f'{f.numerator}/{f.denominator}'

def run():
    family = []
    # Every integer four-cell law with denominator 8: includes correlated,
    # degenerate and non-positivity-of-latent-type cases (action support remains).
    for a in range(9):
      for b in range(9-a):
       for c in range(9-a-b):
        d=8-a-b-c
        family.append(tuple(F(k,8) for k in (a,b,c,d)))
    assert len(family)==comb(11,3)==165
    checks=0
    for law in family:
      for arm in ARMS:
       for policy in ALLOWED[arm]:
        o=evaluate(arm,policy,law)
        assert o['true']==o['ipw']==o['reduced'];checks+=2
        assert o['reduced_second_moment']<=o['second_moment'];checks+=1
    baseline=[F(1,4)]*4
    values={arm:{p:{k:fmt(v) for k,v in evaluate(arm,p,baseline).items()}
                 for p in ALLOWED[arm]} for arm in ARMS}
    g=evaluate('G','probe',baseline);e=evaluate('E','adaptive',baseline)
    assert g['true']==F(11,20)<e['true']==F(3,4)
    assert g['naive']==F(99,130)>e['naive']==F(19,28)
    assert max(evaluate('G',p,baseline)['true'] for p in ALLOWED['G'])==F(11,20)
    assert max(evaluate('E',p,baseline)['true'] for p in ALLOWED['E'])==F(3,4)
    assert max(evaluate('P',p,baseline)['true'] for p in ALLOWED['P'])==F(1,2)
    assert max(evaluate('G',p,baseline)['naive'] for p in ALLOWED['G'])>max(evaluate('E',p,baseline)['naive'] for p in ALLOWED['E'])
    assert g['second_moment']-g['reduced_second_moment']==F(27,50)
    return dict(model='synthetic 3-date connected learner/order/operator',
                integer_laws=len(family),exact_assertions=checks+9,
                policies=values,
                inversion='Selected matched logs falsely rank lawful G above E; full original-buyer menu E > G > P',
                status='exact conditional model, not robotics evidence')
if __name__=='__main__':print(json.dumps(run(),sort_keys=True,indent=2))
