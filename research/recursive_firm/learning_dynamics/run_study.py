"""Regenerate the research results from the published cells and the specified random seeds."""
import argparse
import json
from pathlib import Path

from fleet import fleet_study
from scaling import study


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("part", choices=("all","fleet","scaling"), default="all", nargs="?")
    requested = parser.parse_args().part
    for name, run in (("scaling",study), ("fleet",fleet_study)):
        if requested in ("all",name):
            result = run()
            path = Path(__file__).with_name(name+"_results.json")
            path.write_text(json.dumps(result,indent=2)+"\n")
