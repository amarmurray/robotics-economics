"""Q3 exact synthetic contract/learning/investment comparator (stdlib, no data fit)."""
from fractions import Fraction as F


def source(s, kind):
    """Customer with R=6q-q^2/2, outside w=3; source c=1/hour, T=3."""
    s=F(s)
    if s<=0 or kind not in ('hourly','output'): raise ValueError('bad source option')
    u=F(4)/s if kind=='hourly' else F(2)
    q=min(3*s,max(F(0),F(6)-u))
    H=q/s
    customer=(6-u)*q-q*q/2
    receipts=u*q
    margin=receipts-H
    if customer<F(9,2) or margin<0 or q<=0:
        return {'q':F(0),'H':F(0),'m':F(0),'customer':F(9,2)}
    return {'q':q,'H':H,'m':margin,'customer':customer}


def path(speed,kind,metric='output',tau=F(1),cash=F(4),target_a=F(24),rights=True):
    if metric not in ('output','hours') or min(tau,cash)<0: raise ValueError('bad inputs')
    x=source(speed,kind)
    e=(x['q'] if metric=='output' else x['H']) if rights else F(0)
    Fq=max(F(2),F(11)-tau*e)
    budget=cash+x['m']
    qb=min(F(1),max(F(0),(target_a-2)/2))
    pb=F(4,5)*max(F(0),(target_a-2)*qb-qb*qb-F(2))
    options=[('retain',F(0),F(0))]
    if budget>=8:options.append(('incumbent_A',F(8),F(52,5)-8))
    if budget>=3+Fq:options.append(('qualify_B',F(3)+Fq,pb-(3+Fq)))
    label,investment,gain=max(options,key=lambda v:(v[2],-v[1]))
    return {**x,'e':e,'Fq':Fq,'budget':budget,'choice':label,'cost':investment,
            'gain':gain,'added':x['m']+gain,'terminal':cash+x['m']+gain}


def choose(kind,**kw):
    choices={s:path(s,kind,**kw) for s in (2,4)}
    return max(choices,key=lambda s:choices[s]['added']),choices


if __name__=='__main__':
    for kind,kw in [('hourly',{}),('output',{}),('output',dict(metric='hours',tau=F(2),cash=F(5)))]:
        winner,cases=choose(kind,**kw)
        print(kind,kw,'winner speed',winner,'totals',[(s,str(v['added']),v['choice']) for s,v in cases.items()])
