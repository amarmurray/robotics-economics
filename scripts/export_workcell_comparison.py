#!/usr/bin/env python3
"""Export/check workcell comparison bounds or replay a complete pair."""
import argparse
import json
import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from model.workcell_comparison import artifact, replay, RESULT

if __name__ == '__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--case', type=Path);p.add_argument('--output', type=Path);p.add_argument('--check', action='store_true')
    a=p.parse_args();result=replay(json.loads(a.case.read_text())) if a.case else artifact()
    body=json.dumps(result,indent=2,allow_nan=False)+'\n';path=a.output or ROOT/RESULT
    if a.check:
        if not path.exists() or path.read_text()!=body:raise SystemExit('Workcell comparison differs; regenerate')
        print('Workcell comparison matches complete inputs and current code')
    else:path.write_text(body);print(path)
