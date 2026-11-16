"""Economic checks: exact choices, repayment, saturation and source transcription."""
import unittest
from fractions import Fraction as Q
from model.theory_deployment import Application, best, choices, service, source_output


class TheoryDeploymentTests(unittest.TestCase):
    def setUp(self):
        self.h = Application('H', Q(8), Q(8), Q(4))
        self.low = Application('L', Q(2), Q(12), Q(2))

    def test_reversal_and_exact_funding_boundary(self):
        for limit in [Q(0), Q(999, 1000)]:
            self.assertEqual(best([self.h, self.low], credit=limit)['application'], 'H')
        winner = best([self.h, self.low], credit=Q(1))
        self.assertEqual((winner['application'], winner['expand'], winner['value']),
                         ('L', True, Q(59, 5)))
        self.assertEqual(winner['loan'], Q(1))
        self.assertEqual(winner['after_investment'], 0)

    def test_cash_and_customer_provider_reconciliation(self):
        for app in [self.h, self.low]:
            for c in choices(app, credit=Q(1)):
                s = c['service']
                self.assertEqual(s['customer']+s['provider'], s['revenue']-s['resource'])
                self.assertEqual(c['terminal'], app.cash-c['investment']+s['provider'])
        s = choices(self.low, credit=Q(1))[1]['service']
        self.assertEqual((s['revenue'], s['fee'], s['customer']),
                         (Q(20), Q(84, 5), Q(16, 5)))

    def test_binding_threshold_against_exact_subtraction(self):
        for d in range(4, 13):
            for rho in [Q(1, 4), Q(4, 5), Q(1)]:
                delta = service(d, 0, 2, capture=rho)['provider']-service(d, 0, 1, capture=rho)['provider']
                self.assertEqual(delta, rho*(d-3))
                self.assertEqual(delta >= 3, Q(d) >= 3+3/rho)

    def test_demand_saturation_and_outside_option(self):
        self.assertEqual(service(4, 2, 1)['gross'], service(4, 2, 8)['gross'])
        s = service(4, 2, 8, outside=Q(2))
        self.assertEqual((s['q'], s['provider'], s['customer']), (0, 0, 2))
        s = service(8, 4, 1, outside=Q(1))
        self.assertEqual(s['provider']+s['customer'], s['gross'])
        self.assertEqual(service(1, 2, 1)['q'], 0)

    def test_quantity_global_optimum_on_rational_grid(self):
        for a in [Q(1), Q(4), Q(8), Q(12)]:
            for cap in [Q(0), Q(1), Q(2), Q(5)]:
                optimum = service(a, 2, cap)['gross']
                for step in range(int(cap*10)+1):
                    q = Q(step, 10)
                    self.assertGreaterEqual(optimum, (a-2)*q-q*q)

    def test_ablation_and_failed_expansion(self):
        for low in [Application('L', Q(2), Q(12), Q(4)),
                    Application('L', Q(2), Q(8), Q(2))]:
            self.assertEqual(best([self.h, low], credit=1)['application'], 'H')
        failed = choices(self.low, credit=1, increment=0)
        self.assertEqual(failed[0]['value']-failed[1]['value'], 3)

    def test_source_worked_example(self):
        self.assertAlmostEqual(source_output(6), 29.757, delta=.01)
        self.assertAlmostEqual(source_output(12), 57.2, delta=.1)
        self.assertGreater(2*source_output(6), source_output(12))
        self.assertGreater(source_output(6)/6, source_output(5)/5)
        self.assertGreater(source_output(6)/6, source_output(7)/7)


if __name__ == '__main__':
    unittest.main()
