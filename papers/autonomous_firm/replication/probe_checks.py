"""Exact checks for the autonomous-firm probe example. All payoffs are dollars.

Operating locally gives zero before switching costs. Pooling gives
12000*p - 3000, less the contribution displaced from a shared compute slot.
Retained training data can add a known, separate execution gain when pooled.
The free probe reveals a calibrated posterior before the same choice is made.
"""

from fractions import Fraction
from itertools import product


LOCAL = "local"
POOLED = "pooled"
MODES = (LOCAL, POOLED)
POSTERIORS = (Fraction(1, 5), Fraction(2, 5))
SWITCH_COST = 1200
HALF = Fraction(1, 2)


def operating_advantage(p):
    """Pooled operating contribution relative to local, before other debits."""
    return 12000 * p - 3000


def payoff(incumbent, chosen, posterior, displacement, retained_data_gain):
    value = 0
    if chosen == POOLED:
        value = operating_advantage(posterior) - displacement + retained_data_gain
    if chosen != incumbent:
        value -= SWITCH_COST
    return value


def optimal_values(incumbent, displacement, retained_data_gain=0, high_probability=HALF):
    """Return best expected contribution without, then with, the signal.

    Evaluate both constant policies and all four signal-contingent policies.
    Using the same posterior distribution in both arms enforces a common prior.
    """
    probabilities = (1 - high_probability, high_probability)
    fixed = []
    contingent = []
    for choices in product(MODES, repeat=2):
        expected = sum(
            weight * payoff(incumbent, chosen, p, displacement, retained_data_gain)
            for weight, chosen, p in zip(probabilities, choices, POSTERIORS)
        )
        contingent.append(expected)
        if choices[0] == choices[1]:
            fixed.append(expected)
    return max(fixed), max(contingent)


def probe_value(incumbent, displacement, retained_data_gain=0, high_probability=HALF):
    before, after = optimal_values(
        incumbent, displacement, retained_data_gain, high_probability
    )
    return after - before


def tent_value(incumbent, displacement, retained_data_gain=0, high_probability=HALF):
    """Independent closed form for the two-state value of timely information."""
    low, high = map(operating_advantage, POSTERIORS)
    mean = (1 - high_probability) * low + high_probability * high
    hurdle = displacement - retained_data_gain
    hurdle += SWITCH_COST if incumbent == LOCAL else -SWITCH_COST
    if hurdle <= low or hurdle >= high:
        return 0
    if hurdle <= mean:
        return (1 - high_probability) * (hurdle - low)
    return high_probability * (high - hurdle)


def check_results():
    # Unequal signal probabilities exercise the asymmetric general tent.
    # Include both kinks, the maximum, and points on either side of each.
    low, high = map(operating_advantage, POSTERIORS)
    for probability in (0, Fraction(1, 4), HALF, Fraction(3, 4), 1):
        mean = (1 - probability) * low + probability * high
        for mode in MODES:
            for rights_gain in (0, 800):
                offset = SWITCH_COST if mode == LOCAL else -SWITCH_COST
                debits = set(range(0, 5001, 100))
                for corner in (low, mean, high):
                    for step in (-1, 0, 1):
                        debits.add(corner + step + rights_gain - offset)
                for debit in sorted(d for d in debits if d >= 0):
                    actual = probe_value(mode, debit, rights_gain, probability)
                    predicted = tent_value(mode, debit, rights_gain, probability)
                    assert actual == predicted, (mode, debit, rights_gain, probability)

    expected = {
        0: (300, 0),
        600: (0, 0),
        1200: (0, 300),
        1800: (0, 600),
        3000: (0, 0),
    }
    print("Displaced contribution | Probe value from local | Probe value from pooled")
    for debit, pair in expected.items():
        calculated = tuple(probe_value(mode, debit) for mode in MODES)
        assert calculated == pair, (debit, calculated)
        print(f"{debit:>22} | {str(calculated[0]):>22} | {str(calculated[1]):>23}")

    # Separately vary transient report access and retained-data training rights.
    no_rights = optimal_values(POOLED, 1200)
    rights = optimal_values(POOLED, 1200, retained_data_gain=800)
    assert no_rights == (-600, -300)
    assert rights == (200, 200)
    interaction = (rights[1] - rights[0]) - (no_rights[1] - no_rights[0])
    assert interaction == -300
    print("Report/training-rights interaction:", interaction)
    print("All exact checks passed.")


if __name__ == "__main__":
    check_results()
