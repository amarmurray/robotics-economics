"""Independent optimality oracle and adverse service/cash/authority witnesses."""
import copy
from dataclasses import asdict,replace
import itertools
import random
import unittest
from unittest.mock import patch
from model.conventional_coordination import (Controller,Mode,Outage,Request,Workload,
    coordination_artifact,exact_plan,reference_workload,replay_coordination,run_coordination)


def exhaustive_oracle(snapshot):
    """Cartesian enumeration with set-valued occupancy; no planner helpers."""
    alternatives=[]
    for request in sorted(snapshot['pending'],key=lambda r:r['request_id']):
        choices=[None]
        for mode in request['modes']:
            for start in range(max(snapshot['tick'],request['release']),request['deadline']-mode['duration']+1):
                if start+mode['duration']>snapshot['horizon']:continue
                slots={(resource,t) for resource,offset,length in mode['claims'] for t in range(start+offset,start+offset+length)}
                if not request['mandatory'] and any(resource=='courier' and snapshot['urgent_reserve_mask']&(1<<t) for resource,t in slots):continue
                choices.append((request,mode,start,slots))
        alternatives.append(choices)
    initial={(resource,t) for resource,mask in zip(('courier','robot'),snapshot['occupied_masks']) for t in range(snapshot['horizon']) if mask&(1<<t)}
    best=((0,0,0,0),())
    for candidate in itertools.product(*alternatives):
        selected=[x for x in candidate if x];occupied=set(initial);cost=0;valid=True
        for request,mode,start,slots in selected:
            if occupied&slots:valid=False;break
            occupied|=slots;cost+=mode['resource_cents']
        if not valid or cost>snapshot['available_cash_cents']:continue
        score=(sum(int(r['mandatory']) for r,m,t,s in selected),len(selected),-cost,-sum(t+m['duration'] for r,m,t,s in selected))
        actions=tuple(sorted((t,r['request_id'],m['mode_id']) for r,m,t,s in selected))
        if score>best[0] or (score==best[0] and actions<best[1]):best=score,actions
    return best


class ConventionalCoordination(unittest.TestCase):
    @classmethod
    def setUpClass(cls):cls.artifact=coordination_artifact();cls.cases=cls.artifact['cases']

    def test_exact_solver_matches_independent_exhaustive_small_worlds(self):
        rng=random.Random(1717)
        for trial in range(40):
            jobs=[]
            for index in range(3):
                modes=tuple(Mode(name,rng.randint(1,2),((resource,0,1),),rng.randint(0,4)) for name,resource in [('h','courier'),('r','robot')])
                jobs.append(asdict(Request(str(index),0,rng.randint(2,5),bool(rng.randrange(2)),modes)))
            snapshot={'tick':0,'horizon':5,'pending':jobs,'occupied_masks':[rng.randrange(8),rng.randrange(8)],
                      'urgent_reserve_mask':rng.randrange(8),'available_cash_cents':rng.randrange(9)}
            actual=exact_plan(snapshot);expected=exhaustive_oracle(snapshot)
            self.assertEqual(tuple(actual['objective']),expected[0],trial)
            self.assertEqual(tuple((a['start'],a['request_id'],a['mode_id']) for a in actual['actions']),expected[1],trial)

    def test_solver_state_budget_fails_without_optimality_claim(self):
        with patch('model.conventional_coordination.MAX_STATES',1):
            with self.assertRaisesRegex(ValueError,'no optimality claim'):exact_plan(self.cases['mixed_exact']['observations'][0])

    def test_reference_waits_and_replans_instead_of_forcing_greedy_launch(self):
        r=self.cases['mixed_exact'];starts=[e for e in r['events'] if e['kind']=='started']
        self.assertEqual(starts[0]['start'],1)
        self.assertEqual(r['summary']['accepted'],4)
        self.assertTrue(r['summary']['mandatory_service_gate_met'])
        self.assertNotIn('urgent-E',r['proposals'][0]['plan']['observed_request_ids'])
        self.assertIn('urgent-E',r['proposals'][2]['plan']['observed_request_ids'])

    def test_same_total_completion_can_hide_a_mandatory_miss(self):
        a=self.cases['mixed_exact']['summary'];b=self.cases['no_urgent_reserve']['summary']
        self.assertEqual(a['accepted'],b['accepted'])
        self.assertEqual((a['mandatory_accepted'],b['mandatory_accepted']),(1,0))

    def test_policy_cannot_see_future_arrivals_or_outages(self):
        w=reference_workload();requests=tuple(replace(r,modes=(replace(r.modes[0],resource_cents=999),)) if r.release>=4 else r for r in w.requests)
        changed=run_coordination(replace(w,requests=requests,outage=Outage(7,9)))
        base=self.cases['mixed_exact']
        for key,time in [('observations','tick'),('proposals','as_of'),('admissions','tick')]:
            self.assertEqual([r for r in base[key] if r[time]<4],[r for r in changed[key] if r[time]<4])

    def test_matching_labels_change_no_operational_or_cash_outcome(self):
        a=self.cases['mixed_exact'];b=self.cases['matched_proposal_alias']
        for key in ('summary','accepted_requests','events','cost_lines','closing_treasury','observations','admissions'):
            self.assertEqual(a[key],b[key],key)

    def test_latency_costs_time_and_fast_path_preserves_urgent_service(self):
        b=self.cases['delayed_proposal']['summary'];f=self.cases['delayed_with_urgent_fast_path']['summary']
        self.assertEqual((b['accepted'],b['mandatory_accepted']),(3,0))
        self.assertEqual((f['accepted'],f['mandatory_accepted']),(4,1))
        self.assertEqual(f['controller_calls'],13)
        self.assertEqual(f['declared_decision_slots'],12)

    def test_overhead_is_paid_even_when_service_does_not_improve(self):
        a=self.cases['mixed_exact'];b=self.cases['extra_proposal_overhead']
        self.assertEqual(a['accepted_requests'],b['accepted_requests'])
        self.assertEqual(b['summary']['paid_resource_cents']-a['summary']['paid_resource_cents'],1200)

    def test_paid_staff_is_retained_across_service_policies(self):
        for r in self.cases.values():self.assertEqual(r['summary']['paid_staff_cents'],12000)
        self.assertEqual(self.cases['human_only_exact']['summary']['accepted'],3)

    def test_outage_retains_paid_failed_work_and_counts_only_completions(self):
        r=self.cases['observed_robot_outage'];s=r['summary']
        self.assertEqual((s['attempts_started'],s['failed_attempts'],s['accepted']),(4,1,3))
        self.assertEqual(s['paid_resource_cents'],15630)
        self.assertEqual(s['all_attempt_cash_per_accepted_request'],{'numerator':15630,'denominator':3})
        self.assertTrue(r['failed_attempts'][0]['partial_work_preserved'])
        self.assertNotIn(r['failed_attempts'][0]['request_id'],[a['request_id'] for a in r['accepted_requests']])

    def test_unfunded_recovery_blocks_future_robot_work(self):
        mode=Mode('r',4,(('robot',0,4),),100);later=Mode('r',2,(('robot',0,2),),0)
        w=Workload((Request('first',0,4,False,(mode,)),Request('later',2,6,False,(later,))),horizon=6,
            urgent_courier_reserve=(0,0),opening_cash_cents=150,paid_staff_shift_cents=0,robot_support_cents=0,integration_allocation_cents=0,outage=Outage(1,2,100))
        r=run_coordination(w,Controller(planning_cents_per_slot=0,verification_cents_per_slot=0))
        self.assertEqual(r['summary']['accepted'],0);self.assertEqual(r['summary']['failed_attempts'],1)
        event=next(e for e in r['events'] if e['kind']=='observed_robot_outage')
        self.assertFalse(event['recovery_paid']);self.assertEqual(event['unavailable_until'],6)
        self.assertEqual(r['summary']['paid_resource_cents'],100)

    def test_required_capacity_failure_does_not_create_free_service(self):
        r=self.cases['unfunded_window'];s=r['summary']
        self.assertTrue(s['unfunded_required_capacity']);self.assertEqual(s['accepted'],0)
        self.assertIsNone(s['all_attempt_cash_per_accepted_request'])
        self.assertEqual(s['paid_resource_cents'],12000)
        self.assertFalse(any(e['kind']=='started' for e in r['events']))

    def test_common_guard_rejects_duplicates_unknown_and_bad_identity(self):
        r=self.cases['duplicate_and_malformed_guard']
        reasons={a['reason'] for a in r['admissions'] if a['status']=='rejected'}
        self.assertEqual(reasons,{'duplicate_request_in_proposal','request_not_observed_pending','invalid_action_identity'})
        self.assertEqual([a['request_id'] for a in r['accepted_requests']],['urgent-E'])

    def test_delayed_stale_packet_cannot_execute_through_new_outage(self):
        r=self.cases['delayed_stale_outage_guard']
        self.assertEqual(r['summary']['attempts_started'],0)
        self.assertTrue(any(a['tick']==1 and a['status']=='rejected' for a in r['admissions']))
        self.assertFalse(any(c['category']=='attempt_resources' and c['paid_cents'] for c in r['cost_lines']))

    def test_malformed_inflight_packets_reserve_nothing_and_fail_visibly(self):
        for malformed in (None,{},[None],[{'start':2,'request_id':[],'mode_id':{}}],[{'start':2,'request_id':'unknown','mode_id':'x'}]):
            r=run_coordination(reference_workload(),Controller(latency_ticks=2,fixed_proposals={'0':malformed}))
            self.assertEqual(r['summary']['attempts_started'],0)
            self.assertTrue(any(a['status']=='rejected' for a in r['admissions']))

    def test_atomic_batch_cash_failure_creates_no_partial_work_or_payment(self):
        jobs=(Request('a',0,2,False,(Mode('h',1,(('courier',0,1),),100),)),Request('b',0,2,False,(Mode('r',1,(('robot',0,1),),100),)))
        w=Workload(jobs,horizon=2,urgent_courier_reserve=(0,0),opening_cash_cents=150,paid_staff_shift_cents=0,robot_support_cents=0,integration_allocation_cents=0)
        c=Controller(planning_cents_per_slot=0,verification_cents_per_slot=0,fixed_proposals={'0':[{'start':0,'request_id':'a','mode_id':'h'},{'start':0,'request_id':'b','mode_id':'r'}]})
        r=run_coordination(w,c)
        self.assertEqual(r['summary']['attempts_started'],0);self.assertEqual(r['summary']['paid_resource_cents'],0)

    def test_complete_replay_ignores_tampered_outcomes_and_hash(self):
        for r in self.cases.values():
            saved=copy.deepcopy(r);saved['summary']['accepted']=999;saved['case_hash']='tampered'
            self.assertEqual(replay_coordination(saved),r)

    def test_cash_resource_identity_and_deadline_conservation(self):
        for r in self.cases.values():
            self.assertEqual(sum(a['cash_cents'] for a in r['closing_treasury']['actors']),r['opening_cash_cents'])
            supplier=next(a for a in r['closing_treasury']['actors'] if a['actor_id']=='resource_supplier')
            self.assertEqual(supplier['cash_cents'],sum(c['paid_cents'] for c in r['cost_lines']))
            self.assertEqual(len(r['accepted_requests']),len({a['request_id'] for a in r['accepted_requests']}))
            jobs={j['request_id']:j for j in r['workload']['requests']};failed={f['attempt_id']:f['failed_at'] for f in r['failed_attempts']};used=set()
            for event in r['events']:
                if event['kind']!='started':continue
                mode=next(m for m in jobs[event['request_id']]['modes'] if m['mode_id']==event['mode_id'])
                for resource,offset,length in mode['claims']:
                    for tick in range(event['start']+offset,min(event['start']+offset+length,failed.get(event['attempt_id'],r['workload']['horizon']))):
                        self.assertNotIn((resource,tick),used);used.add((resource,tick))
            for a in r['accepted_requests']:self.assertLessEqual(a['completion_tick'],jobs[a['request_id']]['deadline'])
            self.assertFalse(r['running_at_horizon'])
            self.assertTrue(all(c['ledger_period']==i for i,c in enumerate(r['cost_lines'])))

    def test_invalid_inputs_do_not_coerce_numbers_or_unknown_fields(self):
        for fn in (lambda:Controller(latency_ticks=True),lambda:Controller(latency_ticks=4),lambda:replace(reference_workload(),opening_cash_cents=-1),
                   lambda:Mode('bad',2,(('courier',0,2),('courier',1,1)),0),lambda:replace(reference_workload(),horizon=5),lambda:replay_coordination({})):
            with self.assertRaises((ValueError,TypeError)):fn()


if __name__=='__main__':unittest.main()
