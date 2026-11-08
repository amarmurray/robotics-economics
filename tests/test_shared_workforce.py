"""Paid capacity, complete unlike services and every payer must reconcile."""
import copy
from fractions import Fraction
import json
from pathlib import Path
import random
import unittest

from model.calendar_bridge import rational
from model.shared_workforce import (Workforce, OUTSIDE_BUYER, run_workforce_case,
    replay_workforce_case, workforce_worlds, workforce_summary, workforce_catalog)


class SharedWorkforceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):cls.cases=json.loads(Path('model/results/shared_workforce.json').read_text())['cases']

    def assert_conserved(self,r):
        w=r['shared_workforce'];inputs=w['inputs']
        self.assertEqual(sum(a['cash_cents'] for a in r['opening_treasury']['actors']),sum(a['cash_cents'] for a in r['closing_treasury']['actors']))
        self.assertTrue(all(a['cash_cents']>=0 for a in r['closing_treasury']['actors']))
        self.assertEqual(r['finance']['consolidation']['unclassified_other_boundary_cash_cents'],0)
        invoices=r['closing_treasury']['invoices'];self.assertEqual(len(invoices),len({x['invoice_id'] for x in invoices}))
        for row,market in zip(w['months'],r['enterprise']['months']):
            booked=sum((rational(x['minutes']) for x in row['bookings']),Fraction())
            self.assertEqual(booked,rational(row['booked_minutes']))
            self.assertEqual(booked+rational(row['unused_minutes']),row['worker_budget_minutes'])
            self.assertGreaterEqual(rational(row['unused_minutes']),0)
            self.assertEqual(row['worker_budget_minutes'],row['regular_available_minutes']+row['overtime_paid_minutes'])
            self.assertEqual(len({x['task_id'] for x in row['bookings']}),len(row['bookings']))
            self.assertTrue(all(x['worker_resource_id']==inputs['resource_id'] for x in row['bookings']))
            jobs=[x for x in row['bookings'] if x['kind']=='outside_inventory_job']
            self.assertEqual(len(jobs),row['outside_completed_jobs'])
            self.assertTrue(all(rational(x['accepted_quantity'])==1 and rational(x['minutes'])==inputs['outside_minutes_per_job'] for x in jobs))
            self.assertEqual(row['outside_completed_jobs']+row['outside_unserved_jobs'],row['outside_required_jobs'])
            self.assertEqual(len(row['outside_unserved_ids']),row['outside_unserved_jobs'])
            self.assertFalse(set(row['outside_unserved_ids'])&{x['task_id'] for x in jobs})
            clean=rational(row['robot_cleaning_zones'])+rational(row['human_cleaning_zones'])
            self.assertEqual(clean,rational(row['accepted_cleaning_zones']))
            self.assertEqual(clean+rational(row['unserved_cleaning_zones']),row['cleaning_required_zones'])
            self.assertEqual(clean,rational(market['total_delivered_units']))
            self.assertLessEqual(rational(row['robot_cleaning_zones']),rational(row['robot_capacity_zones']))
            self.assertEqual(row['complete_combined_obligation'],clean==row['cleaning_required_zones'] and row['outside_completed_jobs']==row['outside_required_jobs'] and rational(row['performed_attention_minutes'])==row['required_attention_minutes'])
            self.assertEqual(row['overtime_cash_paid_cents'],row['overtime_paid_minutes']*inputs['overtime_cents_per_minute'])
        self.assertFalse(w['cash']['add_again_to_consolidation'])

    def test_all_worlds_conserve_one_crew_cash_and_distinct_services(self):
        for name,r in self.cases.items():
            with self.subTest(world=name):self.assert_conserved(r)

    def test_staffing_notice_preserves_complete_service_and_only_reduces_declared_commitment(self):
        fixed=self.cases['fixed_crew_with_robots'];cut=self.cases['notice_then_reduce']
        self.assertEqual(fixed['months'][:3],cut['months'][:3])
        self.assertEqual((cut['shared_workforce']['notice_issued_month'],cut['shared_workforce']['notice_effective_month']),(1,3))
        self.assertEqual([m['scheduled_blocks'] for m in cut['shared_workforce']['months']],[2,2,2,1,1,1,1,1])
        a,b=(workforce_summary('',r) for r in (fixed,cut))
        self.assertEqual((a['complete_months'],b['complete_months']),(8,8))
        self.assertEqual((rational(a['cleaning_zones']),rational(b['cleaning_zones']),a['outside_jobs'],b['outside_jobs']),(4000,4000,160,160))
        self.assertEqual(a['staff_paid_cents']-b['staff_paid_cents'],1000000)
        self.assertEqual(a['external_resource_cash_cents']-b['external_resource_cash_cents'],1000000)

    def test_longer_notice_is_a_paid_obligation_not_instant_released_time(self):
        r=self.cases['longer_notice'];self.assertEqual(r['shared_workforce']['notice_effective_month'],5)
        self.assertEqual(r['shared_workforce']['cash']['staff_paid_cents'],2600000)
        self.assertTrue(all(m['complete_combined_obligation'] for m in r['shared_workforce']['months']))

    def test_notice_uses_only_prior_completed_work_not_future_demand(self):
        a=self.cases['notice_then_reduce']['shared_workforce'];b=self.cases['outside_surge_with_overtime']['shared_workforce']
        self.assertEqual(a['months'][:4],b['months'][:4]);self.assertEqual(a['events'],b['events'])
        for event in a['events']:
            self.assertEqual(event['based_only_on_completed_month'],event['month']-1)
            if event['issued']:self.assertGreater(event['effective_month'],event['month'])
        thin=self.cases['low_model_role_cash']['shared_workforce']
        self.assertEqual(thin['notice_effective_month'],3)
        self.assertTrue(all(m['complete_combined_obligation'] for m in thin['months'][:3]))
        self.assertFalse(thin['months'][-1]['complete_combined_obligation'])
        self.assertEqual(thin['months'][-1]['overtime_block_reason'],'unfunded_optional_overtime')

    def test_surge_without_funded_overtime_is_not_a_valid_lower_cost_comparator(self):
        good=workforce_summary('',self.cases['outside_surge_with_overtime']);bad=workforce_summary('',self.cases['outside_surge_without_overtime'])
        self.assertEqual((good['complete_months'],good['outside_jobs'],rational(good['cleaning_zones'])),(8,240,4000))
        self.assertEqual((bad['complete_months'],bad['outside_jobs'],bad['outside_due_jobs'],rational(bad['cleaning_zones'])),(4,232,240,2000))
        self.assertEqual(good['overtime_paid_cents'],496000)
        self.assertLess(bad['external_resource_cash_cents'],good['external_resource_cash_cents'])

    def test_exact_overtime_threshold_and_one_minute_shortfall(self):
        base=workforce_worlds()['outside_surge_with_overtime']
        def case(minutes):
            x=copy.deepcopy(base);x['workforce']['overtime_minutes_per_month']=minutes;return run_workforce_case(x)
        exact,below=case(1240),case(1239)
        self.assertTrue(all(m['complete_combined_obligation'] for m in exact['shared_workforce']['months']))
        self.assertEqual([m['overtime_paid_minutes'] for m in exact['shared_workforce']['months']],[0,0,0,0,1240,1240,1240,1240])
        self.assertEqual(sum(rational(m['accepted_cleaning_zones']) for m in below['shared_workforce']['months']),3998)
        self.assertEqual(sum(m['outside_completed_jobs'] for m in below['shared_workforce']['months']),240)
        self.assert_conserved(below)

    def test_stronger_human_baseline_eliminates_overtime_without_more_staff(self):
        original=self.cases['human_with_funded_overtime'];strong=self.cases['stronger_human_dispatch']
        self.assertEqual(original['shared_workforce']['cash']['overtime_paid_cents'],768000)
        self.assertEqual(strong['shared_workforce']['cash']['overtime_paid_cents'],0)
        for r in (original,strong):
            self.assertEqual(r['shared_workforce']['cash']['staff_paid_cents'],3200000)
            self.assertIsNone(r['shared_workforce']['notice_issued_month'])
            self.assertTrue(all(m['complete_combined_obligation'] for m in r['shared_workforce']['months']))
            self.assertEqual(r['shared_workforce']['inputs']['outside_minutes_per_job'],120)
            self.assertFalse(r['units'])
        self.assertLess(workforce_summary('',strong)['external_resource_cash_cents'],workforce_summary('',self.cases['notice_then_reduce'])['external_resource_cash_cents'])

    def test_unfunded_outside_customer_cannot_create_receipts_or_cancel_required_work(self):
        r=self.cases['unfunded_outside_buyer'];w=r['shared_workforce']
        self.assertEqual((w['cash']['outside_service_invoiced_cents'],w['cash']['outside_service_received_cents'],w['cash']['outside_service_unpaid_cents'],w['cash']['outside_service_due_unpaid_cents']),(960000,0,960000,840000))
        self.assertEqual(sum(m['outside_completed_jobs'] for m in w['months']),160)
        self.assertEqual(next(a['cash_cents'] for a in r['closing_treasury']['actors'] if a['actor_id']==OUTSIDE_BUYER),0)

    def test_funded_customer_still_has_future_due_receivable(self):
        c=self.cases['notice_then_reduce']['shared_workforce']['cash']
        self.assertEqual((c['outside_service_received_cents'],c['outside_service_unpaid_cents'],c['outside_service_due_unpaid_cents']),(840000,120000,0))

    def test_overtime_refusal_spends_no_optional_cash_or_minutes(self):
        reference=self.cases['human_with_funded_overtime'];actor=reference['architecture_execution']['role_entities']['operator']
        mandatory=sum(i['face_cents'] for i in reference['closing_treasury']['invoices'] if i['payer']==actor and i['issued_at']['month']==0 and i['due_at']=={'month':0,'phase':3})
        x=copy.deepcopy(workforce_worlds()['human_with_funded_overtime']);x['execution']['architecture']['role_opening_cash_cents']={'customer':0,'operator':mandatory+95999}
        r=run_workforce_case(x);m=r['shared_workforce']['months'][0]
        self.assertTrue(m['operational']);self.assertEqual(m['overtime_requested_minutes'],960)
        self.assertEqual((m['overtime_paid_minutes'],m['overtime_cash_paid_cents']),(0,0));self.assertEqual(m['overtime_block_reason'],'unfunded_optional_overtime')
        invoice=next(i for i in r['closing_treasury']['invoices'] if i['invoice_id']==m['overtime_invoice_id'])
        self.assertEqual((invoice['paid_cents'],invoice['cancelled_cents'],invoice['outstanding_cents']),(0,96000,0))
        self.assertFalse(m['complete_combined_obligation']);self.assert_conserved(r)

    def test_no_staff_funding_produces_no_free_worker_time(self):
        x=copy.deepcopy(workforce_worlds()['human_with_funded_overtime']);x['execution']['architecture']['role_opening_cash_cents']={'customer':0,'operator':0}
        r=run_workforce_case(x);m=r['shared_workforce']['months'][0]
        self.assertFalse(m['operational']);self.assertEqual(m['worker_budget_minutes'],0)
        self.assertEqual(m['outside_completed_jobs'],0);self.assertEqual(rational(m['accepted_cleaning_zones']),0)
        self.assertEqual(m['staff_commitment_cents'],400000);self.assertEqual(m['staff_cash_paid_cents'],0)
        self.assertIsNone(r['shared_workforce']['notice_issued_month']);self.assert_conserved(r)

    def test_all_saved_worlds_replay_and_ignore_derived_outcomes(self):
        for name,original in self.cases.items():
            saved=copy.deepcopy(original);saved['months']=[];saved['shared_workforce']['months']=[];saved['shared_workforce']['cash']={};saved['closing_treasury']={};saved['case_hash']='forged'
            self.assertEqual(replay_workforce_case(saved),original,name)

    def test_four_legal_architectures_keep_cash_and_crew_conservation(self):
        for name in ('integrated_oem','licensed_independent','open_adapted','model_led_operator'):
            r=run_workforce_case({'execution':{'architecture':{'architecture_id':name}}});self.assert_conserved(r)
            self.assertEqual(r['architecture_execution']['consolidation']['unclassified_boundary_cash_cents'],0)

    def test_unmet_past_service_blocks_notice_and_future_time_does_not_backfill(self):
        r=run_workforce_case({'workforce':{'outside_jobs_by_month':[200,20,20,20,20,20,20,20],'overtime_minutes_per_month':0}})
        w=r['shared_workforce'];self.assertFalse(w['months'][0]['complete_combined_obligation'])
        self.assertEqual((w['notice_issued_month'],w['notice_effective_month']),(2,4))
        self.assertTrue(w['months'][1]['complete_combined_obligation'])
        self.assertGreater(w['months'][0]['outside_unserved_jobs'],0)
        self.assertEqual(w['months'][1]['outside_required_jobs'],20)

    def test_malformed_inputs_identity_and_cash_mismatch_fail_closed(self):
        for x in ([],{'unexpected':1},{'workforce':None},{'execution':None},{'workforce':{'target_blocks':-1}},
                  {'workforce':{'notice_delay_months':0}},{'workforce':{'outside_jobs_by_month':[20]}},
                  {'workforce':{'overtime_minutes_per_month':True}},{'workforce':{'opening_blocks':3}},
                  {'workforce':{'outside_minutes_per_job':0}}):
            with self.assertRaises((ValueError,TypeError)):run_workforce_case(x)
        saved=copy.deepcopy(self.cases['notice_then_reduce']);saved['shared_workforce']['inputs']['outside_buyer_opening_cash_cents']+=1
        with self.assertRaises(ValueError):replay_workforce_case(saved)

    def test_seeded_competing_work_and_capacity_adversaries(self):
        rng=random.Random(35)
        for _ in range(5):
            r=run_workforce_case({'workforce':{'outside_jobs_by_month':[rng.randrange(0,61) for _ in range(8)],
                'overtime_minutes_per_month':rng.randrange(0,2500),'robot_handling_minutes_per_zone':rng.randrange(0,25),
                'attention_minutes_per_supported_unit':rng.randrange(0,241),'notice_delay_months':rng.randrange(1,5)}})
            self.assert_conserved(r)

    def test_unrealized_notice_and_zero_guaranteed_blocks_remain_explicit(self):
        future=run_workforce_case({'workforce':{'notice_delay_months':10}})['shared_workforce']
        self.assertEqual(future['notice_effective_month'],11);self.assertEqual(future['cash']['staff_paid_cents'],3200000)
        zero=run_workforce_case({'workforce':{'target_blocks':0}});self.assert_conserved(zero)
        self.assertTrue(any(m['staff_commitment_cents']==0 for m in zero['shared_workforce']['months']))
        self.assertFalse(all(m['complete_combined_obligation'] for m in zero['shared_workforce']['months']))

    def test_catalog_is_small_and_has_current_source_identity(self):
        data=workforce_catalog();self.assertEqual(set(data['cases']),{'notice_then_reduce'})
        self.assertEqual(len(data['summary']),9);self.assertIn('model/shared_workforce.py',data['source_sha256'])


if __name__=='__main__':unittest.main()
