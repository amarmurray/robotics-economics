#!/usr/bin/env python3
"""Export exact conventional service-window witnesses or replay complete inputs."""
import argparse
import json
from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from model.conventional_coordination import coordination_artifact,replay_coordination


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--case',type=Path);p.add_argument('--output',type=Path);p.add_argument('--check',action='store_true')
    args=p.parse_args();value=replay_coordination(json.loads(args.case.read_text())) if args.case else coordination_artifact()
    path=args.output or ROOT/'model/results/conventional_coordination.json';body=json.dumps(value,indent=2)+'\n'
    if args.check:
        if not path.exists() or path.read_text()!=body:raise SystemExit('Conventional coordination export differs; regenerate')
        print('Conventional coordination export matches current source and complete inputs')
    else:
        path.parent.mkdir(parents=True,exist_ok=True);path.write_text(body);print(path)


if __name__=='__main__':main()
