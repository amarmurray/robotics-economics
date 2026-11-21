"""Independent exact-Fraction verification of synthetic triple-event buyer/rights construction."""
from fractions import Fraction as F
from itertools import product


def distribution(t):
    return {(u, v, license_right): (t if (u+v+license_right) % 2 else F(1, 4)-t)
            for u, v, license_right in product((0, 1), repeat=3)}


def check():
    checks = 0
    for k in range(101):
        t = F(k, 400)
        p = distribution(t)
        assert sum(p.values()) == 1
        checks += 1
        for i in range(3):
            assert sum(prob for state, prob in p.items() if state[i]) == F(1, 2)
            checks += 1
        for i, j in ((0, 1), (0, 2), (1, 2)):
            assert sum(prob for state, prob in p.items() if state[i] and state[j]) == F(1, 4)
            checks += 1
        assert p[(1, 1, 1)] == t
        checks += 1
        r = F(33, 32)
        g = F(17, 16)
        e = F(35, 32)
        s = 1 + max(F(1, 32), t/F(4))
        sg = 1 + max(F(1, 32), t/F(2))
        assert r <= g < e and s <= e and sg >= r
        assert (sg > e) == (t > F(3, 16))
        checks += 2
    assert 1 + max(F(1, 32), F(1, 4)/F(2)) - F(35, 32) == F(1, 32)
    assert 1 + max(F(1, 32), F(0)/F(2)) - F(35, 32) == -F(1, 16)
    checks += 2
    return {"independent_fraction_checks": checks, "grid_points": 101}


if __name__ == "__main__":
    print(check())
