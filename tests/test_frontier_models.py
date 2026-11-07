"""Conserve source boundaries across the intelligence-layer evidence packet."""
import copy
import json
import unittest
from model.frontier_models import ROOT, PACKAGE, validate_packet, acquisition_reconciliation, frontier_model_summary, regional_source_arithmetic, deployment_source_arithmetic


class FrontierEvidence(unittest.TestCase):
    def setUp(self):
        self.packet = json.loads((ROOT/PACKAGE).read_text())

    def test_filing_components_reconcile_without_calling_noncash_cash(self):
        r = acquisition_reconciliation(self.packet)
        self.assertEqual((r["cash_consideration"], r["equity_fair_value"], r["escrow_fair_value"]), (9, 9, 2))
        self.assertEqual((r["total_consideration"], r["net_assets_sold"], r["seller_gain"]), (20, 15, 5))
        self.assertEqual((r["completion_date"], r["announcement_date"]), ("2026-03-27", "2026-04-15"))
        self.assertTrue(all(r["checks"].values()))

    def test_missing_mixed_unit_and_inconsistent_amounts_fail(self):
        for change in ({"value": None}, {"value": True}, {"unit": "USD"}, {"value": 20}, {"value": float("nan")}):
            packet = copy.deepcopy(self.packet)
            q = next(e for e in packet["evidence"] if e["evidence_id"] == "K-E006")["quantities"][0]
            q.update(change)
            with self.assertRaises(ValueError):
                acquisition_reconciliation(packet)

    def test_rights_conflict_cannot_turn_into_blanket_clearance(self):
        card = next(r for r in self.packet["model_rights_cards"] if r["artifact_id"] == "K-R-VLA-WEIGHTS")
        self.assertEqual(card["rights_status"], "conflicting")
        self.assertFalse(card["commercial_use_resolved"])
        card["commercial_use_resolved"] = True
        with self.assertRaisesRegex(ValueError, "rights"):
            validate_packet(self.packet)

    def test_unpriced_architecture_cannot_import_a_vendor_score_as_cost(self):
        self.packet["architecture_alternatives"][0]["annual_resource_cost_usd"] = 56
        with self.assertRaisesRegex(ValueError, "Unpriced"):
            validate_packet(self.packet)

    def test_source_identity_joins_reject_duplicates_and_missing_actors(self):
        validate_packet(self.packet)
        self.packet["model_labs"].append(self.packet["model_labs"][0])
        with self.assertRaisesRegex(ValueError, "Duplicate"):
            validate_packet(self.packet)
        self.packet["model_labs"].pop()
        self.packet["frontier_models"][0]["actor_id"] = "unresolved"
        with self.assertRaisesRegex(ValueError, "actor"):
            validate_packet(self.packet)

    def test_summary_keeps_run_rate_recognition_and_comparison_limits(self):
        summary = frontier_model_summary(packet=self.packet)
        q = {q["quantity_id"]: q for q in summary["skild_issuer_reported_quantities"]}
        self.assertEqual(q["K-Q-SKILD-ARR"]["unit"], "USD per year")
        self.assertIsNone(q["K-Q-SKILD-ARR"]["value"])
        self.assertEqual(q["K-Q-SKILD-RECOGNIZED"]["unit"], "USD")
        self.assertFalse(summary["scenario_inputs_used"])
        self.assertFalse(summary["architecture_costs_available"])
        self.assertFalse(summary["model_benchmark_ranking_available"])


class RegionalFrontierEvidence(unittest.TestCase):
    def setUp(self):
        self.packet=json.loads((ROOT/PACKAGE).read_text())

    def quantity(self,key):
        return next(q for e in self.packet['evidence'] for q in e.get('quantities',[]) if q['quantity_id']==key)

    def test_allex_average_is_not_a_whole_job_probability(self):
        r=regional_source_arithmetic(self.packet)
        self.assertEqual(r['allex']['reported_mean'],86.8)
        self.assertEqual(r['allex']['recomputed_mean'],86.8)
        self.assertIsNone(r['allex']['whole_job_success_probability'])
        card=next(c for c in self.packet['benchmark_cards'] if c['benchmark_id']=='K-B-RLDX-ALLEX')
        card['whole_task_success_established']=True
        with self.assertRaisesRegex(ValueError,'Mixed progress'):regional_source_arithmetic(self.packet)

    def test_table9_preserves_the_source_conflict_without_inventing_correction(self):
        r=regional_source_arithmetic(self.packet)['rldx_table9']
        self.assertTrue(r['source_conflict_present'])
        self.assertEqual([row['score_from_printed_counts_and_rule'] for row in r['rows']],[13,18])
        self.assertEqual([row['printed_score'] for row in r['rows']],[16,20])
        self.assertEqual([sum(row['printed_counts'].values()) for row in r['rows']],[24,24])
        self.assertEqual([row['printed_percent'] for row in r['rows']],[66.7,83.3])
        self.assertIsNone(r['corrected_empirical_effect'])
        card=next(c for c in self.packet['benchmark_cards'] if c['benchmark_id']=='K-B-RLDX-TABLE9')
        self.assertEqual(card['model_ids'],['K-M-RLDX-PT'])
        card['outcome_weights']['PARTIAL']=1
        with self.assertRaisesRegex(ValueError,'stated scoring rule'):regional_source_arithmetic(self.packet)

    def test_rynn_progress_and_final_success_remain_separate(self):
        r=regional_source_arithmetic(self.packet)
        rows=r['rynn_trials']['regimes']
        self.assertEqual([x['reported_final_success_percent'] for x in rows],[86.67,91.67])
        self.assertEqual([x['reported_process_percent'] for x in rows],[91.28,94.14])
        self.assertEqual([x['full_completions_implied_by_percentages'] for x in rows],[52,55])
        self.assertTrue(all(x['protocol_trials']==60 and not x['raw_trial_logs_verified'] for x in rows))
        self.assertFalse(r['cross_model_ranking_available'])
        self.quantity('K-Q-RYNN-TRIALS')['value']=24
        with self.assertRaisesRegex(ValueError,'reconcile'):regional_source_arithmetic(self.packet)

    def test_latency_retains_named_statistic_and_does_not_become_a_deadline(self):
        r=regional_source_arithmetic(self.packet)['rldx_latency']
        self.assertEqual((r['eager_p50_ms'],r['optimized_p50_ms']),(71.22,43.7))
        self.assertAlmostEqual(r['recomputed_ratio'],71.22/43.7)
        self.assertIn('RTX 5090',r['hardware'])
        self.assertIn('no tail',r['scope'])
        for key,value in [('unit','seconds'),('value',0),('value',None),('value',True),('value',float('nan'))]:
            saved=copy.deepcopy(self.quantity('K-Q-RLDX-P50-OPT'))
            self.quantity('K-Q-RLDX-P50-OPT')[key]=value
            with self.assertRaises(ValueError):regional_source_arithmetic(self.packet)
            self.quantity('K-Q-RLDX-P50-OPT').update(saved)

    def test_public_noncommercial_grant_cannot_clear_paid_deployment(self):
        card=next(c for c in self.packet['model_rights_cards'] if c['artifact_id']=='K-R-RLDX-WEIGHTS')
        self.assertEqual(card['public_grant'],'noncommercial_only')
        self.assertFalse(card['commercial_use_resolved'])
        card['commercial_use_resolved']=True
        with self.assertRaisesRegex(ValueError,'commercial clearance'):validate_packet(self.packet)

    def test_operator_partner_role_cannot_become_a_checkpoint_attribution(self):
        d=next(d for d in self.packet['deployment_cards'] if d['deployment_id'].startswith('K-DEP-CJ'))
        self.assertIsNone(d['model_id'])
        self.assertEqual(d['reported_robot_count_quantity_id'],'K-Q-CJ-YANGJI-ROBOTS')
        d['model_id']='K-M-RLDX-ALLEX'
        with self.assertRaisesRegex(ValueError,'attribution'):validate_packet(self.packet)

    def test_repeated_operator_announcement_is_not_a_second_deployment(self):
        d=copy.deepcopy(self.packet['deployment_cards'][0]);d['deployment_id']='duplicate-press-release'
        self.packet['deployment_cards'].append(d)
        with self.assertRaisesRegex(ValueError,'Duplicate deployment'):validate_packet(self.packet)

    def test_benchmark_units_identity_and_calibration_guards(self):
        self.packet['benchmark_cards'][-1]['commercial_service_calibration']=True
        with self.assertRaisesRegex(ValueError,'commercial service'):validate_packet(self.packet)
        self.packet['benchmark_cards'][-1]['commercial_service_calibration']=False
        self.packet['model_rights_cards'][-1]['model_ids']=['not-a-released-or-reported-model']
        with self.assertRaisesRegex(ValueError,'model/release'):validate_packet(self.packet)

    def test_duplicate_or_impossible_source_counts_are_rejected(self):
        self.quantity('K-Q-RLDX-T9-REAL-FULL')['value']=10
        with self.assertRaisesRegex(ValueError,'sum'):regional_source_arithmetic(self.packet)
        self.quantity('K-Q-RLDX-T9-REAL-FULL')['value']=9
        claim=next(e for e in self.packet['evidence'] if e['evidence_id']=='K-E030')
        claim['quantities'].append(copy.deepcopy(claim['quantities'][0]))
        with self.assertRaisesRegex(ValueError,'Duplicate source quantity'):regional_source_arithmetic(self.packet)


class DeploymentEvidence(unittest.TestCase):
    def setUp(self):
        self.packet=json.loads((ROOT/PACKAGE).read_text())

    def quantity(self, key):
        return next(q for e in self.packet['evidence'] for q in e.get('quantities',[]) if q['quantity_id']==key)

    def test_service_margin_is_arithmetic_not_roi_or_staffing(self):
        r=deployment_source_arithmetic(self.packet)['napkin_service']
        self.assertAlmostEqual(r['arithmetic_accepted_per_window'],1590.3)
        self.assertEqual(r['reported_accepted_napkins'],1590)
        self.assertAlmostEqual(r['surplus_as_percent_of_required_output'],6.02)
        self.assertAlmostEqual(r['conditional_effective_hours_required'],1500/88.35)
        self.assertAlmostEqual(r['conditional_additional_time_loss_budget_hours'],18-1500/88.35)
        self.assertFalse(r['time_sensitivity_is_observed_uptime'])
        for k in ('observed_uptime','financial_roi','paid_labor_removed'):self.assertIsNone(r[k])

    def test_reported_output_rounding_is_checked_without_repair(self):
        self.quantity('K-Q-DYNA-DTF-OUTPUT')['value']=1700
        with self.assertRaisesRegex(ValueError,'reconcile'):deployment_source_arithmetic(self.packet)

    def test_unknown_invalid_and_mixed_unit_service_inputs_fail(self):
        original=copy.deepcopy(self.quantity('K-Q-DYNA-DTF-RATE'))
        for change in ({'value':None},{'value':True},{'value':0},{'value':float('nan')},{'unit':'folds per day'},{'population':'another customer'}):
            self.quantity('K-Q-DYNA-DTF-RATE').update(change)
            with self.assertRaises(ValueError):deployment_source_arithmetic(self.packet)
            self.quantity('K-Q-DYNA-DTF-RATE').update(original)
        self.quantity('K-Q-DYNA-DTF-QUALITY')['value']=101
        with self.assertRaisesRegex(ValueError,'quality percent'):deployment_source_arithmetic(self.packet)

    def test_metrics_cannot_be_promoted_into_whole_job_probabilities(self):
        r=deployment_source_arithmetic(self.packet)
        self.assertEqual([v['reported_percent_of_task_ceiling'] for v in r['dyna_scaling']['rungs']],[20,28,45,53])
        self.assertEqual([v['reported_partial_credit_percent'] for v in r['dyna_language']['variants']],[35,67,96])
        self.assertIsNone(r['dyna_scaling']['whole_job_success_probability'])
        self.assertIsNone(r['dyna_language']['complete_task_percent'])
        card=next(c for c in self.packet['benchmark_cards'] if c['benchmark_id']=='K-B-DYNA-ONROBOT')
        card['whole_task_success_established']=True
        with self.assertRaisesRegex(ValueError,'Mixed or partial'):deployment_source_arithmetic(self.packet)

    def test_partial_credit_rule_and_unobserved_financial_boundaries_are_guarded(self):
        card=next(c for c in self.packet['benchmark_cards'] if c['benchmark_id']=='K-B-DYNA-LANGUAGE')
        card['outcome_weights']['correct_attempt_incomplete']=1
        with self.assertRaisesRegex(ValueError,'partial-credit'):deployment_source_arithmetic(self.packet)
        card['outcome_weights']['correct_attempt_incomplete']=0.5
        for k,v in [('financial_roi_established',True),('paid_labor_removal_established',True),('no_additional_uptime_factor_applied',False),('hourly_rate_time_basis','active_time_verified')]:
            old=self.packet['deployment_source_checks'][k];self.packet['deployment_source_checks'][k]=v
            with self.assertRaisesRegex(ValueError,'boundaries'):deployment_source_arithmetic(self.packet)
            self.packet['deployment_source_checks'][k]=old

    def test_customer_accounts_and_family_attribution_are_not_fleet_or_checkpoint(self):
        row=next(d for d in self.packet['deployment_cards'] if d['deployment_id']=='K-DEP-DYNA-MONSTER')
        self.assertIsNone(row['model_id'])
        self.assertIsNone(row['reported_robot_count_quantity_id'])
        self.assertEqual(self.quantity('K-Q-MONSTER-CUSTOMERS')['unit'],'customer accounts')
        row['model_id']='K-M-DYNA2-PROD'
        with self.assertRaisesRegex(ValueError,'attribution'):validate_packet(self.packet)


if __name__ == "__main__":
    unittest.main()
