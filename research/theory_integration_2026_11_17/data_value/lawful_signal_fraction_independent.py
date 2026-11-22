"""Independent exact rational spot check of lawful signal feasible partitions.
No external data or robot observations. Run with python3 verify_lawful_signal_fraction.py.
"""
from fractions import Fraction as F
from itertools import product

Q = [(F(1), F(0)), (F(0), F(1)), (F(1), F(0))]


def value(z):
    total = F(0)
    for label in set(z):
        hs = [h for h, v in enumerate(z) if v == label]
        total += max(sum(Q[h][a] for h in hs) for a in range(2)) / 3
    return total


assert value((0, 0, 0)) == F(2, 3)
assert value((0, 0, 1)) == F(2, 3)
assert value((0, 1, 0)) == F(1, 1)
assert value((0, 1, 2)) == F(1, 1)
old_policy = F(1, 2)
E = F(3, 4)
SG_coarse = max(old_policy, value((0, 0, 1)))
SG_fine = max(old_policy, value((0, 1, 0)))
licensed_report_cost = F(1, 8)
assert SG_coarse - E == -F(1, 12)
assert SG_fine - licensed_report_cost - E == F(1, 8)
assert SG_fine - SG_coarse == F(1, 3)

# Robust Q uncertainty with two possible opposite customer-response kernels.
# Randomized action a with probability alpha has regrets 1-alpha and alpha.
assert min(max(F(1) - F(k, 100), F(k, 100)) for k in range(101)) == F(1, 2)
assert max(min(F(1) - F(k, 100), F(k, 100)) for k in range(101)) == F(1, 2)
print({'rational_checks': 11, 'coarse_SG_minus_E': str(SG_coarse - E),
       'licensed_SG_minus_E': str(SG_fine - licensed_report_cost - E),
       'minimax_mixed_regret': str(F(1, 2)), 'field_data': False})
