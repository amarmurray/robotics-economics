#!/usr/bin/env python3
"""Export/replay one reviewed-release and retained-service history."""
import argparse,json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT))
from model.release_continuity import release_continuity_artifact,replay_release_continuity
p=argparse.ArgumentParser(description=__doc__);p.add_argument('--case',type=Path);p.add_argument('--output',type=Path);p.add_argument('--check',action='store_true');a=p.parse_args()
r=replay_release_continuity(json.loads(a.case.read_text())) if a.case else release_continuity_artifact();path=a.output or ROOT/'model/results/release_continuity.json';body=json.dumps(r,indent=2)+'\n'
if a.check:
 if not path.exists() or path.read_text()!=body:raise SystemExit('Release-continuity export differs; regenerate')
 print('Release-continuity export matches complete inputs and current code')
else:path.write_text(body);print(path)
