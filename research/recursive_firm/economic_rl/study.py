"""Two-release economic RL experiment. Python 3, standard library only."""
from dataclasses import dataclass
from functools import lru_cache
from itertools import product
from math import sqrt
from random import Random
from statistics import mean, stdev
import json

BETA = 0.9
PRICES = (7, 5)
ACTIONS = tuple(product(range(3), repeat=2))  # dispatch, qualification: wait, arm, mobile
MASKS = range(4)
EPISODES = 60000
CALIBRATION = 12000
TRAIN_SEEDS = (104, 205, 306, 407)
WORLD_SEEDS = range(8400, 8440)
POLICIES = ('joint_q', 'blind_q', 'current_margin', 'raw_rule', 'local_rules', 'world_optimum')
METRICS = ('value', 'accepted_arm', 'accepted_mobile', 'qualified_procedure', 'slots_used')


@dataclass(frozen=True)
class World:
    early: tuple = (.12, .22, .21, .45)  # neither, arm, mobile, both
    late: tuple = (.05, .15, .10, .70)
    transfer: tuple = (.1, .9)  # successful source to the other lane, with a reuse grant


def draw_world(seed, regime):
    rng = Random(seed)

    def mix(probabilities):
        draws = [rng.gammavariate(60 * p, 1) for p in probabilities]
        return tuple(x / sum(draws) for x in draws)

    early = mix(World.early)
    late = mix((.32, .31, .28, .09) if regime == 'little_joint_demand' else World.late)
    transfer = (rng.uniform(.04, .16), rng.uniform(.84, .96))
    if regime == 'transfer_reversed':
        transfer = transfer[::-1]
    return World(early, late, transfer)


def draw_mask(rng, probabilities):
    u = rng.random()
    for mask, p in enumerate(probabilities):
        u -= p
        if u <= 0:
            return mask
    return 3


@lru_cache(maxsize=None)
def accepts(mask, inherited, extra):
    result = []
    for j in (1, 2):
        ready_orders = 1 + bool(mask & j)
        service = 1 + (inherited == j) + (extra == j)
        result.append(min(2, ready_orders, service))
    return tuple(result)


@lru_cache(maxsize=None)
def marginal(mask, inherited):
    baseline = accepts(mask, inherited, 0)
    return sum(j * (accepts(mask, inherited, j)[j - 1] - baseline[j - 1]) for j in (1, 2))


@lru_cache(maxsize=None)
def settle(mask, inherited, action):
    dispatch, release = ACTIONS[action]
    lane = dispatch if dispatch == release else 0
    orders = accepts(mask, inherited, lane)
    use = int(dispatch != 0) + int(release != 0)
    value = sum(p * (y - 1) for p, y in zip(PRICES, orders)) - use
    produced = lane if lane and marginal(mask, inherited) & lane else 0
    return value, orders[0] - 1, orders[1] - 1, use, produced


def later_states(source, grant, transfer):
    if source and grant:
        prob = transfer[source - 1]
        return ((0, 1 - prob), (3 - source, prob))
    return ((0, 1.0),)


def largest(values):
    return max(range(len(values)), key=values.__getitem__)


def measured_products(cells):
    """Contrasts from randomly released vs idle service on disjoint calibration episodes."""
    table = {}
    for mask, h in product(MASKS, (0, 1, 2)):
        bits = 0
        for j in (1, 2):
            stratum = (j, bool(mask & j), h == j)
            observed = []
            for granted in (False, True):
                total, n = cells[stratum + (granted,)]
                assert n > 0
                observed.append(total / n)
            effect = observed[1] - observed[0]
            assert effect in (0, 1)  # conditional output is deterministic in this technology
            bits += j * int(effect)
        table[mask, h] = bits
    return table


def fit_q(log, measured=None):
    # Terminal passive receipts come from an earlier release and are invariant
    # to the terminal action. Restore them in the earlier Bellman target.
    terminal = {}
    initial = {}

    def state_key(stage, grant, inherited, mask):
        if stage == 0:
            return (grant, measured[mask, inherited] if measured is not None else 0)
        return measured[mask, inherited] if measured is not None else inherited

    def record(table, key, action, value):
        if key not in table:
            table[key] = [[0.0, 0] for _ in ACTIONS]
        cell = table[key][action]
        cell[0] += value
        cell[1] += 1

    def averages(table):
        assert all(n > 0 for row in table.values() for _, n in row)
        return {key: [total / n for total, n in row] for key, row in table.items()}

    for grant, b0, a0, r0, inherited, b1, a1, r1, passive in log:
        key = state_key(1, grant, inherited, b1)
        record(terminal, key, a1, r1 - passive)
    q1 = averages(terminal)
    for grant, b0, a0, r0, inherited, b1, a1, r1, passive in log:
        k0 = state_key(0, grant, 0, b0)
        k1 = state_key(1, grant, inherited, b1)
        record(initial, k0, a0, r0 + BETA * (passive + max(q1[k1])))
    q0 = averages(initial)
    return {(t, g, h, m): largest((q0 if t == 0 else q1)[state_key(t, g, h, m)])
            for t in (0, 1) for g in (0, 1) for h in ((0,) if t == 0 else (0, 1, 2)) for m in MASKS}


def collect(seed):
    world, rng = World(), Random(seed)
    panel_rng = Random(seed + 90000)
    masks = [[0] * 4 for _ in (0, 1)]
    attempts, transfers = [0, 0], [0, 0]
    log, calibration = [], {}
    for episode in range(EPISODES):
        grant = rng.randrange(2)
        b0, b1 = draw_mask(rng, world.early), draw_mask(rng, world.late)
        a0, a1 = rng.randrange(len(ACTIONS)), rng.randrange(len(ACTIONS))
        r0, x0, y0, _, source = settle(b0, 0, a0)
        inherited = 0
        if source and grant:
            if rng.random() < world.transfer[source - 1]:
                inherited = 3 - source
        if episode < CALIBRATION:
            # A standing reference panel can assign known prior qualifications.
            # Incidental operating histories alone can leave some strata empty.
            inherited = panel_rng.randrange(3)
        r1, x1, y1, _, _ = settle(b1, inherited, a1)
        if episode < CALIBRATION:
            for mask, h, action, obs in ((b0, 0, a0, (x0, y0)), (b1, inherited, a1, (x1, y1))):
                for j in (1, 2):
                    if ACTIONS[action] in ((0, 0), (j, j)):
                        key = (j, bool(mask & j), h == j, ACTIONS[action] == (j, j))
                        cell = calibration.setdefault(key, [0, 0])
                        cell[0] += obs[j - 1]
                        cell[1] += 1
            continue
        masks[0][b0] += 1
        masks[1][b1] += 1
        if source and grant:
            attempts[source - 1] += 1
            transfers[source - 1] += int(inherited != 0)
        passive = settle(b1, inherited, 0)[0]
        log.append((grant, b0, a0, r0, inherited, b1, a1, r1, passive))
    estimate = World(*(tuple(n / len(log) for n in row) for row in masks),
                     tuple(s / n for s, n in zip(transfers, attempts)))
    measured = measured_products(calibration)
    assert all(bits == marginal(mask, h) for (mask, h), bits in measured.items())
    return log, estimate, measured


def decision_rule(world, local=False, myopic=False):
    """Optimal rule given stated local or common information and the supplied law."""
    policy = {}
    for grant in (0, 1):
        future = {}
        for stage in (1, 0):
            probabilities = world.late if stage else world.early
            for inherited in ((0, 1, 2) if stage else (0,)):
                values = []
                for mask in MASKS:
                    row = []
                    for action in range(len(ACTIONS)):
                        value, _, _, _, source = settle(mask, inherited, action)
                        if not stage and not myopic:
                            value += BETA * sum(p * future[h] for h, p in later_states(source, grant, world.transfer))
                        row.append(value)
                    values.append(row)
                if local:
                    # Each of the two roles sees only one readiness bit. Both know
                    # the calendar, inherited capacity and grant, and agree a codebook.
                    scores = [(sum(probabilities[m] * values[m][actions[m]] for m in MASKS), actions)
                              for actions in LOCAL_CODEBOOKS]
                    chosen = max(scores, key=lambda pair: pair[0])[1]
                else:
                    chosen = tuple(largest(row) for row in values)
                for m in MASKS:
                    policy[stage, grant, inherited, m] = chosen[m]
                if stage:
                    future[inherited] = sum(probabilities[m] * values[m][chosen[m]] for m in MASKS)
    return policy


LOCAL_CODEBOOKS = tuple(
    tuple(3 * dispatch[int(bool(m & 1))] + release[int(bool(m & 2))] for m in MASKS)
    for dispatch, release in product(product(range(3), repeat=2), repeat=2)
)


def fit(seed):
    log, estimate, measured = collect(seed)
    return {'joint_q': fit_q(log, measured), 'blind_q': fit_q(log),
            'current_margin': decision_rule(estimate, myopic=True),
            'raw_rule': decision_rule(estimate), 'local_rules': decision_rule(estimate, local=True)}


def evaluate(policy, world, grant, crossed_display=False):
    """Enumerate physical outcomes. Only the input to the frozen policy can be wrong."""
    measures = dict.fromkeys(METRICS, 0.0)
    def act(stage, inherited, mask):
        display = (2 * (mask & 1) + (mask >> 1)) if crossed_display else mask
        return policy[stage, grant, inherited, display]

    for b0, prior in enumerate(world.early):
        r0, x0, y0, use, source = settle(b0, 0, act(0, 0, b0))
        measures['value'] += prior * r0
        measures['accepted_arm'] += prior * x0
        measures['accepted_mobile'] += prior * y0
        measures['slots_used'] += prior * use
        for h, p in later_states(source, grant, world.transfer):
            measures['qualified_procedure'] += prior * p * bool(h)
            for b1, p1 in enumerate(world.late):
                weight = prior * p * p1
                r1, x1, y1, use, _ = settle(b1, h, act(1, h, b1))
                measures['value'] += weight * BETA * r1
                measures['accepted_arm'] += weight * x1
                measures['accepted_mobile'] += weight * y1
                measures['slots_used'] += weight * use
    return measures


def swarm_probability(n, single, common, qualification):
    if n == 0:
        return 0.0
    return qualification * (common * single + (1 - common) * (1 - (1 - single) ** n))


def checks():
    for b, h in product(MASKS, (0, 1, 2)):
        assert marginal(b, h) == (b & ~h)
        for a in range(len(ACTIONS)):
            assert (settle(b, h, a)[4] > 0) == (settle(b, h, a)[1:3] != settle(b, h, 0)[1:3])
    for n, p, rho, q in product(range(1, 8), (.2, .5, .8), (0., .5, 1.), (0., .7, 1.)):
        mass = sum((p ** sum(outcome)) * ((1 - p) ** (n - sum(outcome)))
                   for outcome in product((0, 1), repeat=n) if any(outcome))
        assert abs(swarm_probability(n, p, rho, q) - q * (rho * p + (1 - rho) * mass)) < 1e-12
        gain = swarm_probability(n + 1, p, rho, q) - swarm_probability(n, p, rho, q)
        assert abs(gain - q * (1 - rho) * p * (1 - p) ** n) < 1e-12
    world = World()
    plan = decision_rule(world)
    assert plan[0, 0, 0, 3] == ACTIONS.index((1, 1))
    assert plan[0, 1, 0, 3] == ACTIONS.index((2, 2))


def main():
    checks()
    fitted = [fit(seed) for seed in TRAIN_SEEDS]
    regimes = ('training_family', 'transfer_reversed', 'little_joint_demand', 'display_reversed')
    out = {}
    for regime in regimes:
        rows = []
        for seed in WORLD_SEEDS:
            w = draw_world(seed, regime)
            oracle = decision_rule(w)
            scores = {}
            for name in POLICIES:
                by_grant = []
                for grant in (0, 1):
                    policies = [oracle] if name == 'world_optimum' else [p[name] for p in fitted]
                    worlds = [evaluate(p, w, grant, crossed_display=(regime == 'display_reversed'
                                                                    and name not in ('world_optimum', 'local_rules')))
                              for p in policies]
                    # Local rules read their own lane instrument. The reporting shock
                    # inverts the shared display only. The informed oracle knows its map.
                    by_grant.append({key: mean(z[key] for z in worlds) for key in METRICS})
                scores[name] = by_grant
                for grant in (0, 1):
                    if name == 'world_optimum':
                        assert all(x[grant]['value'] <= by_grant[grant]['value'] + 1e-10 for x in scores.values())
            rows.append(scores)
        means = {}
        for name in POLICIES:
            by_grant = [{key: round(mean(row[name][g][key] for row in rows), 5) for key in METRICS} for g in (0, 1)]
            spread = [row[name][1]['value'] - row[name][0]['value'] for row in rows]
            means[name] = {'local_rights': by_grant[0], 'cross_rights': by_grant[1],
                           'break_even_grant_fee': round(mean(spread), 5)}
        contrasts = {}
        for rival in POLICIES[1:]:
            delta = [row['joint_q'][1]['value'] - row[rival][1]['value'] for row in rows]
            contrasts[rival] = {'paired_mean': round(mean(delta), 5), 'world_se': round(stdev(delta) / sqrt(len(delta)), 5),
                                'worlds_ahead': sum(x > 1e-9 for x in delta), 'worlds_behind': sum(x < -1e-9 for x in delta)}
        out[regime] = {'policies': means, 'joint_q_minus_rival_with_cross_rights': contrasts}
    check = {str(g): {name: list(ACTIONS[fitted[0][name][0, g, 0, 3]]) for name in POLICIES[:-1]} for g in (0, 1)}
    # Table III of Li et al., RSS 2023. All four cells use center picks.
    picks = {'TopoZ-Center': (1158353, 89378), 'TopoLPR-Center': (1156697, 83535),
             'Z-Center': (1157739, 89866), 'LPR-Center': (1160005, 72789)}
    success = {name: 1 - failed / total for name, (total, failed) in picks.items()}
    restricted = 100 * (success['TopoLPR-Center'] - success['TopoZ-Center'])
    unrestricted = 100 * (success['LPR-Center'] - success['Z-Center'])
    physical = {'source': 'https://roboticsproceedings.org/rss19/p023.pdf', 'table': 'III',
                'total_attempts_and_failed_picks': picks,
                'gain_with_topological_ordering_pp': round(restricted, 4),
                'gain_without_topological_ordering_pp': round(unrestricted, 4),
                'difference_in_gains_pp': round(unrestricted - restricted, 4)}
    print(json.dumps({'total_source_episodes_per_seed': EPISODES,
                      'separate_calibration_episodes_per_seed': CALIBRATION,
                      'critic_and_incumbent_episodes_per_seed': EPISODES - CALIBRATION,
                      'reported_physical_evaluation': physical, 'training_seeds': TRAIN_SEEDS,
                      'independent_test_world_seeds': list(WORLD_SEEDS),
                      'both_lanes_ready_first_action_at_first_training_seed': check,
                      'regimes': out}, indent=2))


if __name__ == '__main__':
    main()
