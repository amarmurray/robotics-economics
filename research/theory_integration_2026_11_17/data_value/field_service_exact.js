function run(){
 let checks=0,smallCases=0; const ok=x=>{if(!x)throw Error("check "+checks);checks++};
 const N=6561,A=5157,S=4690,B=4447,plan=24+1246,nonattempt=41+93+plan;
 ok(N===A+nonattempt);ok(A===S+467);ok(N===S+1871);ok(plan===1270);ok(S-B===243);
 const interval=(n,a,b,h)=>{const j=Math.max(0,a+b-n),gain=b-j,loss=a-j;return [Math.max(0,h-(n-gain))-Math.min(h,loss),Math.min(h,gain)-Math.max(0,h-(n-loss))]};
 for(let n=1;n<=9;n++)for(let a=0;a<=n;a++)for(let b=0;b<=n;b++)for(let h=0;h<=n;h++){
  let lo=Infinity,hi=-Infinity;for(let j=Math.max(0,a+b-n);j<=Math.min(a,b);j++){
   const gain=b-j,loss=a-j,zero=n-gain-loss;
   for(let x=0;x<=gain;x++)for(let y=0;y<=loss;y++){const z=h-x-y;if(z<0||z>zero)continue;lo=Math.min(lo,x-y);hi=Math.max(hi,x-y);}
  }const [l,u]=interval(n,a,b,h);ok(l===lo);ok(u===hi);smallCases++;
 }
 const overlap=[Math.max(0,B+S-A),Math.min(B,S)];ok(overlap[0]===3980);ok(overlap[1]===4447);
 ok(B-overlap[0]===467);ok(S-overlap[0]===710);
 const example=interval(A,B,S,467);ok(example[0]===-467);ok(example[1]===467);const all=interval(A,B,S,A);ok(all[0]===243&&all[1]===243);
 const rows=[[333,4403,261908,149250,112658],[334,43825,353273,146845,206428],[335,2862,103591,51913,51678]];
 for(const [id,u,q,i,v] of rows){ok(i+v===q);ok(u<=i);ok(u/q>=0&&u/q<=1);}
 // Retain reported inconsistent count; do not silently repair.
 const robin0=84718/89162,robin1=1-3427/90127;
 ok(84718+4444===89162);ok(87700+3427-90127===1000);ok(Math.round(robin1*10000)===9620);ok(robin1>robin0);ok(335226+59646===394872);ok(34715+6673===41388);
 return {checks,smallCases,observed_technical:{vulcan:{assigned:N,attempts:A,success:S,no_adaptation_reported:B,planning_rejections:plan,nonattempt,attempt_success:S/A,assigned_success:S/N,reported_adaptation_delta_assigned:(S-B)/N,restricted_planning_ceiling:plan/N,restricted_execution_ceiling:(A-S)/N,conditional_joint_overlap:overlap,conditional_gains:[243,710],conditional_losses:[0,467],conditional_common_eligibility_467:example},robin:{baseline_success:robin0,learned_success_implied_by_failure_and_total_only:robin1,reported_success_count:87700,reported_failed:3427,reported_total:90127,count_inconsistency:1000,conditional_rate_difference:robin1-robin0,training_n:394872,replaced_n:41388,replacement_share:41388/394872}},historical_bea:rows.map(([industry,use,output,intermediate,value_added])=>({commodity:334,industry,use_million:use,output_million:output,intermediate,value_added,direct_use_per_dollar:use/output})),field_economic_calibration:false,conditional_bounds_not_observed_effects:true,full_repository_ci:false};
}
console.log(JSON.stringify(run(),null,2));
