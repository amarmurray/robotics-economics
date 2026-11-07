#!/usr/bin/env python3
"""Export bounded workcell witnesses or replay complete saved inputs."""
import argparse,json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT))
from model.automotive_workcell import workcell_artifact,replay_workcell
if __name__=='__main__':
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--case',type=Path);p.add_argument('--output',type=Path);p.add_argument('--check',action='store_true');a=p.parse_args()
 value=replay_workcell(json.loads(a.case.read_text())) if a.case else workcell_artifact();body=json.dumps(value,indent=2)+'\n';path=a.output or ROOT/'model/results/automotive_workcell.json'
 if a.check:
  if not path.exists() or path.read_text()!=body:raise SystemExit('Workcell export differs; regenerate')
  print('Workcell export matches current source and complete inputs')
 else:path.parent.mkdir(parents=True,exist_ok=True);path.write_text(body);print(path)
