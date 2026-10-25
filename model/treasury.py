"""Isolated stage-1 treasury: exact cents, immutable state, explicit settlement.

No physical fleet, revenue recognition, interest accrual or annual-model coupling.
All counterparties require funded accounts. See TREASURY_CORE.md for boundaries.
"""
from __future__ import annotations

from dataclasses import dataclass, replace, asdict
from decimal import Decimal, InvalidOperation
import json


def usd(value: str | Decimal | int) -> int:
    """Convert exact USD to cents; floats, Booleans and fractional cents fail."""
    if isinstance(value,bool) or not isinstance(value,(str,Decimal,int)):
        raise ValueError("Use an exact USD string, Decimal or integer; never float")
    try: amount=Decimal(value)
    except (InvalidOperation,ValueError) as exc: raise ValueError("Invalid money") from exc
    if not amount.is_finite() or amount<0:
        raise ValueError("Money must be finite, nonnegative and exact to cents")
    numerator,denominator=amount.as_integer_ratio()
    cents,remainder=divmod(numerator*100,denominator)
    if remainder:raise ValueError("Fractional cents are not supported")
    return cents


def _money(value,positive=False):
    if type(value) is not int or value<(1 if positive else 0):
        raise ValueError("Money must be integer cents"+(" greater than zero" if positive else " and nonnegative"))
    return value


def _id(value):
    if not isinstance(value,str) or not value.strip():raise ValueError("Identifier/provenance must be a nonempty string")
    return value


def _strings(values):
    if not isinstance(values,(tuple,list)):raise ValueError("Expected a list/tuple of strings")
    result=tuple(values)
    for value in result:_id(value)
    return result


@dataclass(frozen=True,order=True)
class Moment:
    month: int
    phase: int
    def __post_init__(self):
        if type(self.month) is not int or self.month<0 or type(self.phase) is not int or not 1<=self.phase<=7:
            raise ValueError("Moment requires nonnegative integer month and phase 1..7")


@dataclass(frozen=True)
class Account:
    actor_id: str
    opening_cash_cents: int
    minimum_cash_cents: int=0
    currency: str="USD"
    roles: tuple[str,...]=()
    def __post_init__(self):
        _id(self.actor_id);_money(self.opening_cash_cents);_money(self.minimum_cash_cents)
        if self.minimum_cash_cents>self.opening_cash_cents:raise ValueError("Opening cash cannot fund minimum reserve")
        if not isinstance(self.currency,str) or len(self.currency)!=3 or not self.currency.isalpha() or not self.currency.isupper():raise ValueError("Currency must be a three-letter uppercase code")
        object.__setattr__(self,"roles",_strings(self.roles))


@dataclass(frozen=True)
class Posting:
    actor_id: str
    delta_cents: int
    def __post_init__(self):
        _id(self.actor_id)
        if type(self.delta_cents) is not int:raise ValueError("Postings require exact signed cents")


@dataclass(frozen=True)
class Event:
    event_id: str
    at: Moment
    kind: str
    status: str
    reference_id: str
    requested_cents: int
    settled_cents: int
    provenance: str
    reason: str=""
    postings: tuple[Posting,...]=()
    reservation_uses: tuple[tuple[str,int],...]=()
    def __post_init__(self):
        for value in (self.event_id,self.kind,self.status,self.reference_id,self.provenance):_id(value)
        _money(self.requested_cents);_money(self.settled_cents)
        if not isinstance(self.at,Moment):raise ValueError("Event needs a Moment")
        object.__setattr__(self,"postings",tuple(self.postings))
        object.__setattr__(self,"reservation_uses",tuple(tuple(x) for x in self.reservation_uses))
        if any(not isinstance(x,Posting) for x in self.postings):raise ValueError("Invalid posting")
        for rid,amount in self.reservation_uses:_id(rid);_money(amount,True)
        if not isinstance(self.reason,str):raise ValueError("Reason must be text")


@dataclass(frozen=True)
class Invoice:
    invoice_id: str
    payer: str
    payee: str
    face_cents: int
    issued_at: Moment
    eligible_at: Moment
    due_at: Moment
    policy: str="full_or_nothing"
    cancellable: bool=False
    grace_months: int=0
    category: str="operating"
    paid_cents: int=0
    cancelled_cents: int=0
    def __post_init__(self):
        for value in (self.invoice_id,self.payer,self.payee,self.category):_id(value)
        _money(self.face_cents,True);_money(self.paid_cents);_money(self.cancelled_cents)
        if self.payer==self.payee or self.paid_cents+self.cancelled_cents>self.face_cents:raise ValueError("Invalid invoice parties/balance")
        if not all(isinstance(x,Moment) for x in (self.issued_at,self.eligible_at,self.due_at)) or not self.issued_at<self.eligible_at<=self.due_at:raise ValueError("Invalid invoice dates")
        if self.policy not in ("full_or_nothing","partial_allowed") or type(self.cancellable) is not bool or type(self.grace_months) is not int or self.grace_months<0:raise ValueError("Invalid invoice terms")
    @property
    def outstanding_cents(self):return self.face_cents-self.paid_cents-self.cancelled_cents


@dataclass(frozen=True)
class Reservation:
    reservation_id: str
    invoice_id: str
    actor_id: str
    original_cents: int
    remaining_cents: int
    def __post_init__(self):
        for value in (self.reservation_id,self.invoice_id,self.actor_id):_id(value)
        _money(self.original_cents,True);_money(self.remaining_cents)
        if self.remaining_cents>self.original_cents:raise ValueError("Reservation exceeds original amount")


@dataclass(frozen=True)
class Deposit:
    deposit_id: str
    payer: str
    payee: str
    face_cents: int
    placed_at: Moment
    refund_eligible_at: Moment
    restricted: bool=True
    refunded_cents: int=0
    def __post_init__(self):
        for value in (self.deposit_id,self.payer,self.payee):_id(value)
        _money(self.face_cents,True);_money(self.refunded_cents)
        if self.payer==self.payee or self.refunded_cents>self.face_cents or type(self.restricted) is not bool:raise ValueError("Invalid deposit parties/terms")
        if not isinstance(self.placed_at,Moment) or not isinstance(self.refund_eligible_at,Moment) or not self.placed_at<self.refund_eligible_at:raise ValueError("Invalid deposit dates")
    @property
    def outstanding_cents(self):return self.face_cents-self.refunded_cents


@dataclass(frozen=True)
class Credit:
    credit_id: str
    lender: str
    borrower: str
    limit_cents: int
    authorized_at: Moment
    available_from: Moment
    available_until: Moment
    maturity: Moment
    revolving: bool=False
    purposes: tuple[str,...]=("working_capital",)
    drawn_cents: int=0
    repaid_cents: int=0
    def __post_init__(self):
        for value in (self.credit_id,self.lender,self.borrower):_id(value)
        _money(self.limit_cents,True);_money(self.drawn_cents);_money(self.repaid_cents)
        object.__setattr__(self,"purposes",_strings(self.purposes))
        if self.lender==self.borrower or type(self.revolving) is not bool or not self.purposes:raise ValueError("Invalid credit parties/terms")
        if not all(isinstance(x,Moment) for x in (self.authorized_at,self.available_from,self.available_until,self.maturity)) or not self.authorized_at<self.available_from<=self.available_until<self.maturity:raise ValueError("Invalid credit dates")
        if self.outstanding_cents<0 or self.undrawn_cents<0:raise ValueError("Invalid credit balance")
    @property
    def outstanding_cents(self):return self.drawn_cents-self.repaid_cents
    @property
    def undrawn_cents(self):return self.limit_cents-(self.outstanding_cents if self.revolving else self.drawn_cents)


def _replace_item(items,key,value):
    return tuple(value if getattr(x,key)==getattr(value,key) else x for x in items)


@dataclass(frozen=True)
class Treasury:
    accounts: tuple[Account,...]
    invoices: tuple[Invoice,...]=()
    reservations: tuple[Reservation,...]=()
    deposits: tuple[Deposit,...]=()
    credits: tuple[Credit,...]=()
    events: tuple[Event,...]=()
    def __post_init__(self):
        for name,kind in (("accounts",Account),("invoices",Invoice),("reservations",Reservation),("deposits",Deposit),("credits",Credit),("events",Event)):
            object.__setattr__(self,name,tuple(getattr(self,name)))
            if any(not isinstance(x,kind) for x in getattr(self,name)):raise ValueError("Unexpected record type: "+name)
        self.audit()

    def _get(self,items,key,value):
        found=next((x for x in items if getattr(x,key)==value),None)
        if found is None:raise ValueError(f"Unknown {key}: {value}")
        return found
    def account(self,actor):return self._get(self.accounts,"actor_id",actor)
    def invoice(self,iid):return self._get(self.invoices,"invoice_id",iid)
    def credit(self,cid):return self._get(self.credits,"credit_id",cid)
    def deposit(self,did):return self._get(self.deposits,"deposit_id",did)
    def balance(self,actor):
        return self.account(actor).opening_cash_cents+sum(p.delta_cents for e in self.events for p in e.postings if p.actor_id==actor)
    def restricted(self,actor):
        self.account(actor)
        return sum(d.outstanding_cents for d in self.deposits if d.payee==actor and d.restricted)
    def reserved(self,actor):
        self.account(actor)
        return sum(r.remaining_cents for r in self.reservations if r.actor_id==actor)
    def available(self,actor):
        return self.balance(actor)-self.restricted(actor)-self.reserved(actor)-self.account(actor).minimum_cash_cents

    def _actors(self,payer,payee):
        self.account(payer);self.account(payee)
        if payer==payee:raise ValueError("One legal actor cannot pay or lend to itself")

    def _event_check(self,event_id,at,provenance):
        _id(event_id);_id(provenance)
        if not isinstance(at,Moment):raise ValueError("Explicit Moment required")
        if any(e.event_id==event_id for e in self.events):raise ValueError("Duplicate event ID")
        if self.events and at<self.events[-1].at:raise ValueError("Cannot backdate an event")

    def _commit(self,event_id,at,kind,reference_id,requested,provenance,*,settled=0,payer=None,payee=None,status="completed",reason="",uses=(),**changes):
        self._event_check(event_id,at,provenance)
        postings=() if not settled else (Posting(payer,-settled),Posting(payee,settled))
        event=Event(event_id,at,kind,status,reference_id,requested,settled,provenance,reason,postings,uses)
        return replace(self,events=self.events+(event,),**changes)

    def issue_invoice(self,event_id,invoice_id,payer,payee,amount_cents,at,eligible_at,due_at,*,provenance,policy="full_or_nothing",cancellable=False,grace_months=0,category="operating"):
        self._actors(payer,payee);_money(amount_cents,True);_id(invoice_id);_id(category)
        if any(i.invoice_id==invoice_id for i in self.invoices):raise ValueError("Duplicate invoice ID")
        if not all(isinstance(x,Moment) for x in (at,eligible_at,due_at)) or not at<eligible_at<=due_at:raise ValueError("Require issue < earliest settlement <= due Moment")
        if policy not in ("full_or_nothing","partial_allowed") or type(cancellable) is not bool or type(grace_months) is not int or grace_months<0:raise ValueError("Invalid invoice terms")
        item=Invoice(invoice_id,payer,payee,amount_cents,at,eligible_at,due_at,policy,cancellable,grace_months,category)
        return self._commit(event_id,at,"invoice_issue",invoice_id,amount_cents,provenance,invoices=self.invoices+(item,))

    def reserve_invoice(self,event_id,reservation_id,invoice_id,amount_cents,at,*,provenance):
        item=self.invoice(invoice_id);_money(amount_cents,True);_id(reservation_id)
        if any(r.reservation_id==reservation_id for r in self.reservations):raise ValueError("Duplicate reservation ID")
        allocated=sum(r.remaining_cents for r in self.reservations if r.invoice_id==invoice_id)
        if amount_cents+allocated>item.outstanding_cents:raise ValueError("Reservation exceeds outstanding invoice")
        if amount_cents>self.available(item.payer):
            return self._commit(event_id,at,"reservation_create",reservation_id,amount_cents,provenance,status="blocked",reason="insufficient_unencumbered_cash")
        r=Reservation(reservation_id,invoice_id,item.payer,amount_cents,amount_cents)
        return self._commit(event_id,at,"reservation_create",reservation_id,amount_cents,provenance,reservations=self.reservations+(r,))

    def release_reservation(self,event_id,reservation_id,at,*,provenance):
        r=self._get(self.reservations,"reservation_id",reservation_id)
        if r.remaining_cents==0:raise ValueError("Reservation already consumed/released")
        changed=replace(r,remaining_cents=0)
        return self._commit(event_id,at,"reservation_release",reservation_id,r.remaining_cents,provenance,reservations=_replace_item(self.reservations,"reservation_id",changed))

    def settle_invoice(self,event_id,invoice_id,at,*,provenance,amount_cents=None):
        item=self.invoice(invoice_id)
        requested=item.outstanding_cents if amount_cents is None else _money(amount_cents,True)
        if requested<=0 or requested>item.outstanding_cents:raise ValueError("Invoice already closed or overpayment requested")
        if item.policy=="full_or_nothing" and requested!=item.outstanding_cents:raise ValueError("Full-or-nothing policy requires the full outstanding amount")
        self._event_check(event_id,at,provenance)
        if at<item.eligible_at:
            return self._commit(event_id,at,"invoice_payment",invoice_id,requested,provenance,status="blocked",reason="not_yet_eligible")
        own=sum(r.remaining_cents for r in self.reservations if r.invoice_id==invoice_id)
        payable=min(requested,self.available(item.payer)+own)
        if payable<requested and item.policy=="full_or_nothing":payable=0
        if payable==0:
            return self._commit(event_id,at,"invoice_payment",invoice_id,requested,provenance,status="blocked",reason="insufficient_unencumbered_cash")
        left,updated,uses=payable,[],[]
        for r in self.reservations:
            take=min(left,r.remaining_cents) if r.invoice_id==invoice_id else 0
            if take:uses.append((r.reservation_id,take));left-=take
            updated.append(replace(r,remaining_cents=r.remaining_cents-take))
        return self._commit(event_id,at,"invoice_payment",invoice_id,requested,provenance,settled=payable,payer=item.payer,payee=item.payee,
            status="settled" if payable==item.outstanding_cents else "partial",uses=tuple(uses),reservations=tuple(updated),
            invoices=_replace_item(self.invoices,"invoice_id",replace(item,paid_cents=item.paid_cents+payable)))

    def cancel_invoice(self,event_id,invoice_id,at,*,provenance):
        item=self.invoice(invoice_id)
        if not item.cancellable or item.outstanding_cents<=0:raise ValueError("Invoice cannot be cancelled")
        releases=tuple((r.reservation_id,r.remaining_cents) for r in self.reservations if r.invoice_id==invoice_id and r.remaining_cents)
        reservations=tuple(replace(r,remaining_cents=0) if r.invoice_id==invoice_id else r for r in self.reservations)
        return self._commit(event_id,at,"invoice_cancel",invoice_id,item.outstanding_cents,provenance,uses=releases,reservations=reservations,
            invoices=_replace_item(self.invoices,"invoice_id",replace(item,cancelled_cents=item.cancelled_cents+item.outstanding_cents)))

    def invoice_status(self,invoice_id,at=None):
        item=self.invoice(invoice_id)
        current=self.events[-1].at if self.events else item.issued_at
        at=current if at is None else at
        if not isinstance(at,Moment) or at<current:raise ValueError("Query current/future status; retain a prior state for historical queries")
        if item.outstanding_cents==0:return "cancelled" if item.cancelled_cents else "paid"
        if at<item.eligible_at:return "not_yet_payable"
        if at<item.due_at:return "payable_not_due"
        deadline=Moment(item.due_at.month+item.grace_months,item.due_at.phase)
        attempted=any(e.kind=="invoice_payment" and e.reference_id==invoice_id and e.status in ("blocked","partial") and deadline<=e.at<=at for e in self.events)
        return "defaulted" if at>deadline or attempted else "due"

    def place_deposit(self,event_id,deposit_id,payer,payee,amount_cents,at,refund_eligible_at,*,provenance,restricted=True):
        self._actors(payer,payee);_money(amount_cents,True);_id(deposit_id)
        if any(d.deposit_id==deposit_id for d in self.deposits):raise ValueError("Duplicate deposit ID")
        if not isinstance(at,Moment) or not isinstance(refund_eligible_at,Moment) or refund_eligible_at<=at or type(restricted) is not bool:raise ValueError("Invalid deposit dates/restriction")
        if amount_cents>self.available(payer):return self._commit(event_id,at,"deposit_place",deposit_id,amount_cents,provenance,status="blocked",reason="insufficient_unencumbered_cash")
        item=Deposit(deposit_id,payer,payee,amount_cents,at,refund_eligible_at,restricted)
        return self._commit(event_id,at,"deposit_place",deposit_id,amount_cents,provenance,settled=amount_cents,payer=payer,payee=payee,status="settled",deposits=self.deposits+(item,))

    def refund_deposit(self,event_id,deposit_id,at,*,provenance,amount_cents=None):
        item=self.deposit(deposit_id)
        amount=item.outstanding_cents if amount_cents is None else _money(amount_cents,True)
        if amount<=0 or amount>item.outstanding_cents:raise ValueError("Deposit already refunded or refund too large")
        self._event_check(event_id,at,provenance)
        available=self.available(item.payee)+(item.outstanding_cents if item.restricted else 0)
        reason="not_yet_eligible" if at<item.refund_eligible_at else "insufficient_unencumbered_cash" if amount>available else ""
        if reason:return self._commit(event_id,at,"deposit_refund",deposit_id,amount,provenance,status="blocked",reason=reason)
        return self._commit(event_id,at,"deposit_refund",deposit_id,amount,provenance,settled=amount,payer=item.payee,payee=item.payer,status="settled",
            deposits=_replace_item(self.deposits,"deposit_id",replace(item,refunded_cents=item.refunded_cents+amount)))

    def authorize_credit(self,event_id,credit_id,lender,borrower,limit_cents,at,available_from,available_until,maturity,*,provenance,revolving=False,purposes=("working_capital",)):
        self._actors(lender,borrower);_money(limit_cents,True);_id(credit_id)
        if any(c.credit_id==credit_id for c in self.credits):raise ValueError("Duplicate credit ID")
        if not all(isinstance(x,Moment) for x in (at,available_from,available_until,maturity)) or not at<available_from<=available_until<maturity:raise ValueError("Invalid credit availability/maturity sequence")
        purposes=_strings(purposes)
        if type(revolving) is not bool or not purposes:raise ValueError("Invalid credit terms")
        for p in purposes:_id(p)
        item=Credit(credit_id,lender,borrower,limit_cents,at,available_from,available_until,maturity,revolving,purposes)
        return self._commit(event_id,at,"credit_authorize",credit_id,limit_cents,provenance,credits=self.credits+(item,))

    def draw_credit(self,event_id,credit_id,amount_cents,at,*,provenance,purpose="working_capital"):
        item=self.credit(credit_id);_money(amount_cents,True);self._event_check(event_id,at,provenance)
        if purpose not in item.purposes:raise ValueError("Draw purpose not authorized by facility")
        reason="outside_draw_window" if not item.available_from<=at<=item.available_until else "commitment_exhausted" if amount_cents>item.undrawn_cents else "lender_cash_insufficient" if amount_cents>self.available(item.lender) else ""
        if reason:return self._commit(event_id,at,"credit_draw",credit_id,amount_cents,provenance,status="blocked",reason=reason)
        return self._commit(event_id,at,"credit_draw",credit_id,amount_cents,provenance,settled=amount_cents,payer=item.lender,payee=item.borrower,status="settled",
            credits=_replace_item(self.credits,"credit_id",replace(item,drawn_cents=item.drawn_cents+amount_cents)))

    def repay_principal(self,event_id,credit_id,amount_cents,at,*,provenance,policy="full_or_nothing"):
        item=self.credit(credit_id);_money(amount_cents,True);self._event_check(event_id,at,provenance)
        if policy not in ("full_or_nothing","partial_allowed") or amount_cents>item.outstanding_cents:raise ValueError("Invalid repayment or repayment exceeds outstanding principal")
        payable=min(amount_cents,self.available(item.borrower))
        if payable<amount_cents and policy=="full_or_nothing":payable=0
        if payable==0:return self._commit(event_id,at,"principal_repay",credit_id,amount_cents,provenance,status="blocked",reason="borrower_cash_insufficient")
        return self._commit(event_id,at,"principal_repay",credit_id,amount_cents,provenance,settled=payable,payer=item.borrower,payee=item.lender,status="settled" if payable==amount_cents else "partial",
            credits=_replace_item(self.credits,"credit_id",replace(item,repaid_cents=item.repaid_cents+payable)))

    def audit(self):
        """Raise on conservation, replay, encumbrance or obligation inconsistency."""
        if not self.accounts:raise ValueError("At least one funded/zero-cash actor account is required")
        for items,key in ((self.accounts,"actor_id"),(self.invoices,"invoice_id"),(self.reservations,"reservation_id"),(self.deposits,"deposit_id"),(self.credits,"credit_id"),(self.events,"event_id")):
            ids=[getattr(x,key) for x in items]
            if len(ids)!=len(set(ids)):raise ValueError("Duplicate "+key)
        if len({a.currency for a in self.accounts})!=1:raise ValueError("Mixed currencies require an unimplemented FX model")
        last=Moment(0,1)
        for e in self.events:
            if e.at<last:raise ValueError("Nonmonotone event log")
            last=e.at
            if sum(p.delta_cents for p in e.postings)!=0:raise ValueError("Unbalanced cash event")
            if sum(max(0,p.delta_cents) for p in e.postings)!=e.settled_cents:raise ValueError("Settlement/posting disagreement")
            for p in e.postings:self.account(p.actor_id)
        if sum(self.balance(a.actor_id) for a in self.accounts)!=sum(a.opening_cash_cents for a in self.accounts):raise ValueError("Cash not conserved")
        for a in self.accounts:
            if self.balance(a.actor_id)<0 or self.available(a.actor_id)<0:raise ValueError("Negative cash or overlapping/unfunded encumbrance")
        for i in self.invoices:
            self._actors(i.payer,i.payee);_money(i.face_cents,True);_money(i.paid_cents);_money(i.cancelled_cents)
            paid=sum(e.settled_cents for e in self.events if e.kind=="invoice_payment" and e.reference_id==i.invoice_id)
            cancelled=sum(e.requested_cents for e in self.events if e.kind=="invoice_cancel" and e.reference_id==i.invoice_id)
            reserved=sum(r.remaining_cents for r in self.reservations if r.invoice_id==i.invoice_id)
            if i.paid_cents!=paid or i.cancelled_cents!=cancelled or i.outstanding_cents<reserved:raise ValueError("Invoice replay/reservation inconsistency")
        for r in self.reservations:
            invoice=self.invoice(r.invoice_id);_money(r.original_cents,True);_money(r.remaining_cents)
            consumed=sum(n for e in self.events for rid,n in e.reservation_uses if rid==r.reservation_id)
            released=sum(e.requested_cents for e in self.events if e.kind=="reservation_release" and e.reference_id==r.reservation_id)
            if r.actor_id!=invoice.payer or r.remaining_cents!=r.original_cents-consumed-released:raise ValueError("Reservation replay inconsistency")
        for d in self.deposits:
            self._actors(d.payer,d.payee);_money(d.face_cents,True);_money(d.refunded_cents)
            placed=sum(e.settled_cents for e in self.events if e.kind=="deposit_place" and e.reference_id==d.deposit_id)
            refunded=sum(e.settled_cents for e in self.events if e.kind=="deposit_refund" and e.reference_id==d.deposit_id)
            if d.face_cents!=placed or d.refunded_cents!=refunded or d.outstanding_cents<0:raise ValueError("Deposit replay inconsistency")
        for c in self.credits:
            self._actors(c.lender,c.borrower);_money(c.limit_cents,True);_money(c.drawn_cents);_money(c.repaid_cents)
            drawn=sum(e.settled_cents for e in self.events if e.kind=="credit_draw" and e.reference_id==c.credit_id)
            repaid=sum(e.settled_cents for e in self.events if e.kind=="principal_repay" and e.reference_id==c.credit_id)
            if c.drawn_cents!=drawn or c.repaid_cents!=repaid or c.outstanding_cents<0 or c.undrawn_cents<0:raise ValueError("Credit replay/commitment inconsistency")
        return True

    def snapshot(self):
        return {"schema_version":"treasury-core/0.1","scope":"synthetic_stage_1_financial_core_only","currency":self.accounts[0].currency,
            "actors":[{"actor_id":a.actor_id,"opening_cash_cents":a.opening_cash_cents,"cash_cents":self.balance(a.actor_id),
                "restricted_cents":self.restricted(a.actor_id),"reserved_cents":self.reserved(a.actor_id),"minimum_cash_cents":a.minimum_cash_cents,
                "available_cents":self.available(a.actor_id)} for a in self.accounts],
            "invoices":[{**asdict(i),"outstanding_cents":i.outstanding_cents,"status":self.invoice_status(i.invoice_id)} for i in self.invoices],
            "deposits":[{**asdict(d),"outstanding_cents":d.outstanding_cents} for d in self.deposits],
            "credits":[{**asdict(c),"outstanding_cents":c.outstanding_cents,"undrawn_cents":c.undrawn_cents} for c in self.credits],
            "reservations":[asdict(r) for r in self.reservations],"events":[asdict(e) for e in self.events]}


def financial_witnesses():
    """Deterministic financial parts of design witnesses 1, 2, 3, 5 and 7."""
    p={"provenance":"synthetic_treasury_design_witness"};a=Moment(0,1);b=Moment(0,2);c=Moment(0,3)
    base=Treasury((Account("provider",usd("50000"),usd("10000")),Account("payroll",0),Account("supplier",0),Account("buyer",usd("60000")),Account("lender",usd("20000"))))
    for iid,payer,payee,amount,eligible,due in (("payroll","provider","payroll","20000",b,c),("start","provider","supplier","40000",b,c),("sale","buyer","provider","60000",Moment(1,2),Moment(1,3))):
        base=base.issue_invoice("issue-"+iid,iid,payer,payee,usd(amount),a,eligible,due,**p)
    base=base.authorize_credit("commit","loan","lender","provider",usd("20000"),a,b,Moment(1,2),Moment(2,3),**p)
    unfunded=base.settle_invoice("pay-payroll","payroll",c,**p).settle_invoice("blocked-start","start",c,**p)
    funded=base.draw_credit("draw","loan",usd("20000"),b,**p).settle_invoice("pay-payroll","payroll",c,**p).settle_invoice("pay-start","start",c,**p)
    funded=funded.settle_invoice("collect-sale","sale",Moment(1,2),**p).repay_principal("principal","loan",usd("20000"),Moment(1,3),**p)
    yield_case=Treasury((Account("provider",usd("100000")),Account("supplier",0),Account("buyer",usd("60000"))))
    for iid,payer,payee,amount,eligible in (("start-1","provider","supplier","36000",b),("start-2","provider","supplier","36000",b),("one-accepted-sale","buyer","provider","60000",Moment(1,2))):
        yield_case=yield_case.issue_invoice("issue-"+iid,iid,payer,payee,usd(amount),a,eligible,eligible,**p)
    yield_case=yield_case.settle_invoice("cash-start-1","start-1",b,**p).settle_invoice("cash-start-2","start-2",b,**p).settle_invoice("collect","one-accepted-sale",Moment(1,2),**p)
    deposit_case=Treasury((Account("provider",usd("30000")),Account("customer",usd("30000")),Account("supplier",0)))
    deposit_case=deposit_case.issue_invoice("issue-start","start","provider","supplier",usd("40000"),a,b,c,cancellable=True,**p)
    deposit_case=deposit_case.place_deposit("place","deposit","customer","provider",usd("20000"),b,Moment(1,2),**p)
    deposit_case=deposit_case.settle_invoice("blocked-start","start",c,**p).cancel_invoice("cancel-start","start",Moment(1,1),**p).refund_deposit("refund","deposit",Moment(1,2),**p)
    default_case=Treasury((Account("entrant",usd("8000")),Account("financier",0)))
    default_case=default_case.issue_invoice("issue-fee","availability","entrant","financier",usd("10000"),a,b,c,**p).settle_invoice("blocked-fee","availability",c,**p)
    earmark=Treasury((Account("payer",usd("100000")),Account("payee",0)))
    for iid,amount in (("A","100000"),("B","1000")):
        earmark=earmark.issue_invoice("issue-"+iid,iid,"payer","payee",usd(amount),a,b,c,**p)
    earmark=earmark.reserve_invoice("reserve","A-reserve","A",usd("100000"),b,**p)
    earmark=earmark.settle_invoice("block-B","B",c,**p).settle_invoice("pay-A","A",c,**p)
    return {"witness_1_unfunded":unfunded.snapshot(),"witness_1_funded_next_month":funded.snapshot(),"witness_2_start_costs_once":yield_case.snapshot(),
            "witness_3_restricted_deposit_refunded":deposit_case.snapshot(),"witness_5_unpaid_fee":default_case.snapshot(),"witness_7_earmark_consumed":earmark.snapshot()}


if __name__=="__main__":print(json.dumps(financial_witnesses(),indent=2,sort_keys=True,allow_nan=False))
