function run(){
 let checks=0,cases=0;const ok=x=>{if(!x)throw Error("assert "+checks);checks++};
 const frac=(x,n)=>n?x/n:null;
 let low=[],overall=[];
 for(let n=1;n<=122;n++)for(let s=0;s<=n;s++){if(Math.round(10000*s/n)===9552)low.push([s,n]);if(Math.round(10000*s/n)===8703)overall.push([s,n]);}
 for(let n=2;n<=100;n++)for(let s=0;s<=n;s++)for(let k=1;k<n;k++){
   const lo=Math.max(0,k-(n-s)),hi=Math.min(s,k);
   for(let x=lo;x<=hi;x++){cases++;ok(((s-x)*n>s*(n-k))===(x*n<s*k));ok(s-x<=s);ok(x<=k);ok(n-k>=s-x);}
 }
 const info=(p,g)=>{const a=2,b=-1+g,h=.5;return {blind:Math.max(h,p*a+(1-p)*b),informed:p*Math.max(h,a)+(1-p)*Math.max(h,b)}};
 for(let i=0;i<=100;i++)for(let j=0;j<=60;j++){const r=info(i/100,j/20);ok(r.informed+1e-10>=r.blind);}
 const result={checks,cases,observed:{requests:135,eligible:122,completed:108,classifiedFailures:14,excluded:13,completionEligible:108/122,completionOriginal:108/135,blockageRestrictedCeiling:8/122,communicationRestrictedCeiling:2/122,corridorRestrictedCeiling:4/122,reportedOverall:87.03,reportedLow:95.52,roundedLowCandidateFractions:low,roundedOverallCandidateFractions:overall},synthetic:{noContinuation:info(.5,0),failureContinuation:info(.5,2)},fieldCausalDataValue:false,fullRepositoryCI:false};
 return result;
}
if(typeof module!=='undefined'&&require.main===module)console.log(JSON.stringify(run(),null,2));
