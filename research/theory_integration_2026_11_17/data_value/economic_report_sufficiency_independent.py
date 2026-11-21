from fractions import Fraction as Q
from itertools import product

# Independent exact enumeration for the 17 t laws; no input files or third-party packages.
count_full = count_coarse = 0
for j in range(17):
    t = Q(j, 256)
    g = [Q(7,16)-t, Q(1,8)+t, Q(1,16)-t, t]
    scores_full = []
    for policy in product((0, 1), repeat=8):
        value = Q(0)
        for pattern in range(8):
            k = pattern.bit_count()
            value += Q(1,2)*(Q(1,4)*g[k] if policy[pattern] == 0 else Q(3,4)*g[3-k])
        scores_full.append(value)
        count_full += 1
    scores_coarse = []
    for policy in product((0, 1), repeat=2):
        value = Q(0)
        for pattern in range(8):
            k = pattern.bit_count()
            action = policy[int(k>=2)]
            value += Q(1,2)*(Q(1,4)*g[k] if action == 0 else Q(3,4)*g[3-k])
        scores_coarse.append(value)
        count_coarse += 1
    full, coarse = max(scores_full), max(scores_coarse)
    assert full - coarse == max(Q(3,128)-Q(3,2)*t, Q(0))
assert count_full == 4352 and count_coarse == 68
print("17 exact laws; 4352 full policies and 68 compressed policies; identity checked")
