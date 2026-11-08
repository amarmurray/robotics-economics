#!/usr/bin/env python3
"""Export architecture/resource worlds or replay their complete opening inputs."""
import argparse
import json
from pathlib import Path
import sys
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from model.architecture_resources import resource_architecture_artifact, replay_resource_architecture_case


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--case', type=Path); p.add_argument('--output', type=Path); p.add_argument('--check', action='store_true')
    a = p.parse_args(); result = replay_resource_architecture_case(json.loads(a.case.read_text())) if a.case else resource_architecture_artifact()
    path = a.output or ROOT / 'model/results/architecture_resources.json'; body = json.dumps(result, indent=2) + '\n'
    if a.check:
        if not path.exists() or path.read_text() != body: raise SystemExit('Architecture resource export differs; regenerate')
        print('Architecture resource export matches current source and complete inputs')
    else:
        path.parent.mkdir(parents=True, exist_ok=True); path.write_text(body); print(path)


if __name__ == '__main__': main()
