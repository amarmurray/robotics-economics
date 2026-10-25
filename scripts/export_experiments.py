#!/usr/bin/env python3
"""Export isolated synthetic witnesses; does not alter annual scenario exports."""
import hashlib
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from model.coordination_transactions import comparison
from model.treasury import financial_witnesses
from model.monthly_deployment import monthly_witnesses


def exports():
    result = {}
    for name, source, calculate in (
        ("coordination_witnesses", "model/coordination_transactions.py", comparison),
        ("treasury_witnesses", "model/treasury.py", financial_witnesses),
        ("monthly_deployment_witnesses", "model/monthly_deployment.py", monthly_witnesses),
    ):
        result[name] = {
            "schema_version": "isolated-research-witness/0.1",
            "status": "synthetic_unintegrated_not_empirical_calibration",
            "code_sha256": hashlib.sha256((ROOT / source).read_bytes()).hexdigest(),
            "code_path": source,
            "result": calculate(),
        }
        sources = [source]
        if name == "monthly_deployment_witnesses":
            sources.append("model/treasury.py")
        result[name]["source_hashes"] = {path: hashlib.sha256((ROOT/path).read_bytes()).hexdigest() for path in sources}
    return result


if __name__ == "__main__":
    for name, result in exports().items():
        target = ROOT / "model/results" / (name + ".json")
        target.write_text(json.dumps(result, indent=2, allow_nan=False) + "\n")
        print("Wrote", target.relative_to(ROOT))
