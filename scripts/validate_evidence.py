#!/usr/bin/env python3
"""Validate only explicitly accepted evidence, preserving heterogeneous records.

Aliases and null/inheritance rules are documented in model/PACKAGE_VALIDATION.md.
Validation never fills, rewrites, repairs or numerically calibrates source data.
"""
from __future__ import annotations

import datetime as dt
import json
import math
import re
import sys
from pathlib import Path
from urllib.parse import urlparse

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from model.packages import load_accepted_packages, PackageError


CLAIM_FIELDS={
    "claim":("claim","precise_claim"),
    "publisher":("publisher","source_publisher"),
    "url":("url","source_url","urls"),
    "status":("epistemic_status","evidence_status","status"),
    "source_class":("source_class","source_type"),
    "locator":("locator","source_locator","document_locator"),
    "publication_date":("publication_date","published_at","publication_period"),
    "observation_period":("observation_period","observation_date","observed_at"),
    "retrieved_at":("retrieved_at","retrieval_date","retrieved_date"),
}
QUANTITY_FIELDS={
    "unit":("unit","units"),
    "denominator":("denominator",),
    "population":("population","applicable_population"),
    "period":("period","observation_period","observation_date"),
    "status":("measurement_status","epistemic_status","evidence_status","status"),
}
MISSINGNESS_CONTAINERS=("missingness","missingness_reasons","missing_reasons")


def walk(value,path="$",ancestors=()):
    if isinstance(value,dict):
        yield path,value,ancestors
        for key,item in value.items():
            yield from walk(item,f"{path}.{key}",ancestors+(value,))
    elif isinstance(value,list):
        for i,item in enumerate(value):
            yield from walk(item,f"{path}[{i}]",ancestors)


def present(obj,aliases):
    for key in aliases:
        if key in obj:return key,obj[key]
    return None,None


def reason_for(obj,key,aliases=()):
    """A shared reason applies only when exactly one object field is null."""
    names=tuple(dict.fromkeys((key,)+tuple(aliases)))
    for name in names:
        for suffix in ("_missing_reason","_missingness_reason"):
            value=obj.get(name+suffix)
            if isinstance(value,str) and value.strip():return value
        for container in MISSINGNESS_CONTAINERS:
            value=obj.get(container)
            if isinstance(value,dict) and isinstance(value.get(name),str) and value[name].strip():return value[name]
    null_keys=[k for k,v in obj.items() if v is None and not k.endswith(("_missing_reason","_missingness_reason"))]
    if len(null_keys)==1 and null_keys[0] in names:
        for reason_key in ("missingness_reason","missing_reason","reason"):
            value=obj.get(reason_key)
            if isinstance(value,str) and value.strip():return value
    return None


def validate_text_field(obj,canonical,aliases,path,errors,nullable=True):
    key,value=present(obj,aliases)
    if key is None:
        errors.append(f"{path}.{canonical}: required field absent; use a documented alias or explicit null with reason")
        return None,None
    if value is None:
        if not nullable or not reason_for(obj,key,(canonical,)+aliases):
            errors.append(f"{path}.{key}: null requires an explicit field-specific missingness reason")
        return key,value
    if canonical=="denominator" and isinstance(value,(int,float)) and not isinstance(value,bool):
        if not math.isfinite(value) or value<=0:errors.append(f"{path}.{key}: numeric population denominator must be finite and positive")
        return key,value
    if not isinstance(value,str) or not value.strip():errors.append(f"{path}.{key}: expected a nonempty string or explicit null with reason")
    return key,value


def date_valid(value):
    if not isinstance(value,str):return False
    try:
        if re.fullmatch(r"\d{4}",value):return 1<=int(value)<=9999
        if re.fullmatch(r"\d{4}-\d{2}",value):
            dt.date.fromisoformat(value+"-01");return True
        if not re.fullmatch(r"\d{4}-\d{2}-\d{2}(?:[T ]\d{2}:\d{2}(?::\d{2}(?:\.\d+)?)?(?:Z|[+-]\d{2}:\d{2})?)?",value):return False
        dt.datetime.fromisoformat(value.replace("Z","+00:00"));return True
    except ValueError:return False


def validate_claim(record,path,errors):
    if not isinstance(record,dict):
        errors.append(f"{path}: evidence record must be an object");return
    eid=record.get("evidence_id")
    if not isinstance(eid,str) or not eid.strip():errors.append(f"{path}.evidence_id: required nonempty stable ID")
    for canonical,aliases in CLAIM_FIELDS.items():
        if canonical=="url":
            key,value=present(record,aliases)
            if key is None:errors.append(f"{path}.url: required source URL absent")
            elif value is None:
                if not reason_for(record,key,(canonical,)+aliases):errors.append(f"{path}.{key}: null source URL requires explicit missingness reason")
            else:
                values=value if isinstance(value,list) and key=="urls" else [value]
                if not values:errors.append(f"{path}.{key}: source URL list is empty")
                for url in values:
                    try:
                        parsed=urlparse(url) if isinstance(url,str) else None
                        valid=parsed is not None and parsed.scheme in ("http","https") and bool(parsed.hostname) and not any(c.isspace() for c in url)
                        if parsed is not None:parsed.port  # Validate numeric port syntax/range.
                    except ValueError:valid=False
                    if not valid:errors.append(f"{path}.{key}: expected an absolute http(s) source URL")
            continue
        key,value=validate_text_field(record,canonical,aliases,path,errors)
        if canonical in ("publication_date","retrieved_at") and value is not None and not date_valid(value):errors.append(f"{path}.{key}: expected an ISO date/timestamp (year or month precision allowed), or null with reason")


def validate_quantity(obj,path,ancestors,errors,counts):
    if "value" not in obj:return
    value=obj["value"]
    if value is None:
        counts["null_quantity_markers"]+=1
        if not reason_for(obj,"value"):errors.append(f"{path}.value: null quantity requires explicit missingness reason")
        # Missing measurements do not become quantities through invented metadata.
        for canonical,aliases in QUANTITY_FIELDS.items():
            if any(k in obj for k in aliases):validate_text_field(obj,canonical,aliases,path,errors)
        return
    counts["reported_quantities"]+=1
    if isinstance(value,bool) or not isinstance(value,(int,float)) or not math.isfinite(value):errors.append(f"{path}.value: expected a finite numeric value or explicit null")
    for canonical,aliases in QUANTITY_FIELDS.items():
        source=obj
        if canonical in ("population","period","status") and not any(k in obj for k in aliases):
            source=next((a for a in reversed(ancestors) if any(k in a for k in aliases)),obj)
            if source is not obj:counts["inherited_quantity_context_fields"]+=1
        validate_text_field(source,canonical,aliases,path,errors)


def reference_values(key,value,path,errors):
    if key=="external_evidence_registry" and isinstance(value,dict):
        for eid,declared in value.items():
            if not isinstance(declared,str) or not declared.strip():errors.append(f"{path}.{eid}: registry mapping requires a nonempty package path")
        return list(value)
    if not isinstance(value,list):
        errors.append(f"{path}: evidence references must be a list; unknown references use [] with an explanatory record field")
        return []
    result=[]
    for i,ref in enumerate(value):
        if key=="external_evidence_registry":
            if not isinstance(ref,dict) or not isinstance(ref.get("evidence_id"),str):
                errors.append(f"{path}[{i}]: registry list entries require evidence_id objects");continue
            if ref["evidence_id"] in result:errors.append(f"{path}[{i}]: duplicate external registry evidence ID {ref['evidence_id']}")
            if "path" in ref and (not isinstance(ref["path"],str) or not ref["path"].strip()):errors.append(f"{path}[{i}].path: supplied package path must be a nonempty string")
        if isinstance(ref,str) and ref.strip():result.append(ref)
        elif isinstance(ref,dict) and isinstance(ref.get("evidence_id"),str):result.append(ref["evidence_id"])
        else:errors.append(f"{path}[{i}]: expected evidence ID string or object with evidence_id")
    return result


def validate_snapshot(snapshot):
    errors,warnings,records=[],[],{}
    counts={"reported_quantities":0,"null_quantity_markers":0,"inherited_quantity_context_fields":0}
    packages=snapshot["packages"]
    for package in packages:
        path,data=package["path"],package["data"]
        for i,record in enumerate(data["evidence"]):
            location=f"{path}.evidence[{i}]"
            validate_claim(record,location,errors)
            if not isinstance(record,dict):continue
            eid=record.get("evidence_id")
            if isinstance(eid,str) and eid:
                if eid in records:errors.append(f"{location}: duplicate evidence_id {eid}")
                records[eid]=path
    for package in packages:
        for path,obj,ancestors in walk(package["data"],package["path"]):
            validate_quantity(obj,path,ancestors,errors,counts)
            if re.search(r"\.(?:quantities|metrics)\[\d+\]$",path) and "value" not in obj:errors.append(f"{path}: explicit quantity/metric record requires value (numeric or null with reason)")
            for key,value in obj.items():
                if key in ("quantities","metrics") and isinstance(value,list):
                    for i,item in enumerate(value):
                        if not isinstance(item,dict):errors.append(f"{path}.{key}[{i}]: quantity/metric must be an object")
                if key in ("quantities","metrics") and not isinstance(value,list):errors.append(f"{path}.{key}: expected an array of quantity objects")
                ref_field=key.endswith(("evidence_ids","evidence_refs")) or key in ("source_evidence","target_evidence","external_evidence_registry")
                if ref_field:
                    for ref in reference_values(key,value,f"{path}.{key}",errors):
                        if ref not in records:errors.append(f"{path}.{key}: unresolved evidence reference {ref} in accepted packages")
                        elif key=="external_evidence_registry":
                            declared_paths=[value[ref]] if isinstance(value,dict) else [v.get("path") for v in value if isinstance(v,dict) and v.get("evidence_id")==ref]
                            for declared in declared_paths:
                                if declared is not None and declared!=records[ref]:errors.append(f"{path}.{key}: {ref} package locator disagrees with accepted registry")
                if key=="evidence_id" and isinstance(value,str) and value not in records:errors.append(f"{path}.evidence_id: unresolved evidence reference {value} in accepted packages")
    return {"status":"pass" if not errors else "failed","package_index":snapshot["index"],"packages":len(packages),
            "evidence_records":len(records),**counts,"errors":errors,"warnings":warnings}


def validate(root=ROOT):
    try:return validate_snapshot(load_accepted_packages(root))
    except PackageError as exc:return {"status":"failed","packages":0,"evidence_records":0,"errors":[str(exc)],"warnings":[]}


if __name__=="__main__":
    report=validate();print(json.dumps(report,indent=2));sys.exit(bool(report["errors"]))
