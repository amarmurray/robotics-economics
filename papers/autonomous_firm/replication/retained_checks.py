"""Exact finite test of retaining a portable diagnostic in Python 3.

One source regime chooses J uniformly from three candidates once. At each site
three independent fair bits are visible. A paid source label reveals the bit
of J. The rule keeps candidates matching past sources. At a fresh target, it
sees the bits and the known forgone compute contribution, then commits to the
local baseline (increment zero) or pooled training (+9 for eligibility, -3
otherwise, including the stipulated loss on an unsuccessful/refunded outcome,
before subtracting forgone compute). The -3 is net of any refund; no second
refund is debited. No target label is visible
before commitment. One future target in the objective. Source operating
contribution is common; 0.15 or 0.30 per source label is incremental.

Nominal transfer keeps J across sites. In a stress test the target draws a
fresh independent J from all three while the firm uses its frozen source rule.
The oracle knows the target J, and an informed stochastic controller with
identical evidence can implement the same posterior policy as our rule.
"""
from collections import defaultdict
from fractions import Fraction as F
from functools import lru_cache
from itertools import product
from math import comb
import json

LOCAL, POOL = False, True
FEATURES = 3
MAX_LABELS = 5


def target_return(surviving, compute_values, shift=False):
    """Sum over observable target bits, avoiding access to the true label."""
    total = F(0)
    for bits in product(range(2), repeat=FEATURES):
        posterior = F(sum(bits[:surviving]), surviving)
        actual = F(sum(bits), FEATURES) if shift else posterior
        for cost in compute_values:
            take = 12 * posterior - 3 - cost > 0
            if take:
                total += 12 * actual - 3 - cost
    return total / (2**FEATURES * len(compute_values))


def future_sizes(k, n=1):
    """Each false candidate agrees independently across n paid labels."""
    p = F(1, 2**n)
    return [(1+j, comb(k-1,j)*p**j*(1-p)**(k-1-j)) for j in range(k)]


def fixed(n, compute_values, label_cost, shift=False):
    return sum(p * target_return(k, compute_values, shift)
               for k,p in future_sizes(FEATURES, n)) - n * label_cost


def adaptive(compute_values, label_cost):
    """Choose stopping under nominal transfer; then freeze the stopping/action policy."""
    actions = {}
    @lru_cache(None)
    def value(k, remaining):
        stop = target_return(k, compute_values)
        if remaining == 0:
            actions[k, remaining] = "stop"
            return stop
        advance = -label_cost + sum(p*value(j,remaining-1) for j,p in future_sizes(k))
        actions[k, remaining] = "buy" if advance > stop else "stop"
        return max(stop, advance)
    root = value(FEATURES, MAX_LABELS)
    ongoing = {FEATURES:F(1)}
    expected_labels = F(0)
    normal = shifted = F(0)
    stopped = F(0)
    for remaining in reversed(range(MAX_LABELS+1)):
        next_mass = defaultdict(F)
        for k, m in ongoing.items():
            if actions[k,remaining] == "stop":
                normal += m * target_return(k, compute_values)
                shifted += m * target_return(k, compute_values, True)
                stopped += m
            else:
                expected_labels += m
                for j,p in future_sizes(k):
                    next_mass[j] += m*p
        ongoing = next_mass
    assert stopped == 1
    assert normal - expected_labels * label_cost == root
    return root, shifted - expected_labels * label_cost, expected_labels


def survivor_subset_check(n):
    """Independent explicit source-label intersection, tracking identities."""
    # Each source has 8 equally likely observations. Fixing the latent J to
    # feature zero is sufficient by symmetry and is invisible to the chooser.
    mass = {frozenset(range(FEATURES)): F(1)}
    for _ in range(n):
        nxt = defaultdict(F)
        for subset,prob in mass.items():
            for bits in product(range(2), repeat=FEATURES):
                y = bits[0]
                new = frozenset(i for i in subset if bits[i] == y)
                nxt[new] += prob/8
        mass = nxt
    size_mass = defaultdict(F)
    for s,prob in mass.items():
        size_mass[len(s)] += prob
    assert dict((k,v) for k,v in future_sizes(FEATURES,n) if v) == dict(size_mass)


def results(compute_values,label_cost):
    val = [fixed(n,compute_values,label_cost) for n in range(MAX_LABELS+1)]
    best_n = max(range(MAX_LABELS+1), key=val.__getitem__)
    learned,shifted,nbar = adaptive(compute_values,label_cost)
    oracle = sum(F(max(0,9-c),2) for c in compute_values)/len(compute_values)
    assert 0 <= val[0] <= val[best_n] <= learned <= oracle
    assert fixed(0,compute_values,label_cost,True) == val[0]
    return {"foregone_compute":compute_values,"label_cost":str(label_cost),
            "local_only":0,"fixed_net_by_n":[str(a) for a in val],"best_n":best_n,
            "shifted_frozen_fixed_net":str(fixed(best_n,compute_values,label_cost,True)),
            "optimal_stopping_net":str(learned),"expected_source_labels":str(nbar),
            "shifted_frozen_stopping_net":str(shifted),"oracle":str(oracle),
            "known_independent_shift_optimum":str(val[0])}


if __name__ == "__main__":
    for n in range(MAX_LABELS+1):
        survivor_subset_check(n)
    print(json.dumps([results(x,c) for x in ((2,), (4,), (2,4))
                      for c in (F(15,100),F(30,100))], indent=2))
