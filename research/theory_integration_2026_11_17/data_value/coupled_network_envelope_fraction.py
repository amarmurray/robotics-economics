"""Independent exact-Fraction check for two-site shared-network envelope.

Synthetic values only. The mathematical proof is the finite policy-envelope
argument; exact enumerations are software checks, not field evidence.
"""
from fractions import Fraction as F
from itertools import combinations
import json

P = ((F(2), F(4)), (F(3, 2), F(5)))
E = ((F(19, 10), F(39, 10)), (F(3, 2), F(9, 2)))

def value(row, theta):
    return row[0] * (1 - theta) + row[1] * theta

def optimum(rows, theta):
    return max(value(r, theta) for r in rows)

def breakpoints(*groups):
    possible = {F(0), F(1)}
    for rows in groups:
        for a, b in combinations(rows, 2):
            denominator = (b[1] - b[0]) - (a[1] - a[0])
            if denominator:
                theta = (a[0] - b[0]) / denominator
                if 0 <= theta <= 1:
                    possible.add(theta)
    return sorted(possible)

candidates = breakpoints(P, E)
assert candidates == [F(0), F(1, 3), F(2, 5), F(1)]
gaps = [(t, optimum(P, t) - optimum(E, t)) for t in candidates]
assert gaps == [(F(0), F(1, 10)),
                (F(1, 3), F(1, 10)),
                (F(2, 5), F(1, 5)),
                (F(1), F(1, 2))]
checked = 0
for d in range(1, 61):
    for n in range(d + 1):
        t = F(n, d)
        assert F(1, 10) <= optimum(P, t) - optimum(E, t) <= F(1, 2)
        checked += 1

alternate_E = ((F(19, 10), F(39, 10)), (F(11, 5), F(9, 2)))
assert optimum(P, F(0)) - optimum(alternate_E, F(0)) == -F(1, 5)
assert optimum(P, F(7, 12)) == optimum(alternate_E, F(7, 12))
assert optimum(P, F(1)) - optimum(alternate_E, F(1)) == F(1, 2)

# A fixed P pilot mixture rho cannot beat the E environment-specific optimizer
# at both theta=0 (rho<=1/5) and theta=1 (rho>=1/2).
assert F(1, 5) < F(1, 2)
result = {"fraction_switchpoints": [str(t) for t in candidates],
          "fraction_gap": [str(g) for _, g in gaps],
          "fraction_grid_points": checked,
          "synthetic": True, "signed_field_data": False}
if __name__ == "__main__":
    print(json.dumps(result, indent=2))
