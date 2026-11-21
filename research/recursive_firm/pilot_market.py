"""Economic learning with private payoffs and first-trial contracts. Standard library only."""
from dataclasses import dataclass
from fractions import Fraction
from itertools import product
import json
import math
import random

from evidence_budget import evidence_results


VALUE = 10
COST = 3
DATES = 3
FEE_CAP = 8
TAG_COST = 1
FEES = (3.25, 4.5, 6.0, 8.0)
TRAIN_COHORTS = 12000
TEST_COHORTS = 3000
SEEDS = tuple(range(8))


@dataclass(frozen=True)
class Offer:
    first: float
    repeat: float

    @property
    def uses_registry(self):
        return self.first != self.repeat


def buyer_gain(offer, probability):
    return probability * (VALUE + (DATES - 1) * (VALUE - offer.repeat)) - offer.first


def settle(offer, mature, accepts, transferable):
    """Buyer receives actual service value, supplier incurs cost, fees are transfers."""
    seller = mature * DATES * (offer.repeat - COST) - TAG_COST * offer.uses_registry
    buyers = mature * DATES * (VALUE - offer.repeat)
    if accepts:
        seller += offer.first - COST
        buyers -= offer.first
        if transferable:
            seller += (DATES - 1) * (offer.repeat - COST)
            buyers += VALUE + (DATES - 1) * (VALUE - offer.repeat)
    return seller, buyers


def exact_returns(offer, mature, probability):
    # At exact indifference the customer accepts. The three reported example offers
    # use strict choices. The continuous uniform-price bound uses weak participation.
    accepts = buyer_gain(offer, probability) >= 0
    good = settle(offer, mature, accepts, True)
    bad = settle(offer, mature, accepts, False)
    seller, buyers = (probability * x + (1 - probability) * y for x, y in zip(good, bad))
    return {"pilot": bool(accepts), "seller": float(seller), "buyers": float(buyers),
            "joint": float(seller + buyers)}


class SourceAgent:
    """UCB over fee schedules using only settled source contribution."""
    def __init__(self, tagged, rng):
        terms = product(FEES, repeat=2) if tagged else ((fee, fee) for fee in FEES)
        self.offers = [Offer(first, repeat) for first, repeat in terms]
        rng.shuffle(self.offers)
        self.counts = [0] * len(self.offers)
        self.means = [0.0] * len(self.offers)
        self.period = 0

    def quote(self):
        if self.period < len(self.offers):
            return self.period
        # Largest range of realized pilot contribution under any one offer is 15.
        scale = 15 * math.sqrt(2 * math.log(self.period))
        return max(range(len(self.offers)), key=lambda i: self.means[i] + scale / math.sqrt(self.counts[i]))

    def update(self, arm, contribution):
        self.counts[arm] += 1
        self.means[arm] += (contribution - self.means[arm]) / self.counts[arm]
        self.period += 1

    def frozen_quote(self):
        return self.offers[max(range(len(self.offers)), key=self.counts.__getitem__)]


class TargetAgent:
    """A downstream buyer samples its own posterior and sees only purchased trials."""
    def __init__(self, rng):
        self.successes = self.failures = 1
        self.rng = rng

    def accept(self, offer, training):
        if training:
            belief = self.rng.betavariate(self.successes, self.failures)
        else:
            belief = self.successes / (self.successes + self.failures)
        return buyer_gain(offer, belief) >= 0

    def record_first_trial(self, success):
        self.successes += int(success)
        self.failures += int(not success)


def train(seed, mature, probability, tagged):
    seller = SourceAgent(tagged, random.Random(5000 + seed))
    buyer = TargetAgent(random.Random(7000 + seed))
    world = random.Random(9000 + seed)
    for _ in range(TRAIN_COHORTS):
        works = world.random() < probability
        arm = seller.quote()
        offer = seller.offers[arm]
        accepts = buyer.accept(offer, training=True)
        seller_return, _ = settle(offer, mature, accepts, works)
        seller.update(arm, seller_return)
        if accepts:
            buyer.record_first_trial(works)
    return seller.frozen_quote(), buyer


def evaluate(mature, training_probability, test_probability, tagged):
    all_fees, pilot_counts, seller_total, buyers_total = {}, 0, 0.0, 0.0
    by_seed = []
    for seed in SEEDS:
        offer, buyer = train(seed, mature, training_probability, tagged)
        # Identical exogenous histories across institutions. No held-out outcomes train either agent.
        world = random.Random(20000 + seed)
        accepts = buyer.accept(offer, training=False)
        count = TEST_COHORTS * int(accepts)
        seller_seed = buyers_seed = 0.0
        for _ in range(TEST_COHORTS):
            works = world.random() < test_probability
            s, b = settle(offer, mature, accepts, works)
            seller_seed += s
            buyers_seed += b
        key = f"{offer.first:g}/{offer.repeat:g}"
        all_fees[key] = all_fees.get(key, 0) + 1
        pilot_counts += count
        seller_total += seller_seed
        buyers_total += buyers_seed
        by_seed.append(round((seller_seed + buyers_seed) / TEST_COHORTS, 4))
    size = len(SEEDS) * TEST_COHORTS
    return {"frozen_fee_pairs_first_repeat": all_fees, "pilot_rate": pilot_counts / size,
            "seller": round(seller_total / size, 4), "buyers": round(buyers_total / size, 4),
            "joint": round((seller_total + buyers_total) / size, 4), "joint_by_seed": by_seed}


def results():
    p = Fraction(1, 4)
    precision = Fraction(1, 20)
    low = Offer(Fraction(5), Fraction(5))
    high = Offer(Fraction(8), Fraction(8))
    trial = Offer(Fraction(13, 4), Fraction(8))
    return {
        "settings": {"gross_qualified_value": VALUE, "real_cost": COST, "dates": DATES,
                     "price_cap": FEE_CAP, "registry_cost_per_cohort": TAG_COST, "fees": FEES,
                     "training_cohorts_per_seed": TRAIN_COHORTS, "test_cohorts_per_seed": TEST_COHORTS,
                     "training_seeds": SEEDS, "held_out_world_seeds": [20000 + s for s in SEEDS]},
        "exact_at_p_quarter": {"one_mature_uniform_8": exact_returns(high, 1, p),
                               "one_mature_best_pilot_admitting_uniform_5": exact_returns(low, 1, p),
                               "one_mature_verified_first_3_25_repeat_8": exact_returns(trial, 1, p),
                               "no_mature_uniform_5": exact_returns(low, 0, p)},
        "learned_rules": {"uniform_no_mature": evaluate(0, float(p), float(p), False),
                          "uniform_one_mature": evaluate(1, float(p), float(p), False),
                          "registry_available_one_mature": evaluate(1, float(p), float(p), True),
                          "registry_available_unannounced_low_transfer": evaluate(1, float(p), float(precision), True)},
        "research_agent": evidence_results(),
    }


if __name__ == "__main__":
    print(json.dumps(results(), indent=2))
