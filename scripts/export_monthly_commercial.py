#!/usr/bin/env python3
"""Reproduce fixed commercial witnesses or replay one exported case from inputs."""
import argparse
import json
from pathlib import Path
import sys
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from model.monthly_commercial import commercial_artifact, replay_case


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=ROOT/'model/results/monthly_commercial.json')
    parser.add_argument('--case', type=Path, help='Recompute one exported case from its saved opening inputs')
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    value = replay_case(json.loads(args.case.read_text())) if args.case else commercial_artifact()
    text = json.dumps(value, indent=2) + '\n'
    if args.check:
        if not args.output.exists() or args.output.read_text() != text:
            raise SystemExit('Monthly commercial export differs; regenerate with this script')
        print('Monthly commercial export matches current source and inputs')
    else:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text)
        print(args.output)


if __name__ == '__main__':
    main()
