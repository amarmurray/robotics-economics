"""Validated annual levels; no economics, interpolation or empirical calibration."""
from __future__ import annotations

import copy
import math

SCHEMA = "digital-annual-paths/0.1"
CHANNELS = ("digital_efficiency", "coordination", "digital_cost_usd")
UNITS = {
    "digital_efficiency": "fraction of baseline human hours removed at matched service",
    "coordination": "proportional change in accepted robot capacity before the site cap",
    "digital_cost_usd": "constant 2026 USD per supported full robot-year; additional service bundle",
}


def resolve_paths(parameters, base_year, bounds, paths=None):
    """Validate every period before computing anything; absent channels stay constant."""
    supplied = {} if paths is None else paths
    allowed = {"schema_version", "base_year", "epistemic_status", *CHANNELS}
    if not isinstance(supplied, dict) or set(supplied) - allowed:
        raise ValueError("digital_paths must be an object with only the supported fields")
    if paths is not None:
        if supplied.get("schema_version") != SCHEMA:
            raise ValueError(f"digital_paths schema_version must be {SCHEMA}")
        year = supplied.get("base_year")
        if isinstance(year, bool) or not isinstance(year, int) or year != base_year:
            raise ValueError(f"digital_paths base_year must be {base_year}")
        if supplied.get("epistemic_status") != "synthetic_assumption":
            raise ValueError("digital_paths epistemic_status must be synthetic_assumption")
    years = int(parameters["years"])
    resolved = {"schema_version": SCHEMA, "base_year": base_year,
                "epistemic_status": "synthetic_assumption", "units": dict(UNITS),
                "precedence": "Supplied annual levels replace scalars; omitted channels repeat scalars."}
    for name in CHANNELS:
        values = supplied.get(name, [parameters[name]] * years)
        if not isinstance(values, list) or len(values) != years:
            raise ValueError(f"digital_paths {name} must contain exactly {years} annual levels")
        lo, hi = bounds[name]
        for index, value in enumerate(values):
            if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value) or not lo <= value <= hi:
                raise ValueError(f"digital_paths {name}[{index}] must be finite and in [{lo}, {hi}]")
        resolved[name] = list(values)
    return resolved


def parameters_at(parameters, resolved_paths, period_index):
    """Use the same contemporaneous values in costs, eligibility and fleet output."""
    if isinstance(period_index, bool) or not isinstance(period_index, int) or not 0 <= period_index < int(parameters["years"]):
        raise ValueError("period_index must be an integer inside the scenario horizon")
    return {**parameters, **{name: resolved_paths[name][period_index] for name in CHANNELS}}


def run_trajectory(paths, overrides=None, preset="reference"):
    """Public convenience entry point, using the sole authoritative engine."""
    from .engine import run_scenario
    return run_scenario(overrides, preset, digital_paths=copy.deepcopy(paths))
