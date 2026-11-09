#!/usr/bin/env python3
"""Export exact derived inspection comparisons or replay complete pair inputs."""
from pathlib import Path
import argparse,json,sys
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT))
from model.inspection_price_bounds import price_bounds_artifact,replay_price_bounds
p=argparse.ArgumentParser(description=__doc__);p.add_argument('--case',type=Path);p.add_argument('--output',type=Path);p.add_argument('--check',action='store_true');a=p.parse_args();r=replay_price_bounds(json.loads(a.case.read_text()))if a.case else price_bounds_artifact();path=a.output or ROOT/'model/results/inspection_price_bounds.json';body=json.dumps(r,indent=2)+'\n'
if a.check:
 if not path.exists()or path.read_text()!=body:raise SystemExit('Inspection price-bound export differs; regenerate')
 print('Inspection price-bound export matches complete inputs and current code')
else:path.write_text(body);print(path)
