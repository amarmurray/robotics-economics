"""Independent finite-domain checks of the eligibility note; synthetic inputs only."""
from fractions import Fraction as Q
from itertools import product
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from model.qualification_finance import funded, funding_cuts


def interval(cash, base, slopes, edges, lower, upper):
    ceiling=Q(upper)
    for cut in funding_cuts(cash,base,edges):
        if cut['slack']<0:return None
        slope=sum((Q(slopes[i]) for i in cut['payers']),Q(0))
        if slope:ceiling=min(ceiling,cut['slack']/slope)
    return (Q(lower),ceiling) if lower<=ceiling else None


def value(cash,base,slopes,edges,x,lower=Q(1),profit=Q(10)):
    obligations=tuple(Q(k)+Q(g)*x for k,g in zip(base,slopes))
    retain=sum(cash)
    if x<lower or not funded(cash,obligations,edges):return retain
    return max(retain,retain-sum(obligations)+profit)


def check():
    cash=(5,3);base=(2,1);slopes=(0,1)
    assert interval(cash,base,slopes,{},1,3)==(1,2)
    assert [value(cash,base,slopes,{},Q(e)) for e in range(4)]==[8,14,13,8]
    assert [max(value(cash,base,slopes,{},Q(x)) for x in range(e+1)) for e in range(4)]==[8,14,14,14]
    assert value(cash,base,slopes,{(0,1):1},Q(3))==12
    checked=0
    for cash in product(range(4),repeat=2):
        for slopes in product((Q(0),Q(1,2),Q(1)),repeat=2):
            for tau in (Q(0),Q(1)):
                edges={(0,1):tau};bound=interval(cash,base,slopes,edges,1,3)
                previous=sum(cash)
                for step in range(13):
                    e=Q(step,4)
                    actual=e>=1 and funded(cash,tuple(Q(k)+g*e for k,g in zip(base,slopes)),edges)
                    assert actual==(bound is not None and bound[0]<=e<=bound[1])
                    optional=max(value(cash,base,slopes,edges,Q(i,4)) for i in range(step+1))
                    closed=max(sum(cash),sum(cash)-sum(base)-sum(slopes)+10) if bound is not None and e>=1 else sum(cash)
                    assert optional==closed and optional>=previous
                    previous=optional;checked+=1
    print(f'Exact example and {checked} interval/optional-value comparisons passed.')


if __name__=='__main__':check()
