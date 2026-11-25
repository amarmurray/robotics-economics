"""Exact six-shift synthetic dispatch model. Run with Python 3, standard library only.

One digital job appears per shift; its observed contribution is equally likely to
be 2 or 24. One unit of shared compute suffices to serve it or to train. A
second compute slot, if available, is free sunk capacity in this comparison.
A four-robot-hour physical contract is fulfilled in every shift. Common fixed
capital costs are excluded. A sealed site allows assisted operations but no
retention for training, and this toy has no other learning source.

Calendar comparator: choose all shift instructions before observing digital
job values. An infeasible instruction becomes normal service, so there are no
further costs after qualification. The adaptive policy observes the digital
job value, packet state and qualification before acting. Both comparators
adapt to the realised *feasibility* of actions.
"""
from collections import defaultdict
from fractions import Fraction as F
from functools import lru_cache
from itertools import product
import json

SHIFTS = 6
DIGITAL_VALUES = (2, 24)
QUALIFY = F(3, 5)
EMPTY, PACKET, QUALIFIED = "empty", "packet", "qualified"
SERVE, DEMO, TRAIN = "service", "demo", "train"
ACTIONS = (SERVE, DEMO, TRAIN)
STATES = (EMPTY, PACKET, QUALIFIED)


def feasible(state, reusable):
    if reusable and state == EMPTY:
        return (SERVE, DEMO)
    if reusable and state == PACKET:
        return (SERVE, TRAIN)
    return (SERVE,)


def stage(state, digital, action, slots):
    """Contribution booked in the current shift, before any new qualification."""
    human_per_robot_hour = F(8 if state == QUALIFIED else 26, 100)
    physical = 4 * (14 - 6 - 25 * human_per_robot_hour)
    digital_earned = digital if slots >= 2 or action != TRAIN else 0
    return physical + digital_earned - 4 * (action == DEMO)


def transitions(state, action):
    if action == TRAIN:
        return ((QUALIFIED, QUALIFY), (EMPTY, 1 - QUALIFY))
    return ((PACKET if action == DEMO else state, F(1)),)


def optimal(reusable=True, slots=1):
    chosen = {}

    @lru_cache(None)
    def value(t, state):
        if t == SHIFTS:
            return F(0)
        total = F(0)
        for digital in DIGITAL_VALUES:
            alternatives = {}
            for action in feasible(state, reusable):
                follow_on = sum(p * value(t + 1, dest) for dest, p in transitions(state, action))
                alternatives[action] = stage(state, digital, action, slots) + follow_on
            best = max(alternatives, key=alternatives.get)
            chosen[t, state, digital] = best
            total += alternatives[best] / 2
        return total

    return value(0, EMPTY), chosen


def evaluate(choice, reusable, slots):
    """Forward path-mass enumeration, with an independent resource/margin ledger."""
    mass = {EMPTY: F(1)}
    stats = defaultdict(F)
    for t in range(SHIFTS):
        next_mass = defaultdict(F)
        for state, p_state in mass.items():
            for digital in DIGITAL_VALUES:
                action = choice(t, state, digital)
                assert action in feasible(state, reusable)
                weight = p_state / 2
                is_q = state == QUALIFIED
                stats["qualified_shifts"] += weight * is_q
                stats["demo_count"] += weight * (action == DEMO)
                stats["train_count"] += weight * (action == TRAIN)
                stats["intervention_hours"] += weight * 4 * (F(2, 25) if is_q else F(13, 50))
                if action == TRAIN and slots == 1:
                    stats["digital_displaced"] += weight * digital
                if action == TRAIN:
                    next_mass[EMPTY] += weight * F(2, 5)
                    next_mass[QUALIFIED] += weight * F(3, 5)
                else:
                    dest = PACKET if action == DEMO else state
                    next_mass[dest] += weight
        mass = next_mass
        assert sum(mass.values()) == 1
    stats["terminal_qualified"] = mass.get(QUALIFIED, F(0))
    stats["additional_demo_hours"] = stats["demo_count"] * F(4, 25)
    stats["dollars"] = (
        SHIFTS * 4 * (14 - 6) + SHIFTS * 13 - stats["digital_displaced"]
        - 25 * (stats["intervention_hours"] + stats["additional_demo_hours"])
    )
    return stats


def calendar_choice(calendar, reusable):
    def choose(t, state, digital):
        instruction = calendar[t]
        return instruction if instruction in feasible(state, reusable) else SERVE
    return choose


def scenario(reusable, slots):
    value, choices = optimal(reusable, slots)
    adaptive = evaluate(lambda t, state, digital: choices[t, state, digital], reusable, slots)
    assert adaptive["dollars"] == value
    never = evaluate(lambda *args: SERVE, reusable, slots)
    assert never["dollars"] == 114
    eager = (DEMO, TRAIN, DEMO, TRAIN, SERVE, SERVE)
    asap = evaluate(calendar_choice(eager, reusable), reusable, slots)
    # No useful new training in shift 6. Buying a new packet in shift 5 or
    # later can only pay for training in shift 6, with zero following work.
    # A previously banked packet can still be trained in shift 5.
    allowed = [ACTIONS] * 4 + [(SERVE, TRAIN), (SERVE,)]
    candidates = [(c, evaluate(calendar_choice(c, reusable), reusable, slots)) for c in product(*allowed)]
    calendar, best_fixed = max(candidates, key=lambda pair: pair[1]["dollars"])
    assert value >= best_fixed["dollars"] >= max(asap["dollars"], never["dollars"])
    if not reusable:
        assert value == 114
    if reusable and slots == 2:
        assert value == best_fixed["dollars"]
    def to_dict(stats):
        keys = ("dollars", "qualified_shifts", "demo_count", "train_count",
                "digital_displaced", "intervention_hours", "additional_demo_hours", "terminal_qualified")
        return {key: float(stats.get(key, F(0))) for key in keys}
    return {
        "reusable": reusable, "slots": slots, "adaptive": to_dict(adaptive),
        "best_fixed": to_dict(best_fixed), "best_fixed_calendar": list(calendar),
        "asap": to_dict(asap), "never": to_dict(never),
        "adaptive_dollars_exact": str(value),
        "observation_actions": {
            f"shift_{t+1}_{state}":[choices[t,state,d] for d in DIGITAL_VALUES]
            for t in range(SHIFTS) for state in (EMPTY,PACKET) if (t,state,2) in choices
        }
    }


if __name__ == "__main__":
    print(json.dumps([scenario(r, k) for r, k in ((True, 1), (False, 1), (True, 2))], indent=2))
