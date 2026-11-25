"""Run with Python 3. Print results for the analytic restrictions in README.md."""
import json
from dataclasses import dataclass
from itertools import combinations, product
from math import inf, log, prod


LAYERS = "HMD"
BOUNDARIES = tuple(
    "".join(parts) for size in range(4) for parts in combinations(LAYERS, size)
)
STATES = tuple(product(BOUNDARIES, (False, True)))
ENTRY = {"H": 5.0, "M": 3.0, "D": 2.0}
EXIT = {"H": 2.0, "M": 1.0, "D": 1.0}
OVERHEAD = {"H": 1.3, "M": 1.4, "D": 1.0}
DISCOUNT = 0.88
RELIABILITY_PROMISE = 0.54
VINTAGE_CHANGE = 0.20


def coverage(portfolio, probabilities, external, blackout, response):
    """One common failure. Outside evidence is independent of the local blackout."""
    local_miss = prod((1 - p) ** n for n, p in zip(portfolio, probabilities))
    miss = (1 - external) * (blackout + (1 - blackout) * local_miss)
    return response * (1 - miss)


def required_log_coverage(target, external, blackout, response):
    if target <= response * external:
        return 0.0
    ceiling = response * (1 - (1 - external) * blackout)
    if target >= ceiling:
        return inf
    # Interior branch with p_j < 1. Identically saturated cases have returned above.
    ratio = (ceiling - target) / (response * (1 - external) * (1 - blackout))
    return -log(ratio)


def switching_cost(old, new, free):
    if free:
        return 0.0
    return (sum(ENTRY[s] for s in new if s not in old)
            + sum(EXIT[s] for s in old if s not in new))


@dataclass(frozen=True)
class Plan:
    sites: tuple
    vendor_panel: bool
    portability_test: bool
    flow: float
    next_portable: float
    timely_qualification: float


def feasible_plans(boundary, portable, review_hours, reliability):
    """Two markets. One obligation to qualify a common change in each release window."""
    hardware = 0.96 if "H" in boundary else (0.94 if portable else 0.70)
    model = 0.95 if "M" in boundary else (0.93 if portable else 0.73)
    blackout = 0.08 if "D" in boundary else (0.14 if portable else 0.26)
    response = hardware * model
    overhead = sum(OVERHEAD[s] for s in boundary)
    survival = (1 - VINTAGE_CHANGE) if portable else 0.0
    # Idle service: core operations outside this product are the zero comparator.
    plans = [Plan((0, 0), False, False, -overhead, survival, 0.0)]
    for first, second in product(range(5), range(4)):
        if first + second == 0 or first + 2 * second > 7:
            continue
        for panel, test in product((False, True), repeat=2):
            # Cash per site is 1 or 2. Review is a separate constraint, also
            # charging one fixed release hour and one hour for a portability test.
            if 1 + first + 2 * second + int(test) > review_hours:
                continue
            timely = coverage((first, second), (0.25, 0.55),
                              0.40 if panel else 0.12, blackout, response)
            if timely < reliability:
                continue
            # Site margins include fallback. A timely release adds real savings.
            flow = (3.2 * first + 2.8 * second + (first + second) * timely
                    - 1.0 - overhead - 0.8 * panel - 0.6 * test)
            if flow < 0:
                continue
            # A carried test survives ordinary vintages. In its absence, or
            # after a vintage change, a fresh matched test can establish it.
            new_test = 0.85 * timely if test else 0.0
            next_portable = survival + (1 - survival) * new_test
            plans.append(Plan((first, second), panel, test, flow, next_portable, timely))
    return plans


def solve(review_hours=8, reliability=RELIABILITY_PROMISE, free_switching=False):
    menus = {state: feasible_plans(*state, review_hours, reliability) for state in STATES}
    values = dict.fromkeys(STATES, 0.0)
    for _ in range(1000):
        best_inside = {}
        for (boundary, portable), plans in menus.items():
            low, high = values[boundary, False], values[boundary, True]

            def payoff(plan):
                continuation = low + plan.next_portable * (high - low)
                return plan.flow + DISCOUNT * continuation

            choice = max(plans, key=payoff)
            best_inside[boundary, portable] = payoff(choice), choice
        next_values, policy = {}, {}
        for old, portable in STATES:
            # Prefer the incumbent arrangement at exact ties.
            options = (old,) + tuple(g for g in BOUNDARIES if g != old)

            def net_value(g):
                return best_inside[g, portable][0] - switching_cost(old, g, free_switching)

            chosen = max(options, key=net_value)
            next_values[old, portable] = net_value(chosen)
            policy[old, portable] = chosen, best_inside[chosen, portable][1]
        residual = max(abs(next_values[s] - values[s]) for s in STATES)
        values = next_values
        if residual < 1e-10:
            return values, policy, residual
    raise ArithmeticError("Discounted value iteration did not reach tolerance")


def check_coverage():
    checked = 0
    for counts in product(range(3), repeat=2):
        rates = (0.25,) * counts[0] + (0.55,) * counts[1]
        for external, blackout, response in product((0, 0.25, 1), (0, 0.4, 1), (0, 0.8, 1)):
            direct = 0.0
            for outside, blind, timely in product((False, True), repeat=3):
                weight = prod(p if flag else 1 - p for flag, p in
                              zip((outside, blind, timely), (external, blackout, response)))
                for hits in product((False, True), repeat=len(rates)):
                    if timely and (outside or (not blind and any(hits))):
                        direct += weight * prod(p if flag else 1 - p for flag, p in zip(hits, rates))
            expected = coverage(counts, (0.25, 0.55), external, blackout, response)
            assert abs(expected - direct) < 1e-12
            evidence = -sum(log(1 - p) for p in rates)
            for target in (0, 0.2, 0.54, 0.7, 1):
                threshold = required_log_coverage(target, external, blackout, response)
                assert (expected + 1e-12 >= target) == (evidence + 1e-12 >= threshold)
                checked += 1
    return checked


def check_ownership_bounds():
    for cases in product(BOUNDARIES, repeat=3):
        counts = [sum(layer in route for route in cases) for layer in LAYERS]
        complete = cases.count("HMD")
        assert max(0, sum(counts) - 2 * len(cases)) <= complete <= min(counts)
    for cases, expected in [(("HM", "HD", "MD"), 0), (("HMD", "HMD", ""), 2)]:
        assert all(sum(layer in route for route in cases) == 2 for layer in LAYERS)
        assert cases.count("HMD") == expected


def fixed_boundary_minima(review_hours, reliability):
    # Keep the same positive portfolio through either interface state. Activities
    # (including purchase of the vendor panel) may respond to the interface.
    feasible = {}
    for boundary in BOUNDARIES:
        unresolved = feasible_plans(boundary, False, review_hours, reliability)
        portable = feasible_plans(boundary, True, review_hours, reliability)
        common = {p.sites for p in unresolved} & {p.sites for p in portable}
        common.discard((0, 0))
        if common:
            feasible[boundary] = common
    minimal_boundaries = [
        g for g in feasible if not any(set(other) < set(g) for other in feasible)
    ]

    def smallest_portfolios(candidates):
        return sorted(n for n in candidates if not any(
            other != n and all(a <= b for a, b in zip(other, n)) for other in candidates
        ))

    return {
        "minimal_ownership_sets_and_their_minimal_portfolios": {
            g or "external": smallest_portfolios(feasible[g]) for g in minimal_boundaries
        },
        "minimal_portfolios_if_fully_internal": smallest_portfolios(feasible.get("HMD", set())),
    }


def summarize(available_hours, reliability):
    values, policy, residual = solve(available_hours, reliability)
    labels = {}
    for initial in BOUNDARIES:
        rows = {}
        for portable in (False, True):
            boundary, plan = policy[initial, portable]
            rows["portable" if portable else "unresolved"] = {
                "chosen_ownership": boundary or "external",
                "committed_sites_by_market": plan.sites,
                "completed_paid_batches_with_fallback": sum(plan.sites),
                "timely_qualification_probability": round(plan.timely_qualification, 4),
                "expected_recovery_cost_saved": round(sum(plan.sites) * plan.timely_qualification, 4),
                "operating_contribution_before_switch_cost": round(plan.flow, 4),
                "vendor_panel": plan.vendor_panel,
                "portability_test": plan.portability_test,
                "probability_portable_next_date": round(plan.next_portable, 4),
                "discounted_private_value": round(values[initial, portable], 3),
            }
        labels[initial or "external"] = rows
    return {"review_hours": available_hours, "required_reliability": reliability,
            "fixed_boundary_minima": fixed_boundary_minima(available_hours, reliability),
            "bellman_residual": residual, "starting_positions": labels}


def main():
    check_ownership_bounds()
    free, _, _ = solve(free_switching=True)
    for portable in (False, True):
        assert max(free[g, portable] for g in BOUNDARIES) - min(
            free[g, portable] for g in BOUNDARIES) < 1e-9
    print(json.dumps({
        "scope": "Constructed stationary economies. Eight initial ownership sets at each interface state.",
        "coverage_and_threshold_checks": check_coverage(),
        "ordinary_review_capacity": summarize(8, RELIABILITY_PROMISE),
        "scarce_review_capacity": summarize(6, RELIABILITY_PROMISE),
        "stricter_service_promise": summarize(8, 0.76),
    }, indent=2))


if __name__ == "__main__":
    main()
