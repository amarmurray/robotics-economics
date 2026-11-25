"""Economic checks for the autonomous-firm note. Run with Python 3.

All production, demand, financing, and operating-cost assumptions are synthetic.
The fee illustration uses Tutor's public offer, not a signed customer contract:
https://tutorintelligence.com/pricing . The $15 comparison is Massachusetts's
general minimum employee wage: https://www.mass.gov/guides/pay-and-recordkeeping .
"""

import json
from math import isclose


def fixed_rate_case(elasticity, productivity_gain=2.0):
    """Unconstrained annual capacity, fixed task mix, direct service demand.

    The buyer pays per robot-hour. Demand for accepted units has constant
    elasticity with respect to the implied price per accepted unit. Human hours
    count routine remote operations only. Operating contributions deduct the
    provider's variable costs, including routine support, once.
    """
    hourly_rate = 14.0
    baseline_robot_hours = 2000.0
    baseline_units_per_hour = 10.0
    old_variable_cost, new_variable_cost = 10.0, 9.0
    old_human_intensity, new_human_intensity = 0.20, 0.10

    baseline_units = baseline_robot_hours * baseline_units_per_hour
    new_units = baseline_units * productivity_gain**elasticity
    new_robot_hours = new_units / (productivity_gain * baseline_units_per_hour)
    old_human_hours = old_human_intensity * baseline_robot_hours
    new_human_hours = new_human_intensity * new_robot_hours
    old_contribution = (hourly_rate - old_variable_cost) * baseline_robot_hours
    new_contribution = (hourly_rate - new_variable_cost) * new_robot_hours
    return {
        "demand_elasticity": elasticity,
        "old_and_new_accepted_units": [baseline_units, new_units],
        "old_and_new_robot_hours": [baseline_robot_hours, new_robot_hours],
        "old_and_new_routine_human_hours": [old_human_hours, new_human_hours],
        "old_and_new_human_share_of_unweighted_operating_hours": [
            old_human_hours / (baseline_robot_hours + old_human_hours),
            new_human_hours / (new_robot_hours + new_human_hours),
        ],
        "old_and_new_provider_operating_contribution": [old_contribution, new_contribution],
        "contribution_ratio": new_contribution / old_contribution,
    }


def hourly_fee_case(annual_run_hours):
    """Uniform monthly utilization; use a billed floor only if so contracted.

    Tutor states an 80-hour monthly minimum. Both reported scenarios exceed it,
    so a contractual eligibility threshold gives the same numbers as a billing
    floor. A refundable deposit ties up capital. Only its assumed carry enters
    cost. Setup is spread straight-line, with no financing charge on setup.
    """
    if annual_run_hours <= 0:
        raise ValueError("Annual run hours must be positive")
    robot_rate = 14.0
    monthly_minimum = 80.0
    implementation_fee = 10000.0
    years = 3.0
    refundable_deposit = 8000.0
    assumed_annual_carry = 0.06
    annual_billed_hours = 12 * max(monthly_minimum, annual_run_hours / 12)
    annual_bill = robot_rate * annual_billed_hours
    annual_implementation = implementation_fee / years
    annual_deposit_carry = refundable_deposit * assumed_annual_carry
    return {
        "annual_actual_run_hours": annual_run_hours,
        "monthly_actual_run_hours": annual_run_hours / 12,
        "annual_billed_robot_hours": annual_billed_hours,
        "annual_robot_usage_charge": annual_bill,
        "setup_cost_per_year": annual_implementation,
        "deposit_carry_per_year": annual_deposit_carry,
        "charge_plus_setup_and_carry_per_run_hour": (
            annual_bill + annual_implementation + annual_deposit_carry
        ) / annual_run_hours,
    }


def main():
    elasticities = (0.0, 0.5, 1.0, 2.0, 2.5)
    cases = {epsilon: fixed_rate_case(epsilon) for epsilon in elasticities}
    for epsilon, case in cases.items():
        old_h, new_h = case["old_and_new_robot_hours"]
        old_l, new_l = case["old_and_new_routine_human_hours"]
        assert isclose(new_h / old_h, 2 ** (epsilon - 1))
        assert isclose(new_l / old_l, 2 ** (epsilon - 2))
        assert isclose(case["contribution_ratio"], 1.25 * 2 ** (epsilon - 1))
    assert cases[0.5]["contribution_ratio"] < 1
    assert cases[2.5]["old_and_new_routine_human_hours"][1] > 400

    annual_hours = (1000, 4000)
    fee_cases = [hourly_fee_case(h) for h in annual_hours]
    assert all(isclose(c["annual_actual_run_hours"], c["annual_billed_robot_hours"]) for c in fee_cases)
    assert isclose(fee_cases[0]["charge_plus_setup_and_carry_per_run_hour"], 17.813333333333333)
    assert isclose(fee_cases[1]["charge_plus_setup_and_carry_per_run_hour"], 14.953333333333333)
    assert hourly_fee_case(600)["annual_billed_robot_hours"] == 960  # Hypothetical take-or-pay case.
    benchmark_hours = (10000 / 3 + 0.06 * 8000) / (15 - 14)
    assert isclose(hourly_fee_case(benchmark_hours)["charge_plus_setup_and_carry_per_run_hour"], 15)

    print(json.dumps({
        "synthetic_hourly_contract": list(cases.values()),
        "public_terms_with_synthetic_utilization_and_carry": fee_cases,
        "annual_run_hours_matching_wage_only_15_benchmark_at_equal_throughput": benchmark_hours,
        "excluded_from_fee_comparison": "Buyer complements, setup financing, differing accepted throughput or quality and fully loaded alternative labor cost; no inference of labor displacement.",
    }, indent=2))


if __name__ == "__main__":
    main()
