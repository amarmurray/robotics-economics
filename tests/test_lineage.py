"""Calculation traces must reproduce displayed costs without calibration claims."""
import unittest
from model.engine import catalog, run_scenario
from model.lineage import joint_trace


class JointLineage(unittest.TestCase):
    def test_all_cells_match_engine_and_cost_components(self):
        for overrides in ({}, {"assembly_yield": .25, "digital_efficiency": .5,
                              "coordination": -.3, "onboard_configuration": "high_memory"}):
            result = run_scenario(overrides)
            for comparison in result["joint"]:
                trace = joint_trace(comparison["cell_id"], overrides)
                self.assertEqual(trace["comparison"], comparison)
                self.assertEqual(trace["scenario_hash"], result["scenario_hash"])
                self.assertEqual(trace["empirical_coefficient_sources"], [])
                for branch in trace["branches"]:
                    c = branch["calculation"]
                    operating = c["provider_operating_cost_usd"] if branch["robot"] else 0
                    self.assertAlmostEqual(c["resource_cost_usd"], c["customer_human_and_digital_cost_usd"] + operating + c["capital_consumption_usd_year"])
                    self.assertEqual(c["resource_cost_usd"], comparison[branch["branch"]])
                    self.assertIsNone(c["removed_payroll_usd"])

    def test_reference_horizon_and_invalid_inputs(self):
        cell = catalog()["cells"][0]["cell_id"]
        trace = joint_trace(cell, {"years": 3, "capability": .2, "capability_progress": .1, "learning_transfer": .15})
        self.assertEqual(trace["reference_year"], catalog()["base_year"] + 2)
        self.assertEqual(trace["capability"], .4)
        self.assertEqual(len(trace["functions"]), 4)
        for bad in (None, [], "not-a-cell"):
            with self.assertRaises(ValueError):
                joint_trace(bad)
        with self.assertRaises(ValueError):
            joint_trace(cell, {"capability": None})


if __name__ == "__main__":
    unittest.main()
