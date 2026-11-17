import unittest
from dataclasses import replace
from fractions import Fraction as F
from cross_layer import Source, SOURCES, Contracts, Market, evaluate, portfolio, run

class TestCrossLayer(unittest.TestCase):
    def test_source_cash_from_demand(self):
        self.assertEqual([s.cash() for s in SOURCES], [F(5),F(4),F(3),F(0)])

    def test_target_cash_and_customer_splits(self):
        o = evaluate(SOURCES[2])
        self.assertEqual(o.target_provider_profit, F(16))
        self.assertEqual(o.target_customer_profit, F(6))

    def test_baseline_prefers_hybrid(self):
        winner, o = portfolio()
        self.assertEqual(winner, "hybrid")
        self.assertEqual(o["hybrid"].provider_total, F(10))
        self.assertEqual(o["factory"].provider_total, F(47,5))
        self.assertEqual(o["field"].provider_total, F(42,5))
        self.assertEqual(o["hybrid"].action, "enter_specialist")

    def test_ablate_each_channel(self):
        cases = [Contracts(pass_through=F(0)), Contracts(field_reuse_right=F(0)), Contracts(access_effect=F(0))]
        for c in cases:
            with self.subTest(contracts=c):
                self.assertEqual(portfolio(c)[0], "factory")

    def test_two_distinct_boundaries(self):
        # Given delta=1, hybrid financing threshold kappa>=2/3,
        # but strict preference over factory requires kappa>4/5.
        for k,affordable,chosen in [(F(2,3),True,False),(F(7,10),True,False),(F(4,5),True,False),(F(81,100),True,True)]:
            c=Contracts(pass_through=k)
            o=evaluate(SOURCES[2],c)
            self.assertEqual(o.target_investment <= o.investment_budget,affordable)
            self.assertEqual(portfolio(c)[0]=="hybrid",chosen)

    def test_below_finance_boundary(self):
        o=evaluate(SOURCES[2],Contracts(pass_through=F(1,2)))
        self.assertGreater(o.target_investment,o.investment_budget)
        self.assertEqual(o.action,"expand_incumbent")

    def test_supplier_pass_through_can_induce_order(self):
        o_low=portfolio(Contracts(pass_through=F(4,5)))[1]["hybrid"]
        o_high=portfolio(Contracts(pass_through=F(81,100)))[1]["hybrid"]
        self.assertEqual(o_high.supplier_margin_on_target,F(157,100))
        self.assertEqual(portfolio(Contracts(pass_through=F(4,5)))[0],"factory")
        self.assertEqual(portfolio(Contracts(pass_through=F(81,100)))[0],"hybrid")

    def test_supplier_cost_and_invoice_distinct(self):
        for k in (F(0),F(1,2),F(1)):
            for source in SOURCES:
                o=evaluate(source,Contracts(pass_through=k))
                self.assertEqual(o.target_price-o.target_resource_cost, F(1)+F(3)*(1-k)*source.manufacturer_experience)

    def test_invoice_pass_through_conserves_total_surplus_conditional_on_order(self):
        for k in [F(i,20) for i in range(17,21)]:
            o=evaluate(SOURCES[2],Contracts(pass_through=k))
            if o.action=="enter_specialist":
                provider_plus_supplier=o.provider_total+o.supplier_margin_on_target
                independent=o.current_cash+o.target_provider_profit-o.target_resource_cost-o.target_qualification
                self.assertEqual(provider_plus_supplier,independent)

    def test_policy_value_monotonic_in_rights_and_cash(self):
        for i in range(11):
            for j in range(11):
                k,d=F(i,10),F(j,10)
                o=evaluate(SOURCES[2],Contracts(pass_through=k,field_reuse_right=d))
                self.assertLessEqual(o.provider_gain,evaluate(SOURCES[2],Contracts(pass_through=min(F(1),k+F(1,10)),field_reuse_right=d)).provider_gain)
                self.assertLessEqual(o.provider_gain,evaluate(SOURCES[2],Contracts(pass_through=k,field_reuse_right=min(F(1),d+F(1,10)))).provider_gain)
        for cash in range(0,21):
            a=evaluate(SOURCES[2],initial_cash=F(cash))
            b=evaluate(SOURCES[2],initial_cash=F(cash+1))
            self.assertLessEqual(a.provider_gain,b.provider_gain)

    def test_no_double_counting_and_repayment(self):
        for i in range(11):
            for source in SOURCES:
                o=evaluate(source,Contracts(pass_through=F(i,10)))
                spend=F(0) if o.action=="retain" else (F(6) if o.action=="expand_incumbent" else o.target_investment)
                cont=F(0) if o.action=="retain" else (F(52,5) if o.action=="expand_incumbent" else o.target_provider_profit)
                self.assertEqual(o.terminal_cash,o.investment_budget-spend+cont)
                self.assertGreaterEqual(o.investment_budget-spend,0)

    def test_outside_option_and_demand_saturation(self):
        m=Market(F(12),outside=F(100))
        self.assertEqual(m.service(F(2))[1],F(0))
        self.assertEqual(Market(F(12)).service(F(30))[0],F(9,2))

    def test_parameter_validation(self):
        with self.assertRaises(ValueError): Contracts(pass_through=F(11,10))
        with self.assertRaises(ValueError): Contracts(field_reuse_right=F(-1))
        with self.assertRaises(ValueError): evaluate(SOURCES[0],initial_cash=F(-1))

    def test_low_demand_changes_output_and_no_false_sale(self):
        c=Contracts(target_base_intercept=F(1))
        o=evaluate(SOURCES[2],c)
        self.assertEqual(o.action,"expand_incumbent")
        self.assertEqual(o.potential_target_quantity,F(0))
        c=Contracts(target_base_intercept=F(2))
        self.assertEqual(evaluate(SOURCES[2],c).potential_target_quantity,F(3,2))

    def test_deterministic_result(self):
        self.assertEqual(run(),run())

if __name__ == "__main__": unittest.main()

