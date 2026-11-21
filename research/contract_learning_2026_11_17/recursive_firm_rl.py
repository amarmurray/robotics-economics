"""Two-stage tabular Q-learning in RoboEcon's synthetic contracting economy."""
import itertools
import json
import random
from collections import defaultdict
from fractions import Fraction

import contract_core


CONTEXTS = tuple(itertools.product(("hourly", "output"), ("output", "hours"), (True, False)))
SPEEDS = (2, 4)
CASH = Fraction(5)
TRANSFER = Fraction(2)
EPISODES = 8000
SEEDS = (0, 1, 2, 3, 4)
EXPLORATION = 0.35
STEP_SIZE = 0.3


def build_environment():
    """Construct feasible actions and rewards without giving the learner an optimum."""
    environment = {}
    for context in CONTEXTS:
        billing, learning_unit, reuse = context
        for speed in SPEEDS:
            source = contract_core.source(speed, billing)
            margin = source["m"]
            exposure = source["q" if learning_unit == "output" else "H"] if reuse else 0
            budget = CASH + margin
            qualification_cost = max(2, 11 - TRANSFER * exposure)
            menu = {"retain": 0}
            if budget >= 8:
                menu["incumbent_A"] = Fraction(52, 5) - 8
            if budget >= 3 + qualification_cost:
                # The firm captures 4/5 of 19 units of target operating margin.
                menu["qualify_B"] = Fraction(76, 5) - 3 - qualification_cost
            environment[context, speed] = margin, menu
    return environment


def choose_action(q, state, actions, rng):
    if rng.random() < EXPLORATION:
        return rng.choice(tuple(actions))
    return max(actions, key=lambda action: q[state, action])


def train(seed, environment):
    rng = random.Random(seed)
    q = defaultdict(float)
    for _ in range(EPISODES):
        context = rng.choice(CONTEXTS)
        speed = choose_action(q, context, SPEEDS, rng)
        margin, menu = environment[context, speed]
        second_state = (context, speed)
        target = float(margin) + max(q[second_state, action] for action in menu)
        q[context, speed] += STEP_SIZE * (target - q[context, speed])
        investment = choose_action(q, second_state, menu, rng)
        payoff = float(menu[investment])
        q[second_state, investment] += STEP_SIZE * (payoff - q[second_state, investment])
    return q


def audit():
    environment = build_environment()
    for (context, speed), (margin, menu) in environment.items():
        billing, unit, rights = context
        exact = contract_core.path(speed, billing, metric=unit, rights=rights, tau=TRANSFER, cash=CASH)
        assert margin + max(menu.values()) == exact["added"]
    rows = {}
    checks = 0
    for seed in SEEDS:
        q = train(seed, environment)
        for context in CONTEXTS:
            billing, unit, rights = context
            speed = max(SPEEDS, key=lambda s: q[context, s])
            margin, menu = environment[context, speed]
            investment = max(menu, key=lambda action: q[(context, speed), action])
            best_speed, paths = contract_core.choose(billing, metric=unit, rights=rights,
                                                      tau=TRANSFER, cash=CASH)
            assert speed == best_speed
            assert investment == paths[speed]["choice"]
            assert margin + menu[investment] == paths[speed]["added"]
            rows[context] = dict(billing=billing, learning_unit=unit, reuse=rights,
                                 speed=speed, investment=investment, slow=float(paths[2]["added"]),
                                 fast=float(paths[4]["added"]))
            checks += 1
    return dict(episodes=EPISODES, seeds=SEEDS, matched_policy_and_return=checks, contexts=list(rows.values()))


if __name__ == "__main__":
    print(json.dumps(audit(), indent=2))
