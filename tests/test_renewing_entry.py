"""Real renewal, beneficial ownership, funding and retained liabilities reconcile."""
import copy,json,random,unittest
from dataclasses import replace
from fractions import Fraction
from pathlib import Path
from model.calendar_bridge import rational
from model.renewing_entry import run_renewing_entry_case,replay_renewing_entry,renewing_entry_inputs,run_renewing_entry,renewing_entry_worlds
from model.competitive_renewals import run_competitive_renewals

class RenewingEntryTests(unittest.TestCase):
 @classmethod
 def setUpClass(cls):cls.cases=json.loads(Path('model/results/renewing_entry.json').read_text())['cases']
 def conserved(self,r):
  self.assertEqual(sum(x['cash_cents'] for x in r['opening_treasury']['actors']),sum(x['cash_cents'] for x in r['closing_treasury']['actors']))
  self.assertEqual(r['entry_transition']['consolidation']['unclassified_boundary_cash_cents'],0)
  self.assertEqual(r['finance']['consolidation']['unclassified_other_boundary_cash_cents'],0)
  seen=set()
  for m,g,entry in zip(r['competition']['months'],r['renewing_entry']['months'],r['entry_transition']['months']):
   self.assertEqual(sum(x['units'] for x in m['lots']),500)
   self.assertEqual(len({x['lot_id'] for x in m['lots']}),10)
   owned=[x for x in m['lots'] if entry['ultimate_owners'].get(x['owner'])=='platform_buyer']
   self.assertEqual(sum(x['units'] for x in owned),g['platform_assigned_units'])
   self.assertEqual(sum((rational(x['delivered_units']) for x in owned),Fraction()),rational(g['platform_delivered_zones']))
   self.assertFalse(seen&set(g['new_platform_contract_lot_ids']));seen.update(g['new_platform_contract_lot_ids'])
  self.assertTrue(all(x['cash_cents']>=0 for x in r['closing_treasury']['actors']))
 def test_all_worlds_conserve_market_units_and_every_actor_cash(self):
  for r in self.cases.values():self.conserved(r)
 def test_share_reclassification_does_not_create_service_contract_win_or_sweep(self):
  a,b=(self.cases[k] for k in ('status_quo','share_acquisition'))
  self.assertEqual(a['enterprise']['months'],b['enterprise']['months'])
  self.assertEqual(a['competition'],b['competition'])
  self.assertEqual(sum(x['units'] for x in b['renewing_entry']['contracts_reclassified_at_share_close']),500)
  self.assertEqual(sum(m['new_platform_contract_units'] for m in b['renewing_entry']['months']),0)
  self.assertEqual(b['entry_transition']['consolidation']['target_cash_swept_to_buyer_cents'],0)
 def test_common_ownership_separates_internal_transfers_and_new_contracts(self):
  r=self.cases['hybrid'];g=r['renewing_entry']
  self.assertEqual(sum(x['units'] for x in g['contracts_reclassified_at_share_close']),400)
  self.assertEqual(sum(m['new_platform_contract_units'] for m in g['months']),100)
  self.assertEqual(sum(m['intra_platform_reassigned_units'] for m in g['months']),100)
  self.assertTrue(all(m['common_owner_of_active_firms'] for m in g['months'][2:]))
  self.assertIn('not independent competition',g['offer_authority'])
 def test_reacquiring_lost_work_is_not_a_new_platform_contract(self):
  g=self.cases['hybrid_interruption']['renewing_entry']['months']
  self.assertEqual(sum(m['outside_or_unassigned_award_units'] for m in g),400)
  self.assertEqual(sum(m['new_platform_contract_units'] for m in g),100)
 def test_failed_close_retains_prior_diligence_and_separate_growth(self):
  r=self.cases['hybrid_failed_close'];a=r['entry_transition']
  self.assertEqual(a['close_status'],'blocked');self.assertEqual(a['cash']['paid_diligence_cents'],100000)
  self.assertEqual(a['cash']['paid_growth_equity_cents'],6000000)
  for key in ('paid_share_price_cents','paid_transition_resources_cents','paid_target_equity_cents'):self.assertEqual(a['cash'][key],0)
  self.assertFalse(r['renewing_entry']['contracts_reclassified_at_share_close'])
 def test_exact_buyer_cent_switch_does_not_use_target_cash(self):
  for amount,expected in [(16600000,'closed'),(16599999,'blocked')]:
   r=run_renewing_entry_case({'buyer_cash_cents':amount});self.assertEqual(r['entry_transition']['close_status'],expected);self.conserved(r)
 def test_target_payable_survives_and_working_equity_is_separate(self):
  a,b=(self.cases[k] for k in ('inherited_target_liability','funded_target_liability'))
  for r in (a,b):
   invoice=next(x for x in r['closing_treasury']['invoices'] if x['invoice_id']=='opening-target-payable')
   self.assertEqual((invoice['payer'],invoice['payee'],invoice['face_cents']),('incumbent','enterprise_vendor',3000000))
   self.assertEqual(invoice['paid_cents']+invoice['outstanding_cents'],3000000)
  self.assertEqual(b['entry_transition']['cash']['paid_target_equity_cents'],3000000)
  self.assertEqual(b['entry_transition']['cash']['buyer_closing_cents'],400000)
  self.assertGreater(sum(x['intra_platform_reassigned_units'] for x in a['renewing_entry']['months']),sum(x['intra_platform_reassigned_units'] for x in b['renewing_entry']['months']))
 def test_disruption_preserves_locked_contracts_and_unserved_work(self):
  a=self.cases['hybrid_locked_interruption'];months=a['enterprise']['months']
  self.assertLess(rational(months[2]['total_delivered_units']),500)
  self.assertEqual(rational(months[3]['total_delivered_units']),500)
  self.assertFalse(any(x['month']==2 for x in a['competition']['events']))
  self.assertEqual(a['entry_transition']['months'][2]['target_disrupted'],True)
 def test_stronger_human_and_response_has_complete_service_without_customer_wins(self):
  r=self.cases['human_competitive_response'];self.assertTrue(all(rational(m['total_delivered_units'])==500 for m in r['enterprise']['months']))
  self.assertEqual(sum(m['new_platform_contract_units'] for m in r['renewing_entry']['months']),0)
  self.assertEqual(r['entry_transition']['consolidation']['external_operating_and_transaction_cash_cents'],7170000)
 def test_complete_replay_ignores_all_joint_derived_outcomes(self):
  for name,r in self.cases.items():
   saved=copy.deepcopy(r);saved['renewing_entry']={};saved['competition']['months']=[];saved['entry_transition']['events']=[];saved['closing_treasury']={};saved['case_hash']='forged'
   self.assertEqual(replay_renewing_entry(saved),r,name)
 def test_default_renewals_still_reject_inherited_invoices_and_joint_rejects_wrong_bill(self):
  args=list(renewing_entry_inputs({'target_opening_payable_cents':1}));p,t,cs,e,f,b,c,tr=args
  with self.assertRaises(ValueError):run_competitive_renewals(p,t,cs,e,f,b,c)
  args[1]=replace(t,invoices=tuple(replace(i,payee='provider') for i in t.invoices))
  with self.assertRaises(ValueError):run_renewing_entry(*args)
 def test_bad_controls_fail_and_seeded_variants_keep_one_cash_and_market(self):
  for x in ([],{'market':None},{'transition':None},{'human_efficiency':True},{'human_efficiency':1},{'market':{'entrant_cash_cents':100}},{'transition':{'mode':'build'}},{'buyer_cash_cents':True}):
   with self.assertRaises((ValueError,TypeError)):run_renewing_entry_case(x)
  rng=random.Random(38)
  for _ in range(3):
   r=run_renewing_entry_case({'buyer_cash_cents':rng.randrange(12000000,24000000),'transition':{'disruption_months':rng.randrange(0,3)},'market':{'competition':{'term_months':rng.randrange(1,4)}}});self.conserved(r)
if __name__=='__main__':unittest.main()
