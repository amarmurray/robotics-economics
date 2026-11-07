"""Architecture labels cannot invent cash, resources, qualification or service."""
import copy
from dataclasses import replace
from fractions import Fraction
import json
import random
import unittest
from model.architectures import ROLES
from model.calendar_bridge import rational
from model.monthly_architectures import (ArchitectureExecution, ROLE_CASH, RESOURCE_ACTOR,
    architecture_case_inputs, architecture_execution_artifact, replay_architecture_execution,
    run_architecture_case, run_architecture_execution)


class MonthlyArchitectureTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.artifact=architecture_execution_artifact();cls.cases=cls.artifact['cases']

    def test_complete_saved_cases_replay_and_outputs_are_not_inputs(self):
        for name,r in self.cases.items():self.assertEqual(replay_architecture_execution(json.loads(json.dumps(r))),r,name)
        x=copy.deepcopy(self.cases['licensed_independent']);x['architecture_execution']['entities'][0]['closing_cash_cents']=0
        self.assertEqual(replay_architecture_execution(x),self.cases['licensed_independent'])

    def test_equivalent_json_integer_float_forms_preserve_full_case_hash(self):
        r=copy.deepcopy(self.cases['licensed_independent'])
        # JavaScript JSON export removes integral .0 spellings; either spelling
        # must preserve the complete case, including its calculated hash.
        r['calendar_bridge']['inputs']['annual_overrides']['intervention_minutes']=3.0
        r['architecture_execution']['inputs']['annual_reference_overrides']['integration_hours']=70.0
        self.assertEqual(replay_architecture_execution(r),self.cases['licensed_independent'])
        self.assertIs(type(self.cases['licensed_independent']['architecture_execution']['profile']['demonstration_hours']),int)

    def test_same_total_role_capital_survives_entity_consolidation(self):
        for name in ('integrated_oem','licensed_independent','open_adapted','model_led_operator'):
            a=self.cases[name]['architecture_execution']
            self.assertEqual(a['consolidation']['opening_role_cash_cents'],sum(ROLE_CASH.values()))
            for entity in a['entities']:
                self.assertEqual(entity['opening_cash_cents'],sum(ROLE_CASH[role] for role in entity['roles']))
        self.assertEqual(len(self.cases['integrated_oem']['architecture_execution']['entities']),2)
        self.assertEqual(len(self.cases['licensed_independent']['architecture_execution']['entities']),4)

    def test_fee_changes_redistribute_cash_without_adding_resource_cost(self):
        base=self.cases['licensed_independent'];high=self.cases['licensed_high_fee']
        for key in ('external_physical_and_enterprise_cash_cents','itemized_architecture_resource_cash_cents'):
            self.assertEqual(base['architecture_execution']['consolidation'][key],high['architecture_execution']['consolidation'][key])
        self.assertEqual(base['enterprise']['months'],high['enterprise']['months'])
        b={x['actor_id']:x for x in base['architecture_execution']['entities']};h={x['actor_id']:x for x in high['architecture_execution']['entities']}
        model=base['architecture_execution']['role_entities']['model_supplier'];operator=base['architecture_execution']['role_entities']['operator']
        delta=h[model]['closing_cash_cents']-b[model]['closing_cash_cents']
        self.assertGreater(delta,0);self.assertEqual(h[operator]['closing_cash_cents']-b[operator]['closing_cash_cents'],-delta)

    def test_internal_model_fees_have_no_invoice_or_cash_posting(self):
        for name in ('open_adapted','model_led_operator'):
            a=self.cases[name]['architecture_execution']
            fees=[x for x in a['cash_lines'] if x['category']=='model_monthly_fee']
            self.assertTrue(fees)
            self.assertTrue(all(x['internal_eliminated'] and x['invoice_id'] is None and x['paid_cents']==0 for x in fees))
            self.assertTrue(any(x['paid_cents']>0 for x in a['cash_lines'] if x['category']=='inference_resources'))

    def test_digital_bundle_is_replaced_and_inference_charged_once(self):
        for r in self.cases.values():
            self.assertFalse(any(i['category']=='robot_digital_subscription' for i in r['closing_treasury']['invoices']))
            bills=[x for x in r['architecture_execution']['cash_lines'] if x['category']=='inference_resources' and x['paid_cents']]
            supported=sum(m['support']['used'] for m in r['months'])
            self.assertEqual(len(bills),supported)
            self.assertEqual(len({(x['month'],x['unit_id']) for x in bills}),supported)

    def test_one_initial_qualification_per_actual_unit_not_per_month(self):
        for r in self.cases.values():
            a=r['architecture_execution'];paid=[x for x in a['cash_lines'] if x['category']=='model_adaptation_engineering' and x['paid_cents']]
            self.assertEqual(len(paid),len(a['months'][-1]['qualified_unit_ids']))
            self.assertEqual(len({x['unit_id'] for x in paid}),len(paid))
            self.assertTrue(set(a['months'][-1]['qualified_unit_ids'])<={u['unit_id'] for u in r['units']})

    def test_fixed_paid_staff_and_common_service_remain(self):
        for row in self.artifact['summary']:
            self.assertEqual(rational(row['accepted_zones']),4000)
            self.assertEqual(row['staff_cash_paid_cents'],3_200_000)
        self.assertEqual(rational(next(x for x in self.artifact['summary'] if x['case']=='licensed_no_model_cash')['robot_zones']),0)

    def test_model_operator_owns_hardware_and_pays_actual_staff(self):
        r=self.cases['model_led_operator'];a=r['architecture_execution'];operator=a['role_entities']['operator'];customer=a['role_entities']['customer']
        self.assertNotEqual(operator,customer)
        self.assertTrue(all(i['payer']==operator for i in r['closing_treasury']['invoices'] if i['category']=='human_staff'))
        for m in r['commercial']['months']:
            for asset in m['assets']:
                if asset['physical_state']=='installed':self.assertEqual((asset['title_owner'],asset['custodian'],asset['workflow_authority']),(operator,operator,operator))
        self.assertTrue(any(x['category']=='operating_service_payment' and x['payer']==customer and x['payee']==operator and x['paid_cents']>0 for x in a['cash_lines']))

    def test_actual_service_invoices_follow_output_and_preserve_receivable(self):
        r=self.cases['model_led_operator'];a=r['architecture_execution'];rows=[x for x in a['cash_lines'] if x['category']=='operating_service_payment']
        self.assertEqual(len(rows),8)
        for line,m in zip(rows,r['enterprise']['months']):
            self.assertEqual(line['nominal_cents'],rational(m['total_delivered_units'])*600)
        self.assertEqual(rows[-1]['paid_cents'],0);self.assertEqual(rows[-1]['outstanding_cents'],300000)
        self.assertEqual(a['consolidation']['baseline_cost_credit_cents'],0)

    def test_cash_and_boundary_reconciliation(self):
        for r in self.cases.values():
            self.assertEqual(sum(x['cash_cents'] for x in r['opening_treasury']['actors']),sum(x['cash_cents'] for x in r['closing_treasury']['actors']))
            self.assertEqual(r['finance']['consolidation']['unclassified_other_boundary_cash_cents'],0)
            a=r['architecture_execution'];resources=sum(x['paid_cents'] for x in a['cash_lines'] if x['resource_expense'])
            self.assertEqual(resources,a['consolidation']['itemized_architecture_resource_cash_cents'])
            outside=next(x for x in r['closing_treasury']['actors'] if x['actor_id']==RESOURCE_ACTOR)
            self.assertEqual(resources,outside['cash_cents'])

    def test_failed_funding_rolls_back_fees_resources_and_qualification(self):
        r=self.cases['licensed_no_model_cash'];a=r['architecture_execution']
        self.assertFalse(a['months'][-1]['qualified_unit_ids'])
        self.assertEqual(sum(x['paid_cents'] for x in a['cash_lines'] if x['unit_id']),0)
        self.assertTrue(all(rational(x['engineering_hours_used'])==0 for x in a['months']))
        self.assertTrue(any(x['action']=='blocked' and x['reason'].startswith('funding:') for x in a['events']))

    def test_exact_one_cent_model_funding_boundary(self):
        # $10,500 initial work + $225 recurring resources - $3,000 upfront - $333.33 fee.
        threshold=739167
        x={'opening_robots':1,'new_robots':0,'role_opening_cash_cents':{'model_supplier':threshold}}
        funded=run_architecture_case(x);short=run_architecture_case({**x,'role_opening_cash_cents':{'model_supplier':threshold-1}})
        self.assertEqual(funded['months'][0]['support']['used'],1)
        self.assertEqual(short['months'][0]['support']['used'],0)
        self.assertEqual(short['architecture_execution']['months'][0]['qualified_unit_ids'],[])
        self.assertFalse(any(x['month']==0 and x['unit_id'] and x['paid_cents'] for x in short['architecture_execution']['cash_lines']))

    def test_resource_limits_delay_qualification_without_spending_failed_group(self):
        for r in self.cases.values():
            a=r['architecture_execution']
            for m in a['months']:
                self.assertLessEqual(rational(m['engineering_hours_used']),a['inputs']['engineering_hours_per_month'])
                self.assertLessEqual(rational(m['demonstration_hours_used']),a['inputs']['demonstration_hours_per_month'])
        r=self.cases['open_engineering_scarcity']
        self.assertTrue(all(m['support']['used']==0 for m in r['months']))
        self.assertTrue(any(x.get('reason')=='architecture_engineering_hours' for x in r['architecture_execution']['events']))

    def test_false_rights_gate_blocks_robots_without_erasing_human_fallback(self):
        r=self.cases['rights_not_assumed'];a=r['architecture_execution']
        self.assertEqual(a['status'],'robot_policy_not_admitted')
        self.assertEqual(a['failed_assumptions'],['assume_rights_available'])
        self.assertEqual(sum(m['flows']['started'] for m in r['months']),0)
        self.assertEqual(sum(m['support']['used'] for m in r['months']),0)
        self.assertEqual(sum(rational(m['total_delivered_units']) for m in r['enterprise']['months']),4000)

    def test_complete_input_mapping_mismatch_is_rejected(self):
        r=copy.deepcopy(self.cases['licensed_independent'])
        r['architecture_execution']['inputs']['architecture_overrides']['profiles']['licensed_independent']['integration_multiplier']=2
        with self.assertRaisesRegex(ValueError,'reference mapping'):replay_architecture_execution(r)
        r=copy.deepcopy(self.cases['licensed_independent']);r['architecture_execution']['inputs']['role_opening_cash_cents']['model_supplier']+=1
        with self.assertRaisesRegex(ValueError,'logical-role capital'):replay_architecture_execution(r)

    def test_same_total_capital_can_fund_previously_stranded_operator_assets(self):
        b=self.cases['model_led_operator'];r=self.cases['model_operator_capital_reallocated']
        self.assertEqual(b['architecture_execution']['consolidation']['opening_role_cash_cents'],r['architecture_execution']['consolidation']['opening_role_cash_cents'])
        self.assertEqual(len(b['units']),len(r['units']))
        self.assertLess(len(b['architecture_execution']['months'][-1]['qualified_unit_ids']),len(r['architecture_execution']['months'][-1]['qualified_unit_ids']))
        self.assertEqual(len(r['architecture_execution']['months'][-1]['qualified_unit_ids']),4)

    def test_extra_initial_engineering_preserves_existing_support_and_admits_starts(self):
        b=self.cases['open_adapted'];r=self.cases['open_initial_engineering_available']
        self.assertEqual(b['months'][0]['support']['used'],1)
        self.assertEqual(r['months'][0]['support']['used'],2)
        self.assertEqual(b['months'][0]['flows']['started'],0)
        self.assertEqual(r['months'][0]['flows']['started'],2)
        self.assertEqual(len(r['architecture_execution']['months'][-1]['qualified_unit_ids']),4)
        self.assertEqual(r['months'][2]['flows']['commissioned'],1)
        self.assertEqual(r['months'][3]['flows']['commissioned'],1)

    def test_labels_alone_do_not_change_matched_resource_cost_or_service(self):
        from model.architectures import resolve
        settings=resolve();reference=settings['profiles']['licensed_independent']
        profiles={name:{**reference,'role_entities':a['role_entities']} for name,a in settings['profiles'].items()}
        results=[run_architecture_case({'architecture_id':name,'architecture_overrides':{'profiles':profiles},
                    'role_opening_cash_cents':{role:1_000_000_000 for role in ROLES},'engineering_hours_per_month':1000}) for name in profiles]
        self.assertEqual(len({r['architecture_execution']['consolidation']['external_physical_and_enterprise_cash_cents'] for r in results}),1)
        self.assertEqual(len({r['architecture_execution']['consolidation']['itemized_architecture_resource_cash_cents'] for r in results}),1)
        self.assertEqual(len({sum(m['support']['used'] for m in r['months']) for r in results}),1)
        self.assertEqual(len({sum(rational(m['total_delivered_units']) for m in r['enterprise']['months']) for r in results}),1)

    def test_invalid_or_unsupported_inputs_fail_visibly(self):
        for x in ({'architecture_id':'imagined'},{'role_opening_cash_cents':{'unknown':0}},{'opening_robots':5},
                  {'annual_reference_overrides':[]},{'architecture_overrides':{'common':{'service_price_fraction':.5}}},
                  {'engineering_hours_per_month':True},{'service_collection_lag_months':0}):
            with self.assertRaises((ValueError,TypeError)):run_architecture_case(x)
        with self.assertRaisesRegex(ValueError,'annual_reference_overrides'):run_architecture_case(bridge_inputs={'annual_overrides':{}})
        with self.assertRaises(ValueError):run_architecture_case(bridge_inputs=[])

    def test_seeded_resource_cash_and_demand_invariants(self):
        rng=random.Random(1616)
        for _ in range(8):
            x={'architecture_id':rng.choice(['integrated_oem','licensed_independent','open_adapted','model_led_operator']),
               'engineering_hours_per_month':rng.choice([100,200,400,600]),'new_robots':rng.randrange(3),
               'role_opening_cash_cents':{'operator':rng.randrange(0,20_000_000),'model_supplier':rng.randrange(0,10_000_000)}}
            r=run_architecture_case(x);a=r['architecture_execution']
            for m in r['enterprise']['months']:
                self.assertLessEqual(rational(m['total_delivered_units']),500)
                self.assertEqual(rational(m['pools']['baseline']['delivered_units'])+rational(m['pools']['baseline']['unserved_units']),500)
            self.assertEqual(r['finance']['consolidation']['unclassified_other_boundary_cash_cents'],0)
            self.assertTrue(all(rational(m['engineering_hours_used'])<=x['engineering_hours_per_month'] for m in a['months']))


if __name__=='__main__':unittest.main()
