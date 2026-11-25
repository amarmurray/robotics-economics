"""Reproduce the two-state boundary example and check the optimal switching rule."""
from fractions import Fraction as F
from itertools import product


def unresolved_value(flow, probability, mature_value, discount):
    return (flow + discount * probability * mature_value) / (1 - discount * (1 - probability))


def best_unresolved(actions, mature_value, discount):
    return max(unresolved_value(flow, rate, mature_value, discount) for flow, rate in actions)


def verify_switching(discount, options, mature, entry, exit_cost):
    """Check both Bellman equations with setup and exit charged at the switch date."""
    qp, qi = [best_unresolved(actions, value, discount)
              for actions, value in zip(options, mature)]
    values = (max(qp, qi - entry), max(qi, qp - exit_cost))
    for incumbent in (0, 1):
        alternatives = []
        for choice in (0, 1):
            fee = 0 if choice == incumbent else (entry if choice else exit_cost)
            for flow, rate in options[choice]:
                continuation = rate * mature[choice] + (1 - rate) * values[choice]
                alternatives.append(flow - fee + discount * continuation)
        assert values[incumbent] == max(alternatives)
    return qp, qi


def main():
    discount = F(9, 10)
    partner = [(4, F(1, 20)), (3, F(1, 10))]
    integrated = [(4, F(1, 10)), (2, F(2, 5))]
    joint_lab = [(F(7, 2), F(7, 20))]
    qp, qi = verify_switching(discount, (partner, integrated), (100, 98), 4, 2)
    hybrid = best_unresolved(joint_lab, 99, discount) - 1
    print("Partner, integrate net of entry, joint lab net of entry:",
          *(round(float(value), 3) for value in (qp, qi-4, hybrid)))
    assert qp < qi - 4 < hybrid
    tests = 0
    for beta, rate_p, rate_i, setup, unwind in product(
            (F(1, 2), F(9, 10)), (F(0), F(1, 2), F(1)),
            (F(0), F(1, 3), F(1)), (0, 1, 10), (0, 2, 30)):
        mature_p = 10 / (1 - beta)
        mature_i = max(8 / (1 - beta), mature_p - unwind)
        verify_switching(beta, ([(3, rate_p)], [(2, rate_i)]),
                         (mature_p, mature_i), setup, unwind)
        tests += 1
    print("Exact Bellman checks across parameter combinations:", tests)
    # For a one-period versus two-period implementation delay the peak is x=1/2.
    for x in [F(i, 100) for i in range(101)]:
        assert x - x*x == F(1, 4) - (x - F(1, 2))**2


if __name__ == "__main__":
    main()
