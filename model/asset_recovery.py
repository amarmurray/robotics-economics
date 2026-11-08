"""Declared, funded asset sale and relocation after customer-owner default.

Synthetic transaction policy, not insolvency law or estimated salvage value.
Physical IDs, supported service, customer demand and Treasury remain shared.
"""
from dataclasses import asdict,dataclass,replace
from fractions import Fraction
from pathlib import Path
import hashlib,json

from model.calendar_bridge import (Bridge,_BridgedEnterprise,bridge_case_inputs,
    bridge_source_hashes,bridge_context,exact,rational,wire_rationals)
from model.monthly_deployment import RecoveryTransfer,run_monthly,_integer,_name,_rational
from model.monthly_commercial import restore_opening_inputs
from model.monthly_enterprise import Business,CustomerMove,EnterprisePlan,Equity,Market
from model.enterprise_finance import FinancePlan,TermLoan
from model.treasury import Moment

ROOT=Path(__file__).resolve().parents[1]


@dataclass(frozen=True)
class RecoveryPolicy:
    enabled: bool = True
    unit_id: str = 'opening-installed-entrant-1'
    seller_actor: str = 'entrant'
    buyer_operator: str = 'incumbent'
    offer_month: int = 1
    price_cents: int = 2_000_000
    relocation_cents: int = 100_000
    relocation_months: int = 2
    release_authorized: bool = True
    transfer_rights: bool = True
    qualification_eligible: bool = True

    def __post_init__(self):
        for field in ('enabled','release_authorized','transfer_rights','qualification_eligible'):
            if type(getattr(self,field)) is not bool:raise ValueError('Explicit recovery Boolean required')
        for value in (self.unit_id,self.seller_actor,self.buyer_operator):_name(value)
        _integer(self.offer_month);_integer(self.price_cents,1);_integer(self.relocation_cents,1)
        _integer(self.relocation_months,1)
        if self.offer_month>23 or self.relocation_months>24 or max(self.price_cents,self.relocation_cents)>1_000_000_000:
            raise ValueError('Recovery terms exceed bounded scenario limits')


class RecoveryHooks:
    """Owner-sale lifecycle on one initialized physical/financial enterprise."""
    def initialize_recovery(self,plan,contracts,treasury,enterprise,finance,bridge,recovery):
        if not isinstance(recovery,RecoveryPolicy):raise ValueError('Explicit recovery policy required')
        if recovery.offer_month>=plan.months:raise ValueError('Offer outside horizon')
        if recovery.buyer_operator not in self.by_site:raise ValueError('Unknown recovery buyer operator')
        if recovery.seller_actor not in {b.actor_id for b in enterprise.businesses}:
            raise ValueError('This bounded recovery policy requires an operating-customer seller')
        treasury.account(recovery.seller_actor)
        self.recovery=recovery;self.recovery_events=[];self.recovery_months=[]
        self.recovered=set();self.purchase_ids=set();self.relocation_ids=set();self.offer_bills=[]
        # An explicit inherited resource payable is not free opening capital.
        self.enterprise_cost_ids.update(i.invoice_id for i in treasury.invoices
            if i.category=='recovery_inherited_engineering' and i.payee==enterprise.enterprise_vendor_actor)

    def recovery_event(self,month,action,**data):
        self.recovery_events.append(dict(month=month,phase=3,action=action,**data))

    def prepare(self,t,month,units):
        t=super().prepare(t,month,units);p=self.recovery;buyer=self.by_site[p.buyer_operator]
        if p.enabled and month==p.offer_month and buyer.customer_actor!=p.seller_actor:
            for suffix,payee,amount,category in [
                ('purchase',p.seller_actor,p.price_cents,'asset_recovery_purchase'),
                ('relocation',self.plan.deployment_vendor_actor,p.relocation_cents,'asset_recovery_relocation')]:
                iid=self._id('recovery',month,p.unit_id,suffix)
                t=t.issue_invoice(iid+':issue',iid,buyer.customer_actor,payee,amount,Moment(month,1),Moment(month,3),Moment(month,3),
                    provenance=self.provenance,cancellable=True,category=category)
                self.offer_bills.append(iid)
        return t

    def recovery_transfers(self,t,month,units,shipping_slots):
        p=self.recovery
        if not p.enabled or month!=p.offer_month:return t,()
        u=next((u for u in units if u.unit_id==p.unit_id),None)
        buyer=self.by_site[p.buyer_operator];owner=self.owner.get(p.unit_id)
        reason=''
        if u is None or u.status!='installed':reason='unit_not_installed'
        elif owner!=p.seller_actor:reason='seller_does_not_own_unit'
        elif self.by_site[u.operator_id].arrangement!='sale':reason='installed_contract_release_not_modeled'
        elif p.seller_actor not in self.defaulted:reason='seller_not_in_current_debt_default'
        elif buyer.arrangement!='sale' or buyer.customer_actor==p.seller_actor or u.operator_id==p.buyer_operator:reason='ineligible_distinct_owner_buyer'
        elif not p.release_authorized:reason='old_site_release_not_authorized'
        elif not p.transfer_rights:reason='asset_and_configuration_transfer_not_permitted'
        elif not shipping_slots:reason='no_relocation_shipping_slot'
        elif not self.ready(t,self.business[p.buyer_operator],month,3):reason='buyer_not_operationally_eligible'
        if reason:
            for iid in self.offer_bills:t=t.cancel_invoice(iid+':cancel',iid,Moment(month,3),provenance=self.provenance)
            self.recovery_event(month,'sale_blocked',unit_id=p.unit_id,reason=reason,
                seller_actor=p.seller_actor,actual_title_owner=owner,buyer_actor=buyer.customer_actor,committed_cents=0)
            return t,()
        bills=self.offer_bills
        if len(bills)!=2:raise AssertionError('Accepted sale requires two prior contingent invoices')
        buyer_available=t.available(buyer.customer_actor)
        trial=t
        for iid in bills:
            trial=trial.settle_invoice(iid+':pay',iid,Moment(month,3),provenance=self.provenance)
            if trial.invoice(iid).outstanding_cents:
                reason='unfunded_purchase_or_initial_relocation';break
        if reason:
            # Immutable candidate settlement is all-or-nothing. Future site
            # qualification is deliberately a different, later obligation.
            for iid in bills:t=t.cancel_invoice(iid+':cancel',iid,Moment(month,3),provenance=self.provenance)
            self.recovery_event(month,'sale_blocked',unit_id=p.unit_id,reason=reason,
                invoice_ids=bills,committed_cents=0,title_changed=False,buyer_available_cents=buyer_available)
            return t,()
        purchase,relocation=bills
        self.purchase_ids.add(purchase);self.relocation_ids.add(relocation)
        self.enterprise_cost_ids.add(relocation)
        self.recovered.add(p.unit_id);self.owner[p.unit_id]=buyer.customer_actor
        self.current_treasury=trial
        self._record(Moment(month,3),'recovery_title_transfer',unit_id=p.unit_id,previous_owner=owner,
            title_owner=buyer.customer_actor,purchase_invoice_id=purchase,contract_novation=False)
        self.recovery_event(month,'asset_sold',unit_id=p.unit_id,previous_operator_id=u.operator_id,
            buyer_operator_id=p.buyer_operator,seller_actor=p.seller_actor,buyer_actor=buyer.customer_actor,
            price_cents=p.price_cents,relocation_cents=p.relocation_cents,ready_month=month+p.relocation_months,
            buyer_available_cents=buyer_available,
            purchase_invoice_id=purchase,relocation_invoice_id=relocation,
            debt_already_settled_this_month=True,customer_assignments_transferred=False)
        return trial,(RecoveryTransfer(p.unit_id,p.buyer_operator,month+p.relocation_months,purchase,relocation),)

    def admit(self,t,iid,month,phase,physical_reason,unit=None,operator_id=None):
        if unit is not None and unit.unit_id in self.recovered and t.invoice(iid).category in ('support','commission'):
            if not self.recovery.qualification_eligible:physical_reason=physical_reason or 'buyer_site_configuration_not_qualified'
        return super().admit(t,iid,month,phase,physical_reason,unit,operator_id)

    def close(self,t,month,units,supported):
        super().close(t,month,units,supported)
        p=self.recovery;u=next((u for u in units if u.unit_id==p.unit_id),None)
        self.recovery_months.append(dict(month=month,unit_id=p.unit_id,physical_state=u.status if u else None,
            operator_id=u.operator_id if u else None,title_owner=self.owner.get(p.unit_id),supported=p.unit_id in supported,
            seller_cash_cents=t.balance(p.seller_actor),seller_defaulted=p.seller_actor in self.defaulted,
            seller_principal_claim_cents=sum(t.credit(self.credit_id(l)).outstanding_cents for l in self.finance.loans if l.borrower==p.seller_actor)))

    def recovery_result(self,r):
        invoices=r['closing_treasury']['invoices'];p=self.recovery
        purchases=[i for i in invoices if i['invoice_id'] in self.purchase_ids]
        relocation=[i for i in invoices if i['invoice_id'] in self.relocation_ids]
        return dict(schema_version='asset-recovery/0.1',status='synthetic_declared_sale_not_legal_priority',
            inputs=asdict(p),events=self.recovery_events,months=self.recovery_months,
            cash=dict(purchase_transfer_cents=sum(i['paid_cents'] for i in purchases),
                relocation_resource_cents=sum(i['paid_cents'] for i in relocation),
                purchase_is_internal_transfer=True,relocation_in_enterprise_outlay=True,
                add_to_consolidated_outlay_again=False),
            lineage=[
                dict(metric='eligible asset sale',equation='current installed title owner + current debt default + explicit release/transfer permission + funded buyer and relocation',inputs='RecoveryPolicy, commercial owner ledger, finance default set and Treasury',implementation='_RecoveryEnterprise.recovery_transfers',basis='declared synthetic transaction; no repossession authority inferred'),
                dict(metric='unique physical relocation',equation='installed decreases by one; transit increases by one; later paid commissioning restores installed at destination',inputs='RecoveryTransfer, physical stock/flows and actual commissioning/support',implementation='run_monthly; _audit_month',basis='same unit ID and shared shipping capacity; no same-month service'),
                dict(metric='debt recovered from actual funds',equation='later scheduled principal/interest settlements consume actual seller funds including received price; unpaid claims persist',inputs='purchase invoice and Treasury credit/interest events',implementation='_FinancedEnterprise.service_debt',basis='sale follows current debt settlement; no automatic discharge or lender ownership'),
                dict(metric='resource and service boundary',equation='internal consideration cancels; relocation resource is counted once; accepted output uses unchanged customer assignments and funded physical/human capacity',inputs='enterprise/market ledgers and supported unit IDs',implementation='_Enterprise.enterprise_result; _BridgedEnterprise.dispatch_output',basis='no automatic customer transfer, payroll removal or residual valuation')],
            limits=['Only an expressly releasable customer-owned installed asset can be sold in this bounded policy; lease repossession, service-contract novation and secured priorities remain outside scope',
                'Price and rights are declared assumptions, not offers, market salvage values or enforceability findings',
                'One dated offer, positive purchase/relocation charges and a finite relocation delay; no optimized buyer search, auction or automatic retry',
                'Purchase plus initial relocation settle atomically; later failed qualification retains the completed sale and stranded buyer-owned unit',
                'The old operating company retains customers, staffing, payables, credit claims and legal identity; ownership does not move demand',
                'Full insolvency, taxes, asset impairment, cancellation damages, disposal and empirical whole-life economics remain incomplete'])


class _RecoveryEnterprise(RecoveryHooks,_BridgedEnterprise):
    def __init__(self,plan,contracts,treasury,enterprise,finance,bridge,recovery):
        super().__init__(plan,contracts,treasury,enterprise,finance,bridge)
        self.initialize_recovery(plan,contracts,treasury,enterprise,finance,bridge,recovery)


def recovery_source_hashes():
    return {**bridge_source_hashes(),'model/asset_recovery.py':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}


def run_asset_recovery(plan,treasury,contracts,enterprise,finance,bridge,recovery):
    policy=_RecoveryEnterprise(plan,contracts,treasury,enterprise,finance,bridge,recovery)
    r=run_monthly(plan,treasury,commercial=policy)
    r.update(schema_version='monthly-deployment/0.9',scope='synthetic_funded_asset_recovery_on_calendar_finance_loop',
        ownership='one_title_owner_per_unit_separate_from_custody_and_workflow')
    r['commercial']=policy.result(r);r['commercial']['limits']=['Scopes are defined by asset_recovery, calendar_bridge, finance and enterprise inputs']
    r['enterprise']=policy.enterprise_result(r)
    r['enterprise']['limits']=[x for x in r['enterprise']['limits'] if not x.startswith(('No automatic loan','No annual cleaning-zone'))]
    r['finance']=policy.finance_result(r);r['calendar_bridge']=policy.bridge_result(r)
    add_recovery_sections(policy,r,recovery)
    r['source_sha256']=recovery_source_hashes();r=wire_rationals(r)
    r['rational_wire_format']='decimal_string_numerator_and_denominator_for_lossless_JSON'
    r['case_hash']=hashlib.sha256(json.dumps(r,sort_keys=True,separators=(',',':')).encode()).hexdigest()
    return json.loads(json.dumps(r))


def add_recovery_sections(policy,r,recovery):
    enterprise,plan=policy.enterprise,policy.plan
    r['asset_recovery']=policy.recovery_result(r)
    def total_service(name=None):
        return sum((rational(o['total_delivered_units']) for m in r['enterprise']['months'] for o in m['operators'] if name is None or o['operator_id']==name),Fraction())
    a=r['asset_recovery'];tail=a['months'][-1]
    a['summary']=dict(sale_completed=bool(policy.recovered),purchase_transfer_cents=a['cash']['purchase_transfer_cents'],
        relocation_resource_cents=a['cash']['relocation_resource_cents'],accepted_zones=_rational(total_service()),
        buyer_accepted_zones=_rational(total_service(recovery.buyer_operator)),
        seller_accepted_zones=_rational(total_service(next(b.operator_id for b in enterprise.businesses if b.actor_id==recovery.seller_actor))),due_zones=sum(policy.pool_size.values())*plan.months,
        principal_recovered_cents=r['finance']['consolidation']['principal_recovery_cash_cents'],
        closing_principal_claim_cents=tail['seller_principal_claim_cents'],
        closing_interest_claim_cents=r['finance']['consolidation']['closing_interest_claim_cents'],
        final_physical_state=tail['physical_state'],final_title_owner=tail['title_owner'],
        first_buyer_supported_month=next((m['month'] for m in a['months'] if m['operator_id']==recovery.buyer_operator and m['supported']),None),
        buyer_closing_cash_cents=next(x['cash_cents'] for x in r['closing_treasury']['actors'] if x['actor_id']==policy.by_site[recovery.buyer_operator].customer_actor),
        seller_closing_cash_cents=tail['seller_cash_cents'])
    r['finance']['limits']=[x for x in r['finance']['limits'] if not x.startswith('Cash recovery uses')]+['An eligible funded asset sale can create actual seller receipts; asset_recovery defines its bounded rights, timing and physical-service contract.']
    if recovery.enabled:
        for row in r['finance']['months']:
            row['cash_recovery_only']=False
            row['assets_sold_or_repossessed']=[e['unit_id'] for e in policy.recovery_events if e['action']=='asset_sold' and e['month']==row['month']]


def replay_asset_recovery(saved):
    if not isinstance(saved,dict) or saved.get('schema_version')!='monthly-deployment/0.9':raise ValueError('Saved asset recovery case required')
    try:
        e=dict(saved['enterprise']['inputs']);e['market']=Market(**e['market'])
        for key,cls in [('businesses',Business),('moves',CustomerMove),('equity',Equity)]:e[key]=tuple(cls(**x) for x in e[key])
        f=dict(saved['finance']['inputs']);f['loans']=tuple(TermLoan(**x) for x in f['loans'])
        return run_asset_recovery(*restore_opening_inputs(saved),EnterprisePlan(**e),FinancePlan(**f),
            Bridge(**saved['calendar_bridge']['inputs']),RecoveryPolicy(**saved['asset_recovery']['inputs']))
    except (KeyError,TypeError) as exc:
        raise ValueError('Complete valid opening recovery inputs are required') from exc


DEFAULTS=dict(buyer_cash_cents=20_000_000,seller_cash_cents=0,loan_cents=2_000_000,maturity_month=1,
    monthly_rate_basis_points=0,inherited_engineering_cents=1_500_000,source_arrangement='sale',
    commissioning_slots=1,shipping_slots=1,buyer_full_human_capacity=False)


def recovery_case_inputs(overrides=None,recovery_inputs=None):
    if overrides is None:overrides={}
    if isinstance(overrides,dict) and 'policy' in overrides:
        overrides=dict(overrides)
        if recovery_inputs is not None:raise ValueError('Supply recovery policy once')
        recovery_inputs=overrides.pop('policy')
        if not isinstance(recovery_inputs,dict):raise ValueError('Recovery policy must be an object')
    if recovery_inputs is not None and not isinstance(recovery_inputs,dict):raise ValueError('Recovery policy must be an object')
    if not isinstance(overrides,dict) or set(overrides)-set(DEFAULTS):raise ValueError('Unknown recovery case input')
    x={**DEFAULTS,**overrides};rp=RecoveryPolicy(**(recovery_inputs or {}))
    for key in ('buyer_cash_cents','seller_cash_cents','loan_cents','inherited_engineering_cents','monthly_rate_basis_points','commissioning_slots','shipping_slots'):
        _integer(x[key]);
        if x[key]>1_000_000_000:raise ValueError('Recovery case integer outside declared bound')
    _integer(x['maturity_month'],1)
    if x['maturity_month']>24 or x['source_arrangement'] not in ('sale','lease') or type(x['buyer_full_human_capacity']) is not bool:
        raise ValueError('Invalid recovery case contract')
    p,t,cs,e,_,b=bridge_case_inputs({'loan_cents':0,'entrant_cash_cents':10_000_000},
        {'annual_overrides':{'capability_progress':0}})
    p=replace(p,plan_id='asset-recovery-cleaning',starts=(),opening_finished=0,
        operators=tuple(replace(o,opening_installed=1 if o.operator_id=='entrant' else 0,requested_additions=0) for o in p.operators),
        commissioning_slots=(x['commissioning_slots'],)*p.months,shipping_slots=(x['shipping_slots'],)*p.months)
    cs=tuple(replace(c,arrangement=x['source_arrangement'] if c.operator_id=='entrant' else 'sale',
        lessor_actor='lessor' if c.operator_id=='entrant' and x['source_arrangement']=='lease' else None,deposit_cents=0) for c in cs)
    _,a,_,cell,_,calendar=bridge_context(b,p.months);businesses=[]
    for business in e.businesses:
        staff=business.human_staff_cents_by_month[0]
        if business.operator_id=='incumbent' and not x['buyer_full_human_capacity']:staff//=2
        capacities=tuple(int(Fraction(staff,100)/exact(cell['wage_usd_hour'])/exact(cell['human_hours_per_unit'])/(1-exact(row['effective_parameters']['digital_efficiency']))) for row in calendar)
        businesses.append(replace(business,human_staff_cents_by_month=(staff,)*p.months,human_capacity_by_month=capacities,
            active_from_month=0,qualified_month=0,procurement_month=0,formation_cents=0,acquisition_cents_per_recurring_unit=0,
            overhead_cents_by_month=(10_000,)*p.months))
    e=replace(e,market=replace(e.market,baseline_units=500,unmet_units=400,new_units=0),businesses=tuple(businesses),
        moves=(CustomerMove('existing-entrant-customers',0,'unmet',None,'entrant',400),),equity=())
    amounts={'entrant':x['seller_cash_cents'],'incumbent':x['buyer_cash_cents'],'capital_lender':max(2_000_000,x['loan_cents'])}
    t=replace(t,accounts=tuple(replace(account,opening_cash_cents=amounts[account.actor_id]) if account.actor_id in amounts else account for account in t.accounts))
    if x['inherited_engineering_cents']:
        t=t.issue_invoice('recovery:inherited:issue','recovery:inherited','entrant',e.enterprise_vendor_actor,x['inherited_engineering_cents'],
            Moment(0,1),Moment(0,3),Moment(0,3),provenance='synthetic_inherited_engineering',cancellable=False,category='recovery_inherited_engineering')
    f=FinancePlan((TermLoan('owner-term','capital_lender','entrant',x['loan_cents'],0,x['maturity_month'],x['monthly_rate_basis_points'],10000),) if x['loan_cents'] else ())
    return p,t,cs,e,f,b,rp


def run_recovery_case(overrides=None,recovery_inputs=None):
    return run_asset_recovery(*recovery_case_inputs(overrides,recovery_inputs))


def recovery_worlds():
    return {
        'funded_recovery':{},
        'no_asset_sale':{'policy':{'enabled':False}},
        'nonowner_lease':{'source_arrangement':'lease'},
        'release_not_authorized':{'policy':{'release_authorized':False}},
        'transfer_not_permitted':{'policy':{'transfer_rights':False}},
        'one_cent_short':{'buyer_cash_cents':1_971_399},
        'exact_purchase_funding':{'buyer_cash_cents':1_971_400},
        'qualification_unavailable':{'policy':{'qualification_eligible':False}},
        'commissioning_unavailable':{'commissioning_slots':0},
        'shipping_unavailable':{'shipping_slots':0},
        'arrival_after_horizon':{'policy':{'relocation_months':9}},
        'low_sale_price':{'policy':{'price_cents':300_000}},
        'strong_human_buyer_purchase':{'buyer_full_human_capacity':True},
        'strong_human_buyer_no_purchase':{'buyer_full_human_capacity':True,'policy':{'enabled':False}},
    }


def recovery_artifact():
    options=recovery_worlds();cases={name:run_recovery_case(x) for name,x in options.items()}
    return dict(schema_version='asset-recovery-artifact/0.1',source_sha256=recovery_source_hashes(),defaults=DEFAULTS,
        case_inputs=options,cases=cases,summary=[{'case':name,**r['asset_recovery']['summary']} for name,r in cases.items()],
        comparison_boundary='Fourteen synthetic worlds on one identified cleaning asset, dated finance and the unchanged demand ledger. Purchase price is an internal transfer, relocation consumes resources, qualification/support remain later obligations. Stronger human coverage can eliminate incremental buyer service. No legal priority, optimal liquidation, market valuation or empirical return is identified.')


def recovery_catalog():
    path=ROOT/'model/results/asset_recovery.json'
    if not path.exists():raise ValueError('Generate the asset-recovery export first')
    data=json.loads(path.read_text())
    if data['source_sha256']!=recovery_source_hashes():raise ValueError('Asset-recovery export has stale source hashes; regenerate')
    return {k:v for k,v in data.items() if k!='cases'}|{'cases':{'funded_recovery':data['cases']['funded_recovery']}}
