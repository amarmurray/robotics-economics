"""Expansion can consume support cash; forecasts cannot guarantee future service."""
import copy
from dataclasses import replace
from fractions import Fraction
import json
import random
import unittest
from pathlib import Path
from model.calendar_bridge import rational
from model.monthly_deployment import Start
from model.support_expansion import (ExpansionPolicy, expansion_case_inputs, replay_expansion,
                                     run_expansion_case, run_support_expansion)


class SupportExpansion(unittest.TestCase):
    @classmethod
    def setUpClass(cls):cls.cases=json.loads(Path('model/results/support_expansion.json').read_text())['cases']
    def result(self,name):return self.cases[name]['support_expansion']
    def accepted(self,name):return rational(self.result(name)['summary']['accepted_zones'])

    def assert_conserved(self,r):
        self.assertEqual(sum(x['cash_cents'] for x in r['opening_treasury']['actors']),sum(x['cash_cents'] for x in r['closing_treasury']['actors']))
        self.assertEqual(r['finance']['consolidation']['unclassified_other_boundary_cash_cents'],0)
        self.assertEqual(len(r['units']),len({x['unit_id'] for x in r['units']}))
        requested=sum(o['requested_additions'] for o in r['plan']['operators'])
        self.assertLessEqual(sum(u['origin']!='opening_stock' and u['status']!='rejected' for u in r['units']),requested)
        for m,e in zip(r['support_expansion']['months'],r['enterprise']['months']):
            self.assertLessEqual(rational(m['support_and_qualification_hours_used']),m['actual_support_hours'])
            self.assertLessEqual(rational(m['integration_hours_used']),r['calendar_bridge']['inputs']['integration_hours_per_month'])
            self.assertEqual(m['accepted_service_units'],e['total_delivered_units'])
            self.assertLessEqual(rational(m['accepted_service_units']),r['enterprise']['inputs']['market']['baseline_units'])
            for p in e['pools'].values():
                self.assertEqual(sum(x['units'] for x in p['assignments']),p['recurring_demand_units'])
                self.assertEqual(rational(p['delivered_units'])+rational(p['unserved_units']),p['recurring_demand_units'])
        invoices={i['invoice_id']:i for i in r['closing_treasury']['invoices']}
        for event in r['support_expansion']['events']:
            i=invoices[event['invoice_id']]
            if event['status']=='blocked':self.assertEqual(i['paid_cents'],0)
            else:
                self.assertEqual(i['paid_cents'],i['face_cents'])
                self.assertLessEqual(event['committed_growth_units']+event['candidate_units'],event['fixed_requested_growth_units'])
                if event['policy']!='funded_only':
                    self.assertLessEqual(rational(event['planned_fleet_support_hours']),event['planning_support_hours'])
                    self.assertGreaterEqual(event['cash_after_start_before_other_future_obligations_cents'],event['required_payer_reserve_cents'])
            self.assertEqual(i['outstanding_cents'],0)
            self.assertFalse(event['future_actual_support_consulted'])

    def test_all_worlds_conserve_demand_units_cash_and_actual_resources(self):
        for r in self.cases.values():self.assert_conserved(r)

    def test_current_capacity_caution_delays_service_against_credible_announcement(self):
        a=self.result('announced_capacity_reserve');b=self.result('funded_only');c=self.result('current_capacity_reserve')
        admitted=lambda x:[e['month'] for e in x['events'] if e['status']=='admitted']
        self.assertEqual(admitted(a),[2]);self.assertEqual(admitted(b),[0]);self.assertEqual(admitted(c),[4])
        self.assertEqual(self.accepted('announced_capacity_reserve'),self.accepted('funded_only'))
        self.assertGreater(self.accepted('announced_capacity_reserve'),self.accepted('current_capacity_reserve'))
        for x in (a,b,c):self.assertEqual(x['summary']['opening_cohort_supported_unit_months'],16)

    def test_future_realized_allocation_is_not_known_to_earlier_decisions(self):
        a=self.cases['announced_capacity_reserve'];b=self.cases['announced_increase_fails']
        self.assertEqual(a['plan'],b['plan'])
        self.assertEqual(a['support_expansion']['events'][:4],b['support_expansion']['events'][:4])
        self.assertEqual(a['months'][:4],b['months'][:4])
        self.assertEqual(b['support_expansion']['summary']['funded_starts'],1)
        self.assertEqual(b['support_expansion']['summary']['commissioned_new_units'],0)
        self.assertTrue(any(u['origin']!='opening_stock' and u['status']=='transit' for u in b['units']))
        self.assertGreater(self.accepted('announced_capacity_reserve'),self.accepted('announced_increase_fails'))

    def test_cash_reserve_preserves_installed_service_in_thin_provider_world(self):
        a=self.result('thin_provider_funded_only');b=self.result('thin_provider_reserve')
        self.assertEqual(a['summary']['funded_starts'],1);self.assertEqual(b['summary']['funded_starts'],0)
        self.assertEqual(a['summary']['opening_cohort_supported_unit_months'],14)
        self.assertEqual(b['summary']['opening_cohort_supported_unit_months'],16)
        self.assertGreater(self.accepted('thin_provider_reserve'),self.accepted('thin_provider_funded_only'))
        self.assertTrue(any(e['reason']=='installed_and_growth_cash_reserve' for e in b['events']))

    def test_reserve_has_exact_one_cent_boundary_after_paid_current_support(self):
        a=self.result('exact_initial_reserve')['events'][0];b=self.result('one_cent_below_reserve')['events'][0]
        self.assertEqual(a['required_payer_reserve_cents'],504774)
        self.assertEqual(a['cash_after_start_before_other_future_obligations_cents'],504774)
        self.assertEqual(b['cash_after_start_before_other_future_obligations_cents'],504773)
        self.assertEqual(a['status'],'admitted');self.assertEqual(b['reason'],'installed_and_growth_cash_reserve')
        self.assertGreater(self.accepted('exact_initial_reserve'),self.accepted('one_cent_below_reserve'))
        self.assertEqual(a['expected_commission_month_without_delays'],2)
        unit=next(u for u in self.cases['exact_initial_reserve']['units'] if u['origin']!='opening_stock')
        self.assertEqual(unit['commissioned_at']['month'],5)
        blocked=[e['at']['month'] for e in self.cases['exact_initial_reserve']['events'] if e['action']=='commission' and e['reason']=='funding:commission']
        self.assertEqual(blocked,[2,3,4])

    def test_separate_funded_provider_loan_restores_capacity_and_is_repaid(self):
        r=self.cases['separate_provider_loan'];f=r['finance']['consolidation']
        self.assertEqual(f['loan_draw_cash_cents'],500000);self.assertEqual(f['principal_recovery_cash_cents'],500000)
        self.assertEqual(f['net_financing_cash_cents'],0);self.assertEqual(f['closing_principal_claim_cents'],0)
        self.assertGreater(self.accepted('separate_provider_loan'),self.accepted('thin_provider_reserve'))
        self.assert_conserved(r)

    def test_operator_cash_is_not_replaced_by_provider_cash(self):
        x=self.result('operator_cannot_pay')['summary']
        self.assertEqual(rational(x['accepted_zones']),0)
        self.assertEqual(x['opening_cohort_supported_unit_months'],0)
        self.assertGreater(x['provider_closing_cash_cents'],0)

    def test_rejected_start_preserves_sunk_cost_and_later_distinct_replacement(self):
        a=self.cases['funded_only'];b=self.cases['rejected_start_replacement']
        self.assertEqual(a['support_expansion']['events'][0],b['support_expansion']['events'][0])
        self.assertEqual(b['support_expansion']['summary']['funded_starts'],2)
        self.assertEqual(b['support_expansion']['summary']['rejected_manufactured_units'],1)
        self.assertEqual(b['support_expansion']['summary']['commissioned_new_units'],1)
        self.assertEqual(self.accepted('funded_only'),self.accepted('rejected_start_replacement'))
        self.assertEqual(b['support_expansion']['summary']['external_operating_cash_cents']-a['support_expansion']['summary']['external_operating_cash_cents'],3600000)
        self.assertEqual(len([u for u in b['units'] if u['origin']!='opening_stock']),2)

    def test_actual_component_scarcity_cannot_be_cured_by_financial_or_hour_reserve(self):
        r=self.cases['qualified_component_scarcity']
        self.assertTrue(any('components' in e.get('reason','') for e in r['events']))
        self.assertLess(self.accepted('qualified_component_scarcity'),self.accepted('funded_only'))
        self.assert_conserved(r)

    def test_no_growth_request_cannot_create_units_from_candidate_schedule(self):
        r=self.cases['zero_requested_growth'];self.assertEqual(len(r['units']),2)
        self.assertEqual(r['support_expansion']['summary']['funded_starts'],0)
        self.assertTrue(all(e['reason']=='finite_growth_request_already_committed' for e in r['support_expansion']['events']))

    def test_two_same_phase_candidates_observe_first_committed_unit(self):
        p,t,c,e,f,b,x=expansion_case_inputs({'policy':{'actual_support_hours_by_month':[60]*8,'announced_support_hours_by_month':[60]*8}})
        p=replace(p,plan_id='prefix:start:with-separator',starts=(Start('first:start:qualified',0,1,1),Start('second',0,1,1)))
        r=run_support_expansion(p,t,c,e,f,b,x)
        self.assertEqual([e['status'] for e in r['support_expansion']['events']],['admitted','blocked'])
        self.assertEqual(r['support_expansion']['events'][1]['committed_growth_units'],1)
        self.assert_conserved(r)

    def test_manufacturing_lead_and_commission_ramp_are_actual_physical_states(self):
        a=self.cases['longer_manufacturing_lead'];b=self.cases['announced_capacity_reserve']
        self.assertEqual([e['month'] for e in a['support_expansion']['events'] if e['status']=='admitted'],[0])
        self.assertEqual(self.accepted('longer_manufacturing_lead'),self.accepted('announced_capacity_reserve'))
        for r in (a,b):
            new=next(u for u in r['units'] if u['origin']!='opening_stock');self.assertEqual(new['commissioned_at']['month'],4)
            cohort=next(v for v in r['calendar_bridge']['months'][4]['cohorts'] if v['unit_id']==new['unit_id'])
            self.assertEqual(rational(cohort['ramp_fraction']),Fraction(1,4))

    def test_later_support_reduction_hurts_actual_service_without_retconning_earlier_awards(self):
        a=self.cases['ample_support'];b=self.cases['support_allocation_shrinks']
        self.assertEqual(a['months'][:4],b['months'][:4])
        self.assertLess(self.accepted('support_allocation_shrinks'),self.accepted('ample_support'))
        self.assertEqual(b['support_expansion']['summary']['opening_cohort_supported_unit_months'],12)

    def test_full_replay_ignores_results_and_preserves_all_opening_inputs(self):
        for name,r in self.cases.items():
            saved=copy.deepcopy(r);saved['support_expansion']['summary']={};saved['case_hash']='tampered'
            self.assertEqual(replay_expansion(saved),r,name)
        a=copy.deepcopy(self.cases['ample_support']);b=copy.deepcopy(a)
        a['calendar_bridge']['inputs']['annual_overrides']['years']=3.0;b['calendar_bridge']['inputs']['annual_overrides']['years']=3
        self.assertEqual(replay_expansion(a),replay_expansion(b))

    def test_frozen_cohort_projection_preserves_known_software_prices(self):
        p,t,c,e,f,b,x=expansion_case_inputs()
        b=replace(b,software_policy='frozen_cohort',digital_paths={'schema_version':'digital-annual-paths/0.1','base_year':2026,'epistemic_status':'synthetic_assumption','digital_cost_usd':[1500,3000,4500]})
        r=run_support_expansion(p,t,c,e,f,b,x);m=r['support_expansion']['events'][6]
        self.assertEqual({u['planning_annual_period_index'] for u in m['known_cohort_requirements']},{0})
        self.assertEqual({u['recurring_support_cents'] for u in m['known_cohort_requirements']},{84129})
        self.assertEqual(m['candidate_current_recurring_support_cents_per_unit'],96629)

    def test_invalid_resource_series_policies_and_actor_boundaries_fail(self):
        for x in ({'provider_cash_cents':True},{'requested_growth':5},{'assembly_lead_months':0},{'first_candidate_accepted':1},
                  {'policy':None},{'policy':{'mode':'future_oracle'}},{'policy':{'actual_support_hours_by_month':[60]*7}},
                  {'policy':{'actual_support_hours_by_month':[True]*8}},{'unknown':0}):
            with self.assertRaises((TypeError,ValueError)):run_expansion_case(x)
        p,t,c,e,f,b,x=expansion_case_inputs()
        c=tuple(replace(v,arrangement='sale') for v in c)
        with self.assertRaises(ValueError):run_support_expansion(p,t,c,e,f,b,x)
        with self.assertRaises(ValueError):replay_expansion({})

    def test_seeded_resource_funding_yield_and_lead_worlds(self):
        rng=random.Random(2510)
        for _ in range(10):
            hours=[rng.randrange(15,70) for _ in range(8)]
            r=run_expansion_case({'provider_cash_cents':rng.randrange(2_000_000,20_000_000),
                'requested_growth':rng.randrange(4),'service_receipt_lag':rng.randrange(1,5),
                'first_candidate_accepted':bool(rng.randrange(2)),'assembly_lead_months':rng.randrange(1,4),
                'policy':{'mode':rng.choice(['funded_only','current_capacity_reserve','announced_capacity_reserve']),
                          'actual_support_hours_by_month':hours,'announced_support_hours_by_month':[60]*8}})
            self.assert_conserved(r)


if __name__=='__main__':unittest.main()
