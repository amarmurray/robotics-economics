#!/usr/bin/env python3
"""Export dated financing cases or replay a complete saved financed case."""
import argparse
import json
from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from model.enterprise_finance import finance_artifact, replay_financed_enterprise


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--case',type=Path)
    parser.add_argument('--output',type=Path)
    parser.add_argument('--check',action='store_true')
    args=parser.parse_args()
    value=replay_financed_enterprise(json.loads(args.case.read_text())) if args.case else finance_artifact()
    path=args.output or ROOT/'model/results/enterprise_finance.json'
    text=json.dumps(value,indent=2)+'\n'
    if args.check:
        if not path.exists() or path.read_text()!=text:raise SystemExit('Financing export differs; regenerate')
        print('Financing export matches current source and inputs')
    else:
        path.parent.mkdir(parents=True,exist_ok=True);path.write_text(text);print(path)


if __name__=='__main__':main()
