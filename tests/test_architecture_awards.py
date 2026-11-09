import copy
from fractions import Fraction
import unittest

from model.architecture_awards import architecture_awards_artifact,run_architecture_awards_case,replay_architecture_awards
from model.qualified_staffing import available_support
from model.calendar_bridge import rational


class ArchitectureAwardsTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.artifact=architecture_awards_artifact();cls.cases=cls.artifact['cases'];cls.summary={s['case']:s for s in cls.artifact['summary']}

    def test_one_cash_physical_part_and_work_history_conserves(self):
        for name,r in self.cases.items():
            self.assertEqual(sum(a['cash_cents'] for a in r['opening_treasury']['actors']),sum(a['cash_cents'] for a in r['closing_treasury']['actors']),name)
            self.assertEqual(r['entry_transition']['consolidation']['unclassified_boundary_cash_cents'],0)
            self.assertEqual(r['finance']['consolidation']['unclassified_other_boundary_cash_cents'],0)
            for m in r['component_inventory']['months']:
                for k in m['qualified_closing']:
                    self.assertEqual(m['qualified_opening'][k]+m['qualified_release'][k],m['qualified_closing'][k]+m['manufacturing_issued'][k]+m['service_issued'][k])
                    self.assertEqual(m['quarantine_opening'][k]+m['received'][k],m['quarantine_closing'][k]+m['qualified_release'][k])
            for m in r['staffed_renewals']['months']:
                self.assertEqual(sum((rational(b['minutes']) for b in m['bookings']),Fraction())+rational(m['unused_minutes']),m['regular_available_minutes']+m['overtime_paid_minutes'])
                self.assertEqual(m['outside_completed_jobs']+m['outside_unserved_jobs'],m['outside_required_jobs'])
            for m in r['competition']['months']:self.assertEqual(sum(l['units'] for l in m['lots']),500)

    def test_all_payer_resource_cash_excludes_internal_fees(self):
        for r in self.cases.values():
            outside={'manufacturer','deployment_vendor','enterprise_vendor','digital_vendor','entry_resource_vendor','architecture_resources'}
            cash=sum(i['paid_cents'] for i in r['closing_treasury']['invoices'] if i['payee'] in outside)
            self.assertEqual(cash,r['staffed_renewals']['cash']['all_payer_resource_and_transaction_cash_cents'])
            for line in r['architecture_execution']['cash_lines']:
                if line['internal_eliminated']:
                    self.assertIsNone(line['invoice_id']);self.assertEqual(line['paid_cents'],0)

    def test_fixed_logical_capital_merges_only_within_declared_legal_entities(self):
        self.assertEqual(len({sum(x['cash_cents'] for x in r['opening_treasury']['actors']) for r in self.cases.values()}),1)
        for r in self.cases.values():
            a=r['architecture_execution'];cash=a['inputs']['role_opening_cash_cents'];roles=a['role_entities']
            self.assertEqual(sum(cash.values()),60000000)
            for actor in a['entities']:
                self.assertEqual(actor['opening_cash_cents'],sum(v for role,v in cash.items() if roles[role]==actor['actor_id']))
            self.assertEqual(r['architecture_awards']['customer_contract_owners'],{'incumbent':'incumbent','entrant':'entrant'})

    def test_operator_pays_its_staff_and_owns_hardware_outside_acquired_customer(self):
        r=self.cases['model_led_operator'];op='arch:model_operator'
        for i in r['closing_treasury']['invoices']:
            if i['category']=='human_staff' and ':incumbent:' in i['invoice_id']:self.assertEqual(i['payer'],op)
        asset=r['commercial']['months'][-1]['assets'][0]
        self.assertEqual((asset['title_owner'],asset['custodian'],asset['support_payer']),(op,op,op))
        self.assertTrue(r['renewing_entry']['months'][-1]['common_owner_of_active_firms'])
        self.assertNotIn(op,r['renewing_entry']['months'][-1]['separately_funded_accounts'])
        self.assertEqual(r['architecture_awards']['staffing_payers'],{'incumbent':op,'entrant':'entrant'})

    def test_cash_location_can_break_whole_service_at_identical_total_capital(self):
        a,b=(self.summary[n] for n in ('model_led_operator','model_capital_in_customer'))
        self.assertEqual(a['opening_role_cash_cents'],b['opening_role_cash_cents'])
        self.assertEqual((a['complete_whole_service_months'],b['complete_whole_service_months']),(8,0))
        self.assertEqual(rational(b['accepted_zones']),2400);self.assertEqual(b['outside_completed_jobs'],0)
        self.assertEqual(b['operator_due_unpaid_cents'],4040000)
        r=self.cases['model_capital_in_customer'];actors={x['actor_id']:x['cash_cents'] for x in r['closing_treasury']['actors']}
        self.assertEqual(actors['incumbent'],40000000);self.assertEqual(actors['arch:model_operator'],0)
        self.assertEqual(r['months'][0]['flows']['started'],1)
        self.assertEqual(r['commercial']['months'][-1]['assets'][0]['title_owner'],'provider')

    def test_stranded_cash_failure_also_occurs_without_robots(self):
        a,b=(self.summary[n] for n in ('model_capital_in_customer','model_capital_in_customer_human_only'))
        for key in ('accepted_zones','outside_completed_jobs','outside_required_jobs','complete_whole_service_months','operator_due_unpaid_cents'):self.assertEqual(a[key],b[key])
        self.assertFalse(self.cases['model_capital_in_customer_human_only']['units'])
        self.assertEqual(a['all_payer_resource_and_transaction_cash_cents']-b['all_payer_resource_and_transaction_cash_cents'],3600000)

    def test_funded_human_comparisons_keep_all_required_service_and_lower_resource_cash(self):
        for robot,human in [('licensed_independent','licensed_human_only'),('model_led_operator','model_operator_human_only')]:
            a,b=self.summary[robot],self.summary[human]
            for key in ('accepted_zones','outside_completed_jobs','outside_required_jobs','complete_whole_service_months'):self.assertEqual(a[key],b[key])
            self.assertLess(b['all_payer_resource_and_transaction_cash_cents'],a['all_payer_resource_and_transaction_cash_cents'])
            self.assertEqual(b['all_payer_resource_and_transaction_cash_cents'],8730000)

    def test_exact_engineering_gate_preserves_paid_hardware_and_human_fallback(self):
        short=self.cases['open_one_engineering_hour_short']
        exact=run_architecture_awards_case({'architecture':{'architecture_id':'open_adapted','engineering_hours_per_month':300}})
        self.assertFalse(any(m['supported_unit_ids'] for m in short['annual_resources']['months']))
        self.assertTrue(any(m['supported_unit_ids'] for m in exact['annual_resources']['months']))
        self.assertEqual(short['commercial']['months'][-1]['assets'][0]['title_owner'],'incumbent')
        self.assertTrue(any(e.get('reason')=='architecture_engineering_hours' for e in short['architecture_execution']['events']))
        self.assertEqual(self.summary['open_one_engineering_hour_short']['complete_whole_service_months'],8)
        self.assertTrue(all(m['notice_issued_month'] is None for m in short['staffed_renewals']['months']))

    def test_failed_annual_booking_rolls_back_role_fees_parts_and_resource_minutes(self):
        r=run_architecture_awards_case({'qualified':{'resources':available_support(1300)}})
        for month in (4,5):
            self.assertEqual(r['component_inventory']['months'][month]['service_issued']['actuator_h'],0)
            self.assertEqual(r['component_inventory']['months'][month]['qualified_closing']['actuator_h'],1)
            lines=[x for x in r['architecture_execution']['cash_lines'] if x['month']==month and x['unit_id']]
            self.assertTrue(lines);self.assertTrue(all(x['paid_cents']==0 for x in lines))
            self.assertTrue(all(rational(x['committed_minutes']['support'])==0 for x in r['annual_resources']['attempts'] if x['month']==month))
        self.assertEqual(r['component_inventory']['months'][6]['service_issued']['actuator_h'],1)

    def test_prospective_overtime_uses_actual_service_operator_cash(self):
        r=run_architecture_awards_case({'architecture':{'architecture_id':'model_led_operator'},
            'qualified':{'staffed':{'crews':{'incumbent':{'overtime_minutes_per_month':5000,'outside_jobs_by_month':[20]*4+[45]*4}}}}})
        paid=[x for x in r['staffed_renewals']['months'] if x['operator_id']=='incumbent' and x['overtime_paid_minutes']]
        self.assertTrue(paid)
        for x in paid:
            i=next(i for i in r['closing_treasury']['invoices'] if i['invoice_id']==x['overtime_invoice_id'])
            self.assertEqual(i['payer'],'arch:model_operator');self.assertEqual(i['due_at']['phase'],5)
            self.assertEqual(x['cash_before_overtime_cents']-x['cash_after_overtime_before_awards_cents'],i['paid_cents'])

    def test_service_fee_redistributes_cash_without_adding_resource_consumption(self):
        a=self.cases['model_led_operator'];b=run_architecture_awards_case({'architecture':{'architecture_id':'model_led_operator','service_cents_per_accepted_zone':1200}})
        for before,after in zip(a['competition']['months'],b['competition']['months']):
            for key in ('lots','offers_cents_per_unit','funded_capacity_before_awards'):self.assertEqual(before[key],after[key])
        self.assertEqual(a['staffed_renewals']['cash']['all_payer_resource_and_transaction_cash_cents'],b['staffed_renewals']['cash']['all_payer_resource_and_transaction_cash_cents'])
        def fee(r):return sum(x['paid_cents'] for x in r['architecture_execution']['cash_lines'] if x['category']=='operating_service_payment')
        self.assertEqual(fee(b),2*fee(a));self.assertGreater(fee(a),0)

    def test_share_closing_does_not_create_operator_assets_or_pool_cash(self):
        a=self.cases['model_led_operator'];b=run_architecture_awards_case({'architecture':{'architecture_id':'model_led_operator'},'qualified':{'staffed':{'entry':{'mode':'build'}}}})
        self.assertEqual(a['competition']['months'],b['competition']['months'])
        self.assertEqual(a['architecture_execution']['cash_lines'],b['architecture_execution']['cash_lines'])
        self.assertEqual(a['commercial']['months'][-1]['assets'],b['commercial']['months'][-1]['assets'])
        self.assertFalse(b['renewing_entry']['months'][-1]['common_owner_of_active_firms'])

    def test_complete_replay_reconstructs_roles_and_ignores_derived_ledgers(self):
        for name,r in self.cases.items():
            saved=copy.deepcopy(r);saved['architecture_execution']['entities']=[];saved['architecture_execution']['cash_lines']=[]
            saved['architecture_awards']={};saved['staffed_renewals']['months']=[];saved['closing_treasury']={};saved['case_hash']='forged'
            self.assertEqual(replay_architecture_awards(saved),r,name)

    def test_incompatible_second_fleet_and_inconsistent_capital_fail_explicitly(self):
        invalid=[[],{'architecture':None},{'architecture':{'opening_robots':1}},
            {'qualified':{'staffed':{'entry':{'target_cash_cents':1}}}},
            {'qualified':{'staffed':{'entry':{'market':{'entrant_robots':1}}}}}]
        for value in invalid:
            with self.assertRaises((ValueError,TypeError)):run_architecture_awards_case(value)
        saved=copy.deepcopy(self.cases['model_led_operator']);saved['architecture_execution']['inputs']['role_opening_cash_cents']['operator']+=1
        with self.assertRaises(ValueError):replay_architecture_awards(saved)
        saved=copy.deepcopy(self.cases['model_led_operator']);del saved['annual_resources']
        with self.assertRaises(ValueError):replay_architecture_awards(saved)

if __name__=='__main__':unittest.main()
