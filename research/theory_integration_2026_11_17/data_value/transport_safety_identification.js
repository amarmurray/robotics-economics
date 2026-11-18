// Conditional source-to-production transport/safety identification.
// Synthetic rational-style finite tests; not field calibration or operational safety authority.
"use strict";
const EPS=1e-9;
let assertions=0;
function check(ok,msg){assertions++;if(!ok) throw Error("Assertion "+assertions+": "+msg);}
function close(x,y){return Math.abs(x-y)<EPS;}
function cells(p,q){return [1-2*p+q,p-q,p-q,q];}
function valid(p,q){const c=cells(p,q);return c.every(v=>v>=-EPS)&&close(c.reduce((a,b)=>a+b,0),1);}
function diff(qr,qe){return qe-qr;}
function net(mu,bs,ds,deltas,costDiffs){
  return mu.reduce((total,w,i)=>total+w*(bs[i]-deltas[i]*ds[i]-costDiffs[i]),0);
}
const pR=.75,pE=.9;
const A={qr:.75,qe:.80}, B={qr:.5,qe:.85};
check(valid(pR,A.qr)&&valid(pE,A.qe)&&valid(pR,B.qr)&&valid(pE,B.qe),"both site joint laws admissible");
const siteDiff=[diff(A.qr,A.qe),diff(B.qr,B.qe)];
const study=[.9,.1], target=[.4,.6],b=[1,1],delta=[8,8],c=[0,0];
const studyMean=study[0]*siteDiff[0]+study[1]*siteDiff[1];
const targetMean=target[0]*siteDiff[0]+target[1]*siteDiff[1];
const studyNet=net(study,b,siteDiff,delta,c),targetNet=net(target,b,siteDiff,delta,c);
check(close(studyMean,.08)&&close(targetMean,.23),"selection mismatch");
check(close(studyNet,.36)&&close(targetNet,-.84),"sample certificate flips in target");
check(studyMean<.1&&targetMean>.125,"study bound not transported");
const demand={qR:.7,qE:.8};
const before=1-8*diff(demand.qR,demand.qE);
const after=1-12*diff(demand.qR,demand.qE);
check(valid(pR,demand.qR)&&valid(pE,demand.qE),"demand static quality feasible");
check(close(before,.2)&&close(after,-.2),"demand-only reversal");
function lowerBound(mu,bs,delta,u,costDiff){
  return net(mu,bs,u,delta,costDiff);
}
const allSupported=lowerBound(target,b,delta,[.1,.1],c);
const missingTenth=lowerBound([.9,.1],b,delta,[.1,.4],c);
const missingTwentieth=lowerBound([.95,.05],b,delta,[.1,.4],c);
const epsilonCritical=(1/8-.1)/(.4-.1);
check(close(allSupported,.2),"all-sites bound");
check(close(missingTenth,-.04)&&close(missingTwentieth,.08),"coverage bound");
check(close(epsilonCritical,1/12),"missing mass threshold");
const fractions=[];let minPaired=Infinity,minMissing=Infinity,maxPaired=-Infinity;
let nSupported=0,nMissing=0;
// Enumerate valid two-service Fréchet copulas at each site. The product grid represents
// a rectangular sitewise identified set; other correlated sets require joint optimization.
for(let r1=50;r1<=75;r1++){
 const qr1=r1/100;
 for(let e1=80;e1<=90;e1++){
  const qe1=e1/100;
  const d1=qe1-qr1;
  if(d1>.10000001) continue;
  check(valid(pR,qr1)&&valid(pE,qe1),"site one four-cell distribution");
  for(let r2=50;r2<=75;r2++){
   const qr2=r2/100;
   for(let e2=80;e2<=90;e2++){
    const qe2=e2/100;
    const d2=qe2-qr2;
    const missing=net([.9,.1],b,[d1,d2],delta,c);
    minMissing=Math.min(minMissing,missing);
    nMissing++;
    if(d2<=.10000001){
       const paired=net(target,b,[d1,d2],delta,c);
       minPaired=Math.min(minPaired,paired);
       maxPaired=Math.max(maxPaired,paired);
       nSupported++;
       check(paired>=.2-1e-8,"all-supported uniform economic certificate");
    }
   }
  }
 }
}
check(close(minPaired,.2)&&close(minMissing,-.04),"sharp site rectangular bounds");
check(nSupported>0&&nMissing>nSupported,"nonempty grid world sets");
const W0={goodLow:.5,goodHigh:0,badLow:.4,badHigh:.1};
const W1={goodLow:.4,goodHigh:.1,badLow:.5,badHigh:0};
function marginals(W){
 return {good:W.goodLow+W.goodHigh,high:W.goodHigh+W.badHigh,
  sum:Object.values(W).reduce((a,b)=>a+b,0)};
}
const m0=marginals(W0),m1=marginals(W1);
check(close(m0.good,.5)&&close(m1.good,.5)&&close(m0.high,.1)&&close(m1.high,.1)&&close(m0.sum,1)&&close(m1.sum,1),"same separate marginals");
function eligibleGood(W,firstCost=1,low=1,high=2,budget=2.1){
 return (W.goodLow<EPS||firstCost+low<=budget) &&
        (W.goodHigh<EPS||firstCost+high<=budget);
}
check(eligibleGood(W0)&&!eligibleGood(W1),"conditional tail destroys safety despite equal marginals");
check(eligibleGood(W1,1,1,2,3),"physical reserve makes route feasible");
const results={
 schema:"conditional_transport_safety_synthetic_v1",
 provenance:"No robot trial, customer accepted-service data, external safety authority, or calibrated dollar parameters",
 sourceSiteSuccess:{A,B,technicalMarginals:{routine:pR,redesign:pE}},
 selection:{studyWeights:study,targetWeights:target,siteDiff,studyMean,targetMean,studyNet,targetNet},
 demand:{jointSuccess:demand,deltaBefore:8,deltaAfter:12,netBefore:before,netAfter:after},
 certificate:{allSitesPairedUpper:[.1,.1],allSupportedLower:allSupported,
  missingSiteUpper:.4,missingTenPercentLower:missingTenth,missingFivePercentLower:missingTwentieth,
  criticalUnsupportedTargetShare:epsilonCritical,gridSupportedWorlds:nSupported,
  gridMissingWorlds:nMissing,gridSharpPairedLower:minPaired,gridSharpMissingLower:minMissing,
  gridPairedMax:maxPaired},
 safety:{world0:W0,world1:W1,sameMarginals:m0,eligibleInWorld0:eligibleGood(W0),
  eligibleInWorld1:eligibleGood(W1),eligibleWithBudget3:eligibleGood(W1,1,1,2,3)},
 assertions, historicalCI:false, fieldEvidence:false, peerReview:false
};
return results;
