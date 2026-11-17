"""Small-instance model checks; no empirical fitting or historical full-suite claim."""
import json
import unittest
from dataclasses import replace
from fractions import Fraction as F
from delayed_embodiment import (EPSILON, OLD_PROFILE, REDESIGNED_PROFILE, Setting,
                                projects, upper_cent, binding_switch, binding_valid,
                                market_at, provider_profit, value, select, experiment)
from qualification import qualify


class DelayedChoiceTests(unittest.TestCase):
    def test_common_qualification_standard(self):
        old=qualify(OLD_PROFILE,EPSILON,2)
        redesign=qualify(REDESIGNED_PROFILE,EPSILON,2)
        self.assertTrue(old.feasible and redesign.feasible)
        self.assertLessEqual(sum(old.residual),EPSILON+1e-12)
        self.assertLessEqual(sum(redesign.residual),EPSILON+1e-12)
        self.assertEqual(upper_cent(old.total_cost),F(1991,100))
        self.assertEqual(upper_cent(redesign.total_cost),F(956,100))

    def test_richer_design_has_changed_hardware_not_free_software(self):
        self.assertGreater(OLD_PROFILE[1].floor, REDESIGNED_PROFILE[1].floor)
        self.assertGreater(REDESIGNED_PROFILE[1].rate, OLD_PROFILE[1].rate)
        p=projects(Setting())
        self.assertEqual((p['software'].cost,p['redesign'].cost),(F(2291,100),F(2056,100)))
        self.assertEqual((p['software'].lag,p['redesign'].lag),(0,2))

    def test_three_economic_regimes(self):
        self.assertEqual(select(Setting())['winner'],'redesign')
        self.assertEqual(select(replace(Setting(),demand_decline=F(5)))['winner'],'software')
        self.assertEqual(select(replace(Setting(),demand_decline=F(6)))['winner'],'incumbent')

    def test_exact_switch_and_binding_conditions(self):
        s=Setting()
        threshold=binding_switch(s)
        self.assertEqual(threshold,F(623,144))
        b=replace(s,demand_decline=threshold)
        self.assertTrue(binding_valid(b))
        r=select(b)['values']
        self.assertEqual(r['software'],r['redesign'])
        tiny=F(1,100)
        self.assertGreater(select(replace(s,demand_decline=threshold-tiny))['values']['redesign'],
                           select(replace(s,demand_decline=threshold-tiny))['values']['software'])
        self.assertLess(select(replace(s,demand_decline=threshold+tiny))['values']['redesign'],
                        select(replace(s,demand_decline=threshold+tiny))['values']['software'])

    def test_decline_slope_in_binding_regime(self):
        a=select(replace(Setting(),demand_decline=F(1)))['values']
        b=select(replace(Setting(),demand_decline=F(2)))['values']
        self.assertEqual((b['redesign']-b['software'])-(a['redesign']-a['software']),-F(36,5))

    def test_long_build_and_uncertainty_not_fabricated(self):
        s=replace(Setting(),redesigned_lag=4)
        self.assertEqual(value(s,projects(s)['redesign']),-projects(s)['redesign'].cost)
        self.assertEqual(select(s)['winner'],'software')

    def test_fixed_cost_and_cash_ablations(self):
        self.assertNotEqual(select(replace(Setting(),fixed_design_cost=F(25)))['winner'],'redesign')
        s=replace(Setting(),initial_cash=F(22))
        self.assertIsNone(select(s)['values']['software'])
        self.assertIsNotNone(select(s)['values']['redesign'])

    def test_salvage_is_terminal_not_upfront(self):
        s=replace(Setting(),initial_cash=F(0),salvage_share=F(1,2))
        self.assertEqual(select(s)['winner'],'retain')
        self.assertTrue(all(v is None for v in select(s)['values'].values()))
        s=replace(Setting(),beta=F(1,2),salvage_share=F(1,4))
        p=projects(s)['software']
        non_salvage=value(replace(s,salvage_share=F(0)),p)
        self.assertEqual(value(s,p)-non_salvage,F(1,2)**3*F(1,4)*p.acquisition)

    def test_delay_monotone_for_project_with_nonnegative_profits(self):
        s=Setting()
        vals=[]
        for lag in range(5):
            x=replace(s,redesigned_lag=lag)
            vals.append(value(x,projects(x)['redesign']))
        self.assertTrue(all(a>=b for a,b in zip(vals,vals[1:])))

    def test_demand_decline_weakly_reduces_b_project_value(self):
        for n in ('software','redesign'):
            vals=[value(replace(Setting(),demand_decline=F(g)),
                       projects(Setting())[n]) for g in range(7)]
            self.assertTrue(all(x>=y for x,y in zip(vals,vals[1:])))

    def test_extra_budget_never_lowers_optimal_value(self):
        for cash in range(41):
            x=replace(Setting(),initial_cash=F(cash))
            y=replace(x,initial_cash=F(cash+1))
            xvalue=max([F(0)]+[v for v in select(x)['values'].values() if v is not None])
            yvalue=max([F(0)]+[v for v in select(y)['values'].values() if v is not None])
            self.assertLessEqual(xvalue,yvalue)

    def test_retain_option_floors_value_zero(self):
        s=replace(Setting(),b_market=replace(Setting().b_market,a=F(2)),a_market=replace(Setting().a_market,a=F(2)))
        self.assertEqual(select(s)['winner'],'retain')

    def test_incumbent_resource_counterfactual(self):
        s=Setting()
        p=projects(s)['incumbent']
        for t in range(1,5):
            a=market_at(s,t,'A')
            self.assertEqual(provider_profit(s,p,t), a.service(F(2))[1]-a.service(F(1))[1])

    def test_discounting_changes_values_not_entry_accounting(self):
        full=select(Setting())['values']
        less=select(replace(Setting(),beta=F(9,10)))['values']
        self.assertTrue(all(less[k]<=full[k] for k in full if full[k] is not None))

    def test_no_salvage_counts_both_real_costs_once(self):
        s=Setting();p=projects(s)['redesign']
        self.assertEqual(p.cost,upper_cent(qualify(REDESIGNED_PROFILE,EPSILON,2).total_cost)+s.fixed_design_cost+F(3))

    def test_binding_formula_restricted(self):
        with self.assertRaises(ValueError):binding_switch(replace(Setting(),salvage_share=F(1,4)))
        with self.assertRaises(ValueError):binding_switch(replace(Setting(),beta=F(9,10)))

    def test_reproducible_results(self):
        self.assertEqual(json.dumps(experiment(),sort_keys=True),json.dumps(experiment(),sort_keys=True))

    def test_invalid_inputs(self):
        for k,v in [('initial_cash',F(-1)),('horizon',0),('beta',F(0)),
                    ('demand_decline',F(-1)),('redesigned_lag',-1),('salvage_share',F(1))]:
            with self.assertRaises(ValueError):replace(Setting(),**{k:v})


if __name__=='__main__':unittest.main()
