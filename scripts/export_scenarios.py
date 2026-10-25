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
from model.packages import load_accepted_packages
from model.research_calculations import research_summary
from model.physical_requirements import physical_requirements_summary
from model.frontier_models import frontier_model_summary


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output",type=Path,default=ROOT/"model/results")
    parser.add_argument("--scenario",type=Path,help="Reload an exported scenario JSON containing parameters or overrides")
    args = parser.parse_args()
    args.output.mkdir(parents=True,exist_ok=True)
    accepted={p["path"] for p in load_accepted_packages(ROOT)["packages"]}
    atlas=economic_atlas_summary() if "data/market_evidence.json" in accepted else {"status":"not_available","reason":"Market evidence package has not been explicitly accepted."}
    research=research_summary() if {"data/field_support_denominators.json","data/coordination_reproducibility.json"}<=accepted else {"status":"not_available","reason":"Required research packages have not been explicitly accepted."}
    (args.output/"observed_atlas_summary.json").write_text(json.dumps(atlas,indent=2,sort_keys=True)+"\n")
    (args.output/"observed_research_summary.json").write_text(json.dumps(research,indent=2,sort_keys=True,allow_nan=False)+"\n")
    if "data/physical_requirements_crosswalk.json" in accepted:
        (args.output/"physical_requirements_summary.json").write_text(json.dumps(physical_requirements_summary(),indent=2,sort_keys=True,ensure_ascii=False,allow_nan=False)+"\n")
    if "data/frontier_model_economics.json" in accepted:
        (args.output/"frontier_model_summary.json").write_text(json.dumps(frontier_model_summary(),indent=2,sort_keys=True,ensure_ascii=False,allow_nan=False)+"\n")
    specs = [(key,{},None) for key in catalog()["presets"]]
    if args.scenario:
        saved = json.loads(args.scenario.read_text())
        specs = [(saved.get("preset","reference"),saved.get("parameters",saved.get("overrides",{})),saved.get("digital_paths"))]
    summary = []
    for preset, overrides, digital_paths in specs:
        result = run_scenario(overrides,preset,digital_paths=digital_paths)
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
        annual = [{"year": year["year"], "capability": year["capability"],
                   **year["effective_digital_parameters"], **row}
                  for year in result["joint_by_year"] for row in year["comparisons"]]
        with (args.output/f"{preset}_joint_by_year.csv").open("w",newline="") as f:
            w=csv.DictWriter(f,lineterminator="\n",fieldnames=list(annual[0]));w.writeheader();w.writerows(annual)
    with (args.output/"scenario_summary.csv").open("w",newline="") as f:
        w=csv.DictWriter(f,lineterminator="\n",fieldnames=list(summary[0]));w.writeheader();w.writerows(summary)
    print(f"Exported {len(summary)} scenarios to {args.output}")


if __name__=="__main__":
    main()
