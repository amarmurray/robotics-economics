"""Checks for Deployment Portfolios and the Next Robot (November 25, 2026).

All parameter choices below are synthetic checks, not empirical calibration.
Run from any directory with Python 3, NumPy, and SciPy:
    python diagnostic_portfolios.py
The script writes diagnostic_portfolios_results.json beside itself.
"""

from __future__ import annotations

import itertools
import json
import math
from dataclasses import dataclass, replace
from pathlib import Path

import numpy as np
from scipy.integrate import quad


def pdf(z: float) -> float:
    return math.exp(-0.5 * z * z) / math.sqrt(2.0 * math.pi)


def cdf(z: float) -> float:
    return 0.5 * math.erfc(-z / math.sqrt(2.0))


@dataclass(frozen=True)
class Factory:
    prior_variance: float = 1.0
    prior_mean: float = 0.0
    base_margin: float = 0.9
    state_loading: float = 0.6
    mismatch_cost: float = 1.0
    expansion_cost: float = 1.0

    def moments(self, variance: float) -> tuple[float, float]:
        if not 0.0 <= variance <= self.prior_variance:
            raise ValueError("Posterior variance outside the prior range")
        mean = (self.base_margin + self.state_loading * self.prior_mean
                - self.mismatch_cost * variance)
        sd = abs(self.state_loading) * math.sqrt(self.prior_variance - variance)
        return mean, sd

    def value(self, variance: float) -> float:
        mean, sd = self.moments(variance)
        if sd == 0.0:
            return max(mean, 0.0) ** 2 / (2.0 * self.expansion_cost)
        z = mean / sd
        return ((mean * mean + sd * sd) * cdf(z)
                + mean * sd * pdf(z)) / (2.0 * self.expansion_cost)

    def expected_quantity(self, variance: float) -> float:
        mean, sd = self.moments(variance)
        if sd == 0.0:
            return max(mean, 0.0) / self.expansion_cost
        z = mean / sd
        return (mean * cdf(z) + sd * pdf(z)) / self.expansion_cost

    def probability_entry(self, variance: float) -> float:
        mean, sd = self.moments(variance)
        return float(mean > 0.0) if sd == 0.0 else cdf(mean / sd)

    def marginal_precision_value(self, variance: float) -> float:
        # Minus dH/ds, for an interior variance with positive signal dispersion.
        return (self.mismatch_cost * self.expected_quantity(variance)
                + self.state_loading ** 2 * self.probability_entry(variance)
                / (2.0 * self.expansion_cost))


def portfolio_variances(S: float, T: float, rA: float, rB: float) -> dict[str, float]:
    nuisance_after_A = T * rA / (T + rA)
    return {
        "none": S,
        "A": S,
        "B": S - S * S / (S + T + rB),
        "AB": S - S * S / (S + nuisance_after_A + rB),
    }


def matrix_posterior(S: float, T: float, rA: float, rB: float,
                     portfolio: str) -> np.ndarray:
    """Independent calculation from the joint Gaussian covariance formula."""
    prior = np.diag([S, T])
    if portfolio == "none":
        return prior
    rows = {"A": [[0.0, 1.0]], "B": [[1.0, 1.0]],
            "AB": [[0.0, 1.0], [1.0, 1.0]]}
    noise = {"A": [rA], "B": [rB], "AB": [rA, rB]}
    design = np.array(rows[portfolio])
    covariance_y = design @ prior @ design.T + np.diag(noise[portfolio])
    return prior - prior @ design.T @ np.linalg.solve(covariance_y, design @ prior)


def expect_by_integration(factory: Factory, variance: float) -> tuple[float, float]:
    """Directly integrate posterior-contingent decisions, not closed moments."""
    mean, sd = factory.moments(variance)
    if sd == 0.0:
        return factory.value(variance), factory.expected_quantity(variance)
    lower = -mean / sd
    value = quad(lambda z: ((mean + sd * z) ** 2
                           / (2.0 * factory.expansion_cost)) * pdf(z),
                 lower, np.inf, epsabs=1e-11, epsrel=1e-11)[0]
    quantity = quad(lambda z: ((mean + sd * z)
                              / factory.expansion_cost) * pdf(z),
                    lower, np.inf, epsabs=1e-11, epsrel=1e-11)[0]
    return value, quantity


def check_close(actual: float, expected: float, tol: float = 2e-9) -> None:
    if not math.isclose(actual, expected, rel_tol=tol, abs_tol=tol):
        raise AssertionError((actual, expected, tol))


def verify_and_report() -> dict:
    counts: dict[str, int] = {}
    posterior_error = 0.0
    counts["posterior_matrix_comparisons"] = 0
    for S, T, rA, rB in itertools.product([0.25, 1.0, 3.0], repeat=4):
        variances = portfolio_variances(S, T, rA, rB)
        assert variances["AB"] < variances["B"] < variances["A"]
        for portfolio, expected in variances.items():
            actual = matrix_posterior(S, T, rA, rB, portfolio)[0, 0]
            posterior_error = max(posterior_error, abs(actual - expected))
            check_close(actual, expected)
            counts["posterior_matrix_comparisons"] += 1

    counts["normal_moment_integrations"] = 0
    counts["shadow_value_derivatives"] = 0
    integration_error = 0.0
    derivative_error = 0.0
    for margin, loading, kappa, variance in itertools.product(
            [-0.3, 0.9, 2.0], [-0.8, 0.4, 1.2], [0.0, 0.5, 1.0], [0.15, 0.55, 0.9]):
        factory = Factory(base_margin=margin, state_loading=loading,
                          mismatch_cost=kappa, expansion_cost=1.3)
        integrated_value, integrated_quantity = expect_by_integration(factory, variance)
        for actual, expected in [(factory.value(variance), integrated_value),
                                 (factory.expected_quantity(variance), integrated_quantity)]:
            integration_error = max(integration_error, abs(actual - expected))
            check_close(actual, expected)
            counts["normal_moment_integrations"] += 1
        step = 1e-5
        derivative = (factory.value(variance + step) - factory.value(variance - step)) / (2 * step)
        predicted = -factory.marginal_precision_value(variance)
        derivative_error = max(derivative_error, abs(derivative - predicted))
        check_close(derivative, predicted, 2e-7)
        assert factory.value(variance - step) >= factory.value(variance + step) - 1e-12
        counts["shadow_value_derivatives"] += 1

    factory = Factory()
    beta = 0.95
    variances = portfolio_variances(1.0, 1.0, 0.25, 0.25)
    GB = beta * (factory.value(variances["B"]) - factory.value(1.0))
    GAB = beta * (factory.value(variances["AB"]) - factory.value(1.0))
    counts["portfolio_optimality_comparisons"] = 0
    for dA, dB in itertools.product(np.linspace(-0.1, 0.3, 41), repeat=2):
        values = {"none": 0.0, "A": -dA, "B": GB - dB, "AB": GAB - dA - dB}
        direct_pair_optimal = values["AB"] >= max(values.values()) - 1e-12
        inequality_pair_optimal = (dA + dB <= GAB + 1e-12
                                   and dA <= GAB - GB + 1e-12
                                   and dB <= GAB + 1e-12)
        assert direct_pair_optimal == inequality_pair_optimal
        counts["portfolio_optimality_comparisons"] += 1
    # Construct a strict complementarity example from the derived surplus gap.
    gap = GAB - GB
    dA, dB = 0.25 * gap, GB + 0.25 * gap
    pair_values = {"none": 0.0, "A": -dA, "B": GB - dB, "AB": GAB - dA - dB}
    assert pair_values["A"] < 0 and pair_values["B"] < 0 < pair_values["AB"]

    repetitions = []
    previous_increment = -math.inf
    for n in [1, 2, 4, 16, 256, 1000000]:
        v = portfolio_variances(1.0, 1.0, 0.25, 0.25 / n)
        incremental_A = v["B"] - v["AB"]  # W=1, before acquisition costs.
        assert incremental_A > previous_increment
        previous_increment = incremental_A
        independent_nuisance_variance = 1.0 - 1.0 / (1.0 + 1.25 / n)
        repetitions.append({"B_repetitions": n, "variance_with_B": v["B"],
                            "variance_with_AB": v["AB"],
                            "incremental_A_value_at_W_one": incremental_A,
                            "variance_if_nuisance_redrawn": independent_nuisance_variance})
    check_close(repetitions[-1]["variance_with_B"], 0.5, 1e-6)
    assert repetitions[-1]["variance_if_nuisance_redrawn"] < 2e-6

    # A signal about an independent nuisance cannot unlock B's records.
    S = T = 1.0
    rA = rB = 0.25
    joint = np.diag([S, T, T])  # target, B nuisance, unrelated A nuisance
    design = np.array([[1.0, 1.0, 0.0], [0.0, 0.0, 1.0]])
    noise = np.diag([rB, rA])
    posterior = joint - joint @ design.T @ np.linalg.solve(
        design @ joint @ design.T + noise, design @ joint)
    check_close(posterior[0, 0], variances["B"])

    # Exact finite-state counterexample: better information, less expected capital.
    # theta=+-1 equiprobably; m=2, a=3, kappa=1/4, gamma=1, N capped at one.
    prior_N = 1.0
    prior_value = (2.0 - 0.25) * prior_N - 0.5 * prior_N ** 2
    outcomes = []
    for theta in [-1.0, 1.0]:
        margin = 2.0 + 3.0 * theta
        N = min(1.0, max(0.0, margin))
        outcomes.append({"theta": theta, "design": theta, "quantity": N,
                         "value": margin * N - 0.5 * N * N})
    informed_N = sum(row["quantity"] for row in outcomes) / 2
    informed_value = sum(row["value"] for row in outcomes) / 2
    assert informed_N < prior_N and informed_value > prior_value

    # Correctly priced alternatives bound the value of diagnostic hardware.
    # One source hardware generation changes the cost of A for the next design.
    G = factory.value(variances["AB"]) - factory.value(variances["B"])
    c_onboard, c_external = 0.2 * G, 1.4 * G
    hardware_cost = 0.4 * beta * G
    premium = beta * (max(0.0, G - c_onboard) - max(0.0, G - c_external)) - hardware_cost
    assert premium > 0.0
    equal_alternative_premium = beta * (max(0.0, G - c_onboard) - max(0.0, G - c_onboard)) - hardware_cost
    check_close(equal_alternative_premium, -hardware_cost)
    one_generation_premium = -hardware_cost
    assert one_generation_premium < 0.0

    # Stronger timing: after B arrives, each hardware alternative can buy A
    # selectively. Keep the full conditional posterior, including correlation.
    sd_mean_after_B = math.sqrt(factory.prior_variance - variances["B"])

    def conditional_A_gain(z: float) -> float:
        mu_B = factory.prior_mean + sd_mean_after_B * z
        conditional_factory = replace(factory, prior_mean=mu_B,
                                      prior_variance=variances["B"])
        return (conditional_factory.value(variances["AB"])
                - conditional_factory.value(variances["B"]))

    # Ten standard deviations suffice here; the omitted polynomial-weighted
    # normal tail is below the comparison tolerance for these explicit inputs.
    def conditional_option(cost: float) -> float:
        return quad(lambda z: max(0.0, conditional_A_gain(z) - cost) * pdf(z),
                    -10.0, 10.0, points=[-2.0, -1.0, 0.0, 1.0, 2.0],
                    epsabs=1e-11, epsrel=1e-11, limit=300)[0]

    integrated_G = quad(lambda z: conditional_A_gain(z) * pdf(z),
                        -10.0, 10.0, epsabs=1e-11, epsrel=1e-11)[0]
    check_close(integrated_G, G)
    onboard_option = conditional_option(c_onboard)
    external_option = conditional_option(c_external)
    assert onboard_option >= max(0.0, G - c_onboard) - 1e-10
    assert external_option >= max(0.0, G - c_external) - 1e-10
    adaptive_premium = beta * (onboard_option - external_option) - hardware_cost
    assert adaptive_premium > 0.0
    assert adaptive_premium <= beta * (c_external - c_onboard) - hardware_cost + 1e-10

    # No payoff-relevant uncertainty means no value of information.
    zero_learning = Factory(state_loading=0.0, mismatch_cost=0.0)
    for variance in variances.values():
        check_close(zero_learning.value(variance), zero_learning.value(1.0))

    return {
        "status": "all_checks_passed",
        "scope": "Conditional theory checks; synthetic inputs; no empirical calibration or market equilibrium.",
        "counts": counts,
        "max_absolute_errors": {"posterior_matrix": posterior_error,
                                "normal_moment_integration": integration_error,
                                "shadow_value_derivative": derivative_error},
        "synthetic_strict_portfolio_complementarity": {
            "posterior_variances": variances, "G_B": GB, "G_AB": GAB,
            "d_A": dA, "d_B": dB, "net_values": pair_values},
        "repetition_and_information_direction": repetitions,
        "demand_cap_counterexample": {"prior_quantity": prior_N, "prior_value": prior_value,
                                      "informed_expected_quantity": informed_N,
                                      "informed_expected_value": informed_value,
                                      "state_contingent_decisions": outcomes},
        "two_hardware_generations": {"future_incremental_A_value": G,
                                     "onboard_A_cost": c_onboard, "external_A_cost": c_external,
                                     "current_hardware_cost": hardware_cost,
                                     "precommitted_A_hardware_premium": premium,
                                     "adaptive_A_hardware_premium": adaptive_premium,
                                     "adaptive_onboard_A_option": onboard_option,
                                     "adaptive_external_A_option": external_option,
                                     "premium_without_future_learning": one_generation_premium,
                                     "premium_with_equivalent_external_cost": equal_alternative_premium},
        "boundary_checks": ["independent nuisance removes A complementarity",
                            "redrawn nuisance removes repetition floor",
                            "irrelevant uncertainty has zero information value",
                            "equivalent external experiment removes hardware advantage",
                            "hard demand cap separates value from capital quantity"],
    }


if __name__ == "__main__":
    result = verify_and_report()
    destination = Path(__file__).with_name("diagnostic_portfolios_results.json")
    destination.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({key: result[key] for key in ["status", "counts", "max_absolute_errors"]}, indent=2))
