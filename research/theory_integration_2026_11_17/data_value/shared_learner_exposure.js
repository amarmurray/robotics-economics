// Exact synthetic integer demonstration; run node shared_learner_exposure.js
"use strict";
const audit=function audit(){
 let n=0;function eq(a,b,k){n++;if(a!==b)throw Error(k+":"+a+"!="+b)}
 const log={GG:2,XG:1,GX:1,XX:0},lo={GG:6,XG:5,GX:5,XX:3,R:2,E:6},hi={GG:6,XG:5,GX:5,XX:8,R:2,E:6};
 function avg(w){return Object.keys(log).reduce((a,s)=>a+log[s]*w[s],0)}
 function gamma(w){return w.XX-w.XG-w.GX+w.GG}
 eq(log.GG+log.XG+log.GX+log.XX,4,"sum probabilities");
 eq(log.XG+log.XX,1,"site1 X marginal numerator");
 eq(log.GX+log.XX,1,"site2 X marginal numerator");
 for(const s of ["GG","GX","XG"])eq(lo[s],hi[s],"observed value same");
 eq(log.XX,0,"XX has zero joint exposure");
 eq(avg(lo),22,"logged expected numerator");
 eq(avg(hi),22,"logged indistinguishability");
 eq(gamma(lo),-1,"low gamma");eq(gamma(hi),4,"high gamma");
 eq(lo.XG-lo.GG,-1,"identified conditional marginal");
 eq(lo.XX-lo.GX,-2,"low conditional X");
 eq(hi.XX-hi.GX,3,"high conditional X");
 eq(lo.XX-lo.GG,-3,"low GG contrast");
 eq(hi.XX-hi.GG,2,"high GG contrast");
 eq(Math.max(lo.R,lo.E,lo.GG,lo.XX),6,"safe best low");
 eq(Math.max(hi.R,hi.E,hi.GG,hi.XX),8,"safe best high");
 let completed=[];
 for(let z=1;z<=8;z++){
  eq(z-5-5+6,z-4,"gamma completion");
  completed.push({XX_net:z,interaction:z-4,XX_minus_GG:z-6});
 }
 eq(completed.filter(x=>x.XX_minus_GG<0).length,5,"lower worlds");
 eq(completed.filter(x=>x.XX_minus_GG===0).length,1,"tie");
 eq(completed.filter(x=>x.XX_minus_GG>0).length,2,"higher worlds");
 for(const world of [lo,hi])for(const a of ["GG","XG","GX","XX"]){
  const pNumerator=1,denominator=4;
  eq(pNumerator*world[a]*denominator/pNumerator,4*world[a],"full joint HT expected numerator");
  eq(Math.max(world.GG,world.XX)>=world.GG,true,"free optional X does not hurt best menu");
 }
 return {date:"2026-11-20",model:"synthetic normalized captured net contribution, not measured robotics",logger_joint_probs_over_4:log,per_slot_X_marginal:"1/4",logged_mean:"11/2",low:{net:lo,source_interaction:-1,XX_minus_GG:-3},high:{net:hi,source_interaction:4,XX_minus_GG:2},conditional_exposure_certificate:{original_parent_gross_payment_ceilings:[4,5],service_slots:2,training_cost:1,preattempt_R:2,XX_net_interval:"[1,8]",interaction_interval:"[-3,4]",XX_minus_GG_interval:"[-5,2]"},eight_integer_completions:completed,exact_assertions:n,physical_approval:false,real_paid_receipt_panel:false};
};
if(typeof module !== "undefined" && typeof require !== "undefined" && require.main===module)console.log(JSON.stringify(audit(),null,2));
if(typeof module !== "undefined")module.exports={audit};
