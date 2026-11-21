'use strict';

// Exact finite CPU audit; no external packages. Run: node report_value_support_bounds.js
function reportValueSupportAudit(){
  const weights=[2,1,1], probsDenom=4, deltaDenom=4;
  const intervals=[]; for(let a=-2;a<=2;a++)for(let b=a;b<=2;b++)intervals.push([a,b]);
  const value=d=>Math.min(d.reduce((s,x,i)=>s+weights[i]*Math.max(x,0),0),d.reduce((s,x,i)=>s+weights[i]*Math.max(-x,0),0));
  const analyticalLower=(a,b)=>Math.min(a.reduce((s,x,i)=>s+weights[i]*Math.max(x,0),0),b.reduce((s,x,i)=>s+weights[i]*Math.max(-x,0),0));
  const analyticalUpper=(a,b)=>{
    let v=0;
    for(let mask=0;mask<8;mask++){
      let p=0,n=0,possible=true;
      for(let i=0;i<3;i++){
        if(mask&(1<<i)){if(b[i]<0)possible=false;else p+=weights[i]*b[i]}
        else{if(a[i]>0)possible=false;else n+=weights[i]*(-a[i])}
      }
      if(possible)v=Math.max(v,Math.min(p,n));
    }
    return v;
  };
  const brute=(a,b)=>{
    let lo=Infinity,hi=-Infinity,loWitness,hiWitness;
    for(let x=a[0];x<=b[0];x++)for(let y=a[1];y<=b[1];y++)for(let z=a[2];z<=b[2];z++){
      const d=[x,y,z],v=value(d);
      if(v<lo){lo=v;loWitness=d}
      if(v>hi){hi=v;hiWitness=d}
    }
    return {lo,hi,loWitness,hiWitness};
  };
  let tests=0, configurations=0,bruteVectors=0;
  for(const i of intervals)for(const j of intervals)for(const k of intervals){
    const a=[i[0],j[0],k[0]],b=[i[1],j[1],k[1]];
    const exact=brute(a,b);
    const lo=analyticalLower(a,b),hi=analyticalUpper(a,b);
    if(lo!==exact.lo || hi!==exact.hi)throw Error(JSON.stringify({a,b,lo,hi,exact}));
    tests+=2;configurations++;
    bruteVectors+=(b[0]-a[0]+1)*(b[1]-a[1]+1)*(b[2]-a[2]+1);
  }
  const a=[1,-2,-2],b=[2,-1,2],baseline=brute(a,b);
  if(baseline.lo!==1 || baseline.hi!==4)throw Error("Main exact example failed");
  tests+=2;
  return {question:"Sharp missing-action support bounds on Blackwell report refinement for two signed whole-network policies, conditional on rectangular economic action-margin bounds",normalization:"p=(2,1,1)/4 and delta=a/4; outputs are numerator over 16",example:{probabilities:["1/2","1/4","1/4"],lower_delta:["1/4","-1/2","-1/2"],upper_delta:["1/2","-1/4","1/2"],lower_value:"1/16",upper_value:"1/4",lower_witness:baseline.loWitness.map(x=>x+"/4"),upper_witness:baseline.hiWitness.map(x=>x+"/4")},checks:{interval_configurations:configurations,brute_candidate_delta_vectors:bruteVectors,exact_assertions:tests,methods:"independent integer-grid enumeration versus analytic lower formula and signed-endpoint partition for upper"},restrictions:["fictional signed two-action customer-production outcomes","rectangular independent report-cell margin restrictions","same learner, buyer/robot/operator feasibility, action menu","not identified from actual customer receipts","not a new robotics learning law"]};
}
if (typeof require !== 'undefined' && require.main === module) console.log(JSON.stringify(reportValueSupportAudit(),null,2));
if (typeof module !== 'undefined') module.exports = {reportValueSupportAudit};
