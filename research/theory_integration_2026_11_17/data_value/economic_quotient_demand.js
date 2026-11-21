"use strict";
// Exact 1/16-tick arithmetic, no external dependencies; synthetic, not field robotics.
function run(){
  let checks=0;
  const eq=(a,b,msg)=>{checks++;if(a!==b)throw Error(msg+" got "+a+" expected "+b)};
  const m=16, e=12;
  const worlds=[];
  for(let p=0;p<=m;p++){
    const R=p;                    // old policy can serve original buyer A
    const SGcoarse=Math.max(p,m-p);// new licensed recipe B but no order signal
    const SGrich=m;               // matched buyer request observed pre-dispatch
    const E=Math.max(e,R);        // embodiment keeps old recipe as a lawful option
    const sourceInfoComplement=SGrich-SGcoarse-(R-R);
    // Enumerate each pure history-contingent policy (A/A,A/B,B/A,B/B).
    let best=-1;
    for(let a0=0;a0<2;a0++) for(let a1=0;a1<2;a1++){
      const value=(a0===0?p:0)+(a1===1?m-p:0);
      best=Math.max(best,value);
    }
    eq(best,m,"full-policy best");
    eq(SGcoarse,Math.max(p,m-p),"coarse menu");
    eq(sourceInfoComplement,Math.min(p,m-p),"source×demand-information cross difference");
    eq(SGcoarse>=R,true,"optional qualified recipe monotonicity");
    eq(SGrich>=SGcoarse,true,"optional demand observation monotonicity");
    eq(E>=R,true,"embodiment retains old recipe");
    eq(Math.max(R,SGcoarse),SGcoarse,"source retention");
    eq(SGrich-SGcoarse<=Math.min(p,m-p),true,"value of full customer order signal");
    worlds.push({buyerA_num:p,den:m,old_num:R,source_coarse_num:SGcoarse,source_informed_num:SGrich,embodiment_num:E,cross_num:sourceInfoComplement});
  }
  const midpoint=worlds[8];
  eq(midpoint.old_num,8,"midpoint old");
  eq(midpoint.source_coarse_num,8,"midpoint source poor information");
  eq(midpoint.source_informed_num,16,"midpoint full-information source");
  eq(midpoint.embodiment_num,12,"midpoint E");
  eq(midpoint.cross_num,8,"midpoint interaction");
  eq(midpoint.source_coarse_num-midpoint.embodiment_num,-4,"coarse inversion");
  eq(midpoint.source_informed_num-midpoint.embodiment_num,4,"true full-history winner");
  // Worst full-history reward error of C-only stage-1 model is 1/2.
  const abstractRewardA=8, abstractRewardB=8;
  let maxConditionedError=0;
  for(const z of [0,1])for(const action of [0,1]){
    const r=(z===action)?16:0;
    const estimated=action===0?abstractRewardA:abstractRewardB;
    maxConditionedError=Math.max(maxConditionedError,Math.abs(r-estimated));
  }
  eq(maxConditionedError,8,"uniform conditioned reward error");
  eq(midpoint.source_informed_num-midpoint.source_coarse_num,maxConditionedError,"one-period bound attained");
  eq((8-abstractRewardA)+(8-abstractRewardB),0,"average aggregation deceptively exact");
  return {description:"Exact synthetic two-buyer demand-conditioned licensed recipe and state abstraction counterexample",denominator:m,embodiment_success_num:e,midpoint,one_stage_uniform_reward_error_num:maxConditionedError,worlds,checks};
}
console.log(JSON.stringify(run(),null,2));
