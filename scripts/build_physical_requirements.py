#!/usr/bin/env python3
"""Build the observed crosswalk from the explicitly preserved BLS source rows."""
import argparse
import json
from pathlib import Path
import sys
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from model.physical_requirements import build_package, physical_requirements_summary, PACKAGE


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    content = json.dumps(build_package(), indent=2, ensure_ascii=False, allow_nan=False)+"\n"
    target = ROOT/PACKAGE
    if args.check:
        if target.read_text() != content:
            raise SystemExit("Saved crosswalk differs from source-row transformation")
    else:
        target.write_text(content)
    summary = physical_requirements_summary()
    summary_text = json.dumps(summary, indent=2, sort_keys=True, ensure_ascii=False, allow_nan=False)+"\n"
    output = ROOT/"model/results/physical_requirements_summary.json"
    if args.check:
        if output.read_text() != summary_text:
            raise SystemExit("Saved physical-requirements summary differs")
    else:
        output.write_text(summary_text)
    print(json.dumps({k: summary[k] for k in ("published_ors_rows", "unpublished_selected_rows", "exact_code_matches")}))


if __name__ == "__main__":
    main()
