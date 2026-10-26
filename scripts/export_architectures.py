#!/usr/bin/env python3
"""Common-engine conditional architectures and isolated sensitivity witnesses."""
import argparse
import hashlib
import json
from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from model.engine import run_architecture_comparison

CELL="CELL-M05-auto-assembly-US-2025"


def experiments():
    base=run_architecture_comparison(CELL,year=2030)
    specs={
        "reference":None,
        "higher_model_fee":{"common":{"model_fee_usd_year":7000}},
        "more_licensed_adaptation":{"profiles":{"licensed_independent":{"adaptation_engineering_hours":140}}},
        "more_licensed_support":{"profiles":{"licensed_independent":{"support_minutes_delta":10}}},
        "newco_setup_burden":{"common":{"customer_path":"newco","newco_setup_usd":20000}},
        "unqualified_license":{"profiles":{"licensed_independent":{"assume_compatible":False}}},
        "lean_open_adaptation":{"profiles":{"open_adapted":{"adaptation_engineering_hours":40,"model_maintenance_usd_year":500}}},
    }
    cases={name:base if changes is None else run_architecture_comparison(CELL,year=2030,architecture_overrides=changes) for name,changes in specs.items()}
    cases["improved_digital_human"]=run_architecture_comparison(CELL,{"digital_efficiency":.35},year=2030)
    return {"schema_version":"architecture-experiments/0.1","status":"synthetic_conditional_witnesses",
            "source_hashes":{**base["source_hashes"],"scripts/export_architectures.py":hashlib.sha256(Path(__file__).read_bytes()).hexdigest()},"cases":cases,
            "boundary":"Counterfactual alternatives, not simultaneous fleets or named vendor estimates. Source uncertainty is retained; no commercial qualification or company financing is established."}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--scenario",type=Path,help="Replay a saved architecture result")
    parser.add_argument("--output",type=Path,default=ROOT/"model/results/architecture_comparison.json")
    parser.add_argument("--experiments-output",type=Path)
    args=parser.parse_args()
    if args.scenario:
        saved=json.loads(args.scenario.read_text());scope=saved["comparison_scope"]
        result=run_architecture_comparison(scope["cell_id"],saved["parameters"],saved["preset"],saved.get("digital_paths"),scope["year"],saved["architecture_parameters"])
    else:result=run_architecture_comparison(CELL,year=2030)
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(result,indent=2,sort_keys=True,ensure_ascii=False,allow_nan=False)+"\n")
    if args.experiments_output:
        args.experiments_output.parent.mkdir(parents=True,exist_ok=True)
        args.experiments_output.write_text(json.dumps(experiments(),indent=2,sort_keys=True,ensure_ascii=False,allow_nan=False)+"\n")
    print(json.dumps({"output":str(args.output),"case_hash":result["case_hash"],"scope":result["comparison_scope"]}))


if __name__=="__main__":main()
