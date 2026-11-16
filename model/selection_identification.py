"""Exact population selection diagnostic with an explicit funding threshold."""
from fractions import Fraction as Q
from pathlib import Path
import json
import hashlib
from model.theory_deployment import rationalize


def selection(quality, learning, cash, cost=Q(16,5), share=Q(3,4), support=Q(10)):
    quality,learning,cash,cost,share,support=map(Q,(quality,learning,cash,cost,share,support))
    if not 0<quality<=1 or not 0<share<=1 or not 0<=learning<cost or cash<0 or support<=0:
        raise ValueError('Invalid diagnostic primitives')
    economic=(cost-learning)/quality
    advance=share*quality
    funding=max(Q(0),(cost-cash)/advance)
    threshold=max(economic,funding)
    probability=max(Q(0),1-threshold/support)
    mean=(threshold+support)/2 if threshold<support else None
    loan=max(Q(0),cost-cash)
    return dict(quality=quality,learning=learning,cash=cash,cost=cost,
        advance_coefficient=advance,economic_threshold=economic,finance_threshold=funding,
        observed_threshold=threshold,development_probability=probability,
        mean_successful_revenue=mean,required_loan=loan,
        success_state_repayment=loan/quality)


def build():
    rows=[]
    for cash in (Q(7,5),Q(23,10)):
        for name,quality,learning in [('incremental',Q(4,5),Q(0)),
            ('novel_high_learning',Q(2,5),Q(12,5)),('novel_low_learning',Q(2,5),Q(6,5))]:
            rows.append(dict(environment=name,**selection(quality,learning,cash)))
    root=Path(__file__).resolve().parents[1]
    return rationalize(dict(status='synthetic population observational equivalence; not empirical identification',
        units='normalized currency; uniform successful revenue on [0,10]',rows=rows,
        source_sha256={p:hashlib.sha256((root/p).read_bytes()).hexdigest() for p in (
            'model/selection_identification.py','research/theory/selection_identification.md')}))


if __name__=='__main__':
    path=Path(__file__).resolve().parent/'results/selection_identification.json'
    path.write_text(json.dumps(build(),indent=2,sort_keys=True)+'\n')
    print(path)
