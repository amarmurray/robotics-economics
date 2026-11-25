"""Compare responses to the same standard across matched supply-chain architectures."""
import json
from pathlib import Path

from model import Economy, draw
from study import EVALUATION, describe, difference, transmission


def run():
    records = {k:[] for k in ("direct","cross_dock")}
    for seed in EVALUATION:
        world = draw(seed)
        for topology, items in records.items():
            base = Economy(world, topology=topology)
            changed = Economy(world, "standardization", topology)
            items.append(transmission(base, changed, "standardization"))
            base.clear()
            changed.clear()
    variables = ("final","gross","capital_revaluation","upstream_falls_while_hospital_expands","net")
    paired = []
    for direct, dock in zip(records["direct"], records["cross_dock"]):
        paired.append(dock["capital_revaluation"][2]-direct["capital_revaluation"][2])
    return dict(evaluation=[EVALUATION.start,EVALUATION.stop-1],
                topology={k:{v:describe([r[v] for r in rows]) for v in variables}
                          for k,rows in records.items()},
                change_in_fulfillment_revaluation_paired=difference(paired))


if __name__ == "__main__":
    Path(__file__).with_name("route_results.json").write_text(json.dumps(run(),indent=2)+"\n")
