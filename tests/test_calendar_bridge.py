"""Calendar/unit/cohort bridges must change funded execution without extra stock."""
from dataclasses import replace
from fractions import Fraction
import copy
import json
import random
import unittest

from model.calendar_bridge import (Bridge, WORK, bridge_artifact, bridge_case_inputs, bridge_context,
    bridge_witness_options, exact, replay_bridge, run_bridge_case, run_bridged_enterprise)
from model.engine import capability_at, operation
from model.enterprise_finance import FinancePlan
from model.monthly_enterprise import Market


def q(x):return Fraction(int(x['numerator']),int(x['denominator']))


def one_unit(months=1,cash=50_000_000):
    p,t,cs,e,f,b=bridge_case_inputs({'entrant_cash_cents':10_000_000,'loan_cents':0},
                                   {'start_month':1,'annual_overrides':{'capability_progress':0}})
    operators=tuple(replace(o,opening_installed=1 if o.operator_id=='incumbent' else 0,
                    requested_additions=0,demand_units_by_month=(1000,)*months) for o in p.operators)
    p=replace(p,months=months,operators=operators,starts=(),qualified_component_receipts=(0,)*months,
              commissioning_slots=(1,)*months,support_slots=(1,)*months,shipping_slots=(1,)*months)
    businesses=tuple(replace(x,overhead_cents_by_month=(0,)*months,human_capacity_by_month=(0,)*months,
        human_staff_cents_by_month=(0,)*months,price_cents_per_unit_by_month=(2000,)*months,
        receipt_lag_by_month=(1,)*months,active_from_month=0 if x.operator_id=='incumbent' else None,
        formation_cents=0,material_cents_per_delivered_unit=0) for x in e.businesses)
    e=replace(e,businesses=businesses,moves=(),equity=(),market=Market(WORK,'incumbent','end_buyers',500,0,0))
    t=replace(t,accounts=tuple(replace(a,opening_cash_cents=cash) if a.actor_id=='incumbent' else a for a in t.accounts))
    return p,t,cs,e,FinancePlan(),b


class CalendarBridgeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.artifact=bridge_artifact();cls.cases=cls.artifact['cases']

    def test_calendar_levels_change_at_year_boundary_without_interpolation(self):
        r=self.cases['calendar_improving']['calendar_bridge'];months=r['months']
        self.assertEqual([(x['calendar_year'],x['calendar_month']) for x in months],
                         [(2026,m) for m in range(7,13)]+[(2027,1),(2027,2)])
        self.assertEqual([x['effective_parameters']['digital_efficiency'] for x in months],[.15]*6+[.35]*2)
        self.assertEqual([x['whole_month_count'] for x in r['calendar_years']],[6,2])
        self.assertTrue(all(x['annualized_service'] is None for x in r['calendar_years']))

    def test_exact_new_unit_does_not_convert_the_old_bundle(self):
        r=self.cases['C11_robot_digital'];u=r['calendar_bridge']['unit_contract']
        self.assertEqual(u['monthly_units_per_annual_unit'],{'numerator':'1','denominator':'1'})
        self.assertIsNone(u['original_floor_bundle_conversion'])
        self.assertEqual(r['plan']['system']['work_id'],WORK)
        args=list(bridge_case_inputs());args[0]=replace(args[0],system=replace(args[0].system,work_id='WORK-FLOOR-BUNDLE-SYN-02'))
        args[3]=replace(args[3],market=replace(args[3].market,work_id='WORK-FLOOR-BUNDLE-SYN-02'))
        with self.assertRaisesRegex(ValueError,'No inferred conversion'):run_bridged_enterprise(*args)

    def test_twelve_full_months_reproduce_annual_supported_robot_output(self):
        args=one_unit(months=12);r=run_bridged_enterprise(*args)
        _,p,_,cell,system,_=bridge_context(args[-1],12)
        annual=exact(operation(cell,system,p,capability_at(p,0),True)['accepted_units'])
        delivered=sum((q(m['total_delivered_units']) for m in r['enterprise']['months']),Fraction())
        self.assertEqual(delivered,annual)
        self.assertEqual(r['calendar_bridge']['calendar_years'][0]['supported_robot_year_equivalents'],{'numerator':'1','denominator':'1'})
        self.assertEqual(len(r['units']),1)

    def test_new_cohort_ramp_applies_once_to_output_not_twice_to_fees(self):
        r=self.cases['C11_robot_digital'];b=r['calendar_bridge']
        commissioned=[e for e in r['events'] if e['action']=='commission' and e['status']=='installed']
        self.assertEqual(len(commissioned),3)
        for event in commissioned:
            month=event['at']['month'];uid=event['unit_ids'][0]
            cohort=next(x for x in b['months'][month]['cohorts'] if x['unit_id']==uid)
            later=next(x for x in b['months'][month+1]['cohorts'] if x['unit_id']==uid)
            self.assertEqual(q(cohort['ramp_fraction']),Fraction(1,4))
            self.assertEqual(q(cohort['capacity_units'])*4,q(later['capacity_units']))
            bill=next(x for x in b['charge_lines'] if x['month']==month and x['unit_id']==uid and x['category']=='robot_digital_subscription')
            self.assertEqual(bill['rounded_cents'],12500)

    def test_year_rollup_counts_actual_unit_months_and_service_once(self):
        for r in self.cases.values():
            b=r['calendar_bridge']
            self.assertEqual(sum(x['supported_robot_months'] for x in b['calendar_years']),sum(m['support']['used'] for m in r['months']))
            self.assertEqual(sum((q(x['accepted_cleaning_zones']) for x in b['calendar_years']),Fraction()),sum((q(m['total_delivered_units']) for m in r['enterprise']['months']),Fraction()))
            for m,physical in zip(b['months'],r['months']):
                self.assertEqual(len(m['cohorts']),physical['support']['used'])
                self.assertEqual(len({x['unit_id'] for x in m['cohorts']}),len(m['cohorts']))

    def test_fixed_paid_shifts_are_not_removed_when_tasks_shrink(self):
        rows={r['case']:r for r in self.artifact['summary']}
        names=['C00_human_baseline','C01_digital_human','C10_robot_base','C11_robot_digital']
        self.assertEqual({q(rows[n]['accepted_cleaning_zones']) for n in names},{4180})
        self.assertEqual({rows[n]['staff_commitment_cents'] for n in names},{3_840_000})
        self.assertEqual({rows[n]['current_period_staff_cash_paid_cents'] for n in names},{3_840_000})
        self.assertLess(q(rows['C01_digital_human']['retained_human_task_hours']),q(rows['C00_human_baseline']['retained_human_task_hours']))
        self.assertLess(q(rows['C11_robot_digital']['retained_human_task_hours']),q(rows['C01_digital_human']['retained_human_task_hours']))
        for r in self.cases.values():
            self.assertTrue(all(x['removed_payroll_cents'] is None for m in r['calendar_bridge']['months'] for x in m['human_work']))

    def test_joint_interaction_is_not_added_as_an_extra_benefit(self):
        j=self.artifact['joint']['retained_human_task_hours'];v={k:q(x) for k,x in j['values'].items()}
        self.assertEqual(q(j['interaction']),v['C11_robot_digital']-v['C10_robot_base']-v['C01_digital_human']+v['C00_human_baseline'])
        self.assertEqual(q(self.artifact['joint']['accepted_cleaning_zones']['interaction']),0)

    def test_paid_calendar_upgrade_competes_with_support_and_frozen_cohort_stays_old(self):
        current=self.cases['calendar_improving'];frozen=self.cases['frozen_cohorts'];ample=self.cases['upgrade_hours_available']
        self.assertEqual(current['months'][6]['support']['used'],4)
        self.assertEqual(ample['months'][6]['support']['used'],5)
        self.assertEqual(frozen['months'][6]['support']['used'],5)
        self.assertTrue(any(e['reason']=='shared_support_and_qualification_hours' for e in current['calendar_bridge']['events']))
        self.assertTrue(all(x['software_year']==2026 and not x['upgrade_performed'] for m in frozen['calendar_bridge']['months'] for x in m['cohorts']))
        self.assertEqual(sum(x['upgrade_performed'] for m in current['calendar_bridge']['months'] for x in m['cohorts']),5)

    def test_identical_robot_levels_do_not_create_an_upgrade_charge(self):
        r=self.cases['C11_robot_digital']
        self.assertEqual(sum(x['upgrade_performed'] for m in r['calendar_bridge']['months'] for x in m['cohorts']),0)
        self.assertTrue(all(x['rounded_cents']==0 for x in r['calendar_bridge']['charge_lines'] if x['category']=='software_upgrade_qualification'))

    def test_process_integration_hours_delay_actual_commissioning(self):
        r=self.cases['C11_robot_digital']
        self.assertEqual(r['months'][2]['flows']['commissioned'],2)
        self.assertEqual(r['months'][3]['flows']['commissioned'],1)
        self.assertTrue(any(e['reason']=='allocated_process_integration_hours' for e in r['calendar_bridge']['events']))
        self.assertEqual(sum(q(m['integration_hours_used']) for m in r['calendar_bridge']['months']),210)

    def test_one_cent_digital_shortfall_rolls_back_whole_support_booking(self):
        args=one_unit();p=args[0]
        needed=150000+5000+p.system.support_cents_per_robot_month+12500
        short=run_bridged_enterprise(*one_unit(cash=needed-1));funded=run_bridged_enterprise(*one_unit(cash=needed))
        self.assertEqual(short['months'][0]['support']['used'],0)
        self.assertEqual(funded['months'][0]['support']['used'],1)
        self.assertEqual(short['months'][0]['closing_cash_cents']['incumbent'],p.system.support_cents_per_robot_month+12499)
        self.assertEqual(funded['months'][0]['closing_cash_cents']['incumbent'],0)
        self.assertEqual(q(short['calendar_bridge']['months'][0]['support_hours_used']),0)
        self.assertTrue(any(e['reason']=='funding:robot_digital_subscription' for e in short['calendar_bridge']['events']))
        cancelled=[i for i in short['closing_treasury']['invoices'] if i['category'] in ('support','robot_digital_subscription')]
        self.assertTrue(all(i['paid_cents']==0 and i['outstanding_cents']==0 for i in cancelled))

    def test_unfunded_upgrade_never_advances_vintage_or_creates_service(self):
        x=copy.deepcopy(bridge_witness_options()['calendar_improving'])
        x['bridge_inputs']['upgrade_cost_cents_per_robot']=100_000_000
        r=run_bridge_case(**x)
        self.assertEqual(r['months'][6]['support']['used'],0)
        events=[e for e in r['calendar_bridge']['events'] if e['month']==6]
        self.assertTrue(all(e['retained_software_year']==2026 for e in events))
        self.assertTrue(any(e['reason']=='funding:software_upgrade_qualification' for e in events))

    def test_digital_payments_reconcile_to_external_supplier_and_are_not_added_twice(self):
        for r in self.cases.values():
            b=r['calendar_bridge'];vendor=next(a for a in r['closing_treasury']['actors'] if a['actor_id']=='digital_vendor')
            self.assertEqual(vendor['cash_cents'],b['cash']['digital_and_upgrade_paid_cents'])
            self.assertEqual(r['finance']['consolidation']['unclassified_other_boundary_cash_cents'],0)
            self.assertFalse(b['cash']['add_to_consolidated_outlay_again'])

    def test_half_up_invoice_rounding_is_disclosed(self):
        r=run_bridge_case({'entrant_cash_cents':10_000_000,'loan_cents':0},{'annual_overrides':{'digital_cost_usd':1}})
        lines=[x for x in r['calendar_bridge']['charge_lines'] if x['category']=='robot_digital_subscription']
        self.assertTrue(lines)
        for line in lines:
            self.assertEqual(q(line['exact_cents']),Fraction(100,12))
            self.assertEqual(line['rounded_cents'],8)
            self.assertEqual(q(line['rounding_difference_cents']),Fraction(-1,3))

    def test_saved_cost_and_staff_mapping_cannot_silently_change(self):
        args=list(bridge_case_inputs())
        args[0]=replace(args[0],system=replace(args[0].system,support_cents_per_robot_month=1))
        with self.assertRaisesRegex(ValueError,'physical cost/configuration'):run_bridged_enterprise(*args)
        args=list(bridge_case_inputs());business=args[3].businesses[0]
        bad=replace(business,human_capacity_by_month=(10000,)*8)
        args[3]=replace(args[3],businesses=(bad,args[3].businesses[1]))
        with self.assertRaisesRegex(ValueError,'paid-shift'):run_bridged_enterprise(*args)
        with self.assertRaises(ValueError):run_bridge_case(bridge_inputs=[])

    def test_all_saved_worlds_replay_exactly_and_ignore_saved_outputs(self):
        for name,r in self.cases.items():self.assertEqual(replay_bridge(json.loads(json.dumps(r))),r,name)
        tampered=copy.deepcopy(self.cases['C11_robot_digital']);tampered['calendar_bridge']['calendar_years'][0]['accepted_cleaning_zones']['numerator']=999999
        self.assertEqual(replay_bridge(tampered),self.cases['C11_robot_digital'])

    def test_rational_wire_components_preserve_integers_above_browser_safe_range(self):
        large=[]
        def inspect(value):
            if isinstance(value,dict):
                if set(value)=={'numerator','denominator'}:
                    self.assertTrue(all(isinstance(x,str) for x in value.values()))
                    self.assertGreater(int(value['denominator']),0)
                    if abs(int(value['numerator']))>2**53-1:large.append(value)
                else:
                    for x in value.values():inspect(x)
            elif isinstance(value,list):
                for x in value:inspect(x)
            elif type(value) is int:self.assertLessEqual(abs(value),2**53-1)
        inspect(self.artifact)
        self.assertTrue(large,'Fixture must exercise the browser precision boundary')
        self.assertEqual(json.loads(json.dumps(large)),large)
        with self.assertRaisesRegex(ValueError,'lossless browser JSON range'):
            run_bridged_enterprise(*one_unit(cash=2**53))

    def test_seeded_cash_demand_cohort_and_resource_conservation(self):
        rng=random.Random(314159)
        for _ in range(12):
            r=run_bridge_case({'entrant_cash_cents':rng.randrange(50000,8000000),'loan_cents':rng.randrange(0,4000000),'maturity_month':rng.choice([3,7,12])},
                {'support_hours_per_month':rng.choice([25,45,60,65]),'integration_hours_per_month':rng.choice([60,140,200]),
                 'annual_overrides':{'digital_efficiency':rng.random()*.6,'coordination':rng.random()-.4,'capability':.7+rng.random()*.3}})
            self.assertEqual(sum(a['cash_cents'] for a in r['opening_treasury']['actors']),sum(a['cash_cents'] for a in r['closing_treasury']['actors']))
            for m in r['calendar_bridge']['months']:
                self.assertLessEqual(q(m['support_hours_used'])+q(m['qualification_hours_used']),m['hours_capacity'])
                self.assertLessEqual(q(m['integration_hours_used']),m['integration_hours_capacity'])
            for m in r['enterprise']['months']:
                self.assertLessEqual(q(m['total_delivered_units']),650)
                for pool in m['pools'].values():self.assertEqual(q(pool['delivered_units'])+q(pool['unserved_units']),pool['recurring_demand_units'])

    def test_invalid_units_calendar_learning_and_resource_allocations_fail_closed(self):
        for override in [{'cell_id':'other'},{'start_month':13},{'start_year':2035},{'digital_enabled':1},
                         {'software_policy':'free_magic'},{'annual_overrides':{'learning_transfer':.1}},
                         {'annual_overrides':{'integration_hours':0}},{'support_hours_per_month':1001},
                         {'integration_hours_per_month':201}]:
            with self.assertRaises((ValueError,TypeError),msg=str(override)):run_bridge_case(bridge_inputs=override)
        bad={'schema_version':'digital-annual-paths/0.1','base_year':2027,'epistemic_status':'synthetic_assumption'}
        with self.assertRaises(ValueError):run_bridge_case(bridge_inputs={'digital_paths':bad})


if __name__=='__main__':unittest.main()
