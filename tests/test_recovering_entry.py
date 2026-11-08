"""Paid asset title, debt cure, legal cash and actual customer service stay distinct."""
import copy,json,random,unittest
from fractions import Fraction
from pathlib import Path
from model.calendar_bridge import rational
from model.recovering_entry import (recovering_entry_inputs,run_recovering_entry_case,
    run_recovering_entry,replay_recovering_entry)
from model.renewing_entry import run_renewing_entry

def invoices(r,category):return [i for i in r['closing_treasury']['invoices'] if i['category']==category]
def service(r):return [rational(m['total_delivered_units']) for m in r['enterprise']['months']]
def summary(r):return r['asset_recovery']['summary']

class RecoveringEntryTests(unittest.TestCase):
 @classmethod
 def setUpClass(cls):cls.cases=json.loads(Path('model/results/recovering_entry.json').read_text())['cases']
 def conserved(self,r):
  self.assertEqual(sum(a['cash_cents'] for a in r['opening_treasury']['actors']),sum(a['cash_cents'] for a in r['closing_treasury']['actors']))
  self.assertEqual(r['finance']['consolidation']['unclassified_other_boundary_cash_cents'],0)
  self.assertEqual(r['entry_transition']['consolidation']['unclassified_boundary_cash_cents'],0)
  self.assertEqual(len({u['unit_id'] for u in r['units']}),len(r['units']))
  self.assertTrue(all(a['cash_cents']>=0 for a in r['closing_treasury']['actors']))
  for m,g in zip(r['competition']['months'],r['recovering_entry']['months']):
   self.assertEqual(sum(l['units'] for l in m['lots']),500)
   self.assertEqual(len({l['lot_id'] for l in m['lots']}),10)
   self.assertEqual(sum((rational(l['delivered_units']) for l in m['lots']),Fraction()),rational(g['accepted_zones']))
   self.assertEqual(rational(g['accepted_zones'])+rational(g['unserved_zones']),500)
  self.assertEqual(r['recovering_entry']['all_payer_resource_and_transaction_cash_cents'],r['entry_transition']['consolidation']['external_operating_and_transaction_cash_cents']+r['competition']['buyer_switch_resource_cash_cents'])
  vendors={'manufacturer','deployment_vendor','enterprise_vendor','digital_vendor','entry_resource_vendor'}
  opening={a['actor_id']:a['cash_cents'] for a in r['opening_treasury']['actors']}
  receipts=sum(a['cash_cents']-opening[a['actor_id']] for a in r['closing_treasury']['actors'] if a['actor_id'] in vendors)
  self.assertEqual(receipts,r['recovering_entry']['all_payer_resource_and_transaction_cash_cents'])
 def test_all_worlds_conserve_units_contracts_every_actor_cash_and_buyer_costs(self):
  for r in self.cases.values():self.conserved(r)
 def test_disabled_recovery_preserves_the_same_entry_renewal_physical_history(self):
  args=recovering_entry_inputs({'recovery':{'enabled':False}})
  old=run_renewing_entry(*args[:-1]);new=run_recovering_entry(*args)
  for key in ('plan','months','units','events','opening_treasury','closing_treasury','enterprise','competition','calendar_bridge'):
   self.assertEqual(old[key],new[key],key)
  self.assertEqual(old['entry_transition']['cash'],new['entry_transition']['cash'])
 def test_title_has_actual_current_manufacture_hardware_payment_and_loan(self):
  r=self.cases['funded_owner_sale'];g=r['recovering_entry']
  self.assertFalse(g['any_opening_installed_units']);self.assertEqual(r['plan']['opening_finished'],0)
  self.assertEqual([u['unit_id'] for u in r['units']],['start-shared-supply-1'])
  self.assertEqual(sum(i['paid_cents'] for i in invoices(r,'start')),3600000)
  self.assertEqual([(i['payer'],i['payee'],i['paid_cents']) for i in g['original_hardware_purchase_invoices']],[('incumbent','provider',6000000)])
  self.assertEqual(r['finance']['consolidation']['loan_draw_cash_cents'],6000000)
  self.assertEqual([m['title_owner'] for m in r['asset_recovery']['months']],['provider','incumbent','incumbent','incumbent','entrant','entrant','entrant','entrant'])
  for commercial,recovery in zip(r['commercial']['months'],r['asset_recovery']['months']):
   self.assertEqual(commercial['assets'][0]['title_owner'],recovery['title_owner'])
 def test_share_closing_and_later_title_transfer_are_separate(self):
  r=self.cases['funded_owner_sale'];rows=r['recovering_entry']['months']
  self.assertEqual(rows[2]['ultimate_owners']['incumbent'],'platform_buyer')
  self.assertEqual(rows[2]['title_owner'],'incumbent')
  self.assertEqual(rows[4]['title_owner'],'entrant')
  self.assertFalse(r['asset_recovery']['events'][0]['customer_assignments_transferred'])
  self.assertEqual(sum(m['new_platform_contract_units'] for m in r['renewing_entry']['months']),100)
 def test_sale_receipts_cure_on_later_settlement_before_physical_reuse(self):
  r=self.cases['funded_owner_sale'];g=r['recovering_entry']['months']
  self.assertTrue(g[4]['seller_defaulted']);self.assertFalse(g[5]['seller_defaulted'])
  self.assertFalse(g[5]['supported']);self.assertTrue(g[6]['supported'])
  self.assertEqual(service(r),[500,500,500,500,100,500,500,500])
  self.assertEqual(rational(summary(r)['accepted_zones']),3600)
 def test_failed_or_late_robot_qualification_retains_cash_cure_and_missed_service(self):
  for name in ('qualification_unavailable','arrival_after_horizon'):
   r=self.cases[name];a=summary(r)
   self.assertTrue(a['sale_completed']);self.assertEqual(a['final_physical_state'],'transit')
   self.assertEqual((a['purchase_transfer_cents'],a['relocation_resource_cents']),(3000000,100000))
   self.assertEqual(service(r),service(self.cases['funded_owner_sale']))
   self.assertIsNone(a['first_buyer_supported_month']);self.assertEqual(a['closing_principal_claim_cents'],0)
 def test_low_proceeds_preserve_debt_even_after_actual_robot_reuse(self):
  r=self.cases['low_sale_proceeds'];a=summary(r)
  self.assertEqual(a['closing_principal_claim_cents'],578258)
  self.assertEqual(a['first_buyer_supported_month'],6)
  self.assertTrue(r['recovering_entry']['months'][-1]['seller_defaulted'])
  self.assertEqual(rational(a['accepted_zones']),2850)
 def test_lessors_title_and_configuration_rights_refuse_sale(self):
  for name,reason in [('leased_title_refused','seller_does_not_own_unit'),('configuration_rights_unavailable','asset_and_configuration_transfer_not_permitted')]:
   r=self.cases[name];self.assertFalse(summary(r)['sale_completed'])
   self.assertEqual(r['asset_recovery']['events'][0]['reason'],reason)
   self.assertEqual(sum(i['paid_cents'] for i in invoices(r,'asset_recovery_purchase')),0)
  r=self.cases['leased_title_refused'];self.assertEqual(summary(r)['final_title_owner'],'lessor')
  self.assertEqual(r['recovering_entry']['original_hardware_purchase_invoices'][0]['payer'],'lessor')
 def test_exact_cent_purchase_gate_does_not_guarantee_future_operations(self):
  a,b=(self.cases[k] for k in ('exact_buyer_funding','one_cent_short'))
  self.assertEqual(a['asset_recovery']['events'][0]['buyer_available_cents'],3100000)
  self.assertEqual(b['asset_recovery']['events'][0]['buyer_available_cents'],3099999)
  self.assertTrue(summary(a)['sale_completed']);self.assertFalse(summary(b)['sale_completed'])
  for category in ('asset_recovery_purchase','asset_recovery_relocation'):
   self.assertEqual(sum(i['paid_cents'] for i in invoices(b,category)),0)
  self.assertEqual(rational(summary(a)['accepted_zones']),3400)
  self.assertEqual(summary(a)['final_physical_state'],'transit')
 def test_locked_customer_commitments_survive_sale_and_preserve_lost_service(self):
  r=self.cases['locked_customer_commitments']
  self.assertEqual(service(r)[4],0);self.assertEqual(rational(summary(r)['accepted_zones']),3500)
  self.assertFalse(any(e['month']==4 for e in r['competition']['events']))
 def test_prior_separate_target_equity_can_prevent_default_without_sale(self):
  r=self.cases['prior_target_equity'];self.assertFalse(summary(r)['sale_completed'])
  self.assertEqual(r['asset_recovery']['events'][0]['reason'],'seller_not_in_current_debt_default')
  self.assertEqual(service(r),[500]*8)
  self.assertEqual(r['entry_transition']['cash']['paid_target_equity_cents'],3000000)
  self.assertEqual(r['entry_transition']['cash']['buyer_closing_cents'],400000)
 def test_competent_paid_human_buyer_keeps_service_without_recovery(self):
  a,b=(self.cases[k] for k in ('paid_human_buyer_sale','paid_human_buyer_no_sale'))
  self.assertEqual(service(a),service(b));self.assertEqual(service(b),[500]*8)
  for r in (a,b):
   staff=next(x for x in r['enterprise']['inputs']['businesses'] if x['operator_id']=='entrant')
   self.assertEqual(staff['human_staff_cents_by_month'],[400000]*8)
  self.assertGreater(a['recovering_entry']['all_payer_resource_and_transaction_cash_cents'],b['recovering_entry']['all_payer_resource_and_transaction_cash_cents'])
  self.assertGreater(summary(b)['closing_principal_claim_cents'],summary(a)['closing_principal_claim_cents'])
 def test_full_replay_ignores_derived_title_cash_and_service_outcomes(self):
  for name,r in self.cases.items():
   saved=copy.deepcopy(r);saved['recovering_entry']={};saved['asset_recovery']['events']=[];saved['asset_recovery']['summary']={};saved['units']=[];saved['closing_treasury']={};saved['case_hash']='forged'
   self.assertEqual(replay_recovering_entry(saved),r,name)
 def test_bad_inputs_and_malformed_complete_cases_are_rejected(self):
  for x in ([],{'entry':None},{'recovery':None},{'source_arrangement':'raas'},{'buyer_full_human_staff':1},{'maturity_month':0},{'target_loan_cents':True},{'entry':{'market':{'entrant_robots':1}}},{'recovery':{'seller_actor':'platform_buyer'}}):
   with self.assertRaises((ValueError,TypeError)):run_recovering_entry_case(x)
  for saved in (None,{}, {'schema_version':'recovering-entry-window/0.1'}):
   with self.assertRaises(ValueError):replay_recovering_entry(saved)
 def test_seeded_interest_timing_and_price_keep_all_claims_and_cash(self):
  rng=random.Random(39)
  for _ in range(4):
   r=run_recovering_entry_case({'monthly_rate_basis_points':rng.choice([0,50,100]),'recovery':{'price_cents':rng.randrange(10,36)*100000,'relocation_months':rng.randrange(1,5)}})
   self.conserved(r);f=r['finance']['consolidation']
   self.assertEqual(f['loan_draw_cash_cents']-f['principal_recovery_cash_cents'],f['closing_principal_claim_cents'])

if __name__=='__main__':unittest.main()
