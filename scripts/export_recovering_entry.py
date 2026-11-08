#!/usr/bin/env python3
"""Export/replay funded robot recovery on company entry and customer renewal."""
import argparse,json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT))
from model.recovering_entry import recovering_entry_artifact,replay_recovering_entry
p=argparse.ArgumentParser(description=__doc__);p.add_argument('--case',type=Path);p.add_argument('--output',type=Path);p.add_argument('--check',action='store_true');a=p.parse_args()
r=replay_recovering_entry(json.loads(a.case.read_text())) if a.case else recovering_entry_artifact();path=a.output or ROOT/'model/results/recovering_entry.json';body=json.dumps(r,indent=2)+'\n'
if a.check:
 if not path.exists() or path.read_text()!=body:raise SystemExit('Recovering-entry export differs; regenerate')
 print('Recovering-entry export matches complete inputs and current code')
else:path.write_text(body);print(path)
