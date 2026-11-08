import copy
from dataclasses import replace
from fractions import Fraction
import random
import unittest

from model.asset_recovery import (RecoveryPolicy,_RecoveryEnterprise,recovery_case_inputs,
    run_asset_recovery,run_recovery_case,replay_asset_recovery)
from model.calendar_bridge import run_bridged_enterprise,rational
from model.monthly_deployment import RecoveryTransfer,run_monthly


def operator(row,name):return next(x for x in row['operators'] if x['operator_id']==name)
def sold(r):return [e for e in r['asset_recovery']['events'] if e['action']=='asset_sold']
def invoice(r,category):return [x for x in r['closing_treasury']['invoices'] if x['category']==category]


class AssetRecovery(unittest.TestCase):
    def test_disabled_policy_preserves_complete_physical_and_treasury_execution(self):
        p,t,cs,e,f,b,policy=recovery_case_inputs({'inherited_engineering_cents':0})
        old=run_bridged_enterprise(p,t,cs,e,f,b)
        new=run_asset_recovery(p,t,cs,e,f,b,replace(policy,enabled=False))
        for key in ('plan','months','units','events','opening_treasury','closing_treasury','calendar_bridge'):
            self.assertEqual(old[key],new[key],key)
        self.assertEqual(old['enterprise'],new['enterprise'])

    def test_same_unit_leaves_old_service_then_qualifies_at_buyer(self):
        r=run_recovery_case();uid='opening-installed-entrant-1'
        self.assertEqual([u['unit_id'] for u in r['units']],[uid])
        rows=r['asset_recovery']['months']
        self.assertEqual([(x['physical_state'],x['title_owner'],x['supported']) for x in rows[:4]],
            [('installed','entrant',True),('transit','incumbent',False),('transit','incumbent',False),('installed','incumbent',True)])
        self.assertEqual(r['months'][1]['flows']['relocated'],1)
        self.assertEqual(r['months'][1]['closing_stock']['installed'],0)
        for m in (1,2):
            self.assertTrue(all(not o['supported_unit_ids'] for o in r['months'][m]['outputs']))
        self.assertEqual(r['months'][3]['flows']['commissioned'],1)
        self.assertEqual(operator(r['enterprise']['months'][3],'entrant')['robot_delivered_units'],{'numerator':'0','denominator':'1'})

    def test_sale_cash_does_not_repay_debt_in_an_already_closed_phase(self):
        r=run_recovery_case();a=r['asset_recovery']['months']
        self.assertEqual(a[1]['seller_cash_cents'],2_000_000)
        self.assertTrue(a[1]['seller_defaulted']);self.assertGreater(a[1]['seller_principal_claim_cents'],0)
        self.assertFalse(a[2]['seller_defaulted']);self.assertEqual(a[2]['seller_principal_claim_cents'],0)
        self.assertTrue(all(x['title_owner']!='capital_lender' for x in a))

    def test_nonowner_default_cannot_sell_a_lessors_asset(self):
        r=run_recovery_case({'source_arrangement':'lease'})
        self.assertFalse(sold(r));self.assertEqual(r['asset_recovery']['events'][0]['reason'],'seller_does_not_own_unit')
        self.assertTrue(all(x['title_owner']=='lessor' for x in r['asset_recovery']['months']))
        self.assertGreater(sum(i['face_cents'] for i in invoice(r,'lease_rent')),0)
        self.assertTrue(all(i['paid_cents']==0 for i in invoice(r,'asset_recovery_purchase')))

    def test_release_and_transfer_require_distinct_explicit_permissions(self):
        for key,reason in [('release_authorized','old_site_release_not_authorized'),('transfer_rights','asset_and_configuration_transfer_not_permitted')]:
            r=run_recovery_case(recovery_inputs={key:False})
            self.assertFalse(sold(r));self.assertEqual(r['asset_recovery']['events'][0]['reason'],reason)
            self.assertTrue(all(i['cancelled_cents']==i['face_cents'] for i in invoice(r,'asset_recovery_purchase')))

    def test_purchase_and_initial_relocation_are_atomic_at_exact_cent_boundary(self):
        short=run_recovery_case({'buyer_cash_cents':1_971_399})
        exact=run_recovery_case({'buyer_cash_cents':1_971_400})
        self.assertEqual(short['asset_recovery']['events'][0]['buyer_available_cents'],2_099_999)
        self.assertEqual(sold(exact)[0]['buyer_available_cents'],2_100_000)
        self.assertFalse(sold(short));self.assertEqual(len(sold(exact)),1)
        for category in ('asset_recovery_purchase','asset_recovery_relocation'):
            self.assertEqual(sum(i['paid_cents'] for i in invoice(short,category)),0)
        self.assertEqual(short['asset_recovery']['months'][1]['title_owner'],'entrant')
        # No commissioning or support is delivered in the sale month. Future
        # receipts can fund the separately priced later installation.
        self.assertEqual(exact['months'][1]['closing_cash_cents']['incumbent'],0)
        self.assertFalse(exact['asset_recovery']['months'][1]['supported'])

    def test_later_failed_qualification_retains_sale_and_stranded_asset(self):
        r=run_recovery_case(recovery_inputs={'qualification_eligible':False})
        self.assertEqual(len(sold(r)),1)
        self.assertEqual(r['asset_recovery']['months'][-1]['physical_state'],'transit')
        self.assertEqual(r['asset_recovery']['months'][-1]['title_owner'],'incumbent')
        self.assertEqual(r['asset_recovery']['cash']['purchase_transfer_cents'],2_000_000)
        self.assertEqual(r['asset_recovery']['cash']['relocation_resource_cents'],100_000)
        self.assertTrue(any(e['reason']=='buyer_site_configuration_not_qualified' for e in r['events']))

    def test_physical_capacity_and_horizon_do_not_become_support(self):
        r=run_recovery_case({'commissioning_slots':0})
        self.assertEqual(len(sold(r)),1);self.assertEqual(r['units'][0]['status'],'transit')
        r=run_recovery_case(recovery_inputs={'relocation_months':9})
        self.assertEqual(r['units'][0]['ready_month'],10);self.assertEqual(r['units'][0]['status'],'transit')
        r=run_recovery_case({'shipping_slots':0})
        self.assertFalse(sold(r));self.assertEqual(r['asset_recovery']['events'][0]['reason'],'no_relocation_shipping_slot')

    def test_relocation_uses_the_same_shipping_slot_as_new_hardware(self):
        p,t,cs,e,f,b,policy=recovery_case_inputs()
        p=replace(p,opening_finished=1,shipping_slots=(0,1,1,1,1,1,1,1),support_slots=(5,)*8,
            operators=tuple(replace(o,requested_additions=1 if o.operator_id=='incumbent' else 0) for o in p.operators))
        r=run_asset_recovery(p,t,cs,e,f,b,policy)
        self.assertEqual(r['months'][1]['flows']['relocated'],1)
        self.assertEqual(r['months'][1]['flows']['shipped'],0)
        self.assertTrue(any(x['action']=='ship' and x['at']['month']==1 and x['reason']=='shipping_slots' for x in r['events']))

    def test_low_price_does_not_discharge_remaining_credit(self):
        r=run_recovery_case(recovery_inputs={'price_cents':300_000})
        self.assertEqual(len(sold(r)),1)
        self.assertGreater(r['finance']['consolidation']['closing_principal_claim_cents'],0)
        self.assertTrue(r['asset_recovery']['months'][-1]['seller_defaulted'])
        self.assertTrue(r['asset_recovery']['months'][-1]['supported'])

    def test_customer_assignments_and_paid_staff_do_not_move_with_the_asset(self):
        sold_case=run_recovery_case();retained=run_recovery_case(recovery_inputs={'enabled':False})
        for a,b in zip(sold_case['enterprise']['months'],retained['enterprise']['months']):
            for pool in ('baseline','unmet','new'):self.assertEqual(a['pools'][pool]['assignments'],b['pools'][pool]['assignments'])
        for name in ('incumbent','entrant'):
            a=next(x for x in sold_case['enterprise']['inputs']['businesses'] if x['operator_id']==name)
            b=next(x for x in retained['enterprise']['inputs']['businesses'] if x['operator_id']==name)
            self.assertEqual(a['human_staff_cents_by_month'],b['human_staff_cents_by_month'])

    def test_competent_human_buyer_can_have_no_incremental_accepted_service(self):
        a=run_recovery_case({'buyer_full_human_capacity':True})
        b=run_recovery_case({'buyer_full_human_capacity':True},{'enabled':False})
        self.assertEqual(sum(rational(operator(m,'incumbent')['total_delivered_units']) for m in a['enterprise']['months']),4000)
        self.assertEqual([operator(m,'incumbent')['total_delivered_units'] for m in a['enterprise']['months']],
                         [operator(m,'incumbent')['total_delivered_units'] for m in b['enterprise']['months']])
        self.assertGreater(a['asset_recovery']['cash']['purchase_transfer_cents'],0)

    def test_interest_and_claims_reconcile_with_funded_recovery(self):
        r=run_recovery_case({'monthly_rate_basis_points':100});c=r['finance']['consolidation']
        self.assertGreater(c['interest_cash_cents'],0)
        self.assertEqual(c['loan_draw_cash_cents']-c['principal_recovery_cash_cents'],c['closing_principal_claim_cents'])
        self.assertEqual(c['unclassified_other_boundary_cash_cents'],0)

    def test_exact_replay_ignores_tampered_saved_outcomes(self):
        r=run_recovery_case();saved=copy.deepcopy(r)
        saved['asset_recovery']['cash']['purchase_transfer_cents']=1
        saved['units']=[];saved['case_hash']='not trusted'
        self.assertEqual(replay_asset_recovery(saved),r)

    def test_invalid_terms_and_a_nondefaulted_owner_do_not_create_a_sale(self):
        for kwargs in ({'price_cents':0},{'relocation_months':0},{'offer_month':True},{'transfer_rights':1}):
            with self.assertRaises(ValueError):RecoveryPolicy(**kwargs)
        with self.assertRaises(ValueError):run_recovery_case({'unknown':1})
        for invalid in (None,[],{'schema_version':'monthly-deployment/0.9'},
                        {'schema_version':'monthly-deployment/0.9','enterprise':{'inputs':None}}):
            with self.assertRaises(ValueError):replay_asset_recovery(invalid)
        for invalid in ({'policy':None},{'policy':[]},{'buyer_full_human_capacity':1}):
            with self.assertRaises(ValueError):run_recovery_case(invalid)
        r=run_recovery_case({'seller_cash_cents':5_000_000})
        self.assertFalse(sold(r));self.assertEqual(r['asset_recovery']['events'][0]['reason'],'seller_not_in_current_debt_default')

    def test_core_rejects_duplicate_or_mislabelled_paid_transfers(self):
        for mode in ('duplicate','wrong_invoice'):
            class Invalid(_RecoveryEnterprise):
                def recovery_transfers(self,*args):
                    t,moves=super().recovery_transfers(*args)
                    if moves:
                        if mode=='duplicate':moves=moves*2
                        else:moves=(replace(moves[0],purchase_invoice_id=moves[0].relocation_invoice_id,relocation_invoice_id=moves[0].purchase_invoice_id),)
                    return t,moves
            p,t,cs,e,f,b,rp=recovery_case_inputs()
            with self.assertRaises(ValueError):run_monthly(p,t,commercial=Invalid(p,cs,t,e,f,b,rp))

    def test_seeded_physical_demand_and_all_actor_cash_conservation(self):
        rng=random.Random(7228)
        for _ in range(20):
            r=run_recovery_case({'buyer_cash_cents':rng.randint(1,25)*1_000_000,'monthly_rate_basis_points':rng.choice([0,50,100])},
                {'price_cents':rng.randint(1,30)*100_000,'relocation_months':rng.randint(1,10),'qualification_eligible':rng.choice([True,False])})
            self.assertEqual(sum(x['cash_cents'] for x in r['opening_treasury']['actors']),sum(x['cash_cents'] for x in r['closing_treasury']['actors']))
            self.assertEqual(len(r['units']),1)
            for m in r['months']:
                self.assertEqual(sum(m['closing_stock'].values()),1)
                self.assertLessEqual(sum(o['supported_units'] for o in m['outputs']),1)
            for m in r['enterprise']['months']:
                self.assertLessEqual(rational(m['total_delivered_units']),900)
            self.assertEqual(r['finance']['consolidation']['unclassified_other_boundary_cash_cents'],0)


if __name__=='__main__':unittest.main()
