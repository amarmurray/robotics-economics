#!/usr/bin/env python3
"""Export or replay qualified supply, paid staffing and actual customer awards."""
import argparse,json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT))
from model.qualified_staffing import qualified_staffing_artifact,replay_qualified_staffing
p=argparse.ArgumentParser(description=__doc__);p.add_argument('--case',type=Path);p.add_argument('--output',type=Path);p.add_argument('--check',action='store_true');a=p.parse_args()
r=replay_qualified_staffing(json.loads(a.case.read_text())) if a.case else qualified_staffing_artifact();path=a.output or ROOT/'model/results/qualified_staffing.json';body=json.dumps(r,indent=2)+'\n'
if a.check:
 if not path.exists() or path.read_text()!=body:raise SystemExit('Qualified staffing export differs; regenerate')
 print('Qualified staffing export matches complete inputs and current code')
else:path.write_text(body);print(path)
