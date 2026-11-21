"""Independent exact-rational check of the common opportunity numerical example.
Run: python coupled_resource_report_value_independent.py
No dependencies or external data."""
from fractions import Fraction as Q

p = (Q(1, 2), Q(1, 4), Q(1, 4))
values = []
for k in range(33):
    lam = Q(k, 64)
    a = (Q(3, 2), Q(3, 4), 1 + lam)
    b = (1 + lam, 1 + lam, Q(1))
    vf = sum(p[j] * max(a[j], b[j]) for j in range(3))
    vc = max(sum(p[j] * a[j] for j in range(3)),
             sum(p[j] * b[j] for j in range(3)))
    direct = vf - vc
    predicted = min(Q(1, 4) - lam / 4, Q(1, 16) + lam / 4)
    assert direct == predicted, (k, direct, predicted)
    values.append(direct)
assert min(values) == Q(1, 16)
assert max(values) == Q(5, 32)
assert values.index(Q(5, 32)) == 24
rvalues = []
for x in range(33):
    for z in range(33):
        for yy in range(-48, -15):
            delta = (Q(x, 64), Q(yy, 64), Q(z, 64))
            P = sum(p[i] * max(delta[i], 0) for i in range(3))
            N = sum(p[i] * max(-delta[i], 0) for i in range(3))
            rvalues.append(min(P, N))
assert min(rvalues) == 0
assert max(rvalues) == Q(3, 16)
print("33 common-parameter cases and 35,937 rectangular worlds verified with exact Fraction arithmetic")
