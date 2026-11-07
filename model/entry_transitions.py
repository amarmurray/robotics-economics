"""Funded share acquisition and separate organic growth on the calendar loop.

No asset/contract novation: the operating company, its obligations and units stay.
"""
from dataclasses import asdict,dataclass,replace
from fractions import Fraction
import hashlib,json
from pathlib import Path
from model.calendar_bridge import (Bridge,_BridgedEnterprise,bridge_case_inputs,
    bridge_source_hashes,rational,wire_rationals)
from model.monthly_commercial import restore_opening_inputs
from model.monthly_deployment import Start,run_monthly
from model.monthly_enterprise import Business,CustomerMove,EnterprisePlan,Equity,Market
from model.enterprise_finance import FinancePlan,TermLoan
from model.treasury import Account,Moment

ROOT=Path(__file__).resolve().parents[1]
BUYER='platform_buyer';SELLER='selling_owner';VENDOR='entry_resource_vendor'
MODES=('status_quo','build','acquire','hybrid')


def bounded_int(value,maximum=1_000_000_000):
    if type(value) is not int or not 0<=value<=maximum:raise ValueError('Bounded nonnegative exact integer required')


@dataclass(frozen=True)
class Transition:
    mode:str='acquire'
    close_month:int=2
    price_cents:int=10_000_000
    diligence_cents:int=100_000
    transition_cents:int=500_000
    target_equity_cents:int=0
    disruption_months:int=0
    assumed_transfer_consent:bool=True
    def __post_init__(self):
        if self.mode not in MODES:raise ValueError('Unknown entry route')
        bounded_int(self.close_month,7);bounded_int(self.disruption_months,8)
        for value in (self.price_cents,self.diligence_cents,self.transition_cents,self.target_equity_cents):bounded_int(value)
        if type(self.assumed_transfer_consent) is not bool:raise ValueError('Explicit assumed-consent Boolean required')


class _EntryEnterprise(_BridgedEnterprise):
    def __init__(self,plan,contracts,treasury,enterprise,finance,bridge,transition):
        super().__init__(plan,contracts,treasury,enterprise,finance,bridge)
        if not isinstance(transition,Transition):raise ValueError('Explicit entry transition required')
        if set(self.business)!={'incumbent','entrant'} or enterprise.market.incumbent_operator!='incumbent':
            raise ValueError('Explicit incumbent target and separate entrant required')
        if transition.close_month>=plan.months:raise ValueError('Closing month outside horizon')
        existing=set(self.parties)|{enterprise.market.buyer_actor,enterprise.enterprise_vendor_actor,
            plan.manufacturing_vendor_actor,plan.deployment_vendor_actor,bridge.digital_vendor_actor}
        if existing&{BUYER,SELLER,VENDOR}:raise ValueError('Entry counterparties must be separate legal accounts')
        for actor in (BUYER,SELLER,VENDOR):treasury.account(actor)
        if any(loan.lender in (BUYER,SELLER) for loan in finance.loans):
            raise ValueError('This wider boundary requires outside lenders; parent/seller loans are not implemented')
        if any(i.category!='entry_opening_target_payable' or i.payer!=self.business['incumbent'].actor_id or i.payee!=enterprise.enterprise_vendor_actor for i in treasury.invoices):
            raise ValueError('Only the explicit existing target resource payable is supported in this opening contract')
        self.transition=transition;self.closed_month=None;self.close_status='not_planned' if transition.mode in ('status_quo','build') else 'pending'
        self.owners={'incumbent':SELLER,'entrant':BUYER};self.entry_events=[];self.entry_months=[]
        self.entry_ids={};self.diligence_ids=set();self.closing_ids=[]
        self.opening_target_payable_ids={i.invoice_id for i in treasury.invoices if i.payer==self.business['incumbent'].actor_id and i.category=='entry_opening_target_payable'}
        self.enterprise_cost_ids|=self.opening_target_payable_ids

    def entry_event(self,month,action,**detail):
        self.entry_events.append({'month':month,'phase':2,'action':action,**detail})

    def prepare(self,t,month,units):
        t=super().prepare(t,month,units)
        terms=self.transition
        if terms.mode not in ('acquire','hybrid'):return t
        bills=[]
        if month==max(0,terms.close_month-1):bills.append(('diligence_resource',VENDOR,terms.diligence_cents,False))
        if month==terms.close_month:
            bills.extend([('share_consideration',SELLER,terms.price_cents,True),
                ('transition_resource',VENDOR,terms.transition_cents,True),
                ('target_equity',self.business['incumbent'].actor_id,terms.target_equity_cents,True)])
        for category,payee,amount,conditional in bills:
            if not amount:continue
            iid=self._id('entry',category)
            t=self.issue_enterprise(t,iid,BUYER,payee,amount,Moment(month,1),Moment(month,2),'entry_'+category,conditional)
            self.entry_ids[category]=iid
            if conditional:self.closing_ids.append(iid)
            else:self.diligence_ids.add(iid)
        return t

    def collect(self,t,month):
        t=super().collect(t,month)
        t=self.collect_set(t,month,2,self.diligence_ids)
        terms=self.transition
        if terms.mode not in ('acquire','hybrid') or month!=terms.close_month:return t
        reason=''
        if not terms.assumed_transfer_consent:reason='assumed_transfer_consent_not_met'
        if any(t.invoice(iid).outstanding_cents for iid in self.diligence_ids):reason=reason or 'diligence_unpaid'
        if self.owners['incumbent']!=SELLER:reason=reason or 'seller_not_current_owner'
        # Candidate treasury is immutable; a failed contingent group commits nothing.
        candidate=t
        if not reason:
            for iid in self.closing_ids:
                candidate=candidate.settle_invoice(iid+':close',iid,Moment(month,2),provenance=self.provenance)
                if candidate.invoice(iid).outstanding_cents:
                    reason='closing_group_unfunded';break
        if reason:
            for iid in self.closing_ids:t=t.cancel_invoice(iid+':cancel',iid,Moment(month,2),provenance=self.provenance)
            self.close_status='blocked'
            self.entry_event(month,'share_closing',status='blocked',reason=reason,ownership_changed=False,paid_contingent_cents=0)
        else:
            t=candidate;self.owners['incumbent']=BUYER;self.closed_month=month;self.close_status='closed'
            if 'target_equity' in self.entry_ids:self.equity_ids.add(self.entry_ids['target_equity'])
            self.entry_event(month,'share_closing',status='closed',reason='',ownership_changed=True,
                seller=SELLER,buyer=BUYER,target_legal_actor=self.business['incumbent'].actor_id,
                target_cash_not_purchase_funding=True,paid_contingent_cents=sum(t.invoice(iid).paid_cents for iid in self.closing_ids))
        return t

    def ready(self,t,b,month,phase=5):
        if b.operator_id=='incumbent' and self.closed_month is not None and self.closed_month<=month<self.closed_month+self.transition.disruption_months:
            return False
        return super().ready(t,b,month,phase)

    def close(self,t,month,units,supported):
        super().close(t,month,units,supported)
        assets=self.months[-1]['assets'];target=self.business['incumbent'].actor_id
        self.entry_months.append({'month':month,'ultimate_owners':dict(self.owners),'close_status':self.close_status,
            'target_legal_actor':target,'target_cash_cents':t.balance(target),'buyer_cash_cents':t.balance(BUYER),'seller_cash_cents':t.balance(SELLER),
            'target_disrupted':self.closed_month is not None and self.closed_month<=month<self.closed_month+self.transition.disruption_months,
            'target_unit_ids':[u.unit_id for u in units if u.operator_id=='incumbent'],
            'target_asset_contracts':[a for a in assets if a['workflow_authority']==target],
            'target_due_unpaid_cents':sum(i.outstanding_cents for i in t.invoices if i.payer==target and not i.cancellable and i.due_at<=Moment(month,7))})

    def entry_result(self,r):
        opening={a['actor_id']:a['cash_cents'] for a in r['opening_treasury']['actors']}
        closing={a['actor_id']:a['cash_cents'] for a in r['closing_treasury']['actors']}
        invoices={i['invoice_id']:i for i in r['closing_treasury']['invoices']}
        paid=lambda category:invoices[self.entry_ids[category]]['paid_cents'] if category in self.entry_ids else 0
        fees=paid('diligence_resource')+paid('transition_resource')
        base=r['enterprise']['consolidation'];wide=sorted(set(self.parties)|{BUYER,SELLER})
        net=sum(closing[actor]-opening[actor] for actor in wide)
        resources=base['external_physical_outlay_cents']+base['external_enterprise_outlay_cents']+fees
        # All configured equity in the reference comes from the included buyer.
        outside_equity=sum(i['paid_cents'] for i in invoices.values() if i['invoice_id'] in self.equity_ids and i['payer'] not in wide)
        financing=r['finance']['consolidation']['net_financing_cash_cents']
        target=self.business['incumbent'].actor_id
        return {'schema_version':'entry-transitions/0.1','evidence_status':'synthetic_share_purchase_and_separate_growth',
            'inputs':asdict(self.transition),'closed_month':self.closed_month,'close_status':self.close_status,
            'months':self.entry_months,'events':self.entry_events,'entry_invoices':[invoices[i] for i in self.entry_ids.values()],
            'legal_contract':'100% beneficial equity ownership changes; target legal account, customer assignment, asset title/custody, receivables and obligations do not move',
            'cash':{'paid_share_price_cents':paid('share_consideration'),'paid_diligence_cents':paid('diligence_resource'),
                'paid_transition_resources_cents':paid('transition_resource'),'paid_target_equity_cents':paid('target_equity'),
                'paid_growth_equity_cents':sum(i['paid_cents'] for i in invoices.values() if i['invoice_id'] in self.equity_ids and i['payer']==BUYER and i['payee']==self.business['entrant'].actor_id),
                'buyer_opening_cents':opening[BUYER],'buyer_closing_cents':closing[BUYER],'seller_cash_received_cents':closing[SELLER]-opening[SELLER],
                'target_opening_cents':opening[target],'target_closing_cents':closing[target],
                'target_opening_payables_paid_cents':sum(invoices[i]['paid_cents'] for i in self.opening_target_payable_ids),
                'target_opening_payables_unpaid_cents':sum(invoices[i]['outstanding_cents'] for i in self.opening_target_payable_ids),
                'buyer_due_unpaid_cents':sum(i['outstanding_cents'] for i in invoices.values() if i['payer']==BUYER and not i['cancellable'] and (i['due_at']['month'],i['due_at']['phase'])<=(self.plan.months-1,7))},
            'consolidation':{'fixed_included_actors':wide,'fixed_boundary_cash_change_cents':net,
                'end_market_cash_received_cents':base['end_market_cash_received_cents'],'external_operating_and_transaction_cash_cents':resources,
                'external_equity_cash_cents':outside_equity,'external_net_financing_cash_cents':financing,
                'unclassified_boundary_cash_cents':net-(base['end_market_cash_received_cents']+outside_equity+financing-resources),
                'share_price_and_internal_equity_eliminated':True,'target_cash_swept_to_buyer_cents':0,'terminal_equity_value':None},
            'limits':['Synthetic share purchase only; no asset purchase, legal/tax opinion, debt novation, vendor rights grant or real valuation',
                'Price is paid to the selling owner, not to the operating company; target working capital requires separate funded equity',
                'Diligence is a prior committed bill; consideration/transition/equity closing is atomic and a failed closing is not automatically retried',
                'Hybrid growth is a separately committed business leg and can proceed if the acquisition fails; no automatic synergy or payroll removal',
                'Disruption is a declared whole-target service suspension with retained paid obligations, not an observed acquisition effect',
                'Existing operating-company assets, leases, unpaid liabilities and receivables stay with their legal counterparties; ultimate owner is a separate register',
                'Fixed wide consolidation includes seller, buyer and robot-commercial parties; cash is not profit and opening-payable settlement is not new current-period resource use',
                'No dividends, target-cash sweep, terminal share valuation, goodwill accounting or lifecycle ROI is estimated']}


def source_hashes():
    return {**bridge_source_hashes(),'model/entry_transitions.py':hashlib.sha256((ROOT/'model/entry_transitions.py').read_bytes()).hexdigest()}


def canonical_wire(value):
    if isinstance(value,dict):return {key:canonical_wire(v) for key,v in value.items()}
    if isinstance(value,(list,tuple)):return [canonical_wire(v) for v in value]
    if type(value) is float and value.is_integer():return int(value)
    return value


def run_entry_transition(plan,treasury,contracts,enterprise,finance,bridge,transition):
    policy=_EntryEnterprise(plan,contracts,treasury,enterprise,finance,bridge,transition)
    r=run_monthly(plan,treasury,commercial=policy)
    r.update(schema_version='monthly-deployment/0.7',scope='synthetic_funded_share_acquisition_and_separate_growth',ownership='one_legal_title_owner_and_separate_ultimate_equity_owner')
    r['commercial']=policy.result(r);r['commercial']['limits']=['Scope is defined by entry_transition, calendar_bridge and finance limits']
    r['enterprise']=policy.enterprise_result(r);r['enterprise']['limits']=[x for x in r['enterprise']['limits'] if not x.startswith(('No automatic loan','No annual cleaning-zone'))]
    r['finance']=policy.finance_result(r);r['calendar_bridge']=policy.bridge_result(r);r['entry_transition']=policy.entry_result(r)
    assert r['entry_transition']['consolidation']['unclassified_boundary_cash_cents']==0
    assert sum(a['cash_cents'] for a in r['opening_treasury']['actors'])==sum(a['cash_cents'] for a in r['closing_treasury']['actors'])
    r['source_sha256']=source_hashes();r=wire_rationals(canonical_wire(r))
    r['rational_wire_format']='decimal_string_numerator_and_denominator_for_lossless_JSON'
    r['case_hash']=hashlib.sha256(json.dumps(r,sort_keys=True,separators=(',',':')).encode()).hexdigest()
    return json.loads(json.dumps(r))


DEFAULTS={'mode':'acquire','buyer_cash_cents':20_000_000,'target_cash_cents':2_500_000,'growth_equity_cents':6_000_000,
    'close_month':2,'price_cents':10_000_000,'diligence_cents':100_000,'transition_cents':500_000,'target_equity_cents':0,
    'disruption_months':0,'assumed_transfer_consent':True,'target_opening_payable_cents':0,'new_robots':2,
    'growth_move_month':3,'incumbent_response_month':None}


def entry_case_inputs(overrides=None):
    if overrides is None:overrides={}
    if not isinstance(overrides,dict) or set(overrides)-set(DEFAULTS):raise ValueError('Unknown entry-transition input')
    x={**DEFAULTS,**overrides}
    for key,value in x.items():
        if key in ('mode','assumed_transfer_consent'):continue
        if key=='incumbent_response_month' and value is None:continue
        bounded_int(value,7 if key in ('close_month','growth_move_month','incumbent_response_month') else 4 if key=='new_robots' else 8 if key=='disruption_months' else 1_000_000_000)
    terms=Transition(**{k:x[k] for k in asdict(Transition())})
    growth=x['mode'] in ('build','hybrid')
    p,t,cs,e,f,b=bridge_case_inputs({'loan_cents':0,'entrant_cash_cents':0,'response_month':None,'later_start_candidate':False}, {'support_hours_per_month':60,'integration_hours_per_month':200})
    p=replace(p,plan_id='entry-share-transition',operators=tuple(replace(o,requested_additions=x['new_robots'] if growth and o.operator_id=='entrant' else 0) for o in p.operators),
        allocation_cycle=('incumbent','entrant'),starts=(Start('growth',0,x['new_robots'],x['new_robots']),) if growth and x['new_robots'] else ())
    accounts=tuple(replace(a,opening_cash_cents=x['target_cash_cents']) if a.actor_id=='incumbent' else a for a in t.accounts)
    t=replace(t,accounts=accounts+(Account(BUYER,x['buyer_cash_cents']),Account(SELLER,0),Account(VENDOR,0)))
    businesses=tuple(replace(business,active_from_month=0 if growth else None) if business.operator_id=='entrant' else business for business in e.businesses)
    moves=[]
    if growth:
        if x['mode']=='build':moves.append(CustomerMove('organic-baseline-capture',x['growth_move_month'],'baseline','incumbent','entrant',70))
        moves.extend([CustomerMove('growth-unmet',x['growth_move_month'],'unmet',None,'entrant',100),CustomerMove('growth-new',x['growth_move_month'],'new',None,'entrant',50)])
        if x['mode']=='build' and x['incumbent_response_month'] is not None:
            moves.append(CustomerMove('equal-tech-incumbent-response',x['incumbent_response_month'],'baseline','entrant','incumbent',70))
    equity=(Equity('fund-separate-growth',0,BUYER,'entrant',x['growth_equity_cents']),) if growth and x['growth_equity_cents'] else ()
    e=replace(e,businesses=businesses,moves=tuple(moves),equity=equity)
    if x['target_opening_payable_cents']:
        t=t.issue_invoice('opening-target-payable:issue','opening-target-payable','incumbent','enterprise_vendor',x['target_opening_payable_cents'],
            Moment(0,1),Moment(2,3),Moment(2,3),provenance='synthetic_existing_target_obligation',category='entry_opening_target_payable')
    return p,t,cs,e,f,b,terms


def run_entry_case(overrides=None):return run_entry_transition(*entry_case_inputs(overrides))


def replay_entry_transition(saved):
    if not isinstance(saved,dict) or saved.get('schema_version')!='monthly-deployment/0.7':raise ValueError('Complete entry-transition case required')
    try:
        e=dict(saved['enterprise']['inputs']);e['market']=Market(**e['market'])
        for key,cls in [('businesses',Business),('moves',CustomerMove),('equity',Equity)]:e[key]=tuple(cls(**x) for x in e[key])
        f=dict(saved['finance']['inputs']);f['loans']=tuple(TermLoan(**x) for x in f['loans'])
        return run_entry_transition(*restore_opening_inputs(saved),EnterprisePlan(**e),FinancePlan(**f),Bridge(**saved['calendar_bridge']['inputs']),Transition(**saved['entry_transition']['inputs']))
    except (KeyError,AttributeError) as exc:raise ValueError('Incomplete entry-transition inputs') from exc


def witness_options():
    return {'status_quo':{'mode':'status_quo'},'organic_build':{'mode':'build'},'share_acquisition':{},'hybrid':{'mode':'hybrid'},
        'higher_price_same_operations':{'price_cents':15_000_000},'unfunded_closing':{'buyer_cash_cents':10_000_000},
        'consent_not_assumed':{'assumed_transfer_consent':False},'transition_interruption':{'disruption_months':1},
        'purchase_without_operating_cash':{'target_cash_cents':0},'funded_target_working_capital':{'target_cash_cents':0,'target_equity_cents':2_500_000},
        'target_liability_retained':{'target_opening_payable_cents':3_000_000},
        'hybrid_acquisition_fails':{'mode':'hybrid','buyer_cash_cents':16_000_000},
        'hybrid_growth_liquidity':{'mode':'hybrid','growth_equity_cents':6_500_000},
        'prompt_incumbent_response':{'mode':'build','incumbent_response_month':3},
        'delayed_incumbent_response':{'mode':'build','incumbent_response_month':6}}


def entry_artifact():
    options=witness_options();cases={name:run_entry_case(x) for name,x in options.items()}
    summary=[]
    for name,r in cases.items():
        a=r['entry_transition'];cash=a['cash']
        summary.append({'case':name,'close_status':a['close_status'],'accepted_zones':{'numerator':str(sum((rational(m['total_delivered_units']) for m in r['enterprise']['months']),Fraction()).numerator),
            'denominator':str(sum((rational(m['total_delivered_units']) for m in r['enterprise']['months']),Fraction()).denominator)},
            'paid_staff_cents':sum(x['current_period_staff_cash_paid_cents'] for m in r['calendar_bridge']['months'] for x in m['human_work']),
            **cash,'external_operating_and_transaction_cash_cents':a['consolidation']['external_operating_and_transaction_cash_cents']})
    return {'schema_version':'entry-transition-artifact/0.1','case_inputs':options,'cases':cases,'summary':summary,'source_sha256':source_hashes(),
        'comparison_boundary':'Fixed opening buyer capital in the four routes; current operating companies, fixed demand and shared physical execution remain explicit. Price changes ownership, not production. Separate growth and target equity need actual funds; no terminal share value or ROI is estimated.'}
