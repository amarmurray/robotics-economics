"""Scoped tests for the takeover benchmark, not the historical repository suite."""
import json
import unittest
from dataclasses import replace
from fractions import Fraction as F
from expansion import (A, B_LOW, B_HIGH, Market, Technology, optimize,
                       choose_source, incumbent_gain, results)


class ExpansionTests(unittest.TestCase):
    def test_customer_quantity_saturates(self):
        m = Market(F(10), F(2), F(2))
        self.assertEqual(m.service(F(20))[0], F(4))
        self.assertEqual(m.service(F(1))[0], F(1))

    def test_customer_participation(self):
        m = replace(A, outside_profit=F(1000))
        self.assertEqual(m.service(F(3)), (F(0), F(0), F(1000)))

    def test_source_cash_is_derived_not_a_bonus(self):
        r = choose_source()
        self.assertEqual(r['paths']['cash_rich']['source_cash'], F(8))
        self.assertEqual(r['paths']['transfer_rich']['source_cash'], F(6))
        for row in r['paths'].values():
            self.assertEqual(row['source_quantity'], F(1))

    def test_constructive_sequence(self):
        r = choose_source()
        self.assertEqual(r['winner'], 'transfer_rich')
        self.assertEqual(r['paths']['cash_rich']['added_value'], F(76,5))
        self.assertEqual(r['paths']['transfer_rich']['added_value'], F(22))
        self.assertEqual(r['paths']['transfer_rich']['decision'].new_b, 2)

    def test_no_transfer_reverses_choice(self):
        self.assertEqual(choose_source(tech=replace(Technology(), transfer=F(0)))['winner'],
                         'cash_rich')

    def test_weak_target_demand_reverses_choice(self):
        self.assertEqual(choose_source(market_b=B_LOW)['winner'], 'cash_rich')

    def test_fixed_embodiment_reverses_choice(self):
        self.assertEqual(choose_source(allow_new=False)['winner'], 'cash_rich')

    def test_result_not_only_a_financing_gate(self):
        self.assertEqual(choose_source(initial_cash=F(100))['winner'], 'transfer_rich')

    def test_more_cash_need_not_mean_more_breadth(self):
        expected = [(0,1,F(3,5)), (1,0,F(22,5)), (1,1,F(5))]
        for b, (na,nb,g) in zip((5,6,11),expected):
            d = optimize(F(b),F(1),A,B_LOW)
            self.assertEqual((d.new_a,d.new_b,d.gain),(na,nb,g))

    def test_budget_value_monotonicity(self):
        for allow_tooling in (False, True):
            for e in (F(0), F(1,2), F(1)):
                vals=[optimize(F(b),e,A,B_HIGH,allow_tooling=allow_tooling).gain
                      for b in range(21)]
                self.assertTrue(all(x<=y for x,y in zip(vals,vals[1:])))

    def test_free_useful_learning_value_monotonicity(self):
        for b in range(17):
            vals=[optimize(F(b),F(e,4),A,B_HIGH).gain for e in range(5)]
            self.assertTrue(all(x<=y for x,y in zip(vals,vals[1:])))

    def test_tooling_option_cannot_reduce_optimal_value(self):
        for b in range(17):
            for e in (F(0),F(1)):
                old=optimize(F(b),e,A,B_HIGH)
                new=optimize(F(b),e,A,B_HIGH,allow_tooling=True)
                self.assertGreaterEqual(new.gain,old.gain)
        d=choose_source(allow_tooling=True)['paths']['transfer_rich']['decision']
        self.assertEqual((d.new_a,d.new_b,d.tooling,d.investment),(0,3,True,F(10)))

    def test_entry_criterion_with_displaced_incumbent_value(self):
        tech=Technology()
        for budget in map(F,range(21)):
            incumbent=incumbent_gain(budget)
            best=incumbent
            for y in range(1,int(budget/tech.unit_b)+1):
                cost=tech.qualification(F(1))+tech.unit_b*y
                if cost<=budget:
                    j=B_LOW.service(F(y))[1]-cost
                    best=max(best,j+incumbent_gain(budget-cost))
            self.assertEqual(best,optimize(budget,F(1),A,B_LOW).gain)

    def test_cash_and_terminal_asset_accounting(self):
        for salvage in (F(0),F(1,4)):
            tech=replace(Technology(),salvage_share=salvage)
            for allow_tooling in (False,True):
                r=choose_source(tech=tech,allow_tooling=allow_tooling)
                baseline=A.service(F(tech.installed_a))[1]
                for row in r['paths'].values():
                    d=row['decision']
                    self.assertLessEqual(d.investment,row['budget'])
                    terminal=row['budget']-d.investment+d.operating_profit+d.salvage
                    self.assertEqual(terminal,F(4)+baseline+row['added_value'])

    def test_salvage_does_not_fund_upfront_spending(self):
        d=optimize(F(0),F(1),A,B_HIGH,replace(Technology(),salvage_share=F(3,4)))
        self.assertEqual((d.new_a,d.new_b,d.investment),(0,0,F(0)))

    def test_demand_saturation_prevents_wasteful_expansion(self):
        low=Market(F(3),F(2),F(2),F(0))
        d=optimize(F(100),F(1),low,low)
        self.assertEqual((d.new_a,d.new_b),(0,0))

    def test_invalid_parameters(self):
        with self.assertRaises(ValueError):
            Market(F(1),F(0),F(0))
        with self.assertRaises(ValueError):
            Technology(unit_a=F(2))
        with self.assertRaises(ValueError):
            optimize(F(-1),F(0),A,B_LOW)

    def test_deterministic_regeneration(self):
        self.assertEqual(json.dumps(results(),sort_keys=True),json.dumps(results(),sort_keys=True))


if __name__ == '__main__':
    unittest.main()
