#!/usr/bin/env python3
"""Export/replay one paid review and actual whole-service history."""
import argparse,json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT))
from model.paid_development import paid_development_artifact,replay_paid_development
p=argparse.ArgumentParser(description=__doc__);p.add_argument('--case',type=Path);p.add_argument('--output',type=Path);p.add_argument('--check',action='store_true');a=p.parse_args()
r=replay_paid_development(json.loads(a.case.read_text())) if a.case else paid_development_artifact();path=a.output or ROOT/'model/results/paid_development.json';body=json.dumps(r,indent=2)+'\n'
if a.check:
 if not path.exists() or path.read_text()!=body:raise SystemExit('Paid-development export differs; regenerate')
 print('Paid-development export matches complete inputs and current code')
else:path.write_text(body);print(path)
