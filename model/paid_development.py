"""Paid pre-admission work, declared qualification and the existing service history.

This does not simulate learning or measure a robot trial. A declared review outcome
controls admission only after compatible, eligible, funded work. Failed completed
work remains paid. The unchanged human-led service is the feasible outside option.
"""
from dataclasses import asdict,dataclass
from fractions import Fraction
import hashlib,json

from model.architecture_awards import (_ArchitectureAwards,architecture_awards_inputs,
    architecture_awards_result,architecture_awards_summary,source_hashes as award_hashes)
from model.calendar_bridge import ROOT,Bridge,exact
from model.component_inventory import ComponentInventory,read_components
from model.competitive_renewals import Competition
from model.enterprise_finance import FinancePlan,TermLoan
from model.entry_transitions import Transition
from model.monthly_architectures import ArchitectureExecution,RESOURCE_ACTOR,canonical_wire
from model.monthly_commercial import restore_opening_inputs
from model.monthly_deployment import run_monthly,_rational
from model.monthly_enterprise import Business,CustomerMove,EnterprisePlan,Equity,Market
from model.annual_resource_ledger import read_resources
from model.qualified_staffing import available_support
from model.shared_workforce import Workforce
from model.treasury import Moment

SCHEMA='paid-development-window/0.1'
INITIAL_COSTS={'demonstration_collection','customer_path_setup','model_adaptation_engineering',
 'model_adaptation_compute','allocated_model_development','qualification_validation'}


@dataclass(frozen=True)
class ReviewAttempt:
    attempt_id: str
    month: int
    unit_id: str
    evidence_id: str
    declared_pass: bool

    def __post_init__(self):
        for value in (self.attempt_id,self.unit_id,self.evidence_id):
            if not isinstance(value,str) or not value.strip() or len(value)>100:raise ValueError('Named bounded review, unit and evidence IDs required')
        if type(self.month) is not int or not 0<=self.month<8:raise ValueError('Review month must lie in the eight-month contract')
        if type(self.declared_pass) is not bool:raise ValueError('Qualification outcome is an explicit synthetic Boolean premise')


@dataclass(frozen=True)
class DevelopmentPlan:
    configuration_id: str
    attempts: tuple[ReviewAttempt,...]
    collection_allowed: bool=True
    evidence_use_rights: bool=True

    def __post_init__(self):
        if not isinstance(self.configuration_id,str) or not self.configuration_id:raise ValueError('Explicit configuration required')
        if type(self.collection_allowed) is not bool or type(self.evidence_use_rights) is not bool:raise ValueError('Explicit collection and use-rights premises required')
        object.__setattr__(self,'attempts',tuple(self.attempts))
        if len(self.attempts)>8 or any(not isinstance(a,ReviewAttempt) for a in self.attempts):raise ValueError('At most eight explicit review attempts')
        for key in ('attempt_id','month','evidence_id'):
            values=[getattr(a,key) for a in self.attempts]
            if len(set(values))!=len(values):raise ValueError('Duplicate review, evidence or monthly slot')
        if list(self.attempts)!=sorted(self.attempts,key=lambda a:a.month):raise ValueError('Review attempts must be chronological')


def read_development(value):
    if not isinstance(value,dict):raise ValueError('Complete development object required')
    try:return DevelopmentPlan(**{**value,'attempts':tuple(ReviewAttempt(**a) for a in value['attempts'])})
    except (KeyError,TypeError,AttributeError) as exc:raise ValueError('Invalid development plan') from exc


def source_hashes():
    return {**award_hashes(),'model/paid_development.py':hashlib.sha256((ROOT/'model/paid_development.py').read_bytes()).hexdigest()}


class _PaidDevelopment(_ArchitectureAwards):
    def __init__(self,*args,development):
        super().__init__(*args);self.development=development
        expected=self.architecture.architecture_id+':'+self.annual['onboard_configuration']+':review-v1'
        if development.configuration_id!=expected:raise ValueError('Review configuration must match the selected architecture and onboard configuration')
        if self.plan.months!=8 or self.architecture.new_robots not in (0,1):raise ValueError('One target unit and eight months required')
        units={f'start-{s.order_id}-{i+1}' for s in self.plan.starts for i in range(s.quantity)}
        if any(a.unit_id not in units for a in development.attempts):raise ValueError('Review names a unit absent from the physical manufacture contract')
        self.review_events=[];self.review_prepared={};self.review_passed=set();self.review_work_paid=set();self.review_resource_ids=set()
        self.replacing_initial=False

    def arch_charge(self,t,month,phase,payer,payee,category,amount,unit_id=None,resource=False,cancellable=True,due=None):
        if self.replacing_initial:
            if category in INITIAL_COSTS or category=='model_upfront_payment':return t,None
            if category=='integration_validation_payment' and unit_id not in self.qualified:
                # Pre-admission reviews fund validation. This remaining payment is
                # only physical integration and its declared margin, once.
                a=self.profile;c=self.settings['common']
                validation=exact(a['validation_engineering_hours'])*exact(c['engineering_usd_hour'])+exact(a['qualification_resources_usd'])
                amount=exact(amount)-validation*(1+exact(c['integration_markup']))*100
                if amount<0:raise AssertionError('Validation transfer cannot exceed original booking')
        return super().arch_charge(t,month,phase,payer,payee,category,amount,unit_id,resource,cancellable,due)

    def prepare(self,t,month,units):
        self.replacing_initial=True
        try:t=super().prepare(t,month,units)
        finally:self.replacing_initial=False
        for key,(initial,_,_) in list(self.initial_work.items()):
            if key[0]==month:self.initial_work[key]=(initial,Fraction(),Fraction())
        for attempt in self.development.attempts:
            if attempt.month!=month:continue
            u=next((u for u in units if u.unit_id==attempt.unit_id),None)
            reason='already_passed' if attempt.unit_id in self.review_passed else \
                'collection_not_allowed' if not self.development.collection_allowed else \
                'evidence_rights_unavailable' if not self.development.evidence_use_rights else \
                'architecture_assumption_not_admitted' if self.failed_gates else \
                'unit_not_available_for_precommission_review' if u is None or u.status!='transit' or u.ready_month>month else ''
            if reason:
                self.review_events.append({**asdict(attempt),'status':'not_attempted','reason':reason,'work_paid_cents':0,'engineering_hours':_rational(0),'demonstration_hours':_rational(0)});continue
            a=self.profile;c=self.settings['common'];first=attempt.unit_id not in self.review_work_paid
            engineering=exact(c['engineering_usd_hour']);validation=exact(a['validation_engineering_hours'])*engineering+exact(a['qualification_resources_usd'])
            work=[('customer','demonstration_collection',exact(a['demonstration_hours'])*exact(self.cell['wage_usd_hour'])),
                ('model_supplier','model_adaptation_engineering',exact(a['adaptation_engineering_hours'])*engineering),
                ('model_supplier','model_adaptation_compute',exact(a['adaptation_compute_usd'])),
                ('integrator','qualification_validation',validation)]
            if first:work.extend([('customer','customer_path_setup',exact(c[c['customer_path']+'_setup_usd'])),
                ('model_supplier','allocated_model_development',exact(a['model_development_allocation_usd_upfront']))])
            fees=[('operator','integrator','review_validation_fee',validation*(1+exact(c['integration_markup'])))]
            if first:fees.append(('operator','model_supplier','review_upfront_fee',exact(a['model_upfront_payment_usd'])))
            ids=[];resources=[]
            for payer,payee,category,value in fees:
                t,iid=self.arch_charge(t,month,3,self.roles[payer],self.roles[payee],category,value*100,attempt.unit_id)
                if iid:ids.append(iid)
            for role,category,value in work:
                t,iid=self.arch_charge(t,month,3,self.roles[role],RESOURCE_ACTOR,'review_'+category,value*100,attempt.unit_id,resource=True)
                if iid:ids.append(iid);resources.append(iid)
            self.review_prepared[month]=(attempt,ids,resources,exact(a['adaptation_engineering_hours'])+exact(a['validation_engineering_hours']),exact(a['demonstration_hours']))
        return t

    def mandatory(self,t,month):
        t=super().mandatory(t,month)
        if month not in self.review_prepared:return t
        a,ids,resources,engineering,demo=self.review_prepared[month]
        reason='engineering_hours_unavailable' if self.engineering_used+engineering>self.architecture.engineering_hours_per_month else \
            'demonstration_hours_unavailable' if self.demonstration_used+demo>self.architecture.demonstration_hours_per_month else ''
        candidate=t
        if not reason:
            for iid in ids:
                candidate=candidate.settle_invoice(iid+':review-pay',iid,Moment(month,3),provenance=self.provenance)
                if candidate.invoice(iid).outstanding_cents:reason='funding:'+candidate.invoice(iid).category;break
        if reason:
            for iid in ids:t=t.cancel_invoice(iid+':review-cancel',iid,Moment(month,3),provenance=self.provenance)
            self.review_events.append({**asdict(a),'status':'not_attempted','reason':reason,'invoice_ids':ids,'work_paid_cents':0,'engineering_hours':_rational(0),'demonstration_hours':_rational(0)})
        else:
            t=candidate;self.engineering_used+=engineering;self.demonstration_used+=demo;self.review_work_paid.add(a.unit_id);self.review_resource_ids.update(resources)
            if a.declared_pass:self.review_passed.add(a.unit_id)
            self.review_events.append({**asdict(a),'status':'passed' if a.declared_pass else 'failed','reason':'declared_synthetic_review_outcome','invoice_ids':ids,
                'work_paid_cents':sum(t.invoice(i).paid_cents for i in resources),'engineering_hours':_rational(engineering),'demonstration_hours':_rational(demo)})
        self.current_treasury=t
        return t

    def admit(self,t,iid,month,phase,physical_reason,unit=None,operator_id=None):
        if t.invoice(iid).category in ('commission','support') and unit.unit_id not in self.review_passed:
            physical_reason=physical_reason or 'development_review_not_passed'
        return super().admit(t,iid,month,phase,physical_reason,unit,operator_id)

    def architecture_result(self,r):
        result=super().architecture_result(r)
        result['contract']['initial_model_work']='Pre-admission paid review work replaces first-successful-admission development charges. Completed failed reviews remain paid. Setup, allocated development and upfront fee occur once per unit on first completed review; demonstration, adaptation, compute, validation and validation fee recur per completed attempt. Physical integration remains separately charged once at commissioning.'
        result['contract']['resource_hours']='Pre-admission reviews consume the same declared engineering/demonstration pools before commissioning; operating service never recharges that work. These are dedicated specialist resources, distinct from paid site crews and annual provider support.'
        return result

    def development_result(self,r):
        invoices={i['invoice_id']:i for i in r['closing_treasury']['invoices']}
        paid=sum(invoices[i]['paid_cents'] for i in self.review_resource_ids)
        assert paid==sum(e['work_paid_cents'] for e in self.review_events)
        return dict(inputs=asdict(self.development),events=self.review_events,passed_unit_ids=sorted(self.review_passed),resource_cash_cents=paid,
            completed_attempts=sum(e['status'] in ('passed','failed') for e in self.review_events),failed_completed_attempts=sum(e['status']=='failed' for e in self.review_events),
            failed_review_resource_cash_cents=sum(e['work_paid_cents'] for e in self.review_events if e['status']=='failed'),
            rights_scope='Explicit collection/use premises for fresh named review evidence and one configuration/unit. No cross-company data rights, transferred license, learned capability or empirical validation is inferred.',
            timing='Mandatory payroll/debt settle before phase-3 review prepayment. A completed precommission review consumes dedicated specialist engineering and demonstration capacity in a declared pre-service window. Phase-4 physical commissioning and provider resources remain separate. A blocked booking performs no work; a completed failed review is never rolled back by later admission failure.',
            service_boundary='Review evidence is neither customer service nor training output. The outcome is a declared hypothesis, not a simulated acceptance trial or measured learning effect. Existing service capability and crew policies remain unchanged after a declared pass.',
            cash_boundary='Review fees are internal-party transfers; external review resources are included once in all-payer resource cash. Cancelled unperformed work differs from paid failed work. Hardware may remain stranded after stopping, so no lifecycle ROI is reported.',
            decision='Compare the next funded attempt with a qualified human-led service policy. Prior paid failure belongs in history and does not supply engineering capacity, rights, qualification or a reason to continue.',
            limits=['One target configuration and unit, deterministic declared outcomes and fixed eight-month bids; not an optimized development stopping policy.',
                'No detailed robot trial dynamics, trial wear/parts, paid staff for a full external lab, stochastic learning curve or current project prices.',
                'The distinct automotive learning fixture is not imported or added to this cleaning-service world. Shared adaptation, configuration changes and commercial alternative qualification remain open.'])


def paid_development_inputs(inputs=None):
    if inputs is None:inputs={}
    if not isinstance(inputs,dict) or set(inputs)-{'awards','development'}:raise ValueError('Expected awards and development inputs')
    args=architecture_awards_inputs(inputs.get('awards',{}));cfg=args[-1]
    defaults={'configuration_id':cfg.architecture_id+':'+cfg.annual_reference_overrides['onboard_configuration']+':review-v1',
        'attempts':[{'attempt_id':'review-1','month':2,'unit_id':'start-shared-supply-1','evidence_id':'review-evidence-1','declared_pass':True}] if cfg.new_robots else []}
    value=inputs.get('development',{})
    if not isinstance(value,dict):raise ValueError('Development controls must be an object')
    return (*args,read_development({**defaults,**value}))


def run_paid_development(plan,treasury,contracts,enterprise,finance,bridge,competition,transition,crews,resources,components,architecture,development):
    policy=_PaidDevelopment(plan,contracts,treasury,enterprise,finance,bridge,competition,transition,crews,resources,architecture,development=development)
    if components.system_id!=plan.system.system_id or components.onboard_configuration!=policy.annual['onboard_configuration']:raise ValueError('Parts must match reviewed configuration')
    materials=ComponentInventory(components);r=architecture_awards_result(run_monthly(plan,treasury,commercial=policy,materials=materials),policy,materials)
    r.pop('case_hash');r.update(schema_version=SCHEMA,scope='synthetic_paid_pre_admission_work_and_actual_whole_service_history',development=policy.development_result(r),source_sha256=source_hashes());r=canonical_wire(r);r['case_hash']=hashlib.sha256(json.dumps(r,sort_keys=True,separators=(',',':')).encode()).hexdigest();return r


def run_paid_development_case(inputs=None):return run_paid_development(*paid_development_inputs(inputs))


def replay_paid_development(saved):
    if not isinstance(saved,dict) or saved.get('schema_version')!=SCHEMA:raise ValueError('Complete paid-development case required')
    try:
        e=dict(saved['enterprise']['inputs']);e['market']=Market(**e['market'])
        for key,cls in [('businesses',Business),('moves',CustomerMove),('equity',Equity)]:e[key]=tuple(cls(**x) for x in e[key])
        f=dict(saved['finance']['inputs']);f['loans']=tuple(TermLoan(**x) for x in f['loans'])
        return run_paid_development(*restore_opening_inputs(saved),EnterprisePlan(**e),FinancePlan(**f),Bridge(**saved['calendar_bridge']['inputs']),Competition(**saved['competition']['inputs']),Transition(**saved['entry_transition']['inputs']),
            {op:Workforce(**w) for op,w in saved['staffed_renewals']['inputs'].items()},read_resources(saved['annual_resources']['inputs']),read_components(saved['component_inventory']['inputs']),
            ArchitectureExecution(**saved['architecture_execution']['inputs']),read_development(saved['development']['inputs']))
    except (KeyError,TypeError,AttributeError) as exc:raise ValueError('Incomplete development/service opening inputs') from exc


def paid_development_worlds():
    fail={'attempt_id':'review-1','month':2,'unit_id':'start-shared-supply-1','evidence_id':'review-evidence-1','declared_pass':False}
    again={**fail,'attempt_id':'review-2','month':3,'evidence_id':'review-evidence-2','declared_pass':True}
    return {'pass_first_review':{},'fail_then_pass':{'development':{'attempts':[fail,again]}},
        'stop_after_paid_failure':{'development':{'attempts':[fail]}},'no_evidence_rights':{'development':{'evidence_use_rights':False}},
        'human_only_no_development':{'awards':{'architecture':{'new_robots':0}}},
        'paid_review_support_delayed':{'awards':{'qualified':{'resources':available_support(0)}}}}


def paid_development_summary(name,r):
    return {**architecture_awards_summary(name,r),**{k:r['development'][k] for k in ('completed_attempts','failed_completed_attempts','resource_cash_cents','failed_review_resource_cash_cents')}}


def continuation_comparison(continued,stopped,decision_month=3):
    """Compare future paid work only after proving the same realized prefix."""
    if type(decision_month) is not int or not 1<=decision_month<8:raise ValueError('Decision month must be inside the window')
    for key in ('plan','opening_treasury','source_sha256'):
        if continued[key]!=stopped[key]:raise ValueError('Continuation requires the same opening contract and code')
    if continued['commercial']['contracts']!=stopped['commercial']['contracts']:raise ValueError('Different commercial contract')
    for key in ('enterprise','finance','calendar_bridge','competition','entry_transition','staffed_renewals','annual_resources','component_inventory','architecture_execution'):
        if continued[key]['inputs']!=stopped[key]['inputs']:raise ValueError('Different continuation input: '+key)
    for key in ('months','events'):
        when=lambda x:x['month'] if key=='months' else x['at']['month']
        if [x for x in continued[key] if when(x)<decision_month]!=[x for x in stopped[key] if when(x)<decision_month]:raise ValueError('Different realized physical history')
    histories=[[e for e in r['closing_treasury']['events'] if e['at']['month']<decision_month] for r in (continued,stopped)]
    reviews=[[e for e in r['development']['events'] if e['month']<decision_month] for r in (continued,stopped)]
    if histories[0]!=histories[1] or reviews[0]!=reviews[1] or not any(e['status']=='failed' for e in reviews[0]):raise ValueError('No identical realized paid-failure history')
    outside={'manufacturer','deployment_vendor','enterprise_vendor','digital_vendor','entry_resource_vendor',RESOURCE_ACTOR}
    def future(r):
        invoices={i['invoice_id']:i for i in r['closing_treasury']['invoices']};payers={};staff=0
        for e in r['closing_treasury']['events']:
            if e['kind']!='invoice_payment' or e['at']['month']<decision_month:continue
            i=invoices[e['reference_id']]
            if i['payee'] in outside:payers[i['payer']]=payers.get(i['payer'],0)+e['settled_cents']
            if i['category']=='human_staff':staff+=e['settled_cents']
        return dict(resource_cash_cents=sum(payers.values()),resource_cash_by_payer=payers,regular_staff_cash_cents=staff,
            accepted_cleaning_zones=_rational(sum((Fraction(int(m['total_delivered_units']['numerator']),int(m['total_delivered_units']['denominator'])) for m in r['enterprise']['months'] if m['month']>=decision_month),Fraction())),
            completed_inventory_jobs=sum(m['outside_completed_jobs'] for m in r['staffed_renewals']['months'] if m['month']>=decision_month),
            closing_robot_states=[{'unit_id':u['unit_id'],'status':u['status']} for u in r['units']])
    a,b=future(continued),future(stopped);payers=sorted(set(a['resource_cash_by_payer'])|set(b['resource_cash_by_payer']));delta=a['resource_cash_cents']-b['resource_cash_cents']
    assert delta==continued['staffed_renewals']['cash']['all_payer_resource_and_transaction_cash_cents']-stopped['staffed_renewals']['cash']['all_payer_resource_and_transaction_cash_cents']
    return dict(decision_month=decision_month,same_realized_history_through_month=decision_month-1,continued_case='fail_then_pass',stopped_case='stop_after_paid_failure',continued=a,stopped=b,
        additional_resource_cash_cents=delta,regular_staff_cash_difference_cents=a['regular_staff_cash_cents']-b['regular_staff_cash_cents'],
        payer_differences=[{'payer':p,'continued_resource_cash_cents':a['resource_cash_by_payer'].get(p,0),'stopped_resource_cash_cents':b['resource_cash_by_payer'].get(p,0),'difference_cents':a['resource_cash_by_payer'].get(p,0)-b['resource_cash_by_payer'].get(p,0)} for p in payers],
        identical_future_service=(a['accepted_cleaning_zones'],a['completed_inventory_jobs'])==(b['accepted_cleaning_zones'],b['completed_inventory_jobs']),
        boundary='Saved reference policies share every realized physical/cash event through the paid failure. Future settled external-resource cash excludes past spending and internal fees. Terminal robot states differ and future benefits are unvalued; this is not an optimal stopping or lifecycle-value verdict. The human-only case is not a same-history counterfactual.')


def paid_development_artifact():
    options=paid_development_worlds();cases={name:run_paid_development_case(x) for name,x in options.items()}
    return canonical_wire(dict(schema_version='paid-development-artifact/0.1',case_inputs=options,cases=cases,summary=[paid_development_summary(name,r) for name,r in cases.items()],continuation_comparison=continuation_comparison(cases['fail_then_pass'],cases['stop_after_paid_failure']),source_sha256=source_hashes(),comparison_boundary='One synthetic unit and configuration, dated paid reviews and one actual service/Treasury/crew history. Completed failed work costs money; stopped work leaves hardware and obligations. Declared pass/fail outcomes are hypotheses, not measured qualification or training. A competent human-only policy retains the same service obligations. No empirical architecture ranking, optimal stopping or lifecycle ROI.'))


def paid_development_catalog():
    data=json.loads((ROOT/'model/results/paid_development.json').read_text())
    if data['source_sha256']!=source_hashes():raise ValueError('Paid-development export is stale; regenerate')
    return {k:v for k,v in data.items() if k!='cases'}|{'cases':{'pass_first_review':data['cases']['pass_first_review']}}
