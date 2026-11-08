#!/usr/bin/env python3
"""Export annual-resource renewal worlds or replay complete opening inputs."""
import argparse
import json
from pathlib import Path
import sys
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from model.annual_commitments import annual_artifact, replay_annual_case


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--case', type=Path); parser.add_argument('--output', type=Path)
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    result = replay_annual_case(json.loads(args.case.read_text())) if args.case else annual_artifact()
    path = args.output or ROOT / 'model/results/annual_commitments.json'
    body = json.dumps(result, indent=2) + '\n'
    if args.check:
        if not path.exists() or path.read_text() != body: raise SystemExit('Annual commitment export differs; regenerate')
        print('Annual commitment export matches current source and full inputs')
    else:
        path.parent.mkdir(parents=True, exist_ok=True); path.write_text(body); print(path)


if __name__ == '__main__': main()
