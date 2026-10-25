"""Local HTTP behavior and saved-scenario input validation."""
import json
import threading
import unittest
import urllib.error
import urllib.request
from unittest.mock import patch
from http.server import ThreadingHTTPServer
from scripts.serve import Handler
from model.packages import load_accepted_packages


class LocalAPI(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.server=ThreadingHTTPServer(("127.0.0.1",0),Handler)
        cls.thread=threading.Thread(target=cls.server.serve_forever,daemon=True);cls.thread.start()
        cls.base=f"http://127.0.0.1:{cls.server.server_port}"

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown();cls.server.server_close();cls.thread.join()

    def test_local_launch_catalog_and_recalculation(self):
        with urllib.request.urlopen(self.base+"/api/catalog") as f:data=json.load(f)
        self.assertEqual(len(data["catalog"]["cells"]),6)
        self.assertEqual(data["observed_physical_requirements"]["exact_code_matches"],3)
        self.assertFalse(data["observed_physical_requirements"]["scenario_inputs_used"])
        self.assertEqual(data["observed_frontier_models"]["transaction"]["cash_consideration"],9)
        with urllib.request.urlopen(self.base+"/") as f:self.assertIn(b"app.js",f.read())
        def run(body):
            req=urllib.request.Request(self.base+"/api/run",data=json.dumps(body).encode(),headers={"Content-Type":"application/json"})
            with urllib.request.urlopen(req) as f:return json.load(f)
        default=run({"preset":"reference"})
        self.assertEqual(set(default["evidence_snapshot_hashes"]),{p["path"] for p in data["evidence_packages"]})
        self.assertEqual(default["evidence_package_index"],data["evidence_package_index"])
        changed=run({"overrides":{"digital_efficiency":.5}})
        self.assertNotEqual(default["joint"][0]["C01"],changed["joint"][0]["C01"])
        self.assertNotEqual(default["scenario_hash"],changed["scenario_hash"])
        self.assertEqual(run({"preset":changed["preset"],"overrides":changed["parameters"]}),changed)

    def test_private_paths_and_invalid_values(self):
        for path in ("/.git/config","/../etc/passwd","/model/engine.py"):
            with self.assertRaises(urllib.error.HTTPError) as err:urllib.request.urlopen(self.base+path)
            self.assertEqual(err.exception.code,404)
        req=urllib.request.Request(self.base+"/api/run",data=b'{"overrides":{"capability":null}}',headers={"Content-Type":"application/json"})
        with self.assertRaises(urllib.error.HTTPError) as err:urllib.request.urlopen(req)
        self.assertEqual(err.exception.code,400)

    def test_unaccepted_observed_sources_cannot_leak_through_catalog(self):
        snapshot=load_accepted_packages()
        snapshot["packages"]=[p for p in snapshot["packages"] if p["package_id"]=="capability"]
        with patch("scripts.serve.evidence_snapshot",return_value=snapshot),patch("scripts.serve.economic_atlas_summary") as atlas,patch("scripts.serve.research_summary") as research:
            with urllib.request.urlopen(self.base+"/api/catalog") as f:data=json.load(f)
            self.assertEqual(data["observed_summary"]["status"],"not_available")
            self.assertEqual(data["observed_research_summary"]["status"],"not_available")
            self.assertEqual(data["observed_physical_requirements"]["status"],"not_available")
            self.assertEqual(data["observed_frontier_models"]["status"],"not_available")
            atlas.assert_not_called();research.assert_not_called()


if __name__=="__main__":unittest.main()
