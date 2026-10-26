#!/usr/bin/env python3
"""Reproduce shared-enterprise cases, a saved case, or the fixed-policy equity search."""
import argparse
import json
from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from model.monthly_enterprise import enterprise_artifact, enterprise_source_hashes, minimum_reference_bridge, replay_enterprise


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path)
    group=parser.add_mutually_exclusive_group()
    group.add_argument('--case',type=Path)
    group.add_argument('--bridge',action='store_true')
    parser.add_argument('--check',action='store_true')
    args=parser.parse_args()
    if args.case:value=replay_enterprise(json.loads(args.case.read_text()))
    elif args.bridge:value={**minimum_reference_bridge(),"source_sha256":enterprise_source_hashes()}
    else:value=enterprise_artifact()
    target=args.output or ROOT/'model/results'/('enterprise_funding_bridge.json' if args.bridge else 'shared_enterprise.json')
    text=json.dumps(value,indent=2)+'\n'
    if args.check:
        if not target.exists() or target.read_text()!=text:raise SystemExit('Shared-enterprise export differs; regenerate')
        print('Shared-enterprise export matches current source and inputs')
    else:
        target.parent.mkdir(parents=True,exist_ok=True);target.write_text(text);print(target)


if __name__=='__main__':main()
