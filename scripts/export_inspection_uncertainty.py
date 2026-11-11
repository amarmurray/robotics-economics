#!/usr/bin/env python3
"""Export or replay finite inspection uncertainty and evidence partitions."""
import argparse
import json
import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from model.inspection_uncertainty import artifact, replay, RESULT

if __name__ == '__main__':
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--case', type=Path)
    p.add_argument('--output', type=Path)
    p.add_argument('--check', action='store_true')
    a = p.parse_args()
    result = replay(json.loads(a.case.read_text())) if a.case else artifact()
    path = a.output or ROOT / RESULT
    body = json.dumps(result, indent=2, allow_nan=False) + '\n'
    if a.check:
        if not path.exists() or path.read_text() != body:
            raise SystemExit('Inspection uncertainty export differs; regenerate')
        print('Inspection uncertainty export matches complete inputs and current code')
    else:
        path.write_text(body)
        print(path)
