"""Priced and delayed validation of three transfer links. Python 3 and NumPy."""
import json
from itertools import product
from pathlib import Path
import numpy as np

LANES = ("desk", "fixed_arm", "mobile")
VALUE = np.array([4., 7., 10.])
T, K, AUDITS, FEE = 60, 12, 8, 2.
MODES = ("local", "live", "checkpoint")


class World:
    def __init__(self, seeds, regime):
        n = len(seeds)
        draws = [np.random.default_rng(seed).random((T, 6, 32)) for seed in seeds]
        u = np.stack(draws)
        self.n = n
        self.regime = regime
        self.shared = u[:, 0, 0, :K] < .5
        self.initial = np.where(self.shared, .77, .23)
        self.source = np.broadcast_to(self.shared[:, None, :], (n,T,K)).copy()
        self.target = np.broadcast_to(self.shared[:,None,None,:],(n,T,3,K)).copy()
        # Adapter maps actions to canonical binary coordinates before scoring.
        self.target ^= (u[:,0,1,:K] < .12)[:,None,None,:]
        lanes = np.arange(3)[None,:]
        start = 17+(u[:,1,2,:3]*14).astype(int)
        if regime=="late":
            start+=20
        for day in range(T):
            if regime != "stable":
                cut = (day >= start[:,0])[:,None] & (np.arange(K)%3!=0)
                self.source[:,day] ^= cut
                changed = (day >= start+lanes*2) & (lanes!=0)
                self.target[:,day] ^= changed[:,:,None] & (np.arange(K)%3 != 1)
                if regime == "reversal" and day >= 44:
                    self.target[:,day,2] ^= True
            if regime == "reversal" and day >= 43:
                self.source[:,day] ^= np.arange(K)%2==0
        # Independent tape for operating orders, audits, retention and corrections.
        def family(draw, day):
            f = (K*draw**1.8).astype(int)
            shift = 5 if day >= 30 and regime != "stable" else 0
            return (f+shift)%K
        self.orders = np.stack([family(u[:,d,3,:3],d) for d in range(T)],axis=1)
        self.panel = np.stack([family(u[:,d,4,:AUDITS],d) for d in range(T)],axis=1)
        self.action = u[:,:,5,:3]
        self.retain = u[:,:,5,3:6]
        self.rank = u[:,:,5,6:9]
        self.gateway = u[:,:,5,9:12]
        self.native = (u[:,:,5,12:15]*K).astype(int)
        self.label_noise = u[:,:,5,15:18]<.05


def simulate(w, mask=13, allocation="margin", policy="fixed", lag=2, fee=FEE, period=4, window=(0,T), redirect=True):
    n=w.n
    ids=np.arange(n)
    lane=np.arange(3)
    shared=w.initial.copy()
    local=np.full((n,3,K),.5)
    frozen=np.broadcast_to(shared[:,None,:],local.shape).copy()
    mode=np.broadcast_to(((mask // (3**lane))%3),(n,3)).copy()
    age=np.zeros((n,3))
    
    pending={}
    outputs={k:np.zeros(n) for k in ("cash","jobs","audits","updates","switches","copied","retired","opened","native_incidents")}
    for t in range(T):
        live=np.broadcast_to(shared[:,None,:],local.shape)
        if window[0]<=t<window[1] and t%period==0 and t+lag<T and policy!="fixed":
            if policy in ("rotation","rotation_pinned"):
                j=np.full(n,(t//period)%3)
            else:
                disagreement=np.mean(np.abs(live-frozen)+np.abs(live-local),axis=2)
                priority=VALUE*(age+1)*(disagreement+.08)
                j=np.argmax(priority,axis=1)
            fam=w.panel[:,t]
            actual=w.target[ids[:,None],t,j[:,None],fam]
            snapshot=shared.copy()
            choices=np.stack((local[ids,j],shared,frozen[ids,j]),axis=1)
            probs=np.take_along_axis(choices,fam[:,None,:],axis=2)
            score=np.where(actual[:,None,:],probs,1-probs).mean(axis=2)
            # Persist the incumbent on a tie. A prior checkpoint can be restored.
            score[ids,mode[ids,j]]+=1e-9
            selection=np.argmax(score,axis=1)
            pending[t+lag]=(j,selection,snapshot,frozen[ids,j].copy())
            outputs["audits"]+=1
            outputs["cash"]-=fee
            age[ids,j]=0
        if t in pending:
            j,s,snap,old_checkpoint=pending.pop(t)
            old=mode[ids,j].copy()
            if policy in ("versioned","rotation_pinned"):
                # The audit certifies the sampled release. Install its exact parameters.
                copy=s==1
                frozen[ids[copy],j[copy]]=snap[copy]
                restore=s==2
                frozen[ids[restore],j[restore]]=old_checkpoint[restore]
                s=np.where(copy,2,s)
                outputs["copied"]+=copy
            outputs["switches"]+=old!=s
            outputs["retired"]+=(old!=0)&(s==0)
            outputs["opened"]+=(old==0)&(s!=0)
            mode[ids,j]=s
        age+=1
        head=np.where(mode[:,:,None]==0,local,np.where(mode[:,:,None]==1,live,frozen))
        fam=w.orders[:,t]
        p=head[ids[:,None],lane,fam]
        correct=(w.action[:,t]<p)==w.target[ids[:,None],t,lane,fam]
        # All three lanes require a digital release, whose case-dependent quality is given.
        released=w.gateway[:,t] < np.where(fam%4==0,.75,.96)
        paid=correct & released
        outputs["jobs"]+=paid.sum(axis=1)
        outputs["cash"]+=paid@VALUE
        # One post-training slot. Scope admits fewer cases from mobile than desk or arm.
        allowed=(~paid)&(w.retain[:,t]<np.array([1.,.8,.45]))
        priority=w.rank[:,t] if allocation=="uniform" else VALUE+w.rank[:,t]
        pick=np.argmax(np.where(allowed,priority,-1),axis=1)
        ix=ids[allowed.any(axis=1)]
        j=pick[ix]
        k=fam[ix,j]
        y=w.source[ix,t,k]^w.label_noise[ix,t,j]
        private=(mode[ix,j]==0) & redirect
        outputs["native_incidents"][ix[private]]+=1
        si,sk=ix[~private],k[~private]
        shared[si,sk]+=.6*(y[~private]-shared[si,sk])
        li,lj,lk=ix[private],j[private],k[private]
        label=w.target[li,t,lj,lk]^w.label_noise[li,t,lj]
        local[li,lj,lk]+=.6*(label-local[li,lj,lk])
        outputs["updates"][ix]+=1
        outputs["cash"][ix]-=.30
        # Each lane independently receives one local calibration every fifth shift.
        if t%5==4:
            k=w.native[:,t]
            y=w.target[ids[:,None],t,lane,k]^w.label_noise[:,t]
            prior=local[ids[:,None],lane,k]
            local[ids[:,None],lane,k]=prior+.65*(y-prior)
            outputs["cash"]-=.9
    final=np.where(mode[:,:,None]==0,local,np.where(mode[:,:,None]==1,shared[:,None,:],frozen))
    capability=np.where(w.target[:,-1],final,1-final).mean(axis=2)
    for j,name in enumerate(LANES):
        outputs[name]=capability[:,j]
    return outputs


def contrast(x,y):
    d=x-y
    m=d.mean()
    h=1.96*d.std(ddof=1)/np.sqrt(len(d))
    return [round(float(a),4) for a in (m,m-h,m+h)]


def fee_break_even(policy, fixed):
    audits=policy["audits"].mean()
    return round(float(FEE+(policy["cash"]-fixed["cash"]).mean()/audits),4) if audits else None


def study():
    train=World(range(200,248),"drift")
    candidates=list(product(range(27),("uniform","margin")))
    calibration={c:simulate(train,*c)["cash"].mean() for c in candidates}
    best=max(calibration,key=calibration.get)
    live_best=max((c for c in candidates if all((c[0]//3**j)%3<2 for j in range(3))),key=calibration.get)
    adaptive={}
    for policy in ("rotation","priority","versioned"):
        adaptive[policy]=max((2,4,8),key=lambda h:simulate(train,*best,policy=policy,period=h)["cash"].mean())
    windows=[(0,0),(0,T),(0,20),(20,40),(40,T),(20,T)]
    window=max(windows,key=lambda b:simulate(train,*best,policy="versioned",period=adaptive["versioned"],window=b)["cash"].mean())
    results={"selected_window":window,"calibration_worlds":48,"evaluation_worlds":192,"fixed_mask":best[0],
             "fixed_modes":[MODES[(best[0]//3**j)%3] for j in range(3)],"allocation":best[1],"periods":adaptive,"regimes":{}}
    for regime,lag in (("stable",2),("drift",2),("reversal",2),("reversal",7),("late",2)):
        w=World(range(7200,7392),regime)
        runs={"fixed":simulate(w,*best),"fixed_without_checkpoint":simulate(w,*live_best),"local":simulate(w,0,best[1])}
        for policy,h in adaptive.items():
            runs[policy]=simulate(w,*best,policy=policy,lag=lag,period=h)
        # Exact same count, dates, delay and fee as versioned. Only link priority changes.
        # Rotation also pins the validated release in this controlled comparison.
        runs["rotation_pinned"]=simulate(w,*best,policy="rotation_pinned",lag=lag,period=adaptive["versioned"])
        runs["live_matched"]=simulate(w,*best,policy="priority",lag=lag,period=adaptive["versioned"])
        runs["window_pinned"]=simulate(w,*best,policy="versioned",lag=lag,period=adaptive["versioned"],window=window)
        runs["no_redirection"]=simulate(w,*best,policy="versioned",lag=lag,period=adaptive["versioned"],redirect=False)
        summaries={k:{m:round(float(v.mean()),4) for m,v in out.items()} for k,out in runs.items()}
        comp={k:{m:contrast(runs["versioned"][m],row[m]) for m in row} for k,row in runs.items() if k!="versioned"}
        window_diff=contrast(runs["window_pinned"]["cash"],runs["fixed"]["cash"])
        fee_ceiling=fee_break_even(runs["versioned"],runs["fixed"])
        results["regimes"][regime+"_lag"+str(lag)]={"means":summaries,"pinned_selective_minus":comp, "window_minus_fixed_cash":window_diff, "break_even_audit_fee":fee_ceiling}
    return results


if __name__=="__main__":
    Path(__file__).with_name("results.json").write_text(json.dumps(study(),indent=2)+"\n")
