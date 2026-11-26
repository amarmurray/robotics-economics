"""Price a retained organizational procedure with fixed executors. Python 3."""
from dataclasses import dataclass, replace
from fractions import Fraction as F
from itertools import product
import json
from math import sqrt
from random import Random
from statistics import mean, stdev


OPTIONS = {"ordinary": (0, 0), "reference": (1, 0), "reserved_revision": (0, 1), "both": (1, 1)}
RESEARCH_PROGRAMS = {"broad": (F(1, 2), F(4, 5)), "focused": (F(4, 5), F(1, 4))}


@dataclass(frozen=True)
class World:
    lag: int = 1
    beta: F = F(19, 20)
    retention: F = F(4, 5)
    source_accuracy: F = F(9, 10)
    expected_persistence: F = F(4, 5)  # Correlation, not the probability of no flip
    actual_persistence: F = F(4, 5)
    claim: F = F(24)
    test_cost: F = F(4)
    local_accuracy: F = F(7, 10)
    local_premium: F = F(3)
    additional_reentry_delay: int = 0


def sign_accuracy(source_accuracy, persistence, lag):
    return (1 + (2 * source_accuracy - 1) * persistence ** lag) / 2


def accuracy_from_histories(source_accuracy, persistence, lag):
    """Enumerate convention changes. Symmetry permits fixing the source type."""
    stay = (1 + persistence) / 2
    total = F(0)
    for changes in product((False, True), repeat=lag):
        flips = sum(changes)
        weight = stay ** (lag - flips) * (1 - stay) ** flips
        matching_signal = source_accuracy if flips % 2 == 0 else 1 - source_accuracy
        total += weight * matching_signal
    return total


def target_decision(world, has_procedure):
    """Choose once on anticipated conditions. Score that choice under actual drift."""
    actions = [
        ("fallback", F(0), F(0)),
        ("ordinary_test", world.claim / 2 - world.test_cost, world.claim / 2 - world.test_cost),
    ]
    local = world.claim * world.local_accuracy - world.test_cost - world.local_premium
    actions.append(("local_specialist", local, local))
    if has_procedure:
        expected = sign_accuracy(world.source_accuracy, world.expected_persistence, world.lag)
        actual = sign_accuracy(world.source_accuracy, world.actual_persistence, world.lag)
        if expected < F(1, 2):
            expected, actual = 1 - expected, 1 - actual
        actions.append(("carried_test_selector", world.claim * expected - world.test_cost,
                        world.claim * actual - world.test_cost))
    return max(actions, key=lambda action: action[1])


def evaluate(world, name):
    reference, revision = OPTIONS[name]
    ready = 6 - 2 * reference - 3 * revision + world.additional_reentry_delay
    ordinary_job, matched_job = int(ready <= 4), int(ready <= 2)
    operating = 5 * ordinary_job + matched_job
    fee = 2 * reference + 3 * revision
    chance = matched_job * world.retention
    _, ordinary_expected, ordinary_actual = target_decision(world, False)
    rule, expected, actual = target_decision(world, True)
    scale = world.beta ** world.lag * chance
    return {
        "ready_at": ready,
        "incremental_current_orders": ordinary_job + matched_job,
        "current_operating_contribution": operating,
        "standing_cost": fee,
        "probability_of_retained_procedure": chance,
        "target_choice_if_procedure_available": rule,
        "discounted_target_gain_over_ordinary": scale * (actual - ordinary_actual),
        "anticipated_net_gain": operating - fee + scale * (expected - ordinary_expected),
        "net_gain_over_ordinary": operating - fee + scale * (actual - ordinary_actual),
    }


def interaction(rows, key):
    return rows["both"][key] - rows["reference"][key] - rows["reserved_revision"][key] + rows["ordinary"][key]


def describe(world):
    rows = {name: evaluate(world, name) for name in OPTIONS}
    def best(key):
        top = max(row[key] for row in rows.values())
        return [name for name, row in rows.items() if row[key] == top]
    return {
        "lag": world.lag, "assumed_persistence": world.expected_persistence,
        "actual_persistence": world.actual_persistence, "claim": world.claim,
        "retention": world.retention, "extra_delay": world.additional_reentry_delay,
        "target_ordinary_rule": target_decision(world, False)[0],
        "chosen_at_planning_law": best("anticipated_net_gain"),
        "best_in_hindsight_among_scored_programs": best("net_gain_over_ordinary"),
        "operating_interaction": interaction(rows, "current_operating_contribution"),
        "net_interaction": interaction(rows, "net_gain_over_ordinary"),
        "programs": rows,
    }


def successor_value(resolution, reusable, later_stakes, allow_pass):
    """Generation two earns on resolution, then can invest to qualify its successor."""
    operating = resolution * 8 - 2
    conversion = max(F(0), F(19, 20) * reusable * later_stakes - 1) if allow_pass else F(0)
    return operating + resolution * conversion


def successor_study():
    out = {}
    for stakes in (0, 8, 16):
        rows = {}
        for name, (p, e) in RESEARCH_PROGRAMS.items():
            rows[name] = {
                "current_net": successor_value(p, e, stakes, False),
                "with_successor_option": successor_value(p, e, stakes, True),
            }
        current_gap = rows["focused"]["current_net"] - rows["broad"]["current_net"]
        total_gap = rows["focused"]["with_successor_option"] - rows["broad"]["with_successor_option"]
        rows["focused_minus_broad_current"] = current_gap
        rows["focused_minus_broad_total"] = total_gap
        rows["effect_on_value_of_passing_successor"] = total_gap - current_gap
        out[str(stakes)] = rows
    assert out["8"]["focused_minus_broad_total"] == F(58, 100)
    assert out["16"]["focused_minus_broad_total"] == -F(94, 100)
    return out


def recipient_feedback(return_rate):
    """Uncongested uses, fixed prices, one incremental informative return trace."""
    # Net value before the new method already includes the buy/operate alternative.
    recipients = ((3, 4, 2), (-2, 7, 3))  # incumbent net, method gain, posted fee
    fees, new_machines, users = 0, 0, 0
    for incumbent_net, method_gain, posted_fee in recipients:
        use = incumbent_net + method_gain - posted_fee > max(0, incumbent_net)
        if use:
            users += 1
            fees += posted_fee
            new_machines += int(incumbent_net < 0)
    assert new_machines == 1
    stakes = fees + new_machines * (3 + 16 * return_rate)
    chosen = max(RESEARCH_PROGRAMS, key=lambda name: successor_value(*RESEARCH_PROGRAMS[name], stakes, True))
    p, e = RESEARCH_PROGRAMS[chosen]
    invest = F(19, 20) * e * stakes > 1
    return {"users_if_method_qualifies": users, "new_machines_if_method_qualifies": new_machines,
            "usable_return_trace_probability_if_installed": return_rate,
            "source_stakes_at_generation_three": stakes, "chosen_program": chosen,
            "current_resolution_probability": p,
            "expected_induced_machines": p * invest * e * new_machines}


def fresh_histories(world, seed_base, worlds=64, cohorts=600):
    """Independent synthetic panels; couple the four programs within a cohort."""
    r, q = float(world.source_accuracy), float(world.retention)
    stay = (1 + float(world.actual_persistence)) / 2
    invert = sign_accuracy(world.source_accuracy, world.expected_persistence, world.lag) < F(1, 2)
    baseline = target_decision(world, False)[0]
    carried = target_decision(world, True)[0]
    margin, fee, premium = float(world.claim), float(world.test_cost), float(world.local_premium)
    rows = {n: evaluate(world, n) for n in OPTIONS}
    early = {n: int(row["ready_at"] <= 2) for n, row in rows.items()}
    trace_interaction = early["both"] - early["reference"] - early["reserved_revision"] + early["ordinary"]
    operating = float(interaction(rows, "current_operating_contribution"))
    estimates = []
    for i in range(worlds):
        rng = Random(seed_base + i)
        increments = 0.0
        for _ in range(cohorts):
            licensed = rng.random() < q
            signal_correct = rng.random() < r
            for _ in range(world.lag):
                if rng.random() >= stay:
                    signal_correct = not signal_correct
            realized = {
                "fallback": 0.0,
                "ordinary_test": margin * (rng.random() < 0.5) - fee,
                "local_specialist": margin * (rng.random() < float(world.local_accuracy)) - fee - premium,
                "carried_test_selector": margin * (signal_correct != invert) - fee,
            }
            if licensed:
                increments += realized[carried] - realized[baseline]
        estimates.append(operating + float(world.beta ** world.lag) * trace_interaction * increments / cohorts)
    return {"worlds": worlds, "cohorts_per_world": cohorts, "first_seed": seed_base,
            "mean_interaction": round(mean(estimates), 4),
            "monte_carlo_se_across_world_means": round(stdev(estimates) / sqrt(worlds), 4)}


def checks():
    for r, kappa, lag in product((F(1, 2), F(3, 4), F(9, 10), F(1)),
                                 (F(-1), F(-4, 5), F(0), F(4, 5), F(1)), range(1, 6)):
        assert sign_accuracy(r, kappa, lag) == accuracy_from_histories(r, kappa, lag)
    for ready, first, second, deadline in product(range(7), range(4), range(4), range(9)):
        lead_needed = ready - deadline
        joint = max(first, second) < lead_needed <= first + second
        either = 0 < lead_needed <= min(first, second)
        ends = {n: int(ready - d * first - a * second <= deadline) for n, (d, a) in OPTIONS.items()}
        assert ends["both"] - ends["reference"] - ends["reserved_revision"] + ends["ordinary"] == joint - either
    for lag, claim, premium, q in product(range(1, 6), (F(6), F(24), F(48)),
                                           (F(0), F(3)), (F(0), F(4, 5), F(1))):
        w = World(lag=lag, claim=claim, local_premium=premium, retention=q)
        rows = {name: evaluate(w, name) for name in OPTIONS}
        incumbent = target_decision(w, False)[1]
        forecast = max(F(0), w.claim * sign_accuracy(w.source_accuracy, w.actual_persistence, lag)
                       - w.test_cost - incumbent)
        assert interaction(rows, "net_gain_over_ordinary") == -4 + w.beta ** lag * q * forecast


def main():
    checks()
    w = World()
    cases = {"one_release": w, "two_releases": replace(w, lag=2),
             "five_releases": replace(w, lag=5), "rights_expire": replace(w, retention=F(0)),
             "quarter_claim": replace(w, claim=F(6)),
             "routine_matches_procedure": replace(w, local_accuracy=F(82, 100), local_premium=F(0)),
             "unannounced_reversal": replace(w, actual_persistence=F(-4, 5)),
             "anticipated_reversal": replace(w, expected_persistence=F(-4, 5), actual_persistence=F(-4, 5)),
             "two_day_tooling_delay": replace(w, additional_reentry_delay=2)}
    out = {name: describe(world) for name, world in cases.items()}
    assert out["one_release"]["net_interaction"] == F(4688, 10000)
    assert out["two_releases"]["net_interaction"] < 0
    assert out["two_releases"]["chosen_at_planning_law"] == ["both"]
    assert out["five_releases"]["chosen_at_planning_law"] == ["reference"]
    panels = {name: fresh_histories(cases[name], 26000 + 100 * i)
              for i, name in enumerate(("one_release", "two_releases", "unannounced_reversal", "quarter_claim"))}
    feedback = {name: recipient_feedback(rate) for name, rate in
                (("no_return_right", F(0)), ("licensed_and_informative_half_the_time", F(1, 2)))}
    assert feedback["no_return_right"]["expected_induced_machines"] == F(1, 5)
    assert feedback["licensed_and_informative_half_the_time"]["expected_induced_machines"] == F(2, 5)
    print(json.dumps({"successor_routines": successor_study(), "recipient_feedback": feedback, "reentry": out,
                      "independent_synthetic_panels": panels}, indent=2, default=float))


if __name__ == "__main__":
    main()
