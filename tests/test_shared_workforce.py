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
        self.assertEqual(len(data['summary']),18);self.assertIn('model/shared_workforce.py',data['source_sha256'])

    def test_zero_purchase_floor_preserves_the_existing_execution(self):
        a=run_workforce_case();b=run_workforce_case({'fallback':{}})
        b.pop('fallback_reserve');a.pop('case_hash');b.pop('case_hash')
        self.assertEqual(a,b)

    def test_purchase_floor_preserves_both_services_but_retains_sunk_manufacture(self):
        a,b=(self.cases[k] for k in ('tight_site_no_reserve','tight_site_purchase_reserve'))
        x,y=(workforce_summary('',r) for r in (a,b))
        self.assertEqual((x['complete_months'],rational(x['cleaning_zones']),x['outside_jobs']),(7,3530,238))
        self.assertEqual((y['complete_months'],rational(y['cleaning_zones']),y['outside_jobs']),(8,4000,240))
        self.assertEqual((x['overtime_paid_cents'],y['overtime_paid_cents']),(336000,448000))
        self.assertEqual(a['shared_workforce']['events'],b['shared_workforce']['events'])
        for r in (a,b):
            self.assertEqual(r['fallback_reserve']['outcomes']['manufactured_units'],2)
            self.assertEqual(sum(i['paid_cents'] for i in r['closing_treasury']['invoices'] if i['category']=='start'),7200000)
            self.assertFalse(r['fallback_reserve']['reserve_is_expense'])
            self.assertFalse(r['fallback_reserve']['reserve_is_escrow'])
        outcomes=b['fallback_reserve']['outcomes'];self.assertEqual(outcomes['closing_oem_finished_units'],2)
        self.assertEqual(outcomes['purchased_units'],0)
        self.assertEqual(outcomes['actor_closing_cash_cents']['arch:oem'],12800000)
        self.assertEqual(a['fallback_reserve']['outcomes']['actor_closing_cash_cents']['arch:oem'],18790000)
        self.assertTrue(all(x['title_owner']=='arch:oem' for x in b['commercial']['months'][-1]['assets'] if x['physical_state']=='finished'))

    def test_exact_one_cent_purchase_switch_is_not_an_optimal_future_reserve(self):
        base=workforce_worlds()['model_operator_purchase_reserve']
        cases=[]
        for floor in (3841816,3841817):
            x=copy.deepcopy(base);x['fallback']['purchase_floor_cents']=floor;cases.append(run_workforce_case(x))
        at,above=cases;ad=at['fallback_reserve']['purchase_decisions'][0];bd=above['fallback_reserve']['purchase_decisions'][0]
        self.assertEqual(ad['operator_available_if_purchased_cents'],3841816)
        self.assertEqual(ad['status'],'admitted');self.assertEqual(bd['reason'],'operator_fallback_purchase_floor')
        self.assertEqual(bd['group_cash_paid_cents'],0)
        self.assertEqual([workforce_summary('',r)['complete_months'] for r in cases],[7,8])
        for r in cases:self.assert_conserved(r)

    def test_late_floor_does_not_reverse_purchases_notice_or_missed_work(self):
        r=self.cases['model_operator_late_reserve'];old=self.cases['low_model_role_cash']
        self.assertEqual(r['shared_workforce'],old['shared_workforce'])
        self.assertEqual(r['closing_treasury']['actors'],old['closing_treasury']['actors'])
        first=r['fallback_reserve']['purchase_decisions'][0]
        self.assertFalse(first['policy_active']);self.assertEqual(first['status'],'admitted')
        self.assertEqual(r['fallback_reserve']['outcomes']['purchased_units'],1)

    def test_liquidity_does_not_create_worker_capacity_or_supplier_funds(self):
        r=self.cases['tight_site_reserve_without_overtime'];w=r['shared_workforce']
        self.assertEqual(workforce_summary('',r)['complete_months'],4)
        self.assertEqual(sum(m['outside_unserved_jobs'] for m in w['months']),4)
        self.assertGreater(r['fallback_reserve']['outcomes']['actor_closing_cash_cents']['arch:customer_operator'],2000000)
        s=self.cases['unfunded_model_supplier_reserve']
        self.assertEqual(s['fallback_reserve']['outcomes']['supported_unit_months'],0)
        self.assertEqual(s['fallback_reserve']['outcomes']['actor_closing_cash_cents']['arch:model_supplier'],0)
        self.assertEqual(s['shared_workforce']['cash']['overtime_paid_cents'],768000)
        self.assertIsNone(s['shared_workforce']['notice_issued_month'])

    def test_excessive_floor_retains_human_work_and_loses_staffing_option(self):
        a,b=(self.cases[k] for k in ('one_robot_no_reserve','one_robot_excess_reserve'))
        self.assertEqual([workforce_summary('',r)['complete_months'] for r in (a,b)],[8,8])
        self.assertEqual([r['shared_workforce']['cash']['staff_paid_cents'] for r in (a,b)],[2600000,3200000])
        self.assertEqual([r['fallback_reserve']['outcomes']['supported_unit_months'] for r in (a,b)],[20,8])
        self.assertGreater(sum(rational(m['human_cleaning_zones']) for m in b['shared_workforce']['months']),sum(rational(m['human_cleaning_zones']) for m in a['shared_workforce']['months']))
        self.assertIsNone(b['shared_workforce']['notice_issued_month'])

    def test_strong_human_comparator_covers_the_same_surge_at_lower_bounded_outlay(self):
        a,b=(workforce_summary('',self.cases[k]) for k in ('stronger_human_dispatch_surge','tight_site_purchase_reserve'))
        for r in (a,b):self.assertEqual((r['complete_months'],rational(r['cleaning_zones']),r['outside_jobs']),(8,4000,240))
        self.assertEqual(a['external_resource_cash_cents'],5350000)
        self.assertLess(a['external_resource_cash_cents'],b['external_resource_cash_cents'])

    def test_purchase_floor_uses_no_future_work_and_replay_ignores_forged_outcomes(self):
        x=copy.deepcopy(workforce_worlds()['model_operator_purchase_reserve']);a=run_workforce_case(x)
        x['workforce']={'outside_jobs_by_month':[20]*4+[100]*4};b=run_workforce_case(x)
        early=lambda r:[e for e in r['fallback_reserve']['purchase_decisions'] if e['month']<4]
        self.assertEqual(early(a),early(b));self.assertTrue(all(not e['future_actual_work_or_receipts_consulted'] for e in early(a)))
        saved=copy.deepcopy(a);saved['fallback_reserve']['purchase_decisions']=[];saved['fallback_reserve']['outcomes']={'forged':True};saved['fallback_reserve']['months']=[];saved['case_hash']='forged'
        self.assertEqual(replay_workforce_case(saved),a)

    def test_purchase_floor_input_bounds_and_seeded_cash_conservation(self):
        for f in (None,[],{'purchase_floor_cents':True},{'purchase_floor_cents':-1},{'purchase_floor_cents':1000000001},{'active_from_month':37},{'active_from_month':1.5},{'unknown':1}):
            with self.assertRaises((TypeError,ValueError)):run_workforce_case({'fallback':f})
        rng=random.Random(37)
        for _ in range(4):
            r=run_workforce_case({'fallback':{'purchase_floor_cents':rng.randrange(0,40000000),'active_from_month':rng.randrange(0,10)},'workforce':{'outside_jobs_by_month':[rng.randrange(0,61) for _ in range(8)]}})
            self.assert_conserved(r)
            for d in r['fallback_reserve']['purchase_decisions']:
                self.assertEqual(d['operator_available_if_purchased_cents'],d['operator_available_before_cents']-d['candidate_operator_spend_cents'])
                if d['status']=='admitted':self.assertGreaterEqual(d['operator_available_after_cents'],d['required_floor_cents'])
                else:self.assertEqual(d['group_cash_paid_cents'],0)

    def test_reserve_respects_all_legal_actor_mappings_and_unpaid_staff_liability(self):
        for name in ('integrated_oem','licensed_independent','open_adapted','model_led_operator'):
            r=run_workforce_case({'execution':{'architecture':{'architecture_id':name}},'fallback':{'purchase_floor_cents':100000000}})
            self.assert_conserved(r)
            self.assertEqual(r['fallback_reserve']['operator_actor'],r['architecture_execution']['role_entities']['operator'])
            self.assertEqual(r['architecture_execution']['consolidation']['unclassified_boundary_cash_cents'],0)
        r=run_workforce_case({'execution':{'architecture':{'role_opening_cash_cents':{'customer':0,'operator':0}}},'fallback':{'purchase_floor_cents':2000000}})
        self.assert_conserved(r);first=r['shared_workforce']['months'][0]
        self.assertEqual(first['staff_commitment_cents'],400000)
        self.assertEqual(first['staff_unpaid_cents'],400000)
        self.assertEqual(first['worker_budget_minutes'],0)
        self.assertTrue(any(i['category']=='human_staff' and i['outstanding_cents'] for i in r['closing_treasury']['invoices']))


if __name__=='__main__':unittest.main()
