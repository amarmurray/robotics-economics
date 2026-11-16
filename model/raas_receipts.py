"""Small exact RaaS contract diagnostic, not a general deployment simulator."""
from fractions import Fraction as Q
from pathlib import Path
import hashlib
import json
from model.theory_deployment import rationalize


def outcome(speed, rate, contract='hourly', cash=Q(0), investment=Q(4),
            next_profit=Q(10), advance_fraction=Q(1,2)):
    speed,rate,cash,investment,next_profit,advance_fraction=map(Q,
        (speed,rate,cash,investment,next_profit,advance_fraction))
    a,b,incumbent,hour_cost,hours=Q(6),Q(1),Q(3),Q(1),Q(3)
    if speed<=0 or min(rate,cash,investment,next_profit)<0 or not 0<=advance_fraction<=1:
        raise ValueError('Invalid diagnostic inputs')
    if contract not in ('hourly','output'):raise ValueError('Unknown contract')
    price=rate/speed if contract=='hourly' else rate
    outside=(a-incumbent)**2/(2*b)
    if price>incumbent:
        q=robot_hours=receipts=resources=Q(0);customer=outside
    else:
        q=max(Q(0),(a-price)/b);robot_hours=q/speed
        if robot_hours>hours:raise ValueError('Capacity binds: outside this diagnostic domain')
        receipts=price*q;resources=hour_cost*robot_hours
        if receipts<resources:raise ValueError('Negative legacy margin: outside this diagnostic domain')
        customer=a*q-b*q*q/2-receipts
    provider=receipts-resources
    # Keep enough source receipts to meet operating obligations as well as repayment.
    advance=min(advance_fraction*receipts,provider)
    loan=max(Q(0),investment-cash)
    invest=(loan<=advance and next_profit>=investment)
    loan=loan if invest else Q(0)
    spend=investment if invest else Q(0)
    after=cash+loan-spend
    terminal=after+receipts-resources-loan+(next_profit if invest else Q(0))
    assert after>=0 and receipts-resources-loan>=0
    assert terminal==cash+provider-spend+(next_profit if invest else Q(0))
    return dict(speed=speed,contract=contract,rate=rate,unit_price=price,q=q,
        robot_hours=robot_hours,receipts=receipts,resources=resources,
        customer_profit=customer,customer_outside=outside,provider_profit=provider,
        source_joint_surplus=provider+customer,advance_limit=advance,loan=loan,
        invested=invest,after_investment_cash=after,terminal_cash=terminal)


def build():
    worlds={}
    for s in (Q(2),Q(4)):
        worlds[f'fixed_hourly_speed_{s}']=outcome(s,4)
        worlds[f'fixed_output_speed_{s}']=outcome(s,2,'output')
        # For these parameters the incumbent caps the optimal output price at three.
        worlds[f'repriced_speed_{s}']=outcome(s,3,'output')
        worlds[f'own_cash_speed_{s}']=outcome(s,4,cash=4)
    root=Path(__file__).resolve().parents[1]
    return rationalize(dict(status='synthetic contract-regime comparison; no calibration or novelty claim',
        units='normalized accepted output, robot hours and currency; two dates, zero interest',
        assumptions='Deterministic source receipts, complete source service, no shared target resources; next-project receipts not pledgeable before qualification',
        worlds=worlds,source_sha256={p:hashlib.sha256((root/p).read_bytes()).hexdigest() for p in (
            'model/raas_receipts.py','research/theory/raas_receipts.md')}))


if __name__=='__main__':
    path=Path(__file__).resolve().parent/'results/raas_receipts.json'
    path.write_text(json.dumps(build(),indent=2,sort_keys=True)+'\n')
    print(path)
