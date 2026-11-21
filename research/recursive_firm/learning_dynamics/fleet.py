"""Online digital and embodied skill learning from the same operating record."""
from dataclasses import dataclass, replace

import numpy as np


LANES = ("desk", "arm", "mobile")
MARGINS = np.array([4., 7., 10.])
WARMUP = 12
DAYS = 72
PER_LANE = 6
FAMILIES = 32
REVIEW_LIMIT = 3
REVIEW_COST = 1.50
TRAIN_COST = .25
LABEL_NOISE = .05


@dataclass(frozen=True)
class Design:
    patch: float = 0.
    collection: str = "incidents"
    sharing: str = "pooled"
    portable: bool = True
    compute: int = 3
    native_every: int = 4
    shift: str = "steady"
    review_cost: float = REVIEW_COST
    lookahead: int = 12


class World:
    """Only the evaluator owns latent outcomes. Reuse the same realization for all paired policies."""
    def __init__(self, seed):
        rng = np.random.default_rng(seed)
        self.route = rng.integers(0, 2, FAMILIES)
        self.intent = rng.integers(0, 2, FAMILIES)
        self.orientation = rng.integers(0, 2, (3, FAMILIES))
        self.orientation[0] = 0
        self.lane = np.repeat(np.arange(3), PER_LANE)
        order = rng.permutation(FAMILIES)
        frequency = np.arange(1, FAMILIES+1)**-.80
        frequency /= frequency.sum()
        self.mix = np.stack([frequency[np.roll(order, shift)] for shift in (0, 4, 12)])
        # A held-out demand mix introduces cases that were uncommon in the reference lanes.
        self.new_mix = np.roll(self.mix, FAMILIES//2, axis=1)
        self.cases = np.empty((2, DAYS, 3*PER_LANE), dtype=int)
        for m, mix in enumerate((self.mix, self.new_mix)):
            for lane in range(3):
                self.cases[m, :, self.lane==lane] = rng.choice(
                    FAMILIES, size=(PER_LANE, DAYS), p=mix[lane])
        shape = (DAYS, 3*PER_LANE)
        self.gate_coin = rng.random(shape)
        self.patch_coin = rng.random(shape)
        self.action_coin = rng.random(shape)
        self.priority = rng.random(shape)
        self.route_noise = rng.random(shape) < LABEL_NOISE
        self.intent_noise = rng.random(shape) < LABEL_NOISE
        self.native = np.array([rng.choice(FAMILIES, DAYS, p=row) for row in self.mix]).T
        self.native_noise = rng.random((DAYS, 3)) < LABEL_NOISE
        self.base_truth = self.intent[None, :] ^ self.orientation
        self.changed_truth = self.base_truth.copy()
        self.changed_truth[2] ^= 1


def correct_probability(prob, truth):
    return np.where(truth, prob, 1-prob)


class Learners:
    def __init__(self):
        self.route = np.ones((2, FAMILIES))
        self.pool = np.zeros((2, FAMILIES))
        self.native = np.ones((2, 3, FAMILIES))
        # Prequential Brier-loss advantage of pooling on each site's own native labels.
        self.transfer_score = np.zeros(3)
        self.validation_count = 0

    def probabilities(self, world, design):
        route = self.route[1]/self.route.sum(axis=0)
        local = self.native[1]/self.native.sum(axis=0)
        native_pool = np.where(world.orientation, self.pool[0], self.pool[1])
        pooled = (self.native[1]+native_pool)/(self.native.sum(axis=0)+self.pool.sum(axis=0))
        if not design.portable or design.sharing == "local":
            use = np.zeros(3, dtype=bool)
        elif design.sharing == "validated" and self.validation_count >= 4:
            use = self.transfer_score > 0
        else:
            use = np.ones(3, dtype=bool)
        return route, local, pooled, np.where(use[:, None], pooled, local), use

    def admit(self, families, route_label, intent_label, portable):
        np.add.at(self.route, (route_label, families), 1)
        if portable:
            np.add.at(self.pool, (intent_label, families), 1)

    def native_update(self, families, labels, local, pooled):
        lanes = np.arange(3)
        advantage = (local[lanes, families]-labels)**2 - (pooled[lanes, families]-labels)**2
        self.transfer_score = .85*self.transfer_score + .15*advantage
        self.validation_count += 1
        self.native[labels, lanes, families] += 1


def select_reviews(collection, failed, priority, cases, coverage, quota):
    if collection == "incidents":
        eligible = np.flatnonzero(failed)
        return eligible[np.argsort(priority[eligible])[:quota]]
    if collection == "uniform":
        return np.argsort(priority)[:quota]
    if collection == "fill":
        return np.lexsort((priority, ~failed))[:quota]
    if collection in ("reserve_1", "reserve_2"):
        minimum = int(collection[-1])
        count = min(quota, max(minimum, int(failed.sum())))
        return np.lexsort((priority, ~failed))[:count]
    if collection == "coverage":
        # Spend each review on the least represented available family. A current failure
        # takes precedence within a coverage tie. Avoid redundant picks in one shift.
        counts = coverage.copy()
        available = np.ones(len(cases), dtype=bool)
        selected = []
        for _ in range(quota):
            order = np.lexsort((priority, ~failed, counts[cases]))
            chosen = order[available[order]][0]
            available[chosen] = False
            counts[cases[chosen]] += 1
            selected.append(chosen)
        return np.array(selected, dtype=int)
    raise ValueError(collection)


def economic_reviews(learners, world, design, cases, failed, permitted_pool, market, day):
    """A finite-horizon acquisition heuristic operating only on the firm's point-in-time observations."""
    route, _, _, skills, _ = learners.probabilities(world, design)
    patch = design.patch
    # Subjective expected accuracy of a probability-matching binary policy.
    route_ok = 1-2*route*(1-route)*(1-patch)
    skill_ok = 1-2*skills*(1-skills)
    route_counts = learners.route.sum(axis=0).copy()
    skill_counts = learners.native.sum(axis=0) + permitted_pool[:,None]*learners.pool.sum(axis=0)
    present = failed * MARGINS[world.lane] * skill_ok[world.lane, cases]
    remaining = np.ones(len(cases), dtype=bool)
    selected = []
    horizon = min(design.lookahead, DAYS-day-1)
    for slot in range(REVIEW_LIMIT):
        net_bid = present-design.review_cost
        if slot < design.compute:
            route_gain = 2*route*(1-route)/(route_counts+1)**2
            skill_gain = 2*skills*(1-skills)/(skill_counts+1)**2
            stage_gain = ((1-patch)*skill_ok*route_gain + route_ok*skill_gain*permitted_pool[:,None])
            future_bid = horizon*(MARGINS[:,None]*market*stage_gain).sum(axis=0)
            net_bid = net_bid + future_bid[cases]-TRAIN_COST
        chosen = int(np.argmax(np.where(remaining, net_bid, -np.inf)))
        if net_bid[chosen] <= 0:
            break
        selected.append(chosen)
        remaining[chosen] = False
        route_counts[cases[chosen]] += 1
        skill_counts[:, cases[chosen]] += permitted_pool
    return np.asarray(selected, dtype=int)


def run(world, design, quotas=None):
    learners = Learners()
    cash = tickets = updates = native_updates = gate_errors = 0
    seen = np.zeros(FAMILIES, dtype=int)
    shift_quotas = []
    checkpoints = {}
    market = np.ones((3,FAMILIES))*PER_LANE/FAMILIES
    for day in range(DAYS):
        after = day >= WARMUP
        patch = design.patch if after else 0.
        mix_index = int(design.shift == "new_demand" and day>=DAYS//2)
        cases = world.cases[mix_index, day]
        truth = world.changed_truth if design.shift == "mobile_flip" and day>=DAYS//2 else world.base_truth
        route, local, pooled, native, use = learners.probabilities(world, design)
        gateway_wrong = (world.gate_coin[day] < route[cases]) != world.route[cases]
        failed = gateway_wrong & (world.patch_coin[day] >= patch)
        taken = (world.action_coin[day] < native[world.lane, cases])
        skill_ok = taken == truth[world.lane, cases]
        quota = REVIEW_LIMIT if quotas is None else quotas[day]
        selection = design.collection if after else "incidents"
        if design.collection == "economic":
            arrivals = np.zeros_like(market)
            np.add.at(arrivals, (world.lane,cases), 1)
            market = .85*market+.15*arrivals
        if selection == "economic":
            reviews = economic_reviews(learners,world,design,cases,failed,use,market,day)
        else:
            reviews = select_reviews(selection, failed, world.priority[day], cases, seen, quota)
        cleared = ~failed
        cleared[reviews] = True
        train = reviews[:design.compute]
        fam = cases[train]
        route_label = world.route[fam] ^ world.route_noise[day, train]
        intent_label = world.intent[fam] ^ world.intent_noise[day, train]
        learners.admit(fam, route_label, intent_label, design.portable)
        np.add.at(seen, fam, 1)
        calibration_cost = 0.
        if design.native_every and (day+1) % design.native_every == 0:
            native_cases = world.native[day]
            labels = truth[np.arange(3), native_cases] ^ world.native_noise[day]
            learners.native_update(native_cases, labels, local, pooled)
            calibration_cost = 3*(design.review_cost+TRAIN_COST)
            if after:
                native_updates += 3
        if after:
            cash += (MARGINS[world.lane]*(cleared & skill_ok)).sum()
            cash -= design.review_cost*len(reviews) + TRAIN_COST*len(train) + calibration_cost
            tickets += len(reviews)
            updates += len(train)
            gate_errors += failed.sum()
        shift_quotas.append(len(reviews))
        if day+1 in (WARMUP, 24, 36, 48, DAYS):
            route, _, _, native, use = learners.probabilities(world, design)
            route_ok = correct_probability(route, world.route)
            skill = correct_probability(native, truth)
            mix = world.new_mix if mix_index else world.mix
            gate = route_ok + patch*(1-route_ok)
            # All family frequencies are integrated exactly. No training outcome is used as an exam.
            capability = (mix*skill).sum(axis=1)
            auto = (mix*skill*gate).sum(axis=1)
            checkpoints[str(day+1)] = {
                "capability": capability.tolist(), "autonomous_orders": auto.tolist(),
                "gate": float((mix*gate).sum(axis=1).mean()),
                "auto_margin_per_triplet": float(MARGINS@auto), "pooled": use.astype(int).tolist()}
    end = checkpoints[str(DAYS)]
    return {"cash": float(cash), "tickets": tickets, "updates": updates, "native_updates": native_updates,
            "gate_incidents": int(gate_errors), "families": int((seen>0).sum()),
            "mobile_capability": end["capability"][2], "arm_capability": end["capability"][1],
            "desk_capability": end["capability"][0], "gate_capability": end["gate"],
            "autonomous_margin": end["auto_margin_per_triplet"], "mobile_pool": end["pooled"][2],
            "quotas": shift_quotas, "path": checkpoints}


def paired_stats(a):
    a = np.asarray(a, dtype=float)
    mean = a.mean()
    half = 1.96*a.std(ddof=1)/np.sqrt(len(a))
    return dict(mean=round(float(mean), 5), low=round(float(mean-half), 5), high=round(float(mean+half), 5))


def fleet_study(seed_count=96):
    reference = Design()
    patch = replace(reference, patch=.90)
    collection = replace(patch, collection="coverage")
    configs = {
        "incidents": reference, "patched_incidents": patch,
        "patched_uniform": replace(patch, collection="uniform"),
        "patched_fill": replace(patch, collection="fill"), "patched_coverage": collection,
        "unpatched_coverage": replace(collection, patch=0.),
        "matched_coverage": collection,
        "sealed_incidents": replace(reference, portable=False),
        "sealed_patched": replace(patch, portable=False),
        "native_dense": replace(reference, native_every=1),
        "native_dense_patched": replace(patch, native_every=1),
        "scarce_incidents": replace(patch, compute=1),
        "scarce_coverage": replace(collection, compute=1),
        "new_mix_incidents": replace(patch, shift="new_demand"),
        "new_mix_coverage": replace(collection, shift="new_demand"),
        "flipped_pool": replace(collection, shift="mobile_flip"),
        "flipped_local": replace(collection, shift="mobile_flip", sharing="local"),
        "flipped_validated": replace(collection, shift="mobile_flip", sharing="validated"),
        "steady_validated": replace(collection, sharing="validated"),
        "steady_local": replace(collection, sharing="local"),
    }
    # Select the most profitable fixed reserve on independent calibration worlds.
    # 0, 1, 2 or 3 reserved reviews, with priority to known incidents in all four.
    fixed_reserves = ("incidents","reserve_1","reserve_2","fill")
    calibration = {}
    for market_name, settings in (("steady", replace(patch,sharing="validated")),
                                  ("expensive", replace(patch,sharing="validated",review_cost=5.)),
                                  ("flip", replace(patch,sharing="validated",shift="mobile_flip"))):
        scores = {reserve: [] for reserve in fixed_reserves}
        lookaheads = {h: [] for h in (3,12,36,60)}
        for seed in range(88000,88024):
            world = World(seed)
            for reserve in fixed_reserves:
                scores[reserve].append(run(world,replace(settings,collection=reserve))["cash"])
            for h in lookaheads:
                lookaheads[h].append(run(world,replace(settings,collection="economic",lookahead=h))["cash"])
        means = {k: round(float(np.mean(v)),5) for k,v in scores.items()}
        winner = max(means, key=means.get)
        horizon_scores = {h: round(float(np.mean(v)),5) for h,v in lookaheads.items()}
        horizon = max(horizon_scores, key=horizon_scores.get)
        calibration[market_name] = {"selected":winner,"mean_cash":means,
                                    "selected_horizon":horizon,"horizon_mean_cash":horizon_scores}
        configs["economic_"+market_name] = replace(settings,collection="economic")
        configs["tuned_"+market_name] = replace(settings,collection="economic",lookahead=horizon)
        configs["fixed_"+market_name] = replace(settings,collection=winner)
    data = {name: [] for name in configs}
    for seed in range(91000, 91000+seed_count):
        world = World(seed)
        for name, config in configs.items():
            # Deliberately retrospective comparator to isolate the composition of equal update counts.
            quotas = data["patched_incidents"][-1]["quotas"] if name == "matched_coverage" else None
            data[name].append(run(world, config, quotas))
    keys = [name for name in data["incidents"][0] if name not in ("path", "quotas")]
    summaries = {name: {key: round(float(np.mean([row[key] for row in group])), 5) for key in keys}
                 for name, group in data.items()}
    comparisons = [
        ("patched_incidents", "incidents"), ("patched_coverage","unpatched_coverage"),
        ("sealed_patched", "sealed_incidents"), ("native_dense_patched", "native_dense"),
        ("patched_coverage","patched_incidents"), ("patched_uniform","patched_incidents"),
        ("patched_coverage","patched_fill"), ("patched_coverage","patched_uniform"),
        ("matched_coverage","patched_incidents"), ("scarce_coverage","scarce_incidents"),
        ("new_mix_coverage","new_mix_incidents"), ("flipped_validated","flipped_pool"),
        ("flipped_validated","flipped_local"), ("steady_validated","patched_coverage"),
        ("flipped_pool","flipped_local"), ("patched_coverage","steady_local"),
        ("economic_steady","fixed_steady"), ("economic_expensive","fixed_expensive"),
        ("economic_flip","fixed_flip"), ("tuned_steady","fixed_steady"),
        ("tuned_expensive","fixed_expensive"), ("tuned_flip","fixed_flip")]
    diffs = {a+" minus "+b: {k: paired_stats([x[k]-y[k] for x,y in zip(data[a],data[b])])
                              for k in keys} for a,b in comparisons}
    paths = {name:{epoch:{k:np.round(np.mean([r["path"][epoch][k] for r in group],axis=0),5).tolist()
                          for k in ("capability","autonomous_orders","gate","pooled")}
                   for epoch in group[0]["path"]} for name,group in data.items()}
    return {"worlds": seed_count, "first_seed": 91000, "days": DAYS, "warmup": WARMUP,
            "lanes": LANES, "fixed_reserve_calibration": calibration,
            "means": summaries, "paired": diffs, "learning_paths": paths}
