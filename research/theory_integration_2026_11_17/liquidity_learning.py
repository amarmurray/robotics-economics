"""Exact finite-horizon cash/receivables Bellman baseline, no third-party dependencies.

All monetary values are synthetic normalized units, all events ordinary complete-service
acceptance (not robot-motion proxies). This is NOT a calibrated economic model.
"""
from __future__ import annotations
from fractions import Fraction as F
from functools import lru_cache
import json
from dataclasses import dataclass

@dataclass(frozen=True)
class Parameters:
    m: int = 7                         # customer intercept for A contracted surplus receipts
    lag: int = 1                       # invoice payment maturity in periods
    horizon: int = 4
    starting_cash: int = 4
    shared_cost: int = 13
    specialist_cost: int = 20
    p_shared: F = F(3, 4)
    p_specialist: F = F(9, 10)
    b_invoice: int = 16
    b_variable_cost: int = 2
    minimum_A: int = 1                # hard complete-service floor


def a_invoice(m: int, q: int) -> int:
    return m*q - q*(q-1)              # concave discrete accepted-output contract


def choices(par: Parameters, cash: int, qualified: bool):
    """Operating options, immediate costs and dated invoice claims.

    Specialist development may be concurrent with A at q=1 or q=2; shared
    development uses productive capacity and caps accepted A at one.
    A and B sales represent two nonoverlapping service windows after qualification.
    """
    for q in range(par.minimum_A, 3):
        for b in ([0, 1] if qualified else [0]):
            cost=q + par.b_variable_cost*b
            if cost <= cash:
                yield (f"produce_A{q}_B{b}", cost, a_invoice(par.m,q)+par.b_invoice*b, None)
        if qualified: continue
        for route, k, prob in (("shared",par.shared_cost,par.p_shared), ("specialist",par.specialist_cost,par.p_specialist)):
            if route=="shared" and q!=1:continue
            cost=q+k
            if cost <= cash:
                yield (route+"_A"+str(q), cost, a_invoice(par.m,q), prob)


def solve(par: Parameters):
    assert par.lag >= 1 and par.horizon >= 1 and par.minimum_A in (1,2)
    starting = (0, par.starting_cash, (0,)*par.lag, False)
    choice_map={}
    n_states=[0]

    @lru_cache(None)
    def v(t:int, cash:int, pending:tuple[int,...], qualified:bool):
        n_states[0]+=1
        if t==par.horizon:
            return F(cash+sum(pending))
        available = cash + pending[0]
        next_pending=pending[1:]
        best=None
        best_choice=None
        for name,cost,invoice,prob in choices(par,available,qualified):
            due=next_pending+(invoice,)
            residual=available-cost
            if prob is None:
                val=v(t+1,residual,due,qualified)
            else:
                val=prob*v(t+1,residual,due,True)+(1-prob)*v(t+1,residual,due,False)
            if best is None or val>best:
                best=val;best_choice=name
        if best is None: # contract cannot be delivered without financing
            return None
        choice_map[(t,cash,pending,qualified)]=best_choice
        return best
    # Cash is required for every future mandatory service on each branch.
    # For baseline parameter domain all choices have a feasible continuation.
    result=v(*starting)
    return result, choice_map.get(starting), n_states[0], v, choice_map


def no_learning(par:Parameters):
    """Expected terminal equity from serving exactly 2 A accepted units each period."""
    val=par.starting_cash+par.horizon*(a_invoice(par.m,2)-2)
    return F(val)


def scenarios():
    out={}
    for lag in (1,2):
        for m in (4,7,11):
            p=Parameters(m=m,lag=lag)
            v,action,n,_,_=solve(p)
            base=no_learning(p)
            out[f"m{m}_lag{lag}"]={"value":str(v),"baseline":str(base),"premium":str(v-base),"initial_action":action,"states":n,
                                     "t1_cash_after_maturity_normal_t0":p.starting_cash-2+(a_invoice(p.m,2) if lag==1 else 0)}
    return out

if __name__=="__main__":
    print(json.dumps(scenarios(),indent=2,sort_keys=True))


def financed_shared_lag2_paths(fee: int = 1):
    """Constructive, *contingently enforceable* supplier advance benchmark.

    Special to m=7, lag=2, cash0=4, shared attempt t=1, advance 12,
    repayment t=4 against assignable accepted-service A receivables.
    Does not grant an unobserved funding arrangement to any real vendor.
    """
    par=Parameters(m=7,lag=2)
    paths={}
    for success in (False,True):
        cash=4
        pending=[0]*2
        recorded=[]
        for t in range(4):
            matured=pending.pop(0)
            cash+=matured
            if t==1:
                cash+=12
            q=1 if t==1 else 2
            b=int(success and t>=2)
            expenses=q+2*b+(13 if t==1 else 0)
            cash-=expenses
            assert cash>=0
            pending.append(a_invoice(par.m,q)+16*b)
            recorded.append((t,cash,matured,expenses,pending[-1]))
        # At t=4, collect the invoice earned at t=2 before contractual repayment.
        cash += pending.pop(0)
        repay=12+fee
        assert cash>=repay
        cash-=repay
        terminal_equity=cash+sum(pending) # includes t=3 accepted but not yet collected
        paths['success' if success else 'failure']={
            'terminal_equity':terminal_equity,
            't4_repayment_cash_before':cash+repay,
            'repayment':repay,
            'path':recorded,
        }
    return paths
