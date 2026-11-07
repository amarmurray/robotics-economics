"""Dated synthetic financing policies on the existing monthly enterprise loop.

No market financing offer or insolvency-law model. Principal uses Treasury credit,
interest uses invoices, and no collateral or residual asset is sold implicitly.
"""
from __future__ import annotations

from dataclasses import asdict, dataclass, replace
from fractions import Fraction
import hashlib
import json
from pathlib import Path

from model.monthly_commercial import restore_opening_inputs
from model.monthly_deployment import _integer, _name, _rational, run_monthly, Start
from model.monthly_enterprise import (
    _Enterprise, Business, CustomerMove, EnterprisePlan, Equity, Market,
    enterprise_source_hashes, reference_inputs, round_cents, shared_case_inputs,
)
from model.treasury import Account, Moment


@dataclass(frozen=True)
class TermLoan:
    loan_id: str
    lender: str
    borrower: str
    principal_cents: int
    draw_month: int
    maturity_month: int
    monthly_rate_numerator: int = 1
    monthly_rate_denominator: int = 100
    repayment_policy: str = "partial_allowed"

    def __post_init__(self):
        for value in (self.loan_id, self.lender, self.borrower): _name(value)
        _integer(self.principal_cents, 1)
        _integer(self.draw_month); _integer(self.maturity_month)
        _integer(self.monthly_rate_numerator); _integer(self.monthly_rate_denominator, 1)
        if self.borrower == self.lender or self.maturity_month <= self.draw_month:
            raise ValueError("Loan needs distinct actors and maturity after its draw month")
        if self.repayment_policy not in ("partial_allowed", "full_or_nothing"):
            raise ValueError("Explicit principal repayment policy required")


@dataclass(frozen=True)
class FinancePlan:
    loans: tuple[TermLoan, ...] = ()
    payment_priority: str = "operations_then_debt"
    default_policy: str = "suspend_until_cured"
    reinvestment_reserve_cents: int = 0

    def __post_init__(self):
        if not isinstance(self.loans, (list, tuple)) or any(not isinstance(x, TermLoan) for x in self.loans):
            raise ValueError("Explicit loan records required")
        object.__setattr__(self, "loans", tuple(self.loans))
        if len({x.loan_id for x in self.loans}) != len(self.loans):
            raise ValueError("Duplicate loan ID")
        if self.payment_priority not in ("operations_then_debt", "debt_then_operations"):
            raise ValueError("Unknown payment priority")
        if self.default_policy not in ("suspend_until_cured", "stop_permanently"):
            raise ValueError("Unknown default policy")
        _integer(self.reinvestment_reserve_cents)


class _FinancedEnterprise(_Enterprise):
    def __init__(self, plan, contracts, treasury, enterprise, finance):
        super().__init__(plan, contracts, treasury, enterprise)
        if not isinstance(finance, FinancePlan): raise ValueError("Finance plan required")
        if treasury.credits:
            raise ValueError("Opening credits need explicit servicing terms; not supported by this new-loan policy")
        outsiders = {enterprise.market.buyer_actor, enterprise.enterprise_vendor_actor,
                     plan.manufacturing_vendor_actor, plan.deployment_vendor_actor}
        for loan in finance.loans:
            treasury.account(loan.lender); treasury.account(loan.borrower)
            if loan.borrower not in self.parties or loan.lender in set(self.parties) | outsiders:
                raise ValueError("Loan must fund an included actor from a distinct outside capital provider")
            if loan.draw_month >= plan.months: raise ValueError("Loan draw outside execution horizon")
        self.finance = finance
        self.interest_ids = set()
        self.loan_interest_ids = {loan.loan_id:set() for loan in finance.loans}
        self.finance_events = []
        self.finance_months = []
        self.defaulted = set()
        self.ever_defaulted = set()
        self.first_default = {}
        self.interest_lines = []

    def credit_id(self, loan): return self._id("term-loan", loan.loan_id)

    def finance_event(self, month, phase, action, **detail):
        self.finance_events.append({"event_id":self._id("finance-event", len(self.finance_events)+1),
                                    "at":asdict(Moment(month, phase)), "action":action, **detail})

    def prepare(self, t, month, units):
        t = super().prepare(t, month, units)
        for loan in sorted(self.finance.loans, key=lambda x:x.loan_id):
            cid = self.credit_id(loan)
            if month == 0:
                t = t.authorize_credit(cid+":authorize", cid, loan.lender, loan.borrower,
                    loan.principal_cents, Moment(0,1), Moment(loan.draw_month,2),
                    Moment(loan.draw_month,2), Moment(loan.maturity_month,3),
                    provenance=self.provenance, purposes=("working_capital",))
            # Arrears interest: one exact monthly charge on opening principal.
            # A phase-2 draw first earns interest in the following month.
            principal = t.credit(cid).outstanding_cents
            exact = Fraction(principal * loan.monthly_rate_numerator, loan.monthly_rate_denominator)
            charge = round_cents(exact)
            iid = self._id("interest", loan.loan_id, month)
            if charge:
                t = t.issue_invoice(iid+":issue", iid, loan.borrower, loan.lender, charge,
                    Moment(month,1), Moment(month,3), Moment(month,3),
                    provenance=self.provenance, category="loan_interest", policy="partial_allowed")
                self.interest_ids.add(iid)
                self.loan_interest_ids[loan.loan_id].add(iid)
            self.interest_lines.append({"loan_id":loan.loan_id, "month":month,
                "opening_principal_cents":principal, "rate_numerator":loan.monthly_rate_numerator,
                "rate_denominator":loan.monthly_rate_denominator, "exact_interest_cents":_rational(exact),
                "rounded_interest_cents":charge, "invoice_id":iid if charge else None})
        return t

    def collect(self, t, month):
        t = super().collect(t, month)
        for loan in sorted(self.finance.loans, key=lambda x:x.loan_id):
            if month != loan.draw_month: continue
            cid = self.credit_id(loan)
            t = t.draw_credit(cid+":draw", cid, loan.principal_cents, Moment(month,2),
                              provenance=self.provenance)
            e = t.events[-1]
            self.finance_event(month,2,"scheduled_draw",loan_id=loan.loan_id,
                               status=e.status,reason=e.reason,settled_cents=e.settled_cents)
        return t

    def service_debt(self, t, month):
        t = self.collect_set(t, month, 3, self.interest_ids)
        # Older interest before principal; loans then have explicit loan-ID order.
        for loan in sorted(self.finance.loans, key=lambda x:x.loan_id):
            cid = self.credit_id(loan); principal = t.credit(cid).outstanding_cents
            interest_due = any(i.invoice_id in self.interest_ids and i.payer == loan.borrower
                and i.outstanding_cents and i.due_at <= Moment(month,3) for i in t.invoices)
            if month >= loan.maturity_month and principal and not interest_due:
                t = t.repay_principal(cid+f":repay:{month}", cid, principal, Moment(month,3),
                    provenance=self.provenance, policy=loan.repayment_policy)
                e = t.events[-1]
                self.finance_event(month,3,"matured_principal_recovery",loan_id=loan.loan_id,
                    status=e.status,reason=e.reason,requested_cents=principal,settled_cents=e.settled_cents)
        return t

    def mandatory(self, t, month):
        t = self.refunds(t, month)
        # Same operating invoice scheduler as the shared case, excluding interest
        # so the declared policy controls relative priority. Physical prepaid
        # support, commissioning and new starts occur after this phase.
        actors = {b.actor_id for b in self.enterprise.businesses}
        due = {i.invoice_id for i in t.invoices if i.payer in actors
               and not i.cancellable and i.invoice_id not in self.interest_ids}
        if self.finance.payment_priority == "debt_then_operations":
            t = self.service_debt(t, month)
        t = self.collect_set(t, month, 3, due)
        if self.finance.payment_priority == "operations_then_debt":
            t = self.service_debt(t, month)
        now_defaulted = set()
        for loan in self.finance.loans:
            overdue = t.credit(self.credit_id(loan)).outstanding_cents if month >= loan.maturity_month else 0
            interest = sum(i.outstanding_cents for i in t.invoices if i.invoice_id in self.interest_ids
                           and i.payer == loan.borrower and i.due_at <= Moment(month,3))
            if overdue or interest: now_defaulted.add(loan.borrower)
        for actor in sorted(now_defaulted - self.defaulted):
            self.first_default.setdefault(actor, month)
            self.finance_event(month,3,"debt_default",actor_id=actor,policy=self.finance.default_policy)
        for actor in sorted(self.defaulted - now_defaulted):
            self.finance_event(month,3,"debt_cured",actor_id=actor,
                operational_restart_permitted=self.finance.default_policy == "suspend_until_cured")
        self.defaulted = now_defaulted
        self.ever_defaulted.update(now_defaulted)
        self.current_treasury = t
        return t

    def halted(self, actor):
        return actor in (self.ever_defaulted if self.finance.default_policy == "stop_permanently" else self.defaulted)

    def ready(self, t, b, month, phase=5):
        return not self.halted(b.actor_id) and super().ready(t, b, month, phase)

    def _reason(self, t, month, phase, action, operator_id):
        if action == "start" and self.halted(self.plan.provider_actor): return "provider_debt_default_policy"
        if action == "ship" and operator_id is not None and self.halted(self._owner(self.by_site[operator_id])):
            return "asset_funder_debt_default_policy"
        return super()._reason(t, month, phase, action, operator_id)

    def admit(self, t, iid, month, phase, physical_reason, unit=None, operator_id=None):
        invoice = t.invoice(iid)
        if self.halted(invoice.payer): physical_reason = physical_reason or "payer_debt_default_policy"
        if invoice.category == "start" and month > 0 and self.finance.reinvestment_reserve_cents:
            cash_after = t.available(invoice.payer) - invoice.outstanding_cents
            if cash_after < self.finance.reinvestment_reserve_cents:
                physical_reason = physical_reason or "reinvestment_cash_reserve"
            self.finance_event(month,phase,"reinvestment_gate",invoice_id=iid,
                available_cash_cents=t.available(invoice.payer),start_invoice_cents=invoice.outstanding_cents,
                required_remaining_cash_cents=self.finance.reinvestment_reserve_cents,
                reserve_gate_passed=cash_after >= self.finance.reinvestment_reserve_cents)
        return super().admit(t,iid,month,phase,physical_reason,unit,operator_id)

    def close(self, t, month, units, supported):
        super().close(t, month, units, supported)
        rows = []
        for loan in self.finance.loans:
            c = t.credit(self.credit_id(loan))
            interest = [i for i in t.invoices if i.invoice_id in self.loan_interest_ids[loan.loan_id]]
            rows.append({"loan_id":loan.loan_id,"borrower":loan.borrower,"lender":loan.lender,
                "drawn_cents":c.drawn_cents,"principal_recovered_cents":c.repaid_cents,
                "principal_outstanding_cents":c.outstanding_cents,
                "principal_due_cents":c.outstanding_cents if month >= loan.maturity_month else 0,
                "interest_accrued_cents":sum(i.face_cents for i in interest),
                "interest_paid_cents":sum(i.paid_cents for i in interest),
                "interest_due_cents":sum(i.outstanding_cents for i in interest),
                "defaulted_now":loan.borrower in self.defaulted,
                "operating_policy_halted":self.halted(loan.borrower)})
        self.finance_months.append({"month":month,"loans":rows,
            "cash_recovery_only":True,"assets_sold_or_repossessed":[],
            "halted_actors":sorted(a for a in self.parties if self.halted(a))})

    def finance_result(self, r):
        ids = {self.credit_id(loan) for loan in self.finance.loans}
        credit = [c for c in r['closing_treasury']['credits'] if c['credit_id'] in ids]
        interest = [i for i in r['closing_treasury']['invoices'] if i['invoice_id'] in self.interest_ids]
        drawn = sum(c['drawn_cents'] for c in credit)
        repaid = sum(c['repaid_cents'] for c in credit)
        paid_interest = sum(i['paid_cents'] for i in interest)
        net_financing = drawn - repaid - paid_interest
        base = r['enterprise']['consolidation']
        result = {"schema_version":"enterprise-finance/0.1","evidence_status":"synthetic_unqualified_contract_terms",
            "inputs":asdict(self.finance),"months":self.finance_months,"events":self.finance_events,
            "interest_lines":self.interest_lines,"first_debt_default_month":self.first_default,
            "metric_lineage":[
                {"metric":"loan draw cash","equation":"sum settled credit_draw events for these facilities",
                 "inputs":"TermLoan principal, draw month, lender available cash","implementation":"Treasury.draw_credit; _FinancedEnterprise.collect","basis":"synthetic contract and opening accounts"},
                {"metric":"monthly interest","equation":"round_half_up(opening principal cents * rate numerator / rate denominator)",
                 "inputs":"interest_lines; draw and repayment journals","implementation":"_FinancedEnterprise.prepare; round_cents","basis":"synthetic monthly convention; not an observed rate"},
                {"metric":"closing principal claim","equation":"actual draws - actual principal repayments",
                 "inputs":"closing_treasury.credits and matching settled events","implementation":"Treasury.audit; _FinancedEnterprise.finance_result","basis":"cash/claim identity; no write-off or collateral sale"},
                {"metric":"default and cure","equation":"after phase-3 payments: due interest > 0 OR matured principal > 0; cure requires both zero",
                 "inputs":"maturity month, payment priority, available funds, default policy","implementation":"_FinancedEnterprise.mandatory; ready","basis":"declared synthetic operating policy, not law or market credit terms"},
                {"metric":"accepted delivered service","equation":"robot service + human service, capped by one assigned demand ledger and actual paid capacity",
                 "inputs":"enterprise.months operators and pools; supported physical unit IDs","implementation":"_Enterprise.dispatch_output; run_monthly","basis":"synthetic floor-service bundles; no clinical/component/hour conversion"},
                {"metric":"later start reserve gate","equation":"available provider cash - candidate start invoice >= declared reserve; all other physical and funding gates also apply",
                 "inputs":"dated start candidate, Treasury available cash, reserve cents","implementation":"_FinancedEnterprise.admit; _Commercial.admit","basis":"synthetic fixed-policy reinvestment; no optimized order generation"},
                {"metric":"net financing cash","equation":"draw cash - recovered principal - paid interest",
                 "inputs":"settled Treasury credit and interest events","implementation":"_FinancedEnterprise.finance_result","basis":"boundary cash transfer, not profit or physical resource cost"}
            ],
            "consolidation":{"included_actors":self.parties,"outside_capital_providers":sorted({x.lender for x in self.finance.loans}),
                "loan_draw_cash_cents":drawn,"principal_recovery_cash_cents":repaid,
                "interest_cash_cents":paid_interest,"net_financing_cash_cents":net_financing,
                "closing_principal_claim_cents":sum(c['outstanding_cents'] for c in credit),
                "closing_interest_claim_cents":sum(i['outstanding_cents'] for i in interest),
                "unclassified_other_boundary_cash_cents":base['other_boundary_cash_cents']-net_financing,
                "loan_principal_is_revenue":False,"interest_is_physical_resource_cost":False},
            "limits":["One fixed monthly rate on opening principal, rounded half-up to cents; no daily accrual, penalties or interest capitalization",
                "Scheduled one-time draws; lender funding is required; maturity after the horizon remains a visible liability",
                "Default suspends activity until cured or permanently according to explicit policy; no legal priority or insolvency result inferred",
                "Cash recovery uses funded Treasury payments; no sale, repossession, write-off, salvage or automatic contract cancellation",
                "Reinvestment gates declared later start candidates with actual available cash and a reserve; no optimized or autonomous order generation",
                "Annual work-unit/calendar/cohort and intelligence-architecture bridges remain pending"]}
        assert drawn-repaid == result['consolidation']['closing_principal_claim_cents']
        return result


def finance_source_hashes():
    path = Path(__file__).resolve()
    return {**enterprise_source_hashes(),"model/enterprise_finance.py":hashlib.sha256(path.read_bytes()).hexdigest()}


def run_financed_enterprise(plan, treasury, contracts, enterprise, finance):
    policy = _FinancedEnterprise(plan, contracts, treasury, enterprise, finance)
    r = run_monthly(plan, treasury, commercial=policy)
    r.update(schema_version="monthly-deployment/0.4",scope="synthetic_shared_enterprise_with_dated_finance",
             ownership="one_title_owner_per_unit_separate_from_custody_and_workflow")
    r['commercial'] = policy.result(r)
    r['commercial']['limits'] = ["Shared enterprise and finance scopes are defined in enterprise.limits and finance.limits"]
    r['enterprise'] = policy.enterprise_result(r)
    r['enterprise']['limits'] = [x for x in r['enterprise']['limits'] if not x.startswith("No automatic loan draw")]
    r['finance'] = policy.finance_result(r)
    r['source_sha256'] = finance_source_hashes()
    r['case_hash'] = hashlib.sha256(json.dumps(r,sort_keys=True,separators=(',',':')).encode()).hexdigest()
    return json.loads(json.dumps(r))


def replay_financed_enterprise(saved):
    if not isinstance(saved,dict) or saved.get('schema_version') != 'monthly-deployment/0.4':
        raise ValueError("Saved financed-enterprise case required")
    e = dict(saved['enterprise']['inputs']);e['market'] = Market(**e['market'])
    for key,cls in (("businesses",Business),("moves",CustomerMove),("equity",Equity)):
        e[key] = tuple(cls(**x) for x in e[key])
    f = dict(saved['finance']['inputs']); f['loans'] = tuple(TermLoan(**x) for x in f['loans'])
    return run_financed_enterprise(*restore_opening_inputs(saved),EnterprisePlan(**e),FinancePlan(**f))


FINANCE_DEFAULTS = {"entrant_cash_cents":100_000,"loan_cents":2_500_000,"lender_cash_cents":10_000_000,
    "draw_month":0,"maturity_month":7,"monthly_rate_basis_points":100,
    "payment_priority":"operations_then_debt","default_policy":"suspend_until_cured",
    "principal_repayment_policy":"partial_allowed","rescue_equity_cents":0,"rescue_equity_month":5,
    "delayed_receipts":False,"response_month":6,"incumbent_procurement_month":0,
    "reinvestment_reserve_cents":0,"later_start_candidate":False}


def financed_case_inputs(overrides=None):
    if overrides is None: overrides = {}
    if not isinstance(overrides,dict) or set(overrides)-set(FINANCE_DEFAULTS):
        raise ValueError("Unknown financed-enterprise input")
    x = {**FINANCE_DEFAULTS,**overrides}
    for key in ("entrant_cash_cents","loan_cents","lender_cash_cents","rescue_equity_cents","reinvestment_reserve_cents"):
        _integer(x[key])
        if x[key] > 1_000_000_000: raise ValueError("Cash input outside experiment range")
    for key in ("draw_month","rescue_equity_month","incumbent_procurement_month"):
        _integer(x[key])
        if x[key] > 7: raise ValueError("Scheduled action must be within months 0..7")
    _integer(x['maturity_month'],1);_integer(x['monthly_rate_basis_points'])
    if x['maturity_month'] <= x['draw_month'] or x['maturity_month'] > 48:
        raise ValueError("Maturity must follow the draw and be at most month 48")
    if x['monthly_rate_basis_points'] > 10000: raise ValueError("Monthly rate outside experiment range")
    shared_case_inputs({k:x[k] for k in ('entrant_cash_cents','response_month','incumbent_procurement_month','delayed_receipts')})
    if type(x['later_start_candidate']) is not bool: raise ValueError("Explicit Boolean required")
    FinancePlan(payment_priority=x['payment_priority'],default_policy=x['default_policy'])
    if x['principal_repayment_policy'] not in ('partial_allowed','full_or_nothing'):
        raise ValueError("Unknown principal repayment policy")
    return x


def run_financed_case(overrides=None):
    x = financed_case_inputs(overrides)
    p,t,cs,e = reference_inputs(entrant_cash=x['entrant_cash_cents'],
        incumbent_procurement=x['incumbent_procurement_month'],response_month=x['response_month'],
        delayed_receipts=x['delayed_receipts'])
    t = replace(t,accounts=t.accounts+(Account('capital_lender',x['lender_cash_cents']),))
    if x['rescue_equity_cents']:
        e = replace(e,equity=e.equity+(Equity('scheduled-rescue',x['rescue_equity_month'],
                                             'investor','entrant',x['rescue_equity_cents']),))
    if x['later_start_candidate']:
        p = replace(p,starts=p.starts+(Start('later-candidate',3,1,1),))
    loans = (TermLoan('entrant-term','capital_lender','entrant',x['loan_cents'],x['draw_month'],
        x['maturity_month'],x['monthly_rate_basis_points'],10000,x['principal_repayment_policy']),) if x['loan_cents'] else ()
    f = FinancePlan(loans,x['payment_priority'],x['default_policy'],x['reinvestment_reserve_cents'])
    return {"inputs":x,"result":run_financed_enterprise(p,t,cs,e,f),"source_sha256":finance_source_hashes()}


def finance_witness_options():
    return {name:financed_case_inputs(overrides) for name,overrides in {
        'term_reference':{},'lender_unfunded':{'lender_cash_cents':0},
        'delayed_draw':{'draw_month':2},'early_maturity_cash_recovery':{'maturity_month':3},
        'early_maturity_funded_cure':{'maturity_month':3,'rescue_equity_cents':4_000_000},
        'permanent_stop_after_cure':{'maturity_month':3,'rescue_equity_cents':4_000_000,'default_policy':'stop_permanently'},
        'debt_priority':{'maturity_month':3,'payment_priority':'debt_then_operations'},
        'principal_full_or_nothing':{'maturity_month':3,'principal_repayment_policy':'full_or_nothing'},
        'maturity_beyond_horizon':{'maturity_month':12},
        'maturity_paid_service_unfunded':{'rescue_equity_cents':530_000,'rescue_equity_month':0},
        'maturity_service_one_cent_short':{'rescue_equity_cents':539_999,'rescue_equity_month':0},
        'maturity_and_service_funded':{'rescue_equity_cents':540_000,'rescue_equity_month':0},
        'reinvestment_funded_candidate':{'later_start_candidate':True},
        'reinvestment_reserve_blocks':{'later_start_candidate':True,'reinvestment_reserve_cents':18_000_000},
    }.items()}


def finance_artifact():
    options=finance_witness_options();cases={name:run_financed_case(x)['result'] for name,x in options.items()}
    summary=[]
    for name,r in cases.items():
        finance=r['finance'];c=finance['consolidation']
        entrant=next(x for x in r['enterprise']['business_outcomes'] if x['actor_id']=='entrant')
        summary.append({'case':name,'market_delivered_units':_rational(sum((Fraction(**m['total_delivered_units']) for m in r['enterprise']['months']),Fraction())),
            'entrant_delivered_units':entrant['total_delivered_units'],
            'entrant_closing_cash_cents':r['months'][-1]['closing_cash_cents']['entrant'],
            'first_debt_default_month':finance['first_debt_default_month'].get('entrant'),
            'loan_draw_cents':c['loan_draw_cash_cents'],'principal_recovered_cents':c['principal_recovery_cash_cents'],
            'interest_paid_cents':c['interest_cash_cents'],'principal_outstanding_cents':c['closing_principal_claim_cents'],
            'interest_outstanding_cents':c['closing_interest_claim_cents'],
            'total_started_robots':sum(m['flows']['started'] for m in r['months'])})
    out={'schema_version':'enterprise-finance-experiments/0.1','evidence_status':'synthetic_unqualified_contract_terms',
         'counterfactual_families':['DE-CF11 funding, maturity and cash recovery','DE-CF12 funded candidate reinvestment'],
         'source_sha256':finance_source_hashes(),'case_inputs':options,'summary':summary,'cases':cases}
    out['artifact_hash']=hashlib.sha256(json.dumps(out,sort_keys=True,separators=(',',':')).encode()).hexdigest()
    return out
