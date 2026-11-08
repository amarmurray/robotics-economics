"""One paid site crew, two due services and an explicit staffing-notice policy.

All work rates, employment-like capacity blocks and contract terms are synthetic.
Minutes are conserved; unlike service units are never added to one output total.
"""
from dataclasses import asdict, dataclass, replace
from fractions import Fraction
from pathlib import Path
import hashlib
import json
import math

from model.architecture_resources import (_ResourceArchitecture, architecture_resources_result,
    resource_architecture_inputs, source_hashes as resource_hashes)
from model.annual_resource_ledger import read_resources
from model.calendar_bridge import ROOT, Bridge, exact, rational
from model.component_inventory import ComponentInventory, read_components
from model.enterprise_finance import FinancePlan, TermLoan
from model.monthly_architectures import ArchitectureExecution, canonical_wire
from model.monthly_commercial import restore_opening_inputs
from model.monthly_deployment import Moment, _integer, _name, _rational, run_monthly
from model.monthly_enterprise import Business, CustomerMove, EnterprisePlan, Equity, Market, POOLS, round_cents
from model.treasury import Account

OUTSIDE_BUYER = 'site-inventory-work-buyer'


@dataclass(frozen=True)
class Workforce:
    resource_id: str = 'site-service-crew'
    opening_blocks: int = 2
    minutes_per_block: int = 4800
    target_blocks: int | None = 1
    notice_earliest_month: int = 1
    notice_delay_months: int = 2
    notice_supported_units: int = 2
    overtime_minutes_per_month: int = 2400
    overtime_cents_per_minute: int = 100
    robot_handling_minutes_per_zone: int = 2
    attention_minutes_per_supported_unit: int = 60
    outside_jobs_by_month: tuple[int, ...] = (20,) * 8
    outside_minutes_per_job: int = 120
    outside_cents_per_job: int = 6000
    outside_collection_lag_months: int = 1
    outside_buyer_opening_cash_cents: int = 5_000_000

    def __post_init__(self):
        _name(self.resource_id)
        for key in ('opening_blocks','minutes_per_block','notice_earliest_month','notice_delay_months',
                    'notice_supported_units','overtime_minutes_per_month','overtime_cents_per_minute',
                    'robot_handling_minutes_per_zone','attention_minutes_per_supported_unit',
                    'outside_minutes_per_job','outside_cents_per_job','outside_collection_lag_months',
                    'outside_buyer_opening_cash_cents'):
            _integer(getattr(self,key))
        if not 1 <= self.opening_blocks <= 10 or not 1 <= self.minutes_per_block <= 10000:
            raise ValueError('Bounded positive staffing blocks required')
        if self.target_blocks is not None:
            _integer(self.target_blocks)
            if self.target_blocks > self.opening_blocks:raise ValueError('Notice may only reduce declared blocks')
        if not 1 <= self.notice_delay_months <= 36 or self.notice_earliest_month > 36:
            raise ValueError('Notice requires a positive bounded delay')
        if self.notice_supported_units > 8 or self.overtime_minutes_per_month > 100000:
            raise ValueError('Supported fleet or overtime outside declared bounds')
        if not 1 <= self.outside_collection_lag_months <= 36:
            raise ValueError('External receipts require a positive collection lag')
        if not 1 <= self.overtime_cents_per_minute <= 10000 or not 1 <= self.outside_minutes_per_job <= 10000:
            raise ValueError('Paid overtime and positive job work required')
        if self.robot_handling_minutes_per_zone > 1000 or self.attention_minutes_per_supported_unit > 100000:
            raise ValueError('Handling/attention outside bounded experiment')
        if self.outside_cents_per_job > 1_000_000 or self.outside_buyer_opening_cash_cents > 1_000_000_000:
            raise ValueError('Outside cash/rate outside bounded experiment')
        if not isinstance(self.outside_jobs_by_month,(tuple,list)) or not self.outside_jobs_by_month:
            raise ValueError('Explicit outside job series required')
        for x in self.outside_jobs_by_month:
            _integer(x)
            if x > 200:raise ValueError('At most 200 identified outside jobs per month')
        object.__setattr__(self,'outside_jobs_by_month',tuple(self.outside_jobs_by_month))


class _WorkforceArchitecture(_ResourceArchitecture):
    def __init__(self,plan,contracts,treasury,enterprise,finance,bridge,architecture,resources,workforce):
        super().__init__(plan,contracts,treasury,enterprise,finance,bridge,architecture,resources)
        if not isinstance(workforce,Workforce) or len(workforce.outside_jobs_by_month)!=plan.months:
            raise ValueError('One workforce contract and outside demand per month required')
        if OUTSIDE_BUYER in self.parties or treasury.account(OUTSIDE_BUYER).opening_cash_cents!=workforce.outside_buyer_opening_cash_cents:
            raise ValueError('Separate funded outside buyer must match the declared opening cash')
        self.workforce=workforce;self.work_months=[];self.work_events=[];self.work_sales=set();self.overtime_ids=set()
        self.notice_month=None;self.effective_month=None;self.current_work=None
        self.block_cost=round_cents(Fraction(workforce.minutes_per_block,60)*exact(self.cell['wage_usd_hour'])*100)
        if self.block_cost<=0:raise ValueError('A staffing block must have positive cost')
        b=self.business['incumbent']
        if any(x!=workforce.opening_blocks*self.block_cost for x in b.human_staff_cents_by_month):
            raise ValueError('Opening paid blocks must match the original staffing commitment')

    def prepare(self,t,month,units):
        w=self.workforce
        if w.target_blocks is not None and self.notice_month is None and month>=w.notice_earliest_month and self.work_months:
            previous=self.work_months[-1]
            qualifies=previous['complete_combined_obligation'] and previous['supported_units']>=w.notice_supported_units
            if qualifies:
                self.notice_month=month;self.effective_month=month+w.notice_delay_months
            self.work_events.append(dict(month=month,phase=1,action='staffing_notice',issued=qualifies,
                based_only_on_completed_month=month-1,effective_month=self.effective_month,
                reason='' if qualifies else 'prior_complete_service_and_supported_fleet_required'))
        self.blocks=w.target_blocks if self.effective_month is not None and month>=self.effective_month else w.opening_blocks
        # Only this period's declared obligation changes. Opening inputs remain
        # intact for replay; no future observations enter the notice decision.
        original=self.enterprise
        businesses=[]
        for b in original.businesses:
            if b.operator_id=='incumbent':
                costs=list(b.human_staff_cents_by_month);costs[month]=self.blocks*self.block_cost
                b=replace(b,human_staff_cents_by_month=tuple(costs),
                    human_capacity_by_month=tuple(0 if i==month and not costs[i] else v for i,v in enumerate(b.human_capacity_by_month)))
            businesses.append(b)
        self.enterprise=replace(original,businesses=tuple(businesses))
        try:t=super().prepare(t,month,units)
        finally:self.enterprise=original
        self.current_work=None;self.overtime_minutes=0;self.overtime_reason='';self.overtime_id=None
        return t

    def _capacity_and_work(self,month):
        w=self.workforce
        cohorts=[x for x in self.supported.values() if x['operator_id']=='incumbent']
        robot_capacity=sum((rational(x['capacity_units']) for x in cohorts),Fraction())
        demand=sum(self.assignment[p].get('incumbent',0) for p in POOLS)
        efficiency=exact(self.calendar[month]['effective_parameters']['digital_efficiency']) if self.bridge.digital_enabled else Fraction()
        human_minutes=exact(self.cell['human_hours_per_unit'])*60*(1-efficiency)
        robot_units=min(Fraction(demand),robot_capacity) if w.robot_handling_minutes_per_zone<=human_minutes else Fraction()
        attention=len(cohorts)*w.attention_minutes_per_supported_unit
        needed=attention+w.outside_jobs_by_month[month]*w.outside_minutes_per_job+robot_units*w.robot_handling_minutes_per_zone+(demand-robot_units)*human_minutes
        return cohorts,robot_capacity,demand,human_minutes,attention,needed

    def finish_shipping(self,t,month):
        t=super().finish_shipping(t,month)
        w=self.workforce;b=self.business['incumbent'];ready=self.ready(t,b,month,5)
        *_,needed=self._capacity_and_work(month)
        regular=self.blocks*w.minutes_per_block if ready else 0
        requested=min(w.overtime_minutes_per_month,math.ceil(max(Fraction(),needed-regular))) if ready else 0
        if requested:
            iid=self._id('workforce',month,'overtime');self.overtime_id=iid
            t=self.issue_enterprise(t,iid,self.operator,self.enterprise.enterprise_vendor_actor,requested*w.overtime_cents_per_minute,
                Moment(month,5),Moment(month,6),'site_crew_overtime',True)
            self.enterprise_cost_ids.add(iid);self.overtime_ids.add(iid)
            # Invoice after shipping, then prepay at the opening of service phase.
            # No accepted work or phase-6 sale has happened yet.
            candidate=t.settle_invoice(iid+':pay',iid,Moment(month,6),provenance=self.provenance)
            if candidate.invoice(iid).outstanding_cents:
                t=candidate.cancel_invoice(iid+':cancel',iid,Moment(month,6),provenance=self.provenance)
                self.overtime_reason='unfunded_optional_overtime'
            else:t=candidate;self.overtime_minutes=requested
        self.current_treasury=t
        self.current_work=self._allocate(month,regular+self.overtime_minutes,ready)
        self.current_work.update(overtime_requested_minutes=requested,overtime_paid_minutes=self.overtime_minutes,
            overtime_invoice_id=self.overtime_id,overtime_block_reason=self.overtime_reason,
            regular_available_minutes=regular,scheduled_blocks=self.blocks,notice_issued_month=self.notice_month,
            notice_effective_month=self.effective_month)
        return t

    def _allocate(self,month,budget,ready):
        w=self.workforce;cohorts,capacity,demand,human_minutes,attention,needed=self._capacity_and_work(month)
        remaining=Fraction(budget);bookings=[]
        def use(task,kind,minutes,units,unit):
            nonlocal remaining
            assert 0<=minutes<=remaining
            remaining-=minutes
            bookings.append(dict(task_id=task,worker_resource_id=w.resource_id,kind=kind,
                minutes=_rational(minutes),accepted_quantity=_rational(units),service_unit=unit))
        done_attention=min(remaining,Fraction(attention)) if ready else Fraction()
        use(f'attention-{month}','local_robot_attention',done_attention,Fraction(), 'no service quantity')
        usable_capacity=capacity if done_attention==attention and ready else Fraction()
        jobs=w.outside_jobs_by_month[month];completed=min(jobs,int(remaining//w.outside_minutes_per_job)) if ready else 0
        for i in range(completed):use(f'inventory-{month}-{i}','outside_inventory_job',Fraction(w.outside_minutes_per_job),Fraction(1),'inventory jobs')
        robot=human=human_capacity=Fraction()
        if ready:
            if w.robot_handling_minutes_per_zone<=human_minutes:
                robot=min(Fraction(demand),usable_capacity,remaining/w.robot_handling_minutes_per_zone if w.robot_handling_minutes_per_zone else Fraction(demand))
                use(f'robot-zone-{month}','robot_zone_handling',robot*w.robot_handling_minutes_per_zone,robot,'cleaning zones')
            human_capacity=remaining/human_minutes
            human=min(Fraction(demand)-robot,human_capacity)
            use(f'human-zone-{month}','human_cleaning',human*human_minutes,human,'cleaning zones')
        used=Fraction(budget)-remaining
        assert used==sum((rational(x['minutes']) for x in bookings),Fraction())
        assert len({x['task_id'] for x in bookings})==len(bookings)
        return dict(month=month,resource_id=w.resource_id,operational=ready,supported_units=len(cohorts),
            supported_unit_ids=[x['unit_id'] for x in cohorts],worker_budget_minutes=budget,booked_minutes=_rational(used),unused_minutes=_rational(remaining),
            full_obligation_minimum_minutes=_rational(needed),human_minutes_per_zone=_rational(human_minutes),
            robot_capacity_zones=_rational(capacity),required_attention_minutes=attention,performed_attention_minutes=_rational(done_attention),
            human_capacity_after_robot_and_outside_work=_rational(human_capacity),
            cleaning_required_zones=demand,robot_cleaning_zones=_rational(robot),human_cleaning_zones=_rational(human),
            accepted_cleaning_zones=_rational(robot+human),unserved_cleaning_zones=_rational(Fraction(demand)-robot-human),
            outside_required_jobs=jobs,outside_completed_jobs=completed,outside_unserved_jobs=jobs-completed,
            outside_unserved_ids=[f'inventory-{month}-{i}' for i in range(completed,jobs)],bookings=bookings,
            complete_combined_obligation=robot+human==demand and completed==jobs and done_attention==attention)

    def dispatch_output(self,month,operator,robot_capacity):
        if operator.operator_id!='incumbent':return super().dispatch_output(month,operator,robot_capacity)
        row=self.current_work;assert row is not None
        cohorts=[x for x in self.supported.values() if x['operator_id']=='incumbent']
        raw=sum((rational(x['ramp_fraction'])*self.plan.system.full_output_units_per_robot_month for x in cohorts),Fraction())
        assert raw==robot_capacity and rational(row['robot_capacity_zones'])<=raw
        demand=row['cleaning_required_zones'];robot=rational(row['robot_cleaning_zones']);human=rational(row['human_cleaning_zones']);total=robot+human
        allocated={p:self.assignment[p].get('incumbent',0) for p in POOLS};served={p:total*allocated[p]/demand if demand else Fraction() for p in POOLS}
        self.period_service['incumbent']=dict(operator_id='incumbent',actor_id=self.customer,operational=row['operational'],
            assigned_units=allocated,robot_capacity_units=row['robot_capacity_zones'],human_capacity_units=row['human_capacity_after_robot_and_outside_work'],
            robot_delivered_units=_rational(robot),human_delivered_units=_rational(human),total_delivered_units=_rational(total),
            served_by_pool={p:_rational(v) for p,v in served.items()},unserved_by_pool={p:_rational(Fraction(allocated[p])-served[p]) for p in POOLS})
        return demand,robot,dict(human_accepted_output_units=_rational(human),total_accepted_output_units=_rational(total),
            effective_calendar_capacity_units=row['robot_capacity_zones'],supported_unit_ids=row['supported_unit_ids'])

    def bill_service(self,t,month,units,supported):
        t=super().bill_service(t,month,units,supported)
        amount=self.current_work['outside_completed_jobs']*self.workforce.outside_cents_per_job
        iid=None
        if amount:
            iid=self._id('workforce',month,'outside-sale')
            t=self.issue_enterprise(t,iid,OUTSIDE_BUYER,self.operator,amount,Moment(month,6),
                Moment(month+self.workforce.outside_collection_lag_months,2),'outside_inventory_service')
            self.sales_ids.add(iid);self.work_sales.add(iid)
        self.current_work.update(outside_service_invoice_id=iid,outside_service_face_cents=amount)
        return t

    def close(self,t,month,units,supported):
        super().close(t,month,units,supported)
        iid=self._id('enterprise','incumbent',month,'human_staff')
        invoice=next((x for x in t.invoices if x.invoice_id==iid),None)
        self.current_work.update(staff_commitment_cents=invoice.face_cents if invoice else 0,
            staff_cash_paid_cents=invoice.paid_cents if invoice else 0,staff_unpaid_cents=invoice.outstanding_cents if invoice else 0,
            overtime_cash_paid_cents=t.invoice(self.overtime_id).paid_cents if self.overtime_id else 0)
        self.work_months.append(self.current_work)
        for row in self.bridge_months[-1]['human_work']:
            if row['operator_id']=='incumbent':
                row['retained_site_crew_hours']=_rational(rational(self.current_work['booked_minutes'])/60)
                row['payroll_missing_reason']='Empirical payroll removal is unknown; shared_workforce records declared paid blocks, notice and actual synthetic cash.'

    def workforce_result(self,r):
        invoices={i['invoice_id']:i for i in r['closing_treasury']['invoices']}
        sales=[invoices[i] for i in sorted(self.work_sales)]
        return dict(schema_version='shared-site-workforce/0.1',inputs=asdict(self.workforce),months=self.work_months,events=self.work_events,
            staff_block_cost_cents=self.block_cost,notice_issued_month=self.notice_month,notice_effective_month=self.effective_month,
            cash=dict(staff_commitments_cents=sum(m['staff_commitment_cents'] for m in self.work_months),
                staff_paid_cents=sum(m['staff_cash_paid_cents'] for m in self.work_months),
                overtime_paid_cents=sum(m['overtime_cash_paid_cents'] for m in self.work_months),
                outside_service_invoiced_cents=sum(i['face_cents'] for i in sales),outside_service_received_cents=sum(i['paid_cents'] for i in sales),
                outside_service_unpaid_cents=sum(i['outstanding_cents'] for i in sales),
                outside_service_due_unpaid_cents=sum(i['outstanding_cents'] for i in sales if (i['due_at']['month'],i['due_at']['phase'])<=(self.plan.months-1,7)),
                included_in_enterprise_outlay_and_sales=True,add_again_to_consolidation=False),
            metric_lineage=[
                dict(metric='regular paid capacity',equation='effective paid blocks * minutes per block; available only when mandatory operating obligations are current',inputs='workforce inputs, notice events and staff invoice',implementation='_WorkforceArchitecture.prepare/finish_shipping'),
                dict(metric='overtime',equation='min(ceiling(required minutes - regular minutes), overtime ceiling); booked only after full prepayment',inputs='actual supported unit capacities, complete due work, human digital path and operator available cash',implementation='_WorkforceArchitecture.finish_shipping'),
                dict(metric='one shared worker',equation='robot attention + outside jobs + robot handling + human cleaning + unused minutes = available regular + paid overtime minutes',inputs='one resource ID and unique per-month task bookings',implementation='_WorkforceArchitecture._allocate'),
                dict(metric='staffing notice',equation='earliest eligible month after prior complete combined service and required supported fleet; effective only after notice delay',inputs='prior completed month only, target paid blocks, notice delay',implementation='_WorkforceArchitecture.prepare'),
                dict(metric='distinct complete services',equation='cleaning delivered = robot + human; outside jobs delivered separately; all due work required for complete flag',inputs='one market assignment and named outside job IDs',implementation='_WorkforceArchitecture.dispatch_output/close'),
                dict(metric='outside receipts',equation='completed jobs * declared price; collected from separately funded buyer on due date',inputs='outside buyer Treasury, invoice and receipt lag',implementation='_WorkforceArchitecture.bill_service; inherited collect')],
            limits=['Synthetic paid capacity blocks are not measured employees, shifts or legally verified employment terms.',
                'Monthly end deadlines and divisible cleaning zones remain abstractions; no within-shift travel, congestion or clinical workflow is simulated.',
                'Local robot attention and handling belong to this crew. Engineering, demonstration, professional repair/support and integration stay distinct paid resources.',
                'Outside inventory jobs are a declared second workload with a separate buyer; their units are never added to cleaning zones.',
                'Work order is robot attention, outside jobs, then cleaning with the lower marginal crew-minute alternative; it is not global optimal scheduling.',
                'Notice is binding after commitment; later shortfalls use funded overtime or remain visible. No retroactive staffing reduction or future-work backfill.',
                'Additional overtime is prepaid after physical support, commissioning and starts; this policy does not reserve its cash in advance. Transition/severance costs beyond the notice-period commitment are not modeled.',
                'No empirical payroll saving, real labor rule, target ROI, support entitlement or transferable hospital coefficient is inferred.'])


def source_hashes():
    return {**resource_hashes(),'model/shared_workforce.py':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}


@dataclass(frozen=True)
class FallbackReserve:
    purchase_floor_cents: int = 0
    active_from_month: int = 0

    def __post_init__(self):
        _integer(self.purchase_floor_cents);_integer(self.active_from_month)
        if self.purchase_floor_cents>1_000_000_000 or self.active_from_month>36:
            raise ValueError('Bounded purchase floor and activation month required')


class _FallbackWorkforceArchitecture(_WorkforceArchitecture):
    """A prospective purchase gate, not escrow or another staffing contract."""
    def __init__(self,*args,fallback):
        super().__init__(*args)
        if not isinstance(fallback,FallbackReserve):raise ValueError('Explicit fallback reserve policy required')
        self.fallback=fallback;self.purchase_decisions=[];self.fallback_months=[]

    def admit(self,t,iid,month,phase,physical_reason,unit=None,operator_id=None):
        if t.invoice(iid).category!='ship' or operator_id!='incumbent':
            return super().admit(t,iid,month,phase,physical_reason,unit,operator_id)
        quote=self.quotes[(month,unit.unit_id,operator_id)]
        group=[quote,iid]
        spend=sum(t.invoice(i).outstanding_cents for i in group if t.invoice(i).payer==self.operator)
        available=t.available(self.operator);after=available-spend
        active=month>=self.fallback.active_from_month
        floor=self.fallback.purchase_floor_cents if active else 0
        reason=physical_reason
        if floor and after<floor:reason=reason or 'operator_fallback_purchase_floor'
        result,reason=super().admit(t,iid,month,phase,reason,unit,operator_id)
        self.purchase_decisions.append(dict(month=month,phase=phase,unit_id=unit.unit_id,
            operator_actor=self.operator,purchase_invoice_id=quote,group_invoice_ids=group,
            policy_active=active,required_floor_cents=floor,
            operator_available_before_cents=available,candidate_operator_spend_cents=spend,
            operator_available_if_purchased_cents=after,operator_available_after_cents=result.available(self.operator),
            status='blocked' if reason else 'admitted',reason=reason or None,
            group_cash_paid_cents=sum(result.invoice(i).paid_cents for i in group),
            future_actual_work_or_receipts_consulted=False))
        return result,reason

    def finish_shipping(self,t,month):
        before=t.available(self.operator)
        t=super().finish_shipping(t,month)
        self.fallback_months.append(dict(month=month,operator_actor=self.operator,
            available_before_overtime_cents=before,available_after_overtime_cents=t.available(self.operator),
            overtime_requested_minutes=self.current_work['overtime_requested_minutes'],
            overtime_paid_minutes=self.overtime_minutes,overtime_reason=self.overtime_reason or None,
            complete_combined_obligation=self.current_work['complete_combined_obligation']))
        return t

    def fallback_result(self,r):
        actors=sorted(set(self.roles.values()))
        return dict(schema_version='fallback-purchase-reserve/0.1',inputs=asdict(self.fallback),
            operator_actor=self.operator,purchase_decisions=self.purchase_decisions,months=self.fallback_months,
            outcomes=dict(manufactured_units=sum(m['flows']['started'] for m in r['months']),
                purchased_units=sum(m['flows']['shipped'] for m in r['months']),
                commissioned_units=sum(m['flows']['commissioned'] for m in r['months']),
                supported_unit_months=sum(m['support']['used'] for m in r['months']),
                closing_oem_finished_units=r['months'][-1]['closing_stock']['finished'],
                purchase_floor_refusals=sum(x['reason']=='operator_fallback_purchase_floor' for x in self.purchase_decisions),
                actor_closing_cash_cents={actor:r['months'][-1]['closing_cash_cents'][actor] for actor in actors}),
            mechanism='Fixed operator liquidity floor gates optional hardware purchases; retained funds remain spendable on existing obligations and overtime.',
            information_clock='Declared opening policy; actual current available cash and current purchase group only. No future work, capacity, receipts or realized outcomes are consulted.',
            capacity_contract='Existing shared crew overtime: assumed qualified, available within the current month up to its declared ceiling, fully prepaid before service. This gate buys no capacity guarantee or hiring/response entitlement.',
            reserve_is_escrow=False,reserve_is_expense=False,add_again_to_consolidation=False,
            limits=['The floor applies only to operator hardware purchases, not unrelated OEM manufacture or other actors cash.',
                'Earlier manufacture, staffing notice and mandatory liabilities remain. Refused shipment retains OEM stock and sunk cash.',
                'Support, commissioning and other existing payments can consume retained liquidity; a floor cannot guarantee later staffing or service.',
                'Late activation cannot reverse earlier purchases, obligations or missed work. This is a declared policy experiment, not an optimized reserve or empirical staffing contract.'])


def run_shared_workforce(plan,treasury,contracts,enterprise,finance,bridge,architecture,resources,components,workforce,fallback=None):
    args=(plan,contracts,treasury,enterprise,finance,bridge,architecture,resources,workforce)
    policy=_WorkforceArchitecture(*args) if fallback is None else _FallbackWorkforceArchitecture(*args,fallback=fallback)
    if components.onboard_configuration!=policy.annual['onboard_configuration']:raise ValueError('Compatible architecture parts required')
    materials=ComponentInventory(components)
    r=architecture_resources_result(run_monthly(plan,treasury,commercial=policy,materials=materials),policy,materials)
    r.update(schema_version='shared-workforce-window/0.1',scope='synthetic_shared_site_crew_complete_cleaning_and_inventory_work')
    r['shared_workforce']=policy.workforce_result(r)
    if fallback is not None:r['fallback_reserve']=policy.fallback_result(r)
    r['architecture_resource_contract']['baseline']='One complete cleaning obligation plus separately counted inventory jobs, with one explicit paid site crew, notice and funded overtime policy.'
    r['architecture_resource_contract']['resource_relationship']+=' A fifth identified site crew is shared only by cleaning, local robot attention/handling and inventory jobs; it is not interchangeable with those four pools.'
    r['architecture_execution']['contract']['staff_and_site_costs']='Operator pays actual regular blocks, funded overtime, site software and materials. Staffing notice uses prior completed service; unlike outside jobs have separate demand and receipts.'
    r['enterprise']['scope']='synthetic_cleaning_market_with_separate_inventory_service_and_one_site_crew'
    r.pop('case_hash');r['source_sha256']=source_hashes();r=canonical_wire(r)
    r['case_hash']=hashlib.sha256(json.dumps(r,sort_keys=True,separators=(',',':')).encode()).hexdigest()
    return json.loads(json.dumps(r))


def workforce_case_inputs(inputs=None):
    if inputs is None:inputs={}
    if not isinstance(inputs,dict) or set(inputs)-{'execution','workforce','fallback'}:raise ValueError('Expected execution, workforce and optional fallback inputs')
    if 'execution' in inputs and not isinstance(inputs['execution'],dict):raise ValueError('Execution must be an object')
    if 'workforce' in inputs and not isinstance(inputs['workforce'],dict):raise ValueError('Workforce must be an object')
    if 'fallback' in inputs and not isinstance(inputs['fallback'],dict):raise ValueError('Fallback policy must be an object')
    w=Workforce(**inputs.get('workforce',{}));args=list(resource_architecture_inputs(inputs.get('execution')))
    args[1]=replace(args[1],accounts=args[1].accounts+(Account(OUTSIDE_BUYER,w.outside_buyer_opening_cash_cents),))
    return (*args,w,FallbackReserve(**inputs['fallback']) if 'fallback' in inputs else None)


def run_workforce_case(inputs=None):return run_shared_workforce(*workforce_case_inputs(inputs))


def replay_workforce_case(saved):
    if not isinstance(saved,dict) or saved.get('schema_version')!='shared-workforce-window/0.1':raise ValueError('Complete shared workforce case required')
    try:
        e=dict(saved['enterprise']['inputs']);e['market']=Market(**e['market'])
        for key,cls in [('businesses',Business),('moves',CustomerMove),('equity',Equity)]:e[key]=tuple(cls(**x) for x in e[key])
        f=dict(saved['finance']['inputs']);f['loans']=tuple(TermLoan(**x) for x in f['loans'])
        return run_shared_workforce(*restore_opening_inputs(saved),EnterprisePlan(**e),FinancePlan(**f),
            Bridge(**saved['calendar_bridge']['inputs']),ArchitectureExecution(**saved['architecture_execution']['inputs']),
            read_resources(saved['annual_resources']['inputs']),read_components(saved['component_inventory']['inputs']),Workforce(**saved['shared_workforce']['inputs']),
            FallbackReserve(**saved['fallback_reserve']['inputs']) if 'fallback_reserve' in saved else None)
    except (KeyError,TypeError,AttributeError) as exc:raise ValueError('Incomplete shared workforce replay inputs') from exc


def workforce_worlds():
    human={'architecture':{'opening_robots':0,'new_robots':0}}
    surge=[20,20,20,20,40,40,40,40]
    tight={'architecture':{'role_opening_cash_cents':{'customer':0,'operator':8_000_000}}}
    thin={'architecture':{'architecture_id':'model_led_operator','role_opening_cash_cents':{'model_supplier':0}}}
    return {
        'fixed_crew_with_robots':{'workforce':{'target_blocks':None}},
        'notice_then_reduce':{},
        'longer_notice':{'workforce':{'notice_delay_months':4}},
        'outside_surge_with_overtime':{'workforce':{'outside_jobs_by_month':surge}},
        'outside_surge_without_overtime':{'workforce':{'outside_jobs_by_month':surge,'overtime_minutes_per_month':0}},
        'human_with_funded_overtime':{'execution':human,'workforce':{'target_blocks':None}},
        'stronger_human_dispatch':{'execution':{'architecture':{**human['architecture'],'annual_reference_overrides':{'digital_efficiency':0.25}}},'workforce':{'target_blocks':None}},
        'unfunded_outside_buyer':{'workforce':{'outside_buyer_opening_cash_cents':0}},
        'low_model_role_cash':{'execution':{'architecture':{'architecture_id':'model_led_operator','role_opening_cash_cents':{'model_supplier':0}}}},
        'tight_site_no_reserve':{'execution':tight,'workforce':{'outside_jobs_by_month':surge},'fallback':{}},
        'tight_site_purchase_reserve':{'execution':tight,'workforce':{'outside_jobs_by_month':surge},'fallback':{'purchase_floor_cents':2_000_000}},
        'tight_site_reserve_without_overtime':{'execution':tight,'workforce':{'outside_jobs_by_month':surge,'overtime_minutes_per_month':0},'fallback':{'purchase_floor_cents':2_000_000}},
        'model_operator_purchase_reserve':{'execution':thin,'fallback':{'purchase_floor_cents':4_000_000}},
        'model_operator_late_reserve':{'execution':thin,'fallback':{'purchase_floor_cents':4_000_000,'active_from_month':2}},
        'unfunded_model_supplier_reserve':{'execution':{'architecture':{'role_opening_cash_cents':{'model_supplier':0}}},'fallback':{'purchase_floor_cents':2_000_000}},
        'one_robot_no_reserve':{'execution':{'architecture':{'opening_robots':1}},'fallback':{}},
        'one_robot_excess_reserve':{'execution':{'architecture':{'opening_robots':1}},'fallback':{'purchase_floor_cents':100_000_000}},
        'stronger_human_dispatch_surge':{'execution':{'architecture':{**human['architecture'],'annual_reference_overrides':{'digital_efficiency':0.25}}},'workforce':{'target_blocks':None,'outside_jobs_by_month':surge}},
    }


def workforce_summary(name,r):
    w=r['shared_workforce'];rows=w['months'];c=w['cash']
    return dict(case=name,complete_months=sum(m['complete_combined_obligation'] for m in rows),months=len(rows),
        cleaning_zones=_rational(sum((rational(m['accepted_cleaning_zones']) for m in rows),Fraction())),
        outside_jobs=sum(m['outside_completed_jobs'] for m in rows),outside_due_jobs=sum(m['outside_required_jobs'] for m in rows),
        staff_paid_cents=c['staff_paid_cents'],overtime_paid_cents=c['overtime_paid_cents'],notice_effective_month=w['notice_effective_month'],
        staff_commitments_cents=c['staff_commitments_cents'],
        outside_received_cents=c['outside_service_received_cents'],outside_unpaid_cents=c['outside_service_unpaid_cents'],
        external_resource_cash_cents=r['enterprise']['consolidation']['external_physical_outlay_cents']+r['enterprise']['consolidation']['external_enterprise_outlay_cents'],
        case_hash=r['case_hash'])


def workforce_artifact():
    options=workforce_worlds();cases={k:run_workforce_case(v) for k,v in options.items()}
    result=dict(schema_version='shared-workforce-artifact/0.1',status='synthetic_workforce_contract_not_empirical_payroll',source_sha256=source_hashes(),
        comparison_boundary='Compare complete cleaning AND inventory service, actual paid commitments and every payer. Unlike service units are separate. The improved human path is a declared premise under the same site-software charge, not observed digital uplift. No ROI or employee-removal estimate.',
        case_inputs=options,cases=cases,summary=[workforce_summary(k,r) for k,r in cases.items()])
    result=canonical_wire(result)
    result['artifact_hash']=hashlib.sha256(json.dumps(result,sort_keys=True,separators=(',',':')).encode()).hexdigest()
    return result


def workforce_catalog():
    data=json.loads((ROOT/'model/results/shared_workforce.json').read_text())
    if data['source_sha256']!=source_hashes():raise ValueError('Shared workforce export is stale; regenerate')
    return {k:v for k,v in data.items() if k!='cases'} | {'cases':{'notice_then_reduce':data['cases']['notice_then_reduce']}}
