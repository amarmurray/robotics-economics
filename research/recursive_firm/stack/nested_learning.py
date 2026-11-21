"""Nested economic RL with trainable one-step digital and physical controllers."""
from collections import Counter
from itertools import product
import json
import math
import random

DOMAINS = ("desk", "arm", "mobile")
TASK_WEIGHTS = ((.45,.30,.15,.10), (.55,.25,.12,.08), (.08,.12,.32,.48))
ACTIONS = ("ledger", "arm_local", "mobile_local", "arm_pool", "mobile_pool", "replay_pool", "urgent")
SHIFTS = 6
TRAIN_EPISODES = 2400
TEST_EPISODES = 160
MARKETS = {"desk_weighted": ((40,12,4),True), "depot_weighted": ((4,10,50),True),
           "depot_without_alignment": ((4,10,50),False)}


def logistic(x):
    return 1 / (1 + math.exp(-x))


class Cell:
    def __init__(self, seed, margins, aligned, rights=("portable","portable")):
        rng = random.Random(seed)
        self.seed, self.margins, self.aligned, self.rights = seed, margins, aligned, rights
        geometry = [rng.choice((-1,1)) for _ in range(4)]
        self.sign = [[rng.choice((-1,1)) for _ in range(4)], geometry,
                     [(-v if i%2 else v) for i,v in enumerate(geometry)]]
        self.local = [[rng.uniform(-0.6,0.6) for _ in range(4)] for _ in DOMAINS]
        self.shared = [0.0]*4
        self.buffers = {1: {}, 2: {}}
        self.t = 0

    def transform(self, domain, family):
        return -1 if domain == 2 and self.aligned and family%2 else 1

    def logit(self, domain, family):
        value = self.local[domain][family]
        if domain:
            value += self.transform(domain, family)*self.shared[family]
        return value

    def rates(self):
        return tuple(sum(w*logistic(self.sign[d][i]*self.logit(d,i))
                         for i,w in enumerate(TASK_WEIGHTS[d])) for d in range(3))

    def paid_output(self, rates=None):
        desk,arm,mobile = self.rates() if rates is None else rates
        digital_value,plant_value,depot_value = self.margins
        return desk*(digital_value + arm*plant_value + mobile*depot_value)

    def eligible(self):
        actions = ["ledger", "urgent"]
        portable_rows = False
        for d in (1,2):
            if self.rights[d-1] in ("local","portable"):
                actions.append(DOMAINS[d]+"_local")
            if self.rights[d-1] == "portable":
                actions.append(DOMAINS[d]+"_pool")
                portable_rows |= bool(self.buffers[d])
        if portable_rows:
            actions.append("replay_pool")
        return actions

    def observation(self, rates):
        # The upper agent receives task-level validation, its remaining budget and lawful registry availability.
        return (self.t, min(range(3), key=rates.__getitem__), "replay_pool" in self.eligible())

    def gradient(self, d, i, sign, shared):
        # Exact policy gradient for one binary-action correction with a unique successful action.
        q = logistic(self.logit(d,i))
        step = 1.8 * sign * q * (1-q)
        if shared:
            self.shared[i] += self.transform(d,i)*step
        else:
            self.local[d][i] += step

    def step(self, action):
        if action not in self.eligible():
            raise ValueError("Action exceeds available rights or corpus")
        rng = random.Random(1009*self.seed+37*self.t+19)
        sampled = None
        source = {"arm":1,"mobile":2}.get(action.split("_")[0])
        if source:
            # Corrections come from the current policy's failures conditional on a recoverable live job.
            weights = [w*(1-logistic(self.sign[source][i]*self.logit(source,i)))
                       for i,w in enumerate(TASK_WEIGHTS[source])]
            family = rng.choices(range(4),weights)[0]
            self.buffers[source][family] = self.sign[source][family]
            sampled = (DOMAINS[source],family)
        shared = action.endswith("_pool")
        if action == "ledger":
            # A separately licensed archive can be replayed while the operator rescues an urgent job.
            for _ in range(4):
                i = rng.choices(range(4),TASK_WEIGHTS[0])[0]
                self.gradient(0,i,self.sign[0][i],False)
        elif action != "urgent":
            if shared:
                sources = [d for d in (1,2) if self.rights[d-1]=="portable" and self.buffers[d]]
            else:
                sources = [source]
            # Balance donors, then draw distinct families with replacement. Repeated rescues of
            # the same family do not create extra rows. All methods get four gradient steps.
            for _ in range(4):
                d = rng.choice(sources)
                i = rng.choice(tuple(self.buffers[d]))
                self.gradient(d,i,self.buffers[d][i],shared)
        self.t += 1
        rescue = .25 if source else .90
        cost = .15 if action != "urgent" else 0
        return rescue-cost, sampled


def choose_q(q, obs, actions):
    return max(actions,key=lambda a:q.get((obs,a),0))


def train(margins, aligned, replication=0):
    q = {}
    rng = random.Random(749 + replication)
    for seed in range(TRAIN_EPISODES):
        cell = Cell(seed + 100000*replication,margins,aligned)
        rates = cell.rates()
        for _ in range(SHIFTS):
            obs = cell.observation(rates)
            actions = cell.eligible()
            choice = rng.choice(actions) if rng.random()<.28 else choose_q(q,obs,actions)
            old = cell.paid_output(rates)
            cash,_ = cell.step(choice)
            rates = cell.rates()
            reward = cash + cell.paid_output(rates) - old
            future = 0
            if cell.t < SHIFTS:
                nxt = cell.observation(rates)
                future = max(q.get((nxt,a),0) for a in cell.eligible())
            key=(obs,choice)
            previous=q.get(key,0)
            q[key]=previous+.06*(reward+future-previous)
    return q


def rollout(seed, margins, aligned, policy):
    cell = Cell(seed,margins,aligned)
    cash, counts, families = 0.0, Counter(), Counter()
    for _ in range(SHIFTS):
        action = policy(cell)
        receipt,sample = cell.step(action)
        cash += receipt
        counts[action] += 1
        if sample:
            families[f"{sample[0]}_{sample[1]}"] += 1
    return cell.paid_output()+cash,counts,families


def fixed(sequence):
    def act(cell):
        choice = sequence[cell.t%len(sequence)]
        return choice if choice in cell.eligible() else "urgent"
    return act


def lowest_rate(cell):
    rates = cell.rates()
    d = min(range(3),key=rates.__getitem__)
    return "ledger" if d==0 else DOMAINS[d]+("_pool" if cell.aligned else "_local")


def study(margins, aligned):
    q = train(margins,aligned)
    active = lambda cell: choose_q(q,cell.observation(cell.rates()),cell.eligible())
    calibration = range(12000,12032)
    def price(seq):
        return sum(rollout(seed,margins,aligned,fixed(seq))[0] for seed in calibration)
    sequence = max(product(ACTIONS,repeat=2),key=price)
    policies = {"economic_q":active, "fixed_schedule":fixed(sequence), "lowest_task_accuracy":lowest_rate}
    rows = {}
    seed_scores = {}
    for name,policy in policies.items():
        totals, counts, families = [], Counter(), Counter()
        for seed in range(30000,30000+TEST_EPISODES):
            score,actions,observed = rollout(seed,margins,aligned,policy)
            totals.append(score)
            counts.update(actions)
            families.update(observed)
        rows[name] = {"net":round(sum(totals)/len(totals),5), "actions":dict(counts),
                      "sampled_failure_families":dict(families)}
        seed_scores[name] = totals
    def paired_summary(totals, reference):
        diffs = [a-b for a,b in zip(totals, reference)]
        mean = sum(diffs)/len(diffs)
        se = math.sqrt(sum((x-mean)**2 for x in diffs)/(len(diffs)*(len(diffs)-1)))
        return {"difference":round(mean,5),"paired_mc_95":[round(mean-1.96*se,5),round(mean+1.96*se,5)]}
    repetitions = []
    for i in range(4):
        totals = seed_scores["economic_q"]
        if i:
            fitted = train(margins, aligned, i)
            rule = lambda cell: choose_q(fitted,cell.observation(cell.rates()),cell.eligible())
            totals = [rollout(j,margins,aligned,rule)[0] for j in range(30000,30000+TEST_EPISODES)]
        repetitions.append({"training_replication":i, "vs_fixed":paired_summary(totals,seed_scores["fixed_schedule"]),
                            "vs_lowest_accuracy":paired_summary(totals,seed_scores["lowest_task_accuracy"])})
    return {"basket_margins":margins,"mobile_action_map_aligned":aligned,"best_tested_fixed_pair":sequence,
            "held_out":rows,"independent_training_runs":repetitions}


def results():
    return {"training_episodes_per_economy":TRAIN_EPISODES, "shifts":SHIFTS,
            "fixed_schedule_selection_seeds":[12000,12031], "test_seeds":[30000,30000+TEST_EPISODES-1],
            "markets":{name:study(*settings) for name,settings in MARKETS.items()}}


if __name__ == "__main__":
    print(json.dumps(results(),indent=2))
