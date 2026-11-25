"""Replicate the installed-base results in The Production of Capability (Python 3.10+).

All values are illustrative. Run directly. Uses only the Python standard library.
"""
from dataclasses import dataclass
from fractions import Fraction as Q
from itertools import combinations, product


def subsets(items):
    items = tuple(items)
    for count in range(len(items) + 1):
        yield from combinations(items, count)


@dataclass(frozen=True)
class Release:
    gain: Q
    target_hours: int
    hourly_cost: Q
    second_version_cost: Q

    def value(self, available, legacy_hours, separate):
        """One release window. Zero is the best continuation without this change."""
        common_hours = self.target_hours + legacy_hours
        choices = [Q(0)]
        if common_hours <= available:
            choices.append(self.gain - self.hourly_cost * common_hours)
        if separate and self.target_hours <= available:
            choices.append(self.gain - self.hourly_cost * self.target_hours - self.second_version_cost)
        return max(choices)


def enumerate_validation(release, hours, supported_sites, hours_by_class, separate):
    """Independently choose a subset of tests, then see which plans it authorizes."""
    time = dict(hours_by_class, target=release.target_hours)
    required = set(supported_sites) | {"target"}
    best = Q(0)
    for selected in subsets(time):
        used = sum(time[item] for item in selected)
        if used > hours:
            continue
        testing_cost = release.hourly_cost * used
        if required.issubset(selected):
            best = max(best, release.gain - testing_cost)
        if separate and "target" in selected:
            best = max(best, release.gain - testing_cost - release.second_version_cost)
    return best


@dataclass(frozen=True)
class Inquiry:
    ordinary: Q
    extra_yield: Q
    cost_curvature: Q
    discount: Q = Q(1)

    def __post_init__(self):
        assert 0 <= self.ordinary <= self.ordinary + self.extra_yield <= 1
        assert self.cost_curvature > 0 and 0 < self.discount <= 1

    def net_at(self, effort, release_value):
        discovery = self.ordinary + self.extra_yield * effort
        return self.discount * discovery * release_value - self.cost_curvature * effort**2 / 2

    def optimum(self, release_value):
        assert release_value >= 0
        effort = min(Q(1), self.discount * self.extra_yield * release_value / self.cost_curvature)
        return effort, self.net_at(effort, release_value)


def check_plans():
    cases = 0
    for gain, target, wage, version_cost in product((0, 3, 10), (0, 1, 2), (0, 1), (0, 2, 8)):
        release = Release(Q(gain), target, Q(wage), Q(version_cost))
        test_times = {"old": 2, "wide": 1}
        for sites, hours, separate in product(
            ((), ("old",), ("old", "old"), ("old", "wide"), ("wide", "old", "wide")),
            range(7), (False, True),
        ):
            legacy = sum(test_times[key] for key in set(sites))
            formula = release.value(hours, legacy, separate)
            measured = enumerate_validation(release, hours, sites, test_times, separate)
            assert formula == measured, (sites, hours, formula, measured)
            cases += 1

    # A paid release option cannot hurt if exercise is optional. A free separate
    # path removes this legacy burden; admitting new beneficiaries can reverse it.
    free_path = Release(Q(8), 1, Q(1), Q(0))
    assert free_path.value(2, 0, True) == free_path.value(2, 4, True) == 7
    old = Release(Q(8), 1, Q(1), Q(4))
    also_benefits_new_site = Release(Q(15), 1, Q(1), Q(4))
    assert also_benefits_new_site.value(5, 4, False) > old.value(5, 2, False)
    assert old.value(4, 4, False) == 0 < old.value(5, 4, False)
    prepaid = Release(Q(8), 1, Q(0), Q(3))
    assert prepaid.value(5, 0, True) == prepaid.value(5, 4, False) == 8
    return cases


def check_inquiry():
    cases = 0
    grid = [Q(k, 48) for k in range(49)]
    for ordinary in (Q(0), Q(1, 4), Q(3, 4), Q(1)):
        for extra, curvature, discount, release_value in product(
            (Q(0), (1-ordinary)/2, 1-ordinary), (Q(1), Q(3), Q(7)),
            (Q(2, 3), Q(1)), (Q(0), Q(3, 5), Q(3), Q(11)),
        ):
            inquiry = Inquiry(ordinary, extra, curvature, discount)
            effort, net = inquiry.optimum(release_value)
            discrete = max(inquiry.net_at(e, release_value) for e in grid)
            # A quadratic can lose at most kappa / (8 * grid_resolution^2)
            # on rounding to a nearest admissible grid point. Corners are exact.
            assert 0 <= net-discrete <= curvature / (8 * 48**2)
            if effort in grid:
                assert net == discrete
            if ordinary < 1:
                better_routine = Inquiry(ordinary + extra/2, extra/2, curvature, discount)
                new_effort, new_value = better_routine.optimum(release_value)
                assert new_effort <= effort and new_value >= net
            cases += 1

    # Fully assigned factorial comparison, including program-specific fixed costs.
    def payoff(s, r, inquiry_cost, setup_cost):
        return Q(9, 10)*s*r - inquiry_cost - setup_cost

    for base, enhanced in combinations([Q(1, 4), Q(1, 2), Q(3, 4), Q(1)], 2):
        for pooled, versioned in combinations([Q(0), Q(2), Q(3), Q(6)], 2):
            search_gain_v = payoff(enhanced, versioned, 2, 3) - payoff(base, versioned, 0, 3)
            search_gain_p = payoff(enhanced, pooled, 2, 0) - payoff(base, pooled, 0, 0)
            assert search_gain_v-search_gain_p == Q(9, 10)*(enhanced-base)*(versioned-pooled)

    # If every useful discovery comes after capacity expires, independent averages fail.
    events = [(Q(1, 2), 1, 0), (Q(1, 2), 0, 6)]
    joint = sum(p*hit*gain for p, hit, gain in events)
    product_of_means = sum(p*hit for p, hit, _ in events)*sum(p*gain for p, _, gain in events)
    assert joint == 0 < product_of_means
    return cases


def worked_fleet():
    wide = Release(Q(12), 1, Q(1), Q(5))
    local = Release(Q(7), 1, Q(1), Q(0))
    local_value = local.value(4, 0, False)
    wide_values = [wide.value(4, legacy, separate) for legacy, separate in ((2, False), (4, False), (4, True))]
    assert wide_values == [9, 0, 6] and local_value == 6
    assert [Q(1, 2)*v > Q(1, 4)*local_value for v in wide_values] == [True, False, True]

    inquiry = Inquiry(Q(1, 4), Q(3, 4), Q(6))
    effort, gross = inquiry.optimum(wide_values[2])
    assert (effort, gross) == (Q(3, 4), Q(51, 16))
    setup = Q(2)
    assert inquiry.net_at(Q(0), wide_values[2]) == Q(3, 2) < setup < gross
    legacy_value = max(inquiry.optimum(wide_values[1])[1], gross-setup)
    keep = Q(1, 2) + legacy_value
    # Removing the last old configuration makes the pooled route feasible again.
    fresh = wide.value(4, 2, False)
    test_cell = inquiry.optimum(fresh)[1] - 2
    limited = Inquiry(Q(1, 50), Q(1, 20), Q(6))
    sell = 1 + limited.optimum(fresh)[1]
    assert (keep, test_cell, sell) == (Q(27, 16), Q(4), Q(383, 320))
    assert test_cell > max(keep, sell)
    assert limited.optimum(fresh)[1] < legacy_value  # Easier release can lose useful exposure.
    # If the test cell adds no evidence or release freedom, paid work dominates it.
    assert Q(1, 2)+inquiry.optimum(fresh)[1] > test_cell

    for s, new_s, r, new_r in product((Q(1, 4), Q(3, 4)), (Q(1, 3), Q(2, 3)), (0, 3, 6), (0, 2, 7)):
        assert new_s*new_r-s*r == (new_s-s)*new_r+s*(new_r-r)
        assert new_s*new_r-s*r == s*(new_r-r)-(s-new_s)*new_r
    return wide_values, (keep, test_cell, sell)


def check_variety():
    """Count events directly, then test the threshold rule and both comparative statics."""
    sources = 5
    hit_counts = {}
    for per_site in (Q(1, 5), Q(1, 3), Q(3, 5)):
        for k in range(sources + 1):
            # Each independent source may or may not reveal the focal rule.
            hits = Q(0)
            for outcomes in product((0, 1), repeat=k):
                if any(outcomes):
                    count = sum(outcomes)
                    hits += per_site**count * (1-per_site)**(k-count)
            hit_counts[per_site, k] = hits
    checks = 0
    optima = {}
    for per_site, routine, cost in product((Q(1, 5), Q(1, 3), Q(3, 5)),
                                           (Q(0), Q(1, 4), Q(3, 4), Q(1)),
                                           (Q(0), Q(1, 2), Q(1), Q(3, 2))):
        reward = Q(10)
        rates = [routine+(1-routine)*hit_counts[per_site, k] for k in range(sources + 1)]
        gross = [s * (reward-cost*k) for k, s in enumerate(rates)]
        increments = []
        for k in range(sources):
            assert rates[k] == 1-(1-routine)*(1-per_site)**k
            predicted = (1-rates[k])*per_site*(reward-cost*(k+1)) - rates[k]*cost
            assert gross[k+1]-gross[k] == predicted
            increments.append(predicted)
        assert all(a >= b for a, b in zip(increments, increments[1:]))
        best = gross.index(max(gross))
        assert best == sum(gain > 0 for gain in increments)
        optima[per_site, routine, cost] = best
        checks += 1
    for per_site, routine, cost in optima:
        for (u, s, c), k in optima.items():
            if u == per_site and s >= routine and c >= cost:
                assert k <= optima[per_site, routine, cost]
    # Witness strict changes at an interior optimum.
    assert optima[Q(1, 3), Q(0), Q(1)] > optima[Q(1, 3), Q(3, 4), Q(1)]
    assert optima[Q(1, 3), Q(1, 4), Q(1, 2)] > optima[Q(1, 3), Q(1, 4), Q(3, 2)]
    # Equal-probability field states. A high-yield duplicate adds less than a rarer site.
    existing, duplicate, rare = {0, 1, 2}, {0, 1, 2}, {3}
    assert len(duplicate)>len(rare) and len(duplicate-existing)<len(rare-existing)
    # If a diagnostic needs *both* pieces, marginal value can rise with the portfolio.
    def paired_evidence(selected):
        return int({"trace", "outcome"}.issubset(selected))
    assert paired_evidence({"trace"}) == paired_evidence({"outcome"}) == 0
    assert paired_evidence({"trace", "outcome"}) == 1
    return checks


def migration_game():
    tested = 0
    for n in (2, 3):
        shares = [Q(1, 2**(i+1)) for i in range(n)]
        for benefit, costs in product((Q(1), Q(4), Q(8)), product((Q(1, 2), Q(2), Q(3)), repeat=n)):
            def utilities(moves):
                complete = all(moves)
                return [share*benefit*complete - cost*move for share, cost, move in zip(shares, costs, moves)]
            profiles = list(product((False, True), repeat=n))
            pure = []
            for moves in profiles:
                before = utilities(moves)
                gains = []
                for i in range(n):
                    changed = list(moves)
                    changed[i] = not changed[i]
                    gains.append(utilities(changed)[i]-before[i])
                if max(gains) <= 0:
                    pure.append(moves)
                if not any(moves):
                    assert max(gains) < 0
            predicted = [profiles[0]]
            if all(share*benefit >= cost for share, cost in zip(shares, costs)):
                predicted.append(profiles[-1])
            assert set(pure) == set(predicted)
            # Allow for value retained by a sponsor or other firms outside the group.
            def joint(moves):
                return benefit*all(moves) - sum(c*m for c, m in zip(costs, moves))
            assert max(map(joint, profiles)) == max(Q(0), benefit-sum(costs))
            transfers = [max(Q(0), c-share*benefit) for c, share in zip(costs, shares)]
            assert all(share*benefit+payment >= c for c, share, payment in zip(costs, shares, transfers))
            for i, payment in enumerate(transfers):
                if payment:
                    assert shares[i]*benefit+payment == costs[i]
            tested += 1
    return tested


def stationary_policy_values(policy, flows, switching_costs, discount):
    """Solve two linear equations for a policy choosing next period's configuration."""
    rewards = [flows[s] - (switching_costs[s] if policy[s] != s else 0) for s in range(2)]
    a = 1-discount*(policy[0] == 0)
    b = -discount*(policy[0] == 1)
    c = -discount*(policy[1] == 0)
    d = 1-discount*(policy[1] == 1)
    determinant = a*d-b*c
    return ((d*rewards[0]-b*rewards[1])/determinant, (a*rewards[1]-c*rewards[0])/determinant)


def check_histories():
    cases = 0
    for discount, to_new, to_old in product((Q(1, 2), Q(3, 4), Q(9, 10)), (Q(1), Q(3)), (Q(1), Q(2))):
        high = (1-discount)*to_new/discount
        low = -(1-discount)*to_old/discount
        for flow_gap in (low-1, low, low/2, Q(0), high/2, high, high+1):
            flows = (Q(3), Q(3)+flow_gap)
            costs = (to_new, to_old)
            pairs = [stationary_policy_values(p, flows, costs, discount) for p in product((0, 1), repeat=2)]
            v = [max(x[s] for x in pairs) for s in range(2)]
            for s in range(2):
                gain = -costs[s] + discount*(v[1-s]-v[s])
                switch_advantage = flow_gap-high if s == 0 else low-flow_gap
                assert (gain > 0, gain == 0) == (switch_advantage > 0, switch_advantage == 0)
                assert v[s] == flows[s] + max(discount*v[s], -costs[s]+discount*v[1-s])
            cases += 1
    return cases


def check_competition():
    cases = 0
    for q_e, q_i in product((Q(0), Q(1, 4), Q(1, 2), Q(1)), repeat=2):
        low, high = max(Q(0), q_e+q_i-1), min(q_e, q_i)
        for both in {low, (low+high)/2, high}:
            outcomes = [1-q_e-q_i+both, q_e-both, q_i-both, both]
            assert min(outcomes) >= 0 and sum(outcomes) == 1
            assert outcomes[1]-outcomes[2] == q_e-q_i
            cases += 1

    # The incumbent discovers more, yet depends on the one spacious window.
    # The alternate path's upfront cost exceeds its maximum possible incremental receipt.
    incumbent = Release(Q(12), 1, Q(1), Q(5))
    s_i, s_e = Q(4, 5), Q(1, 2)
    capacities = [(Q(2, 3), 3), (Q(1, 3), 5)]
    gross_option = s_i*sum(p*(incumbent.value(h, 4, True)-incumbent.value(h, 4, False)) for p, h in capacities)
    assert 10 > gross_option
    q_i = s_i*sum(p for p, h in capacities if incumbent.value(h, 4, False)>0)
    assert s_e < s_i and q_i == Q(4, 15) < s_e
    return cases


if __name__ == "__main__":
    plans = check_plans()
    inquiry = check_inquiry()
    release_values, asset_values = worked_fleet()
    portfolios = check_variety()
    games = migration_game()
    histories = check_histories()
    joint = check_competition()
    print(f"Release plans versus independent test scheduling: {plans} cases.")
    print(f"Inquiry optima versus discrete effort choices: {inquiry} cases.")
    print(f"Fleet-variety comparisons: {portfolios}.")
    print(f"Retirement games: {games}; switching comparisons: {histories}; joint supplier distributions: {joint}.")
    print("Shared discovery after one class / two classes / isolated release:", [str(x) for x in release_values])
    print("Paid operation / independent test cell / sale, including inquiry:", [str(x) for x in asset_values])
