// Run with Node 18+: node identification_hierarchy.js
const result = (function(){
"use strict";
/* Exact finite demonstration for the Nov 21 identification-hierarchy continuation.
   All reported outcomes are synthetic normalized contributions. */
function assert(cond, message){ if(!cond) throw Error(message); checks++; }
let checks = 0;
function mean2(rows, key){ return rows.reduce((s,r)=>s+r[key],0); } // numerator /2
const common = [0,1].map(u=>({R:u,S:u,G:u,SG:u}));
const parity = [0,1].map(u=>({R:u,S:1-u,G:1-u,SG:u}));
for(const z of ["R","S","G","SG"]){
 assert(mean2(common,z)===1,"common marginal "+z);
 assert(mean2(parity,z)===1,"parity marginal "+z);
}
function factorial(row){return row.SG-row.S-row.G+row.R;}
assert(common.every(row=>factorial(row)===0),"individual interaction common");
assert(factorial(parity[0])===-2 && factorial(parity[1])===2,"individual interactions parity");
assert(parity.reduce((x,row)=>x+factorial(row),0)===0,"population factorial interaction");
const possibleTypes=[];
for(let n=0;n<16;n++){
 const y=[n&1,(n>>1)&1,(n>>2)&1,(n>>3)&1];
 for(let z=0;z<4;z++){
  // Z is uniformly assigned. Exactly sum_{a} 1{a=z}Y_z/(1/4)/4=Y_z.
  const expectation=y.reduce((acc,_,a)=>acc+(a===z?y[z]:0),0);
  assert(expectation===y[z],"Horvitz-Thompson exact law");
 }
 possibleTypes.push(y);
}
const concordant=[{A:0,B:0},{A:1,B:1}];
const discordant=[{A:0,B:1},{A:1,B:0}];
function pair(rows){return {pA_num:mean2(rows,"A"),pB_num:mean2(rows,"B"),h_num:rows.reduce((s,r)=>s+r.A*r.B,0)};}
const c=pair(concordant),d=pair(discordant);
assert(c.pA_num===1 && c.pB_num===1 && d.pA_num===1 && d.pB_num===1,"same marginals");
assert(c.h_num===1 && d.h_num===0,"joint outcomes differ");
function SGnet(rows){return rows.reduce((s,r)=>s+12*r.A*r.B,0)/2-1;}
const netConcordant=SGnet(concordant),netDiscordant=SGnet(discordant);
assert(netConcordant===5 && netDiscordant===-1,"net program alternatives");
assert(netConcordant>4 && netDiscordant<4,"SG versus E ranking reversal");
function productiveDataNet(rows){return rows.reduce((s,r)=>s+8*r.A*r.B,0)/2-1;}
assert(productiveDataNet(concordant)===3 && productiveDataNet(discordant)===-1,"two-date joint data value");
assert(productiveDataNet(concordant)>1 && productiveDataNet(discordant)<1,"two-date choice flip");
for(let a=0;a<=2;a++) for(let b=0;b<=2;b++){
 const lo=Math.max(0,a+b-2),hi=Math.min(a,b);
 assert(lo<=hi,"Frechet feasible counts");
}
const result={
 name:"identified_program_vs_unidentified_crossworld_coupling",
 units:"normalized hypothetical contribution; every two-row law has mass 1/2 per row",
 conditional_exact:true,
 assertions:checks,
 factorial:{
  arm_mean_success:"1/2 for every R,S,G,SG in both worlds",
  population_S_G_interaction:0,
  individual_interaction_common:[0,0],
  individual_interaction_parity:[-2,2],
  within_arm_marginal_evidence_identical:true
 },
 within_SG_qualified_bundle:{
  pA:"1/2",pB:"1/2",h_concordant:"1/2",h_discordant:"0",
  contribution_if_both_qualified:12,SG_cost:1,E_net:4,
  SG_net_concordant:netConcordant,SG_net_discordant:netDiscordant,
  ordering_concordant:"SG > E",ordering_discordant:"E > SG"
 },
 endogenous_productive_data:{
  marginal_rights_cleared_data:"1/2",marginal_future_qualified_sale:"1/2",
  joint_good_world:"1/2",joint_bad_world:"0",
  gross_if_both:8,data_policy_cost:1,alternative_net:1,
  data_program_net_good:productiveDataNet(concordant),
  data_program_net_bad:productiveDataNet(discordant),
  caution:"This joint dependence is not a causal source-data learning effect without intervention support."
 },
 empirical_status:"No actual robot, buyer, signed operator, or admissible training intervention data.",
 novelty_status:"Established potential-outcome, missing-data and policy-evaluation identities, not independent novelty."
};
return result;
})();
process.stdout.write(JSON.stringify(result,null,2)+"\n");
