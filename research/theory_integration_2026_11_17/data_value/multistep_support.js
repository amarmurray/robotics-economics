"use strict";
/* Multi-step safe-support/qualified-production demonstration.
   Finite synthetic controlled kernels and a held-out joint service proxy.
   Node: node multistep_support.js
   No field data, robot training, currency or observed qualification rates.
*/
const MultiStepSupport = (() => {
  const eps=1e-12;
  const validate=(x,k)=>{if(!Number.isFinite(x)||x<0)throw RangeError(k+" must be finite and nonnegative");};
  const prob=(p,k)=>{validate(p,k);if(p>1)throw RangeError(k+" exceeds one");};
  const maxWithName=(choices)=>{
    // Stable tie-break by order; retaining an old/baseline route never becomes infeasible.
    const entries=Object.entries(choices).filter(([,v])=>v!==null);
    if(!entries.length)throw Error("empty feasible action menu");
    return entries.reduce((a,b)=>b[1]>a[1]+eps?b:a);
  };
  function solve(delta, opts={}) {
    validate(delta,"delta");
    const p0=opts.firstProgress===undefined?.5:opts.firstProgress;
    const pG=opts.targetSuccess===undefined?.75:opts.targetSuccess;
    const pE=opts.bodySuccess===undefined?.6:opts.bodySuccess;
    const r=opts.routineSecondSuccess===undefined?0:opts.routineSecondSuccess;
    for(const [k,v] of Object.entries({p0,pG,pE,r}))prob(v,k);
    const costG=opts.groundCost===undefined?.25:opts.groundCost;
    const costE=opts.bodyCost===undefined?2:opts.bodyCost;
    const specialist=opts.specialist===undefined?2:opts.specialist;
    const firstProduction=opts.firstProduction===undefined?1:opts.firstProduction;
    const routineProduction=opts.routineProduction===undefined?1:opts.routineProduction;
    for(const [k,v] of Object.entries({costG,costE,specialist,firstProduction,routineProduction}))validate(v,k);
    const withGround=opts.withGround!==false,withBody=opts.withBody!==false;
    // Action-eligible only after first routine operation; all share last slot.
    const success={routine:routineProduction+r*delta,specialist};
    const failure={routine:routineProduction,specialist};
    if(withGround)success.ground=pG*delta-costG; // only q1 has safe support
    if(withBody){success.body=pE*delta-costE;failure.body=pE*delta-costE;}
    const bestSuccess=maxWithName(success),bestFailure=maxWithName(failure);
    return {value:firstProduction+p0*bestSuccess[1]+(1-p0)*bestFailure[1],
      bestSuccess:{action:bestSuccess[0],value:bestSuccess[1]},
      bestFailure:{action:bestFailure[0],value:bestFailure[1]},
      success,failure,firstProgress:p0,delta};
  }
  function independentEventTree(delta,opts={}) {
    // Explicitly enumerate first progress events and all terminal qualification
    // events for each available last action, rather than using analytic maxima.
    const p0=opts.firstProgress===undefined?.5:opts.firstProgress;
    const g=opts.targetSuccess===undefined?.75:opts.targetSuccess;
    const e=opts.bodySuccess===undefined?.6:opts.bodySuccess;
    const r=opts.routineSecondSuccess===undefined?0:opts.routineSecondSuccess;
    const cG=opts.groundCost===undefined?.25:opts.groundCost;
    const cE=opts.bodyCost===undefined?2:opts.bodyCost;
    const sp=opts.specialist===undefined?2:opts.specialist;
    const first=opts.firstProduction===undefined?1:opts.firstProduction;
    const rp=opts.routineProduction===undefined?1:opts.routineProduction;
    let result=first,decisions={};
    for(const updated of [true,false]) {
      const weight=updated?p0:1-p0;
      const candidates=[["routine",rp,updated?r:0],["specialist",sp,0]];
      if(updated&&opts.withGround!==false)candidates.push(["ground",-cG,g]);
      if(opts.withBody!==false)candidates.push(["body",-cE,e]);
      const scored=candidates.map(([name,flow,p])=>{
        let expected=0;
        for(const [qual,probability] of [[0,1-p],[1,p]])
          expected+=probability*(flow+qual*delta);
        return {name,expected};
      }).sort((a,b)=>b.expected-a.expected);
      result+=weight*scored[0].expected;
      decisions[updated?"updated":"unupdated"]=scored[0];
    }
    return {value:result,decisions};
  }
  // Distribution over validated stages after n *routine* slots.
  function progressDistribution(initial,stageRates,slots){
    if(!Number.isInteger(initial)||initial<0||!Number.isInteger(slots)||slots<0 ||
       !Array.isArray(stageRates))throw RangeError("invalid progress dimensions");
    for(const p of stageRates)prob(p,"stage rate");
    if(initial>stageRates.length)throw RangeError("initial exceeds terminal stage");
    const K=stageRates.length;
    let mass=Array(K+1).fill(0);mass[initial]=1;
    for(let t=0;t<slots;t++){
      const next=Array(K+1).fill(0);
      for(let j=0;j<=K;j++){
        const p=j<K?stageRates[j]:0;
        next[j]+=mass[j]*(1-p);
        if(j<K)next[j+1]+=mass[j]*p;
      }
      mass=next;
    }
    return mass;
  }
  // A simple pathwise-budget safe-reachability certificate, NOT a safety validator.
  // All possible outcomes of a selected action must be explicitly marked approved.
  function reachable(graph,start,target,slots,operatorBudget,cashBudget){
    if(!Number.isInteger(slots)||slots<0)throw RangeError("slots");
    validate(operatorBudget,"operatorBudget");validate(cashBudget,"cashBudget");
    let current=[{node:start,operators:operatorBudget,cash:cashBudget}];
    for(let t=0;t<=slots;t++){
      if(current.some(x=>x.node===target))return true;
      if(t===slots)break;
      const next=[];
      for(const x of current)for(const a of (graph[x.node]||[])){
        if(a.operator>x.operators+eps || a.cash>x.cash+eps)continue;
        if(!a.outcomes.length || !a.outcomes.every(o=>o.safe && o.p>=0 && o.p<=1))continue;
        for(const out of a.outcomes)if(out.p>0)
          next.push({node:out.to,operators:x.operators-a.operator,cash:x.cash-a.cash});
      }
      current=next;
    }
    return false;
  }
  function jointLaw(){
    // Distributions in order no bundle, B only, C only, B and C.
    return {routine:[1/16,7/16,7/16,1/16],
            grounding:[7/16,1/16,1/16,7/16]};
  }
  function jointValues(displacement=4,delta=16,additive=false){
    validate(displacement,"displacement");validate(delta,"delta");
    const out={};
    for(const [name,probs] of Object.entries(jointLaw())) {
      let raw=0,bMarg=0,cMarg=0;
      probs.forEach((p,i)=>{
        const b=(i===1||i===3)?1:0,c=(i===2||i===3)?1:0;
        bMarg+=p*b;cMarg+=p*c;
        raw+=p*(additive ? (delta/2)*(b+c) : delta*b*c);
      });
      out[name]={raw,bMarg,cMarg,net:raw-(name==="grounding"?displacement:0)};
    }
    return out;
  }
  function tests(){
    let assertions=0;
    function equal(a,b,k){if(Math.abs(a-b)>1e-10)throw Error(k+" "+a+" != "+b);assertions++;}
    function yes(b,k){if(!b)throw Error(k);assertions++;}
    const z=solve(7),hi=solve(12),lo=solve(0);
    equal(z.value,23/5,"mid demand adaptive");equal(z.bestSuccess.value,5,"G success");
    equal(z.bestFailure.value,11/5,"E failure");
    yes(z.bestSuccess.action==="ground","selected after success");
    yes(z.bestFailure.action==="body","selected after failure");
    equal(hi.value,319/40,"high demand");
    equal(lo.value,3,"zero customer bundle value");
    yes(lo.bestSuccess.action==="specialist","competent first branch");
    yes(lo.bestFailure.action==="specialist","competent second branch");
    equal(solve(3).value,3,"first boundary");
    equal(solve(20/3).value,35/8,"second boundary");
    equal(solve(7,{withGround:false}).value,16/5,"no grounding");
    equal(solve(7,{withBody:false}).value,9/2,"no redesigned embodiment");
    equal(solve(7,{firstProgress:0}).value,16/5,"no first exposure");
    equal(solve(7,{routineSecondSuccess:.75}).value,
        1+.5*(1+.75*7)+.5*(.6*7-2),"free routine qualification");
    yes(solve(7,{routineSecondSuccess:.75}).bestSuccess.action==="routine",
      "routine byproduct beats target grounding");
    yes(solve(7,{routineSecondSuccess:.25}).bestSuccess.action==="ground",
      "insufficient routine coverage");
    for(const d of [0,1,3,4,6,7,20/3,8,12,30]){
      const a=solve(d),b=independentEventTree(d);
      equal(a.value,b.value,"event tree at "+d);
      yes(a.bestSuccess.action===b.decisions.updated.name,"first event decision "+d);
      yes(a.bestFailure.action===b.decisions.unupdated.name,"second event decision "+d);
    }
    for(const params of [
      {firstProgress:.2,targetSuccess:.5,bodySuccess:.9,bodyCost:1},
      {firstProgress:0,targetSuccess:.1,routineSecondSuccess:.6,withBody:false},
      {firstProgress:.8,targetSuccess:.15,bodySuccess:.8,specialist:3},
      {firstProgress:1,withGround:false,withBody:false},
      {routineSecondSuccess:.9,targetSuccess:.25,bodySuccess:0},
    ])for(const d of [0,2,10,15]){
      equal(solve(d,params).value,independentEventTree(d,params).value,
        "alternative kernel exact tree");
    }
    const p=progressDistribution(0,[.5,0],8);
    equal(p[2],0,"routine zero cut even after eight slots");
    equal(progressDistribution(0,[.5,.75],2)[2],3/8,"positive 2-slot");
    equal(progressDistribution(0,[.5,.75],3)[2],21/32,"positive 3-slot retry");
    equal(progressDistribution(0,[1,1,1],3)[3],1,"certain staged reach");
    const graph={
      start:[{operator:0,cash:0,outcomes:[{to:"q1",p:.5,safe:true},{to:"start",p:.5,safe:true}]}],
      q1:[{operator:0,cash:0,outcomes:[{to:"q1",p:1,safe:true}]},
          {operator:1,cash:.25,outcomes:[{to:"B",p:.75,safe:true},{to:"q1",p:.25,safe:true}]},
          {operator:0,cash:0,outcomes:[{to:"B",p:.5,safe:true},{to:"unsafe",p:.5,safe:false}]}],
      B:[]};
    yes(reachable(graph,"start","B",2,1,2),"ground unlocks graph");
    yes(!reachable(graph,"start","B",2,0,2),"no operator safe reach");
    yes(!reachable(graph,"start","B",1,1,2),"no one-slot B");
    const laws=jointValues();
    equal(laws.routine.bMarg,.5,"routine B marginal");
    equal(laws.routine.cMarg,.5,"routine C marginal");
    equal(laws.grounding.bMarg,.5,"grounding B marginal");
    equal(laws.grounding.cMarg,.5,"grounding C marginal");
    equal(laws.routine.net,1,"routine bundle");
    equal(laws.grounding.net,3,"grounding bundle after cost");
    equal(jointValues(4,16,true).routine.net,8,"additive routine");
    equal(jointValues(4,16,true).grounding.net,4,"additive ground");
    for(const bad of [-1,NaN,Infinity]) {
      let reject=false;try{solve(bad)}catch(e){reject=e instanceof RangeError;}yes(reject,"input");
    }
    return {assertions,independent_event_tree:true,synthetic:true,field_experiment:false};
  }
  function report(){
    return {setting:"two-slot safe-progress production and joint accepted-service value",
      atDemand0:solve(0),atDemand7:solve(7),atDemand12:solve(12),
      noGroundAt7:solve(7,{withGround:false}),
      noEmbodimentAt7:solve(7,{withBody:false}),
      productiveByproductAt7:solve(7,{routineSecondSuccess:.75}),
      jointComplement:jointValues(),jointAdditive:jointValues(4,16,true),
      limitations:"No observed robot, site acceptance, dollars, measured exposure, or risk guarantee."};
  }
  return {solve,independentEventTree,progressDistribution,reachable,jointLaw,jointValues,tests,report};
})();
if(typeof module!=="undefined"&&module.exports) {
 module.exports=MultiStepSupport;
 if(require.main===module)console.log(JSON.stringify({checks:MultiStepSupport.tests(),results:MultiStepSupport.report()},null,2));
}
