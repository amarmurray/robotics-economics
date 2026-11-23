// Four-date extension of the G-assigned service/repair/dual-buyer model.
// All quantities are stipulated synthetic normalized units. No field data.
// Run: node dynamic_riskset_exact.js
'use strict';
const assert = require('node:assert/strict');
function atoms(regime) {
  const out = [];
  for (let h=0;h<2;h++) for (let u=0;u<2;u++)
  for (let v=0;v<2;v++) for (let z=0;z<2;z++) {
    const A = u ^ h, C = v ^ h, W = h ^ u ^ v;
    const risk = Number(h===1 && W===0);
    const D = z; // t4 original C buyer offer; one remaining unit after paid t2 service
    const L = risk ? (z ^ regime) : z; // clearance by t4 of t2-created repair job
    const accepted3 = Number(W===1 && (A===1 || (h===1 && C===1)));
    const accepted4 = Number(risk===1 && D===1 && L===1);
    const paidGross = 2*h + 4*accepted3 + 6*accepted4;
    out.push({h,u,v,z,A,C,W,D,L,risk,accepted3,accepted4,paidGross});
  }
  return out;
}
function count(rows, f) {return rows.filter(f).length;}
function tally(rows, selector) {
 const d = {};
 for (const row of rows) {const k = String(selector(row));d[k]=(d[k]||0)+1;}
 return d;
}
const low=atoms(1), high=atoms(0); let checks=0;
for (const rows of [low,high]) {
 assert.equal(rows.length,16);checks++;
 assert.equal(count(rows,x=>x.risk===1),4);checks++;
 assert.equal(count(rows,x=>x.risk&&x.D),2);checks++;
 assert.equal(count(rows,x=>x.risk&&x.L),2);checks++;
 assert.equal(count(rows,x=>x.h&&x.W&&x.A&&x.C),2);checks++;
 assert.equal(count(rows,x=>x.h&&x.W),4);checks++;
 for (const x of rows) {
   assert.equal(x.risk,Number(x.h===1 && x.W===0));checks++;
   assert.equal(x.accepted4,Number(x.risk===1&&x.D===1&&x.L===1));checks++;
   assert.ok(!(x.accepted3&&x.W===0));checks++;
   assert.ok(!(x.accepted4&&x.W===1));checks++;
   assert.ok((x.h+x.accepted3+x.accepted4)<=3);checks++;
 }
}
assert.deepEqual(tally(low,x=>[x.h,x.A,x.C,x.W].join('')),
                 tally(high,x=>[x.h,x.A,x.C,x.W].join('')));checks++;
// The t3 H=W=1 original-offer audit (even if D,L also logged there) is unchanged.
assert.deepEqual(tally(low.filter(x=>x.h&&x.W),x=>[x.A,x.C,x.D,x.L].join('')),
                 tally(high.filter(x=>x.h&&x.W),x=>[x.A,x.C,x.D,x.L].join('')));checks++;
// Conditional on any H,A,C,W history, D and L have the same individual distribution.
for (const key of Object.keys(tally(low,x=>[x.h,x.A,x.C,x.W].join('')))) {
 const a=low.filter(x=>[x.h,x.A,x.C,x.W].join('')===key),
       b=high.filter(x=>[x.h,x.A,x.C,x.W].join('')===key);
 assert.deepEqual(tally(a,x=>x.D),tally(b,x=>x.D));checks++;
 assert.deepEqual(tally(a,x=>x.L),tally(b,x=>x.L));checks++;
}
// Observing the pair in the blocked risk set distinguishes the regimes.
assert.notDeepEqual(tally(low.filter(x=>x.risk),x=>[x.D,x.L].join('')),
                    tally(high.filter(x=>x.risk),x=>[x.D,x.L].join('')));checks++;
const numerator80 = rows => rows.reduce((s,x)=>s+5*x.paidGross,0)-16;
const V = {R:160,P:168,E:172,G_low:numerator80(low),G_high:numerator80(high)};
assert.deepEqual(V,{R:160,P:168,E:172,G_low:144,G_high:204});checks++;
const m={low:count(low,x=>x.accepted4)/16,high:count(high,x=>x.accepted4)/16};
assert.equal(m.low,0);assert.equal(m.high,1/8);checks+=2;
// B4 and L4 are each fair conditional on the t3 blocked risk set, yet the overlap differs.
const odds={};
for(const [key, rows] of [['low',low],['high',high]]) {
 const risk=rows.filter(x=>x.risk);
 odds[key]={riskMass:risk.length/16,orderRate:count(risk,x=>x.D===1)/risk.length,
  clearanceRate:count(risk,x=>x.L===1)/risk.length,
  jointRate:count(risk,x=>x.D===1&&x.L===1)/risk.length};
 assert.equal(odds[key].riskMass,1/4);checks++;
 assert.equal(odds[key].orderRate,1/2);checks++;
 assert.equal(odds[key].clearanceRate,1/2);checks++;
}
assert.equal(odds.low.jointRate,0);assert.equal(odds.high.jointRate,1/2);checks+=2;
// Regret for t0 commitment fraction x to G (rest independent E), 0<=x<=1.
// In the good G world: regret = (204-172)*(1-x)/80; bad: (172-144)*x/80.
const best_x={numerator:8,denominator:15}, worst_regret={numerator:14,denominator:75};
assert.equal(32*(15-8),28*8);checks++;
assert.equal((32*(15-8))/(80*15),14/75);checks++;
const threshold={numerator:7,denominator:120};
assert.equal(144+480*(7/120),172);checks++;
// Sharp Fréchet interval: with risk mass1/4, conditional marginals1/2 each,
// 0 <= unconditional joint m <= 1/8. Both entire causal worlds attain endpoints.
for(let n=0;n<=16;n++) {
 const w=n/16; const gj=(1-w)*V.G_low+w*V.G_high;
 assert.equal(gj,144+60*w);checks++;
 assert.ok(gj>=144&&gj<=204);checks++;
}
const result={kind:'stipulated synthetic four-date common-law G experiment',
  programs:{R:'2',P:'21/10',E:'43/20',G_low:'9/5',G_high:'51/20'},
  paid_t4_moment:{low:'0',high:'1/8'},audited_risk_set:odds,
  identification:'same complete G t3 (H,A,C,W) histories and t3 paid-early/worker-free audit; different G t4 original-order × repair-clearance coupling in paid-early/worker-blocked group',
  sharp_G_interval:['9/5','51/20'],switch_m:'7/120',
  minimax_G_share:'8/15',minimax_E_share:'7/15',minimax_regret:'14/75',
  checks,limits:'No G field assignment, signed rights, observed receipts, verified E independence or novel empirical estimate.'};
console.log(JSON.stringify(result,null,2));
module.exports={atoms,result};
