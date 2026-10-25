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


def research_summary(root=ROOT):
    field = json.loads((root / 'data/field_support_denominators.json').read_text())
    coordination = json.loads((root / 'data/coordination_reproducibility.json').read_text())
    dataset = next(x for x in coordination['reconstructed_datasets']
                   if x['dataset_id'] == 'HCR-DATA-TAC-GEMINI-COSTS')
    return {'schema_version': 'observed-research-summary/0.1',
            'calculation_code_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'source_snapshot_sha256': {name: hashlib.sha256((root / 'data' / name).read_bytes()).hexdigest()
                                      for name in ['field_support_denominators.json', 'coordination_reproducibility.json']},
            'field_support': field_support_summary(field),
            'tac_costs': tac_cost_summary(dataset)}


if __name__ == '__main__':
    print(json.dumps(research_summary(), indent=2, allow_nan=False))
