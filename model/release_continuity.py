"""Paid release review, prospective eligibility and supported retained versions.

One existing paid-development/architecture/crew/award history. Candidate rates,
review outcomes and entitlements are explicit hypotheses, never observed rights,
training results or a simulated acceptance trial.
"""
from dataclasses import asdict,dataclass,replace
from fractions import Fraction
import hashlib,json

from model.architecture_awards import architecture_awards_result
from model.paid_development import (_PaidDevelopment,paid_development_inputs,paid_development_summary,
    read_development,source_hashes as development_hashes)
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
from model.architectures import ROLES
from model.shared_workforce import Workforce
from model.treasury import Moment

SCHEMA='release-continuity-window/0.1'


def release_paths(legacy,candidate):
    return {'schema_version':'digital-annual-paths/0.1','base_year':2026,'epistemic_status':'synthetic_assumption','coordination':[legacy,candidate,candidate]}


@dataclass(frozen=True)
class ReleasePlan:
    release_id: str='candidate-coordination-2027'
    unit_id: str='start-shared-supply-1'
    evidence_id: str='release-review-evidence-1'
    release_available_month: int=6
    review_month: int=6
    review_engineering_hours: int=40
    review_payer_role: str='model_supplier'
    declared_review_pass: bool=True
    collection_allowed: bool=True
    evidence_use_rights: bool=True
    candidate_operating_rights: bool=True
    adopt_after_review: bool=True
    legacy_support_through_month: int=7
    candidate_coordination: float=0.5

    def __post_init__(self):
        for v in (self.release_id,self.unit_id,self.evidence_id):
            if not isinstance(v,str) or not v.strip() or len(v)>100:raise ValueError('Named bounded release/unit/evidence IDs required')
        for k in ('declared_review_pass','collection_allowed','evidence_use_rights','candidate_operating_rights','adopt_after_review'):
            if type(getattr(self,k)) is not bool:raise ValueError('Explicit Boolean release premise required')
        for k in ('release_available_month','review_month'):
            if type(getattr(self,k)) is not int or not 0<=getattr(self,k)<8:raise ValueError('Release/review month must be within eight-month window')
        if self.review_month<self.release_available_month:raise ValueError('Cannot review an unavailable release')
        if type(self.review_engineering_hours) is not int or not 1<=self.review_engineering_hours<=1000:raise ValueError('Bounded positive engineering hours required')
        if type(self.legacy_support_through_month) is not int or not -1<=self.legacy_support_through_month<=7:raise ValueError('Explicit bounded legacy entitlement end required')
        if self.review_payer_role not in ROLES:raise ValueError('Review payer must be a declared architecture role')
        if type(self.candidate_coordination) not in (int,float) or not 0<=self.candidate_coordination<=0.8:raise ValueError('Bounded candidate coordination premise required')


def read_release(value):
    if not isinstance(value,dict):raise ValueError('Complete release plan required')
    try:return ReleasePlan(**value)
    except TypeError as exc:raise ValueError('Unknown release plan field') from exc


def source_hashes():
    return {**development_hashes(),'model/release_continuity.py':hashlib.sha256((ROOT/'model/release_continuity.py').read_bytes()).hexdigest()}


class _ReleaseContinuity(_PaidDevelopment):
    def __init__(self,*args,development,release):
        # target_vintage is not called during construction; all version state is
        # set before the first prospective monthly booking is issued.
        super().__init__(*args,development=development);self.release=release
        if self.architecture.new_robots!=1:raise ValueError('One actual target robot required for this retained-version contract')
        if self.calendar[0]['annual_period_index']!=0 or self.calendar[release.release_available_month]['annual_period_index']!=1:
            raise ValueError('This contract binds the 2026 retained version to a 2027 release')
        ids={f'start-{s.order_id}-{i+1}' for s in self.plan.starts for i in range(s.quantity)}
        if release.unit_id not in ids:raise ValueError('Release review names an absent physical unit')
        if release.evidence_id in {a.evidence_id for a in development.attempts}:raise ValueError('Release evidence must be distinct from initial review evidence')
        if self.annual['years']!=3:raise ValueError('Three-year annual assumption horizon required')
        expected=release_paths(self.annual['coordination'],release.candidate_coordination)
        if self.bridge.digital_paths!=expected:raise ValueError('Calendar path must match the explicit candidate premise')
        if self.bridge.software_policy!='paid_calendar_upgrade':raise ValueError('Release policy requires explicit paid deployment qualification')
        self.release_review=None;self.release_events=[];self.release_months=[];self.release_approved_month=None
        self.release_resource_ids=set()

    def target_vintage(self,unit,month):
        old=self.vintage.get(unit.unit_id,0)
        eligible=(self.release.adopt_after_review and self.release.candidate_operating_rights and
            self.release_approved_month is not None and month>self.release_approved_month and month>=self.release.release_available_month)
        return 1 if eligible else old

    def prepare(self,t,month,units):
        t=super().prepare(t,month,units);p=self.release
        if month!=p.review_month:return t
        u=next((u for u in units if u.unit_id==p.unit_id),None)
        reason='retain_legacy_policy' if not p.adopt_after_review else 'collection_not_allowed' if not p.collection_allowed else \
            'review_evidence_rights_unavailable' if not p.evidence_use_rights else \
            'unit_not_installed_and_initially_qualified' if u is None or u.status!='installed' or u.unit_id not in self.review_passed else ''
        event=dict(month=month,release_id=p.release_id,unit_id=p.unit_id,evidence_id=p.evidence_id,
            candidate_operating_rights=p.candidate_operating_rights,declared_review_pass=p.declared_review_pass)
        if reason:self.release_events.append({**event,'status':'not_attempted','reason':reason,'engineering_hours':0,'resource_cash_cents':0});return t
        value=p.review_engineering_hours*exact(self.settings['common']['engineering_usd_hour'])*100
        t,iid=self.arch_charge(t,month,3,self.roles[p.review_payer_role],RESOURCE_ACTOR,'release_review_resource',value,p.unit_id,resource=True)
        self.release_review=(event,iid)
        return t

    def mandatory(self,t,month):
        t=super().mandatory(t,month)
        if not self.release_review or month!=self.release.review_month:return t
        event,iid=self.release_review;p=self.release
        reason='engineering_hours_unavailable' if self.engineering_used+p.review_engineering_hours>self.architecture.engineering_hours_per_month else ''
        candidate=t
        if not reason and iid:
            candidate=candidate.settle_invoice(iid+':release-pay',iid,Moment(month,3),provenance=self.provenance)
            if candidate.invoice(iid).outstanding_cents:reason='review_payer_unfunded'
        if reason:
            if iid:t=t.cancel_invoice(iid+':release-cancel',iid,Moment(month,3),provenance=self.provenance)
            self.release_events.append({**event,'status':'not_attempted','reason':reason,'invoice_id':iid,'engineering_hours':0,'resource_cash_cents':0})
        else:
            t=candidate;self.engineering_used+=p.review_engineering_hours
            if iid:self.release_resource_ids.add(iid)
            if p.declared_review_pass:self.release_approved_month=month
            self.release_events.append({**event,'status':'passed' if p.declared_review_pass else 'failed','reason':'declared_synthetic_review_outcome',
                'invoice_id':iid,'engineering_hours':p.review_engineering_hours,'resource_cash_cents':t.invoice(iid).paid_cents if iid else 0,
                'earliest_adoption_month':month+1 if p.declared_review_pass else None})
        self.current_treasury=t
        return t

    def admit(self,t,iid,month,phase,physical_reason,unit=None,operator_id=None):
        if t.invoice(iid).category in ('commission','support'):
            _,target,_=self.robot_invoices[(month,unit.unit_id)]
            if target==0 and month>self.release.legacy_support_through_month:physical_reason=physical_reason or 'legacy_support_entitlement_expired'
            if target==1 and not self.release.candidate_operating_rights:physical_reason=physical_reason or 'candidate_operating_rights_unavailable'
        return super().admit(t,iid,month,phase,physical_reason,unit,operator_id)

    def close(self,t,month,units,supported):
        super().close(t,month,units,supported)
        u=next((u for u in units if u.unit_id==self.release.unit_id),None);cohort=self.supported.get(self.release.unit_id)
        self.release_months.append(dict(month=month,unit_id=self.release.unit_id,physical_state=u.status if u else 'not_yet_manufactured',
            admitted_version_index=self.vintage.get(self.release.unit_id),supported_version_index=cohort['annual_period_index'] if cohort else None,
            supported=self.release.unit_id in supported,review_approved_month=self.release_approved_month,
            legacy_support_entitled=month<=self.release.legacy_support_through_month,candidate_operating_rights=self.release.candidate_operating_rights,
            candidate_eligible_next_booking=bool(self.release.adopt_after_review and self.release.candidate_operating_rights and self.release_approved_month is not None and month>=self.release_approved_month)))

    def release_result(self,r):
        invoices={i['invoice_id']:i for i in r['closing_treasury']['invoices']};paid=sum(invoices[i]['paid_cents'] for i in self.release_resource_ids)
        assert paid==sum(e['resource_cash_cents'] for e in self.release_events)
        return dict(inputs=asdict(self.release),events=self.release_events,months=self.release_months,resource_cash_cents=paid,
            review_payer_actor_id=self.roles[self.release.review_payer_role],adopted_month=next((m['month'] for m in self.release_months if m['supported_version_index']==1),None),
            unsupported_after_legacy_expiry_months=[m['month'] for m in self.release_months if m['physical_state']=='installed' and not m['legacy_support_entitled'] and not m['supported']],
            work_boundary='Provider-funded specialist release evaluation is additional work, separate from initial model work and the existing funded deployment-qualification booking. It consumes the same architecture engineering pool. Completed failed review stays paid; a blocked review performs no work. No model training or physical trial is simulated.',
            eligibility_clock='A paid declared pass makes the candidate eligible only in the following month. The old qualified version continues only under the declared legacy support entitlement. Candidate operating rights are distinct from rights to review evidence.',
            service_boundary='Qualification, physical stock, actual support, license/support entitlement and complete accepted service are separate. A pass supplies no provider capacity, spare, operating right or paid crew. There is no automatic rollback after a failed changed-version booking.',
            cash_boundary='Release review resources are included once in all-payer resource cash. The declared provider pays the review; no extra customer fee is invented. Deployment qualification keeps its existing invoice and shared provider-support hours.',
            limits=['One unchanged hardware configuration and a single dated coordination-release hypothesis; no shared learning, altered architecture roles, onboard-compute replacement or actual vendor entitlement.',
                'Review outcomes and candidate rates are declared premises, not statistical acceptance evidence or an empirical learning curve.',
                'The paid calendar qualification can still fail after eligibility; automatic same-month legacy failover or rollback is not implemented.',
                'Eight fixed monthly periods and declared policies; no optimal release schedule, commercial pricing or lifecycle ROI.'])


def release_continuity_inputs(inputs=None):
    if inputs is None:inputs={}
    if not isinstance(inputs,dict) or set(inputs)-{'base','release'}:raise ValueError('Expected base and release inputs')
    p=read_release(inputs.get('release',{}));args=list(paid_development_inputs(inputs.get('base',{})));bridge=args[5];annual=bridge.annual_overrides
    args[5]=replace(bridge,digital_paths=release_paths(annual['coordination'],p.candidate_coordination))
    return (*args,p)


def run_release_continuity(plan,treasury,contracts,enterprise,finance,bridge,competition,transition,crews,resources,components,architecture,development,release):
    policy=_ReleaseContinuity(plan,contracts,treasury,enterprise,finance,bridge,competition,transition,crews,resources,architecture,development=development,release=release)
    if components.system_id!=plan.system.system_id or components.onboard_configuration!=policy.annual['onboard_configuration']:raise ValueError('Parts must match the reviewed hardware configuration')
    materials=ComponentInventory(components);r=architecture_awards_result(run_monthly(plan,treasury,commercial=policy,materials=materials),policy,materials)
    r.pop('case_hash');r.update(schema_version=SCHEMA,scope='synthetic_reviewed_release_retained_entitlement_and_actual_whole_service',development=policy.development_result(r),release=policy.release_result(r),source_sha256=source_hashes());r=canonical_wire(r);r['case_hash']=hashlib.sha256(json.dumps(r,sort_keys=True,separators=(',',':')).encode()).hexdigest();return r


def run_release_continuity_case(inputs=None):return run_release_continuity(*release_continuity_inputs(inputs))


def replay_release_continuity(saved):
    if not isinstance(saved,dict) or saved.get('schema_version')!=SCHEMA:raise ValueError('Complete release-continuity case required')
    try:
        e=dict(saved['enterprise']['inputs']);e['market']=Market(**e['market'])
        for key,cls in [('businesses',Business),('moves',CustomerMove),('equity',Equity)]:e[key]=tuple(cls(**x) for x in e[key])
        f=dict(saved['finance']['inputs']);f['loans']=tuple(TermLoan(**x) for x in f['loans'])
        return run_release_continuity(*restore_opening_inputs(saved),EnterprisePlan(**e),FinancePlan(**f),Bridge(**saved['calendar_bridge']['inputs']),Competition(**saved['competition']['inputs']),Transition(**saved['entry_transition']['inputs']),
            {op:Workforce(**w) for op,w in saved['staffed_renewals']['inputs'].items()},read_resources(saved['annual_resources']['inputs']),read_components(saved['component_inventory']['inputs']),
            ArchitectureExecution(**saved['architecture_execution']['inputs']),read_development(saved['development']['inputs']),read_release(saved['release']['inputs']))
    except (KeyError,TypeError,AttributeError) as exc:raise ValueError('Incomplete release/service opening inputs') from exc


def release_continuity_worlds():
    expired={'declared_review_pass':False,'legacy_support_through_month':5}
    return {'reviewed_release_supported_legacy':{},'failed_review_supported_legacy':{'release':{'declared_review_pass':False}},
        'failed_review_legacy_expired':{'release':expired},'retain_staff_through_expiry':{'release':expired,'base':{'awards':{'qualified':{'staffed':{'crews':{'incumbent':{'target_blocks':None}}}}}}},
        'review_pass_without_operating_rights':{'release':{'candidate_operating_rights':False,'legacy_support_through_month':5}},
        'retain_supported_legacy':{'release':{'adopt_after_review':False}}}


def release_continuity_summary(name,r):
    return {**paid_development_summary(name,r),'release_review_cash_cents':r['release']['resource_cash_cents'],'adopted_month':r['release']['adopted_month'],
        'unsupported_after_legacy_expiry_months':r['release']['unsupported_after_legacy_expiry_months']}


def release_continuity_artifact():
    options=release_continuity_worlds();cases={name:run_release_continuity_case(x) for name,x in options.items()}
    return canonical_wire(dict(schema_version='release-continuity-artifact/0.1',case_inputs=options,cases=cases,summary=[release_continuity_summary(name,r) for name,r in cases.items()],source_sha256=source_hashes(),comparison_boundary='One synthetic physical and paid-service history with a dated candidate, specialist review, prospective eligibility and explicit legacy entitlement. A retained version is usable only under the assumed contract. Rights to review evidence do not establish operating rights. Human fallback remains subject to actual paid capacity and retained duties. No observed license, learning effect or lifecycle return is inferred.'))


def release_continuity_catalog():
    data=json.loads((ROOT/'model/results/release_continuity.json').read_text())
    if data['source_sha256']!=source_hashes():raise ValueError('Release-continuity export is stale; regenerate')
    return {k:v for k,v in data.items() if k!='cases'}|{'cases':{'reviewed_release_supported_legacy':data['cases']['reviewed_release_supported_legacy']}}
