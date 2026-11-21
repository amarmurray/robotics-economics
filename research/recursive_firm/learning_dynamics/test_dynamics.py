import unittest
from dataclasses import replace

import numpy as np

from fleet import (DAYS, FAMILIES, WARMUP, Design, Learners, World,
                   economic_reviews, run, select_reviews)
from scaling import (SCORES, best_review, cells, clock_error, finite_review, frontier,
                     published_scores, review_value, scale_fleet)


class LearningClockTests(unittest.TestCase):
    def test_qualification_can_open_a_new_evidence_source(self):
        trapped=frontier(16,trials=False)
        invest=frontier(16)
        self.assertTrue(all(point["qualified_share"]==0 for point in trapped["trajectory"]))
        self.assertEqual(frontier(4)["expected_paid_trials"],0)
        self.assertEqual(frontier(16,trial_yield=0)["value"],trapped["value"])
        self.assertGreater(invest["value"],trapped["value"])
        first=next(p for p in invest["trajectory"] if p["qualified_share"])
        self.assertLess(first["mix_completion"],.95)
        self.assertTrue(any(p["qualified_share"] for p in frontier(16,donor_support=4,trials=False)["trajectory"]))

    def test_flow_integrates_the_assumed_useful_label_intensity(self):
        for t in (0, 3, 57):
            alpha, gamma = .7, 1.4
            def age(x):
                return (.5/clock_error(x,alpha,gamma))**(1/alpha)-1
            slope = (age(t+.00001)-age(t))/.00001
            self.assertAlmostEqual(slope, clock_error(t,alpha,gamma)**gamma, places=5)
        self.assertAlmostEqual(clock_error(24, .5, 0), .1)

    def test_public_score_denominators_and_constant_effort_cells(self):
        for maximum, raw in SCORES.values():
            rows = cells(maximum,raw)
            self.assertEqual(len(rows),21)
            self.assertTrue(all(0 < score < 1 and volume<=breadth for breadth,volume,score in rows))
        out = published_scores()
        self.assertAlmostEqual(out["pour_water"]["equal_nominal_volume"]["8"]["difference_pp"],21.667)
        self.assertAlmostEqual(out["arrange_mouse"]["equal_nominal_volume"]["8"]["difference_pp"],30.833)
        self.assertEqual(len(out["pour_water"]["holdout"]["32"]["volume_power"]["predicted_scores"]),6)

    def test_clock_replica_caps_and_duplicate_histories(self):
        s = scale_fleet(worlds=16,shifts=12)["means"]
        self.assertEqual(s["common_record_1_1"],s["common_record_64_64"])
        self.assertLessEqual(s["independent_64_1"]["distinct_updates"],12)
        self.assertGreaterEqual(s["independent_64_4"]["distinct_updates"],s["independent_64_1"]["distinct_updates"])

    def test_review_matches_unrestricted_finite_dynamic_program(self):
        for p,delay,fee in ((.01,3,.6),(.05,0,.6),(.10,3,.6),(.2,3,.6),(.3,8,.6)):
            h, optimum = best_review(p,delay,fee)
            enumeration = max([.5]+[review_value(i,p,delay,fee) for i in range(1,250)])
            self.assertAlmostEqual(optimum,enumeration)
            self.assertLess(abs(finite_review(p,delay,fee,700)-optimum),.002)
            self.assertEqual(h is None, fee >= (1-2*p)**delay/(4*p))


class MixedFleetTests(unittest.TestCase):
    def test_warmup_is_identical_and_no_future_orders_enter_past_training(self):
        base = Design()
        world = World(42)
        ref = run(world,base)
        mod = run(world,replace(base,patch=.9,collection="coverage",shift="new_demand"))
        self.assertEqual(ref["path"][str(WARMUP)],mod["path"][str(WARMUP)])
        world.intent_noise[40:] = ~world.intent_noise[40:]
        self.assertEqual(run(world,base)["path"]["36"],ref["path"]["36"])

    def test_local_records_cannot_update_shared_policy(self):
        learners = Learners()
        fam = np.array([1,2,2])
        y = np.array([1,0,1])
        learners.admit(fam,y,y,False)
        self.assertEqual(learners.pool.sum(),0)
        self.assertEqual(learners.route.sum(),2*FAMILIES+len(y))
        world = World(155)
        no_rights = Design(portable=False)
        original = run(world,no_rights)
        patched = run(world,replace(no_rights,patch=.9))
        for k in ("arm_capability","mobile_capability","desk_capability","native_updates"):
            self.assertEqual(original[k],patched[k])

    def test_compute_and_yoked_annotation_budgets(self):
        world = World(455)
        base=Design(patch=.9,compute=1)
        a=run(world,base)
        b=run(world,replace(base,collection="coverage"),a["quotas"])
        self.assertEqual(a["tickets"],b["tickets"])
        self.assertEqual(a["updates"],b["updates"])
        self.assertLessEqual(a["updates"],DAYS-WARMUP)
        self.assertEqual(a["native_updates"],3*(DAYS-WARMUP)//4)

    def test_sampling_priority_and_positive_economic_bid(self):
        failed=np.array([False, True, False, True])
        priority=np.array([.1,.7,.2,.3])
        cases=np.array([0,1,2,3])
        seen=np.array([3,2,0,1])
        self.assertEqual(select_reviews("incidents",failed,priority,cases,seen,3).tolist(),[3,1])
        self.assertEqual(select_reviews("coverage",failed,priority,cases,seen,3)[0],2)
        world=World(7)
        learners=Learners()
        demand=np.ones((3,FAMILIES))/FAMILIES
        no_incident=np.zeros(18,dtype=bool)
        selected=economic_reviews(learners,world,Design(patch=.9),world.cases[0,-1],no_incident,
                                  np.ones(3,dtype=bool),demand,DAYS-1)
        self.assertEqual(len(selected),0)

    def test_transfer_gate_uses_pre_update_native_scores(self):
        l = Learners()
        w = World(0)
        fs = np.array([0,1,2])
        # Native labels here contradict the candidate for mobile only.
        for _ in range(4):
            local=np.full((3,FAMILIES),.5)
            pooled=np.full((3,FAMILIES),.9)
            l.native_update(fs,np.array([1,1,0]),local,pooled)
        use = l.probabilities(w,Design(sharing="validated"))[-1]
        self.assertEqual(use.tolist(),[True,True,False])


if __name__ == "__main__":
    unittest.main()
