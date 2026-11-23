'use strict';
// Synthetic rational two-cohort source-production / grounding / qualified paid-service model.
// No field outcomes or rights claimed. All expected values use denominator 1600.
const assert = require('node:assert/strict');
const outcomes = k => {
  if (!Number.isInteger(k) || k < 0 || k > 10) throw new Error('k outside 0..10');
  const cells = [[0,0,k],[0,1,10-k],[1,0,10-k],[1,1,k]];
  let numeratorP = 0, numeratorGIndependent = 0, numeratorGCoupled=0;
  let count=0, pOriginal=0, pWorker=0, pPaid=0, qG=0, gD=0, gW=0, gPaid=0, f=0, t=0, ft=0;
  for (const [F,T,n] of cells) {
    for(let repeat=0; repeat<n;repeat++) {
      for(let D0=0;D0<=1;D0++) for(let R=0;R<=1;R++) for(let W0=0;W0<=1;W0++) {
        ++count; f+=F;t+=T;ft+=F*T;
        // P: qualified earlier service produces a field record; it can induce demand
        // and also a recovery job that occupies the next shared worker slot.
        const H=F, S=H, QP=F*S, DP=+(F===1||D0===1), WP=+(F===0||R===0);
        const paidP=QP*DP*WP;
        numeratorP+=2*H+20*paidP;
        pOriginal+=DP;pWorker+=WP;pPaid+=paidP;
        // G: a separately authorized target-grounding record T is acquired,
        // no earlier accepted service; next buyer and independently cleared worker.
        const QG=+(F===1||T===1);
        const paidGI=QG*D0*W0;
        numeratorGIndependent+=30*paidGI-1; // 1/10 cost per atom
        qG+=QG;gD+=D0;gW+=W0;gPaid+=paidGI;
        // Alternative, same G source joint and same D/W marginal,
        // but original order and clearance are coupled to the source state.
        const paidGC=QG*F*T;
        numeratorGCoupled+=30*paidGC-1;
      }
    }
  }
  assert.equal(count,160);
  return {k,count,pNum:numeratorP,gIndependentNum:numeratorGIndependent,
    gCoupledNum:numeratorGCoupled, eNum:992,rNum:0,den:1600,
    observations:{F:f,T:t,FT:ft,DP:pOriginal,WP:pWorker,Ppaid:pPaid,
      QG:qG,DG:gD,WG:gW,Gpaid:gPaid}};
};
let assertions=0;
function check(a,b,msg){assert.deepEqual(a,b,msg);++assertions;}
const all=[];
for(let k=0;k<=10;k++){
  const r=outcomes(k),o=r.observations;all.push(r);
  check(r.count,160);check(r.pNum,960);check(r.eNum,992);
  check(r.gIndependentNum,1040-60*k);check(r.gCoupledNum,240*k-160);
  check(o.F,80);check(o.T,80);check(o.FT,8*k);
  check(o.DP,120);check(o.WP,120);check(o.Ppaid,40);
  check(o.QG,160-8*k);check(o.DG,80);check(o.WG,80);
  check(o.Gpaid,40-2*k);
  check(r.gIndependentNum>r.eNum,k===0);
}
// The P-only complete observation table (F,D_P,W_P,H,S,paidP) does not depend on k.
// Verify it cell-by-cell, not just with a single marginal.
function pLog(k){const counts=new Map();for(const [F,T,n] of [[0,0,k],[0,1,10-k],[1,0,10-k],[1,1,k]]) {
 for(let D=0;D<=1;D++) for(let R=0;R<=1;R++) for(let W=0;W<=1;W++) {
  const H=F,S=H,DP=+(F||D),WP=+(!F||!R),paid=F*DP*WP;
  const key=[F,H,S,DP,WP,paid].join('');counts.set(key,(counts.get(key)||0)+n);
 }}return [...counts.entries()].sort((a,b)=>a[0].localeCompare(b[0]));}
for(let k=0;k<=10;k++)check(pLog(k),pLog(0));
// At k=5, source pair (F,T), G qualification rate, and D/W singles match,
// but policy-dependent buyer/worker coincidence crosses E.
check(all[5].gIndependentNum,740); // 37/80 = .4625
check(all[5].gCoupledNum,1040); // 13/20 = .65
check(all[5].observations.QG,120);
// Expected regret with no predecision report on x in the independence submodel.
// G share 2/25. Check exact extrema at every law (denominator 25*1600).
for(const r of all){
  const mixNum=2*r.gIndependentNum+23*r.eNum; // denominator 25*1600
  const bestNum=25*Math.max(r.gIndependentNum,r.eNum,r.pNum,r.rNum);
  const regret=bestNum-mixNum;
  check(regret<=1104,true); // 69/2500 * 40000 = 1104
}
check(25*Math.max(all[0].gIndependentNum,992)-(2*all[0].gIndependentNum+23*992),1104);
check(25*Math.max(all[10].gIndependentNum,992)-(2*all[10].gIndependentNum+23*992),1104);
// Prior equal only over endpoint worlds: perfect legally pre-commitment signal
// contributes E plus 3/200 relative to no signal (E).
check((Math.max(all[0].gIndependentNum,992)+Math.max(all[10].gIndependentNum,992))/2-992,24);
console.log(JSON.stringify({model:'endogenous-two-cohort-paid-qualification',version:1,
  checks:assertions,states:all.length,endpointLow:all[0],midpoint:all[5],endpointHigh:all[10],
  minimaxGShare:'2/25',minimaxRegret:'69/2500',equalPriorPerfectSignalGross:'3/200',
  qualifier:'synthetic normalized increments; no empirical calibration'},null,2));
