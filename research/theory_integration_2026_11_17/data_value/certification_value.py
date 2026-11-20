#!/usr/bin/env python3
"""Exact synthetic certification/production exercises; standard library only.

Run: python certification_value.py --output certification_value_results.json
No robotics field data, safety authorization, customer dollar estimates or CI claims.
"""
import argparse
import json
from fractions import Fraction as F
from itertools import product
from pathlib import Path


def choose_methods(admitted, demand=(1,1), capacity=2, contribution=None):
    """Two indivisible original orders; one safe recipe or no sale for each.

    Each full order has R=(value, operator capacity), G alternative only if
    certified/admitted. A and B demand indicators are fixed externally.
    """
    if contribution is None:
        contribution={'RA':(F(4),F(2)), 'RB':(F(3),F(2)),
                      'GA':(F(4),F(1)), 'GB':(F(3),F(1))}
    options=[]
    for i,name in enumerate('AB'):
        xs=['none']
        if demand[i]:
            xs.append('R'+name)
            if name in admitted: xs.append('G'+name)
        options.append(xs)
    best=(F(-1),None)
    for actions in product(*options):
        cost=sum((contribution[x][1] for x in actions if x!='none'),F(0))
        if cost>capacity: continue
        value=sum((contribution[x][0] for x in actions if x!='none'),F(0))
        if value>best[0]: best=(value,actions)
    return best


def independent_value(gb, e_fixed=F(1,5)):
    """Independent half-weight original-order populations; G_A signed,
    G_B only hypothetical after prospective physical certification.
    E is separately assumed admitted, B has fixed service value 4.
    """
    base=F(4,2)+F(3,2)
    with_gb=F(4,2)+F(max(F(3),gb),2)
    net_cert=with_gb-F(1)  # prospective certificate/validation cost once
    net_e=F(4,2)+F(4,2)-e_fixed  # incumbent A G and embodiment B
    return base,with_gb,net_cert,net_e


def upper_certificate(admitted, new_contributions):
    """Old dual λ=2 with operator cap 2 and no demand dual needed.
    Valid for indivisible models as an LP *upper*, here old LP is exact.
    New candidate G recipes each allowed at most one unit.
    """
    lam=F(2); old_lp_bound=lam*2
    return old_lp_bound + sum((max(F(0), new_contributions[x][0]-lam*new_contributions[x][1]) for x in admitted),F(0))


def main():
    checks=0
    def ck(v):
        nonlocal checks
        assert v
        checks+=1

    sets=[set(),{'A'},{'B'},{'A','B'}]
    vals={''.join(sorted(a)) or 'R':choose_methods(a)[0] for a in sets}
    ck(vals=={'R':F(4),'A':F(4),'B':F(4),'AB':F(7)})
    cross=vals['AB']-vals['A']-vals['B']+vals['R']
    ck(cross==F(3))
    cons={'A':{'GA':(F(4),F(1))},'B':{'GB':(F(3),F(1))},'AB':{'GA':(F(4),F(1)),'GB':(F(3),F(1))}}
    bound={key:upper_certificate(mp.keys(),mp) for key,mp in cons.items()}
    ck(bound=={'A':F(6),'B':F(5),'AB':F(7)})
    for key,v in vals.items():
        if key=='R':continue
        ck(v<=bound[key])
    ck(vals['AB']==bound['AB'])

    # Marginal purchase rates pA=pB=1/2 in both worlds.
    joint={'joint':{(0,0):F(1,2),(1,1):F(1,2)},
           'alternating':{(1,0):F(1,2),(0,1):F(1,2)}}
    avgs={}
    for world,law in joint.items():
        ck(sum(law.values())==1)
        ck(sum(p for d,p in law.items() if d[0])==F(1,2))
        ck(sum(p for d,p in law.items() if d[1])==F(1,2))
        avgs[world]={'R':sum((p*choose_methods(set(),d)[0] for d,p in law.items()),F(0)),
                     'AB':sum((p*choose_methods({'A','B'},d)[0] for d,p in law.items()),F(0))}
    ck(avgs['joint']=={'R':F(2),'AB':F(7,2)})
    ck(avgs['alternating']=={'R':F(7,2),'AB':F(7,2)})

    b0,_,lo,emb=independent_value(F(0))
    _,_,hi,emb2=independent_value(F(6))
    ck(b0==F(7,2))
    ck(lo==F(5,2) and hi==F(4))
    ck(emb==F(19,5) and emb2==emb)
    no_signal=max(emb,(lo+hi)/2)
    after_signal=(max(emb,lo)+max(emb,hi))/2
    ck(no_signal==F(19,5))
    ck(after_signal==F(39,10))
    ck(after_signal-no_signal==F(1,10))
    # Technical qualification and safe admission can be identical in both
    # worlds; only original customer B willingness/receipt differs.
    # The LP certificate must be an upper, not an asserted attainable gain.
    for m1,m2 in product(range(0,8),repeat=2):
        c={'RA':(F(4),F(2)),'RB':(F(3),F(2)),
           'GA':(F(m1),F(1)),'GB':(F(m2),F(1))}
        old=choose_methods(set(),contribution=c)[0]
        ck(old==F(4))
        for a in sets:
            current=choose_methods(a,contribution=c)[0]
            ub=upper_certificate(['G'+i for i in a],c)
            ck(old<=current<=ub)
    output={'not_empirical':True,'scope':'two indivisible original buyers with one shared operator, and separate two-stratum independent example',
            'vals':{k:str(v) for k,v in vals.items()},'interaction':str(cross),
            'dual_upper':{k:str(v) for k,v in bound.items()},
            'joint_market':{k:{t:str(v) for t,v in z.items()} for k,z in avgs.items()},
            'independent_population':{'baseline_R_and_GA':str(b0),'gross_cert_low':str(lo+1),
                'gross_cert_high':str(hi+1),'net_cert_low':str(lo),'net_cert_high':str(hi),
                'net_E':str(emb),'pre_signal_policy_value':str(no_signal),
                'perfect_customer_signal_value':str(after_signal),'gross_signal_EVSI':str(after_signal-no_signal)},
            'exact_assertions':checks,'field_customer_panels':False,'physical_certification':False,
            'full_repo_CI':False}
    return output


if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--output');args=parser.parse_args();o=main();raw=json.dumps(o,indent=2,sort_keys=True)+'\n'
    if args.output:Path(args.output).write_text(raw)
    print(raw)
