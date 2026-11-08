"""Funded robot title, owner sale and actual renewal after company entry.

One physical/Treasury execution. Company shares, physical title, debt claims and
customer contracts are distinct registers, including under common ownership.
"""
from dataclasses import replace
from fractions import Fraction
import hashlib,json

from model.asset_recovery import RecoveryHooks,RecoveryPolicy,add_recovery_sections
from model.renewing_entry import (_RenewingEntry,renewing_entry_inputs,
    add_entry_renewal_sections,source_hashes as entry_hashes)
from model.entry_transitions import Transition,bounded_int
from model.competitive_renewals import Competition
from model.calendar_bridge import ROOT,Bridge,bridge_context,exact,rational
from model.enterprise_finance import FinancePlan,TermLoan
from model.monthly_enterprise import Business,CustomerMove,EnterprisePlan,Equity,Market
from model.monthly_commercial import restore_opening_inputs
from model.monthly_deployment import run_monthly,_rational
from model.monthly_architectures import canonical_wire


class _RecoveringEntry(RecoveryHooks,_RenewingEntry):
    def __init__(self,plan,contracts,treasury,enterprise,finance,bridge,competition,transition,recovery):
        super().__init__(plan,contracts,treasury,enterprise,finance,bridge,competition,transition)
        self.initialize_recovery(plan,contracts,treasury,enterprise,finance,bridge,recovery)

    def close(self,t,month,units,supported):
        super().close(t,month,units,supported)
        # A unit started this month has not reached the next prepare() snapshot.
        # Use the commercial ledger's actual WIP/provider title, not an absent
        # entry in the recovery policy's prior-unit owner map.
        asset=next((a for a in self.months[-1]['assets'] if a['unit_id']==self.recovery.unit_id),None)
        if asset is not None:self.recovery_months[-1]['title_owner']=asset['title_owner']


def source_hashes():
    return {**entry_hashes(),**{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest()
        for p in ('model/asset_recovery.py','model/recovering_entry.py')}}


def run_recovering_entry(plan,treasury,contracts,enterprise,finance,bridge,competition,transition,recovery):
    policy=_RecoveringEntry(plan,contracts,treasury,enterprise,finance,bridge,competition,transition,recovery)
    r=run_monthly(plan,treasury,commercial=policy)
    r.update(schema_version='recovering-entry-window/0.1',scope='synthetic_funded_title_recovery_entry_and_actual_renewal',
        ownership='legal_robot_title_distinct_from_company_equity_customer_contracts_and_credit_claims')
    add_entry_renewal_sections(policy,r);add_recovery_sections(policy,r,recovery)
    r['commercial']['limits']=['See recovering_entry, asset_recovery, renewing_entry, entry_transition, competition and finance scopes.']
    r['renewing_entry']['limits']=[x for x in r['renewing_entry']['limits'] if not x.startswith('No shared site crew')]+[
        'Eligible recovery is explicitly added on this one execution; shared crew, annual resource commitments, typed parts, four-architecture execution and endogenous learning remain separate.']
    r['entry_transition']['limits']=[x for x in r['entry_transition']['limits'] if not x.startswith('Synthetic share purchase only')]+[
        'Company share purchase and a separately eligible funded owner-asset sale are modeled. No debt novation, vendor rights grant, legal/tax opinion or valuation is inferred.']
    r['asset_recovery']['limits']=[x for x in r['asset_recovery']['limits'] if not x.startswith('The old operating company retains')]+[
        'The seller retains staffing, payables, credit claims and legal identity. Asset sale alone moves no customer contract; subsequent dated renewal may independently reassign service.']
    rows=[]
    for service,debt,asset,entry,joint,market in zip(r['enterprise']['months'],r['finance']['months'],
            r['asset_recovery']['months'],r['entry_transition']['months'],r['renewing_entry']['months'],r['competition']['months']):
        rows.append(dict(month=service['month'],accepted_zones=service['total_delivered_units'],
            unserved_zones=_rational(Fraction(enterprise.market.baseline_units)-rational(service['total_delivered_units'])),
            ultimate_owners=entry['ultimate_owners'],title_owner=asset['title_owner'],
            physical_state=asset['physical_state'],operator_id=asset['operator_id'],supported=asset['supported'],
            seller_defaulted=asset['seller_defaulted'],seller_principal_claim_cents=asset['seller_principal_claim_cents'],
            target_due_unpaid_cents=entry['target_due_unpaid_cents'],
            assigned_units={op:sum(lot['units'] for lot in market['lots'] if lot['owner']==op) for op in ('incumbent','entrant')},
            new_platform_contract_units=joint['new_platform_contract_units'],intra_platform_reassigned_units=joint['intra_platform_reassigned_units']))
    title_events=[e for e in r['commercial']['events'] if e['action']=='shipment_title' and e.get('unit_id')==recovery.unit_id]
    ids={e['purchase_invoice_id'] for e in title_events}
    original=[i for i in r['closing_treasury']['invoices'] if i['invoice_id'] in ids]
    r['recovering_entry']=dict(schema_version='recovering-entry-boundary/0.1',months=rows,
        original_hardware_purchase_invoices=original,original_shipment_title_events=title_events,
        any_opening_installed_units=any(o['opening_installed'] for o in r['plan']['operators']),
        outside_customer_switch_resource_cash_cents=r['competition']['buyer_switch_resource_cash_cents'],
        all_payer_resource_and_transaction_cash_cents=r['entry_transition']['consolidation']['external_operating_and_transaction_cash_cents']+r['competition']['buyer_switch_resource_cash_cents'],
        title_basis='Original shipment title requires actual hardware purchase; equity close is a separate event. Full replay retains the supplied opening-asset basis, if any.',
        event_clock='Debt settlement precedes current sale. Sale receipts cannot cure an already evaluated default until later scheduled servicing. Customer renewals follow funded physical admission; prior missed service remains missed.',
        limits=['Declared sale price, release and configuration rights are synthetic inputs; no enforceability, repossession, secured priority or market value is inferred.',
            'Common ultimate ownership does not pool legal bank accounts or automatically move customer contracts. The internal asset price cancels only inside the fixed consolidated boundary.',
            'Original manufacture and purchased title, retained staff/software, relocation, later qualification and claims remain in the same history. A commissioned robot can add no service if funded humans already cover demand.',
            'These fixed financing/offer/recovery rules are not optimal capital allocation, group pricing or restructuring. No dividends, terminal asset values, payroll removal or lifecycle ROI.',
            'The complete six-cell portfolio, shared-workforce, annual-resource, typed-component, architecture and learning contracts have not all been joined to this execution.'])
    r['source_sha256']=source_hashes();r=canonical_wire(r)
    r['case_hash']=hashlib.sha256(json.dumps(r,sort_keys=True,separators=(',',':')).encode()).hexdigest()
    return json.loads(json.dumps(r))


DEFAULTS=dict(entry={},source_arrangement='sale',target_loan_cents=6_000_000,
    maturity_month=4,monthly_rate_basis_points=0,buyer_full_human_staff=False,recovery={})
RECOVERY_DEFAULTS=dict(unit_id='start-shared-supply-1',seller_actor='incumbent',buyer_operator='entrant',
    offer_month=4,price_cents=3_000_000,relocation_cents=100_000,relocation_months=2)


def recovering_entry_inputs(inputs=None):
    if inputs is None:inputs={}
    if not isinstance(inputs,dict) or set(inputs)-set(DEFAULTS):raise ValueError('Unknown recovering-entry inputs')
    x={**DEFAULTS,**inputs}
    if not isinstance(x['entry'],dict) or not isinstance(x['recovery'],dict):raise ValueError('Entry and recovery controls must be objects')
    if x['source_arrangement'] not in ('sale','lease') or type(x['buyer_full_human_staff']) is not bool:raise ValueError('Explicit title contract and staffing Boolean required')
    for key in ('target_loan_cents','maturity_month','monthly_rate_basis_points'):bounded_int(x[key])
    if not 1<=x['maturity_month']<=24 or x['monthly_rate_basis_points']>10000:raise ValueError('Bounded loan maturity and rate required')
    entry=dict(x['entry']);market=entry.get('market',{})
    if not isinstance(market,dict):raise ValueError('Market controls must be an object')
    if set(market)&{'incumbent_robots','entrant_robots'}:raise ValueError('This fixture produces one target robot and no entrant robot; use full replay for other explicit plans')
    entry['market']={**market,'incumbent_robots':1,'entrant_robots':0}
    p,t,cs,e,_,b,c,tr=renewing_entry_inputs(entry)
    p=replace(p,plan_id='recovering-company-entry')
    cs=tuple(replace(v,arrangement=x['source_arrangement'] if v.operator_id=='incumbent' else 'sale',
        lessor_actor='lessor' if v.operator_id=='incumbent' and x['source_arrangement']=='lease' else None) for v in cs)
    t=replace(t,accounts=tuple(replace(a,opening_cash_cents=max(a.opening_cash_cents,x['target_loan_cents'])) if a.actor_id=='capital_lender' else a for a in t.accounts))
    f=FinancePlan((TermLoan('target-asset-finance','capital_lender','incumbent',x['target_loan_cents'],0,x['maturity_month'],x['monthly_rate_basis_points'],10000),) if x['target_loan_cents'] else ())
    if x['buyer_full_human_staff']:
        _,_,_,cell,_,calendar=bridge_context(b,p.months)
        staff=next(v.human_staff_cents_by_month for v in e.businesses if v.operator_id=='incumbent')
        capacity=tuple(int(Fraction(staff[row['month']],100)/exact(cell['wage_usd_hour'])/exact(cell['human_hours_per_unit'])/(1-exact(row['effective_parameters']['digital_efficiency']))) for row in calendar)
        e=replace(e,businesses=tuple(replace(v,human_staff_cents_by_month=staff,human_capacity_by_month=capacity) if v.operator_id=='entrant' else v for v in e.businesses))
    rp=RecoveryPolicy(**{**RECOVERY_DEFAULTS,**x['recovery']})
    return p,t,cs,e,f,b,c,tr,rp


def run_recovering_entry_case(inputs=None):return run_recovering_entry(*recovering_entry_inputs(inputs))


def replay_recovering_entry(saved):
    if not isinstance(saved,dict) or saved.get('schema_version')!='recovering-entry-window/0.1':raise ValueError('Complete recovering-entry case required')
    try:
        e=dict(saved['enterprise']['inputs']);e['market']=Market(**e['market'])
        for key,cls in [('businesses',Business),('moves',CustomerMove),('equity',Equity)]:e[key]=tuple(cls(**x) for x in e[key])
        f=dict(saved['finance']['inputs']);f['loans']=tuple(TermLoan(**x) for x in f['loans'])
        return run_recovering_entry(*restore_opening_inputs(saved),EnterprisePlan(**e),FinancePlan(**f),
            Bridge(**saved['calendar_bridge']['inputs']),Competition(**saved['competition']['inputs']),
            Transition(**saved['entry_transition']['inputs']),RecoveryPolicy(**saved['asset_recovery']['inputs']))
    except (KeyError,TypeError) as exc:raise ValueError('Complete valid recovering-entry inputs required') from exc


def recovering_entry_worlds():
    return {'funded_owner_sale':{},'no_asset_sale':{'recovery':{'enabled':False}},
        'low_sale_proceeds':{'recovery':{'price_cents':2_000_000}},
        'leased_title_refused':{'source_arrangement':'lease'},
        'configuration_rights_unavailable':{'recovery':{'transfer_rights':False}},
        'exact_buyer_funding':{'entry':{'growth_equity_cents':4_605_000}},
        'one_cent_short':{'entry':{'growth_equity_cents':4_604_999}},
        'qualification_unavailable':{'recovery':{'qualification_eligible':False}},
        'arrival_after_horizon':{'recovery':{'relocation_months':5}},
        'prior_target_equity':{'entry':{'transition':{'target_equity_cents':3_000_000}}},
        'locked_customer_commitments':{'entry':{'market':{'competition':{'term_months':3,'breach_exit':False}}}},
        'paid_human_buyer_sale':{'buyer_full_human_staff':True},
        'paid_human_buyer_no_sale':{'buyer_full_human_staff':True,'recovery':{'enabled':False}}}


def recovering_entry_summary(name,r):
    rows=r['recovering_entry']['months'];a=r['asset_recovery']['summary']
    return dict(case=name,**a,complete_months=sum(rational(m['unserved_zones'])==0 for m in rows),
        target_first_default=next((m['month'] for m in rows if m['seller_defaulted']),None),
        target_first_cure_after_sale=next((m['month'] for m in rows if m['month']>r['asset_recovery']['inputs']['offer_month'] and not m['seller_defaulted']),None) if a['sale_completed'] else None,
        parent_closing_cash_cents=r['entry_transition']['cash']['buyer_closing_cents'],
        equity_reclassified_contract_units=sum(x['units'] for x in r['renewing_entry']['contracts_reclassified_at_share_close']),
        new_platform_contract_units=sum(m['new_platform_contract_units'] for m in r['renewing_entry']['months']),
        external_operating_and_transaction_cash_cents=r['entry_transition']['consolidation']['external_operating_and_transaction_cash_cents'],
        all_payer_resource_and_transaction_cash_cents=r['recovering_entry']['all_payer_resource_and_transaction_cash_cents'],case_hash=r['case_hash'])


def recovering_entry_artifact():
    options=recovering_entry_worlds();cases={name:run_recovering_entry_case(x) for name,x in options.items()}
    return dict(schema_version='recovering-entry-artifact/0.1',case_inputs=options,cases=cases,
        summary=[recovering_entry_summary(name,r) for name,r in cases.items()],source_sha256=source_hashes(),
        comparison_boundary='One newly manufactured and paid robot, actual legal title, funded owner transfer and later qualification share the company-entry/renewal history. Cash cure, physical reuse and customer retention are separate. No free opening asset, optimal restructuring or ROI.')


def recovering_entry_catalog():
    data=json.loads((ROOT/'model/results/recovering_entry.json').read_text())
    if data['source_sha256']!=source_hashes():raise ValueError('Recovering-entry export is stale; regenerate')
    return {k:v for k,v in data.items() if k!='cases'}|{'cases':{'funded_owner_sale':data['cases']['funded_owner_sale']}}
