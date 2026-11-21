"""Independent exact Fraction audit for conditional_component_certificate.js.
Synthetic algebra only; not an independent physical/empirical replication.
Run: python conditional_component_certificate_independent.py
"""
from fractions import Fraction as Q

w0 = Q(1, 4)
q0, q1, c = Q(1, 2), Q(3, 4), Q(1, 4)
E = Q(19, 16)

def trained_value(w, q, rights=True):
    return Q(1) + (w * max(Q(0), q - c) if rights else Q(0))

R = trained_value(w0, q0)
G = trained_value(w0, q1)
assert R == Q(17, 16) and G == Q(9, 8)
assert trained_value(Q(0), q1, False) == Q(1)

checks = 3
for k in range(101):
    w = Q(k, 200)
    # All four joint cells are nonnegative and retain both marginals 1/2.
    p00, p01, p10, p11 = w, Q(1, 2)-w, Q(1, 2)-w, w
    assert p00+p01+p10+p11 == 1
    assert p10+p11 == p01+p11 == Q(1, 2)
    checks += 2
    S = max(R, trained_value(w, q0))
    SG = max(G, trained_value(w, q1))
    assert S >= R and SG >= G
    assert Q(9, 8) <= SG <= Q(5, 4)
    assert SG > E if w > Q(3, 8) else SG <= E
    checks += 3

high = Q(1, 2)
S_high = max(R, trained_value(high, q0))
SG_high = max(G, trained_value(high, q1))
assert SG_high-S_high-G+R == Q(1, 16)
assert max(G, trained_value(Q(0), q1))-E == -Q(1, 16)
assert SG_high-E == Q(1, 16)
assert max(G, trained_value(Q(1, 3), q1)) == Q(7, 6) < E
assert max(G, trained_value(Q(2, 5), q1)) == Q(6, 5) > E
checks += 5
print(f"independent_fraction_checks={checks}; passed=true")
