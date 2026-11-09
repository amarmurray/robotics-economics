import copy
import json
from pathlib import Path
from fractions import Fraction
import unittest

from model.calendar_bridge import rational
from model.qualified_staffing import qualified_staffing_artifact,run_qualified_staffing_case,replay_qualified_staffing,available_support


class QualifiedStaffingTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.artifact=qualified_staffing_artifact();cls.cases=cls.artifact['cases']
        cls.summary={s['case']:s for s in cls.artifact['summary']}

    def rows(self,name,op='incumbent'):
        return [x for x in self.cases[name]['staffed_renewals']['months'] if x['operator_id']==op]

    def test_cash_parts_and_unique_physical_units_conserve_in_every_world(self):
        for name,r in self.cases.items():
            self.assertEqual(sum(a['cash_cents'] for a in r['opening_treasury']['actors']),sum(a['cash_cents'] for a in r['closing_treasury']['actors']),name)
            self.assertEqual(r['entry_transition']['consolidation']['unclassified_boundary_cash_cents'],0)
            self.assertEqual(len(r['units']),len({u['unit_id'] for u in r['units']}))
            for p,a in zip(r['months'],r['component_inventory']['months']):
                self.assertEqual(p['compatible_parts'],a)
                for k in a['qualified_closing']:
                    self.assertEqual(a['qualified_opening'][k]+a['qualified_release'][k],a['qualified_closing'][k]+a['manufacturing_issued'][k]+a['service_issued'][k])
                    self.assertEqual(a['quarantine_opening'][k]+a['received'][k],a['quarantine_closing'][k]+a['qualified_release'][k])

    def test_annual_booking_is_same_physical_admission_not_an_added_capacity_pool(self):
        for r in self.cases.values():
            for year in r['annual_resources']['calendar_years']:
                for kind,v in year['resources'].items():
                    booked=sum((rational(x['committed_minutes'][kind]) for x in r['annual_resources']['attempts'] if x['calendar_year']==year['calendar_year']),Fraction())
                    self.assertEqual(booked,rational(v['booked_here_minutes']))
                    self.assertEqual(v['prior_use_minutes']+v['reserved_elsewhere_minutes']+booked+rational(v['remaining_unbooked_minutes']),rational(v['pool_minutes']))
            for a,b in zip(r['annual_resources']['months'],r['calendar_bridge']['months']):
                self.assertEqual(a['supported_unit_ids'],sorted(x['unit_id'] for x in b['cohorts']))
                attempts=[x for x in r['annual_resources']['attempts'] if x['month']==a['month']]
                self.assertEqual(sum((rational(x['committed_minutes']['support']) for x in attempts),Fraction()),60*(rational(b['support_hours_used'])+rational(b['qualification_hours_used'])))

    def test_crew_minutes_work_obligations_and_awards_conserve_separately(self):
        for r in self.cases.values():
            for x in r['staffed_renewals']['months']:
                self.assertEqual(sum((rational(b['minutes']) for b in x['bookings']),Fraction())+rational(x['unused_minutes']),x['regular_available_minutes']+x['overtime_paid_minutes'])
                self.assertTrue(all(b['worker_resource_id']==x['resource_id'] for b in x['bookings']))
                self.assertEqual(x['outside_completed_jobs']+x['outside_unserved_jobs'],x['outside_required_jobs'])
                self.assertEqual(rational(x['accepted_cleaning_zones'])+rational(x['unserved_cleaning_zones']),x['cleaning_required_zones'])
            for m in r['competition']['months']:self.assertEqual(sum(x['units'] for x in m['lots']),500)
            for e in r['competition']['events']:
                if e['to_operator']:self.assertGreaterEqual(rational(e['available_capacity_before_award'][e['to_operator']]),e['units'])

    def test_unconstrained_composition_preserves_previous_execution(self):
        old=json.loads(Path('model/results/staffed_renewals.json').read_text())['cases']['binding_staff_cut']
        new=self.cases['qualified_control']
        for key in ('units','opening_treasury','closing_treasury','competition','staffed_renewals','entry_transition','finance'):
            self.assertEqual(old[key],new[key],key)
        self.assertEqual(old['calendar_bridge']['months'],new['calendar_bridge']['months'])

    def test_one_minute_shortage_changes_service_and_actual_contracts(self):
        exact=self.cases['exact_support_through_december'];short=self.cases['one_minute_short_after_notice']
        blocked=[x for x in short['annual_resources']['attempts'] if x['reason']=='annual_support_commitments']
        self.assertEqual(len(blocked),1);b=blocked[0]
        self.assertEqual((b['month'],rational(b['needed_minutes']['support']),rational(b['remaining_before_minutes']['support'])),(5,650,649))
        self.assertEqual(rational(b['committed_minutes']['support']),0)
        self.assertEqual(rational(exact['enterprise']['months'][5]['total_delivered_units']),500)
        self.assertEqual(rational(short['enterprise']['months'][5]['total_delivered_units']),450)
        self.assertNotEqual(exact['competition']['months'][5]['lots'],short['competition']['months'][5]['lots'])
        self.assertEqual(self.rows('one_minute_short_after_notice')[6]['supported_units'],1)
        self.assertEqual(self.summary['one_minute_short_after_notice']['complete_whole_service_months'],7)

    def test_notice_is_prior_observed_success_and_remains_binding_after_shortfall(self):
        for name in ('one_minute_short_after_notice','replacement_qualified_in_january'):
            rows=self.rows(name);r=self.cases[name]
            event=next(x for x in r['staffed_renewals']['events'] if x['issued'])
            self.assertEqual((event['month'],event['based_only_on_completed_month'],event['effective_month']),(3,2,5))
            self.assertTrue(rows[2]['complete_obligation']);self.assertEqual(rows[2]['supported_units'],1)
            self.assertEqual([x['scheduled_blocks'] for x in rows],[2]*5+[1]*3)
            self.assertEqual(rows[5]['supported_units'],0)

    def test_retaining_staff_and_buying_fallback_restore_service_at_different_cost(self):
        bad,keep,ot=(self.summary[n] for n in ('one_minute_short_after_notice','retain_staff_through_support_gap','prepaid_fallback_through_support_gap'))
        self.assertEqual((bad['complete_whole_service_months'],keep['complete_whole_service_months'],ot['complete_whole_service_months']),(7,8,8))
        self.assertEqual(keep['outside_completed_jobs'],ot['outside_completed_jobs'])
        self.assertLess(keep['all_payer_resource_and_transaction_cash_cents'],bad['all_payer_resource_and_transaction_cash_cents'])
        self.assertLess(keep['all_payer_resource_and_transaction_cash_cents'],ot['all_payer_resource_and_transaction_cash_cents'])
        for x in self.rows('prepaid_fallback_through_support_gap'):
            if x['overtime_paid_minutes']:
                self.assertGreaterEqual(x['cash_before_overtime_cents'],x['overtime_cash_paid_cents'])
                self.assertEqual(x['cash_before_overtime_cents']-x['cash_after_overtime_before_awards_cents'],x['overtime_cash_paid_cents'])

    def test_late_qualification_does_not_backfill_due_repair_or_missed_service(self):
        r=self.cases['replacement_qualified_in_january'];rows=self.rows('replacement_qualified_in_january')
        self.assertEqual([x['supported_units'] for x in rows],[0,0,1,1,0,0,0,1])
        parts=r['component_inventory']['months']
        self.assertEqual(parts[6]['qualified_release']['actuator_h'],1)
        self.assertEqual(parts[6]['service_issued']['actuator_h'],0)
        self.assertEqual(parts[7]['service_issued']['actuator_h'],1)
        self.assertEqual(self.summary['replacement_qualified_in_january']['complete_whole_service_months'],6)
        self.assertEqual(rational(self.summary['replacement_qualified_in_january']['accepted_zones']),3900)

    def test_unqualified_manufacturing_does_not_trigger_a_staff_cut(self):
        r=self.cases['unqualified_board_no_notice']
        self.assertFalse(r['units']);self.assertTrue(all(x['notice_issued_month'] is None for x in self.rows('unqualified_board_no_notice')))
        self.assertEqual(r['component_inventory']['closing_quarantined_parts']['embedded_lpddr_boards'],1)
        self.assertEqual(self.summary['unqualified_board_no_notice']['staff_paid_cents'],4800000)

    def test_strong_human_comparator_serves_same_required_work_with_lower_resource_cash(self):
        a,b=(self.summary[k] for k in ('qualified_control','human_only_same_service'))
        for key in ('accepted_zones','outside_required_jobs','outside_completed_jobs','complete_whole_service_months'):self.assertEqual(a[key],b[key])
        self.assertLess(b['all_payer_resource_and_transaction_cash_cents'],a['all_payer_resource_and_transaction_cash_cents'])

    def test_equal_robot_access_does_not_duplicate_shared_provider_resources(self):
        r=self.cases['equal_robot_access_shared_support']
        self.assertEqual(len(r['units']),2)
        self.assertEqual({x['operator_id'] for x in r['units']},{'incumbent','entrant'})
        self.assertEqual(rational(r['annual_resources']['calendar_years'][0]['resources']['support']['booked_here_minutes']),2600)
        self.assertEqual(self.summary['equal_robot_access_shared_support']['annual_blocked_bookings'],4)
        self.assertEqual(len({w['resource_id'] for w in r['staffed_renewals']['inputs'].values()}),2)

    def test_blocked_support_does_not_consume_replacement_or_future_year_capacity(self):
        r=run_qualified_staffing_case({'resources':available_support(1300)})
        for month in (4,5):
            self.assertEqual(r['component_inventory']['months'][month]['service_issued']['actuator_h'],0)
            self.assertEqual(r['component_inventory']['months'][month]['qualified_closing']['actuator_h'],1)
        self.assertEqual(r['component_inventory']['months'][6]['service_issued']['actuator_h'],1)

    def test_complete_replay_ignores_all_derived_ledgers(self):
        for name,r in self.cases.items():
            saved=copy.deepcopy(r)
            for section in ('annual_resources','component_inventory','staffed_renewals'):saved[section]['months']=[]
            saved['closing_treasury']={};saved['case_hash']='forged';saved['competition']['events']=[]
            self.assertEqual(replay_qualified_staffing(saved),r,name)

    def test_missing_or_incompatible_contracts_fail_explicitly(self):
        for inputs in ([],{'resources':{}},{'staffed':[]},{'staffed':{'crews':None}}, {'components':{}}, {'resources':{'years':[{'calendar_year':2026}]}}, {'unknown':0}):
            with self.assertRaises((ValueError,TypeError)):run_qualified_staffing_case(inputs)
        saved=copy.deepcopy(self.cases['qualified_control']);saved['component_inventory']['inputs']['onboard_configuration']='high_memory'
        with self.assertRaises(ValueError):replay_qualified_staffing(saved)
        saved=copy.deepcopy(self.cases['qualified_control']);del saved['annual_resources']
        with self.assertRaises(ValueError):replay_qualified_staffing(saved)

if __name__=='__main__':unittest.main()
