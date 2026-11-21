"""Finite-horizon experiment selection between two rival transfer mechanisms."""
from dataclasses import dataclass
from fractions import Fraction as F
from functools import lru_cache
from math import comb

LOW, HIGH = F(1, 20), F(1, 4)
SITES, PROBE_COST = 10, F(1, 5)


def posterior(successes, failures):
    low = LOW ** successes * (1 - LOW) ** failures
    high = HIGH ** successes * (1 - HIGH) ** failures
    return (low * LOW + high * HIGH) / (low + high)


def site_value(probability):
    return 24 * probability - 3


def stop_value(successes, failures):
    return max(F(0), SITES * site_value(posterior(successes, failures)))


@dataclass(frozen=True)
class Decision:
    value: F
    action: str


@lru_cache(None)
def solve(successes, failures, remaining):
    stop = stop_value(successes, failures)
    decision = Decision(stop, "deploy" if stop else "decline")
    if remaining:
        p = posterior(successes, failures)
        yes = solve(successes + 1, failures, remaining - 1).value
        no = solve(successes, failures + 1, remaining - 1).value
        buy = p * yes + (1 - p) * no - PROBE_COST
        if buy > stop:
            decision = Decision(buy, "probe")
    return decision


def batch_value(count):
    value = F(0)
    for successes in range(count + 1):
        failures = count - successes
        weights = [p ** successes * (1 - p) ** failures for p in (LOW, HIGH)]
        chance = F(comb(count, successes), 2) * sum(weights)
        value += chance * stop_value(successes, failures)
    return value


def evidence_results():
    baseline = stop_value(0, 0)
    optimal = solve(0, 0, 3)
    fixed_net = [batch_value(n) - n * PROBE_COST for n in range(4)]
    return {"hypotheses": [float(LOW), float(HIGH)], "future_sites": SITES, "cost_per_probe": float(PROBE_COST),
            "ordinary_incumbent_ledger_value_of_information": 0,
            "batch_gross_gains_over_no_probe": [float(batch_value(n) - baseline) for n in range(4)],
            "no_probe": float(baseline), "best_fixed_batch": float(max(fixed_net)),
            "adaptive_design": float(optimal.value),
            "net_gain_vs_no_probe": float(optimal.value - baseline),
            "value_of_early_stopping_vs_best_batch": float(optimal.value - max(fixed_net)),
            "decisions": {f"{s}_success_{f}_failure": solve(s, f, 3-s-f).action
                          for s in range(4) for f in range(4-s)}}
