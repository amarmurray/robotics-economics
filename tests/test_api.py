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

    def test_support_expansion_http_replay_and_validation(self):
        def post(body):
            req=urllib.request.Request(self.base+'/api/support-expansion',data=json.dumps(body).encode(),headers={'Content-Type':'application/json'})
            with urllib.request.urlopen(req) as f:return json.load(f)
        with urllib.request.urlopen(self.base+'/api/support-expansion') as f:catalog=json.load(f)
        self.assertEqual(len(catalog['case_inputs']),16)
        r=post({'inputs':{'requested_growth':0}})['result']
        self.assertEqual(r['support_expansion']['summary']['funded_starts'],0)
        self.assertEqual(post({'saved_case':r})['result'],r)
        for body in ({'inputs':None},{'inputs':[]},{'inputs':{'requested_growth':True}},{'inputs':{},'saved_case':{}},{'saved_case':{}}):
            with self.assertRaises(urllib.error.HTTPError) as err:post(body)
            self.assertEqual(err.exception.code,400)

    def test_competitive_renewal_http_replay_and_validation(self):
        def post(body):
            req=urllib.request.Request(self.base+'/api/competitive-renewals',data=json.dumps(body).encode(),headers={'Content-Type':'application/json'})
            with urllib.request.urlopen(req) as f:return json.load(f)
        with urllib.request.urlopen(self.base+'/api/competitive-renewals') as f:
            catalog=json.load(f)
        self.assertEqual(len(catalog['case_inputs']),17)
        r=post({'inputs':{'months':8,'competition':{'term_months':6}}})['result']
        self.assertEqual(post({'saved_case':r})['result'],r)
        for body in ({'inputs':None},{'inputs':[]},{'inputs':{'months':True}},{'inputs':{},'saved_case':{}},{'saved_case':{}}):
            with self.assertRaises(urllib.error.HTTPError) as err:post(body)
            self.assertEqual(err.exception.code,400)

    def test_utility_inspection_http_replay_and_validation(self):
        def post(body):
            req=urllib.request.Request(self.base+'/api/utility-inspection',data=json.dumps(body).encode(),headers={'Content-Type':'application/json'})
            with urllib.request.urlopen(req) as f:return json.load(f)
        with urllib.request.urlopen(self.base+'/api/utility-inspection') as f:self.assertEqual(len(json.load(f)['cases']),18)
        r=post({'inputs':{'mobile_points':12,'staffing':'per_visit'}})['result']
        self.assertEqual(r['summary']['visits_completed'],0)
        self.assertEqual(post({'saved_case':r})['result'],r)
        for body in ({'inputs':[]},{'inputs':{'mobile_points':True}},{'inputs':{},'saved_case':{}},{'saved_case':{}},{'inputs':None}):
            with self.assertRaises(urllib.error.HTTPError) as err:post(body)
            self.assertEqual(err.exception.code,400)

    def test_automotive_workcell_http_replay_and_validation(self):
        def post(body):
            req=urllib.request.Request(self.base+'/api/automotive-workcell',data=json.dumps(body).encode(),headers={'Content-Type':'application/json'})
            with urllib.request.urlopen(req) as f:return json.load(f)
        with urllib.request.urlopen(self.base+'/api/automotive-workcell') as f:self.assertEqual(len(json.load(f)['cases']),18)
        r=post({'inputs':{'mixed_variants':True,'changeover_ticks':6}})['result']
        self.assertEqual(r['summary']['on_time_kits'],12);self.assertEqual(post({'saved_case':r})['result'],r)
        for body in ({'inputs':None},{'inputs':[]},{'inputs':{'pick_ticks':0}},{'inputs':{},'saved_case':{}},{'saved_case':{}}):
            with self.assertRaises(urllib.error.HTTPError) as err:post(body)
            self.assertEqual(err.exception.code,400)

    def test_learning_execution_http_replay_and_validation(self):
        def post(body):
            req=urllib.request.Request(self.base+'/api/learning-execution',data=json.dumps(body).encode(),headers={'Content-Type':'application/json'})
            with urllib.request.urlopen(req) as f:return json.load(f)
        with urllib.request.urlopen(self.base+'/api/learning-execution') as f:catalog=json.load(f)
        self.assertEqual(len(catalog['case_inputs']),16);self.assertEqual(len(catalog['summary']),16)
        r=post({'inputs':{'transfer_allowed':False}})['result'];self.assertEqual(r['summary']['qualified_units'],1)
        saved={'schema_version':r['schema_version'],'inputs':r['inputs'],'summary':{'invented':999}}
        self.assertEqual(post({'saved_case':saved})['result'],r)
        for body in ({'inputs':None},{'inputs':[]},{'inputs':{'cycles':True}},{'inputs':{},'saved_case':{}},{'saved_case':{}}):
            with self.assertRaises(urllib.error.HTTPError) as err:post(body)
            self.assertEqual(err.exception.code,400)

    def test_private_paths_and_invalid_values(self):
        for path in ("/.git/config","/../etc/passwd","/model/engine.py"):
            with self.assertRaises(urllib.error.HTTPError) as err:urllib.request.urlopen(self.base+path)
            self.assertEqual(err.exception.code,404)
        req=urllib.request.Request(self.base+"/api/run",data=b'{"overrides":{"capability":null}}',headers={"Content-Type":"application/json"})
        with self.assertRaises(urllib.error.HTTPError) as err:urllib.request.urlopen(req)
        self.assertEqual(err.exception.code,400)

    def test_financed_case_http_replay_and_invalid_saved_inputs(self):
        def post(body):
            req=urllib.request.Request(self.base+'/api/enterprise-finance',data=json.dumps(body).encode(),headers={'Content-Type':'application/json'})
            with urllib.request.urlopen(req) as f:return json.load(f)
        result=post({'inputs':{'maturity_month':3}})['result']
        self.assertEqual(result['finance']['first_debt_default_month']['entrant'],3)
        self.assertEqual(post({'saved_case':result})['result'],result)
        for body in ({'inputs':{'loan_cents':True}}, {'inputs':{},'saved_case':{}},
                     {'saved_case':{'schema_version':'monthly-deployment/0.4'}}, {'unexpected':{}}):
            with self.assertRaises(urllib.error.HTTPError) as err:post(body)
            self.assertEqual(err.exception.code,400)

    def test_calendar_case_replay_and_invalid_mapping(self):
        def post(body):
            req=urllib.request.Request(self.base+'/api/calendar-bridge',data=json.dumps(body).encode(),headers={'Content-Type':'application/json'})
            with urllib.request.urlopen(req) as f:return json.load(f)
        result=post({'inputs':{'finance_inputs':{'entrant_cash_cents':10000000,'loan_cents':0},'bridge_inputs':{'software_policy':'frozen_cohort'}}})['result']
        self.assertEqual(result['calendar_bridge']['months'][6]['calendar_year'],2027)
        self.assertEqual(post({'saved_case':result})['result'],result)
        for body in ({'inputs':{'bridge_inputs':[]}},{'inputs':{'human_only':1}},{'inputs':{},'saved_case':{}},
                     {'saved_case':{'schema_version':'monthly-deployment/0.5'}},{'inputs':{'unknown':True}}):
            with self.assertRaises(urllib.error.HTTPError) as err:post(body)
            self.assertEqual(err.exception.code,400)

    def test_monthly_architecture_replay_and_invalid_contract(self):
        def post(body):
            req=urllib.request.Request(self.base+'/api/monthly-architectures',data=json.dumps(body).encode(),headers={'Content-Type':'application/json'})
            with urllib.request.urlopen(req) as f:return json.load(f)
        result=post({'inputs':{'architecture_inputs':{'architecture_id':'model_led_operator'}}})['result']
        self.assertEqual(result['architecture_execution']['role_entities']['operator'],'arch:model_operator')
        self.assertEqual(post({'saved_case':result})['result'],result)
        for body in ({'inputs':{'architecture_inputs':[]}},{'inputs':{'bridge_inputs':[]}},{'inputs':{'unknown':0}},
                     {'saved_case':{}},{'inputs':{},'saved_case':{}}):
            with self.assertRaises(urllib.error.HTTPError) as err:post(body)
            self.assertEqual(err.exception.code,400)

    def test_conventional_coordination_replays_inputs_and_rejects_invalid_cases(self):
        with urllib.request.urlopen(self.base+'/api/conventional-coordination') as f:artifact=json.load(f)
        result=artifact['cases']['observed_robot_outage']
        def post(body):
            req=urllib.request.Request(self.base+'/api/conventional-coordination',data=json.dumps(body).encode(),headers={'Content-Type':'application/json'})
            with urllib.request.urlopen(req) as f:return json.load(f)
        self.assertEqual(post({'saved_case':result})['result'],result)
        self.assertEqual(post({'inputs':{k:result[k] for k in ('workload','controller')}})['result'],result)
        for body in ({'inputs':{}},{'saved_case':{}},{'inputs':{},'saved_case':{}},
                     {'inputs':{'workload':None,'controller':{}}},{'inputs':{'workload':{},'controller':[]}}):
            with self.assertRaises(urllib.error.HTTPError) as err:post(body)
            self.assertEqual(err.exception.code,400)

    def test_entry_transition_replay_and_invalid_contract(self):
        def post(body):
            req=urllib.request.Request(self.base+'/api/entry-transitions',data=json.dumps(body).encode(),headers={'Content-Type':'application/json'})
            with urllib.request.urlopen(req) as f:return json.load(f)
        result=post({'inputs':{'mode':'hybrid','disruption_months':1}})['result']
        self.assertEqual(post({'saved_case':result})['result'],result)
        for body in ({'inputs':[]},{'inputs':{'mode':'asset_purchase'}},{'saved_case':{}},{'inputs':{},'saved_case':{}}):
            with self.assertRaises(urllib.error.HTTPError) as err:post(body)
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
