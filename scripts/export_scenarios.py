#!/usr/bin/env python3
"""Regenerate deterministic JSON/CSV report inputs from the authoritative engine."""
import argparse
import csv
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from model.engine import catalog, run_scenario
from model.evidence import economic_atlas_summary


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output",type=Path,default=ROOT/"model/results")
    parser.add_argument("--scenario",type=Path,help="Reload an exported scenario JSON containing parameters or overrides")
    args = parser.parse_args()
    args.output.mkdir(parents=True,exist_ok=True)
    (args.output/"observed_atlas_summary.json").write_text(json.dumps(economic_atlas_summary(),indent=2,sort_keys=True)+"\n")
    specs = [(key,{}) for key in catalog()["presets"]]
    if args.scenario:
        saved = json.loads(args.scenario.read_text())
        specs = [(saved.get("preset","reference"),saved.get("parameters",saved.get("overrides",{})))]
    summary = []
    for preset, overrides in specs:
        result = run_scenario(overrides,preset)
        (args.output/f"{preset}.json").write_text(json.dumps(result,indent=2,sort_keys=True,allow_nan=False)+"\n")
        final = result["fleet"]["years"][-1]
        summary.append({"preset":preset,"status":"synthetic_illustration","scenario_hash":result["scenario_hash"],"year":final["year"],
            "active_stock_expected_units":final["active_stock"],"baseline_equivalent_hours":final["accepted_baseline_equivalent_hours"],
            "cumulative_baseline_equivalent_hours":sum(y["accepted_baseline_equivalent_hours"] for y in result["fleet"]["years"]),
            "newco_peak_funding_usd":result["newco"]["peak_funding_required_usd"],"newco_funding_gap_usd":result["newco"]["funding_gap_usd"]})
        for table in ("components","production"):
            rows=result["fleet"][table]
            with (args.output/f"{preset}_{table}.csv").open("w",newline="") as f:
                w=csv.DictWriter(f,lineterminator="\n",fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
        with (args.output/f"{preset}_joint.csv").open("w",newline="") as f:
            w=csv.DictWriter(f,lineterminator="\n",fieldnames=list(result["joint"][0]));w.writeheader();w.writerows(result["joint"])
    with (args.output/"scenario_summary.csv").open("w",newline="") as f:
        w=csv.DictWriter(f,lineterminator="\n",fieldnames=list(summary[0]));w.writeheader();w.writerows(summary)
    print(f"Exported {len(summary)} scenarios to {args.output}")


if __name__=="__main__":
    main()
