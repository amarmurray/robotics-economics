"""Local objective weights under paired feedback. All quantities are synthetic."""
import json
import math
import random

# Each pair is (innovation variance, observation-noise variance).
COMMON = (3, 60)
CONTRAST = (32, 10)
CALIBRATION_SEED = 17
TEST_SEEDS = (101, 102, 103, 104, 105)
CALIBRATION_PERIODS = 20000
TEST_PERIODS = 20000
BURN_IN = 500


def optimal_gain(drift, noise):
    """Best constant gain for a random walk with independent observation noise."""
    if drift <= 0 or noise < 0:
        raise ValueError("Use positive drift variance and nonnegative noise variance.")
    return 2 * drift / (drift + math.sqrt(drift * drift + 4 * drift * noise))


def prediction_variance(drift, noise, gain):
    if not 0 < gain <= 1:
        raise ValueError("The tracking gain must lie in (0, 1].")
    return (drift + gain ** 2 * noise) / (gain * (2 - gain))


def next_gain(prior_variance, noise, drift):
    """Return the weight on the current audit and the next prediction variance."""
    gain = 0 if noise is None else prior_variance / (prior_variance + noise)
    return gain, (1 - gain) * prior_variance + drift


def tracking_loss(modes, gains):
    return sum(prediction_variance(q, r, k) for (q, r), k in zip(modes, gains)) / 2


def site_updates(common_gain, contrast_gain):
    """Diagonal and off-diagonal entries of the update in site coordinates."""
    return (common_gain + contrast_gain) / 2, (common_gain - contrast_gain) / 2


def regime_report(accuracy):
    """Two equally likely long-lived regimes swap the common and contrast dynamics."""
    if not 0.5 <= accuracy <= 1:
        raise ValueError("Use a symmetric report with accuracy between chance and certainty.")
    conditional_modes = [
        tuple(accuracy * a + (1 - accuracy) * b for a, b in zip(correct, incorrect))
        for correct, incorrect in ((COMMON, CONTRAST), (CONTRAST, COMMON))
    ]
    calibrated = [optimal_gain(q, r) for q, r in conditional_modes]
    loss = tracking_loss(conditional_modes, calibrated)
    fixed_loss = tracking_loss(conditional_modes, (0.5, 0.5))
    full_strength = [optimal_gain(*COMMON), optimal_gain(*CONTRAST)]
    return {"accuracy": accuracy, "one_gain_loss": fixed_loss,
            "full_strength_loss": tracking_loss(conditional_modes, full_strength),
            "calibrated_gains": calibrated, "calibrated_loss": loss,
            "report_value_before_cost": fixed_loss - loss}


def coordinates(first, second):
    """Orthonormal transform between two sites and common/contrast coordinates."""
    return (first + second) / math.sqrt(2), (first - second) / math.sqrt(2)


def market(periods, seed):
    """Two sites observe local, noisy audits only after their decisions."""
    rng = random.Random(seed)
    common_value = contrast_value = 0.0
    for _ in range(periods):
        common_value += rng.gauss(0, math.sqrt(COMMON[0]))
        contrast_value += rng.gauss(0, math.sqrt(CONTRAST[0]))
        common_audit = common_value + rng.gauss(0, math.sqrt(COMMON[1]))
        contrast_audit = contrast_value + rng.gauss(0, math.sqrt(CONTRAST[1]))
        yield coordinates(common_value, contrast_value), coordinates(common_audit, contrast_audit)


def estimate_variances(audits):
    """Recover the variances from successive audit differences and their first lag."""
    differences = [right - left for left, right in zip(audits, audits[1:])]
    mean = sum(differences) / len(differences)
    centered = [change - mean for change in differences]
    variance = sum(change * change for change in centered) / len(centered)
    lag_one = sum(a * b for a, b in zip(centered, centered[1:])) / (len(centered) - 1)
    return variance + 2 * lag_one, -lag_one


def fitted_gains():
    series = [[], []]
    for _, local_audits in market(CALIBRATION_PERIODS, CALIBRATION_SEED):
        for values, audit in zip(series, coordinates(*local_audits)):
            values.append(audit)
    variances = [estimate_variances(values) for values in series]
    q_total = sum(q for q, _ in variances)
    r_total = sum(r for _, r in variances)
    return optimal_gain(q_total, r_total), [optimal_gain(q, r) for q, r in variances]


def evaluate_sites(policies):
    """Use the same raw histories for every rule, keep each site's choice local."""
    totals = dict.fromkeys(policies, 0.0)
    for seed in TEST_SEEDS:
        weights = {name: (0.0, 0.0) for name in policies}
        for period, (values, audits) in enumerate(market(BURN_IN + TEST_PERIODS, seed)):
            for name, (own, cross) in policies.items():
                first, second = weights[name]
                if period >= BURN_IN:
                    totals[name] += ((values[0] - first) ** 2 + (values[1] - second) ** 2) / 2
                gap_first, gap_second = audits[0] - first, audits[1] - second
                weights[name] = (first + own * gap_first + cross * gap_second,
                                 second + cross * gap_first + own * gap_second)
    return {name: round(total / (TEST_PERIODS * len(TEST_SEEDS)), 3)
            for name, total in totals.items()}


def results():
    modes = (COMMON, CONTRAST)
    best = [optimal_gain(*mode) for mode in modes]
    pooled = optimal_gain(COMMON[0] + CONTRAST[0], COMMON[1] + CONTRAST[1])
    fitted_pool, fitted_graph = fitted_gains()
    policies = {"common_gain": site_updates(pooled, pooled),
                "paired_feedback": site_updates(*best),
                "reversed_modes": site_updates(*reversed(best)),
                "estimated_common_gain": site_updates(fitted_pool, fitted_pool),
                "estimated_paired_feedback": site_updates(*fitted_graph)}
    baseline = tracking_loss(modes, (pooled, pooled))
    paired = tracking_loss(modes, best)
    return {
        "mode_variances": {"common": COMMON, "contrast": CONTRAST},
        "optimal_gains": {"common": best[0], "contrast": best[1], "one_gain": pooled},
        "site_update": {"own": policies["paired_feedback"][0],
                        "cross": round(policies["paired_feedback"][1], 12)},
        "exact_stationary_loss": {"one_gain": baseline, "paired_feedback": paired,
                                  "reversed_modes": tracking_loss(modes, list(reversed(best)))},
        "break_even_cost_per_joint_period": baseline - paired,
        "regime_reports": [regime_report(p) for p in (0.5, 0.75, 1.0)],
        "precise_common_audit": {"prior_variance": 15, "old_noise": 60, "new_noise": 15,
                                 "first_gain": next_gain(15, 15, 3)[0]},
        "simulation": {"calibration_seed": CALIBRATION_SEED, "test_seeds": TEST_SEEDS,
                       "calibration_periods": CALIBRATION_PERIODS, "test_periods_per_seed": TEST_PERIODS,
                       "burn_in_per_seed": BURN_IN,
                       "estimated_gains": [round(g, 4) for g in fitted_graph],
                       "estimated_one_gain": round(fitted_pool, 4),
                       "mean_test_loss": evaluate_sites(policies)},
    }


if __name__ == "__main__":
    print(json.dumps(results(), indent=2))
