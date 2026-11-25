"""Shared rescue capacity and the economic price of a fleet error.

Standard library only. Run this module to reproduce the hypothetical examples.
Every deadline is one independent decision window. An unserved exception misses
the deadline. Within a window, faults are independent conditional on a common
regime. Reserve the extra slot before observing the regime or the faults.
"""
from fractions import Fraction as F
from math import comb, fsum, isclose
import json


def binomial(n, p):
    """Exact conditional probability mass function, including p=0 and p=1."""
    return [comb(n, x) * p**x * (1 - p)**(n - x) for x in range(n + 1)]


def window(n, slots, regimes):
    """Exact mixture enumeration. Regimes are (probability, fault probability)."""
    assert sum(weight for weight, _ in regimes) == 1
    law = [F(0)] * (n + 1)
    for weight, p in regimes:
        for x, mass in enumerate(binomial(n, p)):
            law[x] += weight * mass
    assert sum(law) == 1
    mean = sum(x * mass for x, mass in enumerate(law))
    overflow = sum(max(0, x - slots) * mass for x, mass in enumerate(law))
    return {
        "raw_faults": mean,
        "variance": sum((x - mean)**2 * mass for x, mass in enumerate(law)),
        "missed_deadlines": overflow,
        "next_slot_rescue_probability": sum(law[slots + 1:]),
    }


def conditional_error_value(n, slots, p, rescue_cost, missed_value):
    """Cost difference for one extra fault at fixed faults of the other n-1.

    Downstream spending is included once. A served fault costs rescue_cost.
    A missed deadline costs missed_value. No rescue is performed on a miss.
    """
    others = binomial(n - 1, p)
    saturated = sum(others[slots:])
    direct_value = rescue_cost + (missed_value - rescue_cost) * saturated

    def cost(faults):
        return rescue_cost * min(faults, slots) + missed_value * max(0, faults - slots)

    enumerated = sum(mass * (cost(k + 1) - cost(k)) for k, mass in enumerate(others))
    assert enumerated == direct_value
    return direct_value


def overload_share(n, capacity_fraction, p):
    """Stable floating-point binomial summation for large fleets and 0<p<1.

    Start at the mode and recur towards both tails. Normalize at the end.
    For the demonstration sizes the resource fraction times n is integral.
    """
    capacity = int(capacity_fraction * n)
    mode = int((n + 1) * p)
    weights = [0.0] * (n + 1)
    weights[mode] = 1.0
    for k in range(mode + 1, n + 1):
        weights[k] = weights[k - 1] * (n - k + 1) * p / (k * (1 - p))
    for k in range(mode - 1, -1, -1):
        weights[k] = weights[k + 1] * (k + 1) * (1 - p) / ((n - k) * p)
    return fsum((k - capacity) * weights[k] for k in range(capacity + 1, n + 1)) / (n * fsum(weights))


def run():
    n, slots = 100, 8
    half = F(1, 2)
    independent = [(F(1), F(5, 100))]
    common = [(half, F(1, 100)), (half, F(9, 100))]
    improved = [(half, F(5, 1000)), (half, F(75, 1000))]
    cases = {"independent": independent, "common": common, "improved_common": improved}
    windows = {name: window(n, slots, regimes) for name, regimes in cases.items()}

    for name, regimes in cases.items():
        w = windows[name]
        w9 = window(n, slots + 1, regimes)
        assert w["missed_deadlines"] - w9["missed_deadlines"] == w["next_slot_rescue_probability"]
        marginal = sum(weight * p for weight, p in regimes)
        regime_variance = sum(weight * (p - marginal)**2 for weight, p in regimes)
        assert w["variance"] == n * marginal * (1 - marginal) + n * (n - 1) * regime_variance
        # In this variant a served fault has zero additional variable cost.
        w["ninth_slot_value_at_10_per_miss"] = 10 * w["next_slot_rescue_probability"]

    assert windows["independent"]["ninth_slot_value_at_10_per_miss"] < 2 < windows["common"]["ninth_slot_value_at_10_per_miss"]
    assert windows["improved_common"]["raw_faults"] < windows["independent"]["raw_faults"]
    assert windows["improved_common"]["missed_deadlines"] > windows["independent"]["missed_deadlines"]

    # A separate unit-cost variant: $0.50 per rescued job; $10 per missed job.
    marginal_values = {str(float(p)): float(conditional_error_value(n, slots, p, half, 10)) for _, p in common}

    sizes = (25, 100, 400, 1600, 6400)
    share = {}
    for size in sizes:
        share[str(size)] = {
            name: sum(float(weight) * overload_share(size, F(8, 100), float(p)) for weight, p in cases[name])
            for name in ("independent", "common")
        }
    for name in ("independent", "common"):
        assert isclose(share["100"][name], float(windows[name]["missed_deadlines"]) / n, rel_tol=1e-12)
    # Conditional LLN and bounded convergence imply E[(P - kappa)+].
    limits = {name: sum(float(weight * max(0, p - F(8, 100))) for weight, p in cases[name]) for name in ("independent", "common")}
    for name, limit in limits.items():
        assert abs(share[str(sizes[-1])][name] - limit) < 1e-5

    return {
        "window": {name: {k: round(float(v), 8) for k, v in row.items()} for name, row in windows.items()},
        "marginal_value_per_prevented_fault_by_regime": marginal_values,
        "expected_missed_fraction_by_fleet_size": share,
        "limiting_missed_fraction": limits,
    }


if __name__ == "__main__":
    print(json.dumps(run(), indent=2))
