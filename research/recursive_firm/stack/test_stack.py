import unittest
from dataclasses import replace

from economy import (Economy, State, Tape, hour_price, operator_actions, run, sample,
                     solve, training, training_actions, value, with_rights)
from experiments import Contract, governance, ledger, license_market, procure_licenses
from nested_learning import Cell


class StackTests(unittest.TestCase):
    def test_unused_license_prices_the_selected_one_and_claims_change_source(self):
        by_hours = license_market(Economy())["by_hours"]
        self.assertEqual(by_hours["0"]["full_claim_both_offers"]["licenses"], [])
        reference = by_hours["1"]
        monopoly = reference["full_claim_arm_offer_only"]
        contest = reference["full_claim_both_offers"]
        split = reference["half_claim_both_offers"]
        self.assertEqual((monopoly["licenses"], contest["licenses"]), (["arm"], ["arm"]))
        self.assertEqual((monopoly["payments"]["arm"], contest["payments"]["arm"]), (11.47, 8.45))
        self.assertEqual(contest["joint_gain_at_truthful_bids"], monopoly["joint_gain_at_truthful_bids"])
        self.assertEqual((split["licenses"], split["joint_gain_at_truthful_bids"]), (["mobile"], 3.02))
        for result in (monopoly, contest, split):
            allocated = (result["sponsor_net"] + result["uncaptured_operating_gain"]
                         + sum(result["seller_gains_at_truthful_bids"].values()))
            self.assertAlmostEqual(allocated, result["joint_gain_at_truthful_bids"])

    def test_pivot_payment_supports_truthful_private_reservations(self):
        gains = {(): 0, ("arm",): 11.47, ("mobile",): 5.02, ("arm", "mobile"): 11.47}
        for site, other in (("arm", "mobile"), ("mobile", "arm")):
            for cost in (0, 2, 5, 6, 9, 13):
                for other_bid in (0, 2, 6, 13):
                    def utility(report):
                        result = procure_licenses(gains, {site: report, other: other_bid}, 1)
                        return result["payments"][site] - cost if site in result["licenses"] else 0
                    truthful = utility(cost)
                    for report in (0, 2, 5, 6, 9, 13):
                        self.assertGreaterEqual(truthful + 1e-8, utility(report))

    def test_executable_contract_replays_optimal_policy(self):
        for rights in ("sealed", "settlement", "local", "portable"):
            for timing in (0, .4, 1):
                e = replace(with_rights(Economy(), rights), amendment=timing)
                for h in (0,1,2):
                    plan = solve(e,h)
                    planned = plan.dispatch(0,State(),h,e.compute).value
                    self.assertAlmostEqual(ledger(plan,e,h)[0]["net"], planned)
                    self.assertEqual(ledger(Contract(plan),e,h)[0],ledger(plan,e,h)[0])

    def test_permission_to_report_is_distinct_from_training(self):
        for rights in ("sealed","settlement","local","portable"):
            e = replace(Economy(), arm_rights=rights)
            s = sample(e,State(),"arm",True)
            self.assertEqual(s.signal, -1 if rights=="sealed" else 1)
            self.assertEqual("arm_demo" in training_actions(e,s,1), rights in ("local","portable"))
            if rights in ("local","portable"):
                p,passed,failed = training(e,s,"arm_demo")
                self.assertEqual(p>0,rights=="portable")
                self.assertTrue(failed.arm_ok)
                self.assertFalse(failed.retrofit_candidate)
                self.assertTrue(passed.arm_spent)
                self.assertNotIn("arm",operator_actions(e,failed,1,"economic"))
        self.assertEqual(training_actions(Economy(),State(saw_arm=True),0),("hold",))

    def test_source_external_rights_and_compute_bind(self):
        e=Economy()
        for rights,price in (("sealed",5),("settlement",6.95),("local",12.95),("portable",16.47)):
            self.assertAlmostEqual(hour_price(with_rights(e,rights)),price)
        self.assertAlmostEqual(hour_price(replace(e,compute=0)),6.95)
        self.assertAlmostEqual(hour_price(replace(e,arm_rights="sealed")),10.02)

    def test_real_option_can_raise_surplus_and_lower_hour_price(self):
        e=Economy()
        bare=replace(e,hardware=("installed",))
        retrofit=replace(e,hardware=("installed","retrofit"))
        self.assertAlmostEqual(hour_price(bare),16.62)
        self.assertAlmostEqual(hour_price(retrofit),20.76)
        self.assertGreater(value(e,1),value(retrofit,1))
        self.assertAlmostEqual(hour_price(e)-hour_price(retrofit),-4.29)
        self.assertAlmostEqual((value(e,1)-value(retrofit,1))-(value(e,0)-value(retrofit,0)),-4.29)

    def test_mpl_and_net_value_measure_distinct_outcomes(self):
        e=Economy()
        initial=ledger(solve(e,0),e,0)[0]
        extra=ledger(solve(e,1),e,1)[0]
        self.assertEqual(extra["depot"],initial["depot"])
        self.assertEqual(extra["plant"]-initial["plant"],1)
        self.assertAlmostEqual(extra["net"]-initial["net"],16.47)

    def test_failed_cross_validation_reroutes_the_next_operator(self):
        e=replace(Economy(),desk_orders=0,plant_orders=1,depot_orders=2,hardware=("installed","retrofit"))
        policy=solve(e,2)
        passed=run(policy,e,2,Tape(True,True,True,False,True))
        failed=run(policy,e,2,Tape(True,True,False,False,True))
        self.assertEqual((passed["samples"],failed["samples"]),(("arm","urgent"),("arm","mobile")))
        self.assertEqual((passed["updates"],failed["updates"]),(("arm_demo","ledger"),("arm_demo","mobile_demo")))
        self.assertEqual((passed["hardware"],failed["hardware"]),("retrofit","installed"))

    def test_private_consents_complete_contract_and_successor(self):
        out=governance(Economy())
        self.assertAlmostEqual(out["one_hour"]["gross_timeliness_gain"],2.394)
        good,bad=out["setup_cost_one"],out["setup_cost_three"]
        self.assertEqual(good["offers"],[0,.25,.5])
        self.assertTrue(good["adopt"])
        self.assertFalse(bad["adopt"])
        self.assertAlmostEqual(good["net_provider"]+good["net_field"],1.394)
        for h,row in out["public_demand_experiment_by_hours"].items():
            self.assertAlmostEqual(row["bilateral_book_on_observed_orders"],row["joint_amendment"])
            turnover=out["turnover_by_hours"][h]
            self.assertAlmostEqual(turnover["gross_value_of_survival"],.3*row["value_of_conditioning"])
        self.assertAlmostEqual(out["turnover_by_hours"]["1"]["gross_value_of_survival"],.7695)


class NestedLearningTests(unittest.TestCase):
    def test_sealed_and_local_traces_cannot_write_shared_weights(self):
        cell=Cell(4,(4,10,50),True,("sealed","local"))
        self.assertNotIn("arm_local",cell.eligible())
        self.assertNotIn("mobile_pool",cell.eligible())
        cell.step("mobile_local")
        self.assertTrue(cell.buffers[2])
        self.assertFalse(cell.buffers[1])
        self.assertEqual(cell.shared,[0.0]*4)
        self.assertNotIn("replay_pool",cell.eligible())

    def test_replay_uses_an_existing_packet_without_an_operator_demo(self):
        cell=Cell(9,(4,10,50),True)
        self.assertNotIn("replay_pool",cell.eligible())
        cell.step("arm_pool")
        rows=tuple(cell.buffers[1])
        weights=tuple(cell.shared)
        _,sampled=cell.step("replay_pool")
        self.assertIsNone(sampled)
        self.assertEqual(tuple(cell.buffers[1]),rows)
        self.assertNotEqual(tuple(cell.shared),weights)

    def test_authorized_gradient_and_telescoping_score(self):
        cell=Cell(14,(4,10,50),True)
        arm,mobile=cell.rates()[1:]
        outcome=cell.sign[1][1]
        cell.gradient(1,1,outcome,True)
        self.assertGreater(cell.rates()[1],arm)
        self.assertGreater(cell.rates()[2],mobile)
        start=cell.paid_output()
        cash=reward=0.0
        for a in ("arm_pool","ledger","mobile_pool","replay_pool","urgent","ledger"):
            before=cell.paid_output()
            direct,_=cell.step(a)
            cash+=direct
            reward+=direct+cell.paid_output()-before
        self.assertAlmostEqual(start+reward,cell.paid_output()+cash)


if __name__=="__main__":
    unittest.main()
