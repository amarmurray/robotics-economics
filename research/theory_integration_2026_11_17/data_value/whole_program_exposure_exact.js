'use strict';
// Complete enumeration for a synthetic original-buyer four-unit graph; no external packages.
function run(){
  const h=[[0,1],[0,1,2],[1,2,3],[2,3]], ys=[8,12,18,16],ye=[10,6,15,13],N=4,den=(20*N)**2;
  const overlap=(i,j)=>h[i].filter(v=>h[j].includes(v)).length;
  const all=[],meanSN=ys.reduce((a,b)=>a+b,0),meanEN=ye.reduce((a,b)=>a+b,0);
  const equals=(x,y,msg)=>{if(x!==y)throw new Error(msg+" "+x+" != "+y)};
  for(let mask=0;mask<16;mask++){
    const a=h.reduce((v,hi,i)=>v+((hi.every(j=>Boolean(mask&(1<<j))))?ys[i]*(2**hi.length):0),0);
    const b=h.reduce((v,hi,i)=>v+((hi.every(j=>!(mask&(1<<j))))?ye[i]*(2**hi.length):0),0);
    all.push([a,b]);
  }
  const sum=arr=>arr.reduce((x,y)=>x+y,0), nStates=all.length;
  equals(sum(all.map(x=>x[0])),nStates*meanSN,"S HT expected numerator");
  equals(sum(all.map(x=>x[1])),nStates*meanEN,"E HT expected numerator");
  const vAS=sum(all.map(x=>(x[0]-meanSN)**2))/nStates;
  const vBE=sum(all.map(x=>(x[1]-meanEN)**2))/nStates;
  const cov=sum(all.map(x=>(x[0]-meanSN)*(x[1]-meanEN)))/nStates;
  const vGap=sum(all.map(x=>(x[0]-x[1]-meanSN+meanEN)**2))/nStates;
  const fAS=sum(h.flatMap((_,i)=>h.map((__,j)=>ys[i]*ys[j]*(2**overlap(i,j)-1))));
  const fBE=sum(h.flatMap((_,i)=>h.map((__,j)=>ye[i]*ye[j]*(2**overlap(i,j)-1))));
  const fCov=-sum(h.flatMap((_,i)=>h.map((__,j)=>overlap(i,j)>0?ys[i]*ye[j]:0)));
  equals(vAS,fAS,"same-arm S variance");equals(vBE,fBE,"same-arm E variance");equals(cov,fCov,"cross-arm covariance");equals(vGap,vAS+vBE-2*cov,"contrast variance");
  equals(meanSN,54,"SG mean numerator");equals(meanEN,44,"E mean numerator");
  equals(vGap,17892,"gap variance numerator");
  const M=Math.max(...h.map((_,i)=>h.filter((__,j)=>overlap(i,j)>0).length)),degree=Math.max(...h.map(x=>x.length));
  const upper=M/N*(2**degree+2**degree);
  if(vGap/den>upper)throw new Error("variance bound");
  const global=n=>2/(2**n), probabilities=[4,10,20].map(n=>({N:n,probability_any_full_network_exposure:global(n),mean_assignments_until_either_full_regime:1/global(n)}));
  // If site 0 truly needs site 1 to qualify, but investigator observes only own assignment.
  let observed=0;for(let m=0;m<4;m++){let z0=m&1,z1=m&2;let y=z0&&z1?1:0;observed+=z0?2*y:0}
  equals(observed,2,"omitted-edge HT numerator across four assignments");
  return {kind:"synthetic_fixed_potential_outcomes_not_robotics_evidence",probability_SG:0.5,N,neighborhoods_zero_based:h,paid_contribution_units:"integer/20 per originally registered buyer unit; net program costs excluded from random variable",SG_numerators_over_20:ys,E_numerators_over_20:ye,mean_SG:"27/40",mean_E:"11/20",mean_gap:"1/8",variance_SG:"2127/1600",variance_E:"129/160",covariance_SG_E:"-33/100",variance_gap:"4473/1600",conservative_variance_bound:upper,overlapping_neighborhoods_max:M,neighborhood_size_max:degree,assignment_states:nStates,global_case:probabilities,omitted_edge_example:{true_full_SG_mean:"1/2",misidentified_own_only_HT_expected_mean:"1/4"},exact_integer_assertions:10};
}
console.log(JSON.stringify(run(), null, 2));
