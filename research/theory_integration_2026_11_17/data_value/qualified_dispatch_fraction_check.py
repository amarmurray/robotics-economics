"""Independent exact-rational verification of the conditional qualified-dispatch model."""
from fractions import Fraction as F
from itertools import product
from math import comb

R_A, R_B = F(1, 4), F(3, 4)
patterns = [sum(bits) for bits in product((0, 1), repeat=3)]
counts = 0
for j in range(17):
    t = F(j, 256)
    g = [F(7, 16)-t, F(1, 8)+t, F(1, 16)-t, t]
    assert sum(comb(3, k)*g[k] for k in range(4)) == 1
    assert g[1]+2*g[2]+g[3] == F(1, 4)
    assert g[2]+g[3] == F(1, 16)
    q = sum(comb(3, k)*max(R_A*g[k], R_B*g[3-k]) for k in range(4))/2
    q_closed = F(55, 128)-t/2 if t <= F(1,64) else F(13,32)+t
    assert q == q_closed
    exhaustive = max(
        sum((R_B*g[3-k] if action else R_A*g[k])
            for k, action in zip(patterns, decision))/2
        for decision in product((0, 1), repeat=8)
    )
    assert exhaustive == q
    counts += 256
assert F(1,2)*(F(55,128)+F(15,32))-F(7,16) == F(3,256)
print({"worlds":17,"rules":counts,"q_min":"27/64","q_max":"15/32","X_only_audit_value":"15/128"})
