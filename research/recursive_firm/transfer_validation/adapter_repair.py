"""Learn the interface between a changing digital donor and two robot policies."""
from itertools import product
from pathlib import Path
import json
import numpy as np
from study import World, VALUE, T, K, contrast


def environment(seeds, regime):
    seeds=list(seeds)
    w=World(seeds,"stable" if regime=="stable" else "drift")
    n=len(seeds)
    out=np.broadcast_to(w.source[:,:,None,:],(n,T,3,K)).copy()
    draws=np.array([np.random.default_rng(105000+s).random((4,K)) for s in seeds])
    w.coin=np.stack([np.random.default_rng(210000+s).random((T,3)) for s in seeds])
    for j in (1,2):
        # Both treatments change exactly six physical action coordinates per target.
        bits=(np.arange(K)%2==0)[None,:] ^ (draws[:,j,0:1]<.5)
        if regime=="fragmented":
            bits=np.argsort(np.argsort(draws[:,j],axis=1),axis=1)<K//2
        start=16+(draws[:,0,j]*16).astype(int)
        if regime=="late": start+=18
        changed=np.arange(T)[None,:]>=start[:,None]
        if regime=="revert": changed &= np.arange(T)[None,:]<44
        if regime=="stable": changed[:]=False
        out[:,:,j]^=changed[:,:,None]&bits[:,None,:]
    w.target=out
    return w


def run(w, modes=(0,0), fraction=.5, allocation="margin", groups=2, audit="none",
        cadence=4, delay=2, fee=2., no_repair=False, keep_training=False, frozen_adapter=False, paired=False, pair_fee=.60, donor_slot=False):
    # modes: 0 local, 1 unmodified live donor, 2 repaired live donor, 3 validated snapshot.
    n=w.n
    i=np.arange(n)
    lanes=np.arange(3)
    shared=w.initial.copy()
    local=np.full((n,2,K),.5)
    odds=np.full((n,2,groups),1.1)  # modest prior for unchanged action coordinates
    saved=np.broadcast_to(shared[:,None,:],local.shape).copy()
    mode=np.tile(modes,(n,1))
    age=np.ones((n,2))
    pending={}
    stats={k:np.zeros(n) for k in ("cash","orders","audits","eligible","donor_updates",
                                    "local_updates","repair_updates","repaired_orders","retirements","installs")}
    def policies():
        aligned=1/(1+np.exp(-odds[:,:,np.arange(K)%groups]))
        live=np.broadcast_to(shared[:,None,:],local.shape)
        repaired=aligned*live+(1-aligned)*(1-live)
        if no_repair: repaired=live
        return np.stack((local,live,repaired,saved),axis=2)
    for t in range(T):
        cand=policies()
        if audit!="none" and t%cadence==0 and t+delay<T:
            if audit=="rotation": j=np.full(n,(t//cadence)%2)
            else: j=np.argmax(VALUE[1:]*(age+1)*(.1+np.abs(cand[:,:,2]-local).mean(axis=2)),axis=1)
            f=w.panel[:,t]
            y=w.target[i[:,None],t,j[:,None]+1,f]
            prob=np.take_along_axis(cand[i,j],f[:,None,:],axis=2)
            score=np.where(y[:,None],prob,1-prob).mean(axis=2)
            score[i,mode[i,j]]+=1e-8
            choice=score.argmax(axis=1)
            pending[t+delay]=(j,choice,cand[i,j,choice].copy())
            stats["audits"]+=1
            stats["cash"]-=fee
            age[i,j]=0
        if t in pending:
            j,choice,snapshot=pending.pop(t)
            old=mode[i,j].copy()
            # A positive test licenses the audited candidate release until reviewed again.
            save=choice!=0
            saved[i[save],j[save]]=snapshot[save]
            mode[i,j]=np.where(save,3,0)
            stats["retirements"]+=(old!=0)&~save
            stats["installs"]+=save
        age+=1
        cand=policies()
        heads=np.concatenate((shared[:,None],cand[i[:,None],np.arange(2),mode]),axis=1)
        f=w.orders[:,t]
        donor_prediction=shared[i[:,None],f].copy()
        prob=heads[i[:,None],lanes,f]
        ok=(w.action[:,t]<prob)==w.target[i[:,None],t,lanes,f]
        paid=ok & (w.gateway[:,t]<np.where(f%4==0,.75,.96))
        stats["cash"]+=paid@VALUE
        stats["orders"]+=paid.sum(axis=1)
        stats["repaired_orders"]+=(paid[:,1:]&(mode==2)).sum(axis=1)
        allowed=~paid & (w.retain[:,t]<np.array([1.,.8,.45]))
        stats["eligible"]+=allowed.sum(axis=1)
        if audit=="none":
            # Static raw and snapshot recipients need no native fit or adapter.
            allowed[:,1:] &= (mode==0)|(mode==2)
        ranking=w.rank[:,t]+(VALUE if allocation=="margin" else 0)
        if donor_slot:
            ii=i[allowed[:,0]]
            fc=f[ii,0]
            label=w.target[ii,t,0,fc]^w.label_noise[ii,t,0]
            shared[ii,fc]+=.6*(label-shared[ii,fc])
            stats["cash"][ii]-=.30
            stats["donor_updates"][ii]+=1
            allowed[:,0]=False
        ix=i[allowed.any(axis=1)]
        j=np.where(allowed,ranking,-1).argmax(axis=1)[ix]
        k=f[ix,j]
        y=w.target[ix,t,j,k]^w.label_noise[ix,t,j]
        stats["cash"][ix]-=.30
        donor=j==0
        shared[ix[donor],k[donor]]+=.6*(y[donor]-shared[ix[donor],k[donor]])
        stats["donor_updates"][ix[donor]]+=1
        a,b,c,label=ix[~donor],j[~donor]-1,k[~donor],y[~donor]
        # A scarce label and slot may train native specifics or the relation to the donor.
        # Following retirement, halve adapter exploration and send the rest to local learning.
        multiplier=np.where((mode[a,b]==0)&(audit!="none")&(not keep_training),.5,1.)
        adapter=(mode[a,b]==2) if audit=="none" else w.coin[a,t,b+1]<fraction*multiplier
        l,m,fam=a[~adapter],b[~adapter],c[~adapter]
        local[l,m,fam]+=.6*(label[~adapter]-local[l,m,fam])
        stats["local_updates"][l]+=1
        l,m,fam=a[adapter],b[adapter],c[adapter]
        p=donor_prediction[l,m+1]
        evidence=np.log(p/(1-p))*np.where(label[adapter],1,-1)
        idx=(l,m,fam%groups)
        if paired:
            # One additional donor annotation for the same retained demonstration.
            # The native annotation can be noisy. The additional donor label is certified.
            same=(label[adapter]==w.source[l,t,fam])
            evidence=np.where(same,1.,-1.)*np.log(.95/.05)
            stats["cash"][l]-=pair_fee
        if not frozen_adapter:
            odds[idx]=np.clip(.78*odds[idx]+evidence,-5.,5.)
        stats["repair_updates"][l]+=1
    cand=policies()
    final=cand[i[:,None],np.arange(2),mode]
    accuracy=np.where(w.target[:,-1,1:],final,1-final).mean(axis=2)
    stats["arm"],stats["mobile"]=accuracy.T
    stats["desk"]=np.where(w.target[:,-1,0],shared,1-shared).mean(axis=1)
    return stats


def study():
    train=environment(range(800,864),"coherent")
    def best(configs):
        return max(configs,key=lambda c:run(train,**c)["cash"].mean())
    configs=[dict(modes=m,allocation=a) for m,a in product(product(range(4),repeat=2),("uniform","margin"))]
    fixed=best(configs)
    local=best([c for c in configs if c["modes"]==(0,0)])
    raw=best([c for c in configs if 2 not in c["modes"]])
    repair=best([c for c in configs if 2 in c["modes"]])
    active=best([dict(modes=fixed["modes"],fraction=f,allocation=a,audit="priority",cadence=h)
                 for f,a,h in product((.25,.5,.75),("uniform","margin"),(3,6,12))])
    out={"calibration":[800,863],"evaluation":[12200,12455],"fixed":fixed,"local":local,"raw":raw,"active":active,"repair":repair,"regimes":{}}
    for regime,delay in (("coherent",2),("fragmented",2),("stable",2),("revert",2),("late",2),("revert",7)):
        w=environment(range(12200,12456),regime)
        designs={"fixed":fixed,"local":local,"raw":raw,"adaptive":active,
                 "rotation":dict(active,audit="rotation"),"no_adapter":dict(active,no_repair=True),
                 "local_spend":dict(active,fraction=0,no_repair=True),
                 "constant_training":dict(active,keep_training=True),
                 "unpooled_adapter":dict(active,groups=K),
                 "frozen_prior":dict(active,frozen_adapter=True),
                 "verified_pair":dict(active,paired=True),
                 "repair":repair,"repair_spare":dict(repair,donor_slot=True),
                 "raw_spare":dict(raw,donor_slot=True),"local_spare":dict(local,donor_slot=True),
                 "fixed_verified":dict(repair,paired=True),
                 "fixed_frozen_prior":dict(repair,frozen_adapter=True)}
        runs={k:run(w,delay=delay,**v) for k,v in designs.items()}
        out["regimes"][regime+"_lag"+str(delay)]={
            "means":{k:{m:round(float(a.mean()),5) for m,a in v.items()} for k,v in runs.items()},
            "adaptive_minus":{k:{m:contrast(runs["adaptive"][m],v[m]) for m in v}
                              for k,v in runs.items() if k!="adaptive"},
            "fixed_minus_local":contrast(runs["fixed"]["cash"],runs["local"]["cash"]),
            "fixed_minus_raw":contrast(runs["fixed"]["cash"],runs["raw"]["cash"]),
            "capacity_interaction":contrast(runs["repair_spare"]["cash"]-runs["raw_spare"]["cash"],runs["repair"]["cash"]-runs["raw"]["cash"]),
            "verified_minus_raw":contrast(runs["fixed_verified"]["cash"],runs["raw"]["cash"]),
            "repair_minus_local":contrast(runs["repair"]["cash"],runs["local"]["cash"]),
            "repair_minus_raw":contrast(runs["repair"]["cash"],runs["raw"]["cash"]),
            "repair_spare_minus_raw_spare":contrast(runs["repair_spare"]["cash"],runs["raw_spare"]["cash"]),
            "repair_spare_minus_local_spare":contrast(runs["repair_spare"]["cash"],runs["local_spare"]["cash"]),
            "repair_learning_minus_frozen":contrast(runs["repair"]["cash"],runs["fixed_frozen_prior"]["cash"]),
            "verified_minus_repair":contrast(runs["fixed_verified"]["cash"],runs["repair"]["cash"]),
            "pair_fee_ceiling":round(float(.60+(runs["fixed_verified"]["cash"]-runs["repair"]["cash"]).mean()/runs["fixed_verified"]["repair_updates"].mean()),4)}
    return out


if __name__=="__main__":
    Path(__file__).with_name("adapter_results.json").write_text(json.dumps(study(),indent=2)+"\n")
