"""Funded intelligence roles on the existing calendar, physical and cash loop.

Synthetic per-unit qualification contracts; no baseline-cost credit, new fleet,
LLM invocation or empirical rights/price assertion is introduced.
"""
from __future__ import annotations
from collections import defaultdict
from dataclasses import asdict, dataclass, replace
from fractions import Fraction
import hashlib
import json

from model.architectures import GATES, ROLES, catalog as architecture_catalog, resolve
from model.calendar_bridge import (ROOT, Bridge, _BridgedEnterprise, bridge_case_inputs,
    bridge_source_hashes, exact, rational, wire_rationals)
from model.engine import parameters
from model.enterprise_finance import FinancePlan, TermLoan
from model.monthly_commercial import restore_opening_inputs
from model.monthly_deployment import Moment, Start, _integer, _rational, run_monthly
from model.monthly_enterprise import Business, CustomerMove, EnterprisePlan, Equity, Market, round_cents
from model.treasury import Account, Treasury
from model.trajectories import parameters_at

ROLE_CASH={"customer":20_000_000,"operator":10_000_000,"oem":20_000_000,
           "model_supplier":5_000_000,"integrator":5_000_000}
RESOURCE_ACTOR='architecture_resources'
IDLE_ACTOR='architecture_idle_business'


@dataclass(frozen=True)
class ArchitectureExecution:
    architecture_id: str = 'licensed_independent'
    architecture_overrides: dict | None = None
    annual_reference_overrides: dict | None = None
    role_opening_cash_cents: dict | None = None
    engineering_hours_per_month: int = 400
    demonstration_hours_per_month: int = 100
    service_cents_per_accepted_zone: int = 600
    service_collection_lag_months: int = 1
    opening_robots: int = 2
    new_robots: int = 2

    def __post_init__(self):
        settings=resolve(self.architecture_overrides)
        if self.annual_reference_overrides is not None and not isinstance(self.annual_reference_overrides,dict):raise ValueError('Annual reference overrides must be an object')
        parameters({'years':3,'capability_progress':0,**(self.annual_reference_overrides or {})})
        if self.architecture_id not in settings['profiles']:raise ValueError('Unknown intelligence architecture')
        for name in ('engineering_hours_per_month','demonstration_hours_per_month','service_cents_per_accepted_zone','opening_robots','new_robots'):
            _integer(getattr(self,name))
            if getattr(self,name)>1_000_000:raise ValueError('Architecture experiment input exceeds declared range')
        _integer(self.service_collection_lag_months,1)
        if self.opening_robots>4 or self.new_robots>4:raise ValueError('Bounded architecture fixture allows at most four opening/new robots each')
        if self.service_collection_lag_months>36:raise ValueError('Service receipt lag exceeds declared horizon range')
        cash=self.role_opening_cash_cents
        if cash is not None and (not isinstance(cash,dict) or set(cash)-set(ROLES)):raise ValueError('Unknown logical-role cash allocation')
        for amount in (cash or {}).values():
            _integer(amount)
            if amount>1_000_000_000:raise ValueError('Role cash exceeds declared experiment range')
        defaults=architecture_catalog()['defaults']['common']
        for name in ('service_price_fraction','receiver_surplus_usd_year','payer_surplus_usd_year'):
            if settings['common'][name]!=defaults[name]:
                raise ValueError(name+' belongs to the separate annual reference, not this monthly contract')
        mapping=settings['profiles'][self.architecture_id]['role_entities']
        if mapping['oem'] in (mapping['customer'],mapping['operator']):raise ValueError('This contract requires an independent hardware seller')


def canonical_wire(value):
    """Equivalent JSON numbers (3 and 3.0) share one browser-stable hash."""
    def normalize(item):
        if isinstance(item,dict):return {key:normalize(x) for key,x in item.items()}
        if isinstance(item,(list,tuple)):return [normalize(x) for x in item]
        if type(item) is float and item.is_integer():return int(item)
        return item
    return wire_rationals(normalize(value))


def resolved(config):
    settings=resolve(config.architecture_overrides)
    profile=settings['profiles'][config.architecture_id]
    roles={key:'arch:'+value for key,value in profile['role_entities'].items()}
    return settings,profile,roles


class _ArchitectureEnterprise(_BridgedEnterprise):
    def __init__(self,plan,contracts,treasury,enterprise,finance,bridge,architecture):
        if not isinstance(architecture,ArchitectureExecution):raise ValueError('Explicit architecture contract required')
        self.architecture=architecture
        self.settings,self.profile,self.roles=resolved(architecture)
        base=parameters({'years':3,'capability_progress':0,**(architecture.annual_reference_overrides or {})})
        expected=parameters({**base,'integration_hours':base['integration_hours']*self.profile['integration_multiplier'],
            'intervention_minutes':base['intervention_minutes']+self.profile['support_minutes_delta']})
        if bridge.annual_overrides!=expected:raise ValueError('Effective bridge parameters must match the explicit architecture reference mapping')
        self.customer=self.roles['customer'];self.operator=self.roles['operator']
        self.resource_ids=set();self.transfer_ids=set();self.service_ids=set()
        self.arch_lines=[];self.arch_events=[];self.arch_months=[];self.qualified=set()
        self.prefees={};self.initial_work={};self.engineering_used=Fraction();self.demonstration_used=Fraction()
        if plan.provider_actor!=self.roles['oem']:raise ValueError('Hardware seller must match the OEM role')
        if enterprise.businesses[0].actor_id!=self.customer or enterprise.market.incumbent_operator!='incumbent':
            raise ValueError('Architecture customer must match the one active market business')
        if any(b.active_from_month is not None for b in enterprise.businesses if b.operator_id!='incumbent'):
            raise ValueError('This architecture mapping has one active service business')
        if any(c.arrangement!='sale' or c.deposit_cents or c.cancel_month is not None for c in contracts):
            raise ValueError('This role contract requires outright purchase without deposit/cancellation')
        super().__init__(plan,contracts,treasury,enterprise,finance,bridge)
        if not bridge.digital_enabled:raise ValueError('Architecture fixture requires the declared digital-human baseline')
        expected_cash=defaultdict(int)
        for role,amount in {**ROLE_CASH,**(architecture.role_opening_cash_cents or {})}.items():expected_cash[self.roles[role]]+=amount
        if any(treasury.account(actor).opening_cash_cents!=amount for actor,amount in expected_cash.items()):
            raise ValueError('Opening legal accounts must equal declared logical-role capital allocations')
        active=next(o for o in plan.operators if o.operator_id=='incumbent')
        if active.opening_installed!=architecture.opening_robots or active.requested_additions!=architecture.new_robots:
            raise ValueError('Physical counts must match the declared architecture fixture')
        if any(o.opening_installed or o.requested_additions for o in plan.operators if o.operator_id!='incumbent'):
            raise ValueError('No second physical business is mapped in this architecture fixture')
        if RESOURCE_ACTOR in self.parties:raise ValueError('Architecture resources require an outside counterparty')
        treasury.account(RESOURCE_ACTOR)
        for actor in self.roles.values():treasury.account(actor)
        self.parties=sorted(set(self.parties)|set(self.roles.values()))
        self.failed_gates=[name for name in GATES if not self.profile[name]]

    def _owner(self,c):
        return self.operator if c.operator_id=='incumbent' else super()._owner(c)

    def payer(self,action,unit):
        if unit is not None and unit.operator_id=='incumbent':
            if action=='support':return self.operator
            if action=='commission':return self.roles['integrator']
        return super().payer(action,unit)

    def _issue(self,t,iid,c,payer,payee,cents,at,eligible,category,cancellable=False):
        if c.operator_id=='incumbent' and category=='hardware_purchase':payer=self.operator
        return super()._issue(t,iid,c,payer,payee,cents,at,eligible,category,cancellable)

    def issue_enterprise(self,t,iid,payer,payee,amount,at,due,category,cancellable=False):
        if payer==self.customer and category in ('human_staff','overhead','materials','site_digital_subscription'):
            payer=self.operator
        return super().issue_enterprise(t,iid,payer,payee,amount,at,due,category,cancellable)

    def charge(self,t,month,phase,payer,category,amount,unit_id=None,cancellable=True):
        if category=='robot_digital_subscription':
            return t,None  # Replaced by itemized inference, maintenance and fees below.
        if category=='software_upgrade_qualification' and unit_id:
            payer=self.operator
        if category=='site_digital_subscription' and payer==self.customer:payer=self.operator
        return super().charge(t,month,phase,payer,category,amount,unit_id,cancellable)

    def arch_charge(self,t,month,phase,payer,payee,category,amount,unit_id=None,resource=False,cancellable=True,due=None):
        exact_cents=Fraction(amount);rounded=round_cents(exact_cents)
        iid=self._id('architecture',month,category,unit_id or payer)
        internal=payer==payee
        self.arch_lines.append({'month':month,'unit_id':unit_id,'category':category,
            'payer':payer,'payee':payee,'resource_expense':resource,'internal_eliminated':internal,
            'exact_cents':_rational(exact_cents),'nominal_cents':rounded,
            'rounding_difference_cents':_rational(Fraction(rounded)-exact_cents),
            'invoice_id':iid if rounded and not internal else None})
        if not rounded or internal:return t,None
        t=super().issue_enterprise(t,iid,payer,payee,rounded,Moment(month,1 if phase<6 else 6),
                                  due or Moment(month,phase),category,cancellable)
        if resource:self.resource_ids.add(iid);self.enterprise_cost_ids.add(iid)
        else:self.transfer_ids.add(iid)
        return t,iid

    def prepare(self,t,month,units):
        self.engineering_used=Fraction();self.demonstration_used=Fraction()
        t=super().prepare(t,month,units)
        a=self.profile;common=self.settings['common'];wage=exact(self.cell['wage_usd_hour'])
        engineering=exact(common['engineering_usd_hour']);roles=self.roles
        for u in units:
            key=(month,u.unit_id)
            if key not in self.robot_invoices:continue
            extras,target,upgrade=self.robot_invoices[key]
            phase=3 if u.status=='installed' else 4
            initial=u.unit_id not in self.qualified
            validation=exact(a['validation_engineering_hours'])*engineering+exact(a['qualification_resources_usd'])
            integration=exact(self.annual['integration_hours'])*60 if phase==4 else Fraction()
            initial_costs=[]
            if initial:
                initial_costs=[('customer','demonstration_collection',exact(a['demonstration_hours'])*wage),
                    ('customer','customer_path_setup',exact(common[common['customer_path']+'_setup_usd'])),
                    ('model_supplier','model_adaptation_engineering',exact(a['adaptation_engineering_hours'])*engineering),
                    ('model_supplier','model_adaptation_compute',exact(a['adaptation_compute_usd'])),
                    ('model_supplier','allocated_model_development',exact(a['model_development_allocation_usd_upfront'])),
                    ('integrator','qualification_validation',validation)]
            transfers=[('operator','model_supplier','model_monthly_fee',exact(common['model_fee_usd_year'])/12)]
            if initial:transfers.append(('operator','model_supplier','model_upfront_payment',exact(a['model_upfront_payment_usd'])))
            if integration or initial:
                transfers.append(('operator','integrator','integration_validation_payment',(integration+(validation if initial else 0))*(1+exact(common['integration_markup']))))
            if phase==4:transfers.append(('operator','integrator','commission_support_passthrough',Fraction(self.plan.system.support_cents_per_robot_month,100)))
            fees=[]
            for payer,payee,category,value in transfers:
                t,iid=self.arch_charge(t,month,phase,roles[payer],roles[payee],category,value*100,u.unit_id)
                if iid:fees.append(iid)
            # Parent's annual path determines the admitted vintage; the opaque bundle is absent.
            annual_price=parameters_at(self.annual,self.paths,target)['digital_cost_usd']
            costs=initial_costs+[
                ('model_supplier','inference_resources',exact(annual_price)*exact(a['inference_resource_multiplier'])/12),
                ('model_supplier','model_maintenance',exact(a['model_maintenance_usd_year'])/12),
                ('operator','network_resilience',exact(a['network_resilience_usd_year'])/12)]
            for role,category,value in costs:
                t,iid=self.arch_charge(t,month,phase,roles[role],RESOURCE_ACTOR,category,value*100,u.unit_id,resource=True)
                if iid:extras.append(iid)
            self.prefees[key]=fees
            self.initial_work[key]=(initial,exact(a['adaptation_engineering_hours'])+exact(a['validation_engineering_hours']) if initial else Fraction(),exact(a['demonstration_hours']) if initial else Fraction())
        return t

    def collect(self,t,month):
        t=super().collect(t,month)
        return self.collect_set(t,month,2,self.service_ids)

    def mandatory(self,t,month):
        t=super().mandatory(t,month)
        business_actors={b.actor_id for b in self.enterprise.businesses}
        due={i.invoice_id for i in t.invoices if i.payer in self.parties and i.payer not in business_actors
             and not i.cancellable and i.invoice_id not in self.interest_ids}
        t=self.collect_set(t,month,3,due)
        self.current_treasury=t
        return t

    def ready(self,t,b,month,phase=5):
        if not super().ready(t,b,month,phase):return False
        if b.operator_id!='incumbent':return True
        return not self.halted(self.operator) and not any(i.payer==self.operator and not i.cancellable
                    and i.outstanding_cents and i.due_at<=Moment(month,phase) for i in t.invoices)

    def _reason(self,t,month,phase,action,operator_id):
        if self.failed_gates and action in ('start','ship'):return 'architecture_assumption_not_admitted'
        return super()._reason(t,month,phase,action,operator_id)

    def admit(self,t,iid,month,phase,physical_reason,unit=None,operator_id=None):
        action=t.invoice(iid).category
        if action not in ('support','commission'):return super().admit(t,iid,month,phase,physical_reason,unit,operator_id)
        key=(month,unit.unit_id);initial,engineering,demo=self.initial_work[key]
        reason=physical_reason
        if self.failed_gates:reason=reason or 'architecture_assumption_not_admitted'
        if self.engineering_used+engineering>self.architecture.engineering_hours_per_month:reason=reason or 'architecture_engineering_hours'
        if self.demonstration_used+demo>self.architecture.demonstration_hours_per_month:reason=reason or 'architecture_demonstration_hours'
        candidate=t
        if not reason:
            for fee in self.prefees[key]:
                candidate=candidate.settle_invoice(fee+':pay',fee,Moment(month,phase),provenance=self.provenance)
                if candidate.invoice(fee).outstanding_cents:reason='funding:'+candidate.invoice(fee).category;break
        candidate,reason=super().admit(candidate,iid,month,phase,reason,unit,operator_id)
        if not reason:
            if initial:self.qualified.add(unit.unit_id)
            self.engineering_used+=engineering;self.demonstration_used+=demo
            self.arch_events.append({'month':month,'unit_id':unit.unit_id,'action':'admitted','initial_qualification':initial,
                'engineering_hours':_rational(engineering),'demonstration_hours':_rational(demo)})
            return candidate,''
        # Roll back the entire contingent group, including fee receipts. No parent
        # vintage/resource state advances on failure; fixed staff/site costs remain.
        for invoice in [iid,*self.prefees[key],*self.robot_invoices[key][0]]:
            if t.invoice(invoice).outstanding_cents:
                t=t.cancel_invoice(invoice+':architecture-cancel',invoice,Moment(month,phase),provenance=self.provenance)
        self.arch_events.append({'month':month,'unit_id':unit.unit_id,'action':'blocked','reason':reason,'committed_contingent_cash_cents':0})
        return t,reason

    def bill_service(self,t,month,units,supported):
        t=super().bill_service(t,month,units,supported)
        output=rational(self.period_service['incumbent']['total_delivered_units'])
        t,iid=self.arch_charge(t,month,6,self.customer,self.operator,'operating_service_payment',
            output*self.architecture.service_cents_per_accepted_zone,cancellable=False,
            due=Moment(month+self.architecture.service_collection_lag_months,2))
        if iid:self.service_ids.add(iid)
        return t

    def close(self,t,month,units,supported):
        super().close(t,month,units,supported)
        for asset in self.months[-1]['assets']:
            if asset['contract_id']==self.by_site['incumbent'].contract_id and asset['physical_state']=='installed':
                asset.update(custodian=self.operator,workflow_authority=self.operator,
                    data_and_ip_rights='scenario premise only; real rights not established')
        for row in self.bridge_months[-1]['human_work']:
            row['paying_actor_id']=self.operator if row['operator_id']=='incumbent' else self.business[row['operator_id']].actor_id
        self.arch_months.append({'month':month,'engineering_hours_used':_rational(self.engineering_used),
            'demonstration_hours_used':_rational(self.demonstration_used),'qualified_unit_ids':sorted(self.qualified),
            'operating_customer':self.customer,'physical_operator':self.operator})

    def architecture_result(self,r):
        invoices={i['invoice_id']:i for i in r['closing_treasury']['invoices']}
        lines=[{**row,'paid_cents':invoices[row['invoice_id']]['paid_cents'] if row['invoice_id'] else 0,
                'outstanding_cents':invoices[row['invoice_id']]['outstanding_cents'] if row['invoice_id'] else 0} for row in self.arch_lines]
        opening={a['actor_id']:a['cash_cents'] for a in r['opening_treasury']['actors']}
        closing={a['actor_id']:a['cash_cents'] for a in r['closing_treasury']['actors']}
        entities=[]
        for actor in sorted(set(self.roles.values())):
            entities.append({'actor_id':actor,'roles':[k for k,v in self.roles.items() if v==actor],
                'opening_cash_cents':opening[actor],'closing_cash_cents':closing[actor],
                'cash_change_cents':closing[actor]-opening[actor],
                'due_unpaid_cents':sum(i['outstanding_cents'] for i in invoices.values() if i['payer']==actor and not i['cancellable'] and (i['due_at']['month'],i['due_at']['phase'])<=(self.plan.months-1,7))})
        base=r['enterprise']['consolidation'];resource=sum(row['paid_cents'] for row in lines if row['resource_expense'])
        assert r['finance']['consolidation']['unclassified_other_boundary_cash_cents']==0
        assert sum(closing.values())==sum(opening.values())
        return {'schema_version':'monthly-intelligence-architectures/0.1','inputs':{**asdict(self.architecture),
                'architecture_overrides':self.settings,'role_opening_cash_cents':{**ROLE_CASH,**(self.architecture.role_opening_cash_cents or {})},
                'annual_reference_overrides':parameters({'years':3,'capability_progress':0,**(self.architecture.annual_reference_overrides or {})})},
            'effective_settings':self.settings,'profile':self.profile,'role_entities':self.roles,
            'status':'robot_policy_not_admitted' if self.failed_gates else 'synthetic_conditional_execution',
            'failed_assumptions':self.failed_gates,'empirical_qualification':'not_established',
            'entities':entities,'months':self.arch_months,'events':self.arch_events,'cash_lines':lines,
            'consolidation':{'opening_role_cash_cents':sum(row['opening_cash_cents'] for row in entities),
                'itemized_architecture_resource_cash_cents':resource,
                'external_physical_and_enterprise_cash_cents':base['external_physical_outlay_cents']+base['external_enterprise_outlay_cents'],
                'architecture_transfers_paid_cents':sum(row['paid_cents'] for row in lines if not row['resource_expense']),
                'internal_nominal_transfers_eliminated_cents':sum(row['nominal_cents'] for row in lines if row['internal_eliminated']),
                'itemized_resources_already_in_enterprise_outlay':True,'baseline_cost_credit_cents':0,
                'unclassified_boundary_cash_cents':0},
            'contract':{'active_service_businesses':1,'role_cash':'Fixed allocations by logical role are summed when roles share one legal account; no capital appears on consolidation',
                'physical_integration':'Integrator prepays commission plus first-month support; operator pays the integration/validation price and support passthrough atomically',
                'staff_and_site_costs':'Operator pays the unchanged actual staff, overhead, materials and site software; customer receives actual end-market receipts',
                'service_payment':'Explicit cents per total accepted zone, invoiced only after delivery; internal customer/operator payments are eliminated',
                'initial_model_work':'Catalog adaptation, demonstration, validation and allocated development are charged per actual unit at its first successful architecture admission, including opening hardware; no second hardware purchase for opening assets',
                'recurring_model_work':'Catalog inference multiplier, maintenance and network costs per supported unit-month; opaque robot digital bundle replaced',
                'resource_hours':'Separate declared engineering and demonstration pools, alongside the existing physical integration and support pools; no empirical capacity is inferred',
                'reference_only_common_fields':['service_price_fraction','receiver_surplus_usd_year','payer_surplus_usd_year']},
            'limits':['All prices, funding, costs, resource pools and qualification gates are synthetic assumptions',
                'No avoided-baseline cash credit, intrinsic architecture productivity multiplier or payroll-removal claim',
                'Per-unit allocated model-development cash is an explicit scenario convention, not measured lab cash or optimal shared adaptation',
                'One active customer business; broader competition, acquisition, portfolio learning and strongest conventional coordination remain open',
                'No autonomous service-price negotiation, optimal capital allocation or asset recovery; standard cases use no debt',
                'Real rights, compatible configuration, sustained quality and whole-system costs remain unknown']}


def architecture_execution_hashes():
    paths=['model/monthly_architectures.py','model/architectures.py','model/architecture_assumptions.json']
    return {**bridge_source_hashes(),**{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in paths}}


def run_architecture_execution(plan,treasury,contracts,enterprise,finance,bridge,architecture):
    policy=_ArchitectureEnterprise(plan,contracts,treasury,enterprise,finance,bridge,architecture)
    return architecture_result(run_monthly(plan,treasury,commercial=policy),policy)


def architecture_result(r,policy):
    """Describe the one completed physical/Treasury run for this role policy."""
    r.update(schema_version='monthly-deployment/0.6',scope='synthetic_funded_monthly_intelligence_roles',
        ownership='one_title_owner_per_unit_from_the_explicit_operator_hardware_contract')
    r['commercial']=policy.result(r);r['enterprise']=policy.enterprise_result(r);r['finance']=policy.finance_result(r)
    r['calendar_bridge']=policy.bridge_result(r);r['architecture_execution']=policy.architecture_result(r)
    r['calendar_bridge']['cost_and_resource_contract']['additional_digital']='Site software and changed-version qualification retain the calendar bills; itemized architecture inference, maintenance and network resources replace the opaque robot digital bundle'
    r['calendar_bridge']['cost_and_resource_contract']['integration']='Integrator pays the physical commission/support booking, funded atomically by the operator integration/validation price and support passthrough'
    r['calendar_bridge']['cash']['scope']='Site software and changed-version qualification only; additional architecture resources are separately traced and already included in enterprise outlay'
    for row in r['calendar_bridge']['metric_lineage']:
        if row['metric']=='digital and upgrade cash':row.update(metric='site software and changed-version qualification cash',inputs='Calendar site and upgrade invoices only; see architecture_execution for itemized robot intelligence costs')
    for row in r['finance']['metric_lineage']:
        if row['metric']=='accepted delivered service':row['basis']='Explicit synthetic accepted cleaning-zone contract; no clinical/component conversion'
    for key in ('commercial','enterprise','calendar_bridge'):
        r[key]['limits']=['Scope is defined by architecture_execution.limits and finance.limits']
    r['finance']['limits']=[x for x in r['finance']['limits'] if not x.startswith('Annual work-unit')]
    r['source_sha256']=architecture_execution_hashes();r=canonical_wire(r)
    r['rational_wire_format']='decimal_string_numerator_and_denominator_for_lossless_JSON'
    r['case_hash']=hashlib.sha256(json.dumps(r,sort_keys=True,separators=(',',':')).encode()).hexdigest()
    return json.loads(json.dumps(r))


def architecture_case_inputs(architecture_inputs=None,bridge_inputs=None):
    if architecture_inputs is not None and not isinstance(architecture_inputs,dict):raise ValueError('Architecture inputs must be an object')
    config=ArchitectureExecution(**(architecture_inputs or {}));settings,a,roles=resolved(config)
    if bridge_inputs is not None and not isinstance(bridge_inputs,dict):raise ValueError('Bridge inputs must be an object')
    b=dict(bridge_inputs or {})
    if 'annual_overrides' in b:raise ValueError('Use architecture annual_reference_overrides before profile physical adjustments')
    base=parameters({'years':3,'capability_progress':0,**(config.annual_reference_overrides or {})})
    effective={**base,'integration_hours':base['integration_hours']*a['integration_multiplier'],
               'intervention_minutes':base['intervention_minutes']+a['support_minutes_delta']}
    b['annual_overrides']=parameters(effective)
    p,t,cs,e,f,bridge=bridge_case_inputs({'entrant_cash_cents':10_000_000,'loan_cents':0},b)
    n=p.months
    operators=tuple(replace(o,opening_installed=config.opening_robots if o.operator_id=='incumbent' else 0,
                    requested_additions=config.new_robots if o.operator_id=='incumbent' else 0) for o in p.operators)
    p=replace(p,plan_id='monthly-intelligence',operators=operators,provider_actor=roles['oem'],
        starts=(Start('architecture-new-units',0,config.new_robots,config.new_robots),) if config.new_robots else ())
    cs=tuple(replace(c,customer_actor=roles['customer'] if c.operator_id=='incumbent' else IDLE_ACTOR,
                     arrangement='sale',lessor_actor=None) for c in cs)
    businesses=tuple(replace(x,actor_id=roles['customer'] if x.operator_id=='incumbent' else IDLE_ACTOR,
                      active_from_month=0 if x.operator_id=='incumbent' else None,formation_cents=0,
                      procurement_month=0,acquisition_cents_per_recurring_unit=0) for x in e.businesses)
    e=replace(e,businesses=businesses,moves=(),equity=(),market=replace(e.market,unmet_units=0,new_units=0))
    funds=defaultdict(int)
    for role,amount in {**ROLE_CASH,**(config.role_opening_cash_cents or {})}.items():funds[roles[role]]+=amount
    accounts=[Account(actor,amount) for actor,amount in sorted(funds.items())]
    required={IDLE_ACTOR:0,p.manufacturing_vendor_actor:0,p.deployment_vendor_actor:0,e.enterprise_vendor_actor:0,
              e.market.buyer_actor:1_000_000_000,bridge.digital_vendor_actor:0,RESOURCE_ACTOR:0,'capital_lender':0,'investor':0}
    accounts.extend(Account(actor,amount) for actor,amount in required.items())
    t=Treasury(tuple(accounts))
    return p,t,cs,e,FinancePlan(),bridge,config


def run_architecture_case(architecture_inputs=None,bridge_inputs=None):
    return run_architecture_execution(*architecture_case_inputs(architecture_inputs,bridge_inputs))


def replay_architecture_execution(saved):
    if not isinstance(saved,dict) or saved.get('schema_version')!='monthly-deployment/0.6':raise ValueError('Saved monthly architecture case required')
    e=dict(saved['enterprise']['inputs']);e['market']=Market(**e['market'])
    for key,cls in [('businesses',Business),('moves',CustomerMove),('equity',Equity)]:e[key]=tuple(cls(**x) for x in e[key])
    f=dict(saved['finance']['inputs']);f['loans']=tuple(TermLoan(**x) for x in f['loans'])
    return run_architecture_execution(*restore_opening_inputs(saved),EnterprisePlan(**e),FinancePlan(**f),Bridge(**saved['calendar_bridge']['inputs']),ArchitectureExecution(**saved['architecture_execution']['inputs']))


def architecture_execution_options():
    return {**{name:{'architecture_inputs':{'architecture_id':name}} for name in architecture_catalog()['labels']},
        'licensed_high_fee':{'architecture_inputs':{'architecture_overrides':{'common':{'model_fee_usd_year':12000}}}},
        'licensed_no_model_cash':{'architecture_inputs':{'role_opening_cash_cents':{'model_supplier':0}}},
        'open_engineering_scarcity':{'architecture_inputs':{'architecture_id':'open_adapted','engineering_hours_per_month':200}},
        'open_initial_engineering_available':{'architecture_inputs':{'architecture_id':'open_adapted','engineering_hours_per_month':600}},
        'model_operator_capital_reallocated':{'architecture_inputs':{'architecture_id':'model_led_operator','role_opening_cash_cents':{'customer':10_000_000,'operator':20_000_000}}},
        'rights_not_assumed':{'architecture_inputs':{'architecture_overrides':{'profiles':{'licensed_independent':{'assume_rights_available':False}}}}}}


def architecture_execution_artifact():
    inputs={k:{'architecture_inputs':asdict(ArchitectureExecution(**x.get('architecture_inputs',{}))),'bridge_inputs':x.get('bridge_inputs',{})} for k,x in architecture_execution_options().items()}
    cases={name:run_architecture_case(**x) for name,x in inputs.items()};summary=[]
    for name,r in cases.items():
        a=r['architecture_execution'];months=r['enterprise']['months']
        summary.append({'case':name,'architecture_id':a['inputs']['architecture_id'],'status':a['status'],
            'accepted_zones':_rational(sum((rational(m['total_delivered_units']) for m in months),Fraction())),
            'robot_zones':_rational(sum((rational(x['robot_delivered_units']) for m in months for x in m['operators']),Fraction())),
            'staff_cash_paid_cents':sum(x['current_period_staff_cash_paid_cents'] for m in r['calendar_bridge']['months'] for x in m['human_work']),
            'supported_robot_months':sum(m['support']['used'] for m in r['months']),
            'qualified_units':len(a['months'][-1]['qualified_unit_ids']),**a['consolidation']})
    out={'schema_version':'monthly-intelligence-witnesses/0.1','evidence_status':'synthetic_unqualified_architecture_contracts',
        'case_inputs':inputs,'cases':cases,'summary':summary,'source_sha256':architecture_execution_hashes(),
        'comparison_boundary':'One active cleaning-service business, fixed paid staffing and common demand. Logical role cash is held constant before entity consolidation. Profile resource assumptions and funded contracts differ explicitly; no calibrated or optimized architecture ranking.'}
    out=canonical_wire(out);out['artifact_hash']=hashlib.sha256(json.dumps(out,sort_keys=True,separators=(',',':')).encode()).hexdigest()
    return out
