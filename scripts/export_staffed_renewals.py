#!/usr/bin/env python3
"""Export or replay one paid-crew and customer-renewal execution."""
import argparse,json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT))
from model.staffed_renewals import staffed_renewals_artifact,replay_staffed_renewals
p=argparse.ArgumentParser(description=__doc__);p.add_argument('--case',type=Path);p.add_argument('--output',type=Path);p.add_argument('--check',action='store_true');a=p.parse_args()
r=replay_staffed_renewals(json.loads(a.case.read_text())) if a.case else staffed_renewals_artifact();path=a.output or ROOT/'model/results/staffed_renewals.json';body=json.dumps(r,indent=2)+'\n'
if a.check:
 if not path.exists() or path.read_text()!=body:raise SystemExit('Staffed-renewals export differs; regenerate')
 print('Staffed-renewals export matches complete inputs and current code')
else:path.write_text(body);print(path)
