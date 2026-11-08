"""Share closing and actual customer renewal on one physical/cash execution.

Common ownership keeps separately declared offer mandates. No independent-firm
competition, optimized group pricing, acquisition synergy or valuation is implied.
"""
from dataclasses import asdict, replace
from fractions import Fraction
from pathlib import Path
import hashlib
import json

from model.calendar_bridge import ROOT, Bridge, rational, bridge_context, exact
from model.competitive_renewals import (Competition, _CompetitiveEnterprise,
    competitive_case_inputs, source_hashes as competition_hashes)
from model.entry_transitions import EntryTransitionHooks, Transition, BUYER, SELLER, VENDOR, bounded_int
from model.enterprise_finance import FinancePlan, TermLoan
from model.monthly_commercial import restore_opening_inputs
from model.monthly_deployment import _rational, run_monthly
from model.monthly_enterprise import Business, CustomerMove, EnterprisePlan, Equity, Market
from model.monthly_architectures import canonical_wire
from model.treasury import Account, Moment


class _RenewingEntry(EntryTransitionHooks, _CompetitiveEnterprise):
    def __init__(self,plan,contracts,treasury,enterprise,finance,bridge,competition,transition):
        super().__init__(plan,contracts,treasury,enterprise,finance,bridge,competition)
        self.initialize_entry(plan,contracts,treasury,enterprise,finance,bridge,transition)
        self.group_months=[];self.reclassified_lots=[];self.platform_seen=set()

    def validate_opening_obligations(self,treasury):
        target=self.business['incumbent'].actor_id
        if any(i.category!='entry_opening_target_payable' or i.payer!=target or
               i.payee!=self.enterprise.enterprise_vendor_actor or i.cancellable for i in treasury.invoices):
            raise ValueError('Only explicit mandatory inherited target resource payables are supported')

    def collect(self,t,month):
        before=[dict(lot) for lot in self.lots]
        t=super().collect(t,month)
        if self.closed_month==month:
            self.reclassified_lots=[dict(month=month,phase=2,lot_id=x['lot_id'],units=x['units'],
                legal_operator=x['owner'],locked_cents_per_unit=x['price_cents'],expires_month=x['expires_month'],
                previous_ultimate_owner=SELLER,new_ultimate_owner=BUYER) for x in before if x['owner']=='incumbent']
            self.platform_seen.update(x['lot_id'] for x in self.reclassified_lots)
        return t

    def close(self,t,month,units,supported):
        super().close(t,month,units,supported)
        owned=[op for op,owner in self.owners.items() if owner==BUYER]
        lots=[x for x in self.renewal_months[-1]['lots'] if x['owner'] in owned]
        events=[x for x in self.renewal_events if x['month']==month and x['from_operator']!=x['to_operator']]
        new=[x for x in events if x['to_operator'] in owned and x['lot_id'] not in self.platform_seen]
        self.group_months.append(dict(month=month,ultimate_owners=dict(self.owners),
            common_owner_of_active_firms=all(self.owners[op]==BUYER and self.active(b,month) for op,b in self.business.items()),
            platform_assigned_units=sum(x['units'] for x in lots),
            platform_delivered_zones=_rational(sum((rational(x['delivered_units']) for x in lots),Fraction())),
            outside_or_unassigned_award_units=sum(x['units'] for x in events if x['to_operator'] in owned and x['from_operator'] not in owned),
            new_platform_contract_units=sum(x['units'] for x in new),new_platform_contract_lot_ids=[x['lot_id'] for x in new],
            intra_platform_reassigned_units=sum(x['units'] for x in events if x['to_operator'] in owned and x['from_operator'] in owned),
            separately_funded_accounts={self.business[op].actor_id:t.balance(self.business[op].actor_id) for op in owned},
            parent_available_cash_cents=t.available(BUYER)))
        self.platform_seen.update(x['lot_id'] for x in lots)

    def joint_result(self):
        return dict(schema_version='renewing-entry-boundary/0.1',months=self.group_months,
            contracts_reclassified_at_share_close=self.reclassified_lots,
            offer_authority='Operating companies retain separate declared offer mandates after common ownership. This is not independent competition or optimized group pricing.',
            service_boundary='One conserved baseline with actual funded awards, locked prices and prior service; share closing alone does not create demand, accepted work or a new customer win.',
            information_clock='Atomic share close in phase2 precedes physical work and phase5 renewals. Awards use current funded capacity and prior realized service. Future outcomes are not consulted.',
            limits=['Parent, target and growth-company accounts remain separate. Target cash never funds the parent share purchase.',
                'Inherited mandatory target bills survive. Share closing and later contract renewal are different events.',
                'Common-owner contract transfers are internal reassignment, not new platform customer wins; equity reclassification is separately reported at the actual closing moment.',
                'Fixed separate offer mandates under common ownership are a declared scenario, not real competition, antitrust advice or an optimal parent policy.',
                'No shared site crew, annual resource commitments, typed parts, four-architecture execution, asset recovery or endogenous learning is added to this joint fixture.',
                'Gross awards from outside/unassigned contracts include regained work; newly acquired contract-lot IDs exclude earlier platform ownership and equity reclassification. Neither metric counts unique people.',
                'Window payments, customer assignments and paid diligence do not identify company value, distributable return or whole-service lifecycle economics.'])


def source_hashes():
    paths=('model/entry_transitions.py','model/renewing_entry.py','model/monthly_architectures.py')
    return {**competition_hashes(),**{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in paths}}


def run_renewing_entry(plan,treasury,contracts,enterprise,finance,bridge,competition,transition):
    policy=_RenewingEntry(plan,contracts,treasury,enterprise,finance,bridge,competition,transition)
    r=run_monthly(plan,treasury,commercial=policy)
    r.update(schema_version='renewing-entry-window/0.1',scope='synthetic_share_acquisition_and_actual_contract_renewal',ownership='legal_asset_title_separate_from_ultimate_equity_and_customer_contract_assignment')
    r['commercial']=policy.result(r);r['commercial']['limits']=['See renewing_entry, entry_transition, competition and finance scopes.']
    r['enterprise']=policy.enterprise_result(r);r['enterprise']['limits']=['One fixed recurring market with dated company acquisition and separate mandated offers; see joint boundary.']
    r['finance']=policy.finance_result(r);r['calendar_bridge']=policy.bridge_result(r)
    r['competition']=policy.competition_result(r);r['entry_transition']=policy.entry_result(r);r['renewing_entry']=policy.joint_result()
    r['entry_transition']['legal_contract']='Share closing changes ultimate equity ownership only; legal accounts, assets, existing customer contracts and obligations remain. Ordinary subsequent renewal may separately reassign service.'
    assert r['entry_transition']['consolidation']['unclassified_boundary_cash_cents']==0
    assert r['finance']['consolidation']['unclassified_other_boundary_cash_cents']==0
    assert sum(a['cash_cents'] for a in r['opening_treasury']['actors'])==sum(a['cash_cents'] for a in r['closing_treasury']['actors'])
    r['source_sha256']=source_hashes();r=canonical_wire(r)
    r['case_hash']=hashlib.sha256(json.dumps(r,sort_keys=True,separators=(',',':')).encode()).hexdigest()
    return json.loads(json.dumps(r))


DEFAULTS=dict(mode='hybrid',buyer_cash_cents=20_000_000,target_cash_cents=2_500_000,
    growth_equity_cents=6_000_000,target_opening_payable_cents=0,transition={},market={},human_efficiency=None)


def renewing_entry_inputs(inputs=None):
    if inputs is None:inputs={}
    if not isinstance(inputs,dict) or set(inputs)-set(DEFAULTS):raise ValueError('Unknown renewing-entry inputs')
    x={**DEFAULTS,**inputs}
    for key in ('buyer_cash_cents','target_cash_cents','growth_equity_cents','target_opening_payable_cents'):bounded_int(x[key])
    for key in ('transition','market'):
        if not isinstance(x[key],dict):raise ValueError(key+' must be an object')
    if 'mode' in x['transition']:raise ValueError('Specify mode once at the top level')
    tr=Transition(mode=x['mode'],**x['transition']);growth=tr.mode in ('build','hybrid')
    if set(x['market'])&{'months','incumbent_cash_cents','entrant_cash_cents','extra_equity_cents','loan_cents'}:
        raise ValueError('Eight months, separate entry funding and no fixture loans are explicit')
    cfg={**x['market'],'months':8,'incumbent_cash_cents':x['target_cash_cents'],'entrant_cash_cents':0,
         'entrant_robots':x['market'].get('entrant_robots',2) if growth else 0,'extra_equity_cents':0,'loan_cents':0}
    p,t,cs,e,f,b,c=competitive_case_inputs(cfg)
    p=replace(p,plan_id='renewing-company-entry')
    t=replace(t,accounts=t.accounts+(Account(BUYER,x['buyer_cash_cents']),Account(SELLER,0),Account(VENDOR,0)))
    e=replace(e,businesses=tuple(replace(v,active_from_month=0 if growth else None) if v.operator_id=='entrant' else v for v in e.businesses),
        equity=(Equity('fund-separate-growth',0,BUYER,'entrant',x['growth_equity_cents']),) if growth and x['growth_equity_cents'] else ())
    if x['target_opening_payable_cents']:
        t=t.issue_invoice('opening-target-payable:issue','opening-target-payable','incumbent','enterprise_vendor',x['target_opening_payable_cents'],
            Moment(0,1),Moment(2,3),Moment(2,3),provenance='synthetic_existing_target_obligation',category='entry_opening_target_payable')
    if x['human_efficiency'] is not None:
        value=x['human_efficiency']
        if type(value) not in (int,float) or not 0<=value<=.9:raise ValueError('Explicit bounded human efficiency required')
        b=replace(b,annual_overrides={**b.annual_overrides,'digital_efficiency':value})
        _,_,_,cell,_,calendar=bridge_context(b,p.months)
        e=replace(e,businesses=tuple(replace(v,human_capacity_by_month=tuple(
            int(Fraction(v.human_staff_cents_by_month[row['month']],100)/exact(cell['wage_usd_hour'])/
                exact(cell['human_hours_per_unit'])/(1-exact(row['effective_parameters']['digital_efficiency'])))
            for row in calendar)) for v in e.businesses))
    return p,t,cs,e,f,b,c,tr


def run_renewing_entry_case(inputs=None):return run_renewing_entry(*renewing_entry_inputs(inputs))


def replay_renewing_entry(saved):
    if not isinstance(saved,dict) or saved.get('schema_version')!='renewing-entry-window/0.1':raise ValueError('Complete renewing-entry case required')
    try:
        e=dict(saved['enterprise']['inputs']);e['market']=Market(**e['market'])
        for key,cls in [('businesses',Business),('moves',CustomerMove),('equity',Equity)]:e[key]=tuple(cls(**x) for x in e[key])
        f=dict(saved['finance']['inputs']);f['loans']=tuple(TermLoan(**x) for x in f['loans'])
        return run_renewing_entry(*restore_opening_inputs(saved),EnterprisePlan(**e),FinancePlan(**f),Bridge(**saved['calendar_bridge']['inputs']),
            Competition(**saved['competition']['inputs']),Transition(**saved['entry_transition']['inputs']))
    except (KeyError,TypeError,AttributeError) as exc:raise ValueError('Incomplete renewing-entry inputs') from exc


def renewing_entry_worlds():
    return {
        'status_quo':{'mode':'status_quo'},'standalone_build':{'mode':'build'},'share_acquisition':{'mode':'acquire'},'hybrid':{},
        'hybrid_interruption':{'transition':{'disruption_months':1}},
        'hybrid_locked_interruption':{'transition':{'disruption_months':1},'market':{'competition':{'term_months':3,'breach_exit':False}}},
        'hybrid_failed_close':{'buyer_cash_cents':16_000_000},
        'inherited_target_liability':{'target_opening_payable_cents':3_000_000},
        'funded_target_liability':{'target_opening_payable_cents':3_000_000,'transition':{'target_equity_cents':3_000_000}},
        'human_competitive_response':{'mode':'build','human_efficiency':.25,'market':{'incumbent_robots':0,'entrant_robots':0,'competition':{'response_mode':'calendar_human'}}},
    }


def renewing_entry_summary(name,r):
    a=r['entry_transition'];g=r['renewing_entry'];rows=r['enterprise']['months']
    return dict(case=name,close_status=a['close_status'],accepted_zones=_rational(sum((rational(m['total_delivered_units']) for m in rows),Fraction())),
        complete_months=sum(rational(m['total_delivered_units'])==r['enterprise']['inputs']['market']['baseline_units'] for m in rows),
        equity_reclassified_contract_units=sum(x['units'] for x in g['contracts_reclassified_at_share_close']),
        outside_or_unassigned_award_units=sum(x['outside_or_unassigned_award_units'] for x in g['months']),
        new_platform_contract_units=sum(x['new_platform_contract_units'] for x in g['months']),
        intra_platform_reassigned_units=sum(x['intra_platform_reassigned_units'] for x in g['months']),
        final_platform_assigned_units=g['months'][-1]['platform_assigned_units'],**a['cash'],
        external_operating_and_transaction_cash_cents=a['consolidation']['external_operating_and_transaction_cash_cents'],case_hash=r['case_hash'])


def renewing_entry_artifact():
    options=renewing_entry_worlds();cases={k:run_renewing_entry_case(x) for k,x in options.items()}
    return canonical_wire(dict(schema_version='renewing-entry-artifact/0.1',case_inputs=options,cases=cases,
        summary=[renewing_entry_summary(k,r) for k,r in cases.items()],source_sha256=source_hashes(),
        comparison_boundary='One conserved recurring market and one physical/Treasury run. Share closing reclassifies ownership; actual renewal changes firm contracts. Parent and operating cash stay separate. Common ownership uses fixed separate offer mandates, not independent competition or optimized pricing. No terminal value or ROI.'))


def renewing_entry_catalog():
    data=json.loads((ROOT/'model/results/renewing_entry.json').read_text())
    if data['source_sha256']!=source_hashes():raise ValueError('Renewing-entry export is stale; regenerate')
    return {k:v for k,v in data.items() if k!='cases'}|{'cases':{'hybrid':data['cases']['hybrid']}}
