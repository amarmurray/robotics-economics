#!/usr/bin/env python3
"""Local, read-only dashboard/API. Python standard library only."""
from __future__ import annotations

import argparse
import json
import mimetypes
import sys
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import unquote, urlparse

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from model.engine import BOUNDS, CHOICES, catalog, run_scenario, run_architecture_comparison
from model.architectures import catalog as architecture_catalog
from model.monthly_commercial import commercial_artifact
from model.monthly_enterprise import enterprise_artifact, run_shared_case
from model.enterprise_finance import finance_artifact, run_financed_case, replay_financed_enterprise
from model.calendar_bridge import bridge_artifact, run_bridge_case, replay_bridge
from model.monthly_architectures import architecture_execution_artifact, run_architecture_case, replay_architecture_execution
from model.conventional_coordination import coordination_artifact, run_coordination_inputs, replay_coordination
from model.entry_transitions import entry_artifact, run_entry_case, replay_entry_transition
from model.utility_inspection import inspection_artifact, run_inspection_case, replay_inspection
from model.automotive_workcell import workcell_artifact, run_workcell_case, replay_workcell
from model.learning_execution import learning_catalog, run_learning_case, replay_learning
from model.competitive_renewals import competitive_catalog, run_competitive_case, replay_competitive_case
from model.evidence import economic_atlas_summary
from model.packages import load_accepted_packages, PackageError
from model.research_calculations import research_summary
from model.lineage import joint_trace
from model.physical_requirements import physical_requirements_summary
from model.frontier_models import frontier_model_summary


def evidence_snapshot():
    return load_accepted_packages(ROOT)


class Handler(BaseHTTPRequestHandler):
    def send(self, status, payload, kind="application/json; charset=utf-8"):
        body = payload if isinstance(payload, bytes) else json.dumps(payload,ensure_ascii=False,allow_nan=False).encode()
        self.send_response(status)
        self.send_header("Content-Type",kind)
        self.send_header("Content-Length",str(len(body)))
        self.send_header("Cache-Control","no-store")
        self.send_header("X-Content-Type-Options","nosniff")
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        path = unquote(urlparse(self.path).path)
        if path == "/api/catalog":
            docs = [str(p.relative_to(ROOT)) for p in sorted(ROOT.glob("research/*.md"))]
            docs += ["model/METHODS.md","REPRODUCE.md"]
            if (ROOT/"REPORT.md").exists():
                docs.insert(0,"REPORT.md")
            try:
                snapshot=evidence_snapshot()
                accepted={p["path"] for p in snapshot["packages"]}
                atlas=economic_atlas_summary() if "data/market_evidence.json" in accepted else {"status":"not_available","reason":"Market evidence package has not been explicitly accepted."}
                research=research_summary() if {"data/field_support_denominators.json","data/coordination_reproducibility.json"}<=accepted else {"status":"not_available","reason":"Required research packages have not been explicitly accepted."}
                physical=physical_requirements_summary() if "data/physical_requirements_crosswalk.json" in accepted else {"status":"not_available","reason":"Physical requirements package has not been explicitly accepted."}
                frontier=frontier_model_summary() if "data/frontier_model_economics.json" in accepted else {"status":"not_available","reason":"Frontier-model package has not been explicitly accepted."}
                self.send(200,{"catalog":catalog(),"architecture_catalog":architecture_catalog(),"bounds":BOUNDS,"choices":CHOICES,"evidence_packages":snapshot["packages"],
                    "evidence_package_index":snapshot["index"],"documents":docs,"observed_summary":atlas,"observed_research_summary":research,"observed_physical_requirements":physical,"observed_frontier_models":frontier})
            except (ValueError,KeyError,OSError) as exc:
                self.send(503,{"error":str(exc)})
            return
        if path == "/api/competitive-renewals":
            try:self.send(200, competitive_catalog())
            except (ValueError,KeyError,OSError) as exc:self.send(503,{"error":str(exc)})
            return
        if path == "/api/learning-execution":
            try:self.send(200, learning_catalog())
            except (ValueError,KeyError,OSError) as exc:self.send(400,{"error":str(exc)})
            return
        if path == "/api/automotive-workcell":
            try:
                self.send(200, workcell_artifact())
            except (ValueError, KeyError, OSError) as exc:
                self.send(503, {"error": str(exc)})
            return
        if path == "/api/utility-inspection":
            try:
                self.send(200, inspection_artifact())
            except (ValueError, KeyError, OSError) as exc:
                self.send(503, {"error": str(exc)})
            return
        if path == "/api/entry-transitions":
            try:
                self.send(200, entry_artifact())
            except (ValueError, KeyError, OSError) as exc:
                self.send(503, {"error": str(exc)})
            return
        if path == "/api/conventional-coordination":
            try:
                self.send(200, coordination_artifact())
            except (ValueError, KeyError, OSError) as exc:
                self.send(503, {"error": str(exc)})
            return
        if path == "/api/monthly-architectures":
            try:
                self.send(200, architecture_execution_artifact())
            except (ValueError, KeyError, OSError) as exc:
                self.send(503, {"error": str(exc)})
            return
        if path == "/api/calendar-bridge":
            try:
                self.send(200, bridge_artifact())
            except (ValueError, KeyError, OSError) as exc:
                self.send(503, {"error": str(exc)})
            return
        if path == "/api/enterprise-finance":
            try:
                self.send(200, finance_artifact())
            except (ValueError, KeyError, OSError) as exc:
                self.send(503, {"error": str(exc)})
            return
        if path == "/api/shared-enterprise":
            try:
                self.send(200, enterprise_artifact())
            except (ValueError, KeyError, OSError) as exc:
                self.send(503, {"error": str(exc)})
            return
        if path == "/api/monthly-commercial":
            try:
                self.send(200, commercial_artifact())
            except (ValueError, KeyError, OSError) as exc:
                self.send(503, {"error": str(exc)})
            return
        if path == "/api/health":
            self.send(200,{"status":"ok","model_version":catalog()["model_version"],"local_only":True})
            return
        if path == "/":
            path = "/dashboard/index.html"
        target = (ROOT/path.lstrip("/")).resolve()
        # Do not expose operational records, .git, or arbitrary workspace files.
        allowed = target.is_relative_to(ROOT) and target.suffix in {".html",".css",".js",".json",".md",".csv"}
        if allowed:
            rel = target.relative_to(ROOT)
            allowed = (len(rel.parts)>1 and rel.parts[0] in {"dashboard","model","data","research"}) or (len(rel.parts)==1 and target.suffix==".md")
        if not allowed or not target.is_file():
            self.send(404,{"error":"File not available"})
            return
        mime = mimetypes.guess_type(target.name)[0] or "text/plain"
        if target.suffix == ".md":
            mime = "text/plain; charset=utf-8"
        self.send(200,target.read_bytes(),mime)

    def do_POST(self):
        endpoint = urlparse(self.path).path
        if endpoint not in {"/api/run", "/api/joint-trace", "/api/architectures", "/api/shared-enterprise", "/api/enterprise-finance", "/api/calendar-bridge", "/api/monthly-architectures", "/api/conventional-coordination", "/api/entry-transitions", "/api/utility-inspection", "/api/automotive-workcell", "/api/learning-execution", "/api/competitive-renewals"}:
            self.send(404,{"error":"Unknown endpoint"})
            return
        try:
            length = int(self.headers.get("Content-Length","0"))
            if length < 0 or length > (8000000 if endpoint == "/api/competitive-renewals" else 2000000 if endpoint in {"/api/enterprise-finance","/api/calendar-bridge","/api/monthly-architectures","/api/entry-transitions","/api/automotive-workcell", "/api/learning-execution"} else 200000):
                raise ValueError("Request too large")
            request = json.loads(self.rfile.read(length))
            if endpoint == "/api/competitive-renewals":
                if not isinstance(request,dict) or set(request) not in ({"inputs"},{"saved_case"}):
                    raise ValueError("Expected exactly inputs or saved_case for competitive renewals")
                if "inputs" in request and not isinstance(request["inputs"],dict):
                    raise ValueError("Competitive renewal inputs must be an object")
                result=replay_competitive_case(request["saved_case"]) if "saved_case" in request else run_competitive_case(request["inputs"])
                self.send(200,{"result":result})
                return
            if endpoint == "/api/learning-execution":
                if not isinstance(request,dict) or set(request) not in ({"inputs"},{"saved_case"}):
                    raise ValueError("Expected exactly inputs or saved_case for learning execution")
                if "inputs" in request and not isinstance(request["inputs"],dict):
                    raise ValueError("Learning inputs must be an object")
                result=replay_learning(request["saved_case"]) if "saved_case" in request else run_learning_case(request["inputs"])
                self.send(200,{"result":result})
                return
            if endpoint == "/api/automotive-workcell":
                if not isinstance(request,dict) or len(request)!=1 or not ({"inputs","saved_case"}&set(request)):
                    raise ValueError("Expected exactly inputs or saved_case for workcell")
                if "inputs" in request and not isinstance(request["inputs"],dict):raise ValueError("Workcell inputs must be an object")
                result=replay_workcell(request["saved_case"]) if "saved_case" in request else run_workcell_case(request["inputs"])
                self.send(200,{"result":result})
                return
            if endpoint == "/api/utility-inspection":
                if not isinstance(request,dict) or len(request)!=1 or not ({"inputs","saved_case"}&set(request)):
                    raise ValueError("Expected exactly inputs or saved_case for inspection")
                if "inputs" in request and not isinstance(request["inputs"],dict):raise ValueError("Inspection inputs must be an object")
                result=replay_inspection(request["saved_case"]) if "saved_case" in request else run_inspection_case(request["inputs"])
                self.send(200,{"result":result})
                return
            if endpoint == "/api/entry-transitions":
                if not isinstance(request,dict) or len(request)!=1 or not ({"inputs","saved_case"}&set(request)):
                    raise ValueError("Expected exactly inputs or saved_case for entry transitions")
                if 'inputs' in request and not isinstance(request['inputs'],dict):raise ValueError('Entry inputs must be an object')
                result=replay_entry_transition(request['saved_case']) if 'saved_case' in request else run_entry_case(request['inputs'])
                self.send(200,{'result':result})
                return
            if endpoint == "/api/conventional-coordination":
                if not isinstance(request,dict) or len(request)!=1 or not ({"inputs","saved_case"}&set(request)):
                    raise ValueError("Expected exactly inputs or saved_case for conventional coordination")
                result=replay_coordination(request['saved_case']) if 'saved_case' in request else run_coordination_inputs(request['inputs'])
                self.send(200,{'result':result})
                return
            if endpoint == "/api/monthly-architectures":
                if not isinstance(request,dict) or len(request)!=1 or not ({"inputs","saved_case"}&set(request)):
                    raise ValueError("Expected exactly inputs or saved_case for monthly architectures")
                if 'saved_case' in request:
                    try:
                        replayed=replay_architecture_execution(request['saved_case'])
                    except KeyError as exc:
                        raise ValueError("Incomplete saved monthly architecture case") from exc
                    self.send(200,{'inputs':None,'result':replayed})
                else:
                    x=request['inputs']
                    if not isinstance(x,dict) or set(x)-{'architecture_inputs','bridge_inputs'}:
                        raise ValueError('Unknown monthly architecture shortcut input')
                    self.send(200,{'inputs':x,'result':run_architecture_case(**x)})
                return
            if endpoint == "/api/calendar-bridge":
                if not isinstance(request,dict) or len(request)!=1 or not ({"inputs","saved_case"}&set(request)):
                    raise ValueError("Expected exactly inputs or saved_case for calendar execution")
                if 'saved_case' in request:
                    try:
                        replayed=replay_bridge(request['saved_case'])
                    except KeyError as exc:
                        raise ValueError("Incomplete saved calendar case") from exc
                    self.send(200,{'inputs':None,'result':replayed})
                else:
                    x=request['inputs']
                    if not isinstance(x,dict) or set(x)-{'finance_inputs','bridge_inputs','human_only'}:
                        raise ValueError('Unknown calendar-execution shortcut input')
                    self.send(200,{'inputs':x,'result':run_bridge_case(**x)})
                return
            if endpoint == "/api/enterprise-finance":
                if not isinstance(request,dict) or len(request)!=1 or not ({"inputs","saved_case"}&set(request)):
                    raise ValueError("Expected exactly inputs or saved_case for financed execution")
                if 'saved_case' in request:
                    try:
                        replayed = replay_financed_enterprise(request['saved_case'])
                    except KeyError as exc:
                        raise ValueError("Incomplete saved financed case") from exc
                    self.send(200,{"inputs":None,"result":replayed})
                else:
                    if not isinstance(request['inputs'],dict):raise ValueError("inputs must be an object")
                    self.send(200,run_financed_case(request['inputs']))
                return
            if endpoint == "/api/shared-enterprise":
                if not isinstance(request, dict) or set(request)-{"inputs"}:
                    raise ValueError("Expected shared-enterprise inputs")
                inputs = request.get("inputs", {})
                if not isinstance(inputs, dict):
                    raise ValueError("inputs must be an object")
                self.send(200, run_shared_case(inputs))
                return
            allowed = {"overrides", "preset", "digital_paths", "architecture_overrides"}
            if endpoint in {"/api/joint-trace", "/api/architectures"}:
                allowed |= {"cell_id", "year"}
            if not isinstance(request,dict) or set(request)-allowed:
                raise ValueError("Expected preset and overrides")
            overrides = request.get("overrides",{})
            if not isinstance(overrides,dict):
                raise ValueError("overrides must be an object")
            if endpoint == "/api/joint-trace":
                self.send(200,joint_trace(request.get("cell_id"),overrides,request.get("preset","reference"),
                                         digital_paths=request.get("digital_paths"),year=request.get("year"),architecture_overrides=request.get("architecture_overrides")))
            elif endpoint == "/api/architectures":
                self.send(200,run_architecture_comparison(request.get("cell_id"),overrides,request.get("preset","reference"),
                    digital_paths=request.get("digital_paths"),year=request.get("year"),architecture_overrides=request.get("architecture_overrides")))
            else:
                self.send(200,run_scenario(overrides,request.get("preset","reference"),digital_paths=request.get("digital_paths"),architecture_overrides=request.get("architecture_overrides")))
        except (ValueError,TypeError,json.JSONDecodeError) as exc:
            self.send(400,{"error":str(exc)})


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--port",type=int,default=8765)
    args = parser.parse_args()
    server = ThreadingHTTPServer(("127.0.0.1",args.port),Handler)
    print(f"Local dashboard: http://127.0.0.1:{args.port} — Ctrl-C to stop",flush=True)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
