"""Feed endogenous adaptation costs into the preserved expansion kernel.

No source evaluation is used to calibrate these synthetic examples.
Costs are conservatively rounded UP to 1/100 of a normalized cash unit.
"""
from dataclasses import replace
from decimal import Decimal, ROUND_CEILING
from fractions import Fraction as F
from pathlib import Path
import json
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'takeover_2026_11_17'))
from expansion import A, B_HIGH, B_LOW, Technology, optimize, jsonable
from qualification import PROFILES, qualify


def rounded_cost(value: float) -> F:
    return F(Decimal(str(value)).quantize(Decimal('.01'),rounding=ROUND_CEILING))


def comparison(initial_cash: int = 30, weak_demand: bool = False,
               equal_profiles: bool = False, verification: float = 2.0):
    rows={}
    # Cash is preserved from the first model's derived source-service accounts.
    for name,cash in (('score_rich',F(8)),('bottleneck_rich',F(6))):
        profile=PROFILES['score_rich' if equal_profiles else name]
        q=qualify(profile,.02,verification)
        if not q.feasible:
            raise ValueError('These declared source profiles must be finitely qualifiable')
        cost=rounded_cost(q.total_cost)
        tech=replace(Technology(),qualification_base=cost,qualification_floor=cost,transfer=F(0))
        d=optimize(F(initial_cash)+cash,F(0),A,B_LOW if weak_demand else B_HIGH,tech)
        rows[name]=dict(current_cash=cash,qualification_cost=cost,decision=d,
                        added_value=cash+d.gain)
    return dict(initial_cash=initial_cash,weak_demand=weak_demand,
                equal_profiles=equal_profiles,verification=verification,
                winner=max(rows,key=lambda k:rows[k]['added_value']),paths=rows)


def experiments():
    return jsonable({
        'base':comparison(),
        'weak_demand':comparison(weak_demand=True),
        'no_profile_difference':comparison(equal_profiles=True),
        'scarce_cash':comparison(initial_cash=4),
        'high_verification_cost':comparison(verification=20),
    })


if __name__=='__main__':
    path=Path(__file__).with_name('bridge_results.json')
    path.write_text(json.dumps(experiments(),indent=2,sort_keys=True)+'\n')
    print(path)
