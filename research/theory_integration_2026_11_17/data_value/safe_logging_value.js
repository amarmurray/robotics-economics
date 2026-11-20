'use strict';
// Finite exact eighth-unit Nov22 identification/EVSI check; synthetic, not robotics field evidence.
const runAudit = function runAudit(){
  let assertions=0;
  const verify=(c,m)=>{assertions++;if(!c)throw new Error(m);};
  // All amounts are integer eighths of a normalized whole-cluster contribution unit.
  const R=16,E=18,G_L=24, H_min=0,H_max=40;
  const policyG=(h)=>{verify(h>=H_min&&h<=H_max,"invalid H");return (G_L+h)/2;};
  let count=0,rankG=0,rankE=0,ties=0;
  for(let h=0;h<=40;h+=2){
    const g=policyG(h), preferred=Math.max(R,E,g);
    verify(Number.isInteger(g),"noninteger eighth ticks");
    verify(g>=12&&g<=32,"sharp bounds");
    verify(preferred===(g>18?g:18),"selected payoff");
    if(g>18)rankG++;else if(g===18)ties++;else rankE++;
    count++;
  }
  verify(count===21,"case count");
  verify(rankG===14&&rankE===6&&ties===1,"rank partition");
  const world0=policyG(H_min),world1=policyG(H_max);
  verify(world0===12&&world1===32,"two completions");
  const priorG=(world0+world1)/2;
  verify(priorG===22,"prior");
  const before=Math.max(R,E,priorG),after=(Math.max(R,E,world0)+Math.max(R,E,world1))/2;
  verify(before===22&&after===25,"optimized before-after");
  verify(after-before===3,"information value");
  verify((G_L+H_min)/2===12&&(G_L+H_max)/2===32,"sharp endpoints");
  return {synthetic_only:true,unit:"one eighth normalized contribution",physical_trial:false,original_customer_data:false,qualified_safe_X:false,original_strata:["L","H"],weights:["1/2","1/2"],logged_G_L:"3",unlogged_G_H_bounds:["0","5"],identified_G_value_bounds:["3/2","4"],incumbent_R:"2",embodiment_E:"9/4",G_world_values:["3/2","4"],equal_world_prior:"1/2",pre_audit_optimized_value:"11/4",post_audit_optimized_expected_value:"25/8",gross_audit_value:"3/8",scan:{H_grid_step:"1/4",H_grid_points:count,G_preferred:rankG,E_preferred:rankE,ties},assertions};
};
if (typeof module !== 'undefined') module.exports = {runAudit};
if (typeof require !== 'undefined' && require.main === module) process.stdout.write(JSON.stringify(runAudit(), null, 2)+'\n');
