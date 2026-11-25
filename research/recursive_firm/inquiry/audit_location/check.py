"""Exact finite-state payoffs. Run with Python 3, no dependencies."""
from fractions import Fraction as F
from itertools import product


def decisions(p, h, joint, work):
    """Unit release cost. Joint is the probability of distinct and beneficial."""
    return {
        "ordinary": max(0, work * (2 * joint - p) - 1),
        "source": max(0, work * (2 * joint - p) - p),
        "recipient": max(0, work * joint - h),
    }


def enumerate_decisions(p, h, joint, work):
    histories = [(1, 1, joint), (1, -1, p - joint),
                 (0, 1, h - joint), (0, -1, 1 - p - h + joint)]
    values = {}
    for name in ("ordinary", "source", "recipient"):
        conditional = {}
        for distinct, sign, weight in histories:
            observation = {"ordinary": None, "source": distinct, "recipient": sign}[name]
            payoff = distinct * sign * work - 1
            conditional[observation] = conditional.get(observation, 0) + weight * payoff
        values[name] = sum(max(0, value) for value in conditional.values())
    return values


def bounds(p, h, work):
    lower, upper = max(0, p + h - 1), min(p, h)
    candidates = [lower, upper, h / work, p * (1 + 1 / work) / 2]
    gaps = []
    for joint in candidates:
        if lower <= joint <= upper:
            value = decisions(p, h, joint, work)
            gaps.append(value["recipient"] - value["source"])
    return min(gaps), max(gaps)


def main():
    count = 0
    for p, h, joint in product([F(i, 10) for i in range(11)], repeat=3):
        if not max(0, p + h - 1) <= joint <= min(p, h):
            continue
        for work in map(F, [1, 2, 4, 10, 20]):
            value = decisions(p, h, joint, work)
            assert value == enumerate_decisions(p, h, joint, work)
            lo, hi = bounds(p, h, work)
            assert lo <= value["recipient"] - value["source"] <= hi
            count += 1
    p, h = F(3, 10), F(4, 5)
    for work in map(F, [4, 10]):
        value = decisions(p, h, p * h, work)
        print("Work", work, "under independence:", {k: str(v) for k, v in value.items()})
    lo, hi = bounds(p, h, F(10))
    assert (lo, hi) == (-F(1, 2), F(17, 20))
    print("Sharp recipient-minus-source bounds at work 10:", lo, hi)
    print("Exact state-enumeration checks:", count)


if __name__ == "__main__":
    main()
