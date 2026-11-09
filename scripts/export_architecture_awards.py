#!/usr/bin/env python3
"""Export or replay one intelligence-role and actual customer-award execution."""
import argparse,json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT))
from model.architecture_awards import architecture_awards_artifact,replay_architecture_awards
p=argparse.ArgumentParser(description=__doc__);p.add_argument('--case',type=Path);p.add_argument('--output',type=Path);p.add_argument('--check',action='store_true');a=p.parse_args()
r=replay_architecture_awards(json.loads(a.case.read_text())) if a.case else architecture_awards_artifact();path=a.output or ROOT/'model/results/architecture_awards.json';body=json.dumps(r,indent=2)+'\n'
if a.check:
 if not path.exists() or path.read_text()!=body:raise SystemExit('Architecture-award export differs; regenerate')
 print('Architecture-award export matches complete inputs and current code')
else:path.write_text(body);print(path)
