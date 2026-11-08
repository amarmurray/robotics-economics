"""Adverse qualification, data lineage, physical and Treasury conservation."""
import copy,json,random,unittest
from model.learning_execution import learning_inputs,run_learning,run_learning_case,learning_artifact,replay_learning


class LearningExecution(unittest.TestCase):
    @classmethod
    def setUpClass(cls):cls.c=learning_artifact()['cases']
    def s(self,name):return self.c[name]['summary']

    def test_data_and_actual_qualification_precede_candidate_service(self):
        r=self.c['qualified_feedback'];self.assertFalse(any(e['kind']=='candidate_built' and e['cycle']==0 for e in r['events']))
        self.assertTrue(r['summary']['candidate_built']);self.assertEqual(r['summary']['qualified_units'],2)
        built=next(e for e in r['events'] if e['kind']=='candidate_built')
        episodes={e['episode_id']:e for e in r['episodes']}
        self.assertTrue(all(episodes[i]['eligible'] and episodes[i]['cycle']<built['cycle'] for i in r['training_episode_ids']))
        for a in r['assets']:
            trial=next(w for w in r['physical_windows'] if w['window_id']==a['trial_window_id'])
            self.assertEqual(trial['kind'],'qualification');self.assertGreaterEqual(trial['physical']['summary']['on_time_kits'],4)
            self.assertGreaterEqual(a['qualified_cycle'],a['module_ready_cycle'])
        self.assertGreater(self.s('qualified_feedback')['on_time_service_kits'],self.s('no_research')['on_time_service_kits'])

    def test_no_learning_keeps_failed_research_cost_and_no_gain(self):
        r=self.c['no_learning'];self.assertTrue(r['summary']['candidate_built'])
        self.assertEqual(r['summary']['qualified_units'],0);self.assertEqual(r['summary']['qualification_attempts'],1)
        self.assertEqual(r['summary']['on_time_service_kits'],self.s('no_research')['on_time_service_kits'])
        self.assertGreater(r['summary']['operator_outlay_cents'],self.s('no_research')['operator_outlay_cents'])
        self.assertGreater(r['summary']['training_cash_cents'],0)

    def test_no_transfer_and_retained_regression_keep_old_configuration(self):
        for name in ('no_transfer','retained_regression'):
            r=self.c[name];assets={a['unit_id']:a for a in r['assets']}
            self.assertEqual(assets['retained-unit']['active_config_id'],'retained-unit-v1')
            self.assertTrue(assets['target-unit']['production_active']);self.assertEqual(r['summary']['qualified_units'],1)
        a=self.c['retained_regression'];self.assertEqual(a['assets'][0]['qualification_status'],'failed')
        self.assertGreater(a['summary']['operator_outlay_cents'],self.s('no_transfer')['operator_outlay_cents'])
        self.assertEqual(a['summary']['on_time_service_kits'],self.s('no_transfer')['on_time_service_kits'])

    def test_rights_sensor_validity_and_unique_episode_denominators(self):
        for name in ('no_training_rights','invalid_observations'):
            s=self.s(name);self.assertGreater(s['unique_collected_episodes'],0)
            self.assertEqual(s['unique_eligible_episodes'],0);self.assertFalse(s['candidate_built']);self.assertEqual(s['training_cash_cents'],0)
        a,b=self.c['qualified_feedback'],self.c['duplicate_observations']
        self.assertEqual(a['episodes'],b['episodes']);self.assertEqual(a['summary'],b['summary'])
        self.assertEqual(a['training_episode_ids'],b['training_episode_ids'])
        self.assertGreater(sum(e.get('duplicates_ignored',0) for e in b['events']),0)

    def test_held_out_trial_output_is_neither_training_nor_customer_service(self):
        r=self.c['qualified_feedback'];self.assertEqual(r['summary']['due_service_kits'],72)
        self.assertEqual(r['summary']['qualification_attempts'],2)
        self.assertGreater(r['summary']['qualification_on_time_kits'],0)
        trial_ids={j['job_id'] for w in r['physical_windows'] if w['kind']=='qualification' for j in w['physical']['jobs']}
        self.assertFalse(trial_ids & {e['job_id'] for e in r['episodes']})
        self.assertEqual(r['summary']['robot_units_owned'],2)
        self.assertEqual(len({a['unit_id'] for a in r['assets']}),2)

    def test_quality_failure_is_funded_and_candidate_not_activated(self):
        s=self.s('failed_target_quality');self.assertEqual(s['qualified_units'],0);self.assertEqual(s['qualification_attempts'],1)
        self.assertGreater(s['qualification_staff_cash_cents'],0)
        self.assertEqual(s['on_time_service_kits'],self.s('no_research')['on_time_service_kits'])
        self.assertEqual(self.c['failed_target_quality']['assets'][1]['qualification_status'],'failed')

    def test_finite_priority_changes_support_without_inventing_staff(self):
        a,b=self.c['support_priority'],self.c['candidate_priority']
        self.assertEqual(a['summary']['unsupported_unit_cycles'],0);self.assertGreater(b['summary']['unsupported_unit_cycles'],0)
        self.assertGreater(a['summary']['on_time_service_kits'],b['summary']['on_time_service_kits'])
        self.assertEqual(a['summary']['production_staff_cash_cents'],b['summary']['production_staff_cash_cents'])
        # Deferred qualification can resume in a later cycle with the same candidate.
        self.assertEqual(a['summary']['qualified_units'],2)
        self.assertEqual(sum(e['kind']=='candidate_built' for e in a['events']),1)
        self.assertEqual(a['summary']['robot_units_owned'],b['summary']['robot_units_owned'])

    def test_physical_validation_slot_has_exact_boundary(self):
        a=self.c['validation_slot_short'];self.assertTrue(a['summary']['candidate_built'])
        self.assertEqual(a['summary']['qualification_attempts'],0);self.assertEqual(a['summary']['qualified_units'],0)
        self.assertEqual(self.c['qualified_feedback']['inputs']['validation_ticks_per_unit_cycle'],156)
        self.assertEqual(a['inputs']['validation_ticks_per_unit_cycle'],155)
        self.assertGreater(a['summary']['training_cash_cents'],0)

    def test_paid_order_is_neither_delivered_nor_qualified_robot(self):
        late=self.c['module_after_horizon'];s=late['summary']
        self.assertEqual(s['modules_ordered'],1);self.assertEqual(s['modules_delivered'],0)
        self.assertEqual(s['qualified_units'],0);self.assertEqual(s['robot_units_owned'],2)
        self.assertGreater(sum(c['paid_cents'] for c in late['charges'] if c['category']=='compatible_module_order'),0)
        bad=self.s('incompatible_module');self.assertEqual(bad['modules_delivered'],1);self.assertEqual(bad['qualification_attempts'],0)
        self.assertLess(self.s('delayed_module')['on_time_service_kits'],self.s('qualified_feedback')['on_time_service_kits'])
        for w in self.c['delayed_module']['physical_windows']:
            if w['kind']=='qualification':
                a=next(a for a in self.c['delayed_module']['assets'] if a['unit_id']==w['unit_id'])
                self.assertGreaterEqual(w['cycle'],a['module_ready_cycle'])

    def test_conventional_qualified_retool_has_same_service_and_no_data_premium(self):
        s=self.s('conventional_fast_retool');self.assertEqual(s['on_time_service_kits'],72)
        self.assertFalse(s['candidate_built']);self.assertEqual(s['qualified_units'],0)
        self.assertEqual(s['robot_units_owned'],2);self.assertEqual(s['production_staff_cash_cents'],300000)
        self.assertIsNone(s['removed_payroll_cents'])

    def test_training_one_cent_funding_boundary(self):
        first=run_learning_case({'cycles':1})['summary']['operator_outlay_cents']
        x=learning_inputs();x['cycles']=2
        threshold=first+2*x['support_hours_per_unit']*x['engineering_cents_per_hour']+x['training_hours']*x['engineering_cents_per_hour']+x['training_compute_cents']
        x['workcell']['opening_cash_cents']=threshold-1;low=run_learning(x)
        x['workcell']['opening_cash_cents']=threshold;high=run_learning(x)
        self.assertFalse(low['summary']['candidate_built']);self.assertTrue(high['summary']['candidate_built'])
        self.assertEqual(high['summary']['qualified_units'],0);self.assertGreater(high['summary']['due_unpaid_cents'],0)

    def test_initial_setup_cannot_become_free_in_later_cycles(self):
        x=learning_inputs();x['learning_enabled']=False;x['collection_allowed']=False
        x['workcell']['staff_cents']=0;x['engineering_cents_per_hour']=0
        x['workcell']['opening_cash_cents']=19999
        r=run_learning(x);self.assertEqual(r['summary']['on_time_service_kits'],0)
        self.assertTrue(all(not a['baseline_setup_funded'] for a in r['assets']))
        self.assertTrue(all(w['physical']['inputs']['startup_cents']==20000 for w in r['physical_windows']))

    def test_paid_turnaround_preserves_recipe_and_quarantined_inventory(self):
        r=self.c['no_research'];self.assertGreater(r['summary']['turnaround_person_ticks'],0)
        self.assertEqual(r['summary']['turnaround_cash_cents'],r['summary']['turnaround_person_ticks']*r['inputs']['turnaround_cents_per_person_tick'])
        cleared=[i for t in r['turnarounds'] if t['performed'] for i in t['buffered_component_ids']]
        self.assertEqual(len(cleared),len(set(cleared)))
        self.assertEqual(set(cleared),{i for s in r['closing_physical_state'].values() for i in s['quarantined_component_ids']})
        blocked=run_learning_case({'learning_enabled':False,'turnaround_capacity_person_ticks_per_unit_cycle':0})
        self.assertLess(blocked['summary']['on_time_service_kits'],r['summary']['on_time_service_kits'])
        self.assertEqual(blocked['summary']['production_staff_cash_cents'],r['summary']['production_staff_cash_cents'])

    def assert_conservation(self,r):
        s=r['summary'];self.assertEqual(s['due_service_kits'],s['on_time_service_kits']+s['late_service_kits']+s['undelivered_service_kits'])
        opening=sum(a['cash_cents'] for a in r['opening_treasury']['actors']);closing=sum(a['cash_cents'] for a in r['closing_treasury']['actors'])
        self.assertEqual(opening,closing);self.assertEqual(s['operator_outlay_cents'],sum(c['paid_cents'] for c in r['charges']))
        self.assertEqual(s['due_unpaid_cents'],sum(i['outstanding_cents'] for i in r['closing_treasury']['invoices']))
        self.assertEqual(s['engineering_hours_used'],sum(a['hours'] for a in r['engineering_allocations']))
        components=[]
        for w in r['physical_windows']:
            components.extend(p['part_id'] for p in w['physical']['components'])
            cash=sum(c['paid_cents'] for c in r['charges'] if c['stage']==w['window_id'])
            self.assertEqual(cash,w['physical']['summary']['operator_outlay_cents'])
            if w['kind']=='qualification':self.assertLessEqual(w['physical']['inputs']['horizon_ticks'],r['inputs']['validation_ticks_per_unit_cycle'])
        self.assertEqual(len(components),len(set(components)))
        for c in r['cycles']:
            self.assertEqual(c['engineering_hours_used'],sum(a['hours'] for a in r['engineering_allocations'] if a['cycle']==c['cycle']))
            self.assertLessEqual(c['engineering_hours_used'],c['engineering_hours_available'])
            for ticks in c['turnaround_person_ticks'].values():self.assertLessEqual(ticks,r['inputs']['turnaround_capacity_person_ticks_per_unit_cycle'])
        for e in r['episodes']:self.assertIn('-production-',e['episode_id'])

    def test_all_worlds_conserve_cash_resources_components_and_service(self):
        for r in self.c.values():self.assert_conservation(r)

    def test_complete_replay_ignores_saved_outputs(self):
        r=self.c['no_transfer'];saved=json.loads(json.dumps(r));saved['summary']={'free_service':999};saved['case_hash']='tampered'
        self.assertEqual(replay_learning(saved),r)

    def test_seeded_cash_engineering_rights_and_delivery_cases(self):
        rng=random.Random(2201)
        for _ in range(12):
            x=learning_inputs();x['cycles']=2;x['engineering_hours_per_cycle']=rng.randrange(0,27)
            x['workcell']['opening_cash_cents']=rng.randrange(60000,500001);x['module_lead_cycles']=rng.randrange(4)
            x['priority']=rng.choice(['support_first','candidate_first']);x['training_rights']=rng.choice([True,False])
            x['minimum_eligible_episodes']=rng.randrange(1,25);self.assert_conservation(run_learning(x))

    def test_fail_closed_on_invalid_inputs(self):
        for o in ({'cycles':True},{'cycles':0},{'priority':'magic'},{'training_rights':1},{'module_lead_cycles':7},{'target_candidate_changeover_ticks':-1},{'minimum_eligible_episodes':0},{'extra':1}):
            with self.assertRaises(ValueError):run_learning_case(o)
        x=learning_inputs();x['workcell']['replacement']={}
        with self.assertRaises(ValueError):run_learning(x)
        with self.assertRaises(ValueError):replay_learning({'schema_version':'learning-execution/0.1'})
