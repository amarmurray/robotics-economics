"""Scoped correctness checks. Rational enumeration is not a proof or field evidence."""
import unittest
from dataclasses import replace
from fractions import Fraction as F
from math import erf, sqrt

from data_value import expected_value, probability
from teleoperation import (Model, State, Solver, signal_branches, transitions,
                          terminal_by_regime, joint_expected_value,
                          brute_force_two_periods, general_two_batch_formula,
                          customer_increment)


class TeleoperationTests(unittest.TestCase):
    def test_exact_adaptive_policy_and_posteriors(self):
        model, initial = Model(), State()
        solver = Solver(model)
        self.assertEqual(solver.solve(2, initial), (F(31, 5), "ground"))
        branches = transitions(model, initial, "ground")
        self.assertEqual([(label, mass, nxt.prior) for label, mass, nxt in branches],
                         [(True, F(11, 40), F(19, 22)), (False, F(29, 40), F(1, 58))])
        self.assertEqual([solver.solve(1, nxt)[1] for _, _, nxt in branches],
                         ["source", "routine"])

    def test_independent_contingent_tree_enumeration(self):
        for prior in (F(0), F(1, 10), F(1, 4), F(1, 2), F(1)):
            for accuracy in (F(1, 2), F(4, 5), F(19, 20), F(1)):
                model, initial = Model(accuracy=accuracy), State(prior=prior)
                self.assertEqual(Solver(model).solve(2, initial)[0],
                                 brute_force_two_periods(model, initial)["optimal"]["value"])

    def test_closed_form_arbitrary_terminal_values(self):
        model = Model()
        payoff = ((F(0), F(0), F(0), F(0)), (F(0), F(0), F(0), F(20)))
        formula = general_two_batch_formula(F(1, 4), F(19, 20), F(2), F(4), payoff)
        self.assertEqual(formula["best_increment"], F(1, 5))
        self.assertEqual(formula["committed_pair"], F(-1))
        self.assertEqual(Solver(model).solve(2, State())[0], 6+formula["best_increment"])

    def test_signal_does_not_add_data_or_training_quality(self):
        early, late = Model(), Model(early_signal=False)
        for good in (False, True):
            for x, g in ((0, 0), (1, 0), (0, 1), (1, 1)):
                state = State(source=x, ground=g)
                self.assertEqual(terminal_by_regime(early, state, good),
                                 terminal_by_regime(late, state, good))
        self.assertEqual(Solver(late).solve(2, State())[0], F(6))
        self.assertEqual(brute_force_two_periods(early, State())["precommitted"]["value"], F(6))

    def test_uninformative_and_perfect_signals(self):
        self.assertEqual(Solver(Model(accuracy=F(1, 2))).solve(2, State())[0], F(6))
        self.assertEqual(Solver(Model(accuracy=F(1))).solve(2, State()), (F(13, 2), "ground"))

    def test_bayes_martingale_and_mass(self):
        for prior in (F(0), F(1, 7), F(3, 5), F(1)):
            for accuracy in (F(1, 2), F(3, 4), F(1)):
                branches = signal_branches(prior, accuracy)
                self.assertEqual(sum(mass for _, mass, _ in branches), 1)
                self.assertEqual(sum(mass*post for _, mass, post in branches), prior)

    def test_direct_specialist_is_real_competing_action(self):
        ordinary = Model(allow_direct=True)
        strong = replace(ordinary, direct_value=F(9))
        self.assertEqual(Solver(ordinary).solve(2, State()), (F(31, 5), "ground"))
        # Ordering direct and routine ties, hence first routine under stable tie rule.
        self.assertEqual(Solver(strong).solve(2, State())[0], F(8))
        self.assertGreater(Solver(strong).action_values(State())["direct"],
                           Solver(strong).action_values(State())["ground"])
        self.assertEqual(Solver(strong).solve(2, State())[0],
                         brute_force_two_periods(strong, State())["optimal"]["value"])

    def test_lab_more_informative_but_too_costly(self):
        model = Model(allow_lab=True)
        values = Solver(model).action_values(State())
        self.assertEqual(values["lab"], F(11, 2))
        self.assertGreater(values["ground"], values["lab"])

    def test_expiring_source_reverses_order(self):
        model, initial = Model(source_deadline=1), State(prior=F(1, 2))
        self.assertEqual(Solver(model).solve(2, initial), (F(10), "source"))
        self.assertEqual(brute_force_two_periods(model, initial)["optimal"]["value"], F(10))

    def test_zero_economic_gain_does_not_buy_learning(self):
        self.assertEqual(Solver(Model(transfer_value=F(0))).solve(2, State()), (F(6), "routine"))

    def test_free_relevant_production_byproduct_erases_timing_premium(self):
        early = Model(source_margin=F(3))
        late = replace(early, early_signal=False)
        self.assertEqual(Solver(early).solve(2, State())[0], F(7))
        self.assertEqual(Solver(late).solve(2, State())[0], F(7))
        self.assertEqual(brute_force_two_periods(early, State())["optimal"]["value"], F(7))

    def test_joint_outcome_accounting_matches_parent_only_when_independent(self):
        p = (F(1, 4), F(1, 2))
        values = (F(0), F(2), F(3), F(20))
        law = tuple(probability(mask, p) for mask in range(4))
        self.assertEqual(joint_expected_value(law, values), expected_value(p, values))
        shared = (F(3, 4), F(0), F(0), F(1, 4))
        bundle = (F(0), F(0), F(0), F(20))
        self.assertEqual(joint_expected_value(shared, bundle), F(5))
        self.assertEqual(expected_value((F(1, 4), F(1, 4)), bundle), F(5, 4))

    def test_gaussian_alternative_uses_existing_information_equation(self):
        model = Model(technology="gaussian", source_margin=F(2), ground_margin=F(0))
        initial = State()
        scalar = terminal_by_regime(model, State(source=1, ground=1), True)
        expected = 30*(erf(1/sqrt(2*2.6))-erf(1/sqrt(2*5.1)))
        self.assertAlmostEqual(scalar, expected, places=12)
        early = Solver(model).solve(2, initial)
        delayed = Solver(replace(model, early_signal=False)).solve(2, initial)
        self.assertEqual(early[1], "ground")
        self.assertGreater(early[0], delayed[0])
        self.assertAlmostEqual(early[0], brute_force_two_periods(model, initial)["optimal"]["value"], places=12)

    def test_general_formula_gaussian_nonzero_partial_values(self):
        model = Model(technology="gaussian", source_margin=F(2), ground_margin=F(0))
        payoff = tuple(tuple(terminal_by_regime(model, State(source=x, ground=g), good)
                             for x, g in ((0, 0), (1, 0), (0, 1), (1, 1)))
                       for good in (False, True))
        formula = general_two_batch_formula(F(1, 4), model.accuracy, 1, 3, payoff)
        self.assertAlmostEqual(Solver(model).solve(2, State())[0], 6+formula["best_increment"], places=12)

    def test_repeated_information_batches_not_forbidden_in_robustness(self):
        model = Model(technology="gaussian", source_margin=F(2), ground_margin=F(0),
                      source_limit=2, ground_limit=2)
        dp = Solver(model).solve(2, State())
        self.assertEqual(dp[1], "ground")
        self.assertAlmostEqual(dp[0], brute_force_two_periods(model, State())["optimal"]["value"], places=12)

    def test_customer_price_outside_option_and_saturation(self):
        self.assertEqual(customer_increment(5, 1, 2, 6), 0)
        self.assertEqual(customer_increment(5, 3, 2, 6), 5)
        self.assertEqual(customer_increment(5, 6, 2, 6), 20)
        self.assertEqual(customer_increment(5, 12, 2, 6), 20)
        self.assertEqual(customer_increment(5, 12, 8, 6), 0)

    def test_discounting_and_full_menu_against_enumeration(self):
        model = Model(discount=F(4, 5), allow_direct=True, allow_lab=True)
        self.assertEqual(Solver(model).solve(2, State())[0],
                         brute_force_two_periods(model, State())["optimal"]["value"])

    def test_current_hours_can_rise_while_total_hours_fall_with_wage(self):
        # Same future accepted service. No-training: 4 future hours. Training:
        # one current hour plus 3 real nonlabor units, removes those future hours.
        policies = [(0, 0, 4), (3, 1, 0)]
        choose = lambda wage: min(policies, key=lambda row: row[0]+wage*(row[1]+row[2]))
        low, high = choose(F(1, 2)), choose(F(2))
        self.assertEqual(low, policies[0])
        self.assertEqual(high, policies[1])
        self.assertGreater(high[1], low[1])
        self.assertLess(high[1]+high[2], low[1]+low[2])

    def test_invalid_probability_and_joint_law_rejected(self):
        with self.assertRaises(ValueError):
            signal_branches(F(3, 2), F(1))
        with self.assertRaises(ValueError):
            joint_expected_value((F(1, 3), F(1, 3)), (0, 1))
        with self.assertRaises(ValueError):
            Model(accuracy=F(1, 4))


if __name__ == "__main__":
    unittest.main()
