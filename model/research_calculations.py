"""Bounded arithmetic on observed source rows; never scenario calibration.

Source formula strings are explanatory metadata, not executable input.
"""
from decimal import Decimal
import json
import hashlib
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def number(value):
    if isinstance(value, bool) or not isinstance(value, (int, float, str)):
        raise ValueError('Expected an observed number, not unknown or a Boolean')
    result = Decimal(str(value))
    if not result.is_finite():
        raise ValueError('Nonfinite source number')
    return result


def field_support_summary(package):
    metrics = {}
    for case in package['cases']:
        for metric in case['metrics']:
            key = metric['metric_id']
            if key in metrics:
                raise ValueError('Duplicate metric ID: ' + key)
            metrics[key] = metric

    expected_units = {
        'FSD-G-M01': 'requests', 'FSD-G-M03': 'eligible missions',
        'FSD-G-M04': 'failed missions', 'FSD-G-M05': 'completed trials',
        'FSD-G-M06': 'percent', 'FSD-G-M07': 'failed missions',
    }

    def value(key, unit=None):
        record = metrics[key]
        unit = unit or expected_units.get(key)
        if unit is not None and record['unit'] != unit:
            raise ValueError('Wrong source unit: ' + key)
        return number(record['value'])

    def ratio(numerator, denominator):
        denominator = value(denominator)
        if denominator <= 0:
            raise ValueError('Source denominator must be positive')
        return float(value(numerator) / denominator)

    results = {
        'FSD-CALC-01': {'value': ratio('FSD-G-M03', 'FSD-G-M01')},
        'FSD-CALC-02': {'value': ratio('FSD-G-M07', 'FSD-G-M04')},
        'FSD-CALC-03': {'value': ratio('FSD-G-M05', 'FSD-G-M03'),
                        'status': 'audit_only_conflicted_not_selected_for_calibration'},
    }
    for key, human_id, robot_id in [
        ('FSD-CALC-04', 'FSD-Q-M05', 'FSD-Q-M04'),
        ('FSD-CALC-05', 'FSD-Q-M07', 'FSD-Q-M06'),
    ]:
        human, robot = value(human_id, 'seconds'), value(robot_id, 'seconds')
        if human <= 0:
            raise ValueError('Manual phase mean must be positive')
        results[key] = {'value': float(human - robot),
                        'relative_value': float((human - robot) / human),
                        'unit': 'seconds difference of published phase means'}
    for saved in package['calculations']:
        calculated = results[saved['calculation_id']]
        for field in ('value', 'relative_value'):
            if field in saved and not math.isclose(float(saved[field]), calculated[field], rel_tol=1e-12, abs_tol=1e-12):
                raise ValueError('Stored source calculation disagrees: ' + saved['calculation_id'])
    return {
        'status': 'source_arithmetic_not_model_parameters',
        'calculations': results,
        'guro_reported_success_percent': float(value('FSD-G-M06')),
        'guro_count_implied_success_percent': 100 * results['FSD-CALC-03']['value'],
        'conflict_disposition': 'Retain both; do not select a calibrated success probability.',
        'paid_labor_saving': None,
        'paid_labor_saving_missing_reason': 'Phase means do not identify complete paid support or removable staffing.',
    }


def tac_cost_summary(dataset):
    seen = set()
    total, perfect_cost = Decimal(0), Decimal(0)
    perfect_count = 0
    for row in dataset['rows']:
        if row['task_id'] in seen:
            raise ValueError('Duplicate source task: ' + row['task_id'])
        seen.add(row['task_id'])
        maximum, earned = number(row['checkpoint_max']), number(row['checkpoint_earned'])
        if maximum <= 0 or not 0 <= earned <= maximum:
            raise ValueError('Invalid checkpoint score')
        perfect = earned == maximum
        if row['perfect'] is not perfect:
            raise ValueError('Perfect flag disagrees with checkpoint scores')
        cost = number(row['cost_usd'])
        if cost < 0:
            raise ValueError('Negative source cost')
        total += cost
        if perfect:
            perfect_count += 1
            perfect_cost += cost
    result = {
        'row_count': len(seen), 'perfect_count': perfect_count,
        'all_displayed_cost_usd': float(total),
        'perfect_displayed_cost_usd': float(perfect_cost),
        'nonperfect_displayed_cost_usd': float(total - perfect_cost),
        'suite_cost_per_perfect_usd': float(total / perfect_count) if perfect_count else None,
    }
    for key, saved in dataset.get('computed_summary', {}).items():
        if saved is None or result.get(key) is None:
            if saved != result.get(key):
                raise ValueError('Stored cost summary disagrees: ' + key)
        elif not math.isclose(float(saved), result[key], rel_tol=1e-12, abs_tol=1e-12):
            raise ValueError('Stored cost summary disagrees: ' + key)
    result.update({
        'status': 'reconstructed_cent_rounded_source_API_costs_not_business_economics',
        'nonperfect_count': len(seen) - perfect_count,
        'nonperfect_cost_fraction': float((total - perfect_cost) / total) if total else None,
        'rounding_bound_usd': float(len(seen) * Decimal('.005')),
        'rounding_assumption': 'Each displayed row rounded independently to nearest cent.',
        'full_business_cost': None,
        'full_business_cost_missing_reason': 'Separate environment models, infrastructure, omitted attempts and human work are not fully priced.',
    })
    return result


def onboard_timing_summary(package):
    """Rounded source arithmetic; no deadline or sustained-throughput estimate."""
    metrics = {}
    for claim in package["evidence"]:
        for metric in claim.get("quantities", []):
            key = metric["metric_id"]
            if key in metrics:
                raise ValueError("Duplicate onboard metric: " + key)
            metrics[key] = metric
    inputs = [("OWQ-M27", "Hz"), ("OWQ-M02", "ms"), ("OWQ-M03", "ms")]
    values = []
    scope = None
    for key, unit in inputs:
        metric = metrics[key]
        if metric["unit"] != unit:
            raise ValueError("Wrong onboard source unit: " + key)
        context = (metric["population"], metric["period"])
        if scope is not None and scope != context:
            raise ValueError("Onboard arithmetic mixes source populations or periods")
        scope = context
        value = number(metric["value"])
        if value <= 0:
            raise ValueError("Onboard timing/rate inputs must be positive")
        values.append(value)
    rate, median, mean = values
    interval = Decimal(1000) / rate
    calculated = dict(zip(("OWQ-C01", "OWQ-C02", "OWQ-C03"),
                          (interval, interval - median, mean - interval)))
    stored = package["calculations"]
    if len(stored) != 3 or {c["calculation_id"] for c in stored} != set(calculated):
        raise ValueError("Expected exactly three onboard source calculations")
    for row in stored:
        if row["unit"] != "ms" or number(row["value"]) != calculated[row["calculation_id"]]:
            raise ValueError("Stored onboard arithmetic disagrees")
    return {"status": "source_arithmetic_not_deadline_qualification",
            "calculations": {key: {"value": float(value), "unit": "ms"} for key, value in calculated.items()},
            "deadline_miss_rate": None, "sustained_policy_throughput": None,
            "missing_reason": "Rounded component-sum summary statistics do not identify a full cycle, sustained operation or deadline-miss distribution."}


def commercial_disclosure_summary(package):
    """Reconcile disclosed components; do not estimate returns or site throughput."""
    audits = package.get('disclosure_audits', [])
    audit = next(a for a in audits if a['audit_id'] == 'FG-AUDIT-01')
    metrics = {}
    for claim in package['evidence']:
        for metric in claim.get('quantities', []):
            key = metric.get('quantity_id', metric.get('metric_id'))
            if key is None:  # Older context quantities have no reusable identifier.
                continue
            if key in metrics:
                raise ValueError('Duplicate commercial source quantity: ' + str(key))
            metrics[key] = metric

    def read(key, unit, population=None, period=None, configuration=None):
        m = metrics[key]
        if m['unit'] != unit:
            raise ValueError('Wrong commercial source unit: ' + key)
        for field, expected in [('population', population), ('period', period), ('configuration', configuration)]:
            if expected is not None and m.get(field) != expected:
                raise ValueError('Commercial source scope mismatch: ' + key)
        return number(m['value'])

    roles = audit['input_roles']
    population = 'Digit 5 illustrative commercial offering; no executed contract'
    period = 'Management planning assumptions, disclosed 2026-10-13'
    units = {'life_years': 'years', 'raas_monthly': 'USD per month',
             'ownership_annual_service': 'USD per year', 'provider_annual_service': 'USD per year'}
    inputs = {role: read(key, units.get(role, 'USD'), population, period, 'Digit 5')
              for role, key in roles.items()}
    if any(v < 0 for v in inputs.values()) or inputs['life_years'] <= 0 or inputs['life_years'] % 1:
        raise ValueError('Invalid illustrative life or monetary component')
    years = inputs['life_years']
    definitions = [
        ('raas_five_year_payments', 'Displayed RaaS payment components',
         inputs['raas_monthly'] * 12 * years + inputs['raas_deployment'],
         'monthly subscription × 12 × assumed life + deployment fee',
         ['raas_monthly', 'life_years', 'raas_deployment'],
         'Undiscounted arithmetic of rounded planning amounts; excludes customer retained work, financing and all other unpriced costs.'),
        ('ownership_five_year_payments', 'Displayed ownership payment components',
         inputs['purchase'] + inputs['purchase_deployment'] + inputs['ownership_annual_service'] * years,
         'purchase + deployment fee + annual service × assumed life',
         ['purchase', 'purchase_deployment', 'ownership_annual_service', 'life_years'],
         'Same hypothetical life; these payments do not identify an executed customer contract or whole-system cost.'),
        ('launch_product_resources', 'Named provider product cost at assumed launch BOM',
         inputs['launch_bom'] + inputs['provider_deployment'] + inputs['provider_annual_service'] * years,
         'Digit 5 launch BOM + provider deployment + annual software/maintenance cost × assumed life',
         ['launch_bom', 'provider_deployment', 'provider_annual_service', 'life_years'],
         'Management product-cost boundary excludes corporate SG&A/R&D; neither complete company cash nor a field-qualified cost estimate.'),
    ]
    calculations = {}
    for key, label, value, formula, source_roles, scope in definitions:
        calculations[key] = {'label': label, 'value': float(value), 'unit': 'USD',
                             'formula': formula, 'input_ids': [roles[r] for r in source_roles],
                             'scope': scope, 'evidence_ids': ['FG-E021']}
    cash = audit['cash_roles']
    gross = read(cash['gross'], 'USD', 'Business combination and related financings', 'Aggregate reported 2026-11-05')
    prior = read(cash['prior'], 'USD', 'Business combination and related financings', 'Aggregate reported 2026-11-05')
    if not 0 <= prior <= gross:
        raise ValueError('Prior funding must be a nonnegative component of gross funding')
    calculations['other_gross_financing_components'] = {
        'label': 'Gross headline less already-received component', 'value': float(gross - prior), 'unit': 'USD',
        'formula': 'reported aggregate gross financing − included prior funding',
        'input_ids': [cash['gross'], cash['prior']], 'evidence_ids': ['FG-E022'],
        'scope': 'Arithmetic of approximate headline components before expenses; not net new cash or available cash balance.'}
    financials = []
    for row in audit['financial_periods']:
        values = {role: read(key, 'USD', 'Agility Robotics standalone company', row['period'])
                  for role, key in row['metric_roles'].items()}
        if any(v % 1 for v in values.values()):
            raise ValueError('Historical statements are recorded in whole USD')
        if values['net_sales'] - values['cost_of_goods_sold'] != values['gross_result']:
            raise ValueError('Historical gross result does not reconcile: ' + row['period'])
        financials.append({'period': row['period'], **{k: int(v) for k, v in values.items()}, 'input_ids': row['metric_roles'],
                           'evidence_ids': row['evidence_ids'],
                           'scope': 'Whole-company amounts for unequal observation periods; no annualization or per-robot allocation.'})
    return {'status': 'disclosure_arithmetic_not_realized_unit_economics', 'audit_id': audit['audit_id'],
            'calculations': calculations, 'financial_periods': financials,
            'unknowns': audit['unresolved'],
            'population_guard': 'No ratio combines site totes and multi-program fleet hours.',
            'rounding_boundary': 'Exact component arithmetic can differ from approximate slide headlines; this is not a correction of undisclosed internal modeling.',
            'source_boundary': 'Source assumptions and historical disclosures remain separate from synthetic model parameters.'}


def research_summary(root=ROOT):
    field = json.loads((root / 'data/field_support_denominators.json').read_text())
    coordination = json.loads((root / 'data/coordination_reproducibility.json').read_text())
    dataset = next(x for x in coordination['reconstructed_datasets']
                   if x['dataset_id'] == 'HCR-DATA-TAC-GEMINI-COSTS')
    result = {'schema_version': 'observed-research-summary/0.2',
            'calculation_code_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'source_snapshot_sha256': {name: hashlib.sha256((root / 'data' / name).read_bytes()).hexdigest()
                                      for name in ['field_support_denominators.json', 'coordination_reproducibility.json']},
            'field_support': field_support_summary(field),
            'tac_costs': tac_cost_summary(dataset)}
    if __package__:
        from .packages import load_accepted_packages
    else:
        from packages import load_accepted_packages
    accepted = {p['path'] for p in load_accepted_packages(root)['packages']}
    path = 'data/onboard_workload_qualification.json'
    if path in accepted:
        result['onboard_timing'] = onboard_timing_summary(json.loads((root/path).read_text()))
        result['source_snapshot_sha256'][Path(path).name] = hashlib.sha256((root/path).read_bytes()).hexdigest()
    path = 'data/customer_evidence.json'
    if path in accepted:
        customer = json.loads((root/path).read_text())
        if customer.get('disclosure_audits'):
            result['commercial_disclosures'] = commercial_disclosure_summary(customer)
            result['source_snapshot_sha256'][Path(path).name] = hashlib.sha256((root/path).read_bytes()).hexdigest()
    return result


if __name__ == '__main__':
    print(json.dumps(research_summary(), indent=2, allow_nan=False))
