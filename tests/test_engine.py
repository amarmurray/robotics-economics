"""Accounting, adverse-state and causal-boundary checks for the common engine."""
import copy
import hashlib
import json
from pathlib import Path
import unittest

from model.engine import ROOT, catalog, run_scenario
from model.evidence import economic_atlas_summary
from model.packages import load_accepted_packages


class ModelAccounting(unittest.TestCase):
    def test_high_memory_is_the_same_hardware_in_both_robot_branches(self):
        controls={"capability":1,"capability_progress":0,"uptime":1,
                  "intervention_minutes":0,"digital_efficiency":0,
                  "coordination":0,"digital_cost_usd":0}
        standard=run_scenario(controls)
        high=run_scenario({**controls,"onboard_configuration":"high_memory"})
        for old,new in zip(standard["joint"],high["joint"]):
            self.assertEqual(new["C00"],old["C00"])
            self.assertEqual(new["C01"],old["C01"])
            # Explicit witness: $800 annual board charge plus $32 electricity
            # at 2,000 hours, 0.1 extra kW, $0.16/kWh, in each robot branch.
            for branch in ("C10","C11"):
                self.assertAlmostEqual(new[branch]-old[branch],832)
            self.assertAlmostEqual(new["C11"]-new["C10"],600)
            self.assertAlmostEqual(new["cost_interaction"],old["cost_interaction"])

    @classmethod
    def setUpClass(cls):
        cls.c=catalog()
        cls.runs=[run_scenario(preset=p) for p in cls.c["presets"]]
        cls.runs += [run_scenario(p) for p in (
            {"supply_multiplier":0}, {"capability":0,"capability_progress":0},
            {"assembly_yield":.1,"spares_rate":.5,"years":12},
            {"arrangement":"lease","support_budget_hours":200,"onboard_configuration":"high_memory"},
            {"provider_capital_usd":0}, {"labor_avoidability":0},
            {"capability":1,"capability_progress":0,"uptime":1,"intervention_minutes":0,"coordination":.6,"digital_efficiency":0,"labor_avoidability":1})]
        # Existing stock, resource, demand and cash invariants also cover changing
        # comparators and adverse annual coordination, across both configurations.
        import random
        rng = random.Random(418)
        for i in range(12):
            paths = {"schema_version": "digital-annual-paths/0.1", "base_year": cls.c["base_year"],
                     "epistemic_status": "synthetic_assumption",
                     "digital_efficiency": [rng.uniform(0, .6) for _ in range(8)],
                     "coordination": [rng.uniform(-.4, .6) for _ in range(8)],
                     "digital_cost_usd": [rng.uniform(0, 20000) for _ in range(8)]}
            cls.runs.append(run_scenario({"years": 8, "assembly_yield": .25 + .05*i,
                                          "onboard_configuration": "high_memory" if i%2 else "standard"}, digital_paths=paths))

    def test_component_and_finished_goods_conservation(self):
        for r in self.runs:
            for x in r["fleet"]["components"]:
                self.assertAlmostEqual(x["opening_inventory"]+x["qualified_net_receipts"]-x["service_consumed"]-x["assembly_consumed"]-x["rework_consumed"]-x["other_allocations"],x["closing_inventory"])
                self.assertGreaterEqual(x["closing_inventory"],-1e-8)
                self.assertLessEqual(x["service_consumed"],x["service_required"]+1e-8)
            previous={}
            for x in r["fleet"]["production"]:
                self.assertAlmostEqual(x["opening_finished"]+x["accepted_completions"]-x["shipments"],x["closing_finished"])
                self.assertGreaterEqual(x["closing_finished"],-1e-8)
                old=previous.get(x["system_id"],{})
                self.assertAlmostEqual(old.get("work_in_progress",0)+x["assembly_starts"]-x["accepted_completions"]-x["rejected_completions"],x["work_in_progress"])
                self.assertAlmostEqual(x["accepted_completions"],old.get("assembly_starts",0)*r["parameters"]["assembly_yield"])
                previous[x["system_id"]]=x

    def test_stock_flow_commissioning_lag_and_replacement(self):
        for r in self.runs:
            previous={}
            for x in sorted(r["fleet"]["cells"],key=lambda x:(x["year"],x["cell_id"])):
                old=previous.get(x["cell_id"],{})
                self.assertAlmostEqual(x["prior_active"]+x["commissioned"]-x["retired"],x["active_stock"])
                self.assertAlmostEqual(x["commissioned"],old.get("shipped",0))
                self.assertAlmostEqual(x["commissioned"],x["replacement_commissioned"]+x["expansion_commissioned"])
                self.assertAlmostEqual(x["replacement_backlog"],old.get("replacement_backlog",0)+x["retired"]-x["replacement_commissioned"])
                self.assertGreaterEqual(x["replacement_backlog"],-1e-8)
                previous[x["cell_id"]]=x

    def test_shared_resources_not_spent_more_than_once(self):
        for r in self.runs:
            for y in r["fleet"]["years"]:
                for resource,used in y["resource_used"].items():
                    self.assertGreaterEqual(used,-1e-8)
                    self.assertLessEqual(used,y["resource_budgets"][resource]+1e-7,(r["preset"],y["year"],resource))
                self.assertLessEqual(y["support_existing_used"]+y["resource_used"]["support_hours_reserved"],r["parameters"]["support_budget_hours"]+1e-7)

    def test_waterfall_same_denominator_and_installed_site_limit(self):
        cells={c["cell_id"]:c for c in self.c["cells"]}
        for r in self.runs:
            for x in r["fleet"]["cells"]:
                vals=list(x["waterfall"].values())
                for before,after in zip(vals,vals[1:]):
                    self.assertLessEqual(after,before+1e-7)
                q=cells[x["cell_id"]]["annual_units_per_site"]
                self.assertLessEqual(x["accepted_baseline_units"],max(0,x["active_stock"]-.5*x["commissioned"])*x["support_fraction"]*q+1e-7)
                self.assertLessEqual(x["accepted_expansion_units"],max(0,x["active_stock"]-.5*x["commissioned"])*x["support_fraction"]*q*r["parameters"]["demand_expansion"]+1e-7)

    def test_labor_time_is_not_observed_payroll(self):
        zero=run_scenario({"labor_avoidability":0})
        self.assertEqual(zero["fleet"]["years"][-1]["active_stock"],0)
        for row in zero["fleet"]["cells"]:
            self.assertIsNone(row["economics"]["removed_payroll_usd"])
            self.assertEqual(row["economics"]["assumed_avoided_labor_cash_usd"],0)
            self.assertIsNone(row["economics"]["payback_years"])

    def test_joint_contrasts_and_no_additive_benefit_premium(self):
        for r in self.runs:
            for x in r["joint"]:
                self.assertAlmostEqual(x["cost_interaction"],x["C11"]-x["C10"]-x["C01"]+x["C00"])
                self.assertAlmostEqual(x["joint_saving"],x["C00"]-x["C11"])
        unchanged=run_scenario({"digital_efficiency":0,"coordination":0,"digital_cost_usd":0})
        # A fixed $600/site digital systems cost remains, by design, in both digital columns.
        for x in unchanged["joint"]:
            self.assertAlmostEqual(x["C11"]-x["C10"],600)
            self.assertAlmostEqual(x["C01"]-x["C00"],600)
            self.assertAlmostEqual(x["cost_interaction"],0)

    def test_expected_manufacturing_cost_includes_test_rejects_once(self):
        for yield_rate in (1,.5,.1):
            r=run_scenario({"assembly_yield":yield_rate})
            row=next(x for x in r["fleet"]["cells"] if x["system_id"]=="SYN-H")
            self.assertAlmostEqual(row["economics"]["manufacture_cost_per_accepted_robot_usd"],36000/yield_rate)
            self.assertAlmostEqual(r["commercial"]["cashflows"][0]["provider_cash_usd"],60000-36000/yield_rate)

    def test_commercial_internal_transfers_cancel(self):
        for arrangement in ("sale","lease","raas"):
            for price in (.5,1,2):
                r=run_scenario({"arrangement":arrangement,"price_multiplier":price})
                for case in r["commercial_by_cell"]:
                    for row in case["cashflows"]:
                        self.assertAlmostEqual(row["customer_cash_usd"]+row["provider_cash_usd"]+row["financier_cash_usd"],row["consolidated_incremental_cash_usd"])
                self.assertEqual([x["C11"] for x in r["joint"]],[x["C11"] for x in self.runs[0]["joint"]])
        low=run_scenario({"price_multiplier":.5})["commercial"]["cashflows"]
        high=run_scenario({"price_multiplier":2})["commercial"]["cashflows"]
        self.assertAlmostEqual(sum(x["consolidated_incremental_cash_usd"] for x in low),sum(x["consolidated_incremental_cash_usd"] for x in high))

    def test_newco_demand_conservation_and_cash(self):
        for r in self.runs:
            n=r["newco"]; cash=r["parameters"]["newco_funding_usd"]-n["upfront_usd"]; prior_revenue=0
            for row in n["rows"]:
                self.assertLessEqual(row["served_units"],row["capacity_units"]+1e-8)
                self.assertLessEqual(row["served_units"],row["demand_units"]+1e-8)
                self.assertAlmostEqual(row["share_transferred_units"]+row["incumbent_remaining_baseline_units"],row["existing_market_units"])
                self.assertAlmostEqual(row["served_units"],row["share_transferred_units"]+row["unmet_demand_served_units"]+row["expansion_units"])
                self.assertAlmostEqual(row["cash_receipts_usd"],prior_revenue)
                cash+=row["cashflow_usd"];self.assertAlmostEqual(cash,row["cash_balance_usd"])
                prior_revenue=row["revenue_usd"]
            self.assertGreaterEqual(n["funding_gap_usd"],0)
        prompt=run_scenario(preset="prompt_response")["newco"]
        delayed=run_scenario(preset="newco_raas")["newco"]
        self.assertGreater(prompt["peak_funding_required_usd"],delayed["peak_funding_required_usd"])

    def test_backcast_targets_and_lags(self):
        for r in self.runs:
            b=r["backcast"]
            if b["rows"]:
                self.assertAlmostEqual(b["rows"][-1]["retained_active"],b["target_active_stock"])
                for x in b["rows"]:
                    self.assertEqual(x["commission_year"]-x["latest_assembly_start_year"],2)
                    self.assertAlmostEqual(x["commissioned_required"],x["assembly_starts_required"]*r["parameters"]["assembly_yield"])
        self.assertEqual(run_scenario({"qualification_delay":10,"target_year":2})["backcast"]["status"],"infeasible_lead_time")

    def test_evidence_immutable_and_scenarios_reproducible(self):
        snapshot=load_accepted_packages(ROOT)
        paths=[ROOT/p["path"] for p in snapshot["packages"]]
        before={p:hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}
        r=run_scenario({"digital_efficiency":.5,"learning_transfer":.1})
        loaded=json.loads(json.dumps(r));again=run_scenario(loaded["parameters"],loaded["preset"])
        self.assertEqual(r,again)
        self.assertEqual(set(r["evidence_snapshot_hashes"]),{p["path"] for p in snapshot["packages"]})
        self.assertEqual(r["evidence_package_index"],snapshot["index"])
        self.assertEqual(before,{p:hashlib.sha256(p.read_bytes()).hexdigest() for p in paths})

    def test_invalid_unknown_and_null_inputs_rejected(self):
        for overrides in ({"capability":None},{"capability":float('nan')},{"capability":2},{"unknown":1},{"years":3.5},{"years":10**400},{"arrangement":"free"}):
            with self.assertRaises(ValueError):run_scenario(overrides)

    def test_empirical_totals_do_not_use_model_assumptions(self):
        summary=economic_atlas_summary()
        if summary["status"]=="missing_evidence":self.skipTest("Evidence package absent")
        self.assertFalse(summary["scenario_inputs_used"])
        self.assertTrue(all(summary["checks"].values()))
        self.assertIsNone(summary["physical_work_hours"])
        self.assertAlmostEqual(summary["market_employment"]["value"],128979.5)


if __name__=="__main__":unittest.main()
