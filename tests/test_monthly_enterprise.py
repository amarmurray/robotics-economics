"""Common demand, delivered-work billing, cash survival and physical-stock checks."""
from dataclasses import replace
from fractions import Fraction
import hashlib
import json
import unittest

from model.monthly_enterprise import (Business, CustomerMove, EnterprisePlan, Equity, Market,
    enterprise_witnesses, reference_inputs, replay_enterprise, run_enterprise, round_cents)
from model.monthly_commercial import Contract, commercial_witnesses
from model.monthly_deployment import Operator, System, monthly_witnesses
from model.treasury import Account, Treasury


def q(value): return Fraction(**value)


def op(r,month,operator="entrant"):
    return next(x for x in r["enterprise"]["months"][month]["operators"] if x["operator_id"]==operator)


def cash_of(r,actor): return r["months"][-1]["closing_cash_cents"][actor]


def closing_account(t,actor,amount):
    return replace(t,accounts=tuple(replace(a,opening_cash_cents=amount) if a.actor_id==actor else a for a in t.accounts))


class EnterpriseTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls): cls.cases=enterprise_witnesses()

    def test_prior_complete_stage_payloads_preserved(self):
        for f,digest in ((monthly_witnesses,"447ccb1592fe3bdf27f1e0e24a1757749b3caca0d67c63635666c28b2c3ed448"),
                         (commercial_witnesses,"0fc480d239cd93d3efa72d87404d1fff583c543e2eef838e1b2563e807af4921")):
            self.assertEqual(hashlib.sha256(json.dumps(f(),sort_keys=True,separators=(',',':')).encode()).hexdigest(),digest)

    def test_customer_transfer_counts_baseline_once(self):
        r=self.cases['shared_reference'];m=r['enterprise']['months'][3]
        self.assertEqual(q(op(r,3)['total_delivered_units']),100)
        self.assertEqual({k:q(v) for k,v in op(r,3)['served_by_pool'].items()},{'baseline':70,'unmet':20,'new':10})
        self.assertEqual(q(op(r,3,'incumbent')['total_delivered_units']),930)
        self.assertEqual(q(m['total_delivered_units']),1030)
        self.assertEqual(q(m['pools']['baseline']['delivered_units']),1000)
        self.assertEqual(q(m['pools']['unmet']['unserved_units']),180)
        self.assertEqual(q(m['pools']['new']['unserved_units']),90)

    def test_ten_robot_requests_are_only_one_real_assignment(self):
        r=self.cases['shared_reference']
        units=[u for u in r['units'] if u['operator_id']=='entrant']
        self.assertEqual(len(units),1);self.assertEqual(units[0]['commissioned_at'],{'month':2,'phase':4})
        self.assertEqual(q(op(r,2)['robot_capacity_units']),25)
        self.assertEqual(q(op(r,3)['robot_capacity_units']),100)
        self.assertEqual(q(op(r,2)['served_by_pool']['baseline']),Fraction(35,2))
        self.assertEqual(q(r['enterprise']['months'][2]['total_delivered_units']),955)
        self.assertEqual(r['unshipped_requested_additions']['entrant'],9)
        self.assertEqual(r['months'][-1]['closing_stock']['finished'],2)

    def test_failure_does_not_restore_displaced_incumbent_output(self):
        r=self.cases['late_receipts_no_automatic_switchback']
        self.assertEqual([q(r['enterprise']['months'][i]['total_delivered_units']) for i in (3,4,5)],[1030,930,930])
        self.assertEqual(op(r,4)['assigned_units']['baseline'],70)
        self.assertEqual(q(op(r,4)['total_delivered_units']),0)
        self.assertEqual(q(op(r,4,'incumbent')['total_delivered_units']),930)
        self.assertEqual(r['months'][4]['closing_stock']['installed'],5)
        assets=r['commercial']['months'][4]['assets']
        entrant=next(x for x in assets if x['contract_id']=='contract-entrant')
        self.assertEqual(entrant['title_owner'],'lessor');self.assertFalse(entrant['supported'])
        self.assertGreater(r['enterprise']['months'][4]['due_unpaid_by_actor_cents']['entrant'],0)

    def test_explicit_paid_switchback_uses_actual_remaining_capacity(self):
        r=self.cases['late_receipts_explicit_switchback']
        self.assertEqual(q(r['enterprise']['months'][4]['total_delivered_units']),930)
        self.assertEqual(q(r['enterprise']['months'][5]['total_delivered_units']),1000)
        self.assertEqual(op(r,5)['assigned_units']['baseline'],0)
        move=next(e for e in r['enterprise']['events'] if e['move']['move_id']=='incumbent-response')
        self.assertEqual(move['status'],'assigned')
        inv=next(i for i in r['closing_treasury']['invoices'] if i['invoice_id']==move['invoice_id'])
        self.assertEqual(inv['paid_cents'],350_000)
        self.assertEqual(q(op(r,5,'incumbent')['human_delivered_units']),600)

    def test_response_timing_does_not_create_robot_capacity(self):
        prompt,delayed=self.cases['prompt_customer_response'],self.cases['shared_reference']
        self.assertEqual(prompt['units'],delayed['units'])
        self.assertEqual(q(op(prompt,3)['total_delivered_units']),30)
        self.assertEqual(q(op(delayed,3)['total_delivered_units']),100)
        self.assertEqual(q(prompt['enterprise']['months'][3]['total_delivered_units']),1030)
        self.assertLess(cash_of(prompt,'entrant'),cash_of(delayed,'entrant'))

    def test_procurement_timing_changes_allocation_in_one_pool(self):
        r=self.cases['delayed_incumbent_procurement']
        self.assertEqual(sum(u['operator_id']=='entrant' and u['status']=='installed' for u in r['units']),3)
        self.assertEqual(q(op(r,2)['robot_capacity_units']),75)
        self.assertEqual(q(op(r,3)['robot_capacity_units']),300)
        self.assertEqual(q(op(r,3)['total_delivered_units']),100)
        self.assertEqual(len(r['units']),7)
        self.assertEqual(r['months'][-1]['closing_stock']['installed'],5)
        self.assertEqual(r['enterprise']['consolidation']['external_physical_outlay_cents'],
                         self.cases['shared_reference']['enterprise']['consolidation']['external_physical_outlay_cents'])

    def test_formation_failure_prevents_capture_and_procurement(self):
        r=self.cases['formation_unfunded']
        self.assertTrue(all(q(op(r,m)['total_delivered_units'])==0 for m in range(8)))
        self.assertTrue(all(q(row['total_delivered_units'])==1000 for row in r['enterprise']['months']))
        self.assertFalse(any(u['operator_id']=='entrant' for u in r['units']))
        self.assertTrue(all(e['status']=='blocked' for e in r['enterprise']['events']))
        outcome=next(x for x in r['enterprise']['business_outcomes'] if x['actor_id']=='entrant')
        self.assertEqual(outcome['first_failed_payment_at'],{'month':0,'phase':3})
        self.assertGreater(outcome['closing_due_unpaid_cents'],0)
        self.assertEqual(cash_of(r,'entrant'),100_000)

    def test_no_entry_is_not_an_additional_copy_of_market(self):
        r=self.cases['incumbent_only']
        self.assertTrue(all(q(m['total_delivered_units'])==1000 for m in r['enterprise']['months']))
        self.assertEqual(sum(q(op(r,m)['total_delivered_units']) for m in range(8)),0)
        self.assertEqual(cash_of(r,'entrant'),2_500_000)
        self.assertEqual(r['enterprise']['events'],[])

    def test_delivered_output_invoice_cash_are_distinct(self):
        r=self.cases['shared_reference'];invoices={i['invoice_id']:i for i in r['closing_treasury']['invoices']}
        for line in r['enterprise']['invoice_lines']:
            self.assertEqual(q(line['unrounded_cents']),q(line['accepted_units'])*line['rate_cents_per_unit'])
            self.assertLessEqual(abs(q(line['rounding_difference_cents'])),Fraction(1,2))
            if line['invoice_id']:
                inv=invoices[line['invoice_id']]
                self.assertEqual(inv['face_cents'],line['face_cents'])
                self.assertEqual(inv['issued_at'],{'month':line['month'],'phase':6})
                self.assertGreater(inv['eligible_at']['month'],line['month'])
                if line['category']=='end_market_sale':self.assertEqual(inv['payer'],'end_buyers')
        outstanding=sum(i['outstanding_cents'] for i in invoices.values() if i['category']=='end_market_sale')
        self.assertEqual(outstanding,10_300_000)
        zero=[x for x in r['enterprise']['invoice_lines'] if x['operator_id']=='entrant' and x['month']<2]
        self.assertTrue(all(x['invoice_id'] is None for x in zero))

    def test_exact_fractional_output_has_one_invoice_rounding(self):
        p,t,cs,e=reference_inputs()
        p=replace(p,operators=(Operator('incumbent',0,(1300,)*8),Operator('entrant',1,(1300,)*8)),
                  starts=(),opening_finished=1,system=replace(p.system,full_output_units_per_robot_month=101,
                       first_month_ramp_numerator=1,first_month_ramp_denominator=2))
        businesses=tuple(replace(b,overhead_cents_by_month=(0,)*8,human_capacity_by_month=(0,)*8,
                    human_staff_cents_by_month=(0,)*8,price_cents_per_unit_by_month=(1,)*8,
                    formation_cents=0,acquisition_cents_per_recurring_unit=0,material_cents_per_delivered_unit=1)
                         for b in e.businesses)
        e=replace(e,market=replace(e.market,baseline_units=0,unmet_units=100,new_units=0),businesses=businesses,
                  moves=(CustomerMove('capture',0,'unmet',None,'entrant',100),))
        r=run_enterprise(p,t,cs,e)
        self.assertEqual(q(op(r,1)['total_delivered_units']),Fraction(101,2))
        lines=[x for x in r['enterprise']['invoice_lines'] if x['month']==1 and x['operator_id']=='entrant']
        self.assertTrue(all(x['face_cents']==51 and q(x['rounding_difference_cents'])==Fraction(1,2) for x in lines))
        self.assertEqual(round_cents(Fraction(101,4)),25)

    def test_human_staff_is_paid_capacity_not_automatic_payroll_removal(self):
        r=self.cases['shared_reference']
        self.assertEqual(q(op(r,0,'incumbent')['human_delivered_units']),800)
        self.assertEqual(q(op(r,3,'incumbent')['human_delivered_units']),530)
        staff=[i for i in r['closing_treasury']['invoices'] if i['category']=='human_staff']
        self.assertEqual([i['paid_cents'] for i in staff],[7_500_000]*8)
        p,t,cs,e=reference_inputs();t=closing_account(t,'incumbent',0)
        poor=run_enterprise(p,t,cs,e)
        self.assertEqual(q(op(poor,0,'incumbent')['human_delivered_units']),0)
        self.assertEqual(q(op(poor,0,'incumbent')['robot_delivered_units']),0)

    def test_equity_is_funded_external_cash_not_sales(self):
        r=self.cases['additional_equity'];c=r['enterprise']['consolidation']
        self.assertEqual(c['equity_cash_received_cents'],1_895_000)
        self.assertEqual(c['end_market_cash_received_cents'],self.cases['shared_reference']['enterprise']['consolidation']['end_market_cash_received_cents'])
        self.assertEqual(cash_of(r,'investor'),100_000_000-1_895_000)
        self.assertEqual(r['enterprise']['minimum_actual_cash_cents']['entrant'],0)
        p,t,cs,e=reference_inputs(entrant_cash=100_000,extra_equity=1_895_000)
        unfunded=run_enterprise(p,closing_account(t,'investor',0),cs,e)
        self.assertEqual(unfunded['enterprise']['consolidation']['equity_cash_received_cents'],0)
        self.assertEqual(q(op(unfunded,2)['total_delivered_units']),0)
        promises=[i for i in unfunded['closing_treasury']['invoices'] if i['category']=='equity_contribution']
        self.assertEqual(promises[0]['outstanding_cents'],1_895_000)

    def test_one_cent_below_bridge_misses_supported_execution(self):
        r=run_enterprise(*reference_inputs(entrant_cash=100_000,extra_equity=1_894_999))
        self.assertEqual(q(op(r,2)['total_delivered_units']),25)
        self.assertEqual(q(op(r,3)['total_delivered_units']),0)
        good=self.cases['additional_equity']
        self.assertEqual(q(op(good,3)['total_delivered_units']),100)
        self.assertEqual(cash_of(r,'entrant')>=0,True)

    def test_late_equity_does_not_reverse_earlier_allocation(self):
        p,t,cs,e=reference_inputs(entrant_cash=100_000,extra_equity=1_895_000)
        e=replace(e,equity=(replace(e.equity[0],month=3),))
        r=run_enterprise(p,t,cs,e)
        self.assertEqual(r['months'][0]['closing_cash_cents']['entrant'],100_000)
        self.assertEqual(q(op(r,2)['total_delivered_units']),0)
        self.assertEqual(r['enterprise']['consolidation']['equity_cash_received_cents'],1_895_000)
        self.assertFalse(any(u['operator_id']=='entrant' for u in r['units']))
        self.assertEqual(op(r,3)['assigned_units']['baseline'],0)

    def test_money_cannot_bypass_component_and_support_limits(self):
        p,t,cs,e=reference_inputs();p=replace(p,opening_components=0)
        r=run_enterprise(p,t,cs,e)
        self.assertEqual(len(r['units']),2)
        self.assertTrue(all(m['flows']['started']==0 for m in r['months']))
        self.assertTrue(all(q(op(r,m)['robot_capacity_units'])==0 for m in range(8)))
        self.assertEqual(sum(i['paid_cents'] for i in r['closing_treasury']['invoices'] if i['category']=='start'),0)

    def test_no_robots_means_no_entrant_robot_delivery(self):
        p,t,cs,e=reference_inputs();p=replace(p,starts=(),operators=tuple(replace(o,opening_installed=0) for o in p.operators))
        r=run_enterprise(p,t,cs,e)
        self.assertEqual(r['units'],[])
        self.assertEqual(q(op(r,3)['robot_delivered_units']),0)
        self.assertEqual(q(r['enterprise']['months'][3]['total_delivered_units']),930)

    def test_failed_customer_move_never_duplicates_or_bills_assignment(self):
        p,t,cs,e=reference_inputs()
        e=replace(e,moves=(CustomerMove('too-many',2,'baseline','incumbent','entrant',1001),))
        r=run_enterprise(p,t,cs,e)
        self.assertEqual(op(r,2)['assigned_units']['baseline'],0)
        self.assertEqual(q(r['enterprise']['months'][2]['total_delivered_units']),1000)
        evt=r['enterprise']['events'][0];self.assertEqual(evt['reason'],'insufficient_source_assignment')
        invoice=next(i for i in r['closing_treasury']['invoices'] if i['invoice_id']==evt['invoice_id'])
        self.assertEqual(invoice['paid_cents'],0);self.assertEqual(invoice['outstanding_cents'],0)

    def test_all_cases_demand_stock_cash_and_round_trip_reconcile(self):
        for r in self.cases.values():
            self.assertEqual(replay_enterprise(r),r)
            hashed={k:v for k,v in r.items() if k!='case_hash'}
            self.assertEqual(r['case_hash'],hashlib.sha256(json.dumps(hashed,sort_keys=True,separators=(',',':')).encode()).hexdigest())
            self.assertIn('model/monthly_enterprise.py',r['source_sha256'])
            actors=r['closing_treasury']['actors']
            self.assertEqual(sum(a['cash_cents'] for a in actors),sum(a['opening_cash_cents'] for a in actors))
            c=r['enterprise']['consolidation'];self.assertEqual(c['other_boundary_cash_cents'],0)
            self.assertEqual(c['included_cash_change_cents'],c['end_market_cash_received_cents']+c['equity_cash_received_cents']-c['external_physical_outlay_cents']-c['external_enterprise_outlay_cents'])
            for physical,market in zip(r['months'],r['enterprise']['months']):
                for pool in market['pools'].values():
                    self.assertEqual(sum(x['units'] for x in pool['assignments']),pool['recurring_demand_units'])
                    self.assertEqual(q(pool['delivered_units'])+q(pool['unserved_units']),pool['recurring_demand_units'])
                for output in physical['outputs']:
                    served=next(x for x in market['operators'] if x['operator_id']==output['operator_id'])
                    self.assertEqual(output['accepted_output_units'],served['robot_delivered_units'])
                    self.assertLessEqual(q(served['robot_delivered_units']),q(output['ramped_capacity_units']))
                    self.assertEqual(q(served['total_delivered_units']),q(served['robot_delivered_units'])+q(served['human_delivered_units']))
                self.assertIsNone(market['baseline_equivalent_labor_hours'])

    def test_common_market_survives_all_three_funded_contract_arrangements(self):
        p,t,cs,e=reference_inputs()
        t=closing_account(t,'entrant',100_000_000)
        worlds=[]
        for arrangement in ('sale','lease','provider_service'):
            contracts=tuple(replace(c,arrangement=arrangement,lessor_actor='lessor' if arrangement=='lease' else None) for c in cs)
            worlds.append(run_enterprise(p,t,contracts,e))
        for other in worlds[1:]:
            self.assertEqual(worlds[0]['enterprise']['months'],other['enterprise']['months'])
            self.assertEqual(worlds[0]['commercial']['consolidation']['external_physical_outlay_cents'],
                             other['commercial']['consolidation']['external_physical_outlay_cents'])
            self.assertEqual(other['enterprise']['consolidation']['other_boundary_cash_cents'],0)

    def test_qualification_is_not_inferred_from_cash_or_later_robot_access(self):
        p,t,cs,e=reference_inputs()
        businesses=tuple(replace(b,qualified_month=4) if b.operator_id=='entrant' else b for b in e.businesses)
        r=run_enterprise(p,t,cs,replace(e,businesses=businesses))
        self.assertTrue(all(op(r,m)['assigned_units']['baseline']==0 for m in range(8)))
        capture=[x for x in r['enterprise']['events'] if x['move']['move_id'].startswith('capture')]
        self.assertTrue(all(x['reason']=='target_unqualified_or_overdue' for x in capture))
        self.assertTrue(all(q(m['total_delivered_units'])==1000 for m in r['enterprise']['months']))

    def test_invalid_identity_numeric_and_failed_run_preserve_inputs(self):
        p,t,cs,e=reference_inputs();before=t.snapshot()
        for field in ('formation_cents','qualified_month','procurement_month','material_cents_per_delivered_unit'):
            for invalid in (True,-1,1.5,float('nan'),float('inf')):
                with self.assertRaises(ValueError):replace(e.businesses[1],**{field:invalid})
        bad=[replace(e,market=replace(e.market,work_id='wrong')),
             replace(e,businesses=(e.businesses[0],e.businesses[0])),
             replace(e,equity=(Equity('self',0,'incumbent','entrant',1),)),
             replace(e,moves=(CustomerMove('unknown',2,'baseline','incumbent','missing',1),))]
        for config in bad:
            with self.assertRaises(ValueError):run_enterprise(p,t,cs,config)
        # A late planning-ceiling error occurs after local paid transitions, without changing input Treasury.
        invalid_p=replace(p,operators=tuple(replace(o,demand_units_by_month=(0,)*8) for o in p.operators))
        with self.assertRaises(ValueError):run_enterprise(invalid_p,t,cs,e)
        self.assertEqual(before,t.snapshot())


if __name__=='__main__':unittest.main()
