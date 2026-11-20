'use strict';

// Conditional finite whole-network robust retry game; NOT a robot safety case.

function winningSets(states, safe, oldActions, goals, horizon) {
  const S=new Set(states), good=new Set(safe), goal=new Set(goals);
  if(![...goal].every(x=>S.has(x)&&good.has(x)))throw Error("invalid goal");
  const out=[new Set(goal)];
  for(let t=1;t<=horizon;t++){
    const w=new Set(out[t-1]);
    for(const s of S){
      if(!good.has(s))continue;
      for(const succ of Object.values(oldActions[s]||{})){
        if(!Array.isArray(succ)||succ.length===0)continue;
        if(succ.every(q=>S.has(q)&&good.has(q)&&out[t-1].has(q))){w.add(s);break}
      }
    }
    out.push(w)
  }
  return out;
}

function gateProbe(probeOutcomes,winning,safe,steps){
  if(steps<1||!Array.isArray(probeOutcomes)||!probeOutcomes.length)return false;
  const prior=winning[steps-1],good=new Set(safe);
  return probeOutcomes.every(x=>good.has(x)&&prior.has(x));
}

function diagnosticFixture(mode){
  const states=["initial","done","retry","blocked","expired","fault"];
  const safe=states.filter(x=>x!=="fault");
  const oldActions={initial:{serve:["done"]},retry:{serve:["done"]}};
  const probes={certified:["done","retry"],operatorLeak:["done","retry","blocked"],deadlineLeak:["done","retry","expired"],unsafeLeak:["done","fault"],alwaysWin:["done"]};
  return {states,safe,oldActions,probes,steps:2,goal:["done"],mode}
}

function runChecks(){
  let checks=0;
  const check=(v,msg)=>{checks++;if(!v)throw Error("FAILED "+msg)};
  const f=diagnosticFixture("demo"), W=winningSets(f.states,f.safe,f.oldActions,f.goal,2);
  check(W[0].has("done")&&!W[0].has("retry"),"terminal");
  check(W[1].has("initial")&&W[1].has("retry"),"old step");
  check(!W[2].has("blocked")&&!W[2].has("expired")&&!W[2].has("fault"),"failed recovery");
  for(const key of Object.keys(f.probes)){check(gateProbe(f.probes[key],W,f.safe,2)===(key==="certified"||key==="alwaysWin"),"gate "+key)}
  const candidates=["done","retry","blocked","expired","fault"];
  let subsets=0,certified=0;
  for(let mask=1;mask<(1<<candidates.length);mask++){
    const sub=candidates.filter((_,i)=>mask&(1<<i));
    const accepted=gateProbe(sub,W,f.safe,2);
    const byDefinition=sub.every(s=>s==="done"||s==="retry");
    check(accepted===byDefinition,"subset "+mask);
    subsets++;if(accepted)certified++;
  }
  const oldActions2={initial:{serve:["done"]},retry:{serve:["done"],wait:["retry"]}};
  const W2=winningSets(f.states,f.safe,oldActions2,f.goal,3);
  for(let i=0;i<3;i++){for(const s of W2[i])check(W2[i+1].has(s),"monotone time")}
  const safe2=f.safe.filter(s=>s!=="retry"),Wbad=winningSets(f.states,safe2,f.oldActions,f.goal,2);
  check(!gateProbe(f.probes.certified,Wbad,safe2,2),"unsupported retry state");
  return {checks,reachable_by_remaining_steps:W.map(s=>[...s].sort()),probe_certifications:Object.fromEntries(Object.entries(f.probes).map(([k,v])=>[k,gateProbe(v,W,f.safe,2)])),nonempty_proposed_outcome_sets:subsets,robustly_admitted_sets:certified,interpretation:"finite toy safety game; no physical/certification evidence"};
}

if(typeof require !== 'undefined' && require.main === module){process.stdout.write(JSON.stringify(runChecks(),null,2)+'\n');}
