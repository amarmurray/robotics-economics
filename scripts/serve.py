#!/usr/bin/env python3
"""Local, read-only dashboard/API. Python standard library only."""
from __future__ import annotations

import argparse
import hashlib
import json
import mimetypes
import sys
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import unquote, urlparse

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from model.engine import BOUNDS, CHOICES, catalog, run_scenario
from model.evidence import economic_atlas_summary


def evidence_snapshot():
    packages = []
    for path in sorted((ROOT / "data").glob("*_evidence.json")):
        raw = path.read_bytes()
        try:
            payload = json.loads(raw)
        except (UnicodeDecodeError, json.JSONDecodeError) as exc:
            packages.append({"path":str(path.relative_to(ROOT)),"error":str(exc)})
            continue
        packages.append({"path":str(path.relative_to(ROOT)),"sha256":hashlib.sha256(raw).hexdigest(),"data":payload})
    return packages


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
            self.send(200,{"catalog":catalog(),"bounds":BOUNDS,"choices":CHOICES,"evidence_packages":evidence_snapshot(),"documents":docs,"observed_summary":economic_atlas_summary()})
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
        if urlparse(self.path).path != "/api/run":
            self.send(404,{"error":"Unknown endpoint"})
            return
        try:
            length = int(self.headers.get("Content-Length","0"))
            if length < 0 or length > 200000:
                raise ValueError("Request too large")
            request = json.loads(self.rfile.read(length))
            if not isinstance(request,dict) or set(request)-{"overrides","preset"}:
                raise ValueError("Expected preset and overrides")
            overrides = request.get("overrides",{})
            if not isinstance(overrides,dict):
                raise ValueError("overrides must be an object")
            self.send(200,run_scenario(overrides,request.get("preset","reference")))
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
