"""Does a matched diagnostic purchase reach the market where a transfer can fail?"""
import json
from pathlib import Path

import numpy as np

from model import DECAY, Q, ZERO, Economy, draw
from study import EVALUATION, difference


PRIOR_GOOD = .50
HOSPITAL_EXCEPTION_SHARE = .45
ACCURACY = .90
FEE = .12


class Candidate(Economy):
    """A plant release has the same source signature in both recipient regimes."""

    def __init__(self, world, hospital_gain):
        super().__init__(world)
        self.hospital_gain = hospital_gain

    def skill(self, period, source, scope):
        q = super().skill(period, source, scope).copy()
        if period == 1 and source == 1:
            q[3] = Q[3] - DECAY[3] + self.hospital_gain
        return q


def margins(world):
    values = []
    for gain in (0., .22, -.27):
        candidate = Candidate(world, gain)
        values.append(candidate.operating(1, ZERO, 1).profit)
        candidate.clear()
    closed, good, bad = values
    return np.array([good - closed, bad - closed])


def diagnostic_value(delta, prior, accuracy):
    """Expected value gained when the sampled family can identify the latent sign."""
    weights = np.array([prior, 1-prior]) * delta
    signal = np.array([accuracy, 1-accuracy])
    situation_value = max(0., weights.sum())
    expected_value = max(0., weights @ signal) + max(0., weights @ (1-signal))
    return max(0., expected_value - situation_value)


def archive_share(relative_retention):
    f = HOSPITAL_EXCEPTION_SHARE
    return f * relative_retention / (1-f + f*relative_retention)


def run():
    deltas = np.array([margins(draw(seed)) for seed in EVALUATION])
    potential = np.array([diagnostic_value(d, PRIOR_GOOD, ACCURACY) for d in deltas])
    result = {}
    for name, odds in (("exceptions_underretained",.1),("uniform",1.),("exceptions_enriched",4.)):
        fractions = {"supplier":0., "recipient_archive":archive_share(odds),
                     "recipient_roster":HOSPITAL_EXCEPTION_SHARE}
        channels = {name:potential*rate for name,rate in fractions.items()}
        result[name] = dict(exception_fraction=fractions, by_source={key:{
            "gross_wtp":difference(gross), "net_if_always_bought":difference(gross-FEE),
            "optimal_buy_share":float(np.mean(gross>FEE)),
            "net_if_optional":difference(np.maximum(gross-FEE,0.))}
            for key,gross in channels.items()},
            roster_minus_archive_equal_price=difference(channels["recipient_roster"]-channels["recipient_archive"]))
    return dict(evaluation=[EVALUATION.start,EVALUATION.stop-1], prior_good=PRIOR_GOOD,
                category_share=HOSPITAL_EXCEPTION_SHARE, conditional_test_accuracy=ACCURACY,
                cost_per_sample=FEE,
                open_minus_closed={name:difference(deltas[:,i]) for i,name in enumerate(("favorable","adverse"))},
                results=result)


if __name__ == "__main__":
    Path(__file__).with_name("audit_results.json").write_text(json.dumps(run(),indent=2)+"\n")
