#!/usr/bin/env python3
"""Export shared-workforce worlds or replay their complete opening inputs."""
import argparse
import json
from pathlib import Path
import sys
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from model.shared_workforce import workforce_artifact, replay_workforce_case


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--case', type=Path); p.add_argument('--output', type=Path); p.add_argument('--check', action='store_true')
    a = p.parse_args(); result = replay_workforce_case(json.loads(a.case.read_text())) if a.case else workforce_artifact()
    path = a.output or ROOT / 'model/results/shared_workforce.json'; body = json.dumps(result, indent=2) + '\n'
    if a.check:
        if not path.exists() or path.read_text() != body: raise SystemExit('Shared workforce export differs; regenerate')
        print('Shared workforce export matches current source and complete inputs')
    else:
        path.parent.mkdir(parents=True, exist_ok=True); path.write_text(body); print(path)


if __name__ == '__main__': main()
