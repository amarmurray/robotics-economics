"""Priced discovery of a reusable correction. Python 3 and NumPy."""
from pathlib import Path
import json
import numpy as np

FAMILIES = 16
SHIFTS = 72
MARGIN = np.array([7., 10.])
FEATURES = ((np.arange(16)[:, None] >> np.arange(4)) & 1).T
RULES = np.concatenate([FEATURES, 1 - FEATURES, np.zeros((1, 16)), np.ones((1, 16))])


def world(first, count, regime):
    # Each site has independent features-to-family assignments, order tape and shocks.
    rng = np.random.default_rng(first)
    family = rng.random((count, 16)).argsort(axis=1)
    rules = RULES[:, family].transpose(1, 0, 2)
    axis = rng.integers(0, 8, (count, 2))
    truth = rules[np.arange(count)[:, None], axis].copy()
    shuffled = rng.random((count, 16)).argsort(axis=1)
    fragmented = rng.random((count, 2, 16)).argsort(axis=2) < 8
    if regime == "common":
        truth[:, 1] = truth[:, 0]
        axis[:, 1] = axis[:, 0]
    if regime == "fragmented":
        truth = fragmented
    tape = rng.random((SHIFTS, count, 2, 11))
    return rules, axis, truth, shuffled, tape


def simulate(w, design, regime, period=8, price=.9, reserve=False, select="diversity"):
    rules, axis, truth, shuffled, tape = w
    n = len(truth)
    sites = np.arange(n)
    rows = sites[:, None]
    lanes = np.arange(2)
    model = np.take_along_axis(rules, shuffled[:, None, :], axis=2) if design == "shuffled" else rules
    score = np.zeros((n, 2, 10))
    local = np.zeros((n, 2, 16))
    live = local.copy()
    pending = None
    digital = np.full(n, .82)
    ledger = np.zeros((n, 7))
    # cols: net, paid orders, paid annotations, validations, donor updates, holdout skill, releases
    for t, u in enumerate(tape):
        correct = truth.copy()
        if t < 12:
            correct[:] = 0
        if regime == "reversal" and t >= 48:
            correct = 1 - truth
        if regime == "new_site":
            alternative = (axis + 1) % 4 + 4 * (axis // 4)
            correct[:, :, 12:] = rules[rows, alternative][:, :, 12:] if t >= 12 else 0
        if t in (19, 47):
            digital = np.maximum(.52, digital - .22)
        if pending and t == pending[0]:
            live = pending[1]
        # Discovery on families 0..7. Independent qualification on 8..11.
        # Families 12..15 generate orders but can never enter either training or qualification.
        logits = score - score.max(axis=2, keepdims=True)
        weight = np.exp(logits)
        prediction = np.einsum('nlh,nhk->nlk', weight / weight.sum(axis=2, keepdims=True), model)
        if design == "mixture":
            # Equal prior odds for a common rule versus two independent uniform rules.
            joint = score.sum(axis=1)
            log_joint = np.logaddexp.reduce(joint, axis=1)
            log_separate = np.logaddexp.reduce(score, axis=2).sum(axis=1)
            odds = log_joint - log_separate + np.log(score.shape[2])
            common_weight = (1 / (1 + np.exp(-odds)))[:, None, None]
            joint_prob = np.exp(joint - log_joint[:, None])
            pooled = np.einsum("nh,nhk->nk", joint_prob, model)
            prediction = (1-common_weight)*prediction + common_weight*pooled[:, None, :]
        if design == "supplied":
            prediction = rules[rows, axis]
        elif design in ("local", "direct_local"):
            prediction = (local > 0).astype(float)
        elif design == "global":
            prediction = np.broadcast_to((local.sum(axis=2, keepdims=True) > 0).astype(float), live.shape)
        if design == "direct_local":
            live = prediction.copy()
        if design not in ("raw", "direct_local") and t % period == 0 and t + 2 < SHIFTS:
            f = 8 + (u[:, :, 0] * 4).astype(int)
            f2 = 8 + (u[:, :, 1] * 4).astype(int)
            proposal = prediction > .5
            candidates = np.stack((live, np.zeros_like(live), proposal), axis=2)
            def hits(families):
                return candidates[rows, lanes, :, families] == correct[rows, lanes, families, None]
            # Independent of production, two draws per lane, incumbent wins ties.
            winner = (hits(f).astype(int) + hits(f2)).argmax(axis=2)
            pending = (t + 2, candidates[rows, lanes, winner].copy())
            ledger[:, 3] += 1
            ledger[:, 0] -= 2
            ledger[:, 6] += (winner != 0).sum(axis=1)
        family = (u[:, :, 2] * 16).astype(int)
        if t >= 36:
            family = np.where(u[:, :, 3] < .35, 12 + family % 4, family)
        routed = u[:, :, 4] < digital[:, None]
        ok = live[rows, lanes, family] == correct[rows, lanes, family]
        completed = routed & (u[:, :, 5] < np.where(ok, .94, .12))
        ledger[:, 1] += completed.sum(axis=1)
        ledger[:, 0] += completed @ MARGIN
        available = routed & ~completed & (family < 8) & (u[:, :, 6] < [.85, .55])
        if design in ("raw", "supplied"):
            available[:] = False
        uncertainty = 1 - abs(2 * prediction[rows, lanes, family] - 1)
        priority = u[:, :, 7] + (2 * uncertainty if select == "diversity" else 0)
        j = np.where(available, priority, -10).argmax(axis=1)
        bought = available.any(axis=1)
        i = sites[bought]
        lane = j[bought]
        k = family[i, lane]
        observation = correct[i, lane, k].astype(bool) ^ (u[i, lane, 8] < .08)
        score *= .96
        local *= .96
        evidence = np.where(model[i, :, k] == observation[:, None], 1., -1.)
        if design == "pooled":
            score[i] += evidence[:, None, :]
        else:
            score[i, lane] += evidence
        local[i, lane, k] += np.where(observation, 1., -1.)
        ledger[:, 2] += bought
        ledger[:, 0] -= price * bought
        donor = (~routed).any(axis=1) & (~bought | reserve)
        digital += .18 * (.96 - digital) * donor
        ledger[:, 4] += donor
        ledger[:, 0] -= .3 * donor
        ledger[:, 5] += (live[:, :, 12:] == correct[:, :, 12:]).mean(axis=(1, 2)) / SHIFTS
    return ledger


def interval(values):
    m = values.mean()
    d = 1.96 * values.std(ddof=1) / len(values)**.5
    return np.round([m, m-d, m+d], 4).tolist()


def study():
    calibration = world(604, 128, "independent")
    arms = ["learned", "shuffled", "supplied", "local", "global", "pooled", "mixture", "direct_local", "raw"]
    schedule = {}
    for arm in arms:
        options = [(p, s) for p in (4, 8, 12) for s in ("uniform", "diversity")]
        schedule[arm] = max(options, key=lambda z: simulate(calibration, arm, "independent", z[0], select=z[1])[:, 0].mean())
    results = {}
    for regime in ("independent", "common", "fragmented", "new_site", "reversal"):
        w = world(72804, 1024, regime)
        def run(arm, reserve=False, match=None):
            p,s = schedule[match or arm]
            return simulate(w, arm, regime, p, reserve=reserve, select=s)
        runs = {a:run(a) for a in arms}
        runs["matched_shuffle"] = run("shuffled", match="learned")
        mixture_same = run("mixture", match="learned")
        protected = run("learned", True)
        results[regime] = dict(means={a:np.round(x.mean(axis=0),4).tolist() for a,x in runs.items()},
            learned_minus={a:interval(runs["learned"][:,0]-x[:,0]) for a,x in runs.items()},
            mixture_matched_minus_separate=interval(mixture_same[:,0]-runs["learned"][:,0]),
            mixture_minus={a:interval(runs["mixture"][:,0]-runs[a][:,0]) for a in ("learned","pooled","direct_local","raw")},
            reserve_interaction=interval(protected[:,0]-runs["learned"][:,0]-(run("raw",True)[:,0]-runs["raw"][:,0])),
            skill_minus_shuffle=interval(runs["learned"][:,5]-runs["matched_shuffle"][:,5]))
    return dict(schedule=schedule,means_columns=["net","paid_orders","pairs","audits","donor_updates","untouched_agreement","release_changes"],results=results)


if __name__ == "__main__":
    Path(__file__).with_name("results.json").write_text(json.dumps(study(), indent=2)+"\n")
