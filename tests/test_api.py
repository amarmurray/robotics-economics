"""Local HTTP behavior and saved-scenario input validation."""
import json
import threading
import unittest
import urllib.error
import urllib.request
from http.server import ThreadingHTTPServer
from scripts.serve import Handler


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
        with urllib.request.urlopen(self.base+"/") as f:self.assertIn(b"app.js",f.read())
        def run(body):
            req=urllib.request.Request(self.base+"/api/run",data=json.dumps(body).encode(),headers={"Content-Type":"application/json"})
            with urllib.request.urlopen(req) as f:return json.load(f)
        default=run({"preset":"reference"})
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


if __name__=="__main__":unittest.main()
