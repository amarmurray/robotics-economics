"""One synthetic service market, funded businesses, and the shared robot ledger."""
from __future__ import annotations
from dataclasses import asdict, dataclass, replace
from fractions import Fraction
import hashlib
import json
from pathlib import Path

from model.monthly_commercial import Contract, _Commercial, restore_opening_inputs
from model.monthly_deployment import Plan, Operator, Start, System, _integer, _name, _series, _rational, run_monthly
from model.treasury import Account, Moment, Treasury

POOLS = ("baseline", "unmet", "new")


@dataclass(frozen=True)
class Business:
    operator_id: str
    actor_id: str
    overhead_cents_by_month: tuple[int, ...]
    human_capacity_by_month: tuple[int, ...]
    human_staff_cents_by_month: tuple[int, ...]
    price_cents_per_unit_by_month: tuple[int, ...]
    receipt_lag_by_month: tuple[int, ...]
    active_from_month: int | None = 0
    qualified_month: int = 0
    procurement_month: int = 0
    formation_cents: int = 0
    acquisition_cents_per_recurring_unit: int = 0
    material_cents_per_delivered_unit: int = 0

    def __post_init__(self):
        _name(self.operator_id); _name(self.actor_id)
        for key in ("overhead_cents_by_month", "human_capacity_by_month", "human_staff_cents_by_month",
                    "price_cents_per_unit_by_month", "receipt_lag_by_month"):
            object.__setattr__(self, key, _series(getattr(self, key)))
        if self.active_from_month is not None:
            _integer(self.active_from_month)
        for key in ("qualified_month", "procurement_month", "formation_cents", "acquisition_cents_per_recurring_unit", "material_cents_per_delivered_unit"):
            _integer(getattr(self, key))
        if any(x < 1 for x in self.receipt_lag_by_month):
            raise ValueError("End-market collection lag must be positive")
        if len(self.human_capacity_by_month) != len(self.human_staff_cents_by_month) or any(
                cap > 0 and cost == 0 for cap, cost in zip(self.human_capacity_by_month, self.human_staff_cents_by_month)):
            raise ValueError("Human capacity requires an explicit positive staffing commitment")


@dataclass(frozen=True)
class Market:
    work_id: str
    incumbent_operator: str
    buyer_actor: str
    baseline_units: int
    unmet_units: int
    new_units: int

    def __post_init__(self):
        for x in (self.work_id, self.incumbent_operator, self.buyer_actor): _name(x)
        for x in (self.baseline_units, self.unmet_units, self.new_units): _integer(x)


@dataclass(frozen=True)
class CustomerMove:
    move_id: str
    month: int
    pool: str
    from_operator: str | None
    to_operator: str | None
    units: int

    def __post_init__(self):
        _name(self.move_id); _integer(self.month); _integer(self.units, 1)
        if self.pool not in POOLS or self.from_operator == self.to_operator:
            raise ValueError("Invalid customer assignment transfer")
        for x in (self.from_operator, self.to_operator):
            if x is not None: _name(x)


@dataclass(frozen=True)
class Equity:
    funding_id: str
    month: int
    funder_actor: str
    recipient_actor: str
    amount_cents: int

    def __post_init__(self):
        for x in (self.funding_id,self.funder_actor,self.recipient_actor): _name(x)
        _integer(self.month); _integer(self.amount_cents,1)
        if self.funder_actor == self.recipient_actor: raise ValueError("Equity needs two legal actors")


@dataclass(frozen=True)
class EnterprisePlan:
    market: Market
    businesses: tuple[Business, ...]
    moves: tuple[CustomerMove, ...] = ()
    equity: tuple[Equity, ...] = ()
    enterprise_vendor_actor: str = "enterprise_vendor"
    material_credit_months: int = 1

    def __post_init__(self):
        if not isinstance(self.market, Market): raise ValueError("Explicit common market required")
        _name(self.enterprise_vendor_actor); _integer(self.material_credit_months,1)
        for key, cls in (("businesses",Business),("moves",CustomerMove),("equity",Equity)):
            value=getattr(self,key)
            if not isinstance(value,(tuple,list)) or any(not isinstance(x,cls) for x in value):
                raise ValueError("Invalid "+key)
            object.__setattr__(self,key,tuple(value))


def round_cents(amount):
    """Nonnegative exact rational cents; one nearest-cent, half-up invoice rounding."""
    amount=Fraction(amount)
    if amount<0: raise ValueError("Negative invoice charge")
    return (2*amount.numerator+amount.denominator)//(2*amount.denominator)


class _Enterprise(_Commercial):
    def __init__(self, plan, contracts, treasury, enterprise):
        super().__init__(plan,contracts,treasury)
        if not isinstance(enterprise,EnterprisePlan): raise ValueError("Enterprise plan required")
        self.enterprise=enterprise
        self.business={b.operator_id:b for b in enterprise.businesses}
        if len(self.business)!=len(enterprise.businesses) or set(self.business)!=set(self.by_site) or len(self.business)!=2:
            raise ValueError("Exactly two unique businesses must match the common physical operators")
        market=enterprise.market
        if market.incumbent_operator not in self.business or market.work_id!=plan.system.work_id:
            raise ValueError("Market identity/work profile must match the physical plan")
        if len({b.actor_id for b in enterprise.businesses})!=len(self.business):
            raise ValueError("Incumbent and entrant must have separate legal accounts")
        for b in enterprise.businesses:
            if b.actor_id!=self.by_site[b.operator_id].customer_actor:
                raise ValueError("Business actor must match its robot-contract customer")
            for key in ("overhead_cents_by_month","human_capacity_by_month","human_staff_cents_by_month","price_cents_per_unit_by_month","receipt_lag_by_month"):
                if len(getattr(b,key))!=plan.months: raise ValueError("Explicit business input required for every month")
            if any(o.opening_installed and b.active_from_month!=0 for o in plan.operators if o.operator_id==b.operator_id):
                raise ValueError("Opening installed stock requires an active business")
        for values,key in ((enterprise.moves,"move_id"),(enterprise.equity,"funding_id")):
            if len({getattr(x,key) for x in values})!=len(values) or any(x.month>=plan.months for x in values):
                raise ValueError("Duplicate/out-of-horizon enterprise action")
        business_actors={b.actor_id for b in enterprise.businesses}
        if any(i.payer in business_actors and not i.cancellable and i.due_at.phase!=3 for i in treasury.invoices):
            raise ValueError("Opening business obligations require phase-3 due dates in this scheduler")
        for move in enterprise.moves:
            if any(x is not None and x not in self.business for x in (move.from_operator,move.to_operator)):
                raise ValueError("Unknown customer assignment endpoint")
        outsiders={market.buyer_actor,enterprise.enterprise_vendor_actor}
        if len(outsiders)!=2 or outsiders.intersection(self.parties) or outsiders.intersection((plan.manufacturing_vendor_actor,plan.deployment_vendor_actor)):
            raise ValueError("End buyer and enterprise vendor must be distinct outside counterparties")
        for actor in outsiders: treasury.account(actor)
        for f in enterprise.equity:
            treasury.account(f.funder_actor);treasury.account(f.recipient_actor)
            if f.recipient_actor not in self.parties or f.funder_actor in self.parties or f.funder_actor in outsiders or f.funder_actor in (plan.manufacturing_vendor_actor,plan.deployment_vendor_actor):
                raise ValueError("Equity must come from a separate, funded outside investor")
        self.assignment={"baseline":{market.incumbent_operator:market.baseline_units},
                         "unmet":{None:market.unmet_units},"new":{None:market.new_units}}
        self.pool_size={p:getattr(market,p+"_units") for p in POOLS}
        self.enterprise_events=[];self.market_months=[];self.invoice_lines=[]
        self.formation_ids={};self.acquisition_ids={};self.sales_ids=set();self.equity_ids=set();self.enterprise_cost_ids=set()
        self.period_service={};self.current_treasury=treasury

    def event(self, month, phase, action, **detail):
        self.enterprise_events.append({"event_id":self._id("enterprise-event",len(self.enterprise_events)+1),
                                      "at":asdict(Moment(month,phase)),"action":action,**detail})

    def active(self,b,month):
        return b.active_from_month is not None and month>=b.active_from_month

    def ready(self,t,b,month,phase=5):
        if not self.active(b,month) or month<b.qualified_month: return False
        formation=self.formation_ids.get(b.operator_id)
        if b.formation_cents and (formation is None or t.invoice(formation).outstanding_cents): return False
        return not any(i.payer==b.actor_id and not i.cancellable and i.outstanding_cents and i.due_at<=Moment(month,phase) for i in t.invoices)

    def issue_enterprise(self,t,iid,payer,payee,amount,at,due,category,cancellable=False):
        return t.issue_invoice(iid+":issue",iid,payer,payee,amount,at,due,due,
                                provenance=self.provenance,cancellable=cancellable,category=category)

    def prepare(self,t,month,units):
        t=super().prepare(t,month,units)
        self.period_service={}
        vendor=self.enterprise.enterprise_vendor_actor
        for b in self.enterprise.businesses:
            if not self.active(b,month): continue
            costs=[("overhead",b.overhead_cents_by_month[month]),("human_staff",b.human_staff_cents_by_month[month])]
            if month==b.active_from_month: costs.insert(0,("formation",b.formation_cents))
            for category,amount in costs:
                if not amount: continue
                iid=self._id("enterprise",b.operator_id,month,category)
                t=self.issue_enterprise(t,iid,b.actor_id,vendor,amount,Moment(month,1),Moment(month,3),category)
                self.enterprise_cost_ids.add(iid)
                if category=="formation": self.formation_ids[b.operator_id]=iid
        for move in (m for m in self.enterprise.moves if m.month==month and m.to_operator is not None):
            b=self.business[move.to_operator];amount=move.units*b.acquisition_cents_per_recurring_unit
            if amount:
                iid=self._id("acquisition",move.move_id)
                t=self.issue_enterprise(t,iid,b.actor_id,vendor,amount,Moment(month,1),Moment(month,5),"customer_acquisition",True)
                self.acquisition_ids[move.move_id]=iid;self.enterprise_cost_ids.add(iid)
        if month==0:
            for f in self.enterprise.equity:
                iid=self._id("equity",f.funding_id)
                t=self.issue_enterprise(t,iid,f.funder_actor,f.recipient_actor,f.amount_cents,Moment(0,1),Moment(f.month,2),"equity_contribution")
                self.equity_ids.add(iid)
        return t

    def collect_set(self,t,month,phase,ids):
        blocked=set()
        due=sorted((i for i in t.invoices if i.invoice_id in ids and i.outstanding_cents and i.due_at<=Moment(month,phase)),
                   key=lambda i:(i.due_at,i.issued_at,i.invoice_id))
        for i in due:
            if i.payer in blocked: continue
            t=t.settle_invoice(self._id("enterprise-collect",month,phase,i.invoice_id),i.invoice_id,Moment(month,phase),provenance=self.provenance)
            if t.invoice(i.invoice_id).outstanding_cents: blocked.add(i.payer)
        return t

    def collect(self,t,month):
        t=self.collect_set(t,month,2,self.sales_ids|self.equity_ids)
        return super().collect(t,month)

    def mandatory(self,t,month):
        t=self.refunds(t,month)
        actors={b.actor_id for b in self.enterprise.businesses}
        due={i.invoice_id for i in t.invoices if i.payer in actors and not i.cancellable}
        t=self.collect_set(t,month,3,due)
        self.current_treasury=t
        return t

    def assignment_enabled(self,operator_id,month):
        b=self.business[operator_id]
        return super().assignment_enabled(operator_id,month) and month>=b.procurement_month and self.ready(self.current_treasury,b,month)

    def _reason(self,t,month,phase,action,operator_id):
        reason=super()._reason(t,month,phase,action,operator_id)
        if reason or action=="start": return reason
        b=self.business[operator_id]
        if not self.ready(t,b,month,phase): return "enterprise_unqualified_or_overdue"
        if action=="ship" and month<b.procurement_month: return "procurement_not_yet_eligible"
        return ""

    def finish_shipping(self,t,month):
        t=super().finish_shipping(t,month)
        for move in (m for m in self.enterprise.moves if m.month==month):
            owners=self.assignment[move.pool];iid=self.acquisition_ids.get(move.move_id)
            reason="insufficient_source_assignment" if owners.get(move.from_operator,0)<move.units else ""
            if move.to_operator is not None and not self.ready(t,self.business[move.to_operator],month):
                reason=reason or "target_unqualified_or_overdue"
            if not reason and iid:
                t=t.settle_invoice(iid+":pay",iid,Moment(month,5),provenance=self.provenance)
                if t.invoice(iid).outstanding_cents: reason="unfunded_customer_acquisition"
            if reason and iid:
                t=t.cancel_invoice(iid+":cancel",iid,Moment(month,5),provenance=self.provenance)
            if not reason:
                owners[move.from_operator]=owners.get(move.from_operator,0)-move.units
                owners[move.to_operator]=owners.get(move.to_operator,0)+move.units
            self.event(month,5,"customer_move",move=asdict(move),status="blocked" if reason else "assigned",reason=reason,invoice_id=iid)
        self.current_treasury=t
        return t

    def dispatch_output(self,month,operator,robot_capacity):
        b=self.business[operator.operator_id];ready=self.ready(self.current_treasury,b,month,6)
        allocated={p:self.assignment[p].get(operator.operator_id,0) for p in POOLS}
        demand=sum(allocated.values())
        if demand>operator.demand_units_by_month[month]: raise ValueError("Common demand exceeds the declared physical planning ceiling")
        robot=min(Fraction(demand),robot_capacity) if ready else Fraction()
        human_capacity=b.human_capacity_by_month[month] if ready else 0
        human=min(Fraction(demand)-robot,Fraction(human_capacity))
        total=robot+human
        served={p:total*allocated[p]/demand if demand else Fraction() for p in POOLS}
        record={"operator_id":operator.operator_id,"actor_id":b.actor_id,"operational":ready,
                "assigned_units":allocated,"robot_capacity_units":_rational(robot_capacity),
                "human_capacity_units":human_capacity,"robot_delivered_units":_rational(robot),
                "human_delivered_units":_rational(human),"total_delivered_units":_rational(total),
                "served_by_pool":{p:_rational(v) for p,v in served.items()},
                "unserved_by_pool":{p:_rational(Fraction(allocated[p])-served[p]) for p in POOLS}}
        self.period_service[operator.operator_id]=record
        return demand,robot,{"human_accepted_output_units":_rational(human),"total_accepted_output_units":_rational(total)}

    def billed(self,t,month,b,category,payer,payee,rate,due):
        service=self.period_service[b.operator_id]
        amount=Fraction(**service["total_delivered_units"])*rate
        rounded=round_cents(amount);iid=self._id("enterprise",b.operator_id,month,category)
        if rounded:
            t=self.issue_enterprise(t,iid,payer,payee,rounded,Moment(month,6),due,category)
            (self.sales_ids if category=="end_market_sale" else self.enterprise_cost_ids).add(iid)
        self.invoice_lines.append({"month":month,"operator_id":b.operator_id,"category":category,
            "invoice_id":iid if rounded else None,"accepted_units":service["total_delivered_units"],
            "rate_cents_per_unit":rate,"unrounded_cents":_rational(amount),"face_cents":rounded,
            "rounding_difference_cents":_rational(Fraction(rounded)-amount),"due_at":asdict(due)})
        return t

    def bill_service(self,t,month,units,supported):
        t=super().bill_service(t,month,units,supported)
        for b in self.enterprise.businesses:
            t=self.billed(t,month,b,"end_market_sale",self.enterprise.market.buyer_actor,b.actor_id,
                          b.price_cents_per_unit_by_month[month],Moment(month+b.receipt_lag_by_month[month],2))
            t=self.billed(t,month,b,"materials",b.actor_id,self.enterprise.enterprise_vendor_actor,
                          b.material_cents_per_delivered_unit,Moment(month+self.enterprise.material_credit_months,3))
        return t

    def close(self,t,month,units,supported):
        super().close(t,month,units,supported)
        pools={}
        for pool in POOLS:
            assignment=self.assignment[pool]
            delivered=sum((Fraction(**r["served_by_pool"][pool]) for r in self.period_service.values()),Fraction())
            assert sum(assignment.values())==self.pool_size[pool] and all(x>=0 for x in assignment.values())
            assert 0<=delivered<=self.pool_size[pool]
            pools[pool]={"recurring_demand_units":self.pool_size[pool],
                         "assignments":[{"operator_id":k,"units":v} for k,v in assignment.items()],
                         "delivered_units":_rational(delivered),"unserved_units":_rational(Fraction(self.pool_size[pool])-delivered)}
        total=sum((Fraction(**p["delivered_units"]) for p in pools.values()),Fraction())
        assert total==sum((Fraction(**r["total_delivered_units"]) for r in self.period_service.values()),Fraction())
        self.market_months.append({"month":month,"pools":pools,"operators":list(self.period_service.values()),
                                   "total_delivered_units":_rational(total),
                                   "due_unpaid_by_actor_cents":{b.actor_id:sum(i.outstanding_cents for i in t.invoices
                                        if i.payer==b.actor_id and not i.cancellable and i.due_at<=Moment(month,7))
                                        for b in self.enterprise.businesses},
                                   "baseline_equivalent_labor_hours":None,
                                   "labor_conversion_unknown_reason":"No observed or assumed hours-per-bundle conversion supplied"})

    def enterprise_result(self,r):
        invoices=r["closing_treasury"]["invoices"]
        sales=sum(i["paid_cents"] for i in invoices if i["invoice_id"] in self.sales_ids)
        equity=sum(i["paid_cents"] for i in invoices if i["invoice_id"] in self.equity_ids)
        enterprise_outlay=sum(i["paid_cents"] for i in invoices if i["invoice_id"] in self.enterprise_cost_ids)
        physical=r["commercial"]["consolidation"]["external_physical_outlay_cents"]
        net=r["commercial"]["consolidation"]["included_cash_change_cents"]
        min_cash={a["actor_id"]:a["cash_cents"] for a in r["opening_treasury"]["actors"] if a["actor_id"] in self.parties}
        balances=dict(min_cash)
        opening_count=len(r["opening_treasury"]["events"])
        for e in r["closing_treasury"]["events"][opening_count:]:
            for p in e["postings"]:
                if p["actor_id"] in balances:
                    balances[p["actor_id"]]+=p["delta_cents"]
                    min_cash[p["actor_id"]]=min(min_cash[p["actor_id"]],balances[p["actor_id"]])
        outcomes=[]
        invoice_by_id={i["invoice_id"]:i for i in invoices}
        for b in self.enterprise.businesses:
            failed=[e for e in r["closing_treasury"]["events"][opening_count:] if e["kind"]=="invoice_payment"
                    and e["status"] in ("blocked","partial") and invoice_by_id[e["reference_id"]]["payer"]==b.actor_id]
            service=[next(o for o in row["operators"] if o["operator_id"]==b.operator_id) for row in self.market_months]
            outcomes.append({"operator_id":b.operator_id,"actor_id":b.actor_id,
                "first_failed_payment_at":failed[0]["at"] if failed else None,
                "first_failed_invoice_id":failed[0]["reference_id"] if failed else None,
                "months_with_due_unpaid_obligations":sum(row["due_unpaid_by_actor_cents"][b.actor_id]>0 for row in self.market_months),
                "total_delivered_units":_rational(sum((Fraction(**o["total_delivered_units"]) for o in service),Fraction())),
                "minimum_actual_cash_cents":min_cash[b.actor_id],
                "closing_due_unpaid_cents":self.market_months[-1]["due_unpaid_by_actor_cents"][b.actor_id],
                "closing_receivables_cents":sum(i["outstanding_cents"] for i in invoices if i["invoice_id"] in self.sales_ids and i["payee"]==b.actor_id)})
        return {"schema_version":"shared-enterprise/0.1","scope":"synthetic_one_market_common_physical_and_financial_execution",
                "inputs":asdict(self.enterprise),"months":self.market_months,"events":self.enterprise_events,"invoice_lines":self.invoice_lines,
                "minimum_actual_cash_cents":min_cash,"business_outcomes":outcomes,
                "consolidation":{"included_actors":self.parties,"end_market_cash_received_cents":sales,
                    "equity_cash_received_cents":equity,"external_physical_outlay_cents":physical,
                    "external_enterprise_outlay_cents":enterprise_outlay,"included_cash_change_cents":net,
                    "other_boundary_cash_cents":net-(sales+equity-physical-enterprise_outlay)},
                "limits":["Synthetic fixed recurring demand and explicit customer moves, not estimated demand/retention",
                          "Human shifts and robot costs have distinct explicit boundaries; no observed payroll removal",
                          "No automatic loan draw, maturity schedule, autonomous reinvestment, repossession or insolvency resolution",
                          "No annual cleaning-zone or K architecture cost bridge; no inferred labor-hour conversion",
                          "Historical ENTRY-FG-01 is a separate reference, not added to this market"]}


def run_enterprise(plan,treasury,contracts,enterprise):
    policy=_Enterprise(plan,contracts,treasury,enterprise)
    r=run_monthly(plan,treasury,commercial=policy)
    r.update(schema_version="monthly-deployment/0.3",scope="synthetic_stage_4_shared_enterprise",
             ownership="one_title_owner_per_unit_separate_from_custody_and_workflow")
    r["commercial"]=policy.result(r)
    r["commercial"]["limits"]=["Contract accounting shares this result's enterprise market; full scope is in enterprise.limits"]
    r["enterprise"]=policy.enterprise_result(r)
    r["source_sha256"]=enterprise_source_hashes()
    r["case_hash"]=hashlib.sha256(json.dumps(r,sort_keys=True,separators=(",",":")).encode()).hexdigest()
    return json.loads(json.dumps(r))


def reference_inputs(*,entrant_cash=2_500_000,incumbent_procurement=0,response_month=6,delayed_receipts=False,no_entry=False,extra_equity=0):
    n=8
    operators=(Operator("incumbent",4,(1300,)*n,2),Operator("entrant",0 if no_entry else 10,(1300,)*n))
    p=Plan("shared-enterprise",n,operators,("incumbent","incumbent","entrant"),(0,)*n,(3,)*n,(5,)*n,(5,)*n,
           system=System(work_id="WORK-FLOOR-BUNDLE-SYN-02"),opening_components=100,starts=(Start("A",0,5,5),))
    t=Treasury((Account("provider",20_000_000),Account("incumbent",50_000_000),Account("entrant",entrant_cash),
                Account("lessor",50_000_000),Account("manufacturer",0),Account("deployment_vendor",0),
                Account("enterprise_vendor",0),Account("end_buyers",1_000_000_000),Account("investor",100_000_000)))
    cs=tuple(Contract("contract-"+o.operator_id,o.operator_id,o.operator_id,"lease","lessor",rent_cents_per_robot_month=150_000) for o in operators)
    businesses=(Business("incumbent","incumbent",(100_000,)*n,(1000,)*n,(7_500_000,)*n,(10_000,)*n,(1,)*n,
                         procurement_month=incumbent_procurement,material_cents_per_delivered_unit=1_000,acquisition_cents_per_recurring_unit=5_000),
                Business("entrant","entrant",(200_000,)*n,(0,)*n,(0,)*n,(10_000,)*n,
                         tuple(4 if delayed_receipts and m>=3 else 1 for m in range(n)),
                         active_from_month=None if no_entry else 0,formation_cents=500_000,
                         acquisition_cents_per_recurring_unit=5_000,material_cents_per_delivered_unit=1_000))
    moves=[] if no_entry else [CustomerMove("capture-baseline",2,"baseline","incumbent","entrant",70),
                               CustomerMove("capture-unmet",2,"unmet",None,"entrant",20),
                               CustomerMove("capture-new",2,"new",None,"entrant",10)]
    if not no_entry and response_month is not None:
        moves.append(CustomerMove("incumbent-response",response_month,"baseline","entrant","incumbent",70))
    equity=(Equity("bridge",0,"investor","entrant",extra_equity),) if extra_equity else ()
    e=EnterprisePlan(Market("WORK-FLOOR-BUNDLE-SYN-02","incumbent","end_buyers",1000,200,100),businesses,tuple(moves),equity)
    return p,t,cs,e


REFERENCE_DEFAULTS={"entrant_cash_cents":2_500_000,"incumbent_procurement_month":0,"response_month":6,
                    "delayed_receipts":False,"no_entry":False,"extra_equity_cents":0}


def shared_case_inputs(overrides=None):
    if overrides is None: overrides={}
    if not isinstance(overrides,dict) or set(overrides)-set(REFERENCE_DEFAULTS):
        raise ValueError("Unknown shared-enterprise input")
    inputs={**REFERENCE_DEFAULTS,**overrides}
    for key in ("entrant_cash_cents","extra_equity_cents"):
        _integer(inputs[key])
        if inputs[key]>1_000_000_000:raise ValueError("Cash input exceeds the declared experiment range")
    for key in ("incumbent_procurement_month","response_month"):
        if key=="response_month" and inputs[key] is None:continue
        _integer(inputs[key])
        if inputs[key]>7:raise ValueError("Response/procurement month must be within 0..7")
    for key in ("delayed_receipts","no_entry"):
        if type(inputs[key]) is not bool:raise ValueError("Explicit Boolean required for "+key)
    return inputs


def run_shared_case(overrides=None):
    inputs=shared_case_inputs(overrides)
    r=run_enterprise(*reference_inputs(entrant_cash=inputs["entrant_cash_cents"],
        incumbent_procurement=inputs["incumbent_procurement_month"],response_month=inputs["response_month"],
        delayed_receipts=inputs["delayed_receipts"],no_entry=inputs["no_entry"],extra_equity=inputs["extra_equity_cents"]))
    return {"inputs":inputs,"result":r,"source_sha256":enterprise_source_hashes()}


def witness_input_options():
    options={"shared_reference":{},"incumbent_only":{"no_entry":True},"prompt_customer_response":{"response_month":3},
             "delayed_incumbent_procurement":{"incumbent_procurement_month":3},
             "formation_unfunded":{"entrant_cash_cents":100_000},
             "late_receipts_no_automatic_switchback":{"entrant_cash_cents":2_050_000,"response_month":None,"delayed_receipts":True},
             "late_receipts_explicit_switchback":{"entrant_cash_cents":2_050_000,"response_month":5,"delayed_receipts":True},
             "additional_equity":{"entrant_cash_cents":100_000,"extra_equity_cents":1_895_000}}
    return {name:shared_case_inputs(kw) for name,kw in options.items()}


def enterprise_witnesses():
    return {name:run_shared_case(kw)["result"] for name,kw in witness_input_options().items()}


def replay_enterprise(saved):
    if not isinstance(saved,dict) or saved.get("schema_version")!="monthly-deployment/0.3":
        raise ValueError("A saved shared-enterprise case is required")
    data=dict(saved["enterprise"]["inputs"])
    data["market"]=Market(**data["market"])
    for key,cls in (("businesses",Business),("moves",CustomerMove),("equity",Equity)):
        data[key]=tuple(cls(**x) for x in data[key])
    return run_enterprise(*restore_opening_inputs(saved),EnterprisePlan(**data))


def minimum_reference_bridge(maximum_cents=2_400_000):
    """Find extra opening equity for this fixed policy, not optimal fund raising."""
    _integer(maximum_cents,1)
    target=run_enterprise(*reference_inputs(entrant_cash=100_000,extra_equity=maximum_cents))
    target_physical=[(m["flows"],m["outputs"]) for m in target["months"]]
    target_market=[m["pools"] for m in target["enterprise"]["months"]]
    def qualifies(r):
        actor=next(b for b in r["enterprise"]["business_outcomes"] if b["actor_id"]=="entrant")
        return (actor["first_failed_payment_at"] is None
                and all(e["status"]=="assigned" for e in r["enterprise"]["events"] if e["action"]=="customer_move")
                and [(m["flows"],m["outputs"]) for m in r["months"]]==target_physical
                and [m["pools"] for m in r["enterprise"]["months"]]==target_market)
    if not qualifies(target): raise ValueError("Declared upper equity bound cannot execute the reference")
    checks=[];lo=0;hi=maximum_cents
    while lo<hi:
        mid=(lo+hi)//2;r=run_enterprise(*reference_inputs(entrant_cash=100_000,extra_equity=mid));ok=qualifies(r)
        checks.append({"extra_equity_cents":mid,"executes_reference":ok})
        if ok:hi=mid
        else:lo=mid+1
    at=run_enterprise(*reference_inputs(entrant_cash=100_000,extra_equity=lo))
    below=run_enterprise(*reference_inputs(entrant_cash=100_000,extra_equity=lo-1)) if lo else None
    assert qualifies(at) and (below is None or not qualifies(below))
    return {"schema_version":"fixed-policy-equity-search/0.1","status":"synthetic_conditioned_on_fixed_policy",
            "opening_entrant_cash_cents":100_000,"maximum_extra_equity_cents":maximum_cents,
            "minimum_extra_upfront_equity_cents":lo,"tested_candidates":checks,
            "at_threshold":at,"one_cent_below":below,
            "limits":"Smallest additional month-0 equity in this declared integer-cent interval under the fixed feasible action path and its monotone cash-feasibility condition. Not optimal financing, valuation, or observed capital access."}


def enterprise_source_hashes():
    root=Path(__file__).resolve().parents[1]
    return {p:hashlib.sha256((root/p).read_bytes()).hexdigest() for p in
            ("model/treasury.py","model/monthly_deployment.py","model/monthly_commercial.py","model/monthly_enterprise.py")}


def enterprise_artifact():
    hashes=enterprise_source_hashes()
    cases=enterprise_witnesses();summary=[]
    for name,r in cases.items():
        e=r["enterprise"];outcome=next(b for b in e["business_outcomes"] if b["actor_id"]=="entrant")
        summary.append({"case":name,"total_market_delivered_units":_rational(sum((Fraction(**m["total_delivered_units"]) for m in e["months"]),Fraction())),
            "entrant_delivered_units":outcome["total_delivered_units"],
            "entrant_installed_robots":sum(u["status"]=="installed" and u["operator_id"]=="entrant" for u in r["units"]),
            "entrant_requested_robots":next(o["requested_additions"] for o in r["plan"]["operators"] if o["operator_id"]=="entrant"),
            "entrant_closing_cash_cents":r["months"][-1]["closing_cash_cents"]["entrant"],
            "entrant_first_failed_payment_at":outcome["first_failed_payment_at"],
            "entrant_closing_due_unpaid_cents":outcome["closing_due_unpaid_cents"],
            "equity_received_cents":e["consolidation"]["equity_cash_received_cents"]})
    payload={"schema_version":"shared-enterprise-experiments/0.1","evidence_status":"synthetic_unqualified_terms",
             "source_sha256":hashes,"summary":summary,"case_inputs":witness_input_options(),"cases":cases}
    payload["artifact_hash"]=hashlib.sha256(json.dumps(payload,sort_keys=True,separators=(",",":")).encode()).hexdigest()
    return payload


if __name__=="__main__":
    print(json.dumps(enterprise_artifact(),indent=2))
