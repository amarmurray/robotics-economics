"""Exact payoff checks for the allocation examples and two linked procurement auctions."""
from fractions import Fraction
from itertools import product


def target_outcome(source_winner, discovery_probability):
    """Enumerate independent discoveries at B after the learner (0) or executor (1) wins A."""
    profits = [Fraction(0), Fraction(0)]
    buyer_saving = Fraction(0)
    real_saving = Fraction(0)
    for learner_discovers, executor_discovers in product((False, True), repeat=2):
        probability = Fraction(1)
        for succeeds in (learner_discovers, executor_discovers):
            probability *= discovery_probability if succeeds else 1 - discovery_probability
        learner_low_cost = (source_winner == 0) or learner_discovers
        if learner_low_cost or executor_discovers:
            real_saving += 8 * probability
        if learner_low_cost and executor_discovers:
            buyer_saving += 8 * probability
        elif learner_low_cost:
            profits[0] += 8 * probability
        elif executor_discovers:
            profits[1] += 8 * probability
    assert sum(profits) + buyer_saving == real_saving
    return profits, real_saving


def check_linked_orders():
    for percent in range(101):
        h = Fraction(percent, 100)
        learner_wins, efficient = target_outcome(0, h)
        executor_wins, alternative = target_outcome(1, h)
        learner_gain = learner_wins[0] - executor_wins[0]
        executor_gain = executor_wins[1] - learner_wins[1]
        assert learner_gain == 8 * (1 - h) ** 2
        assert executor_gain == 8 * h * (1 - h)
        assert efficient - alternative == 8 * (1 - h) ** 2
        bids = (30 - learner_gain, 30 - executor_gain)
        if percent in (25, 75):
            winner = 'learner' if bids[0] < bids[1] else 'executor'
            saving = efficient if winner == 'learner' else alternative
            print(f'h={float(h):.2f}: bids {float(bids[0]):.2f}, {float(bids[1]):.2f}; '
                  f'{winner} wins; expected real saving at B = {float(saving):.2f}')


def check_allocation():
    for displaced, expected in [(2, 4), (10, 0), (18, -4)]:
        assert Fraction(24 - displaced, 2) - 7 == expected
    assert Fraction(12 - 2, 4) - 2 == Fraction(1, 2)
    assert Fraction(12 - 10, 2) - 2 == -1
    print('Sampling gains: +4, 0, -4. Gains with and without timely queue information: +0.5, -1.')


if __name__ == '__main__':
    check_allocation()
    check_linked_orders()
