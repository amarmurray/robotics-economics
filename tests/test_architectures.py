"""Matched service, cent accounting and conditional price/role counterfactuals."""
import copy
import hashlib
import json
from pathlib import Path
import random
import unittest
from unittest.mock import patch

from model.architectures import ROLES, resolve
from model.engine import ROOT, run_scenario, run_architecture_comparison

CELL = "CELL-M05-auto-assembly-US-2025"


def run(architecture=None, overrides=None, year=2030):
    return run_architecture_comparison(CELL, overrides, year=year, architecture_overrides=architecture)


def row(result, name="licensed_independent"):
    return next(x for x in result["architectures"] if x["architecture_id"] == name)


def entities(result):
    return {x["entity"]:x["lifetime_net_incremental_cents"] for x in result["entities"]}


class ArchitectureEconomics(unittest.TestCase):
    def test_declared_service_and_all_lifetime_conservation_identities(self):
        rng = random.Random(107)
        cases = [run()]
        for _ in range(8):
            cases.append(run({"common":{"model_fee_usd_year":round(rng.uniform(0,12000),2)},
                              "profiles":{"licensed_independent":{"adaptation_engineering_hours":rng.uniform(0,400),"support_minutes_delta":rng.uniform(-2,8)}}},
                             {"assembly_yield":rng.uniform(.2,1),"retirement_years":rng.choice([2,5,12])}))
        for case in cases:
            for r in case["architectures"]:
                self.assertEqual(r["accepted_service_units_year"], case["cell"]["annual_units_per_site"])
                self.assertLessEqual(r["robot_accepted_units_year"], r["accepted_service_units_year"])
                self.assertEqual(sum(x["net_incremental_cents"] for x in r["cash_ledger"]),r["lifetime_consolidated_net_incremental_cents"])
                self.assertEqual(sum(entities(r).values()),r["lifetime_baseline_cost_credit_cents"]-r["lifetime_cash_cost_cents"])
                self.assertEqual(sum(x["amount_cents"] for x in r["expense_ledger"] if x["resource_cost"]),r["lifetime_resource_cost_cents"])
                self.assertEqual(sum(x["external_receipts_cents"] for x in r["cash_ledger"]),sum(x["external_payments_cents"] for x in r["cash_ledger"]))
                self.assertAlmostEqual(r["resource_saving_vs_digital_human_usd_year"]-r["cash_benefit_usd_year"],r["unavoidable_released_payroll_cash_usd_year"])

    def test_license_fee_redistributes_without_creating_resource_cost(self):
        a, b = run(), run({"common":{"model_fee_usd_year":7000}})
        for old,new in zip(a["architectures"],b["architectures"]):
            self.assertEqual(old["lifetime_resource_cost_cents"],new["lifetime_resource_cost_cents"])
            self.assertEqual(old["lifetime_consolidated_net_incremental_cents"],new["lifetime_consolidated_net_incremental_cents"])
            self.assertEqual(old["robot_accepted_units_year"],new["robot_accepted_units_year"])
        old,new=row(a),row(b)
        delta=3000*100*old["horizon_years"]
        self.assertEqual(entities(new)["model_supplier"]-entities(old)["model_supplier"],delta)
        self.assertEqual(entities(new)["customer_operator"]-entities(old)["customer_operator"],-delta)
        self.assertEqual(entities(row(a,"open_adapted")),entities(row(b,"open_adapted")))

    def test_service_payment_and_hardware_price_are_transfers(self):
        a,b=run(),run({"common":{"service_price_fraction":.9}})
        old,new=row(a,"model_led_operator"),row(b,"model_led_operator")
        self.assertEqual(old["lifetime_resource_cost_cents"],new["lifetime_resource_cost_cents"])
        self.assertEqual(sum(entities(old).values()),sum(entities(new).values()))
        self.assertLess(entities(new)["customer"],entities(old)["customer"])
        cheap=run(overrides={"price_multiplier":.25})
        self.assertEqual(row(a)["lifetime_resource_cost_cents"],row(cheap)["lifetime_resource_cost_cents"])
        self.assertFalse(row(cheap)["fee_intervals"]["model_fee"]["other_entities_nonnegative"])
        self.assertFalse(row(cheap)["fee_intervals"]["model_fee"]["all_party_interval_feasible"])

    def test_fee_interval_boundaries_and_positive_total_with_losing_supplier(self):
        base=row(run());interval=base["fee_intervals"]["model_fee"]
        self.assertGreater(base["cash_benefit_usd_year"],0)
        self.assertEqual(interval["lower_usd_year"],4200)
        self.assertEqual(next(x["annual_equivalent_net_usd"] for x in base["entities"] if x["entity"]=="model_supplier"),-200)
        for amount, entity in [(interval["lower_usd_year"],"model_supplier"),(interval["upper_usd_year"],"customer_operator")]:
            r=row(run({"common":{"model_fee_usd_year":amount}}))
            self.assertEqual(entities(r)[entity],0)
            self.assertTrue(r["all_entities_nonnegative_at_selected_payments"])
        below=row(run({"common":{"model_fee_usd_year":interval["lower_usd_year"]-.01}}))
        above=row(run({"common":{"model_fee_usd_year":interval["upper_usd_year"]+.01}}))
        self.assertLess(entities(below)["model_supplier"],0)
        self.assertLess(entities(above)["customer_operator"],0)

    def test_role_consolidation_never_creates_another_resource_or_gain(self):
        a=row(run())
        b=row(run({"profiles":{"licensed_independent":{"role_entities":{r:"one_entity" for r in ROLES}}}}))
        self.assertEqual(a["lifetime_resource_cost_cents"],b["lifetime_resource_cost_cents"])
        self.assertEqual(a["lifetime_consolidated_net_incremental_cents"],b["lifetime_consolidated_net_incremental_cents"])
        self.assertEqual(len(b["entities"]),1)
        self.assertTrue(all(x["internal_eliminated"] for x in b["transfer_ledger"]))
        self.assertEqual(b["fee_intervals"]["model_fee"]["status"],"internal_transfer_eliminated")

    def test_fractional_annual_costs_round_price_bounds_outward_and_infeasibility_survives(self):
        base=row(run(overrides={"retirement_years":7}))
        bound=base["fee_intervals"]["model_fee"]["lower_usd_year"]
        at=row(run({"common":{"model_fee_usd_year":bound}}, {"retirement_years":7}))
        below=row(run({"common":{"model_fee_usd_year":round(bound-.01,2)}}, {"retirement_years":7}))
        self.assertGreaterEqual(entities(at)["model_supplier"],0)
        self.assertLess(entities(below)["model_supplier"],0)
        impossible=row(run({"profiles":{"licensed_independent":{"adaptation_engineering_hours":5000}}}))
        interval=impossible["fee_intervals"]["model_fee"]
        self.assertEqual(interval["status"],"no_nonnegative_fee_interval")
        self.assertGreater(interval["lower_cents_year"],interval["upper_cents_year"])

    def test_reference_uses_outright_purchase_and_zero_robot_capability_is_not_free_output(self):
        a,b=run(overrides={"arrangement":"sale"}),run(overrides={"arrangement":"lease"})
        for first,second in zip(a["architectures"],b["architectures"]):
            self.assertEqual(first["cash_ledger"],second["cash_ledger"])
        zero=run(overrides={"capability":0,"capability_progress":0,"learning_transfer":0})
        for case in zero["architectures"]:
            self.assertEqual(case["robot_accepted_units_year"],0)
            self.assertGreater(case["retained_human_hours_year"],0)
            self.assertLess(case["cash_benefit_usd_year"],0)

    def test_itemized_zero_extras_reproduce_shared_physical_resource_cost(self):
        base=run_scenario()
        settings=resolve()
        for p in settings["profiles"].values():
            for key in ['demonstration_hours','adaptation_engineering_hours','adaptation_compute_usd','validation_engineering_hours','qualification_resources_usd','model_development_allocation_usd_upfront','model_maintenance_usd_year','network_resilience_usd_year']:
                p[key]=0
            p.update(integration_multiplier=1,inference_resource_multiplier=1,support_minutes_delta=0)
        expected=next(r for y in base["joint_by_year"] if y["year"]==2030 for r in y["comparisons"] if r["cell_id"]==CELL)["C11"]
        for r in run(settings)["architectures"]:
            self.assertAlmostEqual(r["resource_cost_usd_year"],expected,delta=.02)

    def test_adaptation_and_support_have_different_direct_effects(self):
        base=row(run())
        adaptation=row(run({"profiles":{"licensed_independent":{"adaptation_engineering_hours":140}}}))
        support=row(run({"profiles":{"licensed_independent":{"support_minutes_delta":10}}}))
        self.assertEqual(adaptation["resource_cost_usd_year"]-base["resource_cost_usd_year"],2000)
        self.assertEqual(adaptation["robot_accepted_units_year"],base["robot_accepted_units_year"])
        self.assertLess(support["robot_accepted_units_year"],base["robot_accepted_units_year"])
        self.assertGreater(support["retained_human_hours_year"],base["retained_human_hours_year"])
        self.assertEqual(support["accepted_service_units_year"],base["accepted_service_units_year"])

    def test_unqualified_case_has_no_economic_rank(self):
        r=row(run({"profiles":{"licensed_independent":{"assume_rights_available":False}}}))
        self.assertEqual(r["status"],"not_admitted_under_assumptions")
        self.assertIsNone(r["resource_cost_usd_year"])
        self.assertNotIn("entities",r)

    def test_equal_technology_path_labels_do_not_change_production(self):
        base=run()
        for r in base["customer_path_comparison"]:
            self.assertEqual(r["incumbent_resource_cost_usd_year"],r["newco_resource_cost_usd_year"])
            self.assertTrue(r["physical_service_identical"])
        changed=run({"common":{"newco_setup_usd":20000}})
        for r in changed["customer_path_comparison"]:
            self.assertAlmostEqual(r["newco_resource_cost_usd_year"]-r["incumbent_resource_cost_usd_year"],4000)
            self.assertTrue(r["physical_service_identical"])

    def test_invalid_inputs_and_preserved_source_unknowns(self):
        before=(ROOT/"data/frontier_model_economics.json").read_bytes()
        invalid=[[],{"unknown":1},{"common":{"model_fee_usd_year":True}},{"common":{"model_fee_usd_year":.001}},
                 {"common":{"model_fee_usd_year":float('nan')}},{"common":{"model_fee_usd_year":1e308}},{"common":{"model_fee_usd_year":10**400}},
                 {"profiles":{"licensed_independent":{"adaptation_engineering_hours":-1}}},
                 {"profiles":{"licensed_independent":{"assume_compatible":1}}},
                 {"profiles":{"licensed_independent":{"role_entities":{"customer":"one"}}}}]
        for bad in invalid:
            with self.subTest(bad=bad),self.assertRaises(ValueError):run(bad)
        run()
        self.assertEqual(before,(ROOT/"data/frontier_model_economics.json").read_bytes())
        source=json.loads(before)
        self.assertTrue(all(x["annual_resource_cost_usd"] is None for x in source["architecture_alternatives"]))

    def test_all_inputs_roundtrip_and_helper_source_changes_identity(self):
        a=run({"common":{"model_fee_usd_year":5000},"profiles":{"licensed_independent":{"adaptation_engineering_hours":17.5}}})
        b=run_architecture_comparison(a["comparison_scope"]["cell_id"],a["parameters"],a["preset"],a["digital_paths"],a["comparison_scope"]["year"],a["architecture_parameters"])
        self.assertEqual(a,b)
        original=Path.read_bytes
        def altered(path):
            value=original(path)
            return value+b'\n# changed architecture helper\n' if path.name=='architectures.py' else value
        with patch.object(Path,'read_bytes',altered):c=run()
        d=run()
        self.assertNotEqual(c["scenario_hash"],d["scenario_hash"])
        self.assertNotEqual(c["case_hash"],d["case_hash"])
        self.assertEqual(c["architectures"],d["architectures"])


if __name__ == "__main__":unittest.main()
