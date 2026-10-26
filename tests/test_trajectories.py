"""Annual paths: frozen scalar compatibility, economic witnesses and failure boundaries."""
import copy
import hashlib
import json
from pathlib import Path
import unittest
from unittest.mock import patch

from model import engine
from model.trajectories import CHANNELS, SCHEMA, run_trajectory


def paths(**channels):
    return {"schema_version": SCHEMA, "base_year": 2026,
            "epistemic_status": "synthetic_assumption", **channels}


def numeric_fields(value, path=""):
    if isinstance(value, bool):
        return []
    if isinstance(value, (int, float)):
        return [(path, value)]
    if isinstance(value, dict):
        return [x for key, item in sorted(value.items()) for x in numeric_fields(item, path + "/" + key)]
    if isinstance(value, list):
        return [x for i, item in enumerate(value) for x in numeric_fields(item, path + "/" + str(i))]
    return []


def legacy_projection(result, sections):
    result = copy.deepcopy({key: result[key] for key in sections})
    for row in result["fleet"]["cells"]:
        for key in (*CHANNELS, "exogenous_capability"):
            row.pop(key)
    return result


def toy_catalog(price=10000):
    c = engine.catalog()
    cell = c["cells"][0]
    cell.update(annual_units_per_site=1000, human_hours_per_unit=1,
                wage_usd_hour=10, robot_units_per_hour=.3, capability_threshold=.5)
    c["cells"] = [cell]
    system = next(s for s in c["systems"] if s["system_id"] == cell["system_id"])
    system.update(price_usd=price, manufacture_cost_usd=price,
                  maintenance_usd_year=0, maintenance_hours_year=0, power_kw=0)
    return c


TOY = {"years": 3, "capability": 1, "capability_progress": 0, "learning_transfer": 0,
       "uptime": 1, "intervention_minutes": 0, "integration_hours": 0, "assembly_yield": 1,
       "retirement_years": 5, "digital_efficiency": .2, "coordination": 0,
       "digital_cost_usd": 0, "labor_avoidability": 1, "demand_expansion": 0}


class AnnualPaths(unittest.TestCase):
    def test_every_legacy_numeric_field_matches_frozen_0_1_1(self):
        oracle = json.loads((Path(__file__).parent / "fixtures/annual_scalar_v0_1_1.json").read_text())
        count = 0
        for name, expected in oracle["cases"].items():
            preset, configuration = name.split("/")
            scalar = engine.run_scenario({"onboard_configuration": configuration}, preset)
            p = scalar["parameters"]
            flat = paths(**{key: [p[key]] * int(p["years"]) for key in CHANNELS})
            trajectory = run_trajectory(flat, p, preset)
            for result in (scalar, trajectory):
                values = numeric_fields(legacy_projection(result, oracle["sections"]))
                digest = hashlib.sha256(json.dumps(values, separators=(",", ":"), allow_nan=False).encode()).hexdigest()
                self.assertEqual(len(values), expected["numeric_fields"], name)
                self.assertEqual(digest, expected["sha256"], name)
            self.assertEqual(scalar["scenario_hash"], trajectory["scenario_hash"])
            count += expected["numeric_fields"]
        self.assertEqual(count, 69315)

    def test_channel_precedence_and_exact_nonmonotone_levels(self):
        supplied = paths(coordination=[.2, -.4, .2], digital_cost_usd=[500, 2000, 500])
        r = run_trajectory(supplied, {"years": 3, "coordination": .6, "digital_efficiency": .3})
        self.assertEqual(r["digital_paths"], supplied)
        self.assertEqual(r["resolved_digital_paths"]["digital_efficiency"], [.3] * 3)
        self.assertEqual(r["resolved_digital_paths"]["coordination"], [.2, -.4, .2])
        for row in r["fleet"]["cells"]:
            for key in CHANNELS:
                self.assertEqual(row[key], r["resolved_digital_paths"][key][row["period_index"]])
        self.assertEqual(r["joint"], r["joint_by_year"][-1]["comparisons"])

    def test_invalid_last_period_rejected_before_fleet_calculation(self):
        invalid = [[], {}, paths(coordination=[0, 0]), paths(coordination=None),
                   paths(coordination=[0, 0, True]), paths(coordination=[0, 0, None]),
                   paths(coordination=[0, 0, float("nan")]), paths(coordination=[0, 0, 10**400]), paths(coordination=[0, 0, float("inf")]),
                   paths(coordination=[0, 0, -.401]), paths(digital_efficiency=[0, 0, .601]),
                   paths(digital_cost_usd=[0, 0, -1]), paths(unknown=[0, 0, 0]),
                   {**paths(), "base_year": 2027}, {**paths(), "base_year": True},
                   {**paths(), "schema_version": "future"}, {**paths(), "epistemic_status": "observed"}]
        with patch("model.engine.fleet_model") as fleet:
            for value in invalid:
                with self.subTest(value=value), self.assertRaises(ValueError):
                    run_trajectory(value, {"years": 3})
            fleet.assert_not_called()

    def test_overlap_harm_and_complementarity_through_path_entrypoint(self):
        c = toy_catalog()
        with patch("model.engine.catalog", return_value=c):
            r = run_trajectory(paths(coordination=[0, -.4, .6], digital_cost_usd=[0, 1000, 0]), TOY)
        rows = [y["comparisons"][0] for y in r["joint_by_year"]]
        for row in rows:
            self.assertEqual((row["C00"], row["C01"], row["C10"]), (10000, 8600, 6000))
            self.assertAlmostEqual(row["joint_saving"], (row["C00"]-row["C01"])+(row["C00"]-row["C10"])-row["cost_interaction"])
        self.assertAlmostEqual(rows[0]["C11"], 5800)
        self.assertAlmostEqual(rows[0]["cost_interaction"], 1200)
        self.assertAlmostEqual(rows[1]["C11"], 8720)
        self.assertAlmostEqual(rows[1]["robotics_saving_on_digital_baseline"], -120)
        self.assertAlmostEqual(rows[2]["C11"], 2920)
        self.assertAlmostEqual(rows[2]["cost_interaction"], -1680)

    def test_cost_only_changes_price_and_cost_not_physical_productivity(self):
        c = toy_catalog()
        with patch("model.engine.catalog", return_value=c):
            r = run_trajectory(paths(digital_cost_usd=[2000, 500, 500]), TOY)
        first, second = r["joint_by_year"][:2]
        self.assertEqual(first["capability"], second["capability"])
        self.assertAlmostEqual(first["comparisons"][0]["C11"]-second["comparisons"][0]["C11"], 1500)
        a, b = r["fleet"]["cells"][:2]
        self.assertEqual(a["economics"]["robot_accepted_units"], 600)
        self.assertEqual(b["economics"]["robot_accepted_units"], 600)
        self.assertEqual(a["economics"]["retained_human_hours"], b["economics"]["retained_human_hours"])
        gain = b["economics"]["annual_customer_cash_gain_before_capex_usd"]-a["economics"]["annual_customer_cash_gain_before_capex_usd"]
        margins = [x["economics"]["provider_recurring_receipts_usd"]-x["economics"]["provider_operating_cost_usd"] for x in (a,b)]
        self.assertAlmostEqual(gain, 1725)
        self.assertAlmostEqual(margins[1]-margins[0], -225)

    def test_moving_comparator_closes_admission_without_erasing_stock(self):
        c = toy_catalog(15000)
        with patch("model.engine.catalog", return_value=c):
            r = run_trajectory(paths(digital_efficiency=[0, 0, 0, .6]), {**TOY, "years": 4})
        before, after = r["fleet"]["cells"][2:4]
        self.assertEqual(sum(x["economic"] for x in before["sites"]), 12)
        self.assertEqual(sum(x["ready"] for x in before["sites"]), 10)
        self.assertEqual(sum(x["technical"] for x in after["sites"]), 12)
        self.assertEqual(sum(x["economic"] for x in after["sites"]), 0)
        self.assertGreater(after["active_stock"], 0)
        self.assertEqual(after["active_stock"], before["active_stock"]+after["commissioned"]-after["retired"])
        self.assertEqual(after["accepted_baseline_units"], 0)
        self.assertEqual(after["shipped"], 0)
        self.assertTrue(all(row["assembly_starts"] == 0 for row in r["fleet"]["production"] if row["year"] == 2029))
        self.assertIn("acquisition/payback", r["reference_scopes"]["output_gate"])

    def test_existing_tote_anchor_reverses_economics_at_2030(self):
        base = engine.run_scenario({"years": 5})
        moving = run_trajectory(paths(digital_efficiency=[.15]*4+[.35]), {"years": 5})
        def cell(r):
            return next(x for x in r["fleet"]["cells"] if x["cell_id"] == "CELL-M08-3pl-tote-US-2025" and x["year"] == 2030)
        a, b = cell(base), cell(moving)
        self.assertAlmostEqual(a["economics"]["customer_savings_usd"], 6316.371428571431)
        self.assertAlmostEqual(b["economics"]["customer_savings_usd"], -922.7142857142899)
        self.assertEqual(sum(x["economic"] for x in b["sites"]), 0)
        self.assertEqual(a["capability"], b["capability"])

    def test_zero_capability_not_created_by_coordination_or_cheap_service(self):
        r = run_trajectory(paths(coordination=[0, .3, .6], digital_cost_usd=[2000, 1000, 0]),
                           {"years": 3, "capability": 0, "capability_progress": 0, "learning_transfer": 0})
        self.assertTrue(all(row["accepted_baseline_units"] == 0 and row["capability"] == 0 for row in r["fleet"]["cells"]))

    def test_cost_change_leaves_output_and_exposure_when_stock_path_is_fixed(self):
        c = toy_catalog()
        with patch("model.engine.catalog", return_value=c):
            flat = run_trajectory(paths(digital_cost_usd=[1000]*6), {**TOY, "years": 6})
            cheaper = run_trajectory(paths(digital_cost_usd=[1000]*3+[500]*3), {**TOY, "years": 6})
        for a, b in zip(flat["fleet"]["cells"], cheaper["fleet"]["cells"]):
            for key in ("active_stock", "shipped", "commissioned", "accepted_baseline_units", "capability", "released_human_hours"):
                self.assertEqual(a[key], b[key])
        for a, b in zip(flat["fleet"]["years"], cheaper["fleet"]["years"]):
            self.assertEqual(a["cumulative_exposure_robot_hours"], b["cumulative_exposure_robot_hours"])

    def test_saved_paths_replay_and_legacy_reference_scopes(self):
        r = run_trajectory(paths(digital_efficiency=[.3, .2, .4]), {"years": 3})
        saved = json.loads(json.dumps(r))
        self.assertEqual(r, engine.run_scenario(saved["parameters"], saved["preset"], saved["digital_paths"]))
        initial = engine.run_scenario({"years": 3, "digital_efficiency": .3})
        self.assertEqual(r["commercial_by_cell"], initial["commercial_by_cell"])
        self.assertEqual(r["newco"], initial["newco"])
        self.assertEqual(r["backcast"], initial["backcast"])

    def test_numerical_helper_source_enters_identity(self):
        original = Path.read_bytes
        def changed(path):
            data = original(path)
            return data+b"\n# changed resolver source\n" if path.name == "trajectories.py" else data
        before = engine.run_scenario()
        with patch.object(Path, "read_bytes", changed):
            after = engine.run_scenario()
        self.assertNotEqual(before["scenario_hash"], after["scenario_hash"])
        self.assertEqual(before["fleet"], after["fleet"])
        self.assertEqual(set(before["model_source_hashes"]), {"model/engine.py", "model/trajectories.py", "model/architectures.py"})


if __name__ == "__main__":
    unittest.main()
