"""One explicit accepted-package registry for API, provenance and validation.

No filename glob grants acceptance. Consumers receive the same bytes, parsed
records and hashes. Registry/parse errors fail closed without hiding a package.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path, PurePosixPath

ROOT = Path(__file__).resolve().parents[1]
INDEX_PATH = "data/package_index.json"


class PackageError(ValueError):
    """Accepted evidence registry or package is unavailable or malformed."""


def _read_json(path):
    def reject_constant(value):
        raise ValueError(f"Nonstandard JSON number: {value}")
    def unique_object(pairs):
        result={}
        for key,value in pairs:
            if key in result:raise ValueError(f"Duplicate JSON object key: {key}")
            result[key]=value
        return result
    try:
        raw=path.read_bytes()
        data=json.loads(raw,parse_constant=reject_constant,object_pairs_hook=unique_object)
    except (OSError,UnicodeDecodeError,ValueError) as exc:
        raise PackageError(f"Cannot read accepted evidence artifact {path.name}: {exc}") from exc
    return raw,data


def load_accepted_packages(root=ROOT):
    """Return registry identity and accepted packages, without normalizing records."""
    root=Path(root).resolve()
    raw,index=_read_json(root/INDEX_PATH)
    if not isinstance(index,dict) or index.get("schema_version")!="accepted-evidence-packages/1.0":
        raise PackageError("Unsupported or missing accepted-package index schema")
    entries=index.get("packages")
    if not isinstance(entries,list) or not entries:
        raise PackageError("Accepted-package index requires a nonempty packages array")
    ids,paths,resolved_paths=set(),set(),set()
    packages=[]
    for entry in entries:
        if not isinstance(entry,dict):
            raise PackageError("Package-index entry must be an object")
        pid,path,status=entry.get("package_id"),entry.get("path"),entry.get("status")
        if not isinstance(pid,str) or not pid.strip() or pid in ids:
            raise PackageError(f"Missing or duplicate package_id: {pid}")
        if not isinstance(path,str) or not path or "\\" in path:
            raise PackageError(f"Invalid package path for {pid}")
        parts=PurePosixPath(path)
        target=(root/path).resolve()
        if not parts.parts or parts.is_absolute() or '..' in parts.parts or parts.parts[0]!="data" or parts.suffix!=".json" or not target.is_relative_to(root/"data") or path==INDEX_PATH:
            raise PackageError(f"Package path must be a JSON file within data/: {path}")
        if path in paths or target in resolved_paths or status!="accepted":
            raise PackageError(f"Duplicate or not explicitly accepted package: {path}")
        payload,data=_read_json(target)
        if not isinstance(data,dict) or not isinstance(data.get("evidence"),list):
            raise PackageError(f"Accepted package {path} requires an evidence[] array")
        ids.add(pid);paths.add(path);resolved_paths.add(target)
        packages.append({"package_id":pid,"path":path,"owner_lane":entry.get("owner_lane"),
                         "sha256":hashlib.sha256(payload).hexdigest(),"data":data})
    return {"index":{"path":INDEX_PATH,"sha256":hashlib.sha256(raw).hexdigest(),"schema_version":index["schema_version"]},"packages":packages}


def accepted_package_hashes(root=ROOT):
    snapshot=load_accepted_packages(root)
    return {"index":snapshot["index"],"hashes":{p["path"]:p["sha256"] for p in snapshot["packages"]}}
