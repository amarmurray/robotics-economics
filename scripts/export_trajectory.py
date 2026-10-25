#!/usr/bin/env python3
"""Six synthetic annual counterfactuals, all calculated by the common engine."""
import argparse
import hashlib
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from model.engine import run_scenario
from model.trajectories import SCHEMA


def comparison():
    human = [.15, .20, .25, .30, .35]
    specs = {
        "constant_reference": {},
        "improving_human": {"digital_efficiency": human},
        "cheaper_robot_service": {"digital_cost_usd": [1500, 1200, 900, 600, 300]},
        "worsening_coordination": {"coordination": [.15, .10, 0, -.10, -.20]},
        "joint_paths": {"digital_efficiency": human, "coordination": [.15, .20, .10, .25, .15],
                        "digital_cost_usd": [1500, 1200, 900, 600, 300]},
        "conventional_combined": {"digital_efficiency": human, "coordination": [0]*5,
                                  "digital_cost_usd": [0]*5},
    }
    results = {}
    for name, channels in specs.items():
        paths = {"schema_version": SCHEMA, "base_year": 2026,
                 "epistemic_status": "synthetic_assumption", **channels}
        results[name] = run_scenario({"years": 5, "learning_transfer": 0}, digital_paths=paths)
    return {
        "schema_version": "annual-digital-comparison/0.1", "status": "synthetic_illustration",
        "empirical_aggregate_inclusion": False,
        "cell_id": "CELL-M08-3pl-tote-US-2025",
        "purpose": "Isolate human-baseline, signed coordination and robot-service cost changes, with learning disabled; compare added orchestration with the already priced conventional stack.",
        "source_hashes": {**results["constant_reference"]["model_source_hashes"],
                          "model/assumptions.json": hashlib.sha256((ROOT/"model/assumptions.json").read_bytes()).hexdigest(),
                          "scripts/export_trajectory.py": hashlib.sha256(Path(__file__).read_bytes()).hexdigest()},
        "limitations": ["No coefficient is empirically calibrated.",
                        "Conventional combined means the same digital human baseline and required robot control, with no additional coordination or robot-service bundle; not a measured competing scheduler.",
                        "One-site reference costs are not realized fleet savings. Separate monthly entrant, initial-year cash and treasury examples are not jointly funded by this experiment.",
                        "Annual acquisition screening, free compatible software updates and supported-hours learning exposure retain the legacy limitations documented in METHODS.md."],
        "results": results,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=ROOT/"model/results/annual_digital_comparison.json")
    args = parser.parse_args()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(comparison(), indent=2, sort_keys=True, allow_nan=False)+"\n")
    print(f"Exported six annual counterfactuals to {args.output}")


if __name__ == "__main__":
    main()
