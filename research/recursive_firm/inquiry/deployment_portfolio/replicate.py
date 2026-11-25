"""Check the portfolio identities and bound source interactions in Open X Table II.

Pass this script's path to Python 3. Source scores are expressed in percent and
reported in https://arxiv.org/html/2310.08864v9, Table II, rows 1 to 3.
No trial-level outcomes or estimated discovery probabilities are used.
"""

import csv
import json
from decimal import Decimal
from fractions import Fraction
from itertools import product
from pathlib import Path


HERE = Path(__file__).resolve().parent
SOURCE = "https://arxiv.org/html/2310.08864v9"
ACCESS = ((False, False), (True, False), (False, True), (True, True))


def interaction(values):
    return values[True, True] - values[True, False] - values[False, True] + values[False, False]


def check_source_and_recipient_values():
    """Pointwise checks imply the expectation identity for every joint event law."""
    histories_checked = 0
    for incumbent, source_i, source_j in product((False, True), repeat=3):
        unique_i = not incumbent and source_i
        i_only = unique_i and not source_j
        j_only = not incumbent and source_j and not source_i
        both = unique_i and source_j
        for incumbent_value, use_i, use_j in product((0, 2, 9), repeat=3):
            payouts = {}
            for add_i, add_j in ACCESS:
                qualified = incumbent or (add_i and source_i) or (add_j and source_j)
                eligible_value = incumbent_value + add_i * use_i + add_j * use_j
                payouts[add_i, add_j] = eligible_value * qualified
            predicted_gain = use_i * incumbent + unique_i * (incumbent_value + use_i)
            assert payouts[True, False] - payouts[False, False] == predicted_gain
            predicted_interaction = use_j * i_only + use_i * j_only - incumbent_value * both
            assert interaction(payouts) == predicted_interaction
            histories_checked += 1
    return histories_checked


def check_receiver_expansion():
    """A new receiver may have different release dates and source permissions."""
    schedules_checked = 0
    for ordinary, date_i, date_j in product((0, 1, 2, None), repeat=3):
        for grant_i, grant_j in ACCESS:
            receipts = dict.fromkeys(ACCESS, Fraction(0))
            redundant_value = Fraction(0)
            for date, work_value in enumerate((2, 0, 5)):
                discounted_value = Fraction(3, 4) ** date * work_value
                ordinary_ready = ordinary is not None and ordinary <= date
                i_ready = grant_i and date_i is not None and date_i <= date
                j_ready = grant_j and date_j is not None and date_j <= date
                if not ordinary_ready and i_ready and j_ready:
                    redundant_value += discounted_value
                for add_i, add_j in ACCESS:
                    ready = ordinary_ready or (add_i and i_ready) or (add_j and j_ready)
                    if ready:
                        receipts[add_i, add_j] += discounted_value
            assert interaction(receipts) == -redundant_value
            schedules_checked += 1
    return schedules_checked


def check_joint_evidence():
    """Enumerate qualification rules for two sources, including joint necessity."""
    by_sign = {"negative": 0, "zero": 0, "positive": 0}
    for neither, only_i, only_j, together in product((0, 1), repeat=4):
        if neither > min(only_i, only_j) or max(only_i, only_j) > together:
            continue
        qualified = dict(zip(ACCESS, (neither, only_i, only_j, together)))
        joint_requirement = (neither, only_i, only_j, together) == (0, 0, 0, 1)
        duplication = (neither, only_i, only_j, together) == (0, 1, 1, 1)
        actual = interaction(qualified)
        assert actual == int(joint_requirement) - int(duplication)
        by_sign[{-1: "negative", 0: "zero", 1: "positive"}[actual]] += 1
    return by_sign


def check_audit_thresholds():
    """Compare the two action menus with the predicted value across all regions."""
    checks = 0
    cost = Fraction(2)
    for low, high in ((Fraction(1, 5), Fraction(3, 5)), (Fraction(1, 3), Fraction(1))):
        for prior in (Fraction(1, 4), Fraction(1, 2), Fraction(3, 4)):
            mean = (1 - prior) * low + prior * high
            left, peak, right = cost / high, cost / mean, cost / low
            stakes = (0, left, (left + peak) / 2, peak, (peak + right) / 2, right, 2 * right)
            for work in stakes:
                gain_low = low * work - cost
                gain_high = high * work - cost
                informed = (1 - prior) * max(0, gain_low) + prior * max(0, gain_high)
                ordinary = max(0, (1 - prior) * gain_low + prior * gain_high)
                if work <= left or work >= right:
                    predicted = 0
                elif work <= peak:
                    predicted = prior * gain_high
                else:
                    predicted = -(1 - prior) * gain_low
                assert informed - ordinary == predicted
                checks += 1
    return checks


def published_score_bounds():
    with (HERE / "open_x_cells.csv").open(newline="", encoding="utf-8") as source_file:
        rows = {int(row["source_table_row"]): row for row in csv.DictReader(source_file)}

    results = {}
    for suite in ("selected_emergent_skills_pct", "generalization_pct"):
        google, full, except_bridge = (Decimal(rows[row][suite]) for row in (1, 2, 3))
        intercept = full - except_bridge + google
        monotone = google <= except_bridge <= full
        monotone_bounds = None
        if monotone:
            # The absent Google + Bridge cell can range from the base to the full score.
            monotone_bounds = [float(intercept - full), float(intercept - google)]
        results[suite] = {
            "bridge_given_other_sources_pp": float(full - except_bridge),
            "interaction_zero_at_missing_score_pct": float(intercept),
            "unrestricted_interaction_interval_pp": [float(intercept - 100), float(intercept)],
            "monotone_point_estimates_feasible": monotone,
            "monotone_interaction_interval_pp": monotone_bounds,
        }
    return results


def main():
    result = {
        "source": SOURCE,
        "table": "II, 55B rows 1–3, reported percentages",
        "missing_protocol": "Google Robot action plus Bridge without the other added sources",
        "public_evaluations": published_score_bounds(),
        "algebra_checks": {
            "event_and_value_configurations": check_source_and_recipient_values(),
            "dated_source_and_rights_configurations": check_receiver_expansion(),
            "monotone_qualification_rules_by_interaction_sign": check_joint_evidence(),
            "audit_decision_threshold_cases": check_audit_thresholds(),
        },
    }
    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
