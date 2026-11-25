import unittest
from fractions import Fraction

from evidence import Case, digital_cases, heldout, pooled_and_conditioned, robot_cases, run


class Checks(unittest.TestCase):
    def test_published_totals(self):
        groups = robot_cases()
        self.assertEqual([len(groups["WidowX"]), len(groups["Google"])], [17,12])
        self.assertEqual(len(digital_cases()[0].score),12)
        for name, expected in (("WidowX",[18.5,20.0,50.6,70.6]),("Google",[33.3,26.7,78.3,85.] )):
            rows=groups[name]
            reported=[round(float(sum(r.score[m] for r in rows)/len(rows)),1) for m in rows[0].score]
            self.assertEqual(reported,expected)

    def test_two_option_identity_and_preexisting_specialization(self):
        cases = [Case(str(i),str(i<2),{"A":Fraction(x),"B":Fraction(y)})
                 for i,(x,y) in enumerate(((5,3),(6,2),(1,4)))]
        values=pooled_and_conditioned(cases,["A","B"])
        delta=[c.score["A"]-c.score["B"] for c in cases]
        minority=min(sum(max(d,0) for d in delta),sum(max(-d,0) for d in delta))/len(cases)
        self.assertEqual(values["task_hindsight"]-values["fixed"],minority)
        self.assertEqual(values["remaining_within_family"],0)
        self.assertGreater(values["static_family_gain"],0)

    def test_no_test_outcome_used_to_break_training_tie(self):
        cases=[Case("t1","a",{"X":Fraction(2),"Y":Fraction(2)}),
               Case("t2","a",{"X":Fraction(6),"Y":Fraction(0)})]
        self.assertEqual(heldout(cases,["X","Y"])["family"],Fraction(5,2))

    def test_negative_control_with_complete_menu(self):
        result=run()["digital"]
        self.assertEqual(result["all_reported"]["fixed_models"],["gpt-4o"])
        self.assertEqual(result["all_reported"]["static_family_gain"],0)
        self.assertEqual(result["previous_pair"]["static_family_gain"],Fraction(23,20))

    def test_hindsight_is_not_used_for_heldout_predictions(self):
        reports = run()["robots"]
        for name, raw_gain in (("WidowX", Fraction(-55,34)), ("Google", Fraction(-10,3))):
            sample = reports[name]["in_sample"]
            self.assertGreater(sample["task_hindsight"],sample["fixed"])
            self.assertEqual(reports[name]["leave_one_task_out"]["family_gain"],raw_gain)


if __name__ == "__main__":
    unittest.main()
