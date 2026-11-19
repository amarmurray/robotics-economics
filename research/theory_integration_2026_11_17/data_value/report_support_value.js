"use strict";
// Standalone reproducible integer model: node report_support_value.js
const compute=function compute(){
 const p={F:{h:0,l:0},S:{h:3,l:3},G:{h:12,l:-4},T:{h:16,l:-24}};const names=Object.keys(p);let checks=0;
 function ok(v,s){checks++;if(!v)throw Error("assert: "+s)}
 // All payoffs in quarters; equal high/low states, conditional row numerators over 5.
 function V(a,b,h,l){return h*p[a].h+(5-h)*p[b].h+l*p[a].l+(5-l)*p[b].l}
 function L(a,b){return 3*p[a].h+2*p[b].h+5*Math.min(p[a].l,p[b].l)}
 const rules=[];for(const a of names)for(const b of names)rules.push({after_h:a,after_l:b,robust40:L(a,b),known40:V(a,b,3,2)});
 const top=(field)=>rules.reduce((m,x)=>x[field]>m[field]?x:m,rules[0]);
 const robust=top("robust40"),known=top("known40");
 ok(robust.robust40===40&&robust.after_h==="G"&&robust.after_l==="G","robust G");
 ok(known.known40===43&&known.after_h==="G"&&known.after_l==="S","certified GS");
 ok(L("G","S")===22&&V("G","S",3,2)===43,"conditional GS");
 for(const q of rules){ok(q.robust40===Math.min(...[0,1,2,3,4,5].map(x=>V(q.after_h,q.after_l,3,x))),"row extreme");ok(V(q.after_h,q.after_l,3,3)<=40,"uninformative bound");ok(q.robust40<=q.known40,"row cert monotone")}
 function world(h,l){const e=rules.map(q=>({p:[q.after_h,q.after_l],v:V(q.after_h,q.after_l,h,l)}));e.sort((x,y)=>y.v-x.v);return {conditional_report_high_numerators_over_5:[h,l],pooled_accuracy_numerator_over_10:h+5-l,optimal_value_over_40:e[0].v,optimal_rule:e[0].p}}
 const w=[world(1,0),world(5,4),world(3,2)];
 ok(w.every(x=>x.pooled_accuracy_numerator_over_10===6),"pooled accuracy equal");
 ok(w[0].optimal_value_over_40===44&&w[0].optimal_rule.join(":")==="T:G","world one");
 ok(w[1].optimal_value_over_40===47&&w[1].optimal_rule.join(":")==="G:S","world two");
 ok(w[2].optimal_value_over_40===43&&w[2].optimal_rule.join(":")==="G:S","world three");
 ok(known.known40-robust.robust40===3,"certificate increment");
 return {model:"exact synthetic whole-network service; units 1/40",condition:"target high pre-action state report-high row 3/5 known, target low row completely unknown",robust_policy:[robust.after_h,robust.after_l],robust_value_over_40:robust.robust40,certified_low_state_report_high_2_over_5_policy:[known.after_h,known.after_l],certified_value_over_40:known.known40,certificate_increase_over_40:known.known40-robust.robust40,GS_uncertified_floor_over_40:L("G","S"),equal_pooled_accuracy_worlds:w,enumerated_rules:rules.length,assertions:checks,not_observed:["robot qualification","whole customer order/captured value","physically approved shadow reporter","finite-sample calibration","numeric BLS-BEA crosswalk"]};
};
if(typeof module!=="undefined"&&require.main===module)console.log(JSON.stringify(compute(),null,2));
module.exports={compute};
