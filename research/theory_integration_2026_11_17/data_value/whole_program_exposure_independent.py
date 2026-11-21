#!/usr/bin/env python3
"""Independent exact-fraction check of full-paid-program exposure variance; synthetic only."""
from fractions import Fraction as Q
from itertools import product

N = 4
hoods = ((0, 1), (0, 1, 2), (1, 2, 3), (2, 3))
sg = [Q(x, 20) for x in (8, 12, 18, 16)]
em = [Q(x, 20) for x in (10, 6, 15, 13)]
p = Q(1, 2)
target_sg = sum(sg) / N
target_e = sum(em) / N
rows = []
for z in product((0, 1), repeat=N):
    a = sum((sg[i] / p**len(h) for i, h in enumerate(hoods)
             if all(z[j] == 1 for j in h)), Q(0)) / N
    b = sum((em[i] / (1-p)**len(h) for i, h in enumerate(hoods)
             if all(z[j] == 0 for j in h)), Q(0)) / N
    rows.append((a, b))
mean_a = sum((a for a, _ in rows), Q(0)) / len(rows)
mean_b = sum((b for _, b in rows), Q(0)) / len(rows)
assert (mean_a, mean_b) == (target_sg, target_e)

var_a = sum(((a-mean_a)**2 for a, _ in rows), Q(0)) / len(rows)
var_b = sum(((b-mean_b)**2 for _, b in rows), Q(0)) / len(rows)
cov_ab = sum(((a-mean_a)*(b-mean_b) for a, b in rows), Q(0)) / len(rows)
var_gap = var_a + var_b - 2*cov_ab

def overlap(i, j):
    return len(set(hoods[i]) & set(hoods[j]))

formula_a = sum((sg[i]*sg[j]*(p**(-overlap(i, j))-1)
                 for i in range(N) for j in range(N)), Q(0)) / N**2
formula_b = sum((em[i]*em[j]*((1-p)**(-overlap(i, j))-1)
                 for i in range(N) for j in range(N)), Q(0)) / N**2
formula_cov = -sum((sg[i]*em[j] for i in range(N) for j in range(N)
                   if overlap(i, j)), Q(0)) / N**2
assert (formula_a, formula_b, formula_cov) == (var_a, var_b, cov_ab)
assert (mean_a, mean_b, var_a, var_b, cov_ab, var_gap) == (
    Q(27,40), Q(11,20), Q(2127,1600), Q(129,160), Q(-33,100), Q(4473,1600))
M = max(sum(overlap(i, j)>0 for j in range(N)) for i in range(N))
d = max(map(len, hoods))
upper = Q(M,N)*(p**(-d)+(1-p)**(-d))
assert upper == 16 and var_gap < upper

# Counterexample: missing a second-unit learner edge halves an intended full-SG mean.
wrong = Q(0)
for z in product((0,1), repeat=2):
    y = Q(1) if z == (1,1) else Q(0)
    wrong += (2*y if z[0] else 0)
wrong /= (4*2)  # four assignments and two original buyer units
assert wrong == Q(1,4)
print({"exact_assignment_worlds":len(rows), "SG":str(mean_a), "E":str(mean_b),
       "SG_minus_E":str(mean_a-mean_b), "var_gap":str(var_gap),
       "variance_bound":str(upper), "wrong_graph_expected_mean":str(wrong)})
