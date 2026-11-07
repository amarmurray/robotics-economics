"""Physical identity, one-resource scheduling, funded qualification and due kits."""
import copy,json,random,unittest
from model.automotive_workcell import workcell_artifact,workcell_inputs,run_workcell,run_workcell_case,replay_workcell

class AutomotiveWorkcell(unittest.TestCase):
 @classmethod
 def setUpClass(cls):cls.c=workcell_artifact()['cases']
 def s(self,name):return self.c[name]['summary']
 def test_competent_human_and_fixed_buffered_both_meet_all_due_kits(self):
  for n in ('human_direct','fixed_buffered','humanoid_buffered','human_refill_buffered'):
   self.assertEqual(self.s(n)['on_time_kits'],12,n);self.assertEqual(self.s(n)['paid_staff_cents'],50000,n)
  self.assertEqual(self.s('human_direct')['staff_person_ticks_used'],72)
  self.assertEqual(self.s('fixed_buffered')['staff_person_ticks_used'],12)
 def test_direct_loading_window_and_prebuffered_process_are_not_same_clock(self):
  direct=self.c['fixed_direct'];buffered=self.c['fixed_buffered'];human=self.c['human_direct']
  self.assertEqual(direct['jobs'][0]['completed_tick'],27);self.assertEqual(direct['jobs'][0]['due_tick'],24)
  self.assertEqual(buffered['jobs'][0]['completed_tick'],21);self.assertEqual(human['jobs'][0]['completed_tick'],24)
  self.assertEqual((self.s('fixed_direct')['on_time_kits'],self.s('fixed_direct')['late_kits'],self.s('fixed_direct')['undelivered_kits']),(0,11,1))
 def test_buffer_switch_and_prefill_require_real_operations(self):
  for cap,expected in ((2,0),(3,12)):
   r=run_workcell_case({'buffer_capacity':cap});self.assertEqual(r['summary']['on_time_kits'],expected)
  r=self.c['fixed_buffered'];self.assertEqual(r['summary']['manipulator_busy_ticks'],36*2+12*3)
  self.assertEqual(sum(e['event']=='start' and e['kind']=='pick' for e in r['events']),36)
  self.assertEqual(r['summary']['operating_and_startup_cash_cents'],20000+10800)
 def test_refill_can_overlap_buffer_handoff_but_not_source_picking(self):
  for n in ('fixed_refill_buffered','human_refill_buffered'):
   r=self.c[n];self.assertEqual(r['summary']['on_time_kits'],12)
   starts=[e for e in r['events'] if e['event']=='start']
   self.assertTrue(any(e['kind']=='handoff' and e['start_tick']<34 and e['end_tick']>24 for e in starts))
   self.assertFalse(any(e['kind'] in ('pick','direct') and e['start_tick']<34 and e['end_tick']>24 for e in starts))
 def test_changeover_switch_is_a_parameter_not_a_robot_label(self):
  for n,expected in [('fixed_mixed_variants',4),('humanoid_mixed_variants',12),('fixed_fast_retool',12)]:self.assertEqual(self.s(n)['on_time_kits'],expected)
  for ticks,expected in [(6,12),(7,9)]:self.assertEqual(run_workcell_case({'mixed_variants':True,'changeover_ticks':ticks})['summary']['on_time_kits'],expected)
  x=workcell_inputs();r=run_workcell(x);x['config']['kind']='humanoid';self.assertEqual(r['summary'],run_workcell(x)['summary'])
 def test_lookahead_does_not_skip_product_runs_and_deadlock_next_kit(self):
  for cap in (3,4,5,6):
   r=run_workcell_case({'mixed_variants':True,'changeover_ticks':1,'buffer_capacity':cap})
   self.assertEqual(r['summary']['on_time_kits'],12)
 def test_prepared_presentation_consumes_capacity_and_cash(self):
  self.assertEqual(run_workcell_case({'prepared_presentation':True,'pick_ticks':3})['inputs']['config']['pick_ticks'],3)
  a=self.s('prepared_presentation');b=self.s('presentation_capacity_short')
  self.assertEqual((a['on_time_kits'],a['prepared_parts_by_horizon'],a['preparation_executed_person_ticks'],a['preparation_cash_cents']),(12,36,72,13600))
  self.assertEqual((b['on_time_kits'],b['prepared_parts_by_horizon'],b['remaining_components']),(11,35,3))
  self.assertGreater(a['operator_outlay_cents'],self.s('fixed_buffered')['operator_outlay_cents'])
 def test_preparation_cannot_precede_material_supply_and_partial_work_counts(self):
  x=workcell_inputs();x['prepared_presentation']=True;x['jobs']=x['jobs'][:1];x['horizon_ticks']=24;x['jobs'][0]['supply_tick']=21
  r=run_workcell(x);parts=r['components']
  self.assertEqual([p['presentation_ready_tick'] for p in parts],[23,25,27])
  self.assertEqual(r['summary']['prepared_parts_by_horizon'],1);self.assertEqual(r['summary']['preparation_executed_person_ticks'],3)
  self.assertEqual(r['summary']['preparation_booked_person_ticks'],6)
 def test_quality_reject_preserves_parts_and_costs_and_never_backfills_deadline(self):
  r=self.c['quality_rework'];s=r['summary'];self.assertEqual((s['on_time_kits'],s['late_kits'],s['handoff_attempts']),(11,1,13))
  self.assertEqual(s['delivered_components'],36);self.assertEqual(s['operator_outlay_cents']-self.s('fixed_buffered')['operator_outlay_cents'],700)
  j=next(j for j in r['jobs'] if j['job_id']=='J04');self.assertGreater(j['completed_tick'],j['due_tick']);self.assertFalse(j['on_time'])
 def test_one_cent_handoff_funding_boundary_leaves_real_buffered_stock(self):
  x=workcell_inputs();x['jobs']=x['jobs'][:1];x['horizon_ticks']=24;x['opening_cash_cents']=70900
  self.assertEqual(run_workcell(x)['summary']['on_time_kits'],1)
  x['opening_cash_cents']=70899;r=run_workcell(x)
  self.assertEqual(r['summary']['on_time_kits'],0);self.assertEqual(r['summary']['operator_outlay_cents'],70600)
  self.assertTrue(all(p['state']=='buffer' for p in r['components']));self.assertEqual(r['summary']['handoff_attempts'],0)
 def test_support_expiry_keeps_owned_units_and_fixed_staff(self):
  r=self.c['support_expires'];self.assertEqual(r['summary']['on_time_kits'],5);self.assertEqual(r['summary']['paid_staff_cents'],50000)
  self.assertEqual(r['assets'][0]['closing_status'],'unsupported_retained')
  self.assertTrue(all(e['end_tick']<=72 for e in r['events'] if e['event']=='start'))
 def test_replacement_is_paid_distinct_and_qualified_after_commissioning(self):
  r=self.c['qualified_replacement'];self.assertEqual((r['summary']['on_time_kits'],r['summary']['late_kits']),(11,1))
  self.assertEqual(r['summary']['robot_units_owned'],2);self.assertEqual(r['summary']['replacement_cash_cents'],40000)
  self.assertTrue(all(e['start_tick']>=84 for e in r['events'] if e['event']=='start' and e['unit_id']=='replacement-resource'))
  u=self.c['unqualified_replacement'];self.assertEqual(u['summary']['on_time_kits'],5);self.assertEqual(u['summary']['robot_units_owned'],2)
  self.assertFalse(any(e['event']=='start' and e['unit_id']=='replacement-resource' for e in u['events']))
 def test_unfunded_unavailable_or_unassumed_rights_cannot_create_replacement(self):
  for r in [self.c['unfunded_replacement'],self.c['replacement_stock_unavailable'],run_workcell_case({'support_until_tick':72,'replacement':True,'replacement_rights':False})]:
   self.assertEqual(r['summary']['robot_units_owned'],1);self.assertEqual(r['summary']['replacement_cash_cents'],0);self.assertEqual(r['summary']['on_time_kits'],5)
 def test_paid_replacement_configuration_does_not_require_failed_old_setup(self):
  x=copy.deepcopy(self.c['qualified_replacement']['inputs']);x['startup_cents']=2000000;r=run_workcell(x)
  self.assertEqual(r['summary']['replacement_status'],'activated');self.assertGreater(r['summary']['delivered_components'],0)
  self.assertFalse(any(e['event']=='start' and e['unit_id']=='opening-resource' for e in r['events']))
 def test_replacement_ready_at_horizon_is_not_falsely_marked_activated(self):
  x=copy.deepcopy(self.c['qualified_replacement']['inputs']);x['replacement']['order_tick']=156;x['replacement']['commission_ticks']=0;r=run_workcell(x)
  self.assertEqual(r['assets'][-1]['closing_status'],'ready_not_activated');self.assertEqual(r['summary']['on_time_kits'],5)
 def test_staff_capacity_and_paid_commitment_gate_operation(self):
  x=workcell_inputs();x['staff_capacity_person_ticks']=0;r=run_workcell(x)
  self.assertEqual(r['summary']['on_time_kits'],0);self.assertGreater(r['summary']['manipulator_busy_ticks'],0)
  x=workcell_inputs();x['opening_cash_cents']=49999;r=run_workcell(x)
  self.assertEqual(r['summary']['on_time_kits'],0);self.assertEqual(r['summary']['due_unpaid_cents'],50000)
 def assert_flow(self,r):
  s=r['summary'];x=r['inputs'];self.assertEqual(s['on_time_kits']+s['late_kits']+s['undelivered_kits'],len(x['jobs']))
  self.assertEqual(s['delivered_components']+s['remaining_components'],3*len(x['jobs']))
  self.assertEqual(len(r['components']),len({p['part_id'] for p in r['components']}));self.assertEqual(s['delivered_components'],3*(s['on_time_kits']+s['late_kits']))
  self.assertLessEqual(s['staff_person_ticks_used'],x['staff_capacity_person_ticks']);self.assertLessEqual(s['max_buffer_parts'],x['buffer_capacity'])
  self.assertEqual(sum(a['cash_cents'] for a in r['opening_treasury']['actors']),sum(a['cash_cents'] for a in r['closing_treasury']['actors']))
  self.assertEqual(s['operator_outlay_cents'],sum(a['cash_cents'] for a in r['closing_treasury']['actors'] if a['actor_id']!='operator'))
  starts=[e for e in r['events'] if e['event']=='start'];self.assertTrue(all(a['end_tick']<=b['start_tick'] for a,b in zip(starts,starts[1:])))
  self.assertTrue(all(e['end_tick']<=x['horizon_ticks'] for e in starts));self.assertEqual(s['manipulator_busy_ticks'],sum(e['end_tick']-e['start_tick'] for e in starts))
  jobs={j['job_id']:j for j in x['jobs']};configs={x['config']['config_id']:x['config']}
  if x['replacement']:configs[x['replacement']['config']['config_id']]=x['replacement']['config']
  for e in starts:
   self.assertLessEqual(e['end_tick'],configs[e['config_id']]['support_until_tick']);self.assertIn(e['variant'],configs[e['config_id']]['qualified_variants'])
   if e['kind'] in ('direct','handoff'):self.assertGreaterEqual(e['start_tick'],jobs[e['job_id']]['release_tick'])
  # Independently replay component state from physical events, with rejection dispositions.
  states={p['part_id']:'raw' for p in r['components']};rejected={(e['job_id'],e['tick']) for e in r['events'] if e['event']=='quality_rejected'}
  for e in r['events']:
   if e['event'] not in ('start','finish'):continue
   kind=e['kind']
   if kind not in ('pick','direct','handoff'):continue
   for p in e['part_ids']:
    if e['event']=='start':
     self.assertEqual(states[p],'buffer' if kind=='handoff' else 'raw');states[p]='in_'+kind
    else:
     self.assertEqual(states[p],'in_'+kind)
     states[p]='buffer' if kind=='pick' or kind=='handoff' and (e['job_id'],e['end_tick']) in rejected else 'raw' if (e['job_id'],e['end_tick']) in rejected else 'delivered'
  self.assertEqual(states,{p['part_id']:p['state'] for p in r['components']})
 def test_all_worlds_conserve_and_replay_complete_inputs(self):
  for name,r in self.c.items():
   self.assert_flow(r);saved=json.loads(json.dumps(r));saved['summary']={'invented':999};saved['case_hash']='tampered';self.assertEqual(replay_workcell(saved),r,name)
 def test_seeded_physical_cash_and_support_adversity(self):
  rng=random.Random(2320)
  for _ in range(30):
   x=workcell_inputs();x['jobs']=x['jobs'][:rng.randrange(1,7)];x['horizon_ticks']=x['jobs'][-1]['due_tick'];x['buffer_capacity']=rng.randrange(7)
   x['opening_cash_cents']=rng.randrange(65000,100001);x['staff_capacity_person_ticks']=rng.randrange(60);x['config']['support_until_tick']=rng.randrange(0,x['horizon_ticks']+1)
   x['config']['pick_ticks']=rng.randrange(1,5);x['config']['changeover_ticks']=rng.randrange(9)
   for j in x['jobs']:j['variant']=rng.choice(['A','B'])
   x['quality_fail_first_job_ids']=[x['jobs'][0]['job_id']] if rng.choice([True,False]) else []
   self.assert_flow(run_workcell(x))
 def test_complete_input_identity_and_types_fail_closed(self):
  for bad in ({'unknown':1},{'mode':'magic'},{'buffer_capacity':True},{'pick_ticks':0},{'source_refill':1},{'opening_cash_cents':None}):
   with self.assertRaises(ValueError):run_workcell_case(bad)
  changes=[lambda x:x.update(extra=1),lambda x:x['jobs'][1]['part_ids'].__setitem__(0,x['jobs'][0]['part_ids'][0]),lambda x:x['config'].update(extra=1),lambda x:x['source_closed_intervals'].append([2,1]),lambda x:x['quality_fail_first_job_ids'].append('unknown')]
  for change in changes:
   x=workcell_inputs();change(x)
   with self.assertRaises(ValueError):run_workcell(x)
  with self.assertRaises(ValueError):replay_workcell({'schema_version':'automotive-workcell/0.1'})
