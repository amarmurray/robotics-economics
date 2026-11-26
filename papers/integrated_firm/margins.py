#!/usr/bin/env python3
"""Typed finite changes in accepted service and private value."""
import json
from dataclasses import replace,asdict
from core import Config,State,Firm

def run():
    f=Firm();s=State();h=3
    cases=[
       ('arm_added_to_no_robot',replace(s,arm=0),s,0),
       ('mobile_added',s,replace(s,mobile=1),0),
       ('physical_model_increment',s,replace(s,physical_model=1),0),
       ('digital_model_increment',s,replace(s,digital_model=1),0),
       ('procedure_increment',s,replace(s,procedure=1),0),
       ('reference_added',s,replace(s,reference=1),0),
       ('cash_increment',s,replace(s,cash=s.cash+1),1),
    ]
    result={'remaining_periods':h,'interpretation':'Reoptimized current accepted-service finite differences; private wealth includes principal and equipment salvage, both separately reported.','cases':{}}
    for name,lo,hi,principal in cases:
        vlo=f.value(lo,h);vhi=f.value(hi,h)
        a=f.policy[lo,h];b=f.policy[hi,h]
        _,endlo=f.distribution(lo,h);_,endhi=f.distribution(hi,h)
        result['cases'][name]={'low_state':asdict(lo),'high_state':asdict(hi),
              'physical_service_change':b.production.physical-a.production.physical,
              'digital_service_change':b.production.digital-a.production.digital,
              'private_terminal_wealth_change':vhi-vlo,
              'additional_initial_cash':principal,
              'terminal_salvage_change':endhi['expected_salvage']-endlo['expected_salvage'],
              'cash_generation_change':endhi['expected_cash']-hi.cash-(endlo['expected_cash']-lo.cash),
              'low_first_research':a.research.name,'high_first_research':b.research.name}
    return result

if __name__=='__main__':
    result=run()
    with open('marginal_results.json','w') as out:json.dump(result,out,indent=2);out.write('\n')
    print(json.dumps(result,indent=2))

