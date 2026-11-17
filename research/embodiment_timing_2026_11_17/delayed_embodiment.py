"""Deterministic, synthetic embodiment-development and demand-timing model.

Consumes the prior capability-to-qualification program and its fixed-criterion
cost. A three-option t=0 investment compares software adaptation, physical
redesign, and incumbent deployment. No uncertainty or empirical calibration.
Run from this directory: python delayed_embodiment.py
"""
from __future__ import annotations
from dataclasses import dataclass, replace, asdict
from decimal import Decimal, ROUND_CEILING
from fractions import Fraction as F
from math import isfinite
from pathlib import Path
import json
import sys

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'qualification_bridge_2026_11_17'))
sys.path.insert(0,str(ROOT/'takeover_2026_11_17'))
from qualification import Component, qualify
from expansion import Market, jsonable

EPSILON=.02
VERIFICATION=2.0
OLD_PROFILE=(Component('perception',.08,0,1,1),
             Component('force-control',.05,.012,1,8))
REDESIGNED_PROFILE=(Component('perception',.08,0,1,1),
                    Component('force-control',.05,0,2,8))


def upper_cent(cost: float) -> F:
    if not isfinite(cost) or cost < 0:
        raise ValueError('Finite nonnegative cost required')
    return F(Decimal(str(cost)).quantize(Decimal('.01'), rounding=ROUND_CEILING))


@dataclass(frozen=True)
class Project:
    name: str
    market: str # B for the new application; A for incumbent extension
    capacity: F
    cost: F
    lag: int
    acquisition: F


@dataclass(frozen=True)
class Setting:
    initial_cash: F = F(30)
    horizon: int = 4
    beta: F = F(1)
    demand_decline: F = F(0)
    fixed_design_cost: F = F(8)
    redesigned_lag: int = 2
    salvage_share: F = F(0)
    a_market: Market = Market(F(12),F(2),F(2),F(7))
    b_market: Market = Market(F(25),F(2),F(2),F(2))

    def __post_init__(self):
        if self.initial_cash < 0 or self.horizon < 1 or not 0 < self.beta <= 1:
            raise ValueError('Require nonnegative cash, positive horizon and beta (0,1]')
        if self.demand_decline < 0 or self.fixed_design_cost < 0 or self.redesigned_lag < 0:
            raise ValueError('Nonnegative decline, design cost, and lag required')
        if not 0 <= self.salvage_share < 1:
            raise ValueError('Salvage share in [0,1) required')


def projects(setting:Setting) -> dict[str,Project]:
    old=qualify(OLD_PROFILE,EPSILON,VERIFICATION)
    new=qualify(REDESIGNED_PROFILE,EPSILON,VERIFICATION)
    if not old.feasible or not new.feasible:
        raise ValueError('Declared profiles must qualify under the common standard')
    old_cost=upper_cent(old.total_cost)
    new_cost=upper_cent(new.total_cost)
    return {
        'incumbent':Project('incumbent','A',F(1),F(6),0,F(6)),
        'software':Project('software','B',F(1),F(3)+old_cost,0,F(3)),
        'redesign':Project('redesign','B',F(3),F(3)+setting.fixed_design_cost+new_cost,
                           setting.redesigned_lag,F(3)),
    }


def market_at(setting:Setting,t:int,market:str) -> Market:
    if not 1<=t<=setting.horizon:
        raise ValueError('t outside demand horizon')
    if market=='A':return setting.a_market
    if market=='B':return replace(setting.b_market,
        a=setting.b_market.a-setting.demand_decline*(t-1))
    raise ValueError('unknown market')


def provider_profit(setting:Setting,p:Project,t:int) -> F:
    if t<=p.lag:return F(0)
    if p.market=='A':
        market=market_at(setting,t,'A')
        return market.service(F(1)+p.capacity)[1]-market.service(F(1))[1]
    return market_at(setting,t,'B').service(p.capacity)[1]


def value(setting:Setting,p:Project)->F | None:
    if p.cost>setting.initial_cash:return None
    flows=sum((setting.beta**(t-1))*provider_profit(setting,p,t)
              for t in range(1,setting.horizon+1))
    salvage=(setting.beta**(setting.horizon-1))*setting.salvage_share*p.acquisition
    return flows-p.cost+salvage


def select(setting:Setting) -> dict:
    ps=projects(setting)
    vals={name:value(setting,p) for name,p in ps.items()}
    eligible={name:val for name,val in vals.items() if val is not None}
    # Retaining cash and incumbent assets is always a feasible zero-gain policy.
    eligible['retain']=F(0)
    winner=max(eligible,key=lambda n:(eligible[n],-int(ps[n].cost) if n in ps else 0,n))
    return dict(winner=winner,values=vals,projects=ps)


def binding_switch(setting:Setting) -> F:
    """Formal gamma at redesign/software indifference in common binding regime.

    Only a candidate. Test capacity and adoption conditions at the result.
    Assumes beta=1, same B market resource cost and capture share, no salvage,
    software lag0, no change in A value. Valid for any nonnegative lags.
    """
    ps=projects(setting)
    h,l=ps['redesign'],ps['software']
    if setting.beta != 1 or setting.salvage_share != 0 or l.lag != 0:
        raise ValueError('Binding formula only for beta=1/no salvage/software lag 0')
    at0=replace(setting,demand_decline=F(0))
    delta=value(at0,h)-value(at0,l)
    if delta is None:raise ValueError('Unfunded alternatives')
    gradient=setting.b_market.capture*(
        h.capacity*sum(t-1 for t in range(h.lag+1,setting.horizon+1))-
        l.capacity*sum(t-1 for t in range(1,setting.horizon+1)))
    if gradient<=0:raise ValueError('Redesign advantage is not necessarily decreasing')
    return delta/gradient


def binding_valid(setting:Setting)->bool:
    for p in (projects(setting)['software'],projects(setting)['redesign']):
        for t in range(p.lag+1,setting.horizon+1):
            m=market_at(setting,t,'B')
            if (m.a-m.c)/m.b<p.capacity:return False
            if m.service(p.capacity)[0]!=p.capacity:return False
    return True


def experiment()->dict:
    base=Setting()
    cases={
       'stable_demand':base,
       'decline_three':replace(base,demand_decline=F(3)),
       'decline_five':replace(base,demand_decline=F(5)),
       'decline_six':replace(base,demand_decline=F(6)),
       'long_build':replace(base,redesigned_lag=4),
       'tight_cash':replace(base,initial_cash=F(22)),
       'higher_design_cost':replace(base,fixed_design_cost=F(25)),
       'salvage_quarter':replace(base,salvage_share=F(1,4)),
       'discount':replace(base,beta=F(9,10)),
    }
    result={k:dict(setting=s,decision=select(s)) for k,s in cases.items()}
    g=binding_switch(base)
    boundary=replace(base,demand_decline=g)
    return jsonable(dict(status='Exact deterministic synthetic experiment; not empirical calibration',
        qualification_old_cost=upper_cent(qualify(OLD_PROFILE,EPSILON,VERIFICATION).total_cost),
        qualification_redesign_cost=upper_cent(qualify(REDESIGNED_PROFILE,EPSILON,VERIFICATION).total_cost),
        switch_decline=g,binding_regime_at_switch=binding_valid(boundary),
        boundary_values=select(boundary)['values'],cases=result))


if __name__=='__main__':
    out=Path(__file__).with_name('results.json')
    out.write_text(json.dumps(experiment(),sort_keys=True,indent=2)+'\n')
    print(out)
