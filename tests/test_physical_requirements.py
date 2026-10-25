"""Source fidelity, missingness and population-safe crosswalk checks."""
import copy
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from model.physical_requirements import ROOT, ROWS, PACKAGE, build_package, observation, physical_requirements_summary
from scripts.extract_physical_requirements import extract, source_inputs


class PhysicalRequirements(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.raw = json.loads((ROOT/ROWS).read_text())
        cls.package = json.loads((ROOT/PACKAGE).read_text())

    def test_complete_source_reextraction_matches_saved_rows(self):
        self.assertEqual(extract(), self.raw)
        self.assertEqual(len(self.raw["ors_rows"]), 25)
        self.assertEqual(len(self.raw["oews_rows"]), 5)
        self.assertEqual(self.raw["ors_data_row_count"], 73710)
        self.assertEqual(self.raw["oews_data_row_count"], 1401)

    def test_package_is_reproducible_and_synthetic_controls_are_absent(self):
        self.assertEqual(build_package(), self.package)
        summary = physical_requirements_summary()
        self.assertFalse(summary["scenario_inputs_used"])
        self.assertEqual(summary["exact_code_matches"], 3)
        for occupation in summary["occupations"]:
            self.assertIsNone(occupation["physical_work_hours"])
            self.assertIsNone(occupation["robot_addressable_jobs"])
            self.assertFalse(occupation["population_equivalent"])

    def test_exact_employment_codes_and_duplicate_aggregate_are_not_substituted(self):
        rows = {r["soc_2018"]: r for r in self.package["occupational_crosswalk"]}
        self.assertEqual(rows["37-2011"]["employment"]["value"], 2209760)
        self.assertEqual(rows["47-2061"]["employment"]["value"], 1096780)
        self.assertEqual(rows["53-7062"]["employment"]["value"], 2950280)
        self.assertIsNone(rows["51-2092"]["employment"]["value"])
        aggregates = [r for r in self.raw["oews_rows"] if r["cells"]["OCC_CODE"] == "51-2090"]
        self.assertEqual({r["cells"]["O_GROUP"] for r in aggregates}, {"broad", "detailed"})
        self.assertEqual([r["cells"]["TOT_EMP"] for r in aggregates], [1405030, 1405030])

    def test_missing_team_assembler_requirements_stay_unpublished(self):
        missing = [r for r in self.package["physical_requirements"] if r["source_row"] is None]
        self.assertEqual({(r["soc_2018"], r["metric"]) for r in missing},
                         {("51-2092", "sitting_mean"), ("51-2092", "reaching_overhead"), ("51-2092", "reaching_at_below_shoulder")})
        self.assertTrue(all(r["estimate"]["value"] is None and r["estimate"]["measurement_status"] == "not_published" for r in missing))

    def test_range_bounds_are_not_points_and_se_dash_footnotes_differ(self):
        rows = {r["requirement_id"]: r for r in self.package["physical_requirements"]}
        standing = rows["372011-01003"]
        self.assertEqual(standing["estimate"]["value"], 97.7)
        self.assertIsNone(standing["standard_error"]["value"])
        self.assertEqual((standing["standard_error"]["comparison"], standing["standard_error"]["bound"]), ("<", .5))
        gross = rows["372011-00771"]
        self.assertIsNone(gross["estimate"]["value"])
        self.assertEqual((gross["estimate"]["comparison"], gross["estimate"]["bound"]), (">", 99.5))
        self.assertEqual(gross["standard_error"]["measurement_status"], "not_available")
        self.assertNotIn("bound", gross["standard_error"])

    def test_published_sitting_and_standing_share_one_workday_only(self):
        rows = {(r["soc_2018"],r["metric"]):r for r in self.package["physical_requirements"]}
        for soc in ("37-2011", "47-2061", "53-7062"):
            a, b = (rows[soc,k]["estimate"] for k in ("sitting_mean", "standing_mean"))
            self.assertAlmostEqual(a["value"]+b["value"], 100)
            self.assertEqual(a["unit"], "percent of workday (mean)")
            self.assertEqual(rows[soc,"gross_manipulation"]["estimate"]["unit"], "percent of workers")

    def test_duplicate_detailed_match_is_rejected(self):
        altered = copy.deepcopy(self.raw)
        altered["oews_rows"].append(altered["oews_rows"][0])
        original = Path.read_text
        def read(path, *args, **kwargs):
            return json.dumps(altered) if path == ROOT/ROWS else original(path, *args, **kwargs)
        with patch.object(Path, "read_text", read), self.assertRaisesRegex(ValueError, "Ambiguous"):
            build_package()

    def test_source_hash_change_is_rejected_and_zero_is_not_missing(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            dest = root/"data/sources/physical_requirements"
            dest.mkdir(parents=True)
            manifest = json.loads((ROOT/"data/sources/physical_requirements/source_manifest.json").read_text())
            manifest["sources"] = manifest["sources"][:1]
            (dest/"source_manifest.json").write_text(json.dumps(manifest))
            (root/manifest["sources"][0]["path"]).write_bytes(b"changed source")
            with self.assertRaisesRegex(ValueError, "hash mismatch"):
                source_inputs(root)
        value = observation("0", "percent", "workers", "test population", "test period")
        self.assertEqual(value["value"], 0)
        self.assertEqual(value["measurement_status"], "published_point")


if __name__ == "__main__":
    unittest.main()
