import copy
import unittest
from model.research_calculations import research_summary, tac_cost_summary, field_support_summary, ROOT
import json


class SourceArithmetic(unittest.TestCase):
    def test_published_rows_and_conflict_remain_separate(self):
        result = research_summary()
        field = result['field_support']
        self.assertAlmostEqual(field['calculations']['FSD-CALC-04']['value'], 56.41)
        self.assertAlmostEqual(field['calculations']['FSD-CALC-05']['value'], 21.36)
        self.assertNotEqual(field['guro_reported_success_percent'], field['guro_count_implied_success_percent'])
        self.assertIsNone(field['paid_labor_saving'])
        costs = result['tac_costs']
        self.assertEqual((costs['row_count'], costs['perfect_count']), (175, 53))
        self.assertEqual(costs['all_displayed_cost_usd'], 740.34)
        self.assertEqual(costs['nonperfect_displayed_cost_usd'], 659.49)
        self.assertIsNone(costs['full_business_cost'])

    def test_no_success_has_unknown_cost_per_success(self):
        rows = [{'task_id': 'failed', 'checkpoint_max': 2, 'checkpoint_earned': 1,
                 'perfect': False, 'cost_usd': 4}]
        result = tac_cost_summary({'rows': rows})
        self.assertIsNone(result['suite_cost_per_perfect_usd'])
        self.assertEqual(result['nonperfect_cost_fraction'], 1)

    def test_duplicate_and_false_success_rejected(self):
        row = {'task_id': 'one', 'checkpoint_max': 2, 'checkpoint_earned': 1,
               'perfect': False, 'cost_usd': 4}
        with self.assertRaises(ValueError):
            tac_cost_summary({'rows': [row, copy.deepcopy(row)]})
        row['perfect'] = True
        with self.assertRaises(ValueError):
            tac_cost_summary({'rows': [row]})

    def test_unit_or_saved_result_drift_rejected(self):
        package = json.loads((ROOT / 'data/field_support_denominators.json').read_text())
        changed = copy.deepcopy(package)
        metric = next(m for c in changed['cases'] for m in c['metrics'] if m['metric_id'] == 'FSD-Q-M05')
        metric['unit'] = 'minutes'
        with self.assertRaises(ValueError):
            field_support_summary(changed)
        for metric_id, wrong_unit in [('FSD-G-M01', 'hours'), ('FSD-G-M06', 'fraction')]:
            changed = copy.deepcopy(package)
            metric = next(m for c in changed['cases'] for m in c['metrics'] if m['metric_id'] == metric_id)
            metric['unit'] = wrong_unit
            with self.assertRaises(ValueError):
                field_support_summary(changed)
        package['calculations'][0]['value'] = 0
        with self.assertRaises(ValueError):
            field_support_summary(package)
