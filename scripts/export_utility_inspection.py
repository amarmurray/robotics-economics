#!/usr/bin/env python3
"""Export inspection witnesses or replay complete saved inputs."""
import argparse,json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT))
from model.utility_inspection import inspection_artifact,replay_inspection
if __name__=='__main__':
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--case',type=Path);p.add_argument('--output',type=Path);p.add_argument('--check',action='store_true');a=p.parse_args()
 value=replay_inspection(json.loads(a.case.read_text())) if a.case else inspection_artifact();body=json.dumps(value,indent=2)+'\n';path=a.output or ROOT/'model/results/utility_inspection.json'
 if a.check:
  if not path.exists() or path.read_text()!=body:raise SystemExit('Inspection export differs; regenerate')
  print('Inspection export matches current source and complete inputs')
 else:path.parent.mkdir(parents=True,exist_ok=True);path.write_text(body);print(path)
