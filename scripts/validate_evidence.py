#!/usr/bin/env python3
"""Validate evidence IDs/links across heterogeneous, independently authored packages."""
import json
import sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]


def walk(value,path="$ structure"):
    if isinstance(value,dict):
        yield path,value
        for k,v in value.items():
            yield from walk(v,f"{path}.{k}")
    elif isinstance(value,list):
        for i,v in enumerate(value):
            yield from walk(v,f"{path}[{i}]")


def validate():
    errors,warnings,records,packages=[],[],{},[]
    for f in sorted((ROOT/"data").glob("*_evidence.json")):
        try:
            data=json.loads(f.read_text())
        except (ValueError,UnicodeDecodeError) as exc:
            errors.append(f"{f.name}: {exc}");continue
        packages.append((f.name,data))
        if not isinstance(data,dict) or not isinstance(data.get("evidence"),list):
            errors.append(f"{f.name}: missing evidence[] array");continue
        for e in data["evidence"]:
            eid=e.get("evidence_id")
            if not eid:
                errors.append(f"{f.name}: evidence record lacks evidence_id");continue
            if eid in records:
                errors.append(f"Duplicate evidence_id {eid}")
            records[eid]=e
            if not e.get("claim"):
                warnings.append(f"{eid}: missing claim (may use an alternate title field)")
            if not (e.get("url") or e.get("source_url") or e.get("urls")):
                warnings.append(f"{eid}: no source URL field")
            if not (e.get("epistemic_status") or e.get("status")):
                warnings.append(f"{eid}: epistemic status not explicit")
    for name,data in packages:
        for path,obj in walk(data,name):
            for key in ("evidence_ids","source_evidence_ids","target_evidence_ids","evidence_refs"):
                refs=obj.get(key)
                if refs is None:
                    continue
                if not isinstance(refs,list):
                    warnings.append(f"{path}.{key}: reference field is not a list");continue
                for ref in refs:
                    if isinstance(ref,str) and ref not in records:
                        errors.append(f"{path}.{key}: unresolved {ref}")
    return {"status":"pass" if not errors else "failed","packages":len(packages),"evidence_records":len(records),"errors":errors,"warnings":warnings}


if __name__=="__main__":
    result=validate();print(json.dumps(result,indent=2));sys.exit(bool(result["errors"]))
