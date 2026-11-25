"""Reproduce the examples in When Faster Learning Pays. Requires Python 3.10+."""

from dataclasses import dataclass
from fractions import Fraction
from itertools import product


ZERO = Fraction(0)
ONE = Fraction(1)


def outcomes(probability):
    return ((False, 1 - probability), (True, probability))


def qualification(yield_per_shift, shifts, baseline, transfer):
    return baseline + transfer * (1 - (1 - yield_per_shift) ** shifts)


def terminal_value(shifts, own_ordinary, own_fast, rival_yield, baseline, prize):
    transfer = 1 - baseline
    rival = qualification(rival_yield, shifts, baseline, transfer)
    own_gain = qualification(own_fast, shifts, baseline, transfer) - qualification(
        own_ordinary, shifts, baseline, transfer
    )
    return prize * own_gain * (1 - rival)


def probability_by_iteration(source_yield, shifts, baseline, transfer):
    unknown = ONE
    learned = ZERO
    for _ in range(shifts):
        learned += unknown * source_yield
        unknown *= 1 - source_yield
    return learned * (baseline + transfer) + unknown * baseline


def adaptive_investigation(margins, costs, ordinary, accelerated, discount):
    """Actions apply only while still searching. Break ties in favor of routine work."""
    premium = ZERO
    actions = []
    for margin, cost in reversed(list(zip(margins, costs, strict=True))):
        value_of_discovery = margin + discount * premium
        net_gain = (accelerated - ordinary) * value_of_discovery - cost
        actions.append(net_gain > 0)
        premium = (1 - ordinary) * value_of_discovery - max(ZERO, net_gain)
    known_value = sum(discount**t * m for t, m in enumerate(margins))
    return tuple(reversed(actions)), known_value - premium


def payoff_for_plan(plan, margins, costs, ordinary, accelerated, discount):
    """Evaluate a complete conditional plan forwards, with costs on unknown paths only."""
    unknown = ONE
    value = ZERO
    for t, (invest, margin, cost) in enumerate(zip(plan, margins, costs, strict=True)):
        if invest:
            value -= discount**t * unknown * cost
        rate = accelerated if invest else ordinary
        unknown *= 1 - rate
        value += discount**t * (1 - unknown) * margin
    return value


@dataclass(frozen=True)
class Game:
    ordinary: Fraction
    accelerated: Fraction
    baseline: Fraction
    prize: Fraction
    leader_cost: Fraction
    follower_cost: Fraction

    def source_yield(self, invest):
        return self.accelerated if invest else self.ordinary


@dataclass(frozen=True)
class Accounts:
    leader: Fraction
    follower: Fraction
    buyer: Fraction
    saving: Fraction
    cost: Fraction
    rival_alone: Fraction

    @property
    def joint(self):
        return self.saving - self.cost


def settle(game, leader_invests, follower_plan, *, observed=None):
    """Enumerate the two discoveries, the two target qualifications and transfers.

    follower_plan indexes A's public discovery (False/True). Passing observed
    fixes that discovery for a conditional best-response calculation.
    """
    if observed is None:
        first = outcomes(game.source_yield(leader_invests))
    else:
        first = ((observed, ONE),)

    a_profit = b_profit = buyer = total_saving = total_cost = rival_alone = ZERO
    a_cost = game.leader_cost * leader_invests
    for a_learned, prob_a in first:
        b_invests = follower_plan[a_learned]
        b_cost = game.follower_cost * b_invests
        for b_learned, prob_b in outcomes(game.source_yield(b_invests)):
            a_ready = ONE if a_learned else game.baseline
            b_ready = ONE if b_learned else game.baseline
            for (a_low, prob_i), (b_low, prob_r) in product(outcomes(a_ready), outcomes(b_ready)):
                mass = prob_a * prob_b * prob_i * prob_r
                prize = game.prize
                a_profit += mass * (prize * (a_low and not b_low) - a_cost)
                b_profit += mass * (prize * (b_low and not a_low) - b_cost)
                buyer += mass * prize * (a_low and b_low)
                total_saving += mass * prize * (a_low or b_low)
                total_cost += mass * (a_cost + b_cost)
                rival_alone += mass * (prize * b_low - b_cost)
    row = Accounts(a_profit, b_profit, buyer, total_saving, total_cost, rival_alone)
    assert row.joint == row.leader + row.follower + row.buyer
    assert row.joint == row.leader + row.rival_alone
    return row


def follower_best_response(game):
    choices = []
    for known in (False, True):
        ordinary = settle(game, False, (False, False), observed=known)
        accelerated = settle(game, False, (True, True), observed=known)
        private_gain = accelerated.follower - ordinary.follower
        social_gain = accelerated.joint - ordinary.joint
        assert private_gain == social_gain
        choices.append(private_gain > 0)
    return tuple(choices)


def check_deadlines():
    baseline, prize = Fraction(1, 2), Fraction(100)
    grid = tuple(Fraction(i, 5) for i in range(1, 5))
    comparisons = 0
    for ordinary, accelerated, rival in product(grid, repeat=3):
        if accelerated <= ordinary:
            continue
        values = []
        for n in range(29):
            p0, p1, pr = [
                probability_by_iteration(rate, n, baseline, 1-baseline)
                for rate in (ordinary, accelerated, rival)
            ]
            value = terminal_value(n, ordinary, accelerated, rival, baseline, prize)
            x = (1 - ordinary) * (1 - rival)
            z = (1 - accelerated) * (1 - rival)
            assert value == prize * (p1 - p0) * (1 - pr)
            assert value == prize * (1-baseline)**2 * (x**n - z**n)
            values.append(value)
            comparisons += 1
        saw_decline = False
        for earlier, later in zip(values, values[1:]):
            if later < earlier:
                saw_decline = True
            if saw_decline:
                assert later <= earlier
        assert saw_decline
    ordinary, accelerated = Fraction(1, 10), Fraction(2, 5)
    print("Source shifts  Ordinary rival  Accelerated rival")
    for n in (0, 1, 2, 3, 4, 5, 8):
        gains = [terminal_value(n, ordinary, accelerated, r, baseline, prize)
                 for r in (ordinary, accelerated)]
        print(f"{n:>13}{float(gains[0]):>16.2f}{float(gains[1]):>19.2f}")
    accepted = [
        n for n in range(30)
        if terminal_value(n, ordinary, accelerated, ordinary, baseline, prize) > 8
    ]
    assert accepted == [2, 3, 4]
    return comparisons


def check_adaptive_schedules():
    ordinary, accelerated = Fraction(1, 10), Fraction(2, 5)
    cases = plans = 0
    for length in range(1, 8):
        profiles = [
            [0] * (length - 1) + [20],
            [20] + [0] * (length - 1),
            [3 + 2 * (t % 3) for t in range(length)],
        ]
        for rewards, discount, cost in product(profiles, (ONE, Fraction(4, 5)), (ZERO, 4, 10)):
            costs = [cost] * length
            schedule, value = adaptive_investigation(rewards, costs, ordinary, accelerated, discount)
            enumerated = [
                payoff_for_plan(plan, rewards, costs, ordinary, accelerated, discount)
                for plan in product((False, True), repeat=length)
            ]
            assert value == max(enumerated)
            assert value == payoff_for_plan(schedule, rewards, costs, ordinary, accelerated, discount)
            if rewards[:-1] == [0] * (length - 1):
                assert list(schedule) == sorted(schedule)
            cases += 1
            plans += len(enumerated)
    for date, expected in [(0, (True, False, False, False, False)),
                           (4, (False, False, True, True, True))]:
        rewards = [0] * 5
        rewards[date] = 20
        schedule, _ = adaptive_investigation(rewards, [4]*5, ordinary, accelerated, ONE)
        assert schedule == expected
        print(f"Margin due on shift {date+1}: investigate on",
              [i + 1 for i, active in enumerate(schedule) if active])
    return cases, plans


def check_overlap():
    # j is a matched date and task. Outcomes here are independent across firms.
    checked = 0
    for i0, i1, r0, r1 in product((ZERO, Fraction(1, 3), Fraction(2, 3), ONE), repeat=4):
        gain0 = (i1 - i0) * (1 - r0)
        gain1 = (i1 - i0) * (1 - r1)
        assert gain0 - gain1 == (i1 - i0) * (r1 - r0)
        checked += 1
    # A pointwise check permits arbitrary joint potential outcomes, including opposite signs.
    for i0, i1, r0, r1 in product((0, 1), repeat=4):
        diff = i1*(1-r0) - i0*(1-r0) - i1*(1-r1) + i0*(1-r1)
        assert diff == (i1-i0)*(r1-r0)
        checked += 1
    return checked


def check_strategic_game():
    game = Game(Fraction(1, 5), Fraction(4, 5), Fraction(1, 2), Fraction(100),
                Fraction(10), Fraction(10))
    response = follower_best_response(game)
    assert response == (True, False)
    rows = [settle(game, action, response) for action in (False, True)]
    for row, expected in zip(rows, [(12, 28, 48, 96, 8, 76), (23, 7, 57, 99, 12, 64)], strict=True):
        assert row == Accounts(*expected)
        print("A, B, buyer, gross saving, real cost, joint:",
              *(int(x) for x in (row.leader, row.follower, row.buyer, row.saving, row.cost, row.joint)))
    feasible = [
        settle(game, action, plan).joint
        for action in (False, True) for plan in product((False, True), repeat=2)
    ]
    assert max(feasible) == rows[0].joint == 88
    assert rows[1].leader - rows[0].leader == 11
    assert rows[1].joint - rows[0].joint == -1

    # Check the range with a strategic follower, plus all fixed follower programs.
    for a_cost in range(26):
        changed = Game(game.ordinary, game.accelerated, game.baseline, game.prize,
                       Fraction(a_cost), game.follower_cost)
        low, high = [settle(changed, a, follower_best_response(changed)) for a in (False, True)]
        assert high.leader - low.leader == 21 - a_cost
        assert high.joint - low.joint == 9 - a_cost
        for action_b in (False, True):
            low, high = [settle(changed, a, (action_b, action_b)) for a in (False, True)]
            assert high.leader - low.leader == high.joint - low.joint


if __name__ == "__main__":
    deadlines = check_deadlines()
    cases, plans = check_adaptive_schedules()
    overlaps = check_overlap()
    check_strategic_game()
    print(f"Verified {deadlines} deadline values, {plans} policies in {cases} adaptive settings, "
          f"{overlaps} overlap checks, and the sequential game.")
