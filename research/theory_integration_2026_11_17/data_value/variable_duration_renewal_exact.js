"use strict";
// Conditional synthetic counterworlds: not field data or measured robot economics.
// Full tickets, job minutes, paid service deadlines and renewed original buyer orders.
const runDurationModel=function runDurationModel(){
 "use strict";
 const G=[1,1,2,2], modes=["neutral","synergy","antagonism"];
 let checks=0;
 function chk(condition,label){checks++;if(!condition)throw Error("duration model check: "+label)}
 function choose2(){const a=[];for(let i=0;i<4;i++)for(let j=i+1;j<4;j++)a.push([i,j]);return a}
 function durationK(g,k,mode){return mode==="synergy"?Math.max(1,k-1):mode==="antagonism"&&g===2?k+1:k}
 function evalWorld(longK,mode){
   let total4=0,safe4=0,onTime4=0,accepted4=0,originalRenew4=0,overlap4=0,shortShort4=0;
   let Gobs=[],Kobs=[],technical=[];
   for(let i=0;i<4;i++){
     const g=G[i],k=longK.includes(i)?2:1,kBoth=durationK(g,k,mode),completion=g+kBoth+1;
     const accepted=completion<=4?1:0,renew=completion<=3?1:0;
     const receipt=4*accepted+renew;
     chk(completion>=g+kBoth+1,"worker conservation");chk(renew<=accepted,"no fabricated renewal");
     chk(completion===g+kBoth+1,"serial queue identity");
     chk([1,2,3].includes(kBoth),"admissible remedial duration");
     chk(accepted===+(completion<=4),"accepted by deadline");
     chk(renew===+(completion<=3),"separately ordered B after early accepted A");
     total4+=receipt;
     safe4+=g===1?receipt:3;
     accepted4+=accepted;originalRenew4+=renew;onTime4+=(completion<=3?1:0);
     overlap4+=(g===2&&k===2?1:0);shortShort4+=(g===1&&k===1?1:0);
     Gobs.push(`${g}/1/1`);Kobs.push(`${k}/1/1`);technical.push("1/1");
   }
   return {longK,mode,overlap4,shortShort4,values_quarters:{R:8,P:8,G:12,K:12,E:13,GK:total4,adaptive_safe:safe4},accepted4,renewedB4:originalRenew4,onTime4,Gobs:Gobs.slice().sort(),Kobs:Kobs.slice().sort(),technical:technical.slice().sort()};
 }
 const worlds=[];
 for(const longK of choose2())for(const mode of modes)worlds.push(evalWorld(longK,mode));
 const refG=JSON.stringify(worlds[0].Gobs),refK=JSON.stringify(worlds[0].Kobs),refT=JSON.stringify(worlds[0].technical);
 for(const w of worlds){
  const z4=w.overlap4, j=w.values_quarters;
  chk(JSON.stringify(w.Gobs)===refG&&JSON.stringify(w.Kobs)===refK&&JSON.stringify(w.technical)===refT,"identical full isolated arms and paired technical qualifications");
  chk(w.shortShort4===z4,"Fréchet symmetry with half-long marginal");
  chk(z4>=0&&z4<=2,"sharp Fréchet interval");
  chk(j.G===12&&j.K===12&&j.R===8&&j.E===13,"fixed whole-program comparators");
  chk(w.renewedB4===w.onTime4,"separate buyer order iff on time");
  chk(j.GK===4*w.accepted4+w.renewedB4,"receipt conservation");
  if(w.mode==="neutral"){
   chk(j.GK===16-3*z4,"neutral duration overlap formula");
   chk(j.adaptive_safe===14+z4,"neutral adaptive rule");
   chk(j.GK-(16-4*z4)===z4,"renewal premium equals short-short coincidence");
  }
  if(w.mode==="synergy"){
   chk(j.GK===18,"duration shortening has constant payoff");
   chk(j.adaptive_safe===16,"safe policy with shortening");
  }
  if(w.mode==="antagonism"){
   chk(j.GK===8+z4,"duration elongation payoff");
   chk(j.adaptive_safe===14+z4,"robust safe rule under elongation");
  }
  chk(j.adaptive_safe>=14,"nonanticipative duration-conditioned guarantee");
  chk(j.adaptive_safe>j.E,"safe policy beats stipulated independent E");
 }
 const n=worlds.filter(w=>w.mode==="neutral"),s=worlds.filter(w=>w.mode==="synergy"),a=worlds.filter(w=>w.mode==="antagonism");
 chk(Math.min(...n.map(w=>w.values_quarters.GK))===10&&Math.max(...n.map(w=>w.values_quarters.GK))===16,"neutral sharp range");
 chk(Math.min(...a.map(w=>w.values_quarters.GK))===8&&Math.max(...a.map(w=>w.values_quarters.GK))===10,"antagonism sharp range");
 chk(s.every(w=>w.values_quarters.GK===18),"synergy sharp single point");
 chk(Math.min(...worlds.map(w=>w.values_quarters.GK))===8&&Math.max(...worlds.map(w=>w.values_quarters.GK))===18,"joint duration envelope sharp overall");
 chk(n.some(w=>w.values_quarters.GK>13)&&n.some(w=>w.values_quarters.GK<13),"neutral ranking reversal vs E");
 chk(a.every(w=>w.values_quarters.GK<13)&&s.every(w=>w.values_quarters.GK>13),"cross-program duration regime reversal");
 const out={synthetic:true,model:"one conserved worker, remedial jobs precede original A service",time_units:"integer worker minutes",receipt_units:"four equally probable original failed-customer clusters; values_quarters divide by 4",G_duration:[1,1,2,2],K_long_positions:"choose any 2 of four",single_arm_obs:{G:worlds[0].Gobs,K:worlds[0].Kobs,paired_qualification:worlds[0].technical},A_original_still_authorized:true,paid_A_deadline:4,renewal_B_requires_completion_by:3,B_is_separately_authorized:true,E_assumed:"13/4",analytical:{neutral:"J_GK=4-3z",synergy:"J_GK=9/2",antagonism:"J_GK=2+z",neutral_or_antagonism_safe:"J_safe=7/2+z",synergy_safe:"J_safe=4",z:"Pr(G duration=2,K standalone duration=2) in [0,1/2]",joint_envelope:"J_committed_GK in [2,9/2] under stipulated cross-program duration envelope",maximin_safe_lower:"7/2 > 13/4 (E)",deadline_effect:"J_neutral=4(1-z)+Pr(both short)=4-3z"},assertions:checks,worlds:worlds.map(w=>({longK:w.longK,mode:w.mode,overlap4:w.overlap4,values_quarters:w.values_quarters,accepted4:w.accepted4,renewedB4:w.renewedB4}))};
 return out;
};
if(typeof module!=="undefined"){module.exports={runDurationModel};if(require.main===module)console.log(JSON.stringify(runDurationModel(),null,2));}
