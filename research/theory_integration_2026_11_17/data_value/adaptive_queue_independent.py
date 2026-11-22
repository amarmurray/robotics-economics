"""Independent exact Fraction audit of conditional synthetic action-induced queue model."""
from fractions import Fraction as F

def joint(z):
    return {(1, 0): z, (1, 1): F(3, 4)-z,
            (0, 0): F(1, 2)-z, (0, 1): z-F(1, 4)}

def paid_p(z, choose_target):
    total = F(0)
    for d in (1, 2):
        for (u, j), mass in joint(z).items():
            if d == 1 and choose_target:
                increment = F(1, 8) + (F(1) if u == 1 and j == 0 else F(0))
            else:
                increment = F(4, 5) * F(5, 8)
            total += F(1, 2) * mass * (4-F(1, 4)+increment)
    return total

checks = 0
for k in range(16, 33):
    z = F(k, 64)
    law = joint(z)
    assert all(p >= 0 for p in law.values()); checks += 1
    assert sum(law.values()) == 1; checks += 1
    assert sum(v for (u, j), v in law.items() if u == 1) == F(3, 4); checks += 1
    assert sum(v for (u, j), v in law.items() if j == 1) == F(1, 2); checks += 1
    r, t = paid_p(z, False), paid_p(z, True)
    assert r == F(17, 4); checks += 1
    assert t == 4+F(1, 2)*(F(1, 8)+z); checks += 1
    assert max(r, t) == 4+F(1, 2)*max(F(1, 2), F(1, 8)+z); checks += 1
    assert (t > r) == (z > F(3, 8)); checks += 1
G = 4+F(7, 10)-F(21, 50)
E = 4+F(9, 10)-F(3, 5)
assert G == F(107, 25); checks += 1
assert E == F(43, 10); checks += 1
assert max(paid_p(F(1, 4), False), paid_p(F(1, 4), True)) == F(17, 4); checks += 1
assert max(paid_p(F(1, 2), False), paid_p(F(1, 2), True)) == F(69, 16); checks += 1
assert F(17, 4) < G < E < F(69, 16); checks += 1
for i in range(101):
    x = F(i, 100)
    worst = min((1-x)*paid_p(z, False)+x*paid_p(z, True)
                for z in (F(1, 4), F(1, 2)))
    assert worst <= F(17, 4); checks += 1
print({"checked": checks, "low_P": "17/4", "high_P": "69/16",
       "grounding_G": str(G), "embodiment_E": str(E),
       "real_customer_observations": False})
