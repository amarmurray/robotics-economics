"""The API, selected-year trace and saved-file export share the same annual result."""
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import threading
import unittest
import urllib.error
import urllib.request
from http.server import ThreadingHTTPServer

from model.engine import ROOT, run_scenario
from model.lineage import joint_trace
from scripts.serve import Handler

PATHS = {"schema_version": "digital-annual-paths/0.1", "base_year": 2026,
         "epistemic_status": "synthetic_assumption", "digital_efficiency": [.15, .25, .35],
         "coordination": [.15, .1, -.1], "digital_cost_usd": [1500, 1200, 1800]}


class TrajectoryIntegration(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.server = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
        cls.thread = threading.Thread(target=cls.server.serve_forever, daemon=True)
        cls.thread.start()

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown(); cls.server.server_close(); cls.thread.join()

    def post(self, endpoint, payload):
        request = urllib.request.Request(f"http://127.0.0.1:{self.server.server_port}"+endpoint,
                                         data=json.dumps(payload).encode(), headers={"Content-Type": "application/json"})
        with urllib.request.urlopen(request) as response:
            return json.load(response)

    def test_every_selected_year_trace_and_http_replay(self):
        body = {"overrides": {"years": 3}, "digital_paths": PATHS}
        result = self.post("/api/run", body)
        self.assertEqual(result, run_scenario(body["overrides"], digital_paths=PATHS))
        for year in result["joint_by_year"]:
            for row in year["comparisons"]:
                trace = self.post("/api/joint-trace", {**body, "year": year["year"], "cell_id": row["cell_id"]})
                self.assertEqual(trace["comparison"], row)
                self.assertEqual(trace["reference_year"], year["year"])
                self.assertEqual(trace["scenario_hash"], result["scenario_hash"])
                self.assertEqual(trace["parameters"]["digital_efficiency"], PATHS["digital_efficiency"][year["period_index"]])
        self.assertEqual(result, self.post("/api/run", {"overrides": result["parameters"], "preset": result["preset"], "digital_paths": result["digital_paths"]}))

    def test_bad_path_or_trace_year_returns_400(self):
        body = {"overrides": {"years": 3}, "digital_paths": {**PATHS, "coordination": [0, 0, None]}}
        with self.assertRaises(urllib.error.HTTPError) as error:
            self.post("/api/run", body)
        self.assertEqual(error.exception.code, 400)
        for year in (2025, 2029, True, "2026", 2026.5):
            with self.assertRaises(urllib.error.HTTPError) as error:
                self.post("/api/joint-trace", {"overrides": {"years": 3}, "year": year, "cell_id": run_scenario()["joint"][0]["cell_id"]})
            self.assertEqual(error.exception.code, 400)

    def test_integer_valued_float_horizon_has_valid_default_trace(self):
        result = run_scenario({"years": 3.0}, digital_paths=PATHS)
        trace = joint_trace(result["joint"][0]["cell_id"], {"years": 3.0}, digital_paths=PATHS)
        self.assertEqual(trace["reference_year"], 2028)
        self.assertEqual(trace["comparison"], result["joint"][0])

    def test_architecture_http_trace_and_cli_replay_preserve_complete_inputs(self):
        architecture={"common":{"model_fee_usd_year":7000},"profiles":{"licensed_independent":{"adaptation_engineering_hours":17.5}}}
        body={"overrides":{"years":3},"digital_paths":PATHS,"architecture_overrides":architecture}
        parent=self.post('/api/run',body)
        scope={"cell_id":"CELL-M05-auto-assembly-US-2025","year":2027}
        case=self.post('/api/architectures',{**body,**scope})
        trace=self.post('/api/joint-trace',{**body,**scope})
        self.assertEqual(case['scenario_hash'],parent['scenario_hash'])
        self.assertEqual(trace['scenario_hash'],parent['scenario_hash'])
        self.assertEqual(case['architecture_parameters'],parent['architecture_parameters'])
        with tempfile.TemporaryDirectory() as directory:
            directory=Path(directory);saved=directory/'case.json';output=directory/'replay.json'
            saved.write_text(json.dumps(case))
            subprocess.run([sys.executable,str(ROOT/'scripts/export_architectures.py'),'--scenario',str(saved),'--output',str(output)],check=True,capture_output=True)
            self.assertEqual(json.loads(output.read_text()),case)
            base_saved=directory/'parent.json';base_saved.write_text(json.dumps(parent))
            subprocess.run([sys.executable,str(ROOT/'scripts/export_scenarios.py'),'--scenario',str(base_saved),'--output',str(directory/'base')],check=True,capture_output=True)
            self.assertEqual(json.loads((directory/'base/reference.json').read_text()),parent)
        with self.assertRaises(urllib.error.HTTPError) as error:
            self.post('/api/architectures',{**body,**scope,'architecture_overrides':{'common':{'model_fee_usd_year':None}}})
        self.assertEqual(error.exception.code,400)

    def test_cli_preserves_paths_and_legacy_fixed_horizon(self):
        with tempfile.TemporaryDirectory() as directory:
            directory = Path(directory)
            for name, result in [("annual", run_scenario({"years": 3}, digital_paths=PATHS)),
                                  ("scalar", run_scenario({"years": 4}))]:
                saved = directory/(name+".json")
                saved.write_text(json.dumps(result))
                target = directory/name
                subprocess.run([sys.executable, str(ROOT/"scripts/export_scenarios.py"), "--scenario", str(saved), "--output", str(target)], check=True, capture_output=True)
                self.assertEqual(json.loads((target/"reference.json").read_text()), result)
                self.assertEqual(len((target/"reference_joint_by_year.csv").read_text().splitlines()), 1+6*int(result["parameters"]["years"]))


if __name__ == "__main__":
    unittest.main()
