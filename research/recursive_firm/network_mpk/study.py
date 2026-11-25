"""Generate joint marginal-product distributions and propagation ledgers from seeded worlds."""
import argparse
import csv
import json
from pathlib import Path
import numpy as np
from model import (BETA, BLOCK, FIRST_COST, LOG_DENSITY, NODES, OPTIONS, Q, ZERO,
                   Economy, draw)

ROOT = Path(__file__).resolve().parent
CALIBRATION = range(900,924)
EVALUATION = range(37100,37196)
REGIMES = ("baseline","hospital_surge","standardization","controller_drift",
           "compute_squeeze","duplicate_logs","selective_retention","late_release")
COST = np.r_[0.,FIRST_COST]
RULES = [(source,release) for source in ("none",0,1,2,3) for release in
         (("local",) if source=="none" else ("local","pooled"))]


def decisions(e, scope="open", source="optimize"):
    policies = [e.policy(k,scope,source) for k in OPTIONS]
    return policies,np.array([p.value for p in policies])-COST


def calibrate():
    scores = np.zeros((len(RULES),len(OPTIONS)))
    for seed in CALIBRATION:
        e = Economy(draw(seed))
        for r,(source,release) in enumerate(RULES):
            scores[r] += decisions(e,release,source)[1]
        e.clear()
    r,investment=np.unravel_index(scores.argmax(),scores.shape)
    return int(investment),RULES[r]


def collect(e, fixed, forecast_choice=None):
    policies,v = decisions(e)
    frozen,fv = decisions(e,source="none")
    _,local_v = decisions(e,scope="local")
    base = policies[0]
    ratio=(v[1:]+FIRST_COST-v[0])/FIRST_COST
    winner=int(v.argmax())
    frozen_choice=int(fv.argmax())
    i,(s,release)=fixed
    incumbent_value=e.policy(OPTIONS[i],release,s).value-COST[i]
    raw=base.first.attempts*(1-Q)*LOG_DENSITY
    rows=[]
    front = [e.operating(0,k,objective="physical_frontier") for k in OPTIONS]
    for i,p in enumerate(policies[1:]):
        capval = p.value-base.value
        static = p.first.profit-base.first.profit
        # No-learning counterfactual preserves the option to add another block.
        nolearn=frozen[i+1].value-frozen[0].value
        own=(p.account-base.account)[i]
        fy=front[i+1].final-front[0].final
        rows.append(dict(node=NODES[i],frontier_output_per_service=(fy/BLOCK[i]).tolist(),
                         frontier_value_per_service=float(e.world.price@fy/BLOCK[i]),
                         gross_stage_change=(p.first.gross-base.first.gross).tolist(),
                         realized_final_change=(p.first.final-base.first.final).tolist(),
                         role_hours_change=(p.first.labor-base.first.labor).tolist(),
                         next_final_change=(p.expected_final_next-base.expected_final_next).tolist(),
                         next_machine_work_change=(p.expected_auto_next-base.expected_auto_next).tolist(),
                         two_period_accounts=(p.account-base.account).tolist(),
                         spot=static, dynamic=capval, frozen=nolearn, learning_wedge=capval-nolearn,
                         own=own, others=capval-own, ratio=ratio[i], raw_volume=raw[i],
                         usable_chance=e.chance(base.first)[i], source=p.source,
                         release=p.release, base_source=base.source,
                         after_success=p.last_signal, after_miss=p.last_no_signal))
    best=policies[winner]
    return rows,dict(first_option=winner, source=best.source, release=best.release,
                raw_predicts_top=int(raw.argmax()==ratio.argmax()),
                forecast_regret=0. if forecast_choice is None else v[winner]-v[forecast_choice],
                fixed_regret=v[winner]-incumbent_value,
                price_cross_rights=v[winner]-local_v.max(),
                learning_changes_first=int(winner!=frozen_choice),
                training_changes_after_install=int(any(p.source!=base.source for p in policies[1:])),
                learning_changes_second=int(best.source>=0 and best.last_signal!=best.last_no_signal),
                learning_changes_second_probability=float(best.chance*(best.last_signal!=best.last_no_signal)),
                selected_value=v[winner],established_tech_value=fv[frozen_choice],
                option_value_learning=v[winner]-fv[frozen_choice])


def transmission(base, changed, transform):
    # Hold capital, input prices and training history fixed at date 1.
    b0,b1=base.network[1],changed.network[1]
    prior=base.operating(1,ZERO)
    source=1 if transform=="plant_release" else -1
    after=changed.operating(1,ZERO,source,"pooled")
    final=after.final-prior.final
    induced=changed.require[1]@final
    engineering=changed.require[1]@((b1-b0)@prior.gross)
    assert np.allclose(induced+engineering,after.gross-prior.gross)
    def increments(e,op,source):
        return np.array([e.operating(1,k,source,"pooled").profit-op.profit for k in OPTIONS[1:]])
    return dict(final=final,gross=after.gross-prior.gross,induced=induced,engineering=engineering,
                incidence=after.ledger-prior.ledger,net=after.profit-prior.profit,
                capital_revaluation=increments(changed,after,source)-increments(base,prior,-1),
                role_hours=after.labor-prior.labor,
                auto_share=after.machine_output/np.maximum(after.gross,1e-9)
                           -prior.machine_output/np.maximum(prior.gross,1e-9),
                upstream_falls_while_hospital_expands=int(after.gross[1]<prior.gross[1]-1e-7 and final[3]>1e-7))


def describe(values):
    a=np.asarray(values,dtype=float)
    return dict(mean=np.round(a.mean(axis=0),5).tolist(),
                p10=np.round(np.quantile(a,.10,axis=0),5).tolist(),
                p50=np.round(np.quantile(a,.50,axis=0),5).tolist(),
                p90=np.round(np.quantile(a,.90,axis=0),5).tolist())


def difference(values):
    a=np.asarray(values,dtype=float)
    mean=a.mean()
    err=1.96*a.std(ddof=1)/np.sqrt(len(a))
    return np.round([mean,mean-err,mean+err],5).tolist()


def summarize(records):
    actions=[v for _,v in records]
    samples={}
    for i,name in enumerate(NODES):
        r=[rows[i] for rows,_ in records]
        samples[name]={k:describe([row[k] for row in r]) for k in
            ("spot","dynamic","frozen","learning_wedge","own","others","ratio",
            "frontier_value_per_service","frontier_output_per_service","realized_final_change",
            "gross_stage_change","role_hours_change","next_final_change","next_machine_work_change")}
        samples[name]["profitable"]=float(np.mean([row["ratio"]>1 for row in r]))
        samples[name]["private_chain_disagree"]=float(np.mean([(row["own"]>FIRST_COST[i]) !=
                                                            (row["ratio"]>1) for row in r]))
    org={k:difference([a[k] for a in actions]) for k in ("option_value_learning","fixed_regret","forecast_regret",
               "raw_predicts_top","learning_changes_first","learning_changes_second",
               "learning_changes_second_probability","training_changes_after_install","price_cross_rights")}
    org["purchase_shares"]=[float(np.mean([a["first_option"]==i for a in actions])) for i in range(5)]
    org["cross_rights_acquisition"]={str(fee):float(np.mean([a["price_cross_rights"]>fee+1e-8 for a in actions]))
                                      for fee in (0,.5,1.,2.)}
    return dict(nodes=samples,organization=org)


def run_study():
    fixed=calibrate()
    raw={r:[] for r in REGIMES}
    propagation={r:[] for r in ("hospital_surge","standardization","compute_squeeze","plant_release","labor_remix")}
    with (ROOT/"baseline_worlds.csv").open("w",newline="") as stream:
        writer=None
        for seed in EVALUATION:
            world=draw(seed)
            base=Economy(world)
            prediction=None
            for regime in REGIMES:
                e=base if regime=="baseline" else Economy(world,regime)
                rows,actions=collect(e,fixed,prediction)
                if regime=="baseline":
                    prediction=actions["first_option"]
                    for row in rows:
                        record=dict(seed=seed,**row)
                        if writer is None:
                            writer=csv.DictWriter(stream,fieldnames=record.keys())
                            writer.writeheader()
                        writer.writerow(record)
                if regime in propagation:
                    propagation[regime].append(transmission(base,e,regime))
                raw[regime].append((rows,actions))
                if e is not base: e.clear()
            propagation["plant_release"].append(transmission(base,base,"plant_release"))
            remix=Economy(world,"labor_remix")
            propagation["labor_remix"].append(transmission(base,remix,"labor_remix"))
            remix.clear()
            base.clear()
    movement={k:{field:describe([r[field] for r in records]) for field in records[0]}
              for k,records in propagation.items()}
    return dict(calibration=[CALIBRATION.start,CALIBRATION.stop-1],evaluation=[EVALUATION.start,EVALUATION.stop-1],
                node_order=NODES, fixed_first=fixed[0],fixed_training=fixed[1],
                regimes={k:summarize(v) for k,v in raw.items()},transformations=movement)


if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("--smoke",action="store_true",help="Run a single world without writing study outputs")
    if parser.parse_args().smoke:
        rows,actions=collect(Economy(draw(7)),(0,("none","local")))
        print(actions)
    else:
        (ROOT/"results.json").write_text(json.dumps(run_study(),indent=2)+"\n")
