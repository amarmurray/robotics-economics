"""Read-only trace of the existing matched-output calculation.

No independent economic formula or empirical calibration is introduced here.
"""
import inspect
from . import engine
from . import trajectories


def joint_trace(cell_id, overrides=None, preset="reference", digital_paths=None, year=None, architecture_overrides=None):
    if not isinstance(cell_id, str):
        raise ValueError("cell_id must identify one modeled cell")
    catalog = engine.catalog()
    cell = next((c for c in catalog["cells"] if c["cell_id"] == cell_id), None)
    if cell is None:
        raise ValueError("Unknown modeled cell")
    result = engine.run_scenario(overrides, preset, digital_paths=digital_paths, architecture_overrides=architecture_overrides)
    if year is None:
        year = result["joint_by_year"][-1]["year"]
    if isinstance(year, bool) or not isinstance(year, int):
        raise ValueError("year must be an integer inside the scenario horizon")
    annual = next((row for row in result["joint_by_year"] if row["year"] == year), None)
    if annual is None:
        raise ValueError("year must be inside the scenario horizon")
    p = trajectories.parameters_at(result["parameters"], result["resolved_digital_paths"], annual["period_index"])
    system = next(s for s in catalog["systems"] if s["system_id"] == cell["system_id"])
    capability = annual["capability"]
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
    path_sources = []
    for function in (trajectories.resolve_paths, trajectories.parameters_at):
        lines, start = inspect.getsourcelines(function)
        path_sources.append({"path": "model/trajectories.py", "function": function.__name__,
                             "start_line": start, "source": "".join(lines)})
    return {
        "schema_version": "joint-calculation-trace/0.2",
        "status": "synthetic_illustration",
        "scope": "One matched annual site at the requested year, using contemporaneous digital conditions and exogenous capability; no learned increment. Not realized fleet savings.",
        "scenario_hash": result["scenario_hash"], "engine_sha256": result["engine_sha256"],
        "reference_year": year,
        "model_source_hashes": result["model_source_hashes"],
        "scalar_parameters": result["parameters"],
        "digital_paths": result["digital_paths"],
        "resolved_digital_paths": result["resolved_digital_paths"],
        "capability": capability,
        "input_source": "model/assumptions.json, explicit scenario overrides and literal assumptions in the engine functions",
        "cell": cell, "system": system, "parameters": p,
        "branches": branches,
        "comparison": next(r for r in annual["comparisons"] if r["cell_id"] == cell_id),
        "empirical_coefficient_sources": [],
        "source_boundary": "All numerical inputs are synthetic. Source dossiers provide context and limitations; none calibrates these coefficients. Literal constants are visible in the engine function excerpts.",
        "functions": sources,
        "path_functions": path_sources,
    }
