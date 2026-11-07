"""Dated finance changes actual execution; preserve cash, claims and old worlds."""
from dataclasses import replace
from fractions import Fraction
import json
import random
import unittest

from model.enterprise_finance import (FinancePlan, TermLoan, finance_artifact,
    financed_case_inputs, replay_financed_enterprise, run_financed_case, run_financed_enterprise)
from model.monthly_enterprise import reference_inputs, run_enterprise
from model.treasury import Account, Moment


def actor(r, name): return next(a for a in r['closing_treasury']['actors'] if a['actor_id']==name)
def op(r, month, name='entrant'):
    return next(x for x in r['enterprise']['months'][month]['operators'] if x['operator_id']==name)
def q(x): return Fraction(**x)


class FinanceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.artifact=finance_artifact();cls.cases=cls.artifact['cases']

    def test_empty_finance_preserves_existing_execution(self):
        inputs=reference_inputs()
        old=run_enterprise(*inputs);new=run_financed_enterprise(*inputs,FinancePlan())
        for key in ('plan','months','units','events','opening_treasury','closing_treasury','unshipped_requested_additions'):
            self.assertEqual(old[key],new[key],key)
        for section in ('commercial','enterprise'):
            self.assertEqual({k:v for k,v in old[section].items() if k!='limits'},
                             {k:v for k,v in new[section].items() if k!='limits'})

    def test_loan_draw_is_funded_cash_not_commitment_or_sales(self):
        r=self.cases['term_reference'];c=r['finance']['consolidation']
        draws=[e for e in r['closing_treasury']['events'] if e['kind']=='credit_draw']
        self.assertEqual(len(draws),1);self.assertEqual(draws[0]['settled_cents'],2_500_000)
        self.assertEqual(sum(p['delta_cents'] for p in draws[0]['postings']),0)
        self.assertEqual(actor(r,'capital_lender')['cash_cents'],10_000_000-2_500_000+c['principal_recovery_cash_cents']+c['interest_cash_cents'])
        self.assertFalse(c['loan_principal_is_revenue'])
        self.assertEqual(c['unclassified_other_boundary_cash_cents'],0)

    def test_unfunded_lender_creates_no_principal_interest_or_service(self):
        r=self.cases['lender_unfunded'];c=r['finance']['consolidation']
        self.assertEqual(c['loan_draw_cash_cents'],0)
        self.assertEqual(c['closing_principal_claim_cents'],0)
        self.assertEqual(c['interest_cash_cents'],0)
        self.assertEqual(sum(x['rounded_interest_cents'] for x in r['finance']['interest_lines']),0)
        self.assertTrue(all(q(op(r,m)['total_delivered_units'])==0 for m in range(8)))
        self.assertEqual(r['finance']['events'][0]['reason'],'lender_cash_insufficient')

    def test_draw_delay_cannot_pay_earlier_obligations(self):
        r=self.cases['delayed_draw']
        self.assertEqual([x['rounded_interest_cents'] for x in r['finance']['interest_lines'][:3]],[0,0,0])
        self.assertEqual(r['finance']['events'][0]['at'],{'month':2,'phase':2})
        self.assertTrue(all(not op(r,m)['operational'] for m in (0,1)))
        self.assertTrue(all(e['at']['month']>=2 for e in r['closing_treasury']['events']
            if e['kind']=='credit_draw' and e['settled_cents']))

    def test_interest_arrears_basis_and_rounding_are_explicit(self):
        r=self.cases['term_reference'];lines=r['finance']['interest_lines']
        self.assertEqual([x['rounded_interest_cents'] for x in lines],[0]+[25_000]*7)
        small=run_financed_case({'loan_cents':1,'monthly_rate_basis_points':5000})['result']
        self.assertEqual(small['finance']['interest_lines'][1]['exact_interest_cents'],{'numerator':1,'denominator':2})
        self.assertEqual(small['finance']['interest_lines'][1]['rounded_interest_cents'],1)
        self.assertEqual(small['closing_treasury']['credits'][0]['drawn_cents'],1)

    def test_maturity_halts_actual_service_and_retains_claims_assets_and_demand(self):
        r=self.cases['early_maturity_cash_recovery']
        self.assertEqual(r['finance']['first_debt_default_month']['entrant'],3)
        self.assertEqual(q(op(r,2)['total_delivered_units']),25)
        self.assertEqual(q(op(r,3)['total_delivered_units']),0)
        self.assertEqual(op(r,3)['assigned_units']['baseline'],70)
        self.assertTrue(any(u['operator_id']=='entrant' and u['status']=='installed' for u in r['units']))
        self.assertEqual(r['finance']['consolidation']['closing_principal_claim_cents'],1_960_000)
        self.assertGreater(r['finance']['consolidation']['closing_interest_claim_cents'],0)
        self.assertTrue(all(not m['assets_sold_or_repossessed'] for m in r['finance']['months']))

    def test_cash_recovery_does_not_manufacture_cash_or_erase_unpaid_principal(self):
        r=self.cases['early_maturity_cash_recovery'];c=r['finance']['consolidation']
        self.assertEqual(c['principal_recovery_cash_cents'],540_000)
        self.assertEqual(c['loan_draw_cash_cents'],c['principal_recovery_cash_cents']+c['closing_principal_claim_cents'])
        payments=[e for e in r['closing_treasury']['events'] if e['kind']=='principal_repay']
        self.assertEqual(sum(e['settled_cents'] for e in payments),540_000)
        self.assertTrue(all(e['at']['month']>=3 for e in payments))

    def test_funded_cure_restarts_only_the_declared_policy(self):
        cure=self.cases['early_maturity_funded_cure'];stop=self.cases['permanent_stop_after_cure']
        for r in (cure,stop):
            self.assertEqual(r['finance']['consolidation']['closing_principal_claim_cents'],0)
            self.assertEqual(r['finance']['consolidation']['closing_interest_claim_cents'],0)
            self.assertEqual(r['finance']['consolidation']['principal_recovery_cash_cents'],2_500_000)
            self.assertEqual(next(e for e in r['finance']['events'] if e['action']=='debt_cured')['at']['month'],5)
        self.assertEqual(q(op(cure,5)['total_delivered_units']),100)
        self.assertEqual(q(op(stop,5)['total_delivered_units']),0)
        self.assertEqual(cure['units'],stop['units'])

    def test_payment_priority_changes_recovery_not_total_money(self):
        operations=self.cases['early_maturity_cash_recovery'];debt=self.cases['debt_priority']
        self.assertEqual(operations['finance']['consolidation']['principal_recovery_cash_cents'],540_000)
        self.assertEqual(debt['finance']['consolidation']['principal_recovery_cash_cents'],915_000)
        for r in (operations,debt):
            self.assertEqual(sum(a['cash_cents'] for a in r['closing_treasury']['actors']),
                             sum(a['cash_cents'] for a in r['opening_treasury']['actors']))

    def test_full_or_nothing_repayment_preserves_whole_claim(self):
        r=self.cases['principal_full_or_nothing']
        self.assertEqual(r['finance']['consolidation']['principal_recovery_cash_cents'],0)
        self.assertEqual(r['finance']['consolidation']['closing_principal_claim_cents'],2_500_000)
        self.assertGreater(r['months'][3]['closing_cash_cents']['entrant'],0)

    def test_maturity_outside_horizon_is_a_liability_not_free_funding(self):
        r=self.cases['maturity_beyond_horizon'];last=r['finance']['months'][-1]['loans'][0]
        self.assertEqual(last['principal_due_cents'],0)
        self.assertEqual(last['principal_outstanding_cents'],2_500_000)
        self.assertEqual(r['finance']['first_debt_default_month'],{})
        self.assertGreater(q(op(r,7)['total_delivered_units']),0)

    def test_reinvestment_reserve_gates_real_paid_start_without_output_premium(self):
        funded=self.cases['reinvestment_funded_candidate'];reserve=self.cases['reinvestment_reserve_blocks']
        self.assertEqual(sum(m['flows']['started'] for m in funded['months']),6)
        self.assertEqual(sum(m['flows']['started'] for m in reserve['months']),5)
        self.assertEqual(actor(reserve,'manufacturer')['cash_cents']-actor(funded,'manufacturer')['cash_cents'],-3_600_000)
        self.assertEqual([m['total_delivered_units'] for m in funded['enterprise']['months']],
                         [m['total_delivered_units'] for m in reserve['enterprise']['months']])
        self.assertTrue(any(e['reason']=='reinvestment_cash_reserve' for e in reserve['events']))

    def test_paying_maturity_is_not_the_same_as_funding_service_one_cent_boundary(self):
        debt=self.cases['maturity_paid_service_unfunded']
        below=self.cases['maturity_service_one_cent_short'];at=self.cases['maturity_and_service_funded']
        for r in (debt,below,at):
            self.assertEqual(r['finance']['consolidation']['closing_principal_claim_cents'],0)
            self.assertEqual(r['finance']['first_debt_default_month'],{})
        self.assertEqual(q(op(debt,7)['total_delivered_units']),0)
        self.assertEqual(q(op(below,7)['total_delivered_units']),0)
        self.assertEqual(actor(below,'entrant')['cash_cents'],9_999)
        self.assertEqual(q(op(at,7)['total_delivered_units']),30)
        self.assertEqual(actor(at,'entrant')['cash_cents'],0)
        self.assertEqual(below['units'],at['units'])

    def test_new_cases_replay_exactly_and_ignore_tampered_outputs(self):
        for r in self.cases.values():
            saved=json.loads(json.dumps(r));saved['months'][0]['closing_cash_cents']['entrant']=99999999
            self.assertEqual(replay_financed_enterprise(saved),r)

    def test_seeded_worlds_conserve_cash_principal_demand_and_supported_output(self):
        rng=random.Random(142601)
        for _ in range(24):
            draw=rng.randrange(4)
            x={'entrant_cash_cents':rng.randrange(0,4_000_000),'loan_cents':rng.randrange(1,4_000_000),
               'lender_cash_cents':rng.randrange(0,5_000_000),'draw_month':draw,
               'maturity_month':rng.randrange(draw+1,13),'monthly_rate_basis_points':rng.randrange(501),
               'default_policy':rng.choice(['suspend_until_cured','stop_permanently']),
               'payment_priority':rng.choice(['operations_then_debt','debt_then_operations']),
               'delayed_receipts':bool(rng.randrange(2))}
            r=run_financed_case(x)['result'];c=r['finance']['consolidation']
            self.assertEqual(c['loan_draw_cash_cents']-c['principal_recovery_cash_cents'],c['closing_principal_claim_cents'])
            self.assertEqual(c['unclassified_other_boundary_cash_cents'],0)
            self.assertEqual(sum(a['cash_cents'] for a in r['opening_treasury']['actors']),sum(a['cash_cents'] for a in r['closing_treasury']['actors']))
            self.assertTrue(all(a['available_cents']>=0 for a in r['closing_treasury']['actors']))
            for m in r['enterprise']['months']:
                self.assertLessEqual(q(m['total_delivered_units']),1300)
                self.assertEqual(q(m['total_delivered_units']),sum(q(o['total_delivered_units']) for o in m['operators']))
                for o in m['operators']:
                    self.assertLessEqual(q(o['robot_delivered_units']),q(o['robot_capacity_units']))

    def test_two_loans_with_related_ids_keep_interest_separate(self):
        p,t,c,e=reference_inputs();t=replace(t,accounts=t.accounts+(Account('capital',10_000_000),))
        f=FinancePlan((TermLoan('A','capital','entrant',100,0,9,1,2),TermLoan('A:1','capital','entrant',200,0,9,1,4)))
        r=run_financed_enterprise(p,t,c,e,f)
        rows=r['finance']['months'][-1]['loans']
        self.assertEqual([x['interest_accrued_cents'] for x in rows],[350,350])

    def test_lessor_default_blocks_purchase_without_taking_customer_title(self):
        p,t,c,e=reference_inputs();t=replace(t,accounts=t.accounts+(Account('capital',1_000_000),))
        # Lessor collects installed-asset rent before debt service. Include those
        # real receipts: interest plus matured principal exceeds the funded cash.
        f=FinancePlan((TermLoan('lessor','capital','lessor',1_000_000,0,1,1,1),))
        t=replace(t,accounts=tuple(replace(a,opening_cash_cents=100) if a.actor_id=='lessor' else a for a in t.accounts))
        r=run_financed_enterprise(p,t,c,e,f)
        self.assertIn('lessor',r['finance']['first_debt_default_month'])
        self.assertFalse(any(e['action']=='ship' and e['status']=='completed' for e in r['events']))
        self.assertTrue(any(e.get('reason')=='asset_funder_debt_default_policy' for e in r['commercial']['events']))

    def test_invalid_inputs_and_unserviced_opening_credit_fail_closed(self):
        for x in ({'loan_cents':True},{'monthly_rate_basis_points':-1},{'draw_month':3,'maturity_month':3},
                  {'default_policy':'erase_debts'},{'lender_cash_cents':None},{'extra_unknown':1}):
            with self.assertRaises(ValueError):financed_case_inputs(x)
        p,t,c,e=reference_inputs();t=replace(t,accounts=t.accounts+(Account('capital',100),))
        t=t.authorize_credit('opening-auth','opening-credit','capital','entrant',100,Moment(0,1),
            Moment(0,2),Moment(1,2),Moment(2,3),provenance='synthetic_test')
        with self.assertRaisesRegex(ValueError,'Opening credits'):run_financed_enterprise(p,t,c,e,FinancePlan())


if __name__=='__main__':unittest.main()
