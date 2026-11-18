"""Production, teleoperation and information timing in the common data-value model.

Finite-horizon exact rational benchmark; Gaussian-information robustness uses
stdlib erf. All payoffs/parameters are synthetic, not robotics calibration.
The terminal reward is incremental optimized production contribution relative
to a retained human/specialist baseline, not an additional data asset premium.
Python 3.10+; no ML training or external dependencies.
"""
from __future__ import annotations

from dataclasses import dataclass, replace
from fractions import Fraction as F
from functools import lru_cache
from itertools import product
from math import erf, sqrt
from pathlib import Path
import argparse
import json


@dataclass(frozen=True)
class State:
    source: int = 0
    ground: int = 0
    prior: F = F(1, 4)
    direct: bool = False


@dataclass(frozen=True)
class Model:
    horizon: int = 2
    discount: F = F(1)
    routine_margin: F = F(3)
    source_margin: F = F(1)
    ground_margin: F = F(-1)
    lab_margin: F = F(-2)
    direct_margin: F = F(-4)
    transfer_value: F = F(20)
    direct_value: F = F(6)
    accuracy: F = F(19, 20)
    lab_accuracy: F = F(1)
    source_deadline: int = 2
    source_limit: int = 1
    ground_limit: int = 1
    early_signal: bool = True
    allow_direct: bool = False
    allow_lab: bool = False
    technology: str = "bundle"
    gaussian_reward: float = 30.0
    gaussian_source_loading: tuple[float, float] = (0.0, 4.0)
    gaussian_a: float = 1.0
    gaussian_b: float = 1.0
    gaussian_ground_loading: float = 1.0
    gaussian_residual: float = 0.1
    gaussian_tolerance: float = 1.0

    def __post_init__(self):
        if (self.horizon < 1 or not F(0) < self.discount <= 1
                or not F(1, 2) <= self.accuracy <= 1
                or not F(1, 2) <= self.lab_accuracy <= 1
                or min(self.transfer_value, self.direct_value) < 0
                or min(self.source_limit, self.ground_limit) < 0
                or self.technology not in ("bundle", "gaussian")):
            raise ValueError("Invalid horizon, probabilities, limits or technology")
        if (min(self.gaussian_a, self.gaussian_b, self.gaussian_tolerance) <= 0
                or min(*self.gaussian_source_loading, self.gaussian_ground_loading,
                       self.gaussian_residual, self.gaussian_reward) < 0):
            raise ValueError("Invalid Gaussian information parameters")


def signal_branches(prior: F, accuracy: F):
    """(signal, unconditional mass, posterior); omit impossible signals."""
    if not 0 <= prior <= 1 or not F(1, 2) <= accuracy <= 1:
        raise ValueError("Invalid binary prior or diagnostic accuracy")
    result = []
    for positive in (True, False):
        likelihood_good = accuracy if positive else 1 - accuracy
        likelihood_bad = 1 - accuracy if positive else accuracy
        mass = prior * likelihood_good + (1-prior) * likelihood_bad
        if mass:
            result.append((positive, mass, prior * likelihood_good / mass))
    return tuple(result)


def joint_expected_value(law, values):
    """General qualification-set law, same mask/value convention as data_value.py.

    Deliberately does not multiply marginal qualification probabilities.
    """
    if (len(law) != len(values) or not law
            or any(p < 0 for p in law) or sum(law) != 1):
        raise ValueError("A normalized joint law matching the value table is required")
    return sum(p*v for p, v in zip(law, values))


def terminal_by_regime(model: Model, state: State, good: bool):
    if model.technology == "bundle":
        transfer = model.transfer_value if (good and state.source and state.ground) else F(0)
    else:
        A = model.gaussian_source_loading[int(good)]
        def quality(x, g):
            variance = (A/(model.gaussian_a+x)
                        + model.gaussian_ground_loading/(model.gaussian_b+g)
                        + model.gaussian_residual)
            if variance == 0:
                return 1.0
            return erf(model.gaussian_tolerance / sqrt(2*variance))
        transfer = model.gaussian_reward * (quality(state.source, state.ground)-quality(0, 0))
    outside = model.direct_value if state.direct else F(0)
    return max(F(0), transfer, outside)


def terminal(model: Model, state: State):
    return (state.prior*terminal_by_regime(model, state, True)
            + (1-state.prior)*terminal_by_regime(model, state, False))


def available(model: Model, state: State, period: int):
    acts = ["routine"]
    if state.source < model.source_limit and period <= model.source_deadline:
        acts.append("source")
    if state.ground < model.ground_limit:
        acts.append("ground")
        if model.allow_lab:
            acts.append("lab")
    if model.allow_direct and not state.direct:
        acts.append("direct")
    return tuple(acts)


def margin(model: Model, action: str):
    return getattr(model, {"routine": "routine_margin", "source": "source_margin",
                          "ground": "ground_margin", "lab": "lab_margin",
                          "direct": "direct_margin"}[action])


def physical_update(state: State, action: str):
    return replace(state, source=state.source+(action == "source"),
                   ground=state.ground+(action in ("ground", "lab")),
                   direct=state.direct or action == "direct")


def transitions(model: Model, state: State, action: str):
    after = physical_update(state, action)
    if action in ("ground", "lab") and model.early_signal:
        accuracy = model.accuracy if action == "ground" else model.lab_accuracy
        return tuple((label, mass, replace(after, prior=posterior))
                     for label, mass, posterior in signal_branches(state.prior, accuracy))
    return ((None, F(1), after),)


class Solver:
    """Belief-state DP. Prices and feasible observation laws are fixed primitives."""
    def __init__(self, model: Model):
        self.model = model

    @lru_cache(None)
    def solve(self, remaining: int, state: State):
        if remaining == 0:
            return terminal(self.model, state), "terminal"
        period = self.model.horizon - remaining + 1
        candidates = []
        for action in available(self.model, state, period):
            continuation = sum(mass*self.solve(remaining-1, nxt)[0]
                               for _, mass, nxt in transitions(self.model, state, action))
            candidates.append((margin(self.model, action)+self.model.discount*continuation, action))
        # Stable tie convention: routine, source, ground, lab, direct.
        return max(candidates, key=lambda pair: pair[0])

    def action_values(self, state: State, remaining=None):
        remaining = self.model.horizon if remaining is None else remaining
        period = self.model.horizon - remaining + 1
        return {action: margin(self.model, action)+self.model.discount*sum(
            mass*self.solve(remaining-1, nxt)[0]
            for _, mass, nxt in transitions(self.model, state, action))
            for action in available(self.model, state, period)}


def brute_force_two_periods(model: Model, initial: State):
    """Independent small-instance baseline: enumerate complete contingent plans.

    Integrates over true regimes and signal likelihoods, without posterior
    updates or Bellman recursion. Also returns the best precommitted plan.
    """
    if model.horizon != 2:
        raise ValueError("Independent enumeration is a two-period baseline")
    plans = []
    for first in available(model, initial, 1):
        state1 = physical_update(initial, first)
        seconds = available(model, state1, 2)
        observes = first in ("ground", "lab") and model.early_signal
        labels = (True, False) if observes else (None,)
        for choices in product(seconds, repeat=len(labels)):
            value = F(0)
            for good, prior in ((True, initial.prior), (False, 1-initial.prior)):
                for label, second in zip(labels, choices):
                    if observes:
                        acc = model.accuracy if first == "ground" else model.lab_accuracy
                        likelihood = acc if label == good else 1-acc
                    else:
                        likelihood = F(1)
                    state2 = physical_update(state1, second)
                    payoff = (margin(model, first)+model.discount*margin(model, second)
                              +model.discount**2*terminal_by_regime(model, state2, good))
                    value += prior*likelihood*payoff
            plans.append({"value": value, "first": first,
                          "second": dict(zip(map(str, labels), choices)),
                          "precommitted": len(set(choices)) == 1})
    return {"optimal": max(plans, key=lambda p: p["value"]),
            "precommitted": max((p for p in plans if p["precommitted"]),
                                key=lambda p: p["value"]),
            "plans_enumerated": len(plans)}


def general_two_batch_formula(prior, accuracy, k_source, k_ground, payoff_by_regime):
    """payoff_by_regime[h] = (F00,F10,F01,F11); arbitrary terminal technology.

    Two date-invariant slots, at most one batch of each source, no source signal,
    no additional investment actions. A ground signal is observed before slot 2.
    """
    def expected(index, p):
        return (1-p)*payoff_by_regime[0][index]+p*payoff_by_regime[1][index]
    source_only = -k_source+expected(1, prior)-expected(0, prior)
    ground_base = -k_ground+expected(2, prior)-expected(0, prior)
    option = sum(mass*max(0, expected(3, post)-expected(2, post)-k_source)
                 for _, mass, post in signal_branches(prior, accuracy))
    ground_first = ground_base+option
    committed_pair = -k_source-k_ground+expected(3, prior)-expected(0, prior)
    return {"source_only": source_only, "ground_first": ground_first,
            "committed_pair": committed_pair,
            "best_increment": max(0, source_only, ground_first)}


def customer_increment(quantity, service_price, robot_cost, alternative_cost):
    """Same finite accepted-service quantity, retain matched outside recipe.

    One provider, same output payment in either mode; alternative cost includes
    competent human/specialist delivery. Not a welfare or general equilibrium claim.
    """
    if min(quantity, robot_cost, alternative_cost) < 0:
        raise ValueError("Nonnegative quantity and real costs required")
    return quantity*(max(0, service_price-min(robot_cost, alternative_cost))
                     -max(0, service_price-alternative_cost))


def record_case(model: Model, initial=State()):
    solver = Solver(model)
    value, first = solver.solve(model.horizon, initial)
    after = [{"signal": label, "probability": mass, "posterior": nxt.prior,
              "next_action": solver.solve(model.horizon-1, nxt)[1]}
             for label, mass, nxt in transitions(model, initial, first)]
    result = {"value": value, "first_action": first,
              "action_values": solver.action_values(initial), "after_first": after}
    if model.horizon == 2:
        result["independent_enumeration"] = brute_force_two_periods(model, initial)
    return result


def results():
    base = Model()
    # Nonlinear alternative reuses G1/G2 information structure from the preceding
    # chapter. Reward is a normalized scalar evaluation proxy, not field dollars.
    gaussian = replace(base, technology="gaussian", source_margin=F(2),
                       ground_margin=F(0), gaussian_reward=30.0)
    return {
        "status": "Conditional theory; synthetic normalized values; no robot training or calibration",
        "baseline_parameters": {k: getattr(base, k) for k in base.__dataclass_fields__},
        "productive_diagnostic": record_case(base),
        "same_data_delayed_signal": record_case(replace(base, early_signal=False)),
        "routine_supplies_source_free": record_case(replace(base, source_margin=base.routine_margin)),
        "free_source_delayed_signal": record_case(replace(base, source_margin=base.routine_margin, early_signal=False)),
        "uninformative_diagnostic": record_case(replace(base, accuracy=F(1, 2))),
        "perfect_diagnostic": record_case(replace(base, accuracy=F(1))),
        "competent_direct_available": record_case(replace(base, allow_direct=True)),
        "stronger_direct_wins": record_case(replace(base, allow_direct=True, direct_value=F(9))),
        "pure_lab_alternative": record_case(replace(base, allow_lab=True)),
        "source_demand_expires": record_case(replace(base, source_deadline=1), State(prior=F(1, 2))),
        "no_future_incremental_value": record_case(replace(base, transfer_value=F(0))),
        "gaussian_information": record_case(gaussian),
        "gaussian_delayed_signal": record_case(replace(gaussian, early_signal=False)),
        "gaussian_repeated_data_allowed": record_case(replace(gaussian, source_limit=2, ground_limit=2)),
        "customer_price_mapping": {str(w): customer_increment(F(5), F(w), F(2), F(6))
                                   for w in (1, 3, 6, 8, 12)},
        "shared_qualification": {"joint_law": [F(3, 4), F(0), F(0), F(1, 4)],
                                 "values": [F(0), F(0), F(0), F(20)],
                                 "correct_expected_gain": F(5),
                                 "incorrect_independent_gain": F(5, 4)},
        "wage_timing_counterexample": {
            "policies": {"serve_manually_later": {"other_cost": 0, "hours_now": 0, "hours_later": 4},
                         "teach_now_then_automate": {"other_cost": 3, "hours_now": 1, "hours_later": 0}},
            "wage_0_5": {"best": "serve_manually_later", "cost": F(2), "total_hours": 4},
            "wage_2": {"best": "teach_now_then_automate", "cost": F(5), "total_hours": 1}}}


def encode(value):
    if isinstance(value, F):
        return {"exact": str(value), "decimal": float(value)}
    raise TypeError(type(value).__name__)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=Path(__file__).with_name("teleoperation_results.json"))
    args = parser.parse_args()
    args.output.write_text(json.dumps(results(), default=encode, indent=2, sort_keys=True)+"\n")
    print(args.output)
