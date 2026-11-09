"""Paid qualified crews, retained work and actual customer renewal in one run.

Synthetic monthly policy: reserve local attention/outside duties and prepay
prospective overtime BEFORE awards. Neither future receipts nor a shareholder's
cash or spare crew is available to a separate operating company automatically.
"""
from dataclasses import asdict, replace
from fractions import Fraction
import hashlib
import json

from model.renewing_entry import (_RenewingEntry, renewing_entry_inputs,
    add_entry_renewal_sections, source_hashes as entry_hashes)
from model.shared_workforce import Workforce
from model.calendar_bridge import ROOT, Bridge, bridge_context, exact, rational
from model.competitive_renewals import Competition
from model.entry_transitions import Transition
from model.enterprise_finance import FinancePlan, TermLoan
from model.monthly_architectures import canonical_wire
from model.monthly_commercial import restore_opening_inputs
from model.monthly_deployment import _rational, run_monthly
from model.monthly_enterprise import Business, CustomerMove, EnterprisePlan, Equity, Market, POOLS, round_cents
from model.treasury import Account, Moment


def outside_buyer(op): return 'crew-outside-buyer-' + op


class _StaffedRenewals(_RenewingEntry):
    def crew_payer(self,operator_id):
        return self.business[operator_id].actor_id

    def resource_vendors(self):
        return {self.plan.manufacturing_vendor_actor,self.plan.deployment_vendor_actor,
            self.enterprise.enterprise_vendor_actor,self.bridge.digital_vendor_actor,'entry_resource_vendor'}

    def __init__(self, plan, contracts, treasury, enterprise, finance, bridge, competition, transition, crews):
        super().__init__(plan, contracts, treasury, enterprise, finance, bridge, competition, transition)
        if set(crews) != set(self.business) or len({w.resource_id for w in crews.values()}) != len(crews):
            raise ValueError('Each operator needs its own uniquely identified qualified crew')
        self.crews=crews; self.crew_months=[]; self.crew_events=[]; self.crew_current={}
        self.notices={op:None for op in crews}; self.effective={op:None for op in crews}
        self.blocks={}; self.block_cost={}; self.outside_sales=set()
        for op,w in crews.items():
            if not isinstance(w,Workforce) or len(w.outside_jobs_by_month)!=plan.months:
                raise ValueError('Explicit workforce and outside-duty calendar required')
            if outside_buyer(op) in self.parties or treasury.account(outside_buyer(op)).opening_cash_cents!=w.outside_buyer_opening_cash_cents:
                raise ValueError('Separately funded outside-duty buyer required')
            self.block_cost[op]=round_cents(Fraction(w.minutes_per_block,60)*exact(self.cell['wage_usd_hour'])*100)
            if any(x!=w.opening_blocks*self.block_cost[op] for x in self.business[op].human_staff_cents_by_month):
                raise ValueError('Opening paid staffing must match declared blocks')

    def prepare(self,t,month,units):
        original=self.enterprise; businesses=[]
        for op,w in self.crews.items():
            prior=next((x for x in reversed(self.crew_months) if x['operator_id']==op),None)
            if w.target_blocks is not None and self.notices[op] is None and month>=w.notice_earliest_month and prior:
                ok=prior['complete_obligation'] and prior['supported_units']>=w.notice_supported_units
                if ok:self.notices[op]=month;self.effective[op]=month+w.notice_delay_months
                self.crew_events.append(dict(month=month,phase=1,operator_id=op,action='staffing_notice',issued=ok,
                    based_only_on_completed_month=month-1,effective_month=self.effective[op]))
            self.blocks[op]=w.target_blocks if self.effective[op] is not None and month>=self.effective[op] else w.opening_blocks
        for b in original.businesses:
            costs=list(b.human_staff_cents_by_month);costs[month]=self.blocks[b.operator_id]*self.block_cost[b.operator_id]
            businesses.append(replace(b,human_staff_cents_by_month=tuple(costs),
                human_capacity_by_month=tuple(0 if i==month and not costs[i] else v for i,v in enumerate(b.human_capacity_by_month))))
        self.enterprise=replace(original,businesses=tuple(businesses))
        try:t=super().prepare(t,month,units)
        finally:self.enterprise=original
        self.crew_current={};self.overtime_quotes={}
        for op,w in self.crews.items():
            if w.overtime_minutes_per_month:
                iid=self._id('crew',op,month,'prospective-overtime')
                t=self.issue_enterprise(t,iid,self.crew_payer(op),self.enterprise.enterprise_vendor_actor,
                    w.overtime_minutes_per_month*w.overtime_cents_per_minute,Moment(month,1),Moment(month,5),'prospective_crew_overtime',True)
                self.enterprise_cost_ids.add(iid);self.overtime_quotes[op]=iid
        return t

    def work_parameters(self,op,month):
        w=self.crews[op]; cohorts=[x for x in self.supported.values() if x['operator_id']==op]
        capacity=sum((rational(x['capacity_units']) for x in cohorts),Fraction())
        efficiency=exact(self.calendar[month]['effective_parameters']['digital_efficiency']) if self.bridge.digital_enabled else Fraction()
        human_minutes=exact(self.cell['human_hours_per_unit'])*60*(1-efficiency)
        return cohorts,capacity,human_minutes,len(cohorts)*w.attention_minutes_per_supported_unit

    def allocate(self,op,month,budget,demand,ready):
        w=self.crews[op];cohorts,capacity,human_minutes,attention=self.work_parameters(op,month)
        remaining=Fraction(budget);bookings=[]
        def book(kind,minutes,quantity,unit,suffix=''):
            nonlocal remaining
            assert 0<=minutes<=remaining
            remaining-=minutes
            bookings.append(dict(task_id=f'{op}-{month}-{kind}{suffix}',worker_resource_id=w.resource_id,
                kind=kind,minutes=_rational(minutes),accepted_quantity=_rational(quantity),service_unit=unit))
        attended=min(remaining,Fraction(attention)) if ready else Fraction()
        book('local_robot_attention',attended,Fraction(),'no service quantity')
        usable=capacity if attended==attention and ready else Fraction()
        jobs=w.outside_jobs_by_month[month]
        done=min(jobs,int(remaining//w.outside_minutes_per_job)) if ready else 0
        for i in range(done):book('outside_inventory_job',Fraction(w.outside_minutes_per_job),Fraction(1),'inventory jobs',f'-{i}')
        robot=human=human_capacity=Fraction()
        if ready:
            if w.robot_handling_minutes_per_zone<=human_minutes:
                robot=min(Fraction(demand),usable,remaining/w.robot_handling_minutes_per_zone if w.robot_handling_minutes_per_zone else Fraction(demand))
                book('robot_zone_handling',robot*w.robot_handling_minutes_per_zone,robot,'cleaning zones')
            human_capacity=remaining/human_minutes
            human=min(Fraction(demand)-robot,human_capacity)
            book('human_cleaning',human*human_minutes,human,'cleaning zones')
        return dict(operator_id=op,month=month,resource_id=w.resource_id,operational=ready,
            worker_budget_minutes=budget,booked_minutes=_rational(Fraction(budget)-remaining),unused_minutes=_rational(remaining),
            supported_units=len(cohorts),supported_unit_ids=[x['unit_id'] for x in cohorts],
            robot_capacity_zones=_rational(capacity),human_minutes_per_zone=_rational(human_minutes),
            human_capacity_after_retained_work_and_robot_handling=_rational(human_capacity),
            attention_required_minutes=attention,attention_performed_minutes=_rational(attended),
            outside_required_jobs=jobs,outside_completed_jobs=done,outside_unserved_jobs=jobs-done,
            outside_unserved_ids=[f'{op}-{month}-outside_inventory_job-{i}' for i in range(done,jobs)],
            cleaning_required_zones=demand,robot_cleaning_zones=_rational(robot),human_cleaning_zones=_rational(human),
            accepted_cleaning_zones=_rational(robot+human),unserved_cleaning_zones=_rational(Fraction(demand)-robot-human),
            complete_obligation=robot+human==demand and done==jobs and attended==attention,bookings=bookings)

    def finish_shipping(self,t,month):
        # Physical support/commissioning/shipping have completed. No awards or
        # phase-6 output exist yet. Buy capacity for the declared whole-market
        # offer ceiling; losing a bid does not refund paid unused capacity.
        for op,w in self.crews.items():
            b=self.business[op]; ready=self.ready(t,b,month,5)
            cohorts,capacity,human_minutes,attention=self.work_parameters(op,month)
            demand=self.enterprise.market.baseline_units
            robot=min(Fraction(demand),capacity) if w.robot_handling_minutes_per_zone<=human_minutes else Fraction()
            needed=attention+w.outside_jobs_by_month[month]*w.outside_minutes_per_job+robot*w.robot_handling_minutes_per_zone+(demand-robot)*human_minutes
            regular=self.blocks[op]*w.minutes_per_block if ready else 0
            requested=w.overtime_minutes_per_month if ready and needed>regular else 0
            iid=self.overtime_quotes.get(op);paid=0;reason='';cash_before=t.available(self.crew_payer(op))
            if requested:
                candidate=t.settle_invoice(iid+':pay',iid,Moment(month,5),provenance=self.provenance)
                if candidate.invoice(iid).outstanding_cents:
                    assert candidate.invoice(iid).paid_cents==0
                    t=candidate.cancel_invoice(iid+':cancel',iid,Moment(month,5),provenance=self.provenance)
                    reason='unfunded_prospective_overtime'
                else:t=candidate;paid=requested
            elif iid:t=t.cancel_invoice(iid+':cancel',iid,Moment(month,5),provenance=self.provenance)
            prospect=self.allocate(op,month,regular+paid,demand,ready)
            self.crew_current[op]=dict(scheduled_blocks=self.blocks[op],regular_available_minutes=regular,
                notice_issued_month=self.notices[op],notice_effective_month=self.effective[op],
                offer_ceiling_zones=demand,offer_complete_minimum_minutes=_rational(needed),
                funded_capacity_before_awards=prospect['accepted_cleaning_zones'],outside_jobs_reserved_before_awards=prospect['outside_completed_jobs'],
                cash_before_overtime_cents=cash_before,cash_after_overtime_before_awards_cents=t.available(self.crew_payer(op)),
                overtime_requested_minutes=requested,overtime_paid_minutes=paid,overtime_invoice_id=iid,overtime_block_reason=reason)
        t=super().finish_shipping(t,month)
        for op,row in self.crew_current.items():
            assigned=sum(self.assignment[p].get(op,0) for p in POOLS)
            row.update(self.allocate(op,month,row['regular_available_minutes']+row['overtime_paid_minutes'],assigned,self.ready(t,self.business[op],month,6)))
        return t

    def capacity(self,t,operator,month):
        return rational(self.crew_current[operator]['funded_capacity_before_awards']) if self.ready(t,self.business[operator],month,5) else Fraction()

    def dispatch_output(self,month,operator,robot_capacity):
        op=operator.operator_id;row=self.crew_current[op]
        cohorts=[x for x in self.supported.values() if x['operator_id']==op]
        assert sum((rational(x['ramp_fraction'])*self.plan.system.full_output_units_per_robot_month for x in cohorts),Fraction())==robot_capacity
        allocated={p:self.assignment[p].get(op,0) for p in POOLS};demand=sum(allocated.values())
        robot=rational(row['robot_cleaning_zones']);human=rational(row['human_cleaning_zones']);total=robot+human
        served={p:total*allocated[p]/demand if demand else Fraction() for p in POOLS}
        self.period_service[op]=dict(operator_id=op,actor_id=self.business[op].actor_id,operational=row['operational'],assigned_units=allocated,
            robot_capacity_units=row['robot_capacity_zones'],human_capacity_units=row['human_capacity_after_retained_work_and_robot_handling'],robot_delivered_units=_rational(robot),
            human_delivered_units=_rational(human),total_delivered_units=_rational(total),served_by_pool={p:_rational(v) for p,v in served.items()},
            unserved_by_pool={p:_rational(Fraction(allocated[p])-served[p]) for p in POOLS})
        return demand,robot,dict(human_accepted_output_units=_rational(human),total_accepted_output_units=_rational(total),
            effective_calendar_capacity_units=row['robot_capacity_zones'],supported_unit_ids=row['supported_unit_ids'])

    def bill_service(self,t,month,units,supported):
        t=super().bill_service(t,month,units,supported)
        for op,row in self.crew_current.items():
            w=self.crews[op];amount=row['outside_completed_jobs']*w.outside_cents_per_job;iid=None
            if amount:
                iid=self._id('crew',op,month,'outside-sale')
                t=self.issue_enterprise(t,iid,outside_buyer(op),self.business[op].actor_id,amount,Moment(month,6),
                    Moment(month+w.outside_collection_lag_months,2),'outside_inventory_service')
                self.sales_ids.add(iid);self.outside_sales.add(iid)
            row.update(outside_service_invoice_id=iid,outside_service_face_cents=amount)
        return t

    def close(self,t,month,units,supported):
        super().close(t,month,units,supported)
        for op,row in self.crew_current.items():
            iid=self._id('enterprise',op,month,'human_staff');invoice=next((i for i in t.invoices if i.invoice_id==iid),None)
            row.update(staff_commitment_cents=invoice.face_cents if invoice else 0,staff_cash_paid_cents=invoice.paid_cents if invoice else 0,
                staff_unpaid_cents=invoice.outstanding_cents if invoice else 0,
                overtime_cash_paid_cents=t.invoice(row['overtime_invoice_id']).paid_cents if row['overtime_invoice_id'] else 0)
            self.crew_months.append(row)
            human=next(x for x in self.bridge_months[-1]['human_work'] if x['operator_id']==op)
            human['retained_site_crew_hours']=_rational(rational(row['booked_minutes'])/60)
            human['payroll_missing_reason']='Synthetic paid blocks and actual cash are in staffed_renewals; empirical payroll removal remains unknown.'


def source_hashes():
    return {**entry_hashes(),**{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in ('model/staffed_renewals.py','model/shared_workforce.py')}}


def run_staffed_renewals(plan,treasury,contracts,enterprise,finance,bridge,competition,transition,crews):
    policy=_StaffedRenewals(plan,contracts,treasury,enterprise,finance,bridge,competition,transition,crews)
    return staffed_renewals_result(run_monthly(plan,treasury,commercial=policy),policy)


def staffed_renewals_result(r,policy):
    """Describe one already completed execution; never run another cash/fleet loop."""
    plan=policy.plan;enterprise=policy.enterprise;bridge=policy.bridge;crews=policy.crews
    r.update(schema_version='staffed-renewals-window/0.1',scope='synthetic_separate_paid_crews_retained_work_entry_and_renewal')
    add_entry_renewal_sections(policy,r)
    r['renewing_entry']['limits']=[x for x in r['renewing_entry']['limits'] if not x.startswith('No shared site crew')]+[
        'Separate operating-company crews are added here; annual resources, typed parts, four architectures, asset recovery and endogenous learning remain separate.']
    rows=policy.crew_months;inv=r['closing_treasury']['invoices'];sales=[i for i in inv if i['invoice_id'] in policy.outside_sales]
    cash=r['entry_transition']['consolidation']['external_operating_and_transaction_cash_cents']+r['competition']['buyer_switch_resource_cash_cents']
    vendors=policy.resource_vendors()
    assert cash==sum(i['paid_cents'] for i in inv if i['payee'] in vendors)
    r['staffed_renewals']=dict(schema_version='staffed-renewals-boundary/0.1',inputs={op:asdict(w) for op,w in crews.items()},months=rows,events=policy.crew_events,
        cash=dict(staff_commitments_cents=sum(x['staff_commitment_cents'] for x in rows),staff_paid_cents=sum(x['staff_cash_paid_cents'] for x in rows),
            overtime_paid_cents=sum(x['overtime_cash_paid_cents'] for x in rows),outside_service_invoiced_cents=sum(i['face_cents'] for i in sales),
            outside_service_received_cents=sum(i['paid_cents'] for i in sales),outside_service_unpaid_cents=sum(i['outstanding_cents'] for i in sales),
            all_payer_resource_and_transaction_cash_cents=cash,included_in_existing_consolidation=True,add_again=False),
        information_clock='Prior complete month qualifies notice; a fixed overtime-block quote is issued in phase1. Mandatory staffing and physical work precede phase5 optional full prepayment. Reserve local attention and outside work before awards. Dispatch actual assigned cleaning; phase6 receipts cannot fund phase5 offers.',
        metric_lineage=[dict(metric='crew conservation',equation='local attention + outside jobs + robot handling + human cleaning + unused = regular paid capacity + fully prepaid overtime'),
            dict(metric='funded offer capacity',equation='maximum cleaning within paid qualified minutes after retained work, capped at the fixed market ceiling'),
            dict(metric='whole service',equation='fixed market accepted zones AND each separately due outside job; unlike units are never summed'),
            dict(metric='all-payer cash',equation='entry-wide external resource/transaction payments + outside customer switching payments = actual outside resource-vendor receipts')],
        limits=['All crew blocks, qualifications, notice, work rates, overtime and contract prices are synthetic; no empirical labor law or removed-payroll estimate.',
            'Monthly divisible cleaning and indivisible outside jobs omit within-shift travel and timed job deadlines.',
            'A fixed optional overtime block targets the full market before awards and must be prepaid in full. Losing bids can leave paid unused minutes; this is a declared policy, not an optimized offer or roster.',
            'Notice tests only prior completed assigned work and supported units, not guaranteed future demand or retained-work loads; it remains binding after later shortfall.',
            'Each legal operator has a different qualified crew, staffing obligation and cash account. Common ownership alone pools neither.',
            'Outside duties persist after lost cleaning contracts. Unperformed duties, uncovered lots, unpaid bills and terminal claims remain visible.',
            'Fees and underlying resource payments are different boundaries. Outside-work invoices are already in consolidated service receipts, with separate unit/cash rows here.',
            'No severance, empirical all-service cost, six-cell portfolio, actual human headcount or lifecycle return is inferred.'])
    r['source_sha256']=source_hashes();r=canonical_wire(r)
    r['case_hash']=hashlib.sha256(json.dumps(r,sort_keys=True,separators=(',',':')).encode()).hexdigest()
    return json.loads(json.dumps(r))


def staffed_renewals_inputs(inputs=None):
    if inputs is None:inputs={}
    if not isinstance(inputs,dict) or set(inputs)-{'entry','crews'}:raise ValueError('Unknown staffed-renewal inputs')
    if not isinstance(inputs.get('entry',{}),dict) or not isinstance(inputs.get('crews',{}),dict):raise ValueError('Entry and crews must be objects')
    if set(inputs.get('crews',{}))-{'incumbent','entrant'}:raise ValueError('Unknown crew operator')
    entry={'target_cash_cents':15_000_000,'growth_equity_cents':15_000_000,'buyer_cash_cents':40_000_000,'human_efficiency':.25,**inputs.get('entry',{})}
    entry['market']={'incumbent_robots':1,'entrant_robots':0,'competition':{'response_mode':'calendar_human'},**entry.get('market',{})}
    p,t,cs,e,f,b,c,tr=renewing_entry_inputs(entry);p=replace(p,plan_id='staffed-renewals')
    crews={op:Workforce(**dict(resource_id='qualified-crew-'+op,opening_blocks=2 if op=='incumbent' else 1,
        target_blocks=None,notice_supported_units=1,overtime_minutes_per_month=0,
        outside_jobs_by_month=(20 if op=='incumbent' else 0,)*p.months)|inputs.get('crews',{}).get(op,{})) for op in ('incumbent','entrant')}
    _,_,_,cell,_,calendar=bridge_context(b,p.months);businesses=[]
    for v in e.businesses:
        w=crews[v.operator_id];staff=w.opening_blocks*round_cents(Fraction(w.minutes_per_block,60)*exact(cell['wage_usd_hour'])*100)
        caps=tuple(int(Fraction(staff,100)/exact(cell['wage_usd_hour'])/exact(cell['human_hours_per_unit'])/(1-(exact(row['effective_parameters']['digital_efficiency']) if b.digital_enabled else 0))) for row in calendar)
        businesses.append(replace(v,human_staff_cents_by_month=(staff,)*p.months,human_capacity_by_month=caps))
    e=replace(e,businesses=tuple(businesses));t=replace(t,accounts=t.accounts+tuple(Account(outside_buyer(op),w.outside_buyer_opening_cash_cents) for op,w in crews.items()))
    return p,t,cs,e,f,b,c,tr,crews


def run_staffed_renewals_case(inputs=None):return run_staffed_renewals(*staffed_renewals_inputs(inputs))


def replay_staffed_renewals(saved):
    if not isinstance(saved,dict) or saved.get('schema_version')!='staffed-renewals-window/0.1':raise ValueError('Complete staffed-renewal case required')
    try:
        e=dict(saved['enterprise']['inputs']);e['market']=Market(**e['market'])
        for key,cls in [('businesses',Business),('moves',CustomerMove),('equity',Equity)]:e[key]=tuple(cls(**x) for x in e[key])
        f=dict(saved['finance']['inputs']);f['loans']=tuple(TermLoan(**x) for x in f['loans'])
        return run_staffed_renewals(*restore_opening_inputs(saved),EnterprisePlan(**e),FinancePlan(**f),Bridge(**saved['calendar_bridge']['inputs']),
            Competition(**saved['competition']['inputs']),Transition(**saved['entry_transition']['inputs']),
            {op:Workforce(**w) for op,w in saved['staffed_renewals']['inputs'].items()})
    except (KeyError,TypeError,AttributeError) as exc:raise ValueError('Incomplete staffed-renewal inputs') from exc


def staffed_renewals_worlds():
    return {'complete_control':{},'binding_staff_cut':{'crews':{'incumbent':{'target_blocks':1}}},
        'outside_surge_after_notice':{'crews':{'incumbent':{'target_blocks':1,'outside_jobs_by_month':[20]*4+[45]*4}}},
        'prepaid_fallback':{'crews':{'incumbent':{'target_blocks':1,'outside_jobs_by_month':[20]*4+[45]*4,'overtime_minutes_per_month':5000}}},
        'human_no_robot':{'entry':{'market':{'incumbent_robots':0,'entrant_robots':0}}},
        'long_locked_contracts':{'entry':{'market':{'competition':{'term_months':4,'breach_exit':False,'response_mode':'calendar_human'}}},
            'crews':{'incumbent':{'target_blocks':1,'outside_jobs_by_month':[20]*4+[45]*4}}},
        'strong_paid_human_rival':{'crews':{'incumbent':{'target_blocks':1,'outside_jobs_by_month':[20]*4+[45]*4},'entrant':{'opening_blocks':2}}},
        'independent_firms':{'entry':{'mode':'build'},'crews':{'incumbent':{'target_blocks':1}}},
        'human_two_minutes_short':{'entry':{'market':{'incumbent_robots':0,'entrant_robots':0}},'crews':{'incumbent':{'minutes_per_block':4799}}},
        'exact_overtime_funding':{'entry':{'target_cash_cents':785000,'market':{'incumbent_robots':0,'entrant_robots':0}},'crews':{'incumbent':{'opening_blocks':1,'overtime_minutes_per_month':4800}}},
        'one_cent_short_overtime':{'entry':{'target_cash_cents':784999,'market':{'incumbent_robots':0,'entrant_robots':0}},'crews':{'incumbent':{'opening_blocks':1,'overtime_minutes_per_month':4800}}},
        'strong_human_surge':{'entry':{'market':{'incumbent_robots':0,'entrant_robots':0}},'crews':{'incumbent':{'opening_blocks':3,'outside_jobs_by_month':[20]*4+[45]*4}}},
        'paid_losing_offer':{'entry':{'market':{'competition':{'response_mode':'calendar_human','entrant_offer_cents':2300}}},
            'crews':{'incumbent':{'target_blocks':1,'overtime_minutes_per_month':5000}}}}


def staffed_renewals_summary(name,r):
    w=r['staffed_renewals'];rows=w['months'];market=r['enterprise']['months']
    return dict(case=name,complete_market_months=sum(rational(m['total_delivered_units'])==r['enterprise']['inputs']['market']['baseline_units'] for m in market),
        complete_whole_service_months=sum(rational(m['total_delivered_units'])==r['enterprise']['inputs']['market']['baseline_units'] and all(x['complete_obligation'] for x in rows if x['month']==m['month']) for m in market),
        accepted_zones=_rational(sum((rational(m['total_delivered_units']) for m in market),Fraction())),outside_required_jobs=sum(x['outside_required_jobs'] for x in rows),outside_completed_jobs=sum(x['outside_completed_jobs'] for x in rows),
        final_assigned_units={op:sum(l['units'] for l in r['competition']['months'][-1]['lots'] if l['owner']==op) for op in ('incumbent','entrant')},
        paid_unused_minutes=_rational(sum((rational(x['unused_minutes']) for x in rows),Fraction())),
        notice_effective_months={op:next(x['notice_effective_month'] for x in reversed(rows) if x['operator_id']==op) for op in ('incumbent','entrant')},
        **w['cash'],case_hash=r['case_hash'])


def staffed_renewals_artifact():
    options=staffed_renewals_worlds();cases={k:run_staffed_renewals_case(v) for k,v in options.items()}
    return canonical_wire(dict(schema_version='staffed-renewals-artifact/0.1',case_inputs=options,cases=cases,
        summary=[staffed_renewals_summary(k,r) for k,r in cases.items()],source_sha256=source_hashes(),
        comparison_boundary='One physical/Treasury execution; actual awards and separate qualified crews share retained-work constraints. Both service units and every payer remain distinct. Synthetic policies, no empirical payroll or optimized roster.'))


def staffed_renewals_catalog():
    data=json.loads((ROOT/'model/results/staffed_renewals.json').read_text())
    if data['source_sha256']!=source_hashes():raise ValueError('Staffed-renewals export is stale; regenerate')
    return {k:v for k,v in data.items() if k!='cases'}|{'cases':{'complete_control':data['cases']['complete_control']}}
