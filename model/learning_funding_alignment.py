"""Exact directional learning threshold over existing funding cuts."""
from fractions import Fraction as Q
from pathlib import Path
import hashlib
import json
from model.qualification_finance import funding_cuts, funded
from model.theory_deployment import rationalize, service


def experience_threshold(cash, costs, edges, loading, upper):
    costs, loading, upper = tuple(map(Q,costs)), tuple(map(Q,loading)), Q(upper)
    if len(costs)!=len(loading) or upper<0 or any(x<0 for x in loading):
        raise ValueError('Invalid experience domain')
    if any(k<l*upper for k,l in zip(costs,loading)):
        raise ValueError('Linear domain would create negative costs')
    required=Q(0)
    for cut in funding_cuts(cash,costs,edges):
        deficit=-cut['slack']
        effect=sum((loading[i] for i in cut['payers']),Q(0))
        if deficit>0 and effect==0:
            return None
        if effect>0:
            required=max(required,deficit/effect)
    return required if required<=upper else None


def build():
    cash=(Q(5),Q(1)); costs=(Q(2),Q(2)); upper=Q(2); e=Q(1)
    loads={'provider_focused':(Q(1),Q(0)), 'operator_focused':(Q(0),Q(1)),
           'broad':(Q(1,2),Q(1,2))}
    continuation=service(10,2,2,capture=Q(5,6))['provider']
    worlds=[]
    for tau in (Q(0),Q(1,2),Q(1)):
        edges={(0,1):tau}
        for name,loading in loads.items():
            remaining=tuple(k-l*e for k,l in zip(costs,loading))
            feasible=funded(cash,remaining,edges)
            value=sum(cash)-sum(remaining)+continuation if feasible else sum(cash)
            worlds.append(dict(source=name,tau=tau,loading=loading,experience=e,
                threshold=experience_threshold(cash,costs,edges,loading,upper),
                costs=remaining,feasible=feasible,value=value,
                threshold_null='No feasible threshold within declared domain' if experience_threshold(cash,costs,edges,loading,upper) is None else None))
    root=Path(__file__).resolve().parents[1]
    return rationalize(dict(status='synthetic conditional corollary; no novelty/calibration claim',
        input=dict(cash=cash,costs=costs,experience_upper=upper,continuation=continuation),worlds=worlds,
        source_sha256={p:hashlib.sha256((root/p).read_bytes()).hexdigest() for p in (
            'model/learning_funding_alignment.py','model/qualification_finance.py',
            'model/theory_deployment.py','research/theory/learning_funding_alignment.md')}))


if __name__=='__main__':
    path=Path(__file__).resolve().parent/'results/learning_funding_alignment.json'
    path.write_text(json.dumps(build(),indent=2,sort_keys=True)+'\n')
    print(path)
