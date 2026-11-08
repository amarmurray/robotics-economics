#!/usr/bin/env python3
"""Export finite support/expansion worlds or recompute complete opening inputs."""
import argparse
import json
from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from model.support_expansion import expansion_artifact,replay_expansion


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--case',type=Path);p.add_argument('--output',type=Path);p.add_argument('--check',action='store_true')
    a=p.parse_args();value=replay_expansion(json.loads(a.case.read_text())) if a.case else expansion_artifact()
    path=a.output or ROOT/'model/results/support_expansion.json';body=json.dumps(value,indent=2)+'\n'
    if a.check:
        if not path.exists() or path.read_text()!=body:raise SystemExit('Support-expansion export differs; regenerate')
        print('Support-expansion export matches current source and full inputs')
    else:
        path.parent.mkdir(parents=True,exist_ok=True);path.write_text(body);print(path)


if __name__=='__main__':main()
