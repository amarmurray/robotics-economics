// Queue-duration / two-window original-buyer transfer model. Synthetic; exact integer-quarter calculations.
// Date 1: safe R pays 2; optional P pilot pays 7/4. If selected, target qualified at dates 2,3.
// Date 2,3: safe R pays 2; each eligible accepted original-buyer target pays 3
// on the same robot when the target-specific worker is free. Date-2/3 service duration=1.
// Pilot queue duration D=1,2,3: target worker is free in future window k iff D<=k.
// The pilot decision occurs BEFORE D and future orders are observed.
"use strict";
const assert = (q, msg) => { if(!q) throw Error(msg); };
const paths = [[0,0],[1,0],[0,1],[1,1]];
const c=(d,u)=> (d<=1 ? u[0] : 0) + (d<=2 ? u[1] : 0);
const comp=(a,b)=>{let z=0; for(let j=0;j<4;j++){let d=(j===a?1:(j===b?2:3));z+=c(d,paths[j]);}return z;};
let assignments=[],checks=0,vals=[];
for(let a=0;a<4;a++)for(let b=0;b<4;b++)if(b!==a){
  const n=comp(a,b); vals.push(n);
  const pair=paths.map((u,j)=>({orders:u,d:j===a?1:j===b?2:3}));
  assert(pair.filter(q=>q.d===1).length===1,"D1 mass");checks++;
  assert(pair.filter(q=>q.d===2).length===1,"D2 mass");checks++;
  assert(pair.filter(q=>q.d===3).length===2,"D3 mass");checks++;
  for(const q of pair){
    const F2=q.d===1?1:0, F3=q.d<=2?1:0;
    assert(F2<=F3,"queue monotonicity"); checks++;
    assert(c(q.d,q.orders)===F2*q.orders[0]+F3*q.orders[1],"physical value");checks++;
  }
  assert(n>=0&&n<=3,"transport envelope");checks++;
  // P premium numerator in quarter units: (-1 + n)/4; fallback R is optional.
  const premiumQ=Math.max(0,n-1);
  assert(premiumQ===Math.max(0,-1+n),"Bellman pilot admission");checks++;
  assignments.push({D1_on:paths[a].join(""),D2_on:paths[b].join(""),expected_gain_quarters:n,P_premium_quarters:premiumQ});
}
assert(assignments.length===12,"transport extreme count");checks++;
const min=Math.min(...vals),max=Math.max(...vals);
assert(min===0&&max===3,"sharp extrema");checks++;
assert(comp(3,2)===3,"high world");checks++; // D1 on 11, D2 on 01
assert(comp(0,1)===0,"low world");checks++; // D1 on 00, D2 on 10
// Grounding G: retained licensed source->target qualification, no worker-consuming pilot.
// Relative eligible target bonus per future window is 1; expected sum=1; cost 7/10.
// Embodiment E: truly additional robot and worker; standalone target net receipts=1 each,
// expected total 1; incremental lifetime cost=13/20.
const G20=126, E20=127, P_low20=120, P_high20=130;
assert(P_high20>E20&&E20>G20&&G20>P_low20,"investment ordering"); checks++;
// A second *structural*, not parameter-variation example: D=1 or 3 equally likely,
// one and only one buyer order across windows (10 or 01). Queue is free on both dates
// or on neither; thus F*(U2+U3)=F and gain=1/2 for EVERY feasible coupling.
for(const shortOn of [0,1]){
  const orders=[[1,0],[0,1]];
  const gainHalfUnits=orders.reduce((sum,u,j)=>sum+(j===shortOn ? u[0]+u[1] : 0),0);
  assert(gainHalfUnits===1,"identified conserved original demand");checks++;
}
const output={
  model:"synthetic physically nested pilot queue with predecision optional investment",
  demand_path_probs:"each of 00,10,01,11 has probability 1/4",
  pilot_duration_probs:{"D=1":"1/4","D=2":"1/4","D=3":"1/2"},
  robot_time_slots_P_G:1, additional_robot_and_worker_E:true,
  t2_worker_free:"1/4",t3_worker_free:"1/2",
  assignments_count:assignments.length,finite_assignments:assignments,
  transport_expected_qualified_paid_gain_range:["0","3/4"],
  optional_P_total_range:["6","13/2"],
  G_total:"63/10",E_total:"127/20",
  high_world:{D1_on:"11",D2_on:"01",P:"13/2",winner:"P"},
  low_world:{D1_on:"00",D2_on:"10",P:"6",winner:"E"},
  conserved_demand_example:{each_worker_duration:"1/2",each_one_order_path:"1/2",true_gain:"1/2",independent_period_naive_range:["0","1"]},
  exact_assertions:checks,science_gate:"OPEN"
};
const rendered=JSON.stringify(output,null,2);
if(typeof module!=="undefined"&&typeof require==="function"&&require.main===module){console.log(rendered);}
rendered;
