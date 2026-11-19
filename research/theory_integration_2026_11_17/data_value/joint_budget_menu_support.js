"use strict";
/* Joint eligible-procurement budgets and qualified robot production, exact integer ticks.
   Synthetic countermodels only; algebraic derivations are in JOINT_BUDGET_MENU_SUPPORT.md.
   Node 18+; run: node joint_budget_menu_support.js */
let checks=0;
function ok(x,label){checks++;if(!x)throw Error("FAILED "+label)}
function cap(price,budget,slots,high){return high?price*Math.min(2,slots,Math.floor(budget/price)):0}
function highGross(budget,slots){
  return Math.max(...[4,5,6].map(price=>cap(price,budget,slots,true)));
}
function jointCells(N,Q,B,T){
  return {highB8:T,highB7:Q-T,lowB8:B-T,lowB7:N-Q-B+T};
}
// Each output is net policy contribution multiplied by 2*N.
// B is the fraction of parent cohorts with budget=8, Q the fraction of
// simultaneous two-order requests, T their JOINT incidence. Upfront
// costs are paid in all request states. G's "conditional" price schedule
// requires budget to be legally visible BEFORE offer and demand realization.
function values(N,Q,B,T){
  const c=jointCells(N,Q,B,T);
  if(Object.values(c).some(x=>x<0)||Q>N||B>N)throw Error("infeasible joint law");
  const X=12*Q;                                     // one slot; price 6
  const Gc=12*Q+4*T-N;                              // budget-contingent G
  const Gn=2*Math.max(6*Q,4*Q+4*T)-N;             // one precommitted G menu
  const E=2*Math.max(6*Q,4*Q+4*T)-4*N;            // extra embodied slot cost 2
  const R=4*N;                                     // reserved competent fallback 2
  return {X,Gc,Gn,E,R,deltaC:Gc-X,deltaN:Gn-X,cells:c};
}
function run(){
  const N=16;let worlds=0,pairs=0;
  for(let Q=0;Q<=N;Q++)for(let B=0;B<=N;B++){
    pairs++;
    const lo=Math.max(0,Q+B-N),hi=Math.min(Q,B);
    let observedMin=Infinity,observedMax=-Infinity;
    for(let T=lo;T<=hi;T++){
      worlds++;const v=values(N,Q,B,T);
      const c=v.cells;
      ok(Object.values(c).reduce((a,b)=>a+b,0)===N,"mass");
      ok(v.X===12*Q,"X");
      ok(v.Gc-v.X===4*T-N,"contingent difference");
      ok(v.Gn-v.X===2*Math.max(0,4*T-2*Q)-N,"fixed menu difference");
      ok(v.Gc>=v.Gn,"optional budget information");
      ok(v.Gc-v.Gn===4*Math.min(T,Q-T),"information gain identity");
      ok(v.E===v.Gn-3*N,"new slot fixed-cost difference");
      // Compare independent enumeration of menus for each atom of the SAME
      // joint market response law, with budget only known before offer for Gc.
      const exX2=2*(c.highB7*cap(6,7,1,true)+c.highB8*cap(6,8,1,true));
      const exGCond2=2*(c.highB7*highGross(7,2)+c.highB8*highGross(8,2))-N;
      const exGFixed2=2*Math.max(...[4,5,6].map(k=>
        c.highB7*cap(k,7,2,true)+c.highB8*cap(k,8,2,true)))-N;
      ok(v.X===exX2,"separate X enumeration");
      ok(v.Gc===exGCond2,"separate G conditional enumeration");
      ok(v.Gn===exGFixed2,"separate G fixed enumeration");
      observedMin=Math.min(observedMin,v.deltaC);
      observedMax=Math.max(observedMax,v.deltaC);
    }
    ok(observedMin===4*lo-N && observedMax===4*hi-N,"sharp Frechet paired moment");
  }
  const lo=values(16,8,8,0),hi=values(16,8,8,8),mid=values(10,5,5,3);
  ok(lo.deltaC===-16 && hi.deltaC===16,"sign reversal same marginals");
  ok(mid.deltaC===2 && mid.deltaN===-6 && mid.Gc-mid.Gn===8,"budget info reversal");
  ok(Math.max(mid.X,mid.Gc,mid.E,mid.R)-Math.max(mid.X,mid.Gn,mid.E,mid.R)===2,"whole-decision information gain is smaller");
  ok(hi.X===96 && hi.Gc===112 && hi.E===64 && hi.R===64,"budget eight normalized values");
  ok(lo.X===96 && lo.Gc===80,"budget seven normalized values");
  const report={model:"joint original-buyer procurement budget/menu/qualified resource countermodel",
    date_utc:"2026-11-19",synthetic:true,denominator:N,
    enumerated_feasible_joint_laws:worlds,marginal_pairs:pairs,exact_assertions:checks,
    same_marginals_t0:{X:"3",G_contingent:"5/2",difference:"-1/2"},
    same_marginals_t_half:{X:"3",G_contingent:"7/2",E:"2",R:"2",difference:"+1/2"},
    matched_t_three_tenths:{X:"3",G_contingent:"31/10",G_fixed_menu:"27/10",grounding_only_information_gain:"2/5",whole_decision_information_gain:"1/10"},
    conditional_gap:"2 Pr(high_request and budget8)-1/2",
    noncontingent_gap:"max(0,4 Pr(high_request and budget8)-2 Pr(high_request))-1/2",
    scope:"No source-to-qualification field measurement; no customer budget or offer data; no approval or complete CI."};
  return report;
}
if(require.main===module)process.stdout.write(JSON.stringify(run(),null,2)+"\n");
module.exports={run,values,jointCells,cap};
