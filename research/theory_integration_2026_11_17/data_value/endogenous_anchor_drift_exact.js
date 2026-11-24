"use strict";
const run = function(){
 let checks=0;const ck=(x,m)=>{checks++;if(!x)throw Error(m)};
 const rows=[];
 for(const N of [16,32,64]){
  let count=0,auditCount=0,minG=Infinity,maxG=-Infinity,minE=Infinity,maxE=-Infinity,minD=Infinity,maxD=-Infinity,minAudit=Infinity,witness=null;
  for(let x=N/2;x<=3*N/4;x++)for(let e=N/2;e<=3*N/4;e++)for(let z=0;z<=3*N/4-x;z++){
   count++;
   const a=[N/2-z,x-N/2+z,z,3*N/4-x-z,3*N/4-x,x-N/2];
   const v=[e,3*N/4-e,3*N/4-e,e-N/2];
   ck(Math.min(...a,...v)>=0,"nonnegative common-law arm marginals");
   ck(a.reduce((s,n)=>s+n,0)===N&&v.reduce((s,n)=>s+n,0)===N,"probability mass");
   ck(a[0]+a[1]===x&&a[0]+a[2]===N/2,"joint renewal and upgraded offer");
   ck(a.slice(0,4).reduce((s,n)=>s+n,0)===3*N/4&&a[0]+a[1]+a[4]===3*N/4,"G marginals");
   ck(v[0]+v[1]===3*N/4&&v[0]+v[2]===3*N/4,"E marginals");
   // payoffs in 1/(8N) units
   const G=12*N+48*x+32*z,E=18*N+48*e,D=G-E;
   ck(G===12*N+48*(a[0]+a[1])+32*a[2],"feasible dispatch");
   ck(x+z<=3*N/4,"worker conservation");
   minG=Math.min(minG,G);maxG=Math.max(maxG,G);minE=Math.min(minE,E);maxE=Math.max(maxE,E);minD=Math.min(minD,D);maxD=Math.max(maxD,D);
   const free=G+4*N,shared=2*N+48*e+16*(3*N/4-e);
   ck(free-G===4*N&&shared<=38*N,"free matched routine and shared staff");
   if(x-e>=N/8&&z>=N/16){
    auditCount++;
    for(const dg of [-1,1])for(const de of [-1,1])for(const db of [-2,2]){
     const drift=D+dg*x-de*e+db*z;
     ck(drift*64>=5*8*N,"sharp audit bound");
     if(drift<minAudit){minAudit=drift;witness={x,e,z,dg,de,db}}
    }
   }
  }
  ck(minG===36*N&&maxG===48*N&&minE===42*N&&maxE===54*N,"sharp level endpoints");
  ck(minD===-18*N&&maxD===6*N,"sharp difference endpoints");
  ck(minAudit*64===5*8*N,"audit attainability");
  ck(witness.x===11*N/16&&witness.e===9*N/16&&witness.z===N/16,"audit minimizer");
  rows.push({N,units:`1/${8*N}`,count,auditCount,minG,maxG,minE,maxE,minD,maxD,minAudit,witness});
 }
 return {synthetic:true,checks,rows,exact_continuous_base_difference:["-9/4","3/4"],sharp_drift_audit_lower:"5/64",separate_rectangle_lower:"3/64"};
};
console.log(JSON.stringify(run(),null,2));
