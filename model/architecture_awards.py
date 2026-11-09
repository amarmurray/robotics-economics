"""One architectural service business and an actual human-led competitor.

Architecture roles change the staffing/asset payer, never the customer contract
owner or ultimate-equity register. Both businesses share one market history.
The competitor deliberately has no robots: a second architectural fleet needs
its own explicit role and qualification contract, which is not inferred here.
"""
from collections import defaultdict
from dataclasses import asdict,replace
from fractions import Fraction
import hashlib
import json

from model.architectures import GATES
from model.calendar_bridge import ROOT,Bridge,bridge_context,exact,rational
from model.component_inventory import ComponentInventory,read_components
from model.competitive_renewals import Competition
from model.engine import parameters,operation,capability_at
from model.enterprise_finance import FinancePlan,TermLoan
from model.entry_transitions import Transition
from model.monthly_architectures import (_ArchitectureEnterprise,ArchitectureExecution,ROLE_CASH,RESOURCE_ACTOR,
    resolved,canonical_wire,architecture_execution_hashes)
from model.monthly_commercial import restore_opening_inputs
from model.monthly_deployment import run_monthly
from model.monthly_enterprise import Business,CustomerMove,EnterprisePlan,Equity,Market,round_cents
from model.qualified_staffing import (_QualifiedStaffing,qualified_staffing_inputs,qualified_staffing_result,
    qualified_staffing_summary,source_hashes as qualified_hashes)
from model.annual_resource_ledger import read_resources
from model.shared_workforce import Workforce
from model.treasury import Account


def architecture_roles(config):
    settings,profile,_=resolved(config)
    entities=profile['role_entities']
    aliases={entities['customer']:'incumbent',entities['oem']:'provider'}
    return settings,profile,{role:aliases.get(entity,'arch:'+entity) for role,entity in entities.items()}


class _ArchitectureAwards(_ArchitectureEnterprise,_QualifiedStaffing):
    def __init__(self,plan,contracts,treasury,enterprise,finance,bridge,competition,transition,crews,resources,architecture):
        if not isinstance(architecture,ArchitectureExecution):raise ValueError('Explicit architecture contract required')
        self.architecture=architecture;self.settings,self.profile,self.roles=architecture_roles(architecture)
        base=parameters({'years':3,'capability_progress':0,**(architecture.annual_reference_overrides or {})})
        expected=parameters({**base,'integration_hours':base['integration_hours']*self.profile['integration_multiplier'],
            'intervention_minutes':base['intervention_minutes']+self.profile['support_minutes_delta']})
        if bridge.annual_overrides!=expected:raise ValueError('Explicit profile physical mapping required')
        if architecture.opening_robots!=0:raise ValueError('This joined fixture requires original paid manufacture, not opening robots')
        if plan.provider_actor!=self.roles['oem']:raise ValueError('The OEM must be the physical seller')
        if {b.operator_id:b.actor_id for b in enterprise.businesses}!={'incumbent':'incumbent','entrant':'entrant'}:
            raise ValueError('Preserve the two legal customer businesses')
        if any(o.opening_installed or (o.requested_additions if o.operator_id=='entrant' else o.requested_additions!=architecture.new_robots) for o in plan.operators):
            raise ValueError('Only the target has the explicitly configured architectural robot fleet')
        if any(c.arrangement!='sale' or c.deposit_cents or c.cancel_month is not None for c in contracts):
            raise ValueError('Outright robot purchase without deposit or cancellation required')
        if not bridge.digital_enabled:raise ValueError('The digital-improved human comparison is required')
        self.customer=self.roles['customer'];self.operator=self.roles['operator']
        self.resource_ids=set();self.transfer_ids=set();self.service_ids=set()
        self.arch_lines=[];self.arch_events=[];self.arch_months=[];self.qualified=set()
        self.prefees={};self.initial_work={};self.engineering_used=Fraction();self.demonstration_used=Fraction()
        # This explicit constructor preserves the old architecture's one-business
        # validator. Its inherited operational hooks cooperate with this new,
        # separately validated two-business contract through the actual MRO.
        _QualifiedStaffing.__init__(self,plan,contracts,treasury,enterprise,finance,bridge,competition,transition,crews,resources)
        funds=defaultdict(int)
        for role,amount in {**ROLE_CASH,**(architecture.role_opening_cash_cents or {})}.items():funds[self.roles[role]]+=amount
        if any(treasury.account(actor).opening_cash_cents!=amount for actor,amount in funds.items()):
            raise ValueError('Opening role allocations must sum to actual legal accounts')
        if RESOURCE_ACTOR in self.parties:raise ValueError('Architecture resources need an outside supplier')
        treasury.account(RESOURCE_ACTOR)
        for actor in self.roles.values():treasury.account(actor)
        self.parties=sorted(set(self.parties)|set(self.roles.values()))
        self.failed_gates=[name for name in GATES if not self.profile[name]]

    def crew_payer(self,operator_id):
        return self.operator if operator_id=='incumbent' else super().crew_payer(operator_id)

    def resource_vendors(self):return super().resource_vendors()|{RESOURCE_ACTOR}


def source_hashes():
    return {**qualified_hashes(),**architecture_execution_hashes(),
        'model/architecture_awards.py':hashlib.sha256((ROOT/'model/architecture_awards.py').read_bytes()).hexdigest()}


def run_architecture_awards(plan,treasury,contracts,enterprise,finance,bridge,competition,transition,crews,resources,components,architecture):
    policy=_ArchitectureAwards(plan,contracts,treasury,enterprise,finance,bridge,competition,transition,crews,resources,architecture)
    if components.system_id!=plan.system.system_id or components.onboard_configuration!=policy.annual['onboard_configuration']:
        raise ValueError('Parts must match the selected physical configuration')
    materials=ComponentInventory(components)
    return architecture_awards_result(run_monthly(plan,treasury,commercial=policy,materials=materials),policy,materials)


def architecture_awards_result(execution,policy,materials):
    """Format one completed history; do not create another execution or Treasury."""
    r=qualified_staffing_result(execution,policy,materials)
    r.pop('case_hash');r.update(schema_version='architecture-awards-window/0.1',scope='synthetic_one_architectural_business_human_competitor_paid_crews_entry_and_actual_awards')
    r['architecture_execution']=policy.architecture_result(r)
    a=r['architecture_execution'];a['contract'].update(active_service_businesses=2,architectural_service_businesses=1,
        staff_and_site_costs='The target service operator pays target regular staffing, prospective overtime, overhead, materials and site software. The rival funds its own human crew. Each customer company retains customer contracts and service receipts.',
        service_payment='The target customer company pays an explicit amount per accepted cleaning zone after delivery. The service scope includes its retained inventory duties; no additional inventory fee is assumed. Same-entity payments are eliminated.',
        competition='Actual fixed-lot customer awards use paid qualified capacity and prior service. The rival is a digital-improved human business with no robot fleet; a second architecture contract is not inferred.')
    a['limits']=[x for x in a['limits'] if not x.startswith('One active customer business')]+[
        'One architectural target and a human-led rival; two architectural fleets, optimal bids, shared adaptation and endogenous learning remain unimplemented.',
        'Fixed logical-role capital is summed by legal entity. A fixed synthetic share price is not a comparable enterprise valuation across different opening target cash or outsourcing arrangements.']
    for row in r['staffed_renewals']['months']:row['staffing_payer_actor_id']=policy.crew_payer(row['operator_id'])
    r['renewing_entry']['limits']=[x for x in r['renewing_entry']['limits'] if not x.startswith('Separate paid crews')]+[
        'Separate paid crews, qualified parts, annual support and one explicit target intelligence-role contract are joined. Asset recovery and endogenous learning remain separate.']
    r['annual_resources']['limits']=[x.replace('Four intelligence architectures, asset recovery and endogenous learning remain separate contracts.','One target architecture is joined; asset recovery and endogenous learning remain separate.') for x in r['annual_resources']['limits']]
    r['calendar_bridge']['cost_and_resource_contract']['additional_digital']='Site software and changed-version qualification retain calendar bills; itemized architecture resources replace the target robot digital bundle.'
    r['architecture_awards']=dict(staffing_payers={op:policy.crew_payer(op) for op in policy.crews},
        customer_contract_owners={op:b.actor_id for op,b in policy.business.items()},
        cash_boundary='Internal model, integration and operator service prices redistribute cash. All-payer resource/transaction cash includes the architecture resource supplier exactly once.',
        title_boundary='The architectural service operator buys and owns target robots. Acquiring the customer company does not transfer separately owned operator assets or pool its crew/cash.',
        scope='One selected architecture on the target; the rival is human-led. Each complete case has one physical, part, provider-resource, crew, Treasury and customer-award history.')
    r['competition']['operator_cash_semantics']='These rows identify the customer-contract businesses. A separately contracted physical service operator has its own account in architecture_execution.entities; customer cash is not its available staffing cash.'
    r['source_sha256']=source_hashes();r=canonical_wire(r)
    r['case_hash']=hashlib.sha256(json.dumps(r,sort_keys=True,separators=(',',':')).encode()).hexdigest()
    return json.loads(json.dumps(r))


def architecture_awards_inputs(inputs=None):
    if inputs is None:inputs={}
    if not isinstance(inputs,dict) or set(inputs)-{'architecture','qualified'}:raise ValueError('Unknown architecture-award inputs')
    if not isinstance(inputs.get('architecture',{}),dict) or not isinstance(inputs.get('qualified',{}),dict):raise ValueError('Explicit input objects required')
    cfg=ArchitectureExecution(**{'opening_robots':0,'new_robots':1,**inputs.get('architecture',{})})
    base=parameters({'years':3,'capability_progress':0,'digital_efficiency':.25,**(cfg.annual_reference_overrides or {})})
    cfg=replace(cfg,annual_reference_overrides=base)
    _,profile,roles=architecture_roles(cfg);funds=defaultdict(int)
    for role,amount in {**ROLE_CASH,**(cfg.role_opening_cash_cents or {})}.items():funds[roles[role]]+=amount
    x=dict(inputs.get('qualified',{}));staffed=dict(x.get('staffed',{}));entry=dict(staffed.get('entry',{}));market=dict(entry.get('market',{}))
    if set(entry)&{'target_cash_cents','human_efficiency'} or set(market)&{'incumbent_robots','entrant_robots','provider_cash_cents'}:
        raise ValueError('Role cash, human efficiency and robot counts belong to the architecture contract')
    entry.update(target_cash_cents=funds['incumbent'],human_efficiency=base['digital_efficiency'],
        market={**market,'incumbent_robots':cfg.new_robots,'entrant_robots':0,'provider_cash_cents':funds['provider']})
    staffed['entry']=entry;x['staffed']=staffed
    args=list(qualified_staffing_inputs(x));p,t,cs,e,f,b,c,tr,w,resources,parts=args
    effective=parameters({**base,'integration_hours':base['integration_hours']*profile['integration_multiplier'],
        'intervention_minutes':base['intervention_minutes']+profile['support_minutes_delta']})
    b=replace(b,annual_overrides=effective)
    _,annual,_,cell,system,calendar=bridge_context(b,p.months)
    physical=operation(cell,system,annual,capability_at(annual,0),False)
    p=replace(p,system=replace(p.system,bundled_start_cents=round_cents(exact(system['manufacture_cost_usd'])*100),
        commissioning_cents=round_cents(exact(annual['integration_hours'])*6000),
        support_cents_per_robot_month=round_cents(exact(physical['robot_operating_cost_usd'])*100/12)))
    cs=tuple(replace(c,arrangement='sale',lessor_actor=None) for c in cs)
    accounts=[replace(a,opening_cash_cents=funds[a.actor_id]) if a.actor_id in funds else a for a in t.accounts]
    seen={a.actor_id for a in accounts};accounts.extend(Account(actor,amount) for actor,amount in funds.items() if actor not in seen)
    if RESOURCE_ACTOR in seen:raise ValueError('Distinct architecture supplier account required')
    accounts.append(Account(RESOURCE_ACTOR,0));t=replace(t,accounts=tuple(accounts))
    return p,t,cs,e,f,b,c,tr,w,resources,parts,cfg


def run_architecture_awards_case(inputs=None):return run_architecture_awards(*architecture_awards_inputs(inputs))


def replay_architecture_awards(saved):
    if not isinstance(saved,dict) or saved.get('schema_version')!='architecture-awards-window/0.1':raise ValueError('Complete architecture-award case required')
    try:
        e=dict(saved['enterprise']['inputs']);e['market']=Market(**e['market'])
        for key,cls in [('businesses',Business),('moves',CustomerMove),('equity',Equity)]:e[key]=tuple(cls(**x) for x in e[key])
        f=dict(saved['finance']['inputs']);f['loans']=tuple(TermLoan(**x) for x in f['loans'])
        return run_architecture_awards(*restore_opening_inputs(saved),EnterprisePlan(**e),FinancePlan(**f),Bridge(**saved['calendar_bridge']['inputs']),
            Competition(**saved['competition']['inputs']),Transition(**saved['entry_transition']['inputs']),
            {op:Workforce(**w) for op,w in saved['staffed_renewals']['inputs'].items()},
            read_resources(saved['annual_resources']['inputs']),read_components(saved['component_inventory']['inputs']),
            ArchitectureExecution(**saved['architecture_execution']['inputs']))
    except (KeyError,TypeError,AttributeError) as exc:raise ValueError('Incomplete architecture-award inputs') from exc


def architecture_awards_worlds():
    stranded={'customer':40000000,'operator':0,'model_supplier':0,'integrator':0}
    return {**{name:{'architecture':{'architecture_id':name}} for name in ('integrated_oem','licensed_independent','open_adapted','model_led_operator')},
        'licensed_human_only':{'architecture':{'new_robots':0}},
        'model_operator_human_only':{'architecture':{'architecture_id':'model_led_operator','new_robots':0}},
        'model_capital_in_customer':{'architecture':{'architecture_id':'model_led_operator','role_opening_cash_cents':stranded}},
        'model_capital_in_customer_human_only':{'architecture':{'architecture_id':'model_led_operator','role_opening_cash_cents':stranded,'new_robots':0}},
        'open_one_engineering_hour_short':{'architecture':{'architecture_id':'open_adapted','engineering_hours_per_month':299}}}


def architecture_awards_summary(name,r):
    s=qualified_staffing_summary(name,r);a=r['architecture_execution'];op=a['role_entities']['operator'];entity=next(x for x in a['entities'] if x['actor_id']==op)
    s.update(architecture_id=a['inputs']['architecture_id'],operator_actor_id=op,
        opening_role_cash_cents=sum(x['opening_cash_cents'] for x in a['entities']),
        operator_due_unpaid_cents=entity['due_unpaid_cents'],operator_closing_cash_cents=entity['closing_cash_cents'],
        internal_nominal_transfers_eliminated_cents=a['consolidation']['internal_nominal_transfers_eliminated_cents'],
        architecture_resource_cash_cents=a['consolidation']['itemized_architecture_resource_cash_cents'])
    return s


def architecture_awards_artifact():
    options=architecture_awards_worlds();cases={k:run_architecture_awards_case(v) for k,v in options.items()}
    return canonical_wire(dict(schema_version='architecture-awards-artifact/0.1',case_inputs=options,cases=cases,
        summary=[architecture_awards_summary(k,r) for k,r in cases.items()],source_sha256=source_hashes(),
        comparison_boundary='Synthetic target intelligence-role contracts, actual customer awards, paid crews, entry, annual support and qualified parts share one execution. Logical-role opening capital totals are fixed across the displayed cases; its legal location varies. The human-led rival keeps a separate crew and cash account, including after common ownership with fixed separate offers. Outsourced staffing is not automatically customer payroll. No empirical architecture ranking, acquisition valuation or lifecycle ROI.'))


def architecture_awards_catalog():
    data=json.loads((ROOT/'model/results/architecture_awards.json').read_text())
    if data['source_sha256']!=source_hashes():raise ValueError('Architecture-award export is stale; regenerate')
    return {k:v for k,v in data.items() if k!='cases'}|{'cases':{'licensed_independent':data['cases']['licensed_independent']}}
