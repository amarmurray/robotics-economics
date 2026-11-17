"""Finite-state retained qualification with partially productive states and joint events.

Research model. Units and qualification rates are synthetic; no robotics calibration.
One unit of paid effort per effort-clock unit. Each chosen program j triggers a
Poisson qualification jump at rate_j and adds its typed qualifications. The
agent can stop and retain all acquired qualifications and operating value.
"""
from dataclasses import dataclass
from math import exp
from scipy.integrate import solve_ivp


@dataclass(frozen=True)
class Program:
    label: str
    adds: int
    rate: float


def validate(values, programs, cost=1.0):
    nstates = len(values)
    if nstates < 2 or nstates & (nstates - 1):
        raise ValueError("Value table length must be a power of two >=2")
    if cost < 0 or any(v < 0 for v in values):
        raise ValueError("Require nonnegative operating values and cost")
    for mask in range(nstates):
        for dest in range(nstates):
            if (mask | dest) == dest and values[mask] > values[dest] + 1e-12:
                raise ValueError("Operating value must be monotone in qualifications")
    if not programs or any(p.rate <= 0 or p.adds <= 0 or p.adds >= nstates for p in programs):
        raise ValueError("Programs need positive rates and valid nonempty qualified masks")


def hamiltonian(values, programs, cost=1.0):
    """Derivative in remaining effort budget for the value of each state."""
    n = len(values)
    def rhs(b, v):
        return [max([0.0] + [p.rate * (v[s | p.adds] - v[s]) - cost
                           for p in programs if (s | p.adds) != s])
                for s in range(n)]
    return rhs


def solve(values, programs, budget, cost=1.0):
    validate(values, programs, cost)
    if budget < 0:
        raise ValueError("Budget must be nonnegative")
    if budget == 0:
        y = tuple(map(float, values))
    else:
        r = solve_ivp(hamiltonian(values, programs, cost), (0, float(budget)),
                      list(map(float, values)), rtol=1e-10, atol=1e-12,
                      max_step=min(0.025, budget / 12))
        if not r.success:
            raise ArithmeticError(r.message)
        y = tuple(float(x) for x in r.y[:, -1])
    action = []
    for s in range(len(values)):
        candidates = [(p.rate * (y[s | p.adds] - y[s]) - cost, p.label)
                      for p in programs if (s | p.adds) != s]
        best = max(candidates, default=(-float('inf'), 'stop'))
        action.append(best[1] if best[0] > 1e-9 else 'stop')
    return {'budget': budget, 'values': y, 'actions': tuple(action),
            'initial_net': y[0] - values[0]}


def discrete_bellman(values, programs, budget, steps=10000, cost=1.0):
    """Independent finite-step dynamic program; first-order Markov approximation.

    Each small effort slice causes at most one successful qualification. This is
    deliberately independent from the continuous-state differential solver.
    Convergence must be checked as step-size falls; not an exact probability law.
    """
    validate(values, programs, cost)
    if budget < 0 or steps < 1:
        raise ValueError("Invalid budget or steps")
    h = budget / steps
    if any(p.rate * h > 1 for p in programs):
        raise ValueError("Step too coarse for valid probabilities")
    v = list(map(float, values))
    for _ in range(steps):
        old = v.copy()
        for s in range(len(values)):
            v[s] = max([float(values[s])] + [
                (1 - p.rate * h) * old[s] + p.rate * h * old[s | p.adds] - cost * h
                for p in programs if (s | p.adds) != s])
    return v[0] - values[0]


def full_event_only(reward, rate, budget, cost=1.0):
    """Exact single bundle event with opportunity to stop."""
    return max(0.0, reward - cost / rate) * (1 - exp(-rate * budget))


def example():
    # 0: qualified for neither new service; A: accepted unloading;
    # B: order-routing integration only; AB: complete second service.
    # No claim that actual warehouses have these rates, costs, or values.
    v = (0.0, 7.0, 0.0, 10.0)
    p = (Program('unloading_A', 1, 2.0),
         Program('routing_B', 2, 2.0),
         Program('joint_redesign_AB', 3, 1.2))
    return v, p


def summary():
    v, p = example()
    out = {str(b): solve(v, p, b) for b in (0.0001, 0.05, 0.25, 1, 2, 4, 8, 16)}
    return {'values':v, 'programs':[p.__dict__ for p in p], 'cost_per_effort':1.0,
            'budget_results':out,
            'initial_action_slopes':{x.label:x.rate*v[x.adds]-1 for x in p},
            'unlimited_candidate_target_A_then_B':10-2/2,
            'unlimited_candidate_joint':10-1/1.2}


if __name__ == '__main__':
    import json
    print(json.dumps(summary(), indent=2, sort_keys=True))
