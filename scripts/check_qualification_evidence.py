"""Validate the sparse evidence links and conditional score bounds, not the studies."""
from fractions import Fraction as Q
from itertools import product
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parents[1]


def full_score_bounds(mean, nonfull_ceiling):
    s,r=Q(mean),Q(nonfull_ceiling)
    if not (0<=s<=1 and 0<=r<1):raise ValueError('Invalid normalized rubric')
    return max(Q(0),(s-r)/(1-r)),s


def check():
    d=json.loads((ROOT/'research/theory/evidence_transitions.json').read_text())
    sources={s['id'] for s in d['sources']}
    records={r['id'] for r in d['records']}
    assert len(records)==len(d['records'])
    assert d['commercial_cost_transition_calibrated'] is False
    for r in d['records']:
        assert r['source_id'] in sources and r['locator'] and r['source_nodes'] and r['target_node']
        assert r['unknowns']['qualification_cost_change'] is None
        assert r['unknowns']['responsible_payer'] is None
    for row in d['conditional_full_score_bounds']:
        assert row['record'] in records and row['condition']
        low,high=full_score_bounds(row['mean_score'],row['nonfull_ceiling'])
        assert (low,high)==(Q(row['lower']),Q(row['upper']))
        s,r=Q(row['mean_score']),Q(row['nonfull_ceiling'])
        # Explicit distributions attain each endpoint on {0,r,1}.
        assert high==s # mass s at one, remainder at zero
        if s>r:assert low+(1-low)*r==s
        else:assert (s/r)*r==s
    # Independent finite-support trial enumeration checks validity, including zero/full endpoints.
    for r in (Q(1,2),Q(3,4)):
        for trials in product((Q(0),r,Q(1)),repeat=5):
            mean=sum(trials)/5
            full=Q(sum(x==1 for x in trials),5)
            low,high=full_score_bounds(mean,r)
            assert low<=full<=high
    # Conditional exact-ten-trial illustration for DreamGen's .55 graded mean.
    counts=[full for full in range(11) for partial in range(11-full)
            if Q(full)+Q(partial,2)==Q(11,2)]
    assert (min(counts),max(counts))==(1,5)
    print('Evidence links, unknown-cost markers, sharp bounds and finite-trial illustration verified.')


if __name__=='__main__':check()
