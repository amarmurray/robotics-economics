import copy,json,unittest
from fractions import Fraction
from pathlib import Path
from model.calendar_bridge import rational
from model.paid_development import paid_development_artifact,run_paid_development_case,replay_paid_development,continuation_comparison
from model.qualified_staffing import available_support

class PaidDevelopmentTests(unittest.TestCase):
 @classmethod
 def setUpClass(cls):
  cls.artifact=paid_development_artifact();cls.cases=cls.artifact['cases'];cls.summary={x['case']:x for x in cls.artifact['summary']}

 def test_one_cash_component_crew_and_service_history_conserves(self):
  for r in self.cases.values():
   self.assertEqual(sum(x['cash_cents'] for x in r['opening_treasury']['actors']),sum(x['cash_cents'] for x in r['closing_treasury']['actors']))
   self.assertEqual(r['entry_transition']['consolidation']['unclassified_boundary_cash_cents'],0)
   outside={'manufacturer','deployment_vendor','enterprise_vendor','digital_vendor','entry_resource_vendor','architecture_resources'}
   self.assertEqual(sum(x['paid_cents'] for x in r['closing_treasury']['invoices'] if x['payee'] in outside),r['staffed_renewals']['cash']['all_payer_resource_and_transaction_cash_cents'])
   for m in r['staffed_renewals']['months']:
    self.assertEqual(sum((rational(x['minutes']) for x in m['bookings']),Fraction())+rational(m['unused_minutes']),m['regular_available_minutes']+m['overtime_paid_minutes'])
   for m in r['component_inventory']['months']:
    for k in m['qualified_closing']:self.assertEqual(m['qualified_opening'][k]+m['qualified_release'][k],m['qualified_closing'][k]+m['manufacturing_issued'][k]+m['service_issued'][k])

 def test_first_pass_matches_prior_total_work_without_double_charging(self):
  prior=json.loads(Path('model/results/architecture_awards.json').read_text())['cases']['licensed_independent'];r=self.cases['pass_first_review']
  self.assertEqual(r['staffed_renewals']['cash'],prior['staffed_renewals']['cash'])
  self.assertEqual(r['competition']['months'],prior['competition']['months'])
  self.assertEqual(r['units'],prior['units']);self.assertEqual(r['development']['resource_cash_cents'],1950000)
  self.assertFalse(any(x['category'] in ('allocated_model_development','qualification_validation','model_adaptation_engineering') for x in r['architecture_execution']['cash_lines']))

 def test_failed_work_stays_paid_and_retry_repeats_only_attempt_work(self):
  r=self.cases['fail_then_pass'];d=r['development'];self.assertEqual([x['status'] for x in d['events']],['failed','passed']);self.assertEqual([x['work_paid_cents'] for x in d['events']],[1950000,1450000]);self.assertEqual(d['resource_cash_cents'],3400000)
  lines=r['architecture_execution']['cash_lines'];self.assertEqual(sum(x['paid_cents'] for x in lines if x['category']=='review_allocated_model_development'),500000)
  self.assertEqual(sum(x['paid_cents'] for x in lines if x['category']=='review_upfront_fee'),300000)
  self.assertEqual([rational(x['engineering_hours']) for x in d['events']],[120,120]);self.assertEqual(r['units'][0]['commissioned_at']['month'],3)
  self.assertEqual(self.summary['fail_then_pass']['notice_effective_months']['incumbent'],6)

 def test_stopping_retains_paid_failure_hardware_and_human_obligations(self):
  r=self.cases['stop_after_paid_failure'];s=self.summary['stop_after_paid_failure'];self.assertEqual(r['development']['failed_review_resource_cash_cents'],1950000);self.assertEqual(s['supported_robot_months'],0);self.assertEqual(r['units'][0]['status'],'transit');self.assertEqual(s['complete_whole_service_months'],8);self.assertEqual(s['outside_completed_jobs'],160);self.assertEqual(rational(s['accepted_zones']),4000)

 def test_no_rights_means_no_review_not_free_qualification(self):
  r=self.cases['no_evidence_rights'];d=r['development'];self.assertEqual(d['completed_attempts'],0);self.assertEqual(d['resource_cash_cents'],0);self.assertEqual(d['passed_unit_ids'],[]);self.assertEqual(d['events'][0]['reason'],'evidence_rights_unavailable');self.assertFalse(any(x['category'].startswith('review_') for x in r['architecture_execution']['cash_lines']))
  self.assertEqual(r['units'][0]['status'],'transit')

 def test_passed_review_is_not_rolled_back_when_provider_delays_admission(self):
  r=run_paid_development_case({'awards':{'qualified':{'resources':available_support(0)}}});self.assertEqual(r['development']['resource_cash_cents'],1950000);self.assertEqual(len(r['development']['passed_unit_ids']),1);self.assertEqual(r['units'][0]['commissioned_at']['month'],6);self.assertEqual(sum(m['flows']['commissioned'] for m in r['months'][2:6]),0);self.assertEqual(len(r['development']['events']),1)
  self.assertEqual(sum(x['paid_cents'] for x in r['architecture_execution']['cash_lines'] if x['category']=='review_allocated_model_development'),500000)

 def test_exact_engineering_threshold_blocks_unperformed_work_atomically(self):
  good=run_paid_development_case({'awards':{'architecture':{'engineering_hours_per_month':120}}});bad=run_paid_development_case({'awards':{'architecture':{'engineering_hours_per_month':119}}})
  self.assertEqual(good['development']['completed_attempts'],1);self.assertEqual(bad['development']['completed_attempts'],0);self.assertEqual(bad['development']['events'][0]['reason'],'engineering_hours_unavailable')
  invoices=[i for i in bad['closing_treasury']['invoices'] if i['category'].startswith('review_')];self.assertTrue(invoices);self.assertTrue(all(i['paid_cents']==0 and i['cancelled_cents']==i['face_cents'] for i in invoices))
  self.assertEqual(sum(rational(m['engineering_hours_used']) for m in bad['architecture_execution']['months']),0)

 def test_wrong_payer_funding_does_not_pool_cash_or_retain_partial_fees(self):
  r=run_paid_development_case({'awards':{'architecture':{'role_opening_cash_cents':{'model_supplier':0,'customer':25000000}}}});d=r['development'];self.assertEqual(d['completed_attempts'],0);self.assertTrue(d['events'][0]['reason'].startswith('funding:'));self.assertEqual(d['resource_cash_cents'],0)
  lines=[x for x in r['architecture_execution']['cash_lines'] if x['category'].startswith('review_')];self.assertTrue(lines);self.assertTrue(all(x['paid_cents']==0 for x in lines));self.assertEqual(sum(x['opening_cash_cents'] for x in r['architecture_execution']['entities']),60000000)

 def test_declared_review_outcome_does_not_create_training_or_customer_output(self):
  for r in self.cases.values():
   self.assertEqual(sum(rational(m['total_delivered_units']) for m in r['enterprise']['months']),4000)
   for m in r['architecture_execution']['months']:
    self.assertLessEqual(rational(m['engineering_hours_used']),r['architecture_execution']['inputs']['engineering_hours_per_month'])
    self.assertLessEqual(rational(m['demonstration_hours_used']),r['architecture_execution']['inputs']['demonstration_hours_per_month'])

 def test_later_scheduled_review_does_not_recharge_a_passed_unit(self):
  inputs=copy.deepcopy(self.artifact['case_inputs']['fail_then_pass']);inputs['development']['attempts'][0]['declared_pass']=True;r=run_paid_development_case(inputs)
  self.assertEqual([x['status'] for x in r['development']['events']],['passed','not_attempted']);self.assertEqual(r['development']['events'][1]['reason'],'already_passed');self.assertEqual(r['development']['resource_cash_cents'],1950000)

 def test_human_alternative_requires_no_development_or_robot(self):
  r=self.cases['human_only_no_development'];self.assertEqual(r['development']['events'],[]);self.assertEqual(r['units'],[]);self.assertEqual(r['staffed_renewals']['cash']['all_payer_resource_and_transaction_cash_cents'],8730000)

 def test_complete_replay_ignores_saved_outcomes_and_requires_opening_contracts(self):
  for r in self.cases.values():
   saved=copy.deepcopy(r);saved['development']['events']=[];saved['development']['passed_unit_ids']=['forged'];saved['architecture_execution']['cash_lines']=[];saved['closing_treasury']={};saved['case_hash']='forged';self.assertEqual(replay_paid_development(saved),r)
  saved=copy.deepcopy(self.cases['pass_first_review']);del saved['development']['inputs'];self.assertRaises(ValueError,replay_paid_development,saved)

 def test_incompatible_configuration_or_review_evidence_fails_before_execution(self):
  base=self.cases['pass_first_review']['development']['inputs'];attempt=base['attempts'][0]
  invalid=[{'configuration_id':'different'},{'attempts':[attempt,attempt]},{'attempts':[{**attempt,'declared_pass':1}]},{'attempts':[{**attempt,'unit_id':'other-unit'}]},{'attempts':[{**attempt,'month':8}]},{'evidence_use_rights':1},{'unknown':0}]
  for d in invalid:
   with self.subTest(d=d):self.assertRaises((ValueError,TypeError),run_paid_development_case,{'development':d})
  self.assertRaises(ValueError,run_paid_development_case,{'awards':{'architecture':{'new_robots':2}}})

 def test_continuation_comparison_excludes_identical_sunk_history(self):
  c=self.artifact['continuation_comparison'];self.assertEqual(c['additional_resource_cash_cents'],2142310);self.assertEqual(c['regular_staff_cash_difference_cents'],-400000);self.assertTrue(c['identical_future_service']);self.assertEqual(rational(c['continued']['accepted_cleaning_zones']),2500);self.assertEqual(c['continued']['completed_inventory_jobs'],100)
  self.assertEqual(sum(x['difference_cents'] for x in c['payer_differences']),c['additional_resource_cash_cents']);self.assertNotEqual(c['continued']['closing_robot_states'],c['stopped']['closing_robot_states'])

 def test_continuation_rejects_a_different_past_or_unmatched_human_only_case(self):
  a=copy.deepcopy(self.cases['fail_then_pass']);b=self.cases['stop_after_paid_failure'];a['months'][0]['closing_cash_cents']['incumbent']+=1;self.assertRaises(ValueError,continuation_comparison,a,b)
  self.assertRaises(ValueError,continuation_comparison,self.cases['fail_then_pass'],self.cases['human_only_no_development'])

if __name__=='__main__':unittest.main()
