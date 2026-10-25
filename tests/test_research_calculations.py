import copy
import unittest
from model.research_calculations import research_summary, tac_cost_summary, field_support_summary, ROOT
from model.research_calculations import onboard_timing_summary
from unittest.mock import patch
import json


class SourceArithmetic(unittest.TestCase):
    def test_onboard_summary_preserves_qualification_missingness(self):
        packet=json.loads((ROOT/'data/onboard_workload_qualification.json').read_text())
        summary=onboard_timing_summary(packet)
        self.assertEqual([v['value'] for v in summary['calculations'].values()],[40,.1,1])
        self.assertIsNone(summary['deadline_miss_rate'])
        self.assertIsNone(summary['sustained_policy_throughput'])
        with patch('model.packages.load_accepted_packages',return_value={'packages':[]}):
            result=research_summary()
        self.assertNotIn('onboard_timing',result)
        self.assertNotIn('onboard_workload_qualification.json',result['source_snapshot_sha256'])

    def test_onboard_wrong_units_populations_and_stale_arithmetic_fail(self):
        original=json.loads((ROOT/'data/onboard_workload_qualification.json').read_text())
        for field,value in [('unit','seconds'),('population','different task suite'),('period','different run'),('value',None),('value',-1)]:
            packet=copy.deepcopy(original)
            metric=next(q for e in packet['evidence'] for q in e.get('quantities',[]) if q['metric_id']=='OWQ-M02')
            metric[field]=value
            with self.assertRaises(ValueError):onboard_timing_summary(packet)
        original['calculations'][0]['value']=50
        with self.assertRaises(ValueError):onboard_timing_summary(original)

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
