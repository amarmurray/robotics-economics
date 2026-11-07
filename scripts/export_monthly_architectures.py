#!/usr/bin/env python3
"""Export funded monthly intelligence roles or replay one complete saved case."""
import argparse
import json
from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from model.monthly_architectures import architecture_execution_artifact,replay_architecture_execution


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--case',type=Path);p.add_argument('--output',type=Path);p.add_argument('--check',action='store_true')
    args=p.parse_args();value=replay_architecture_execution(json.loads(args.case.read_text())) if args.case else architecture_execution_artifact()
    path=args.output or ROOT/'model/results/monthly_architectures.json';body=json.dumps(value,indent=2)+'\n'
    if args.check:
        if not path.exists() or path.read_text()!=body:raise SystemExit('Monthly architecture export differs; regenerate')
        print('Monthly architecture export matches current source and complete inputs')
    else:
        path.parent.mkdir(parents=True,exist_ok=True);path.write_text(body);print(path)


if __name__=='__main__':main()
