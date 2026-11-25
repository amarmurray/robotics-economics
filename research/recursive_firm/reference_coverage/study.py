"""Reference coverage under selected deployment records. Run with Python and NumPy."""
from itertools import combinations, product
from pathlib import Path
import json
import numpy as np

T = 12
FEE = .16
SHARES = np.array([.55, .45])
MENUS = [(0,"late")] + list(product((1,2,4,6),("early","spread","late")))
REGIMES = ("ordinary","duplicates","reversal","mobile_interference","late","review_shortage","archive_leak")
SITES = ((8.,6.,9.,7.), (6.,9.,6.,9.))  # two known demand and fixture configurations
ACTIONS = list(product((-1,0,1),(-1,0,1),(0,1,2)))  # default checkpoint or signed diagnostic, next block


def slots(count, timing):
    if not count: return []
    if timing=="early": return list(range(count))
    if timing=="late": return list(range(T-count,T))
    return np.linspace(0,T-1,count,dtype=int).tolist() if count>1 else [T//2]


def schedule(site, arm, mobile, installed, shortage):
    d1,d2,k1,k2=SITES[site]
    # Two final markets, distinct stage, handling and review requirements.
    A=np.array([[1,.55],[.4,1],[.70,.42],[.18,.49],[1,0],[0,1],[-1,0],[0,-1]])
    cap=np.array([k1+2*arm+1.8*(installed==1),k2+2.2*mobile+2*(installed==2),
                  7.1,2.9 if shortage else 4.8,d1,d2,0,0])
    vertices=[np.zeros(2)]
    for i,j in combinations(range(len(A)),2):
        mat=A[[i,j]]
        if abs(np.linalg.det(mat))<1e-9: continue
        x=np.linalg.solve(mat,cap[[i,j]])
        if np.all(A@x<=cap+1e-8): vertices.append(x)
    x=max(vertices,key=lambda x:x@np.array([3.,4.]))
    return np.r_[x@np.array([3.,4.])-2.25*(installed!=0), x, A[:2]@x, A[2:4]@x]


def payoff(shortage=False, interference=False):
    # Expected outcome conditional on hidden convention. A qualified method adds service
    # capacity; a failed diagnostic leaves the existing physical executor in place.
    table=np.empty((2,len(ACTIONS),2,9))
    for site in range(2):
        states={(a,b,k):schedule(site,a,b,k,shortage) for a,b,k in product(range(2),range(2),range(3))}
        for i,(a,b,k) in enumerate(ACTIONS):
            for m in (0,1):
                right=2*m-1
                def qualification(action,sign):
                    if not action: return .57
                    return .85 if action==sign else .25
                pa=qualification(a,right)
                pb=qualification(b,-right if interference else right)
                outcome=sum((pa if x else 1-pa)*(pb if y else 1-pb)*states[x,y,k]
                            for x,y in product(range(2),repeat=2))
                table[site,i,m]=np.r_[outcome,pa,pb]
    return table


def tape(seed,n,regime):
    rng=np.random.default_rng(seed)
    site=rng.integers(0,2,n)
    prior=np.where(site==0,.67,.33)
    m=rng.random(n)<prior
    flips=rng.random((T,n))<.035
    if regime=="reversal": flips[9]=~flips[9]
    latent=np.logical_xor.accumulate(np.vstack((m,flips)),axis=0)
    u=rng.random((T,n,4))
    ids=np.arange(T)
    if regime=="duplicates":
        ids=ids//3*3
    return site,prior,latent,u,ids


def policy(data,menu,regime,kind,tables,clamp=False, install=None, local_heads=False):
    site,prior,latent,u,ids=data
    belief=prior.copy()
    appointments=slots(*menu)
    seen=set()
    reviews=0
    retained=np.zeros(len(site))
    admitted=retained.copy()
    # All ordinary records are available for free. Random slots buy a paired diagnostic
    # label on the original roster. A paid archive replay has identical timing and price.
    lag=4 if regime=="late" else 1
    # Keep likelihood ratios at observation dates. Delayed reports can then be
    # applied to the original case without pretending it occurred at release.
    factors=np.ones((T+1,len(prior)))
    reports={}
    for t in range(T+1):
        if t:
            belief=.035+.93*belief
        if t in reports:
            origin,sign=reports[t]
            factors[origin]*=np.where(sign,3.,1/3)
            belief=prior.copy()
            for j in range(t):
                odds=factors[j]
                belief=belief*odds/(1-belief+belief*odds)
                belief=.035+.93*belief
        if t==T: break
        source=ids[t]
        truth=latent[source]
        p=np.where(truth,.75,.25)
        label=u[source,:,0]<p
        prefer=belief>=.5
        # Both hidden worlds generate identical admission counts and archived
        # signatures in the ordinary regime at every observable routing choice.
        bplus=np.where(prefer,.19,.13)+np.where(truth,.015,-.015)
        b=np.where(label,bplus,.32-bplus)
        wplus=np.where(prefer,.11,.07)
        w=np.where(label,wplus,.18-wplus)
        if regime=="archive_leak":
            w=w+np.where(label==truth,.025,-.025)
        accepted=u[t,:,1]<b/np.where(label,p,1-p)
        kept=accepted & (u[t,:,2]<w/b)
        admitted+=accepted
        retained+=kept
        if regime=="archive_leak" and kind!="blind_archive":
            # Favor the incumbent: also give it the correct reduced-form signed
            # leakage likelihood. It needs no case-specific retention propensities.
            mass=np.where(label,wplus,.18-wplus)
            tilt=np.where(label,.025,-.025)
            odds=np.where(kept,(mass+tilt)/(mass-tilt),1.)
            factors[t]*=odds
            belief=belief*odds/(1-belief+belief*odds)
        if t in appointments:
            reviews+=1
            if source not in seen and t+lag<=T and kind=="roster":
                seen.add(source)
                reports[t+lag]=(source,u[source,:,3]<p)
    if clamp: belief=.5+(prior-.5)*.93**T
    neutral,actual=tables
    expected=(1-belief[:,None])*neutral[site,:,0,0]+belief[:,None]*neutral[site,:,1,0]
    if install is not None:
        expected[:,np.arange(len(ACTIONS))%3!=install]=-np.inf
    if local_heads:
        expected[:,[i for i,(a,b,_) in enumerate(ACTIONS) if a or b]]=-np.inf
    action=expected.argmax(axis=1)
    measures=actual[site,action,latent[-1].astype(int)].copy()
    measures[:,0]-=FEE*reviews
    return measures,action,admitted,retained


def ci(x):
    return [round(float(f(x)),5) for f in (np.mean,lambda y:y.mean()-1.96*y.std(ddof=1)/len(y)**.5,
                                                lambda y:y.mean()+1.96*y.std(ddof=1)/len(y)**.5)]


def run():
    base=payoff()
    train=tape(3461,12000,"ordinary")
    scores=[]
    for menu in MENUS:
        net=policy(train,menu,"ordinary","roster",(base,base))[0][:,0].mean()
        gross=net+FEE*menu[0]
        scores.append([gross*share-FEE*menu[0] for share in [1.,*SHARES]])
    winners=np.argmax(scores,axis=0)
    # Each claimant can independently reserve the same shared coverage. Nested
    # subscriptions use the larger requested count, paid in full by its sponsor.
    joint=MENUS[winners[0]]
    private=MENUS[max(winners[1:],key=lambda i:MENUS[i][0])]
    # At each fee first give either firm a unilateral sponsorship option.
    # Use a designated lead sponsor with the larger claim; both receive the
    # same service. With proportional benefits it is the most willing buyer.
    gross_scores=np.array(scores)[:,0]+FEE*np.array([m[0] for m in MENUS])
    fees=(0.,.08,.16,.24,.32,.40,.48,.56,.64,.80)
    counts=np.array([m[0] for m in MENUS])
    frontier={}
    validation=tape(89722,24000,"ordinary")
    realized=np.array([policy(validation,m,"ordinary","roster",(base,base))[0][:,0]+FEE*m[0] for m in MENUS])
    for fee in fees:
        joint_i=int(np.argmax(gross_scores-fee*counts))
        private_i=int(np.argmax(max(SHARES)*gross_scores-fee*counts))
        gain=realized[joint_i]-realized[private_i]-fee*(counts[joint_i]-counts[private_i])
        frontier[str(fee)]=dict(joint=MENUS[joint_i],sponsor=MENUS[private_i],joint_net_advantage=ci(gain))
    result={}
    returns={}
    for regime in REGIMES:
        data=tape(89722,24000,regime)
        known=payoff(regime=="review_shortage")
        actual=payoff(regime=="review_shortage",regime=="mobile_interference")
        tables=known,actual
        designs={"joint":(joint,"roster"),"separate":(private,"roster"),"site_rule":(MENUS[0],"none"),
                 "matched_archive":(joint,"archive"),"blind_archive":(MENUS[0],"blind_archive")}
        runs={k:policy(data,m,regime,kind,tables) for k,(m,kind) in designs.items()}
        ref,choice,_,_=runs["site_rule"]
        treated,act,ad,ret=runs["joint"]
        clamp=policy(data,joint,regime,"roster",tables,True)[0]
        checkpoints=policy(data,MENUS[0],regime,"none",tables,local_heads=True)[0]
        early=policy(data,(joint[0],"early"),regime,"roster",tables)[0]
        if regime in ("ordinary","review_shortage","mobile_interference"):
            candidate={}
            for name,menu,kind in (("ordinary_service",MENUS[0],"none"),("audited",joint,"roster")):
                supplied=[policy(data,menu,regime,kind,tables,install=k)[0] for k in range(3)]
                candidate[name]=np.stack([supplied[k]-supplied[0] for k in (1,2)],axis=1)
            change=candidate["audited"]-candidate["ordinary_service"]
            returns[regime]={}
            for site in (0,1):
                x=change[data[0]==site]
                returns[regime][str(site)]=dict(mean_change=x.mean(axis=0).round(5).tolist(),
                    net_change_quantiles=np.quantile(x[:,:,0],[.1,.5,.9],axis=0).round(5).tolist(),
                    baseline_net=candidate["ordinary_service"][data[0]==site,:,0].mean(axis=0).round(5).tolist())
        result[regime]=dict(net_vs_site={k:ci(v[0][:,0]-ref[:,0]) for k,v in runs.items()},
            joint_minus_separate=ci(treated[:,0]-runs["separate"][0][:,0]),
            joint_minus_matched_archive=ci(treated[:,0]-runs["matched_archive"][0][:,0]),
            joint_minus_checkpoints=ci(treated[:,0]-checkpoints[:,0]),early_vs_site=ci(early[:,0]-ref[:,0]),clamped_gain=ci(clamp[:,0]-ref[:,0]),mean_changes=np.round((treated-ref).mean(axis=0),5).tolist(),
            changed_installation=float(np.mean(act%3!=choice%3)),mean_source_admitted=ad.mean(),mean_source_retained=ret.mean())
    return dict(train_worlds=12000,evaluation_worlds=24000,fee=FEE,fee_frontier=frontier,capital_revaluation=returns,joint=joint,
                private_choices=[MENUS[i] for i in winners[1:]],separate=private,
                calibration_scores={str(menu):np.round(row,6).tolist() for menu,row in zip(MENUS,scores)},
                columns=["net","warehouse_orders","supply_orders","arm_work","mobile_work","handling_hours","review_hours","arm_qualified","mobile_qualified"],
                results=result)


if __name__=="__main__":
    Path(__file__).with_name("results.json").write_text(json.dumps(run(),indent=2)+"\n")
