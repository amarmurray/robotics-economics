import copy,json,unittest
from pathlib import Path
from model.inspection_price_bounds import compare_inputs,price_bounds_artifact,replay_price_bounds,obligation
from model.utility_inspection import inspection_inputs,run_inspection

class InspectionPriceBoundsTests(unittest.TestCase):
 @classmethod
 def setUpClass(cls):
  cls.artifact=price_bounds_artifact();cls.cases=cls.artifact['comparisons'];cls.original=json.loads(Path('model/results/utility_inspection.json').read_text())
 def test_existing_complete_executions_are_reproduced_without_new_worlds(self):
  self.assertEqual(len(self.original['cases']),18);self.assertEqual(len(self.cases),8)
  for key,r in self.cases.items():
   for role,name in self.artifact['pairs'][key].items():self.assertEqual(r['executions'][role],self.original['cases'][name])
 def test_cash_perimeter_reconciles_for_every_pair(self):
  for r in self.cases.values():
   for c in r['cash'].values():
    self.assertEqual(c['monitor_fees_cents']-c['provider_cash_change_cents'],c['provider_resource_cash_cents']);self.assertEqual(c['customer_outlay_cents']-c['provider_cash_change_cents'],c['consolidated_resource_cash_cents']);self.assertEqual(sum(x['resource_cash_cents']for x in c['payer_resources']),c['consolidated_resource_cash_cents'])
   if r['bounds']:
    v=r['bounds'];self.assertEqual(v['interval_width_cents'],v['customer_fee_ceiling_cents']-v['provider_recorded_resource_recovery_cents']);self.assertEqual(v['interval_width_cents'],v['baseline_provider_cash_change_cents']-v['consolidated_resource_change_cents'])
 def test_retained_paid_crew_can_leave_a_negative_fee_ceiling(self):
  r=self.cases['retained_paid_crew'];v=r['bounds'];self.assertEqual(v['customer_fee_ceiling_cents'],-4000);self.assertEqual(v['provider_recorded_resource_recovery_cents'],27800);self.assertEqual(v['further_net_customer_value_needed_at_recorded_fee_cents'],48000);self.assertEqual(v['further_net_customer_value_needed_at_resource_recovery_cents'],31800)
  self.assertEqual(r['executions']['baseline']['summary']['paid_field_crew_cents'],r['executions']['alternative']['summary']['paid_field_crew_cents'])
 def test_avoidable_visit_bounds_do_not_impute_downstream_value(self):
  v=self.cases['avoidable_visit']['bounds'];self.assertEqual(v['customer_fee_ceiling_cents'],116000);self.assertEqual(v['provider_recorded_resource_recovery_cents'],27800);self.assertEqual(v['interval_width_cents'],88200);self.assertEqual(v['further_net_customer_value_needed_at_recorded_fee_cents'],0)
 def test_existing_fixed_alternative_changes_the_buyer_comparator(self):
  v=self.cases['mobile_against_fixed']['bounds'];self.assertEqual(v['customer_fee_ceiling_cents'],22000);self.assertEqual(v['interval_width_cents'],-5800);self.assertEqual(v['consolidated_resource_change_cents'],13400);self.assertEqual(v['baseline_provider_cash_change_cents'],7600)
 def test_physical_duties_and_fallback_retain_paid_service(self):
  for key in ['physical_duty_remains','one_bad_reading']:
   v=self.cases[key]['bounds'];self.assertEqual(v['customer_fee_ceiling_cents'],-12000);self.assertEqual(v['further_net_customer_value_needed_at_recorded_fee_cents'],56000)
 def test_incomplete_or_unfunded_monitoring_is_not_assigned_a_price_bound(self):
  for key in ['late_fallback_not_matched','unfunded_provider_not_priced']:
   r=self.cases[key];self.assertFalse(r['comparison']['eligible']);self.assertIsNone(r['bounds']);self.assertTrue(r['comparison']['reasons']);self.assertIn('alternative',r['cash'])
 def test_different_physical_obligation_or_presence_is_not_equivalent(self):
  x=copy.deepcopy(self.cases['avoidable_visit']['inputs']);x['alternative']['field_duty_cycles']=[0];r=compare_inputs(x);self.assertIsNone(r['bounds']);self.assertTrue(any('field_duty_cycles'in x for x in r['comparison']['reasons']))
  x=copy.deepcopy(self.cases['avoidable_visit']['inputs']);x['alternative']['replacement_authorized']=False;r=compare_inputs(x);self.assertIsNone(r['bounds']);self.assertTrue(any('presence_cycles'in x for x in r['comparison']['reasons']))
 def test_required_identity_order_is_not_a_different_service(self):
  x=copy.deepcopy(self.cases['avoidable_visit']['inputs']);x['alternative']['required_points'].reverse();self.assertEqual(compare_inputs(x)['bounds'],self.cases['avoidable_visit']['bounds'])
 def test_one_cent_visit_bill_boundary_is_exact(self):
  x=copy.deepcopy(self.cases['avoidable_visit']['inputs'])
  for cents,width in [(7949,-4),(7950,0),(7951,4)]:
   x['baseline']['visit_crew_cents']=cents;r=compare_inputs(x);self.assertEqual(r['bounds']['interval_width_cents'],width);self.assertEqual(r['bounds']['window_interval_nonempty'],width>=0)
 def test_same_total_fee_does_not_guarantee_provider_funding_timing(self):
  x=copy.deepcopy(self.cases['fixed_qualified_alternative']['inputs']);x['alternative']['channels'][0].update(initial_fee_cents=0,cycle_fee_cents=5500);r=compare_inputs(x)
  self.assertEqual(r['cash']['alternative']['monitor_fees_cents'],self.cases['fixed_qualified_alternative']['cash']['alternative']['monitor_fees_cents']);self.assertEqual(r['executions']['alternative']['summary']['complete_service_windows'],4);self.assertIn('alternative:unfunded_monitoring_booking',r['comparison']['reasons']);self.assertIsNone(r['bounds'])
 def test_unpaid_commitments_or_absent_monitoring_service_reject_bounds(self):
  x=copy.deepcopy(self.cases['avoidable_visit']['inputs']);x['alternative']['utility_cash_cents']=0;r=compare_inputs(x);self.assertIn('alternative:unpaid_commitments',r['comparison']['reasons']);self.assertIsNone(r['bounds'])
  x=copy.deepcopy(self.cases['avoidable_visit']['inputs']);x['alternative']=copy.deepcopy(x['baseline']);r=compare_inputs(x);self.assertIn('alternative:no_monitoring_service',r['comparison']['reasons']);self.assertIsNone(r['bounds'])
 def test_replay_ignores_forged_cash_eligibility_and_executions(self):
  for r in self.cases.values():
   saved=copy.deepcopy(r);saved.update(bounds={'interval_width_cents':999999},comparison={'eligible':True},cash={},executions={},case_hash='forged');self.assertEqual(replay_price_bounds(saved),r)
 def test_input_schema_and_exact_money_are_validated(self):
  for x in [None,{},[],{'baseline':{},'alternative':{},'extra':1}]:
   with self.assertRaises(ValueError):compare_inputs(x)
  x=copy.deepcopy(self.cases['avoidable_visit']['inputs']);x['alternative']['visit_crew_cents']=True
  with self.assertRaises(ValueError):compare_inputs(x)

if __name__=='__main__':unittest.main()
