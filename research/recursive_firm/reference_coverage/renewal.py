"""Adaptive renewal of a reference panel before a dated installation decision."""
from pathlib import Path
import json
from itertools import combinations
import numpy as np
from study import T, FEE, ACTIONS, payoff, policy, tape, ci

GRID=np.linspace(0.,1.,2001)


def update(b,positive):
    ratio=np.where(positive,3.,1/3)
    return b*ratio/(1-b+b*ratio)


def forecast(b):
    return .035+.93*b


def solve(table,fee,share,limit):
    choices=np.zeros((T,2,limit+1,len(GRID)),bool)
    terminal=[]
    for site in range(2):
        v=table[site,:,:,0]
        terminal.append(share*((1-GRID)*v[:,0,None]+GRID*v[:,1,None]).max(axis=0))
    future=np.repeat(np.array(terminal)[:,None,:],limit+1,axis=1)
    for t in reversed(range(T)):
        current=np.zeros_like(future)
        for site in range(2):
            for k in range(limit+1):
                wait=np.interp(forecast(GRID),GRID,future[site,k])
                current[site,k]=wait
                if k:
                    chance=.25+.5*GRID
                    yes=np.interp(forecast(update(GRID,True)),GRID,future[site,k-1])
                    no=np.interp(forecast(update(GRID,False)),GRID,future[site,k-1])
                    buy=chance*yes+(1-chance)*no-fee
                    choices[t,site,k]=buy>wait+1e-10
                    current[site,k]=np.maximum(wait,buy)
        future=current
    return choices,future


def evaluate(data,plan,limit,known,actual,fee,trace=None):
    site,b0,state,u,_=data
    b=b0.copy()
    k=np.full(len(site),limit)
    purchases=[]
    for t in range(T):
        buy=trace[t] if trace is not None else plan[t,site,k,np.rint(b*(len(GRID)-1)).astype(int)]
        purchases.append(buy)
        label=u[t,:,3]<np.where(state[t],.75,.25)
        b=forecast(np.where(buy,update(b,label),b))
        k-=buy
    choice=((1-b[:,None])*known[site,:,0,0]+b[:,None]*known[site,:,1,0]).argmax(axis=1)
    used=limit-k
    return actual[site,choice,state[-1].astype(int),0]-fee*used,used,choice,np.array(purchases)


def fixed_frontier(known):
    """Enumerate all precommitted subsets of the 12 shifts up to the six-slot cap."""
    rows=[]
    for k in range(7):
        for dates in combinations(range(T),k):
            value=[]
            for site,prior in enumerate((.67,.33)):
                mass=np.array([[1-prior,prior]])
                prev=0
                for date in (*dates,T):
                    stay=(1+.93**(date-prev))/2
                    mass=mass@np.array([[stay,1-stay],[1-stay,stay]])
                    if date!=T:
                        mass=np.vstack((mass*[.75,.25],mass*[.25,.75]))
                    prev=date
                value.append((mass@known[site,:,:,0].T).max(axis=1).sum())
            rows.append((dates,np.array(value)))
    return rows


def run():
    known=payoff()
    interference=payoff(interference=True)
    out={}
    fixed_options=fixed_frontier(known)
    for fee in (.16,.40):
        plans={s:solve(known,fee,s,6) for s in (1.,.55)}
        for regime in ("ordinary","reversal","mobile_interference"):
            data=tape(89722,24000,regime)
            actual=interference if regime=="mobile_interference" else known
            design={s:evaluate(data,plans[s][0],6,known,actual,fee) for s in plans}
            joint,nj,aj,_=design[1.]
            fixed_dates=[max(fixed_options,key=lambda r:r[1][site]-fee*len(r[0]))[0] for site in (0,1)]
            ft=np.array([[t in ds for ds in fixed_dates] for t in range(T)])[:,data[0]]
            best_fixed=evaluate(data,None,6,known,actual,fee,ft)[0]
            donor=list(tape(89723,24000,regime))
            # Match donors and recipients by site, using an independent world at that site.
            donor_result=evaluate(donor,plans[1.][0],6,known,actual,fee)[3]
            separate_rng=np.random.default_rng(89724)
            yoked=np.empty_like(donor_result)
            for site in (0,1):
                mask=data[0]==site
                idx=separate_rng.choice(np.flatnonzero(donor[0]==site),mask.sum())
                yoked[:,mask]=donor_result[:,idx]
            yoke=evaluate(data,None,6,known,actual,fee,yoked)[0]
            private,npv,ap,_=design[.55]
            fixed,_,_,_=policy(data,(1,"late"),regime,"roster",(known,actual))
            fixed_net=fixed[:,0]+FEE-fee
            site_rule=policy(data,(0,"late"),regime,"none",(known,actual))[0][:,0]
            out[f"{fee}_{regime}"]=dict(exact_fixed_dates=fixed_dates,joint_minus_exact_fixed=ci(joint-best_fixed),joint_minus_yoked=ci(joint-yoke),matched_audits=yoked.sum(axis=0).mean(),joint_minus_site=ci(joint-site_rule),
                joint_minus_fixed_one=ci(joint-fixed_net),joint_minus_sponsor=ci(joint-private),
                joint_audits=round(nj.mean(),5),sponsor_audits=round(npv.mean(),5),
                joint_counts=np.bincount(nj,minlength=7).tolist(),sponsor_counts=np.bincount(npv,minlength=7).tolist(),
                different_installation=float(np.mean(aj%3!=ap%3)))
    return out


if __name__=="__main__":
    Path(__file__).with_name("renewal_results.json").write_text(json.dumps(run(),indent=2)+"\n")
