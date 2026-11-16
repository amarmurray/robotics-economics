import unittest
from fractions import Fraction as Q
from itertools import product
from model.learning_funding_alignment import experience_threshold, build
from model.qualification_finance import funded


class LearningFundingAlignmentTests(unittest.TestCase):
    def test_directed_thresholds(self):
        self.assertIsNone(experience_threshold((5,1),(2,2),{},(1,0),2))
        self.assertEqual(experience_threshold((5,1),(2,2),{},(0,1),2),1)
        self.assertEqual(experience_threshold((5,1),(2,2),{},(Q(1,2),Q(1,2)),2),2)
        self.assertEqual(experience_threshold((5,1),(2,2),{(0,1):1},(0,0),2),0)

    def test_threshold_against_feasibility_and_monotonicity(self):
        for cash in product(range(4),repeat=2):
            for loading in [(Q(1),Q(0)),(Q(0),Q(1)),(Q(1,2),Q(1,2))]:
                for tau in [Q(0),Q(1,2),Q(1)]:
                    edge={(0,1):tau}
                    threshold=experience_threshold(cash,(2,2),edge,loading,2)
                    for e in (Q(i,4) for i in range(9)):
                        costs=tuple(Q(2)-l*e for l in loading)
                        self.assertEqual(funded(cash,costs,edge),threshold is not None and e>=threshold)

    def test_equal_total_improvement_not_equal_value(self):
        rows=build()['worlds']
        no_transfer={r['source']:r for r in rows if r['tau']=='0'}
        self.assertEqual({r['value'] for r in no_transfer.values()},{'6','13'})
        self.assertEqual(no_transfer['operator_focused']['value'],'13')
        permitted=[r for r in rows if r['tau']=='1']
        self.assertEqual({r['value'] for r in permitted},{'13'})
        for r in rows:self.assertEqual(sum(map(Q,r['costs'])),3)

    def test_domain_limits_not_global_impossibility(self):
        self.assertIsNone(experience_threshold((5,1),(2,2),{},(Q(1,2),Q(1,2)),1))
        with self.assertRaises(ValueError):
            experience_threshold((5,1),(2,2),{},(1,0),3)
        self.assertEqual(experience_threshold((2,2),(2,2),{},(0,0),0),0)


if __name__=='__main__':unittest.main()
