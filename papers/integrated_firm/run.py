#!/usr/bin/env python3
"""Reproduce the integrated finite economy; standard library, CPU only."""
import argparse
import json
from dataclasses import asdict
from core import Config, State, Firm
from verify import replay, run as verify
from competition import run as compete

def result(h,c,s):
    f=Firm(c);v=f.value(s,h);path,end=f.distribution(s,h)
    out={'horizon':h,'parameters':asdict(c),'initial':asdict(s),'terminal_wealth':v,
         'net_cash_generation':end['expected_cash']-s.cash,
         'terminal_salvage':end['expected_salvage'],
         'first_action':asdict(f.policy[s,h]),'expected_path':path,
         'terminal':end,'verification':replay(f,s,h),'stats':f.stats}
    f.value.cache_clear();f.last_choice.cache_clear();f.productions.cache_clear();f.researches.cache_clear()
    return out

def save(path,value):
    with open(path,'w') as out:json.dump(value,out,indent=2);out.write('\n')

def standard():
    cases=[
       ('baseline_t2',2,Config(),State()),
       ('baseline_t3',3,Config(),State()),
       ('baseline_t4',4,Config(),State()),
       ('no_learning_t4',4,Config(allow_training=False,allow_procedure=False,diagnostic_collection=False),State()),
       ('financed_t4',4,Config(),State(cash=18)),
       ('complementary_stack_t4',4,Config(),State(cash=18,physical_model=1,digital_model=1)),
       ('hardware_entry_t3',3,Config(demand_intercepts=((18,8),(18,8)),market_persistence=1),State(arm=0,physical_model=2,digital_model=1,internal_lab=0,cash=18)),
       ('hardware_fixed_assets_t3',3,Config(demand_intercepts=((18,8),(18,8)),market_persistence=1,allow_build=False),State(arm=0,physical_model=2,digital_model=1,internal_lab=0,cash=18)),
       ('evidence_to_training_t4',4,Config(research_human=0,training_tokens=1,procedure_tokens=1),State(cash=18,physical_data=0,digital_data=0)),
       ('evidence_no_retention_t4',4,Config(research_human=0,training_tokens=1,procedure_tokens=1,rights_mask=0),State(cash=18,physical_data=0,digital_data=0)),
    ]
    outcomes={}
    for name,h,c,s in cases:
        outcomes[name]=result(h,c,s)
        print(name,outcomes[name]['net_cash_generation'],outcomes[name]['first_action']['research']['name'],outcomes[name]['terminal'],flush=True)
        save('integrated_results.json',outcomes)
    save('verification_results.json',verify())
    save('competition_results.json',compete())
    from cohorts import run as cohorts
    save('cohort_results.json',cohorts())
    from verify_cohorts import run_checks
    save('cohort_verification.json',run_checks())
    from margins import run as margins
    save('marginal_results.json',margins())

if __name__=='__main__':
    p=argparse.ArgumentParser()
    p.add_argument('--suite',choices=['standard','cohorts'],default='standard')
    args=p.parse_args()
    if args.suite=='standard':standard()
    else:
        from cohorts import run as cohorts
        from verify_cohorts import run_checks
        save('cohort_results.json',cohorts())
        save('cohort_verification.json',run_checks())

