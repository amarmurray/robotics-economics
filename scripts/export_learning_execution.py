#!/usr/bin/env python3
"""Export learning/qualification worlds or replay complete saved inputs."""
import argparse,json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT))
from model.learning_execution import learning_artifact,replay_learning
if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--case',type=Path);p.add_argument('--output',type=Path);p.add_argument('--check',action='store_true');a=p.parse_args()
    value=replay_learning(json.loads(a.case.read_text())) if a.case else learning_artifact()
    body=json.dumps(value,indent=2)+'\n';path=a.output or ROOT/'model/results/learning_execution.json'
    if a.check:
        if not path.exists() or path.read_text()!=body:raise SystemExit('Learning execution export differs; regenerate')
        print('Learning execution export matches complete inputs and source')
    else:path.parent.mkdir(parents=True,exist_ok=True);path.write_text(body);print(path)
