"""Pairwise capital complementarity at the same state, separate from correlated returns."""
import json
from dataclasses import replace
from itertools import combinations
from pathlib import Path

import numpy as np

from model import FIRST_COST, NODES, OPTIONS, ZERO, Economy, draw
from study import EVALUATION, describe


def run():
    joint, pairs = [], {}
    relaxations = {key:[] for key in ("baseline","ample_compute","ample_role_hours","both")}
    for seed in EVALUATION:
        world = draw(seed)
        e = Economy(world)
        base = e.policy(ZERO)
        single = [e.policy(k) for k in OPTIONS[1:]]
        joint.append([(p.value-base.value)/cost for p,cost in zip(single,FIRST_COST)])
        for i,j in combinations(range(len(NODES)),2):
            k = tuple(np.add(OPTIONS[i+1],OPTIONS[j+1]))
            both = e.policy(k)
            # A controlled two-block installation tests a technology interaction.
            # The primary adoption model still has one installation slot per period.
            cross = both.value-single[i].value-single[j].value+base.value
            spot = both.first.profit-single[i].first.profit-single[j].first.profit+base.first.profit
            pairs.setdefault(f"{NODES[i]}+{NODES[j]}",[]).append((spot,cross))
        plant,warehouse = OPTIONS[2:4]
        paired = tuple(np.add(plant,warehouse))
        for key,crosses in relaxations.items():
            alternative = replace(world,
                compute=world.compute*(10 if key in ("ample_compute","both") else 1),
                labor=world.labor*(10 if key in ("ample_role_hours","both") else 1))
            control = Economy(alternative)
            empty,up,down,both = [control.operating(0,k).profit for k in (ZERO,plant,warehouse,paired)]
            crosses.append(both-up-down+empty)
            control.clear()
        e.clear()
    def summary(data):
        a = np.asarray(data)
        return dict(spot=describe(a[:,0]),two_date=describe(a[:,1]),
                    share_positive=float(np.mean(a[:,1]>1e-7)),
                    share_negative=float(np.mean(a[:,1]<-1e-7)))
    return dict(evaluation=[EVALUATION.start,EVALUATION.stop-1],node_order=NODES,
                covariance_of_value_cost_ratios=np.cov(np.array(joint).T).round(5).tolist(),
                plant_warehouse_spot_resource_checks={k:describe(v) for k,v in relaxations.items()},
                same_world_block_interactions={k:summary(v) for k,v in pairs.items()})


if __name__ == "__main__":
    Path(__file__).with_name("interaction_results.json").write_text(json.dumps(run(),indent=2)+"\n")
