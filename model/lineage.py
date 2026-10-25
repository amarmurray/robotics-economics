"""Read-only trace of the existing matched-output calculation.

No independent economic formula or empirical calibration is introduced here.
"""
import inspect
from . import engine


def joint_trace(cell_id, overrides=None, preset="reference"):
    if not isinstance(cell_id, str):
        raise ValueError("cell_id must identify one modeled cell")
    catalog = engine.catalog()
    cell = next((c for c in catalog["cells"] if c["cell_id"] == cell_id), None)
    if cell is None:
        raise ValueError("Unknown modeled cell")
    result = engine.run_scenario(overrides, preset)
    p = result["parameters"]
    system = next(s for s in catalog["systems"] if s["system_id"] == cell["system_id"])
    capability = engine.capability_at(p, p["years"] - 1)
    branches = []
    for robot, digital in ((False, False), (False, True), (True, False), (True, True)):
        branches.append({
            "branch": f"C{int(robot)}{int(digital)}",
            "robot": robot, "digital": digital,
            "calculation": engine.matched_economics(cell, system, p, capability, digital, robot),
        })
    sources = []
    for function in (engine.capability_at, engine.operation, engine.matched_economics, engine.joint_comparisons):
        lines, start = inspect.getsourcelines(function)
        sources.append({"path": "model/engine.py", "function": function.__name__,
                        "start_line": start, "source": "".join(lines)})
    return {
        "schema_version": "joint-calculation-trace/0.1",
        "status": "synthetic_illustration",
        "scope": "One matched annual site at the final scenario horizon; no learned increment. Independent of selected display year or installed fleet.",
        "scenario_hash": result["scenario_hash"], "engine_sha256": result["engine_sha256"],
        "reference_year": result["fleet"]["years"][-1]["year"],
        "capability": capability,
        "input_source": "model/assumptions.json, explicit scenario overrides and literal assumptions in the engine functions",
        "cell": cell, "system": system, "parameters": p,
        "branches": branches,
        "comparison": next(r for r in result["joint"] if r["cell_id"] == cell_id),
        "empirical_coefficient_sources": [],
        "source_boundary": "All numerical inputs are synthetic. Source dossiers provide context and limitations; none calibrates these coefficients. Literal constants are visible in the engine function excerpts.",
        "functions": sources,
    }
