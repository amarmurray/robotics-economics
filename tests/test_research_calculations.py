import copy
import unittest
from model.research_calculations import research_summary, tac_cost_summary, field_support_summary, ROOT
from model.research_calculations import onboard_timing_summary, commercial_disclosure_summary, recovery_contract_summary
from model.research_calculations import hospital_economics_summary
from unittest.mock import patch
import json


class SourceArithmetic(unittest.TestCase):
    def hospital_packet(self):
        return json.loads((ROOT/'data/field_support_denominators.json').read_text())

    def test_hospital_versions_preserve_different_methods_and_numerators(self):
        packet=self.hospital_packet();before=copy.deepcopy(packet);result=hospital_economics_summary(packet)
        rows={r['calculation_id']:r for r in result['rows']}
        self.assertEqual(rows['FSD-ECON-C01']['value'],90.91)
        self.assertAlmostEqual(rows['FSD-ECON-C02']['value'],1650000/553)
        self.assertEqual(rows['FSD-ECON-C03']['value'],1366281)
        self.assertEqual(rows['FSD-ECON-C04']['value'],1108.28)
        self.assertAlmostEqual(rows['FSD-ECON-C05']['value'],1366281/1108.28)
        self.assertEqual(rows['FSD-ECON-C06']['value'],1)
        self.assertTrue(all(len(r['evidence_ids'])==1 for r in result['rows']))
        self.assertEqual(packet,before)

    def test_hospital_sensitivity_is_a_diagnostic_not_a_repaired_forecast(self):
        result=hospital_economics_summary(self.hospital_packet());rows={r['calculation_id']:r for r in result['rows']}
        self.assertEqual(rows['FSD-ECON-C07']['value'],6928000)
        self.assertEqual(rows['FSD-ECON-C08']['value'],6846000)
        self.assertEqual(rows['FSD-ECON-C09']['value'],6146000)
        self.assertIn('Neither allocation is verified',rows['FSD-ECON-C09']['boundary'])
        self.assertEqual(rows['FSD-ECON-C10']['value'],63800)
        self.assertTrue(all(x['value'] is None for x in result['unknowns'].values()))
        self.assertNotIn('roi',result);self.assertNotIn('calibrated_parameters',result)

    def test_hospital_arithmetic_rejects_mixed_source_dimensions_and_versions(self):
        for field,value in [('unit','USD per year'),('population','another hospital'),('period','different observation'),
                ('source_version','ISPOR abstract used as poster'),('measurement_status','observed_payroll'),
                ('value',None),('value',True),('value',float('inf')),('value',-1),('value',0)]:
            with self.subTest(field=field,value=value):
                p=self.hospital_packet();q=next(e for e in p['evidence'] if e['evidence_id']=='FSD-E007')['quantities'][0];q[field]=value
                with self.assertRaises(ValueError):hospital_economics_summary(p)

    def test_hospital_missing_duplicate_and_swapped_sources_fail(self):
        for mode in ('missing','duplicate','role','metric_id','version'):
            p=self.hospital_packet();e=next(e for e in p['evidence'] if e['evidence_id']=='FSD-E006')
            if mode=='missing':p['evidence'].remove(e)
            elif mode=='duplicate':p['evidence'].append(copy.deepcopy(e))
            elif mode=='role':e['quantities'].append(copy.deepcopy(e['quantities'][0]))
            elif mode=='metric_id':e['quantities'][0]['metric_id']='FSD-ECON-POSTER-MANUAL-HOURS'
            else:p['economic_audits'][0]['source_versions']['abstract']['evidence_id']='FSD-E007'
            with self.assertRaises(ValueError):hospital_economics_summary(p)

    def test_hospital_nonpositive_released_time_and_impossible_percent_fail(self):
        for eid,role,value in [('FSD-E007','robot_hours',1233.78),('FSD-E008','capital',5705001),('FSD-E009','assigned_completion',101)]:
            p=self.hospital_packet();e=next(e for e in p['evidence'] if e['evidence_id']==eid)
            next(q for q in e['quantities'] if q['role']==role)['value']=value
            with self.assertRaises(ValueError):hospital_economics_summary(p)

    def test_hospital_extension_requires_accepted_package_and_leaves_legacy_results(self):
        packet=self.hospital_packet();without=copy.deepcopy(packet)
        without.pop('economic_audits');without['evidence']=without['evidence'][:5]
        self.assertEqual(field_support_summary(packet),field_support_summary(without))
        self.assertIn('hospital_economics',research_summary())
        with patch('model.packages.load_accepted_packages',return_value={'packages':[]}):
            self.assertNotIn('hospital_economics',research_summary())

    def test_finance_illustration_does_not_repair_source_or_convert_currencies(self):
        packet=json.loads((ROOT/'data/customer_evidence.json').read_text());before=copy.deepcopy(packet)
        r=recovery_contract_summary(packet);eur,usd=r['rows']
        self.assertEqual((eur['headline_hourly'],eur['monthly_payment'],eur['implied_payment_per_planned_hour']),(7.99,575,3.59375))
        self.assertEqual((usd['headline_hourly'],usd['monthly_payment'],usd['implied_payment_per_planned_hour']),(8.67,711,4.44375))
        self.assertEqual((eur['undiscounted_payment_components'],usd['undiscounted_payment_components']),(27600,34128))
        self.assertFalse(eur['reconciles']);self.assertFalse(usd['reconciles'])
        self.assertEqual(packet,before)
        self.assertTrue(all(x['value'] is None for x in r['unknowns'].values()))
        self.assertNotIn('roi',r);self.assertNotIn('accepted_service_cost',r)

    def test_finance_illustration_requires_the_same_source_clock_and_scope(self):
        original=json.loads((ROOT/'data/customer_evidence.json').read_text())
        for field,value in [('unit','accepted jobs per month'),('population','A particular MiR250 contract'),('period','2025'),('value',0),('value',None),('value',True)]:
            p=copy.deepcopy(original);q=next(q for e in p['evidence'] for q in e.get('quantities',[]) if q.get('metric_id')=='FG-Q-MIR-HOURS');q[field]=value
            with self.assertRaises(ValueError):recovery_contract_summary(p)

    def test_finance_illustration_rejects_mixed_missing_and_duplicate_source_quantities(self):
        original=json.loads((ROOT/'data/customer_evidence.json').read_text())
        for mode in ('missing','duplicate','wrong_source'):
            p=copy.deepcopy(original);e=next(e for e in p['evidence'] if e['evidence_id']=='FG-E030')
            if mode=='missing':e['quantities'].pop()
            elif mode=='duplicate':e['quantities'].append(copy.deepcopy(e['quantities'][0]))
            else:e['evidence_id']='unrelated'
            with self.assertRaises(ValueError):recovery_contract_summary(p)

    def test_public_document_gates_do_not_become_transaction_permissions(self):
        p=json.loads((ROOT/'data/customer_evidence.json').read_text());a=next(x for x in p['disclosure_audits'] if x['audit_id']=='FG-AUDIT-03')
        self.assertEqual(len(a['gates']),5);self.assertEqual(len(a['unknowns']),6)
        self.assertTrue(all(v['value'] is None for v in a['unknowns'].values()))
        self.assertIn('declared scenarios',a['model_use'])
        r=research_summary();self.assertIn('recovery_contracts',r)
        with patch('model.packages.load_accepted_packages',return_value={'packages':[]}):self.assertNotIn('recovery_contracts',research_summary())

    def test_commercial_components_are_not_returns_or_cash_balances(self):
        packet=json.loads((ROOT/'data/customer_evidence.json').read_text())
        result=commercial_disclosure_summary(packet)
        self.assertEqual([r['value'] for r in result['calculations'].values()], [535000,400000,240000,365000000])
        self.assertEqual(result['financial_periods'][0]['gross_result'],-2691267)
        self.assertEqual(result['financial_periods'][1]['operating_cash_flow'],-86162577)
        self.assertNotEqual(result['financial_periods'][1]['net_result'],result['financial_periods'][1]['operating_cash_flow'])
        self.assertTrue(all(x['value'] is None for x in result['unknowns'].values()))
        self.assertNotIn('throughput', result['calculations'])
        self.assertIn('commercial_disclosures',research_summary())
        with patch('model.packages.load_accepted_packages',return_value={'packages':[]}):
            unaccepted=research_summary()
        self.assertNotIn('commercial_disclosures',unaccepted)
        self.assertNotIn('customer_evidence.json',unaccepted['source_snapshot_sha256'])

    def test_commercial_wrong_generation_units_period_and_missing_values_fail(self):
        original=json.loads((ROOT/'data/customer_evidence.json').read_text())
        for field,value in [('configuration','Digit 4'),('unit','USD per year'),('population','other offering'),('period','2025'),('value',None),('value',True),('value',-1)]:
            packet=copy.deepcopy(original)
            metric=next(q for e in packet['evidence'] for q in e.get('quantities',[]) if q.get('quantity_id')=='FG-Q-D5-LAUNCH-BOM')
            metric[field]=value
            with self.assertRaises(ValueError):commercial_disclosure_summary(packet)

    def test_commercial_historical_and_funding_reconciliation_rejects_inconsistent_sources(self):
        original=json.loads((ROOT/'data/customer_evidence.json').read_text())
        for key,value in [('FG-Q-AGILITY-2025-GROSS-RESULT',-1),('FG-Q-AGILITY-2025-NET-SALES',1781967.5),('FG-Q-CLOSE-PRIOR',466000000)]:
            packet=copy.deepcopy(original)
            metric=next(q for e in packet['evidence'] for q in e.get('quantities',[]) if q.get('quantity_id')==key)
            metric['value']=value
            with self.assertRaises(ValueError):commercial_disclosure_summary(packet)
        packet=copy.deepcopy(original)
        funding_source=next(e for e in packet['evidence'] if e['evidence_id']=='FG-E022')
        packet['evidence'].append(copy.deepcopy(funding_source))
        with self.assertRaises(ValueError):commercial_disclosure_summary(packet)

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
