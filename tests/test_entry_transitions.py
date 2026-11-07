"""Share ownership, funded settlement and unchanged service/asset identities."""
import copy
from dataclasses import replace
from fractions import Fraction
import random
import unittest
from model.calendar_bridge import rational
from model.entry_transitions import (BUYER,SELLER,entry_artifact,entry_case_inputs,replay_entry_transition,run_entry_case,run_entry_transition)


class EntryTransitions(unittest.TestCase):
    @classmethod
    def setUpClass(cls):cls.artifact=entry_artifact();cls.cases=cls.artifact['cases']

    def test_share_purchase_and_price_do_not_create_service_or_assets(self):
        base=self.cases['status_quo']
        for name in ('share_acquisition','higher_price_same_operations'):
            r=self.cases[name]
            for key in ('units','events'):self.assertEqual(base[key],r[key])
            for original,changed in zip(base['months'],r['months']):
                self.assertEqual({k:v for k,v in original.items() if k not in ('opening_cash_cents','closing_cash_cents')},
                                 {k:v for k,v in changed.items() if k not in ('opening_cash_cents','closing_cash_cents')})
            self.assertEqual(base['enterprise']['months'],r['enterprise']['months'])
            self.assertEqual(base['commercial']['months'],r['commercial']['months'])
            self.assertEqual(base['entry_transition']['cash']['target_closing_cents'],r['entry_transition']['cash']['target_closing_cents'])

    def test_owner_changes_only_at_funded_closing_and_title_stays_with_lessor(self):
        r=self.cases['share_acquisition'];a=r['entry_transition']
        self.assertEqual([m['ultimate_owners']['incumbent'] for m in a['months']],[SELLER]*2+[BUYER]*6)
        for m in a['months']:
            self.assertEqual(m['target_unit_ids'],a['months'][0]['target_unit_ids'])
            self.assertTrue(all(asset['title_owner']=='lessor' and asset['custodian']=='incumbent' and asset['workflow_authority']=='incumbent' for asset in m['target_asset_contracts']))

    def test_exact_one_cent_closing_boundary_and_atomic_failure(self):
        exact=run_entry_case({'buyer_cash_cents':10_600_000});short=run_entry_case({'buyer_cash_cents':10_599_999})
        self.assertEqual(exact['entry_transition']['close_status'],'closed')
        a=short['entry_transition'];self.assertEqual(a['close_status'],'blocked')
        self.assertEqual(a['cash']['paid_diligence_cents'],100000)
        self.assertEqual(a['cash']['paid_share_price_cents'],0);self.assertEqual(a['cash']['paid_transition_resources_cents'],0)
        self.assertEqual(a['cash']['buyer_closing_cents'],10499999)
        self.assertTrue(all(m['ultimate_owners']['incumbent']==SELLER for m in a['months']))
        self.assertFalse(any(e['kind']=='invoice_payment' and e['settled_cents'] and 'share_consideration' in e['reference_id'] for e in short['closing_treasury']['events']))

    def test_closing_failure_does_not_strand_a_partial_equity_injection(self):
        r=run_entry_case({'buyer_cash_cents':10_600_000,'target_equity_cents':1})
        a=r['entry_transition'];self.assertEqual(a['close_status'],'blocked')
        for key in ('paid_share_price_cents','paid_transition_resources_cents','paid_target_equity_cents'):self.assertEqual(a['cash'][key],0)

    def test_consideration_moves_to_seller_and_is_not_target_working_cash(self):
        r=self.cases['purchase_without_operating_cash'];a=r['entry_transition']
        self.assertEqual(a['close_status'],'closed');self.assertEqual(a['cash']['seller_cash_received_cents'],10000000)
        self.assertEqual(a['cash']['target_closing_cents'],0)
        self.assertEqual(sum(rational(m['total_delivered_units']) for m in r['enterprise']['months']),0)
        self.assertEqual(a['consolidation']['target_cash_swept_to_buyer_cents'],0)

    def test_separate_working_equity_restores_future_not_missed_service(self):
        r=self.cases['funded_target_working_capital'];a=r['entry_transition']
        self.assertEqual(a['cash']['paid_target_equity_cents'],2500000)
        delivered=[rational(m['total_delivered_units']) for m in r['enterprise']['months']]
        self.assertEqual(delivered[:2],[0,0]);self.assertEqual(delivered[2:],[500]*6)
        self.assertEqual(a['cash']['seller_cash_received_cents'],10000000)

    def test_existing_target_liability_survives_share_closing(self):
        r=self.cases['target_liability_retained'];a=r['entry_transition']
        self.assertEqual(a['close_status'],'closed')
        invoice=next(i for i in r['closing_treasury']['invoices'] if i['invoice_id']=='opening-target-payable')
        self.assertEqual((invoice['payer'],invoice['payee'],invoice['face_cents']),('incumbent','enterprise_vendor',3000000))
        self.assertEqual(a['cash']['target_opening_payables_paid_cents']+a['cash']['target_opening_payables_unpaid_cents'],3000000)
        self.assertGreater(a['cash']['target_opening_payables_unpaid_cents'],0)
        self.assertGreater(a['cash']['target_closing_cents'],0)

    def test_preclose_receivables_stay_payable_to_same_company(self):
        r=self.cases['share_acquisition']
        invoices=[i for i in r['closing_treasury']['invoices'] if i['category']=='end_market_sale' and i['issued_at']['month']<2]
        self.assertTrue(invoices);self.assertTrue(all(i['payee']=='incumbent' for i in invoices))
        self.assertFalse(any(i['category']=='end_market_sale' and i['payee'] in (BUYER,SELLER) for i in r['closing_treasury']['invoices']))

    def test_blocked_consent_keeps_ownership_and_prior_diligence_cost(self):
        a=self.cases['consent_not_assumed']['entry_transition']
        self.assertEqual(a['events'][0]['reason'],'assumed_transfer_consent_not_met')
        self.assertEqual(a['cash']['paid_diligence_cents'],100000);self.assertEqual(a['cash']['paid_share_price_cents'],0)
        self.assertTrue(all(m['ultimate_owners']['incumbent']==SELLER for m in a['months']))

    def test_transition_disruption_loses_service_but_retains_fixed_staff(self):
        a=self.cases['share_acquisition'];b=self.cases['transition_interruption']
        self.assertEqual(rational(b['enterprise']['months'][2]['total_delivered_units']),0)
        self.assertEqual(sum(rational(m['total_delivered_units']) for m in a['enterprise']['months'])-sum(rational(m['total_delivered_units']) for m in b['enterprise']['months']),500)
        staff=lambda r:sum(x['staff_commitment_cents'] for m in r['calendar_bridge']['months'] for x in m['human_work'])
        self.assertEqual(staff(a),staff(b));self.assertEqual(staff(a),3200000)
        self.assertEqual(a['units'],b['units'])

    def test_hybrid_growth_is_separate_and_can_survive_failed_acquisition(self):
        a=self.cases['hybrid'];b=self.cases['hybrid_acquisition_fails']
        self.assertEqual(a['entry_transition']['close_status'],'closed');self.assertEqual(b['entry_transition']['close_status'],'blocked')
        self.assertEqual(a['enterprise']['months'],b['enterprise']['months'])
        self.assertEqual(a['units'],b['units'])
        self.assertEqual(b['entry_transition']['cash']['paid_growth_equity_cents'],6000000)
        self.assertFalse(any(e['move']['pool']=='baseline' for e in a['enterprise']['events'] if e['action']=='customer_move'))

    def test_common_opening_buyer_capital_across_four_routes(self):
        for name in ('status_quo','organic_build','share_acquisition','hybrid'):
            self.assertEqual(self.cases[name]['entry_transition']['cash']['buyer_opening_cents'],20000000)
        self.assertEqual(self.cases['share_acquisition']['entry_transition']['cash']['paid_growth_equity_cents'],0)
        self.assertEqual(self.cases['organic_build']['entry_transition']['cash']['paid_share_price_cents'],0)

    def test_extra_internal_growth_equity_can_fund_previously_unserved_work(self):
        a=self.cases['hybrid'];b=self.cases['hybrid_growth_liquidity']
        self.assertEqual(a['units'],b['units'])
        self.assertEqual(a['entry_transition']['cash']['buyer_opening_cents'],b['entry_transition']['cash']['buyer_opening_cents'])
        self.assertEqual(sum(rational(m['total_delivered_units']) for m in a['enterprise']['months']),4717)
        self.assertEqual(sum(rational(m['total_delivered_units']) for m in b['enterprise']['months']),4750)
        self.assertEqual(a['entry_transition']['cash']['buyer_closing_cents']-b['entry_transition']['cash']['buyer_closing_cents'],500000)

    def test_competitive_response_transfers_customers_without_new_demand(self):
        base=self.cases['organic_build'];prompt=self.cases['prompt_incumbent_response'];late=self.cases['delayed_incumbent_response']
        for r in (base,prompt,late):
            self.assertEqual(r['enterprise']['inputs']['market'],base['enterprise']['inputs']['market'])
            self.assertEqual(r['source_sha256'],base['source_sha256'])
        returned=next(e for e in prompt['enterprise']['events'] if e.get('move',{}).get('move_id')=='equal-tech-incumbent-response')
        self.assertEqual(returned['status'],'assigned')
        self.assertEqual(returned['move']['units'],70)

    def test_price_is_fixed_boundary_transfer_not_extra_resource_cost(self):
        a=self.cases['share_acquisition']['entry_transition'];b=self.cases['higher_price_same_operations']['entry_transition']
        self.assertEqual(a['consolidation'],b['consolidation'])
        delta=b['cash']['paid_share_price_cents']-a['cash']['paid_share_price_cents']
        self.assertEqual(delta,5000000)
        self.assertEqual(a['cash']['buyer_closing_cents']-b['cash']['buyer_closing_cents'],delta)
        self.assertEqual(b['cash']['seller_cash_received_cents']-a['cash']['seller_cash_received_cents'],delta)

    def test_complete_replay_and_browser_integral_number_spelling(self):
        for name,r in self.cases.items():
            saved=copy.deepcopy(r);saved['entry_transition']['close_status']='invented';saved['case_hash']='tampered'
            self.assertEqual(replay_entry_transition(saved),r,name)
        saved=copy.deepcopy(self.cases['share_acquisition'])
        saved['calendar_bridge']['inputs']['annual_overrides']={'years':3.0}
        other=copy.deepcopy(saved);other['calendar_bridge']['inputs']['annual_overrides']={'years':3}
        self.assertEqual(replay_entry_transition(saved),replay_entry_transition(other))

    def assert_invariants(self,r):
        self.assertEqual(sum(a['cash_cents'] for a in r['opening_treasury']['actors']),sum(a['cash_cents'] for a in r['closing_treasury']['actors']))
        self.assertEqual(r['entry_transition']['consolidation']['unclassified_boundary_cash_cents'],0)
        self.assertEqual(r['finance']['consolidation']['unclassified_other_boundary_cash_cents'],0)
        self.assertEqual(len(r['units']),len({u['unit_id'] for u in r['units']}))
        for m in r['enterprise']['months']:
            for pool in m['pools'].values():
                self.assertEqual(sum(a['units'] for a in pool['assignments']),pool['recurring_demand_units'])
                self.assertEqual(rational(pool['delivered_units'])+rational(pool['unserved_units']),pool['recurring_demand_units'])
            self.assertLessEqual(rational(m['total_delivered_units']),650)
        for m in r['entry_transition']['months']:self.assertEqual(set(m['ultimate_owners']),{'incumbent','entrant'})

    def test_cash_physical_and_request_conservation_in_reference_worlds(self):
        for r in self.cases.values():self.assert_invariants(r)

    def test_seeded_funding_disruption_and_growth_invariants(self):
        rng=random.Random(1818)
        for _ in range(8):
            r=run_entry_case({'mode':rng.choice(['build','acquire','hybrid']),'buyer_cash_cents':rng.randrange(25_000_000),
                'target_cash_cents':rng.randrange(5_000_000),'target_equity_cents':rng.randrange(3_000_000),
                'disruption_months':rng.randrange(3),'new_robots':rng.randrange(4),'assumed_transfer_consent':bool(rng.randrange(2))})
            self.assert_invariants(r)

    def test_invalid_contract_inputs_fail_visibly(self):
        for x in ({'mode':'asset_sale'},{'buyer_cash_cents':True},{'close_month':8},{'new_robots':5},{'assumed_transfer_consent':1},{'unknown':0}):
            with self.assertRaises((ValueError,TypeError)):run_entry_case(x)
        with self.assertRaises(ValueError):replay_entry_transition({})


if __name__=='__main__':unittest.main()
