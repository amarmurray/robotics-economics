"use strict";

// Synthetic exact-integer verification only; not robot evidence.
function run() {
 let checks=0,slopeCases=0,zeroThird=0;
 const ok=(c,m)=>{checks++;if(!c)throw Error(m)};
 const probabilities=k=>[100-k,k,k,100-k,k,100-k,100-k,k];
 const triple=f=>f[1]+f[2]+f[4]+f[7]-f[0]-f[3]-f[5]-f[6];
 const expected=(k,f)=>probabilities(k).reduce((v,p,i)=>v+p*f[i],0);
 let minGap=9999,maxGap=-9999,signs={SG:0,E:0,tie:0};
 for(let k=0;k<=100;k++){
  const p=probabilities(k);ok(p.reduce((a,b)=>a+b,0)===400,"mass "+k);
  for(let bit=0;bit<3;bit++){
   ok(p.reduce((a,b,i)=>a+(((i>>bit)&1)?b:0),0)===200,"marginal "+k);
   for(let other=bit+1;other<3;other++)ok(p.reduce((a,b,i)=>a+(((i>>bit)&1)&&((i>>other)&1)?b:0),0)===100,"pair "+k);
  }
  const R=1650,G=1700,E=1750,S=Math.max(1650,1600+k),SG=Math.max(1650,1600+2*k);
  ok(R<=G&&G<=E&&S<=E&&SG>=R,"menu "+k);
  const gap=SG-E;minGap=Math.min(gap,minGap);maxGap=Math.max(gap,maxGap);
  signs[gap>0?"SG":gap<0?"E":"tie"]++;
  ok((gap>0)===(k>75),"threshold "+k);
  ok((gap===0)===(k===75),"tie "+k);
 }
 for(let n=0;n<6561;n++){
  let x=n,f=[];
  for(let j=0;j<8;j++){f.push(x%3-1);x=Math.floor(x/3)}
  const d=triple(f);
  for(const k of [0,1,20,75,100]){ok(expected(k,f)===expected(0,f)+k*d,"difference "+n+" "+k);slopeCases++}
  if(d===0){zeroThird++;ok(expected(0,f)===expected(100,f),"identified "+n)}
 }
 ok(minGap===-100&&maxGap===50,"bounds");
 return {date:"2026-11-21",scope:"synthetic exact integer arithmetic; 1/400 joint-mass grid; 6561 payoff tables",denominatorValue:1600,denominatorMass:400,checks,slopeCases,zeroThirdTables:zeroThird,stageOneMarginal:"1/2 each",allPairwiseJoint:"1/4",thirdMassInterval:"[0,1/4]",programsAtT0:{R:1650,G:1700,S:1650,SG:1650,E:1750},programsAtTQuarter:{R:1650,G:1700,S:1700,SG:1800,E:1750},sgMinusEIntervalScaled:[minGap,maxGap],sgMinusEInterval:"[-1/16,+1/32]",indifferenceT:"3/16",gridSigns:signs,meaning:"Two pairwise-indistinguishable paid-history/rights worlds reverse optimized source-plus-grounding versus embodiment investment."};
}

if(typeof module!=="undefined" && require.main===module) console.log(JSON.stringify(run(),null,2));
if(typeof module!=="undefined") module.exports={run};
