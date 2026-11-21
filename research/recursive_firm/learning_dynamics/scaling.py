"""Published robot-score reanalysis, endogenous feedback clock, and optimal review interval."""
from functools import lru_cache
from math import expm1, log

import numpy as np


# Published aggregate rubric scores in Lin et al., arXiv:2410.18647v1, Tables 6 and 10.
# Rows are 1, 2, ..., 32 distinct environment-object pairs at powers of two.
# Each row's columns run from 1/pairs to 100% of the collected traces per pair.
SCORES = {
    "pour_water": (9, [
        [.45], [1.65, 1.425], [2.725, 5.3, 5.325], [4.95, 6.175, 5.775, 5.625],
        [4.8, 5.8, 6.9, 6.95, 6.875], [3.95, 5.225, 6.95, 7.575, 8.3, 7.875]]),
    "arrange_mouse": (6, [
        [.75], [.975, .875], [1.8, 2.3, 2.325], [2.425, 3.725, 3.425, 3.35],
        [3.375, 4.925, 4.5, 5.05, 4.75], [4.225, 4.225, 5.075, 5.2, 5.6, 5.525]]),
}


def cells(maximum, rows):
    return [(2**row, 2**col, score / maximum)
            for row, scores in enumerate(rows) for col, score in enumerate(scores)]


def holdout(rows, maximum_pairs):
    """Fit below a held-out breadth. All loss is in normalized rubric-score units."""
    train = [r for r in rows if r[0] < maximum_pairs]
    test = [r for r in rows if r[0] == maximum_pairs]
    def features(pair_count, volume, with_breadth):
        return [1, log(volume)] + ([log(pair_count)] if with_breadth else [])
    forecasts = {}
    for model, with_breadth in (("volume_power", False), ("volume_and_breadth_power", True)):
        design = [features(j, v, with_breadth) for j, v, _ in train]
        beta = np.linalg.lstsq(design, np.log([1-s for _, _, s in train]), rcond=None)[0]
        predicted = [np.clip(1-np.exp(np.dot(features(j, v, with_breadth), beta)), 0, 1)
                     for j, v, _ in test]
        forecasts[model] = predicted
    # Flexible count-only benchmark, with a plateau for previously unseen volumes.
    available = sorted({v for _, v, _ in train})
    fitted = {v: np.mean([s for _, count, s in train if count == v]) for v in available}
    forecasts["volume_lookup"] = [fitted[min(v, available[-1])] for _, v, _ in test]
    return {model: {"mae": round(float(np.mean([abs(p-r[2]) for p, r in zip(pred, test)])), 6),
                    "predicted_scores": np.round(pred, 5).tolist()}
            for model, pred in forecasts.items()}


def published_scores():
    results = {}
    for name, (maximum, data) in SCORES.items():
        rows = cells(maximum, data)
        lookup = {(j, v): s for j, v, s in rows}
        comparisons = {str(v): {"narrow": round(lookup[v, v], 6),
                                 "broad": round(lookup[32, v], 6),
                                 "difference_pp": round(100*(lookup[32, v]-lookup[v, v]), 3)}
                       for v in (2, 4, 8, 16)}
        results[name] = {"equal_nominal_volume": comparisons,
                         "holdout": {str(j): holdout(rows, j) for j in (16, 32)}}
    return results


def clock_error(t, alpha=.5, gamma=1.0, initial_error=.5):
    """Conditional fluid identity for error against opportunities when useful yield is error**gamma."""
    return initial_error * (1 + (1+alpha*gamma)*initial_error**gamma*t)**(-alpha/(1+alpha*gamma))


def stochastic_clock(alpha, gamma, seed_count=160):
    """Exact event-time Bernoulli process. Geometric waiting times avoid time-step bias."""
    sizes = np.array([256, 1024, 4096, 16384, 65536])
    log_slope = []
    last = []
    for seed in range(seed_count):
        rng = np.random.default_rng(20300+seed)
        n = 0
        elapsed = 0
        errors = []
        for t in sizes:
            while elapsed <= t:
                n += 1
                elapsed += rng.geometric((.5*n**(-alpha))**gamma)
            # Only n-1 useful labels have arrived at this evaluation point.
            errors.append(.5*n**(-alpha))
        log_slope.append(-np.polyfit(np.log(sizes[-3:]), np.log(errors[-3:]), 1)[0])
        last.append(errors[-1])
    return {"theory": alpha/(1+alpha*gamma), "mean_tail_slope": round(float(np.mean(log_slope)), 5),
            "mean_final_error": round(float(np.mean(last)), 6), "seeds": seed_count,
            "opportunities": sizes.tolist()}


def scale_fleet(worlds=256, shifts=128):
    """Binomial arrival of distinct usable incident records under staffing and compute caps."""
    rng = np.random.default_rng(107572)
    coins = rng.random((shifts, worlds, 64))
    configurations = ((1, 1), (4, 1), (16, 1), (64, 1), (4, 4), (16, 4), (64, 4),
                      (16, 16), (64, 16), (64, 64))
    data = {}
    for mode in ("independent", "common_record"):
        for replicas, slots in configurations:
            independent_sources = replicas if mode == "independent" else 1
            n = np.zeros(worlds)
            binding = np.zeros(worlds)
            for tape in coins:
                p = .5*(1+n)**(-.5)
                arrivals = (tape[:, :independent_sources] < p[:, None]).sum(axis=1)
                binding += arrivals > slots
                n += np.minimum(arrivals, slots)
            data[mode, replicas, slots] = (.5*(1+n)**(-.5), n, binding/shifts)
    means = {f"{mode}_{f}_{k}": dict(error=round(float(e.mean()),6),
                                      distinct_updates=round(float(n.mean()),4),
                                      shifts_losing_updates=round(float(b.mean()),4))
             for (mode,f,k),(e,n,b) in data.items()}
    paired = {}
    for left, right in [((64,1),(16,1)),((64,16),(64,1)),((64,64),(64,16))]:
        a = data["independent",*left][0]-data["independent",*right][0]
        center, half = a.mean(), 1.96*a.std(ddof=1)/np.sqrt(worlds)
        paired[str(left)+" minus "+str(right)] = np.round([center,center-half,center+half],6).tolist()
    return {"worlds": worlds, "shifts": shifts, "means": means, "paired_final_error": paired}


def frontier(horizon, donor_support=2, trial_cost=3., trial_yield=1., trials=True):
    """Qualification opens a second workflow that then supplies its own distinct evidence."""
    cap, qualification = 9, 4
    def skill(n):
        return .5+.05*n
    @lru_cache(None)
    def plan(left, n, donor_left):
        if not left:
            return 0., False
        qualified = n>=qualification
        receipts = 2.+(6*skill(n)-3 if qualified else 0)
        after = min(cap,n+int(donor_left>0)+int(qualified))
        next_donor = max(0,donor_left-1)
        ordinary = plan(left-1,after,next_donor)[0]
        if trials and after<cap:
            successful = plan(left-1,after+1,next_donor)[0]
            improvement = trial_yield*(successful-ordinary)-trial_cost
            if improvement>1e-10:
                return receipts+ordinary+improvement, True
        return receipts+ordinary, False
    # Independent forward accounting under the selected strategy, including failed paid trials.
    distribution = {(0,donor_support): 1.}
    cash = paid = 0.
    trajectory = []
    for t in range(horizon):
        population = {}
        qualified_share = area = new_records = 0.
        for (n,donor_left), mass in distribution.items():
            spend = plan(horizon-t,n,donor_left)[1]
            qualified = n>=qualification
            qualified_share += mass*qualified
            area += mass*(skill(n) if qualified else 0)
            new_records += mass*n
            cash += mass*(2.+(6*skill(n)-3 if qualified else 0)-trial_cost*spend)
            paid += mass*spend
            after = min(cap,n+int(donor_left>0)+int(qualified))
            chance = trial_yield if spend else 0.
            for increment,weight in ((0,1-chance),(1,chance)):
                if weight:
                    state = (min(cap,after+increment),max(0,donor_left-1))
                    population[state] = population.get(state,0.)+mass*weight
        trajectory.append({"shift":t+1, "expected_start_records":round(new_records,5),
                           "qualified_share":round(qualified_share,5),
                           "mix_completion":round((.95+area)/(1+qualified_share),5)})
        distribution = population
    assert abs(plan(horizon,0,donor_support)[0]-cash)<1e-8
    return {"value":round(cash,5), "expected_paid_trials":round(paid,5), "trajectory":trajectory}


def frontier_experiments():
    return {name:frontier(h,d,c,q,allow) for name,h,d,c,q,allow in (
        ("short",4,2,3.,1.,True), ("long",16,2,3.,1.,True), ("long_passive",16,2,3.,1.,False),
        ("adequate_transfer_passive",16,4,3.,1.,False), ("uncertain_trials",16,2,3.,.5,True),
        ("no_trial_yield",16,2,3.,0.,True))}


def review_value(interval, hazard, delay, fee, gain=1):
    """Per-shift expected reward with a perfect audit of the state 'delay' shifts ago."""
    if interval is None:
        return gain/2
    rho = 1-2*hazard
    accumulation = -expm1(interval*log(rho))/(1-rho)
    return gain/2 + (gain*rho**delay*accumulation/2 - fee)/interval


def best_review(hazard, delay, fee, gain=1):
    limit = gain*(1-2*hazard)**delay/(4*hazard)
    if fee >= limit:
        return None, gain/2
    value = review_value(1, hazard, delay, fee, gain)
    interval = 1
    # Geometric marginal gains decrease. Average net reward is unimodal.
    while True:
        candidate = review_value(interval+1, hazard, delay, fee, gain)
        if candidate <= value:
            return interval, value
        interval += 1
        value = candidate


def finite_review(hazard, delay, fee, horizon):
    """Independent Bellman solution from an unknown symmetric regime, no periodicity constraint."""
    ages = np.arange(horizon+1)
    correct = (1+(1-2*hazard)**(delay+ages))/2
    future = np.zeros(horizon+1)
    unknown = 0.
    for _ in range(horizon):
        buy = correct[0] - fee + future[1]
        unknown = max(.5+unknown, buy)
        future = np.maximum(buy, correct+future[np.minimum(ages+1, horizon)])
    return unknown/horizon


def review_study():
    rows = []
    for delay in (0, 3, 8):
        for hazard in (.01, .05, .10, .20, .30):
            interval, value = best_review(hazard, delay, .60)
            rows.append({"hazard": hazard, "delay": delay, "interval": interval,
                         "mean_reward": round(value, 6),
                         "finite_600": round(finite_review(hazard, delay, .60, 600), 6)})
    return rows


def study():
    return {"public_robot_scores": published_scores(),
            "conditional_clock": [dict(alpha=a, gamma=g, **stochastic_clock(a, g))
                                  for a, g in ((.25, 1), (.5, 1), (1, 1), (.5, 2))],
            "replicas_and_update_capacity": scale_fleet(), "frontier":frontier_experiments(),
            "review_fee": .60, "review": review_study()}
