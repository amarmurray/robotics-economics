import copy, unittest
from fractions import Fraction
from model.staffed_renewals import (staffed_renewals_artifact,run_staffed_renewals_case,replay_staffed_renewals)
from model.calendar_bridge import rational

class StaffedRenewalsTests(unittest.TestCase):
 @classmethod
 def setUpClass(cls):
  cls.artifact=staffed_renewals_artifact();cls.cases=cls.artifact['cases'];cls.summary={x['case']:x for x in cls.artifact['summary']}
 def rows(self,name,op='incumbent'):return [x for x in self.cases[name]['staffed_renewals']['months'] if x['operator_id']==op]
 def test_one_ledger_every_payer_and_distinct_units(self):
  for name,r in self.cases.items():
   self.assertEqual(sum(a['cash_cents'] for a in r['opening_treasury']['actors']),sum(a['cash_cents'] for a in r['closing_treasury']['actors']),name)
   self.assertEqual(r['entry_transition']['consolidation']['unclassified_boundary_cash_cents'],0)
   for m in r['competition']['months']:self.assertEqual(sum(x['units'] for x in m['lots']),500)
   for m in r['staffed_renewals']['months']:
    self.assertEqual(m['outside_completed_jobs']+m['outside_unserved_jobs'],m['outside_required_jobs'])
    self.assertEqual(rational(m['accepted_cleaning_zones'])+rational(m['unserved_cleaning_zones']),m['cleaning_required_zones'])
 def test_exact_worker_minutes_and_no_resource_alias(self):
  for r in self.cases.values():
   ids=[]
   for m in r['staffed_renewals']['months']:
    booked=sum((rational(x['minutes']) for x in m['bookings']),Fraction())
    self.assertEqual(booked,rational(m['booked_minutes']))
    self.assertEqual(booked+rational(m['unused_minutes']),m['regular_available_minutes']+m['overtime_paid_minutes'])
    self.assertTrue(all(x['worker_resource_id']==m['resource_id'] for x in m['bookings']))
    ids.extend(x['task_id'] for x in m['bookings'])
   self.assertEqual(len(ids),len(set(ids)))
 def test_new_awards_fit_paid_capacity_after_retained_work(self):
  for r in self.cases.values():
   for e in r['competition']['events']:
    if e['to_operator']:self.assertGreaterEqual(rational(e['available_capacity_before_award'][e['to_operator']]),e['units'])
   for m in r['competition']['months']:
    for op,cap in m['funded_capacity_before_awards'].items():
     row=next(x for x in r['staffed_renewals']['months'] if x['operator_id']==op and x['month']==m['month'])
     self.assertEqual(cap,row['funded_capacity_before_awards'])
 def test_notice_uses_only_prior_complete_month_and_remains_binding(self):
  r=self.cases['outside_surge_after_notice'];events=r['staffed_renewals']['events'];e=next(x for x in events if x['issued'])
  self.assertEqual((e['month'],e['based_only_on_completed_month'],e['effective_month']),(3,2,5))
  rows=self.rows('outside_surge_after_notice');self.assertTrue(rows[2]['complete_obligation'])
  self.assertEqual([x['scheduled_blocks'] for x in rows],[2]*5+[1]*3)
  self.assertEqual(r['enterprise']['inputs']['businesses'][0]['human_staff_cents_by_month'],[400000]*8)
 def test_reduced_bid_capacity_reallocates_actual_contracts(self):
  s=self.summary['binding_staff_cut'];self.assertEqual(s['complete_whole_service_months'],8)
  self.assertEqual(s['final_assigned_units'],{'incumbent':450,'entrant':50})
  self.assertEqual(s['staff_paid_cents'],4200000)
 def test_customer_rescue_leaves_outside_work_undone(self):
  s=self.summary['strong_paid_human_rival'];self.assertEqual(s['complete_market_months'],8)
  self.assertEqual(s['complete_whole_service_months'],5);self.assertEqual((s['outside_completed_jobs'],s['outside_required_jobs']),(242,260))
  self.assertTrue(all(x['outside_required_jobs']==45 for x in self.rows('strong_paid_human_rival')[4:]))
 def test_locked_contracts_keep_unserved_work(self):
  a,b=(self.summary[x] for x in ('outside_surge_after_notice','long_locked_contracts'))
  self.assertEqual(rational(a['accepted_zones']),3400);self.assertEqual(rational(b['accepted_zones']),2590)
  self.assertEqual(b['final_assigned_units']['incumbent'],500)
 def test_fixed_prepaid_overtime_preserves_whole_service(self):
  s=self.summary['prepaid_fallback'];self.assertEqual(s['complete_whole_service_months'],8)
  self.assertEqual(s['outside_completed_jobs'],260);self.assertEqual(s['overtime_paid_cents'],1500000)
  r=self.cases['prepaid_fallback']
  for row in r['staffed_renewals']['months']:
   if row['overtime_paid_minutes']:
    inv=next(x for x in r['closing_treasury']['invoices'] if x['invoice_id']==row['overtime_invoice_id'])
    self.assertEqual(inv['issued_at']['phase'],1);self.assertEqual(inv['due_at']['phase'],5)
    self.assertEqual(inv['face_cents'],inv['paid_cents']);self.assertGreaterEqual(row['cash_before_overtime_cents'],inv['face_cents'])
 def test_exact_funding_cent_changes_first_service_not_just_cash(self):
  a=self.rows('exact_overtime_funding')[0];b=self.rows('one_cent_short_overtime')[0]
  self.assertEqual((a['cash_before_overtime_cents'],b['cash_before_overtime_cents']),(480000,479999))
  self.assertEqual((a['overtime_paid_minutes'],b['overtime_paid_minutes']),(4800,0))
  self.assertEqual(self.summary['exact_overtime_funding']['complete_whole_service_months'],8)
  self.assertEqual(self.summary['one_cent_short_overtime']['complete_whole_service_months'],7)
  self.assertEqual(b['overtime_block_reason'],'unfunded_prospective_overtime')
 def test_two_minutes_can_move_one_indivisible_customer_lot(self):
  a,b=(self.summary[x] for x in ('human_no_robot','human_two_minutes_short'))
  self.assertEqual(a['final_assigned_units']['incumbent'],500);self.assertEqual(b['final_assigned_units']['incumbent'],450)
  self.assertEqual(a['complete_whole_service_months'],b['complete_whole_service_months'])
 def test_strong_human_same_surge_and_every_payer_cost(self):
  a,b=(self.summary[x] for x in ('prepaid_fallback','strong_human_surge'))
  self.assertEqual((a['complete_whole_service_months'],b['complete_whole_service_months']),(8,8))
  self.assertEqual(a['outside_required_jobs'],b['outside_required_jobs'])
  self.assertLess(b['all_payer_resource_and_transaction_cash_cents'],a['all_payer_resource_and_transaction_cash_cents'])
 def test_common_owner_does_not_pool_people_or_operating_cash(self):
  a,b=(self.cases[x] for x in ('binding_staff_cut','independent_firms'))
  self.assertEqual(a['staffed_renewals']['months'],b['staffed_renewals']['months'])
  self.assertTrue(a['renewing_entry']['months'][-1]['common_owner_of_active_firms'])
  self.assertFalse(b['renewing_entry']['months'][-1]['common_owner_of_active_firms'])
 def test_paid_offer_capacity_can_remain_unused(self):
  rows=self.rows('paid_losing_offer');paid=[m for m in rows if m['overtime_paid_minutes']]
  self.assertTrue(paid);self.assertTrue(any(rational(m['unused_minutes'])>m['overtime_paid_minutes'] for m in paid))
 def test_full_replay_ignores_derived_outcomes(self):
  for name,r in self.cases.items():
   saved=copy.deepcopy(r);saved['staffed_renewals']['months']=[];saved['staffed_renewals']['cash']={};saved['competition']['events']=[];saved['closing_treasury']={};saved['case_hash']='forged'
   self.assertEqual(replay_staffed_renewals(saved),r,name)
 def test_invalid_qualification_and_crew_alias_refused(self):
  for x in ([],{'crews':None},{'crews':{'unknown':{}}},{'crews':{'incumbent':{'outside_jobs_by_month':[1]}}},
            {'crews':{'incumbent':{'resource_id':'same'},'entrant':{'resource_id':'same'}}},{'crews':{'incumbent':{'opening_blocks':True}}}):
   with self.assertRaises((ValueError,TypeError)):run_staffed_renewals_case(x)
  r=run_staffed_renewals_case({'entry':{'market':{'entrant_qualified_month':7}},'crews':{'incumbent':{'target_blocks':1}}})
  self.assertTrue(all(rational(x['funded_capacity_before_awards'])==0 for x in r['staffed_renewals']['months'] if x['operator_id']=='entrant' and x['month']<7))

if __name__=='__main__':unittest.main()
