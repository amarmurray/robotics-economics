import unittest
from fractions import Fraction as Q
from itertools import product
from model.qualification_finance import funded, funding_cuts, project_choices
from model.theory_deployment import service


class QualificationFinanceTests(unittest.TestCase):
    def test_cuts_against_independent_flow_enumeration(self):
        # Includes an indirect route and a cycle. Integer small-instance oracle.
        edges = {(0, 1): 1, (1, 2): 1, (2, 0): 1}
        for cash in product(range(3), repeat=3):
            for obligations in product(range(3), repeat=3):
                possible = False
                for flow in product(range(2), repeat=3):
                    remaining = list(cash)
                    for (a, b), amount in zip(edges, flow):
                        remaining[a] -= amount
                        remaining[b] += amount
                    if all(remaining[i] >= obligations[i] for i in range(3)):
                        possible = True
                        break
                self.assertEqual(funded(cash, obligations, edges), possible)

    def test_aggregate_cash_not_sufficient(self):
        self.assertGreater(sum((5, 1)), sum((2, 2)))
        self.assertFalse(funded((5, 1), (2, 2), {}))
        self.assertTrue(funded((2, 2), (2, 2), {}))
        cuts = funding_cuts((5, 1), (2, 2), {(0, 1): Q(999, 1000)})
        failed = [c for c in cuts if c['slack'] < 0]
        self.assertEqual(len(failed), 1)
        self.assertEqual((failed[0]['payers'], failed[0]['slack']), ((1,), Q(-1, 1000)))

    def test_exact_switch_and_partial_investment(self):
        for tau, winner, value in [(0, 'L', 10), (Q(999,1000), 'L', 10), (1, 'H', 12)]:
            options = project_choices('H', (5,1), tau)+project_choices('L', (2,2), tau)
            best = max((x for x in options if x['feasible']), key=lambda x:x['value'])
            self.assertEqual((best['deployment'], best['value']), (winner, value))
            for c in options:
                if c['qualify'] != c['commission']:
                    self.assertEqual(c['profits'], (0,0))

    def test_payer_conservation_and_individual_gains(self):
        for name, cash in [('H',(5,1)), ('L',(2,2))]:
            for c in project_choices(name, cash, 1):
                if c['feasible']:
                    self.assertGreaterEqual(min(c['after']),0)
                    self.assertEqual(sum(c['after']),sum(cash)-sum(c['obligations']))
                    self.assertEqual(c['value'],sum(cash)-sum(c['obligations'])+sum(c['profits']))
                    if c['qualify'] and c['commission']:
                        self.assertTrue(all(c['terminal'][i]>=cash[i] for i in range(2)))
        s = service(10,2,2,capture=Q(5,6))
        self.assertEqual((s['revenue'],s['resource'],s['fee'],s['customer'],s['provider']),
                         (16,4,14,2,10))

    def test_direction_and_domain(self):
        self.assertFalse(funded((5,1),(2,2),{(1,0):100}))
        self.assertTrue(funded((5,1),(2,2),{(0,1):1}))
        with self.assertRaises(ValueError):
            funded((1,1),(1,1),{(0,1):-1})

    def test_demand_finance_phase_partition(self):
        for a in (Q(i,10) for i in range(0,121)):
            for tau in [Q(0), Q(999,1000), Q(1), Q(2)]:
                options = project_choices('H',(5,1),tau,a)+project_choices('L',(2,2),tau,a)
                candidates = [x for x in options if x['feasible']]
                value = max(x['value'] for x in candidates)
                winners = {(x['deployment'],x['qualify'] and x['commission'])
                           for x in candidates if x['value']==value}
                if tau < 1:
                    predicted = {('H',False)} if a < Q(38,5) else {('L',True)}
                    if a==Q(38,5): predicted = {('H',False),('L',True)}
                else:
                    predicted = {('H',False)} if a < Q(32,5) else {('H',True)}
                    if a==Q(32,5): predicted = {('H',False),('H',True)}
                self.assertEqual(winners,predicted,(a,tau))


if __name__ == '__main__':
    unittest.main()
