"use strict";
// All values are numerator units of 1/20 captured full-network contribution.
// This is an intentionally synthetic two-type exercise, not field calibration.
function stageScreeningAudit() {
  const states = [
    {name:"easy", q0:0, q1:1, ground:1, body:0},
    {name:"hard", q0:0, q1:0, ground:0, body:1}
  ];
  const w=40, groundCost=8, bodyCost=14, sourceCost=6; // 2, .4, .7, .3
  let checks=0;
  function eq(actual,expected,label) {
    if (actual !== expected) throw new Error(label+": "+actual+" != "+expected);
    checks++;
  }
  const sum=(xs)=>xs.reduce((a,b)=>a+b,0);
  // Expected value for the equiprobable two-type population; 20 units = 1.
  function initial(x) { return sum(states.map(z=>w*z["q"+x]))/2; }
  function incremental(x,action,cg=groundCost,ch=bodyCost) {
    const cost=action==="ground"?cg:ch;
    return sum(states.map(z=>(1-z["q"+x])*(w*z[action]-cost)))/2;
  }
  function best(x,cg=groundCost,ch=bodyCost) {
    const acts=["skip","ground","body"];
    const gains=[0,incremental(x,"ground",cg,ch),incremental(x,"body",cg,ch)];
    const max=Math.max(...gains);
    return {max,act:acts[gains.indexOf(max)]};
  }
  eq(initial(0),0,"old initial");
  eq(initial(1),20,"new initial");
  eq(incremental(0,"ground"),12,"old grounding ex ante");
  eq(incremental(0,"body"),6,"old body ex ante");
  eq(incremental(1,"ground"),-4,"new grounding ex ante");
  eq(incremental(1,"body"),13,"new body ex ante");
  eq(best(0).max,12,"old best");
  eq(best(1).max,13,"new second stage best");
  eq(initial(1)+best(1).max,33,"gross improved source policy");
  eq(initial(1)+best(1).max-sourceCost,27,"net improved source policy");
  eq((w*states[0].ground-groundCost)-(w*states[0].body-bodyCost),46,"removed easies ground-body");
  eq((w*states[1].ground-groundCost)-(w*states[1].body-bodyCost),-34,"remaining hards ground-body");
  eq((46-34)/2,6,"old ground-body ranking");
  eq(-34<0,true,"new ranking reversed");
  // Without the source screen, a perfect pre-choice type diagnostic allows type-specific actions.
  const diagnostic=sum(states.map(z=>Math.max(0,w*z.ground-groundCost,w*z.body-bodyCost)))/2;
  eq(diagnostic,29,"perfect diagnostic policy");
  eq(diagnostic > initial(1)+best(1).max-sourceCost,true,"diagnostic reverses source net ranking");
  // If more source data are optional and free, old controller/policy stays available.
  eq(Math.max(initial(0)+best(0).max,initial(1)+best(1).max),33,"option monotonicity");
  // Nested-failure composition: delta_old = (pi_new*delta_new + pi_removed*delta_removed)/pi_old.
  // Equal masses 1/2; conditional values in twentieth units.
  eq(((-8)+32)/2,12,"grounding selection identity");
  eq(((26)+(-14))/2,6,"body selection identity");
  // Exhaust the sign-reversal criterion for permitted nonnegative stage-two costs.
  let gridCases=0, reversals=0;
  for (let cg=0;cg<=40;cg++) for(let ch=0;ch<=40;ch++) {
    let removed=(w-cg)-(-ch);
    let retained=(-cg)-(w-ch);
    let oldDelta=(removed+retained)/2;
    let newDelta=retained;
    let oldActual=incremental(0,"ground",cg,ch)-incremental(0,"body",cg,ch);
    let newActual=incremental(1,"ground",cg,ch)-incremental(1,"body",cg,ch);
    eq(oldActual,oldDelta,"old decomposition on grid");
    eq(newActual,newDelta/2,"new decomposition on grid");
    eq(oldActual > 0 && newActual < 0, removed > -retained && retained < 0,"reversal iff inequality");
    if(oldActual>0 && newActual<0) reversals++;
    gridCases++;
  }
  return {
    units:"1/20 of hypothetical full-network captured contribution",
    initial:{old:0,moreSource:20},
    secondStage:{old:{ground:12,body:6,best:best(0)},moreSource:{ground:-4,body:13,best:best(1)}},
    policyGainOverRetainedOld:{oldSourceBest:12,moreSourceBestBeforeSourceCost:33,moreSourceBestAfterSourceCost:27,perfectTypeDiagnosticWithoutMoreSource:29},
    conditionalPerFailure:{oldGround:12,oldBody:6,newGround:-8,newBody:26},
    screeningRanking:{removedEasyGroundMinusBody:46,remainingHardGroundMinusBody:-34},
    checks,gridCases,reversals,
    evidence_status:"synthetic algebra only; no customer data, signed safety approval or learned model test"
  };
}
if (typeof module!=="undefined") {
  module.exports=stageScreeningAudit;
  if (require.main===module) process.stdout.write(JSON.stringify(stageScreeningAudit(),null,2)+"\n");
}
stageScreeningAudit();
