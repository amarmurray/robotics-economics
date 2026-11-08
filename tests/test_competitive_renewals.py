"""Conserved service, funded awards, locked prices and cash-window falsifiers."""
import copy
from dataclasses import replace
from fractions import Fraction
import json
from pathlib import Path
import random
import unittest
from model.calendar_bridge import rational
from model.competitive_renewals import (Competition, competitive_case_inputs, replay_competitive_case,
                                       run_competitive_case, run_competitive_renewals)
from model.monthly_enterprise import round_cents


class CompetitiveRenewals(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.cases=json.loads(Path('model/results/competitive_renewals.json').read_text())['cases']

    def entrant(self,r):return next(x for x in r['competition']['outcomes'] if x['operator_id']=='entrant')

    def assert_conserved(self,r):
        self.assertEqual(sum(a['cash_cents'] for a in r['opening_treasury']['actors']),sum(a['cash_cents'] for a in r['closing_treasury']['actors']))
        self.assertEqual(r['finance']['consolidation']['unclassified_other_boundary_cash_cents'],0)
        self.assertEqual(len(r['units']),len({u['unit_id'] for u in r['units']}))
        demand=r['enterprise']['inputs']['market']['baseline_units']
        for month, service in zip(r['competition']['months'],r['enterprise']['months']):
            self.assertEqual(sum(x['units'] for x in month['lots']),demand)
            self.assertEqual(len(month['lots']),len({x['lot_id'] for x in month['lots']}))
            delivered=sum((rational(x['delivered_units']) for x in month['lots']),Fraction())
            self.assertEqual(delivered,rational(service['total_delivered_units']))
            self.assertLessEqual(delivered,demand)
            for lot in month['lots']:
                self.assertEqual(rational(lot['delivered_units'])+rational(lot['unserved_units']),lot['units'])
                self.assertGreaterEqual(rational(lot['unserved_units']),0)
        for event in r['competition']['events']:
            owner=event['to_operator']
            if owner:
                self.assertGreaterEqual(rational(event['available_capacity_before_award'][owner]),event['units'])
                self.assertEqual(event['attempts'][-1]['status'],'funded')
        for invoice in r['closing_treasury']['invoices']:
            if invoice['category'].startswith('competitive_'):
                self.assertEqual(invoice['outstanding_cents'],0)

    def test_reference_and_adverse_worlds_conserve_cash_demand_and_funded_awards(self):
        for r in self.cases.values():self.assert_conserved(r)

    def test_bid_response_changes_commercial_outcome_with_same_physical_execution(self):
        base=self.cases['prompt_response']
        for name in ('no_response','response_month_seven','response_month_ten'):
            r=self.cases[name]
            for key in ('plan','units'):self.assertEqual(base[key],r[key])
            for a,b in zip(base['calendar_bridge']['months'],r['calendar_bridge']['months']):
                self.assertEqual({k:v for k,v in a.items() if k!='human_work'},{k:v for k,v in b.items() if k!='human_work'})
        self.assertIsNone(self.entrant(base)['first_cash_break_even_month'])
        self.assertEqual(self.entrant(self.cases['no_response'])['first_cash_break_even_month'],8)
        self.assertLess(self.entrant(base)['terminal_cash_after_recorded_bills_cents'],0)
        self.assertGreater(self.entrant(self.cases['response_month_ten'])['terminal_cash_after_recorded_bills_cents'],0)

    def test_robot_response_requires_actual_supported_units_not_only_calendar(self):
        r=self.cases['prompt_response'];c=r['competition']
        self.assertEqual(c['incumbent_response_first_month'],2)
        self.assertEqual([m['offers_cents_per_unit']['incumbent'] for m in c['months'][:3]],[2900,2900,2500])
        delayed=self.cases['delayed_procurement']['competition']
        self.assertGreater(delayed['incumbent_response_first_month'],2)

    def test_human_led_comparator_can_protect_service_without_robot_purchase(self):
        r=self.cases['human_led_response']
        self.assertEqual(r['competition']['incumbent_response_first_month'],2)
        self.assertFalse(any(u['operator_id']=='incumbent' for u in r['units']))
        self.assertEqual(sum(rational(m['total_delivered_units']) for m in r['enterprise']['months']),6000)
        self.assertIsNone(self.entrant(r)['first_cash_break_even_month'])

    def test_one_cent_switch_boundary_and_tie_retains_current_provider(self):
        a=self.cases['switch_cost_tie']['competition']['months'][0]
        b=self.cases['one_cent_below_switch_tie']['competition']['months'][0]
        self.assertEqual(sum(x['units'] for x in a['lots'] if x['owner']=='entrant'),0)
        self.assertEqual(sum(x['units'] for x in b['lots'] if x['owner']=='entrant'),100)
        self.assertEqual(50*(2900-2700),10000)

    def test_locked_prices_and_expiry_persist_without_unilateral_repricing(self):
        r=self.cases['six_month_contracts'];c=r['competition']
        self.assertEqual(c['months'][2]['offers_cents_per_unit']['incumbent'],2500)
        for m in c['months'][:6]:
            self.assertEqual({x['price_cents'] for x in m['lots']},{2700,2900})
            self.assertTrue(all(x['expires_month']==6 for x in m['lots']))
        self.assertFalse(any(0<e['month']<6 for e in c['events']))
        self.assertTrue(any(x['price_cents']==2500 for x in c['months'][6]['lots']))

    def test_breach_is_backward_looking_and_no_escape_preserves_unserved_contract(self):
        a=self.cases['breach_allows_exit'];b=self.cases['breach_locks_service']
        breaches=[e for e in a['competition']['events'] if e['prior_service_breach']]
        self.assertTrue(breaches)
        for e in breaches:
            self.assertGreater(e['month'],0)
            lot=next(x for x in a['competition']['months'][e['month']-1]['lots'] if x['lot_id']==e['lot_id'])
            self.assertLess(rational(lot['delivered_units'])*10000,lot['units']*9000)
        self.assertFalse(any(e['prior_service_breach'] for e in b['competition']['events']))
        self.assertGreater(sum(rational(m['total_delivered_units']) for m in a['enterprise']['months']),sum(rational(m['total_delivered_units']) for m in b['enterprise']['months']))

    def test_unfunded_onboarding_has_no_partial_resource_payment(self):
        r=self.cases['onboarding_unfunded'];c=r['competition']
        self.assertEqual(c['operator_onboarding_resource_cash_cents'],0)
        self.assertEqual(c['buyer_switch_resource_cash_cents'],0)
        self.assertTrue(any(a['status']=='unfunded_onboarding' for e in c['events'] for a in e['attempts']))
        self.assertTrue(all(x['owner']=='incumbent' for m in c['months'] for x in m['lots']))
        self.assertFalse(any(i['paid_cents'] for i in r['closing_treasury']['invoices'] if i['category'].startswith('competitive_')))

    def test_buyer_failure_rolls_back_already_possible_onboarding_payment(self):
        p,t,k,e,f,b,c=competitive_case_inputs({'months':8,'competition':{'term_months':6}})
        t=replace(t,accounts=tuple(replace(a,opening_cash_cents=0) if a.actor_id==e.market.buyer_actor else a for a in t.accounts))
        r=run_competitive_renewals(p,t,k,e,f,b,c)
        self.assertTrue(any(a['status']=='unfunded_buyer_switch' for e in r['competition']['events'] for a in e['attempts']))
        self.assertEqual(r['competition']['operator_onboarding_resource_cash_cents'],0)
        self.assertFalse(any(i['paid_cents'] for i in r['closing_treasury']['invoices'] if i['category']=='competitive_onboarding'))
        self.assert_conserved(r)

    def test_unqualified_or_unfunded_staff_cannot_win_awards(self):
        r=self.cases['late_entrant_qualification']
        self.assertTrue(all(x['owner']!='entrant' for m in r['competition']['months'][:4] for x in m['lots']))
        r=run_competitive_case({'months':8,'entrant_cash_cents':0})
        self.assertTrue(all(x['owner']!='entrant' for m in r['competition']['months'] for x in m['lots']))
        self.assertEqual(self.entrant(r)['delivered_zones'],{'numerator':'0','denominator':'1'})

    def test_sum_exact_lot_revenue_then_round_once_and_wait_for_collection(self):
        for r in self.cases.values():
            for invoice in r['enterprise']['invoice_lines']:
                if invoice['category']!='end_market_sale':continue
                lines=[x for x in r['competition']['contract_lines'] if x['month']==invoice['month'] and x['operator_id']==invoice['operator_id']]
                exact=sum((rational(x['accepted_units'])*x['locked_cents_per_unit'] for x in lines),Fraction())
                self.assertEqual(rational(invoice['unrounded_cents']),exact)
                self.assertEqual(invoice['face_cents'],round_cents(exact))
        r=self.cases['short_observation_window']
        self.assertTrue(any(i['outstanding_cents'] for i in r['closing_treasury']['invoices'] if i['category']=='end_market_sale' and i['payee']=='entrant'))
        self.assertIsNone(self.entrant(r)['first_cash_break_even_month'])
        self.assertEqual(self.entrant(self.cases['no_response'])['first_cash_break_even_month'],8)

    def test_equity_and_net_loan_principal_do_not_count_as_operating_recovery(self):
        r=run_competitive_case({'months':8,'loan_cents':1_000_000,'extra_equity_cents':2_000_000,'competition':{'term_months':6}})
        opening=next(x['cash_cents'] for x in r['opening_treasury']['actors'] if x['actor_id']=='entrant')
        for m in r['competition']['months']:
            x=next(x for x in m['operator_cash'] if x['operator_id']=='entrant')
            self.assertEqual(x['cumulative_operating_cash_cents'],x['cash_cents']-opening-x['funded_equity_cents']-x['net_loan_principal_cash_cents'])
            self.assertEqual(x['cash_after_recorded_bills_cents'],x['cumulative_operating_cash_cents']-x['recorded_unpaid_obligations_cents'])
        self.assertGreater(r['competition']['months'][0]['operator_cash'][1]['funded_equity_cents'],0)

    def test_first_crossing_can_reverse_before_observed_stable_recovery(self):
        x=self.cases['prompt_response']['competition']['outcomes'][0]
        self.assertEqual(x['first_cash_break_even_month'],1)
        self.assertEqual(x['cash_break_even_held_through_horizon_month'],5)

    def test_full_replay_ignores_saved_outcomes(self):
        for name in ('prompt_response','breach_locks_service','no_response'):
            r=self.cases[name];saved=copy.deepcopy(r);saved['competition']['outcomes']=[];saved['case_hash']='invented'
            self.assertEqual(replay_competitive_case(saved),r,name)

    def test_invalid_boundaries_and_ambiguous_price_authority_rejected(self):
        for x in ({'months':7},{'months':25},{'months':True},{'competition':None},{'competition':{'breach_exit':1}},
                  {'competition':{'lot_count':0}},{'competition':{'response_mode':'oracle'}},{'unknown':1}):
            with self.assertRaises((ValueError,TypeError)):competitive_case_inputs(x)
        p,t,k,e,f,b,c=competitive_case_inputs({'months':8})
        e=replace(e,businesses=tuple(replace(v,price_cents_per_unit_by_month=(1,)*8) for v in e.businesses))
        with self.assertRaises(ValueError):run_competitive_renewals(p,t,k,e,f,b,c)
        with self.assertRaises(ValueError):replay_competitive_case({})

    def test_seeded_cash_and_contract_stress(self):
        rng=random.Random(2405)
        for _ in range(6):
            r=run_competitive_case({'months':8,'entrant_cash_cents':rng.randrange(4_000_000),
                'support_hours_per_month':rng.randrange(100),'entrant_receipt_lag':rng.randrange(1,5),
                'competition':{'term_months':rng.randrange(2,7),'breach_exit':bool(rng.randrange(2)),
                               'response_after_month':rng.randrange(8)}})
            self.assert_conserved(r)


if __name__=='__main__':unittest.main()
