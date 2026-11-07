"""Accepted service, funded resource and exact residual-visit boundaries."""
import copy,json,random,unittest
from model.utility_inspection import POINTS,inspection_artifact,inspection_inputs,replay_inspection,run_inspection,run_inspection_case

class InspectionService(unittest.TestCase):
 @classmethod
 def setUpClass(cls):cls.artifact=inspection_artifact();cls.c=cls.artifact['cases']
 def s(self,name):return self.c[name]['summary']
 def test_fixed_commitment_survives_all_released_field_time(self):
  a,b=self.s('human_committed'),self.s('mobile_complete_committed')
  self.assertEqual(a['paid_field_crew_cents'],b['paid_field_crew_cents']);self.assertEqual(b['paid_field_crew_cents'],100000)
  self.assertEqual((a['field_person_minutes'],b['field_person_minutes']),(592,0))
  self.assertGreater(b['operator_outlay_cents'],a['operator_outlay_cents'])
 def test_one_residual_point_retains_full_visit_and_staff(self):
  a,b=self.s('human_committed'),self.s('mobile_residual')
  self.assertEqual(b['remote_accepted_point_windows'],44);self.assertEqual(b['visits_completed'],4)
  self.assertEqual((b['complete_service_windows'],b['paid_field_crew_cents']),(4,100000))
  self.assertEqual(a['field_person_minutes']-b['field_person_minutes'],176)
  self.assertEqual(a['executed_person_minutes']-b['executed_person_minutes'],48)
 def test_per_visit_cash_switch_requires_complete_coverage(self):
  for fee in (11999,12000,12001):
   human=run_inspection_case({'mode':'human','staffing':'per_visit','visit_crew_cents':fee})['summary']
   mobile=run_inspection_case({'mobile_points':12,'staffing':'per_visit','visit_crew_cents':fee})['summary']
   self.assertEqual(mobile['operator_outlay_cents']-human['operator_outlay_cents'],4*(12000-fee))
  bad=self.s('one_bad_reading');self.assertEqual(bad['operator_outlay_cents']-self.s('human_per_visit')['operator_outlay_cents'],56000)
 def test_complete_fixed_alternative_and_qualification_are_explicit(self):
  self.assertEqual(self.s('fixed_complete_avoidable')['complete_service_windows'],4)
  self.assertLess(self.s('fixed_complete_avoidable')['operator_outlay_cents'],self.s('mobile_complete_avoidable')['operator_outlay_cents'])
  self.assertEqual(self.s('fixed_partial')['visits_completed'],4)
  self.assertEqual(self.s('unqualified_last_point')['remote_accepted_point_windows'],44)
 def test_overlap_is_union_not_sum_and_complementarity_can_close_it(self):
  a,b=self.s('mixed_overlap_residual'),self.s('mixed_complementary')
  self.assertEqual((a['raw_captures'],a['remote_accepted_point_windows'],a['visits_completed']),(76,44,4))
  self.assertEqual((b['raw_captures'],b['remote_accepted_point_windows'],b['visits_completed']),(56,48,0))
 def test_duplicate_capture_costs_remain_without_extra_accepted_output(self):
  a,b=self.s('mobile_complete_committed'),self.s('duplicate_captures')
  self.assertEqual(b['raw_captures'],2*a['raw_captures']);self.assertEqual(b['accepted_point_windows'],a['accepted_point_windows'])
  self.assertEqual(b['review_person_minutes'],a['review_person_minutes'])
  self.assertEqual(b['external_resource_cash_cents']-a['external_resource_cash_cents'],4800)
  self.assertEqual(a['provider_net_cash_change_cents']-b['provider_net_cash_change_cents'],4800)
 def test_review_capacity_exact_boundary(self):
  for cap,visits in ((23,4),(24,0)):
   s=run_inspection_case({'mobile_points':12,'review_capacity_person_minutes':cap})['summary']
   self.assertEqual(s['visits_completed'],visits);self.assertLessEqual(s['review_person_minutes'],4*cap)
 def test_review_deadline_and_bad_quality_do_not_erase_attempts(self):
  x=inspection_inputs();x['channels'][1]['coverage_ids']=POINTS[:];x['decision_minute']=33
  r=run_inspection(x);self.assertEqual(r['summary']['raw_captures'],48);self.assertEqual(r['summary']['remote_accepted_point_windows'],44)
  x['decision_minute']=34;self.assertEqual(run_inspection(x)['summary']['remote_accepted_point_windows'],48)
  a=self.s('one_bad_reading');self.assertEqual(a['review_person_minutes'],96)
 def test_field_work_and_policy_visit_are_separate_gates(self):
  for name in ('field_duty_remains','replacement_not_authorized'):
   s=self.s(name);self.assertEqual(s['remote_accepted_point_windows'],48);self.assertEqual(s['visits_completed'],4)
  # Match the added field duty in the human comparator, rather than omitting it.
  self.assertEqual(self.s('human_field_duty')['field_person_minutes'],672)
  x=copy.deepcopy(self.c['field_duty_remains']['inputs']);x['field_capacity_person_minutes']=0
  r=run_inspection(x);self.assertEqual(r['summary']['accepted_point_windows'],48);self.assertEqual(r['summary']['complete_service_windows'],0)
 def test_late_fallback_loses_service_not_prepaid_staff_and_attempts(self):
  s=self.s('fallback_late');self.assertEqual((s['raw_captures'],s['accepted_point_windows'],s['complete_service_windows']),(48,44,0))
  self.assertEqual(s['paid_field_crew_cents'],100000);self.assertEqual(s['visits_completed'],0)
  self.assertEqual(run_inspection_case({'mode':'human','deadline_minute':90})['summary']['complete_service_windows'],4)
 def test_exact_cash_boundary_and_atomic_visit_failure(self):
  x=inspection_inputs();x['cycles']=1;x['staffing']='per_visit'
  for c in x['channels']:c['enabled']=False
  x['utility_cash_cents']=32000;self.assertEqual(run_inspection(x)['summary']['complete_service_windows'],1)
  x['utility_cash_cents']=31999;r=run_inspection(x)
  self.assertEqual(r['summary']['complete_service_windows'],0);self.assertEqual(r['summary']['operator_outlay_cents'],0)
  self.assertTrue(all(i['paid_cents']==0 and i['outstanding_cents']==0 for i in r['closing_treasury']['invoices']))
 def test_customer_payment_does_not_create_provider_resources(self):
  r=self.c['provider_resource_shortfall'];s=r['summary']
  self.assertEqual(s['internal_monitor_fees_cents'],44000);self.assertEqual(s['raw_captures'],0)
  self.assertEqual(s['provider_net_cash_change_cents'],44000);self.assertEqual(s['visits_completed'],4)
  self.assertTrue(any(not f['funded'] and f['conditional'] for f in r['funding']))
 def test_unpaid_committed_staff_retains_obligation_and_blocks_human_work(self):
  x=inspection_inputs();x['cycles']=1;x['utility_cash_cents']=24999
  for c in x['channels']:c['enabled']=False
  r=run_inspection(x);self.assertEqual(r['summary']['complete_service_windows'],0);self.assertEqual(r['summary']['due_unpaid_cents'],25000)
  self.assertEqual(r['cycles'][0]['visit_reason'],'unfunded_committed_staff')
 def test_review_is_not_free_when_unfunded(self):
  x=inspection_inputs();x['cycles']=1;x['staffing']='per_visit';x['utility_cash_cents']=2999
  c=x['channels'][1];c['initial_fee_cents']=0;c['cycle_fee_cents']=100;c['initial_resource_cents']=0;c['cycle_resource_cents']=0;c['attempt_resource_cents']=0
  r=run_inspection(x);self.assertEqual(r['summary']['raw_captures'],11);self.assertEqual(r['summary']['remote_accepted_point_windows'],0)
  self.assertTrue(all(o['status']=='review_not_funded' for o in r['cycles'][0]['observations']))
 def invariants(self,r):
  s=r['summary'];self.assertEqual(s['required_point_windows'],s['accepted_point_windows']+s['unaccepted_point_windows'])
  self.assertEqual(sum(a['cash_cents'] for a in r['opening_treasury']['actors']),sum(a['cash_cents'] for a in r['closing_treasury']['actors']))
  self.assertEqual(s['operator_outlay_cents']-s['provider_net_cash_change_cents'],s['external_resource_cash_cents'])
  for c in r['cycles']:
   ids=[a['point_id'] for a in c['accepted_points']];self.assertEqual(len(ids),len(set(ids)))
   self.assertEqual(set(ids)|set(c['unaccepted_point_ids']),set(r['inputs']['required_points']))
   self.assertFalse(set(ids)&set(c['unaccepted_point_ids']));self.assertLessEqual(c['review_person_minutes'],r['inputs']['review_capacity_person_minutes'])
   if c['service_complete']:self.assertEqual(len(ids),len(r['inputs']['required_points']))
   if c['visit_completed']:self.assertLessEqual(c['field_person_minutes'],r['inputs']['field_capacity_person_minutes'])
 def test_every_saved_world_conserves_and_replays_complete_inputs(self):
  for name,r in self.c.items():
   self.invariants(r);saved=json.loads(json.dumps(r));saved['summary']={'invented':99};saved['case_hash']='tampered'
   self.assertEqual(replay_inspection(saved),r,name)
 def test_seeded_adverse_capacity_cash_quality_cases(self):
  rng=random.Random(2319)
  for _ in range(30):
   x=inspection_inputs();x['cycles']=rng.randrange(1,5);x['utility_cash_cents']=rng.randrange(0,150000);x['provider_cash_cents']=rng.randrange(0,10000)
   x['field_capacity_person_minutes']=rng.randrange(200);x['review_capacity_person_minutes']=rng.randrange(35);x['staffing']=rng.choice(['committed','per_visit'])
   x['deadline_minute']=rng.randrange(60,181)
   for c in x['channels']:
    c['enabled']=rng.choice([True,False]);c['coverage_ids']=rng.sample(POINTS,rng.randrange(13));c['bad_quality_ids']=rng.sample(POINTS,3)
   self.invariants(run_inspection(x))
 def test_identity_unknown_fields_null_bool_and_bounds_fail_closed(self):
  for bad in ({'unknown':1},{'mobile_points':True},{'review_capacity_person_minutes':None},{'mobile_repeats':0},{'field_duty':1},{'deadline_minute':59}):
   with self.assertRaises(ValueError):run_inspection_case(bad)
  for alter in (lambda x:x['required_points'].append('P01'),lambda x:x['channels'][0]['coverage_ids'].append('unknown'),lambda x:x.update(extra=1),lambda x:x['channels'][0].update(extra=1)):
   x=inspection_inputs();alter(x)
   with self.assertRaises(ValueError):run_inspection(x)
  with self.assertRaises(ValueError):replay_inspection({'schema_version':'utility-inspection/0.1'})
