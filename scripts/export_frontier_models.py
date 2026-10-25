#!/usr/bin/env python3
"""Validate model-layer evidence links and export source-disclosure arithmetic."""
import argparse
import json
from pathlib import Path
import sys
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from model.frontier_models import frontier_model_summary


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    result = frontier_model_summary()
    text = json.dumps(result, indent=2, sort_keys=True, ensure_ascii=False, allow_nan=False)+"\n"
    target = ROOT/"model/results/frontier_model_summary.json"
    if args.check:
        if target.read_text() != text:
            raise SystemExit("Stale frontier-model summary")
    else:
        target.write_text(text)
    print(json.dumps({"status": "pass", "actors": result["coverage"]["mapped_actors"],
                      "dossiers": result["coverage"]["contrasting_dossiers"],
                      "transaction_checks": result["transaction"]["checks"]}))


if __name__ == "__main__":
    main()
