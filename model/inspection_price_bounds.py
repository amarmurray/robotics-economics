"""Derived window-cash bounds for matched existing inspection executions.

No new deployment worlds, empirical prices, maintenance benefits or failure values.
Both complete inputs are recomputed; stored summaries never establish eligibility.
"""
import copy,hashlib,json
from .utility_inspection import ROOT,ACTORS,run_inspection

SCHEMA='inspection-price-bounds/0.1'
RESULT='model/results/inspection_price_bounds.json'
SOURCE='model/results/utility_inspection.json'


def digest(x):return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':'),allow_nan=False).encode()).hexdigest()


def source_hashes():
    return {p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest()for p in ('model/inspection_price_bounds.py','model/utility_inspection.py','model/treasury.py',SOURCE)}


def obligation(x):
    return dict(cycles=x['cycles'],required_points=sorted(x['required_points']),deadline_minute=x['deadline_minute'],
        field_duty_cycles=sorted(x['field_duty_cycles']),field_duty_person_minutes=x['field_duty_person_minutes'] if x['field_duty_cycles'] else 0,
        presence_cycles=sorted(set(x['mandatory_visit_cycles']) if x['replacement_authorized'] else set(range(x['cycles']))))


def cash_account(r):
    s=r['summary'];invoices=r['closing_treasury']['invoices'];external=set(ACTORS[2:])
    rows=[dict(payer=payer,resource_cash_cents=sum(i['paid_cents']for i in invoices if i['payer']==payer and i['payee']in external))for payer in ACTORS[:2]]
    provider=rows[1]['resource_cash_cents'];fees=s['internal_monitor_fees_cents'];gain=s['provider_net_cash_change_cents']
    assert provider==fees-gain
    assert sum(v['resource_cash_cents']for v in rows)==s['external_resource_cash_cents']
    assert s['operator_outlay_cents']-gain==s['external_resource_cash_cents']
    return dict(customer_outlay_cents=s['operator_outlay_cents'],monitor_fees_cents=fees,customer_nonfee_outlay_cents=s['operator_outlay_cents']-fees,
        provider_resource_cash_cents=provider,provider_cash_change_cents=gain,consolidated_resource_cash_cents=s['external_resource_cash_cents'],payer_resources=rows)


def compare_inputs(inputs):
    if not isinstance(inputs,dict) or set(inputs)!={'baseline','alternative'}:raise ValueError('Exactly complete baseline and alternative inspection inputs required')
    cases={key:run_inspection(inputs[key])for key in ('baseline','alternative')};base,alt=(cases[k]for k in ('baseline','alternative'));ob={k:obligation(r['inputs'])for k,r in cases.items()};reasons=[]
    different=[k for k in ob['baseline']if ob['baseline'][k]!=ob['alternative'][k]]
    if different:reasons.append('unmatched_obligation:'+','.join(different))
    if not any(c['enabled']for c in alt['inputs']['channels']):reasons.append('alternative:no_monitoring_service')
    for key,r in cases.items():
        if r['summary']['complete_service_windows']!=r['inputs']['cycles']:reasons.append(key+':incomplete_due_service')
        if r['summary']['due_unpaid_cents']:reasons.append(key+':unpaid_commitments')
        if any(not c['fee_funded'] or not c['resource_funded']for row in r['cycles']for c in row['channels']):reasons.append(key+':unfunded_monitoring_booking')
    cash={k:cash_account(r)for k,r in cases.items()};b,a=cash['baseline'],cash['alternative'];bounds=None
    if not reasons:
        ceiling=b['customer_outlay_cents']-a['customer_nonfee_outlay_cents'];recovery=a['provider_resource_cash_cents'];width=ceiling-recovery
        resource_delta=a['consolidated_resource_cash_cents']-b['consolidated_resource_cash_cents'];customer_delta=a['customer_outlay_cents']-b['customer_outlay_cents']
        assert width== -resource_delta+b['provider_cash_change_cents']
        bounds=dict(customer_fee_ceiling_cents=ceiling,provider_recorded_resource_recovery_cents=recovery,interval_width_cents=width,
            window_interval_nonempty=width>=0,customer_outlay_change_cents=customer_delta,consolidated_resource_change_cents=resource_delta,
            further_net_customer_value_needed_at_recorded_fee_cents=max(0,customer_delta),
            further_net_customer_value_needed_at_resource_recovery_cents=max(0,-width),
            further_net_consolidated_value_needed_cents=max(0,resource_delta),baseline_provider_cash_change_cents=b['provider_cash_change_cents'])
    r=dict(schema_version=SCHEMA,status='derived_synthetic_window_comparison_not_commercial_price',inputs=copy.deepcopy(inputs),executions=cases,
        comparison=dict(eligible=not reasons,reasons=reasons,obligations=ob,scope='Same declared point/property identities and due obligation within the synthetic fixture. This is not empirical diagnostic equivalence or a current contract.'),
        cash=cash,bounds=bounds,source_sha256=source_hashes(),
        equations=['Buyer fee ceiling = baseline customer outlay - alternative customer nonfee outlay.',
            'Provider recorded-resource recovery amount = alternative provider external-resource payments.',
            'Interval width = buyer fee ceiling - provider recovery amount = baseline provider cash change - consolidated resource change.',
            'Fees cancel inside the fixed customer/provider perimeter. Changed physical duties and incomplete service cannot be priced as equivalent.'],
        boundaries=['All numerical amounts are inherited synthetic window bills. No observed price, labor effect, maintenance value or avoided outage is assigned.',
            'A nonempty interval is a necessary aggregate window-cash condition only. Repricing requires a new complete execution; fee timing can change funding, service and costs.',
            'The provider recovery amount excludes unmodeled asset lifecycle, capital, taxes, risk and profit. Provider cash change is not enterprise profit.',
            'Further net value is a required evidence threshold after all additional downstream costs, not an estimated benefit. Same accepted readings alone establish no changed intervention.',
            'The inspection transaction sequence is not a calendar or a financed enterprise. Retained assets, capital exposure and terminal obligations preclude a lifecycle ROI ranking.'])
    r=json.loads(json.dumps(r,allow_nan=False));r['case_hash']=digest(r);return r


def replay_price_bounds(saved):
    if not isinstance(saved,dict) or saved.get('schema_version')!=SCHEMA:raise ValueError('Complete inspection price-bound comparison required')
    return compare_inputs(saved.get('inputs'))


def comparison_pairs():
    return {'retained_paid_crew':('human_committed','mobile_complete_committed'),
        'avoidable_visit':('human_per_visit','mobile_complete_avoidable'),
        'physical_duty_remains':('human_field_duty','field_duty_remains'),
        'fixed_qualified_alternative':('human_per_visit','fixed_complete_avoidable'),
        'mobile_against_fixed':('fixed_complete_avoidable','mobile_complete_avoidable'),
        'one_bad_reading':('human_per_visit','one_bad_reading'),
        'late_fallback_not_matched':('human_committed','fallback_late'),
        'unfunded_provider_not_priced':('human_committed','provider_resource_shortfall')}


def selected_price_bounds(pair):
    if not isinstance(pair,str) or pair not in comparison_pairs():raise ValueError('Unknown existing inspection comparison')
    data=json.loads((ROOT/SOURCE).read_text());b,a=comparison_pairs()[pair]
    return compare_inputs({'baseline':data['cases'][b]['inputs'],'alternative':data['cases'][a]['inputs']})


def price_bounds_artifact():
    pairs=comparison_pairs();results={k:selected_price_bounds(k)for k in pairs}
    return dict(schema_version='inspection-price-bounds-artifact/0.1',source_sha256=source_hashes(),pairs={k:dict(baseline=b,alternative=a)for k,(b,a)in pairs.items()},
        comparisons=results,summary=[dict(comparison=k,**pairs_as_dict,eligible=results[k]['comparison']['eligible'],reasons=results[k]['comparison']['reasons'],bounds=results[k]['bounds'])for k,pairs_as_dict in {k:dict(baseline=b,alternative=a)for k,(b,a)in pairs.items()}.items()],
        boundary='Eight derived comparisons reuse the eighteen existing inspection executions. They add no synthetic deployment worlds and supply no observed commercial price or maintenance benefit.')


def price_bounds_catalog():
    data=json.loads((ROOT/RESULT).read_text())
    if data['source_sha256']!=source_hashes():raise ValueError('Inspection price bounds are stale; regenerate')
    return {k:v for k,v in data.items()if k!='comparisons'}|{'comparisons':{'retained_paid_crew':data['comparisons']['retained_paid_crew']}}
