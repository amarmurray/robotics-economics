"""Frontier-model evidence joins and seller-disclosure arithmetic, not an ROI model."""
from decimal import Decimal
import copy
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = "data/frontier_model_economics.json"


def validate_packet(packet, root=ROOT):
    """Keep roles, rights uncertainty and unpriced target architectures explicit."""
    identities = {}
    for collection, key in (("model_labs", "actor_id"), ("frontier_models", "model_id"),
                            ("model_rights_cards", "artifact_id"), ("dossiers", "dossier_id"),
                            ("architecture_alternatives", "comparison_id")):
        ids = [r[key] for r in packet[collection]]
        if len(ids) != len(set(ids)):
            raise ValueError("Duplicate identities in "+collection)
        identities[collection] = set(ids)
    actors = identities["model_labs"]
    systems = {s["system_id"] for s in json.loads((root/"data/capability_evidence.json").read_text())["systems"]}
    for collection in ("frontier_models", "model_rights_cards", "dossiers"):
        for row in packet[collection]:
            if row["actor_id"] not in actors:
                raise ValueError("Unresolved model-layer actor")
            if set(row.get("related_system_ids", []))-systems:
                raise ValueError("Unresolved related system; do not create duplicate system identities")
    for card in packet["model_rights_cards"]:
        if card["rights_status"] in ("unknown", "conflicting") and card.get("commercial_use_resolved") is not False:
            raise ValueError("Unresolved rights cannot become commercial clearance")
    for relation in packet["relationships"]:
        for key in ("from_actor_id", "to_actor_id"):
            if relation[key] not in actors:
                raise ValueError("Unresolved relationship counterparty")
    for row in packet["architecture_alternatives"]:
        if row["empirical_compatibility"] != "not_established":
            raise ValueError("This source packet establishes no matched-service qualification")
        for key in ("annual_resource_cost_usd", "model_payment_usd"):
            if row[key] is not None or not row.get(key+"_missing_reason"):
                raise ValueError("Unpriced architecture requires explicit unknown costs, not invented point estimates")
    if packet["coverage"]["scenario_coefficients_imported"] is not False:
        raise ValueError("Publisher model scores cannot silently calibrate scenario coefficients")


def acquisition_reconciliation(packet):
    evidence = next(e for e in packet["evidence"] if e["evidence_id"] == "K-E006")
    amounts = {}
    for q in evidence["quantities"]:
        if q["unit"] != "USD millions" or q["epistemic_status"] != "company_filing_reported_amount":
            raise ValueError("Transaction arithmetic requires the same filing, unit and accounting boundary")
        value = q["value"]
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            raise ValueError("Missing transaction amounts are not zero")
        number = Decimal(str(value))
        if not number.is_finite():
            raise ValueError("Nonfinite transaction amount")
        if q["quantity_id"] in amounts:
            raise ValueError("Duplicate transaction quantity")
        amounts[q["quantity_id"].removeprefix("K-Q-ZBRA-")] = number
    consideration = sum(amounts[k] for k in ("CASH", "EQUITY", "ESCROW"))
    assets = sum(amounts[k] for k in ("GOODWILL", "TECHNOLOGY", "INVENTORY", "OTHER-NET-ASSETS"))
    checks = {"consideration_components_match": consideration == amounts["TOTAL"],
              "net_assets_components_match": assets == amounts["NET-ASSETS"],
              "seller_gain_matches": consideration-assets == amounts["GAIN"]}
    if not all(checks.values()):
        raise ValueError("Filing arithmetic does not reconcile; preserve and investigate the conflict")
    return {"status": "source_arithmetic_reproduced", "unit": "USD millions",
            "completion_date": "2026-03-27", "announcement_date": "2026-04-15",
            "cash_consideration": float(amounts["CASH"]),
            "equity_fair_value": float(amounts["EQUITY"]),
            "escrow_fair_value": float(amounts["ESCROW"]),
            "total_consideration": float(consideration), "net_assets_sold": float(assets),
            "seller_gain": float(consideration-assets), "checks": checks,
            "evidence_ids": ["K-E006"],
            "boundary": "Seller disclosed accounting amounts. Total consideration is not all cash, and seller gain is not buyer/model operating profit. Escrow availability is conditional."}


def frontier_model_summary(root=ROOT, packet=None):
    packet = packet if packet is not None else json.loads((root/PACKAGE).read_text())
    validate_packet(packet, root)
    operating = next(e for e in packet["evidence"] if e["evidence_id"] == "K-E005")
    return {"schema_version": "frontier-model-summary/1.0", "as_of": packet["as_of"],
            "status": "bounded_source_synthesis_not_company_valuation",
            "scenario_inputs_used": False, "coverage": copy.deepcopy(packet["coverage"]),
            "transaction": acquisition_reconciliation(packet),
            "skild_issuer_reported_quantities": copy.deepcopy(operating["quantities"]),
            "operating_quantity_boundary": "ARR, recognized revenue and paying-customer count retain their separate denominators; no combined revenue or margin is calculated.",
            "source_conflicts": copy.deepcopy(packet["source_conflicts"]),
            "architecture_costs_available": False,
            "model_benchmark_ranking_available": False,
            "source_hashes": {PACKAGE: hashlib.sha256((root/PACKAGE).read_bytes()).hexdigest(),
                              "model/frontier_models.py": hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}}
