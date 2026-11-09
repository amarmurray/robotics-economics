import copy,json,unittest
from fractions import Fraction
from pathlib import Path
from model.calendar_bridge import rational
from model.release_continuity import release_continuity_artifact,run_release_continuity_case,replay_release_continuity

class ReleaseContinuityTests(unittest.TestCase):
 @classmethod
 def setUpClass(cls):
  cls.artifact=release_continuity_artifact();cls.cases=cls.artifact['cases'];cls.summary={x['case']:x for x in cls.artifact['summary']}

 def test_cash_stock_parts_and_minutes_remain_one_history(self):
  for r in self.cases.values():
   self.assertEqual(sum(x['cash_cents'] for x in r['opening_treasury']['actors']),sum(x['cash_cents'] for x in r['closing_treasury']['actors']))
   self.assertEqual(len(r['units']),1);self.assertEqual(r['units'][0]['unit_id'],'start-shared-supply-1');self.assertEqual(r['entry_transition']['consolidation']['unclassified_boundary_cash_cents'],0)
   for m in r['staffed_renewals']['months']:
    self.assertEqual(sum((rational(x['minutes']) for x in m['bookings']),Fraction())+rational(m['unused_minutes']),m['regular_available_minutes']+m['overtime_paid_minutes'])
   for m in r['component_inventory']['months']:
    for k in m['qualified_closing']:self.assertEqual(m['qualified_opening'][k]+m['qualified_release'][k],m['qualified_closing'][k]+m['manufacturing_issued'][k]+m['service_issued'][k])

 def test_frozen_supported_version_preserves_previous_service_and_cash(self):
  prior=json.loads(Path('model/results/paid_development.json').read_text())['cases']['pass_first_review'];r=self.cases['retain_supported_legacy'];self.assertEqual(r['staffed_renewals']['cash'],prior['staffed_renewals']['cash']);self.assertEqual(r['competition']['months'],prior['competition']['months']);self.assertEqual(r['units'],prior['units']);self.assertEqual(r['release']['resource_cash_cents'],0)

 def test_review_success_is_prospective_and_deployment_qualification_is_separate(self):
  r=self.cases['reviewed_release_supported_legacy'];m=r['release']['months'];self.assertEqual((m[6]['supported_version_index'],m[7]['supported_version_index']),(0,1));self.assertEqual(r['release']['events'][0]['earliest_adoption_month'],7);self.assertEqual(r['release']['resource_cash_cents'],400000)
  q=[i for i in r['closing_treasury']['invoices'] if i['category']=='software_upgrade_qualification' and i['paid_cents']];self.assertEqual(len(q),1);self.assertEqual(q[0]['paid_cents'],50000);self.assertEqual(q[0]['due_at']['month'],7);self.assertEqual(rational(r['calendar_bridge']['months'][7]['qualification_hours_used']),2)

 def test_failed_review_stays_paid_while_supported_legacy_can_continue(self):
  r=self.cases['failed_review_supported_legacy'];self.assertEqual(r['release']['events'][0]['status'],'failed');self.assertEqual(r['release']['resource_cash_cents'],400000);self.assertIsNone(r['release']['adopted_month']);self.assertTrue(all(m['supported_version_index']==0 for m in r['release']['months'][2:]));self.assertEqual(self.summary['failed_review_supported_legacy']['complete_whole_service_months'],8)

 def test_expired_entitlement_can_leave_unassigned_market_work_after_notice(self):
  r=self.cases['failed_review_legacy_expired'];s=self.summary['failed_review_legacy_expired'];self.assertEqual(r['release']['unsupported_after_legacy_expiry_months'],[6,7]);self.assertEqual(s['complete_whole_service_months'],6);self.assertEqual(rational(s['accepted_zones']),3900);self.assertEqual(s['outside_completed_jobs'],160)
  self.assertTrue(all(m['complete_obligation'] for m in r['staffed_renewals']['months']));self.assertEqual(r['units'][0]['status'],'installed')

 def test_retained_staff_restores_complete_service_without_restoring_robot_entitlement(self):
  s=self.summary['retain_staff_through_expiry'];r=self.cases['retain_staff_through_expiry'];self.assertEqual(s['complete_whole_service_months'],8);self.assertEqual(rational(s['accepted_zones']),4000);self.assertEqual(r['release']['unsupported_after_legacy_expiry_months'],[6,7]);self.assertEqual(s['all_payer_resource_and_transaction_cash_cents']-self.summary['failed_review_legacy_expired']['all_payer_resource_and_transaction_cash_cents'],220000)

 def test_review_rights_and_operating_rights_are_separate(self):
  r=self.cases['review_pass_without_operating_rights'];self.assertEqual(r['release']['events'][0]['status'],'passed');self.assertEqual(r['release']['resource_cash_cents'],400000);self.assertIsNone(r['release']['adopted_month']);self.assertEqual(self.summary['review_pass_without_operating_rights']['complete_whole_service_months'],6)
  r=run_release_continuity_case({'release':{'evidence_use_rights':False}});self.assertEqual(r['release']['events'][0]['reason'],'review_evidence_rights_unavailable');self.assertEqual(r['release']['resource_cash_cents'],0);self.assertIsNone(r['release']['adopted_month'])

 def test_engineering_shortfall_performs_no_release_work(self):
  r=run_release_continuity_case({'release':{'review_engineering_hours':401}});self.assertEqual(r['release']['events'][0]['reason'],'engineering_hours_unavailable');self.assertEqual(r['release']['resource_cash_cents'],0);self.assertEqual(r['development']['completed_attempts'],1);self.assertEqual(rational(r['architecture_execution']['months'][6]['engineering_hours_used']),0)

 def test_one_cent_review_funding_boundary_does_not_pool_customer_cash(self):
  r=self.cases['reviewed_release_supported_legacy'];actor=r['release']['review_payer_actor_id'];before=r['months'][5]['closing_cash_cents'][actor];opening=r['architecture_execution']['inputs']['role_opening_cash_cents']['model_supplier'];required=opening-before+400000
  def case(amount):return run_release_continuity_case({'base':{'awards':{'architecture':{'role_opening_cash_cents':{'model_supplier':amount,'customer':20000000+opening-amount}}}}})
  good,bad=case(required),case(required-1);self.assertEqual(good['release']['resource_cash_cents'],400000);self.assertEqual(bad['release']['resource_cash_cents'],0);self.assertEqual(bad['release']['events'][0]['reason'],'review_payer_unfunded');self.assertEqual(sum(x['opening_cash_cents'] for x in good['architecture_execution']['entities']),sum(x['opening_cash_cents'] for x in bad['architecture_execution']['entities']))

 def test_no_retroactive_adoption_when_legacy_expires_before_a_passing_review(self):
  r=run_release_continuity_case({'release':{'legacy_support_through_month':5}});self.assertFalse(r['release']['months'][6]['supported']);self.assertEqual(r['release']['months'][7]['supported_version_index'],1);self.assertEqual(r['release']['unsupported_after_legacy_expiry_months'],[6])

 def test_external_review_cost_counted_once_and_transfers_not_added(self):
  outside={'manufacturer','deployment_vendor','enterprise_vendor','digital_vendor','entry_resource_vendor','architecture_resources'}
  for r in self.cases.values():
   self.assertEqual(sum(i['paid_cents'] for i in r['closing_treasury']['invoices'] if i['payee'] in outside),r['staffed_renewals']['cash']['all_payer_resource_and_transaction_cash_cents']);self.assertEqual(sum(i['paid_cents'] for i in r['closing_treasury']['invoices'] if i['category']=='release_review_resource'),r['release']['resource_cash_cents'])

 def test_complete_replay_ignores_derived_adoption_and_entitlement_claims(self):
  for r in self.cases.values():
   saved=copy.deepcopy(r);saved['release']['events']=[];saved['release']['months']=[];saved['release']['adopted_month']=0;saved['closing_treasury']={};saved['case_hash']='forged';self.assertEqual(replay_release_continuity(saved),r)

 def test_unavailable_release_incompatible_path_or_reused_evidence_rejected(self):
  invalid=[{'release_available_month':6,'review_month':5},{'unit_id':'absent'},{'evidence_id':'review-evidence-1'},{'review_engineering_hours':True},{'candidate_coordination':float('nan')},{'legacy_support_through_month':8},{'candidate_operating_rights':1},{'review_payer_role':'someone_else'}]
  for x in invalid:
   with self.subTest(x=x):self.assertRaises(ValueError,run_release_continuity_case,{'release':x})
  saved=copy.deepcopy(self.cases['reviewed_release_supported_legacy']);saved['calendar_bridge']['inputs']['digital_paths']['coordination'][1]=0.2;self.assertRaises(ValueError,replay_release_continuity,saved)

 def test_no_candidate_gain_keeps_review_cost_but_avoids_performance_upgrade_charge(self):
  r=run_release_continuity_case({'release':{'candidate_coordination':0.15}});self.assertEqual(r['release']['resource_cash_cents'],400000);self.assertEqual(r['release']['adopted_month'],7);self.assertFalse(any(i['category']=='software_upgrade_qualification' and i['paid_cents'] for i in r['closing_treasury']['invoices']))

if __name__=='__main__':unittest.main()
