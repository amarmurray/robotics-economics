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
                            ("architecture_alternatives", "comparison_id"), ("benchmark_cards", "benchmark_id"),
                            ("relationships", "relationship_id")):
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
    models=identities["frontier_models"]
    for collection in ("model_rights_cards", "benchmark_cards"):
        for row in packet[collection]:
            if set(row.get("model_ids",[]))-models:
                raise ValueError("Unresolved model/release reference")
    for card in packet["model_rights_cards"]:
        if card.get("public_grant") in ("noncommercial_only","mixed_component_terms","not_identified") and card.get("commercial_use_resolved") is not False:
            raise ValueError("Public artifact terms cannot become blanket commercial clearance")
        if card["rights_status"] in ("unknown", "conflicting") and card.get("commercial_use_resolved") is not False:
            raise ValueError("Unresolved rights cannot become commercial clearance")
    for card in packet["benchmark_cards"]:
        if card.get("commercial_service_calibration") is not False:
            raise ValueError("A laboratory benchmark cannot silently calibrate commercial service")
    deployments=packet.get("deployment_cards",[])
    if len({d["deployment_id"] for d in deployments})!=len(deployments) or len({d["event_identity"] for d in deployments})!=len(deployments):
        raise ValueError("Duplicate deployment identity/event")
    for deployment in deployments:
        if deployment["operator_actor_id"] not in actors:
            raise ValueError("Unresolved deployment operator")
        if deployment.get("model_attribution_status")=="not_established_in_inspected_sources" and deployment.get("model_id") is not None:
            raise ValueError("Unverified deployed model attribution")
        for partner in deployment.get("named_partner_roles",[]):
            if partner["actor_id"] not in actors:raise ValueError("Unresolved named partner")
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
    return {"schema_version": "frontier-model-summary/1.1", "as_of": packet["as_of"],
            "status": "bounded_source_synthesis_not_company_valuation",
            "scenario_inputs_used": False, "coverage": copy.deepcopy(packet["coverage"]),
            "transaction": acquisition_reconciliation(packet),
            "skild_issuer_reported_quantities": copy.deepcopy(operating["quantities"]),
            "operating_quantity_boundary": "ARR, recognized revenue and paying-customer count retain their separate denominators; no combined revenue or margin is calculated.",
            "source_conflicts": copy.deepcopy(packet["source_conflicts"]),
            "regional_source_checks": regional_source_arithmetic(packet),
            "deployment_cards": copy.deepcopy(packet.get("deployment_cards",[])),
            "architecture_costs_available": False,
            "model_benchmark_ranking_available": False,
            "source_hashes": {PACKAGE: hashlib.sha256((root/PACKAGE).read_bytes()).hexdigest(),
                              "model/frontier_models.py": hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}}


def _source_quantities(packet):
    index={}
    for claim in packet['evidence']:
        for quantity in claim.get('quantities',[]):
            key=quantity['quantity_id']
            if key in index:raise ValueError('Duplicate source quantity identity')
            index[key]=quantity
    return index


def regional_source_arithmetic(packet):
    """Reconcile stated metrics; never silently repair a conflicting source."""
    cards={c['benchmark_id']:c for c in packet['benchmark_cards']}
    needed={'K-B-RLDX-ALLEX','K-B-RLDX-LATENCY','K-B-RYNN-VLA','K-B-RLDX-TABLE9'}
    if not needed.intersection(cards):return {'status':'not_available_in_this_packet'}
    if needed-set(cards):raise ValueError('Incomplete regional benchmark records')
    quantities=_source_quantities(packet)
    def number(key,unit,positive=False):
        q=quantities[key]
        if q['unit']!=unit:raise ValueError('Source quantity unit mismatch: '+key)
        value=q['value']
        if isinstance(value,bool) or not isinstance(value,(int,float)):
            raise ValueError('Unknown source quantity is not zero: '+key)
        value=Decimal(str(value))
        if not value.is_finite() or value<0 or (positive and value==0):raise ValueError('Invalid source number')
        return value
    def close(a,b,tolerance):
        if abs(a-b)>Decimal(tolerance):raise ValueError('Reported source arithmetic does not reconcile within displayed precision')
    allex=cards['K-B-RLDX-ALLEX']
    kinds=[row['metric_kind'] for row in allex['series']]
    if kinds!=['binary_task_success','binary_selection_success','graded_progress','graded_progress'] or allex['whole_task_success_established']:
        raise ValueError('Mixed progress metrics cannot become a whole-task probability')
    allex_trials=number(allex['trials_quantity_id'],'trials per task per policy',True)
    if allex_trials!=allex_trials.to_integral_value():raise ValueError('Trials must be integer counts')
    values=[number(row['quantity_id'],'percent of task-specific score') for row in allex['series']]
    if any(v>100 for v in values):raise ValueError('Invalid source percent')
    average=sum(values)/len(values)
    reported=number(allex['reported_mean_quantity_id'],'percent mean task-specific score')
    close(average,reported,'0.05')
    latency=cards['K-B-RLDX-LATENCY']
    eager=number(latency['eager_quantity_id'],'milliseconds',True)
    optimized=number(latency['optimized_quantity_id'],'milliseconds',True)
    ratio=eager/optimized
    published_ratio=number(latency['reported_ratio_quantity_id'],'ratio',True)
    close(ratio,published_ratio,'0.005')
    rynn=cards['K-B-RYNN-VLA']
    trials=number(rynn['trials_quantity_id'],'trials per task per policy',True)
    if trials!=trials.to_integral_value():raise ValueError('Trials must be integer counts')
    regimes=[]
    for regime in rynn['regimes']:
        rates=[number(rynn['source_quantity_prefix']+regime+'-'+task,'percent complete-task success') for task in rynn['tasks']]
        progress=[number(rynn['source_quantity_prefix']+regime+'-PROC-'+task,'percent subtask progress') for task in rynn['tasks']]
        if any(v>100 for v in rates+progress):raise ValueError('Invalid source percent')
        final_mean=sum(rates)/len(rates);process_mean=sum(progress)/len(progress)
        reported_final=number(rynn['source_quantity_prefix']+regime+'-MEAN','percent mean complete-task success')
        reported_process=number(rynn['source_quantity_prefix']+regime+'-PROC-MEAN','percent mean subtask progress')
        close(final_mean,reported_final,'0.005');close(process_mean,reported_process,'0.005')
        reconstructed=[]
        for rate in rates:
            count=(trials*rate/100).to_integral_value()
            close(count/trials*100,rate,'0.005')
            reconstructed.append(int(count))
        regimes.append({'regime':regime.lower(),'reported_final_success_percent':float(reported_final),
                        'recomputed_final_success_percent':float(final_mean),
                        'reported_process_percent':float(reported_process),'recomputed_process_percent':float(process_mean),
                        'full_completions_implied_by_percentages':sum(reconstructed),'protocol_trials':int(trials)*len(rates),
                        'raw_trial_logs_verified':False})
    t9=cards['K-B-RLDX-TABLE9']
    if t9['outcome_weights']!={'FULL':1,'PARTIAL':0.5,'FAIL':0} or t9['corrected_empirical_effect_available']:
        raise ValueError('Preserve the stated scoring rule and unresolved empirical effect')
    n=number(t9['trials_quantity_id'],'trials per condition',True)
    rows=[]
    for condition in t9['conditions']:
        counts={key:number(t9['source_quantity_prefix']+condition+'-'+key,'reported trial outcomes') for key in t9['outcome_weights']}
        if any(v!=v.to_integral_value() for v in counts.values()) or sum(counts.values())!=n:
            raise ValueError('Reported outcome counts do not sum to the declared trials')
        reconstructed=sum(counts[k]*Decimal(str(weight)) for k,weight in t9['outcome_weights'].items())
        printed=number(t9['source_quantity_prefix']+condition+'-SCORE','reported weighted score sum')
        printed_percent=number(t9['source_quantity_prefix']+condition+'-RATE','reported percent score')
        close(printed/n*100,printed_percent,'0.05')
        rows.append({'condition':condition.lower(),'trials':int(n),'printed_counts':{k.lower():int(v) for k,v in counts.items()},
                     'score_from_printed_counts_and_rule':float(reconstructed),'printed_score':float(printed),
                     'printed_percent':float(printed_percent),'score_reconciles':reconstructed==printed})
    conflict=not all(row['score_reconciles'] for row in rows)
    return {'status':'bounded_source_arithmetic_not_runtime_validation','scenario_inputs_used':False,
            'allex':{'reported_mean':float(reported),'recomputed_mean':float(average),
                     'metric':'mean of heterogeneous binary and progress task scores',
                     'whole_job_success_probability':None,'whole_job_success_probability_missing_reason':'Full completion cannot be reconstructed from mixed progress averages.',
                     'evidence_ids':['K-E016']},
            'rldx_latency':{'eager_p50_ms':float(eager),'optimized_p50_ms':float(optimized),
                            'recomputed_ratio':float(ratio),'reported_ratio':float(published_ratio),
                            'hardware':'RTX 5090 and Core Ultra 7 265K desktop',
                            'scope':'Reported all-modality p50 inference setup; no tail/embedded/complete-robot-loop guarantee.',
                            'evidence_ids':['K-E017']},
            'rynn_trials':{'regimes':regimes,'scope':'Three trained tasks; 20 randomized trials per task. Process and final-success metrics remain distinct; implied counts are arithmetic, not a trial-log audit.',
                           'evidence_ids':['K-E028','K-E029']},
            'rldx_table9':{'status':'unresolved_source_arithmetic' if conflict else 'source_arithmetic_consistent',
                           'rows':rows,'source_conflict_present':conflict,'corrected_empirical_effect':None,
                           'corrected_empirical_effect_missing_reason':('Counts, scoring rule and printed score column disagree; which source entry requires correction is unknown.' if conflict else 'Arithmetic consistency alone does not independently validate an empirical effect.'),
                           'scope':'Verified in direct HTML and visually in arXiv v2 PDF page 53. Conditional reconstruction is not corrected measured performance.',
                           'evidence_ids':['K-E030']},
            'cross_model_ranking_available':False}
