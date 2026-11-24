"""What can a firm learn from two robots' undifferentiated settlement?"""
import json
from pathlib import Path
import numpy as np

STATES = np.array([[0,0],[0,1],[1,0],[1,1]])
DIST = (STATES[:,None] != STATES).sum(axis=2)
TRANS = .025**DIST * .975**(2-DIST)
HORIZON = 48
MARGIN = 5.
SWITCH = .6


def channel(route):
    p = route * np.where(STATES[:,None,:] == STATES[None,:,:], .90, .25)
    first, second = p.transpose(2,0,1)
    # likelihood[action, state, aggregate count]
    likelihood = np.stack(((1-first)*(1-second), first*(1-second)+second*(1-first), first*second),axis=2)
    return p, likelihood, p.sum(axis=2)*MARGIN


def tagged_channel(p):
    # The last axis enumerates neither paid, mobile only, arm only and both paid.
    return np.where(STATES[None,None,:,:],p[:,:,None,:],1-p[:,:,None,:]).prod(axis=3)


def evaluate(posterior, deployed, revenue, likelihood, horizon, price_information=True):
    """Gross operating value plus finite-horizon value of observing one pooled count."""
    now = posterior @ revenue.T - SWITCH * DIST[deployed]
    future = np.zeros_like(now)
    for action in range(4):
        signals = likelihood[action].T if price_information else [np.ones(4)]
        for signal in signals:
            joint = posterior * signal
            mass = joint.sum(axis=1, keepdims=True)
            forecast = joint @ TRANS @ revenue.T
            feasible = DIST[action] <= 1
            future[:,action] += (forecast[:,feasible] - SWITCH * DIST[action,feasible] * mass / horizon).max(axis=1)
    score = now + horizon * future
    return np.where(DIST[deployed] <= 1, score, -np.inf)


def tape(seed,n):
    rng=np.random.default_rng(seed)
    return rng.random((HORIZON,n,8))


def simulate(u, regime, policy, span=4, cadence=6, lag=1, fee=2., tag_rate=0.):
    n=u.shape[1]
    idx=np.arange(n)
    who=(u[0,:,6] < .5).astype(int)
    start=8+(u[0,:,7]*12).astype(int)
    post=np.tile([.94,.025,.025,.01],(n,1))
    deployed=np.zeros(n,int)
    ledger=np.zeros((n,9))
    history=[]
    releases=[]
    for t, draw in enumerate(u):
        route=.68 if 18<=t<28 else .93
        realized_route=.58 if regime=="congestion" and 28<=t<42 else route
        p,likelihood,revenue=channel(route)
        fault=t>=start
        if regime=="stable": fault=np.zeros(n,bool)
        if regime=="reversal": fault=fault & (t<32)
        state=np.where(fault,1+who,0)
        if regime=="common": state=np.where(fault,3,0)
        if lag>0 and t>=lag and releases[t-lag] is not None:
            old, evidence=releases[t-lag]
            post=old*evidence
            for observation in history[t-lag:t]:
                post*=observation
                post/=post.sum(axis=1,keepdims=True)
                post=post@TRANS
        audit=policy in ("target","rotate","incumbent","audit_only","selective") and t%cadence==0 and t+lag<HORIZON
        record=None
        if audit:
            marginals=post @ STATES
            lane=np.argmin(abs(marginals-.5),axis=1)
            if policy=="rotate": lane=np.full(n,(t//cadence)%2)
            if policy=="incumbent":
                evidence=np.ones_like(post)
            else:
                observed=STATES[state,lane] ^ (draw[:,4]<.10)
                evidence=np.where(STATES[:,lane].T==observed[:,None],.90,.10)
            buy=np.ones(n,bool)
            if policy=="selective":
                # One label, two possible reports, one future release decision.
                # The index assumes current routing reliability persists for its short horizon.
                steps=min(max(span,1), HORIZON-t-lag)
                forecast=np.linalg.matrix_power(TRANS,lag) @ revenue.T
                allowed=DIST[deployed]<=1
                def operating_value(joint):
                    payoff=steps*(joint@forecast) - joint.sum(axis=1,keepdims=True)*SWITCH*DIST[deployed]
                    return np.where(allowed,payoff,-np.inf).max(axis=1)
                positive=np.where(STATES[:,lane].T==1,.9,.1)
                gain=operating_value(post*positive)+operating_value(post*(1-positive))-operating_value(post)
                buy=gain>fee
                evidence=np.where(buy[:,None],evidence,1.)
            record=(post.copy(),evidence)
            if lag==0:
                post=post*evidence
                post/=post.sum(axis=1,keepdims=True)
            ledger[:,3]+=buy
            ledger[:,0]-=fee*buy
        releases.append(record)
        val=post@revenue.T-SWITCH*DIST[deployed]
        greedy=np.where(DIST[deployed]<=1,val,-np.inf).argmax(axis=1)
        action=greedy
        if policy in ("experiment","target","incumbent","rotate","blind_plan","selective") and span and t+1<HORIZON:
            signals = np.concatenate(((1-tag_rate)*likelihood, tag_rate*tagged_channel(p)),axis=2) if tag_rate else likelihood
            action=evaluate(post,deployed,revenue,signals,min(span,HORIZON-1-t), policy!="blind_plan").argmax(axis=1)
        if policy=="fixed": action=np.zeros(n,int)
        # Two routed orders, one per embodiment. Only paid count enters the pooled learner.
        routed=draw[:,:2]<realized_route
        aligned=STATES[action]==STATES[state]
        paid=routed & (draw[:,2:4]<np.where(aligned,.90,.25))
        count=paid.sum(axis=1)
        cost=SWITCH*DIST[deployed,action]
        ledger[:,0]+=MARGIN*count-cost
        ledger[:,1]+=count
        ledger[:,2]+=aligned.mean(axis=1)/HORIZON
        ledger[:,4]+=DIST[deployed,action]
        ledger[:,5]+=action!=greedy
        ledger[:,6]+=val[idx,greedy]-val[idx,action]
        ledger[:,7]+=post[idx,state]/HORIZON
        evidence=likelihood[action,:,count]
        if policy=="tagged" or tag_rate:
            tag=(count==1) & (draw[:,5] < (1. if policy=="tagged" else tag_rate))
            identity=np.where(paid[:,None,:],p[action],1-p[action]).prod(axis=2)
            evidence=np.where(tag[:,None],identity,evidence)
            ledger[:,8]+=tag
        if policy in ("fixed","audit_only"): evidence=np.ones_like(post)
        history.append(evidence)
        post=post*evidence
        post/=post.sum(axis=1,keepdims=True)
        post=post@TRANS
        deployed=action
    return ledger


def ci(x):
    m=x.mean()
    d=1.96*x.std(ddof=1)/np.sqrt(len(x))
    return np.round([m,m-d,m+d],4).tolist()


def study():
    train=tape(6314,192)
    test=tape(830162,1536)
    policies=["fixed","greedy","experiment","blind_plan","selective","target","rotate","incumbent","audit_only","tagged"]
    configs={}
    for name in ("experiment","target","audit_only","selective"):
        options=[(s,c) for s in ([0,3,9] if name!="audit_only" else [0])
                 for c in ([4,8,16] if name!="experiment" else [8])]
        configs[name]=max(options,key=lambda sc:simulate(train,"single",name,*sc)[:,0].mean())
    configs.update(blind_plan=configs["experiment"],rotate=configs["target"],incumbent=configs["target"])
    results={}
    for env,lag in [("single",1),("stable",1),("common",1),("reversal",1),("congestion",1),("single",3)]:
        runs={name:simulate(test,env,name,*configs.get(name,(0,8)),lag=lag) for name in policies}
        results[f"{env}_lag{lag}"]={
            "means":{k:v.mean(axis=0).round(5).tolist() for k,v in runs.items()},
            "paired_net":{f"{a}-{b}":ci(runs[a][:,0]-runs[b][:,0])
                for a,b in [("experiment","blind_plan"),("selective","experiment"),("selective","target"),("target","incumbent"),("target","rotate"),("target","experiment"),("experiment","greedy"),("experiment","fixed"),("tagged","experiment"),("target","audit_only")]}}
    attribution={}
    for r in (0.,.25,.5,1.):
        experiment=simulate(test,"single","experiment",*configs["experiment"],tag_rate=r)
        myopic=simulate(test,"single","greedy",tag_rate=r)
        reference=simulate(test,"single","experiment",*configs["experiment"])
        count=experiment[:,8].mean()
        blind=simulate(test,"single","blind_plan",*configs["experiment"],tag_rate=r)
        attribution[r]=dict(planning_minus_blind=ci(experiment[:,0]-blind[:,0]),planning_minus_myopic=ci(experiment[:,0]-myopic[:,0]),
            incremental_net=ci(experiment[:,0]-reference[:,0]),mean_tags=round(count,4),
            fee_ceiling=round((experiment[:,0]-reference[:,0]).mean()/count,4) if count else None)
    # Selected illustrative cells from Kim et al., arXiv:2406.09246v1, Table 4.
    # Rubric points over ten trials, in task order: regular eggplant pot, regular carrot plate.
    observed={"RT-1-X":[0,1],"Octo":[1,0]}
    public=dict(source="https://arxiv.org/html/2406.09246v1",
                trials_per_cell=10, task_order=["eggplant_pot","carrot_plate"],scores=observed,
                total_by_policy={k:sum(v) for k,v in observed.items()})
    return dict(published_robot_scores=public,attribution=attribution, columns=["net","paid","alignment","audits","writes","nonmyopic_actions","immediate_expected_sacrifice","mean_probability_true_state","identified_singletons"],calibration=configs,results=results)


if __name__=="__main__":
    Path(__file__).with_name("results.json").write_text(json.dumps(study(),indent=2)+"\n")
