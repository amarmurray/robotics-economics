"""Two-shift economic control problem for software agents and a mixed robot fleet."""
from dataclasses import dataclass, replace
from functools import partial
from typing import NamedTuple


@dataclass(frozen=True)
class Economy:
    desk_orders: int = 3
    plant_orders: int = 2
    depot_orders: int = 4
    desk_wage: float = 3
    floor_wage: float = 10
    hard_probability: float = 0.55
    arm_transfer: float = 0.8
    mobile_transfer: float = 0.2
    sim_pass: float = 0.5
    arm_rights: str = "portable"
    mobile_rights: str = "portable"
    compute: int = 2
    compute_cost: float = 1
    retrofit_cost: float = 3
    fixture_cost: float = 11
    hardware: tuple = ("installed", "retrofit", "fixture")
    amendment: float = 1
    interim_fraction: float = 0.25
    urgent_receipt: float = 5
    arm_receipt: float = 2
    mobile_receipt: float = 1


class State(NamedTuple):
    # No trajectory enters a learner unless its source's rights admit it.
    signal: int = -1
    saw_arm: bool = False
    saw_mobile: bool = False
    desk_ok: bool = False
    sim_spent: bool = False
    arm_spent: bool = False
    mobile_spent: bool = False
    arm_ok: bool = False
    mobile_ok: bool = False
    retrofit_candidate: bool = False


class Decision(NamedTuple):
    value: float
    action: str


class Service(NamedTuple):
    contribution: float
    digital: float
    plant: float
    depot: float
    desk_hours: float
    floor_hours: float


def service(e, s, hardware, hard, interim=False):
    """Choose paid complete orders. Unresolved stages each need a paid fallback hour."""
    mobile_capable = (not hard or s.mobile_ok or hardware == "fixture"
                      or (hardware == "retrofit" and s.retrofit_candidate))
    manual_desk = int(not s.desk_ok)
    lines = [(e.desk_orders, 4, 0), (e.plant_orders, 6, int(not s.arm_ok)),
             (0 if interim else e.depot_orders, 8, int(not mobile_capable))]
    net = desk_hours = floor_hours = 0.0
    accepted = []
    for volume, margin, manual_floor in lines:
        price_less_labor = margin - e.desk_wage * manual_desk - e.floor_wage * manual_floor
        count = volume if price_less_labor > 0 else 0
        count *= e.interim_fraction if interim else 1
        accepted.append(count)
        net += count * price_less_labor
        desk_hours += count * manual_desk
        floor_hours += count * manual_floor
    if not interim:
        net -= {"installed": 0, "retrofit": e.retrofit_cost, "fixture": e.fixture_cost}[hardware]
    return Service(net, *accepted, desk_hours, floor_hours)


def operator_actions(e, s, hours, rule):
    if not hours:
        return ("wait",)
    choices = ["urgent"]
    if not s.saw_arm and not s.arm_ok:
        choices.append("arm")
    if not s.saw_mobile and not s.mobile_ok:
        choices.append("mobile")
    if rule == "cash":
        return (max(choices, key=lambda a: receipt(e, a)),)
    if rule == "arm_first":
        return (next(a for a in ("arm", "mobile", "urgent") if a in choices),)
    return tuple(choices + ["wait"])


def receipt(e, action):
    return {"wait": 0, "urgent": e.urgent_receipt, "arm": e.arm_receipt,
            "mobile": e.mobile_receipt}[action]


def sample(e, s, action, hard):
    if action not in ("arm", "mobile"):
        return s
    rights = e.arm_rights if action == "arm" else e.mobile_rights
    observed = s.signal if rights == "sealed" else int(hard)
    return s._replace(signal=observed, **{"saw_" + action: True})


def training_actions(e, s, compute):
    if not compute:
        return ("hold",)
    actions = []
    if not s.desk_ok:
        actions.append("ledger")
    if s.saw_arm and not s.arm_spent and e.arm_rights in ("local", "portable"):
        actions.append("arm_demo")
    if s.saw_mobile and not s.mobile_spent and e.mobile_rights in ("local", "portable"):
        actions.append("mobile_demo")
    if not s.sim_spent and not s.arm_ok:
        actions.append("simulation")
    return tuple(actions + ["hold"])


def training(e, s, action):
    """Return probability of a positive validation, and the corresponding two states."""
    if action == "hold":
        return 1, s, s
    if action == "ledger":
        updated = s._replace(desk_ok=True)
        return 1, updated, updated
    if action == "simulation":
        updated = s._replace(sim_spent=True)
        return e.sim_pass, updated._replace(arm_ok=True), updated
    if action == "arm_demo":
        updated = s._replace(arm_spent=True, arm_ok=True)
        p = e.arm_transfer if e.arm_rights == "portable" else 0
        return p, updated._replace(retrofit_candidate=True), updated
    if action == "mobile_demo":
        updated = s._replace(mobile_spent=True, mobile_ok=True)
        p = e.mobile_transfer if e.mobile_rights == "portable" else 0
        return p, updated._replace(arm_ok=True), updated
    raise ValueError(action)


def expect(p, yes, no):
    if p == 0:
        return no()
    if p == 1:
        return yes()
    return p * yes() + (1 - p) * no()


def best(actions, value):
    choices = (Decision(value(action), action) for action in actions)
    return max(choices, key=lambda decision: round(decision.value, 11))


class Program:
    """Belief-state backward induction. Asset changes may miss the dispatch deadline."""
    def __init__(self, economy, fallback, operator_rule):
        self.e = economy
        self.fallback = fallback
        self.rule = operator_rule
        self.dispatch_cache = {}
        self.training_cache = {}
        self.hardware_cache = {}

    def hardware_decision(self, s):
        if s not in self.hardware_cache:
            p = self.e.hard_probability if s.signal < 0 else s.signal
            def value(hardware):
                return expect(p, lambda: service(self.e, s, hardware, True).contribution,
                              lambda: service(self.e, s, hardware, False).contribution)
            winner = best(self.e.hardware, value)
            return_value = self.e.amendment * winner.value + (1-self.e.amendment) * value(self.fallback)
            self.hardware_cache[s] = Decision(return_value, winner.action)
        return self.hardware_cache[s]

    def dispatch(self, t, s, hours, compute):
        if t == 2:
            return self.hardware_decision(s)
        key = (t, s, hours, compute)
        if key not in self.dispatch_cache:
            def value(action):
                p = self.e.hard_probability if s.signal < 0 else s.signal
                next_hours = hours - int(action != "wait")
                def after(hard):
                    state = sample(self.e, s, action, hard)
                    return self.posttrain(t, state, next_hours, compute).value
                return receipt(self.e, action) + expect(p, partial(after, True), partial(after, False))
            self.dispatch_cache[key] = best(operator_actions(self.e, s, hours, self.rule), value)
        return self.dispatch_cache[key]

    def posttrain(self, t, s, hours, compute):
        key = (t, s, hours, compute)
        if key not in self.training_cache:
            def value(action):
                p, yes, no = training(self.e, s, action)
                spend = int(action != "hold")
                def after(state):
                    current = service(self.e, state, "installed", False, interim=True).contribution if t == 0 else 0
                    return current + self.dispatch(t + 1, state, hours, compute-spend).value
                return expect(p, partial(after, yes), partial(after, no)) - spend * self.e.compute_cost
            self.training_cache[key] = best(training_actions(self.e, s, compute), value)
        return self.training_cache[key]


def solve(e, hours, rule="economic"):
    if hours not in (0, 1, 2) or e.compute < 0 or not e.hardware:
        raise ValueError("Use zero to two operator hours, a nonnegative compute budget and a hardware menu.")
    licenses = {"sealed", "settlement", "local", "portable"}
    if e.arm_rights not in licenses or e.mobile_rights not in licenses:
        raise ValueError("Unknown deployment rights.")
    defaults = e.hardware[:1] if e.amendment == 1 else e.hardware
    candidates = [Program(e, default, rule) for default in defaults]
    return max(candidates, key=lambda p: round(p.dispatch(0, State(), hours, e.compute).value, 11))


def value(e, hours, rule="economic"):
    p = solve(e, hours, rule)
    return p.dispatch(0, State(), hours, e.compute).value


def hour_price(e):
    return value(e, 1) - value(e, 0)


def with_rights(e, rights):
    return replace(e, arm_rights=rights, mobile_rights=rights)


class Tape(NamedTuple):
    hard: bool
    sim: bool
    arm_transfer: bool
    mobile_transfer: bool
    amend: bool


def run(policy, reality, hours, tape):
    """Separate forward evaluator. Only the evaluator can see hidden world outcomes."""
    s = State()
    compute = reality.compute
    net = accepted_digital = accepted_plant = 0.0
    desk_hours = floor_hours = 0.0
    samples, updates, evidence = [], [], []
    for t in range(2):
        op = policy.dispatch(t, s, hours, compute).action
        assert op in operator_actions(reality, s, hours, "economic")
        samples.append(op)
        net += receipt(reality, op)
        hours -= int(op != "wait")
        s = sample(reality, s, op, tape.hard)
        update = policy.posttrain(t, s, hours, compute).action
        assert update in training_actions(reality, s, compute)
        updates.append(update)
        _, yes, no = training(reality, s, update)
        passed = True
        if update == "simulation":
            passed = tape.sim
        elif update == "arm_demo":
            passed = reality.arm_rights == "portable" and tape.arm_transfer
            if reality.arm_rights == "portable":
                evidence.append(("arm", passed))
        elif update == "mobile_demo":
            passed = reality.mobile_rights == "portable" and tape.mobile_transfer
            if reality.mobile_rights == "portable":
                evidence.append(("mobile", passed))
        s = yes if passed else no
        compute -= int(update != "hold")
        net -= int(update != "hold") * reality.compute_cost
        if t == 0:
            interim = service(reality, s, "installed", False, interim=True)
            net += interim.contribution
            accepted_digital += interim.digital
            accepted_plant += interim.plant
            desk_hours += interim.desk_hours
            floor_hours += interim.floor_hours
    desired = policy.hardware_decision(s).action
    chosen = desired if tape.amend else policy.fallback
    final = service(reality, s, chosen, tape.hard)
    return {"net": net + final.contribution, "samples": tuple(samples), "updates": tuple(updates),
            "hardware": chosen, "evidence": tuple(evidence), "digital": accepted_digital + final.digital,
            "plant": accepted_plant + final.plant, "depot": final.depot,
            "desk_hours": desk_hours + final.desk_hours, "floor_hours": floor_hours + final.floor_hours}
