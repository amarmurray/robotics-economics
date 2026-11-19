// Conditional synthetic signal-transport model for When Capabilities Become Production.
// Exact rational arithmetic; no field estimate, physical authorization, or novelty claim.
'use strict';
const assert = require('node:assert/strict');
function gcd(a,b){a=a<0n?-a:a;b=b<0n?-b:b;while(b!==0n){[a,b]=[b,a%b]}return a||1n}
function F(n,d=1n){n=BigInt(n);d=BigInt(d);assert(d!==0n);if(d<0n){n=-n;d=-d}const g=gcd(n,d);return {n:n/g,d:d/g}}
const add=(a,b)=>F(a.n*b.d+b.n*a.d,a.d*b.d);
const neg=a=>F(-a.n,a.d);
const sub=(a,b)=>add(a,neg(b));
const mul=(a,b)=>F(a.n*b.n,a.d*b.d);
const cmp=(a,b)=>a.n*b.d<b.n*a.d?-1:a.n*b.d>b.n*a.d?1:0;
const max=(a,b)=>cmp(a,b)>=0?a:b;
const min=(a,b)=>cmp(a,b)<=0?a:b;
const str=a=>a.d===1n?String(a.n):String(a.n)+'/'+String(a.d);
const Z=F(0), ONE=F(1), HALF=F(1,2);
// Complete qualified, net original-order contribution in (high, low) commercial states.
// The specialist S is a qualified fallback, not an assumed robot safety certificate.
const A={F:[F(0),F(0)],S:[F(3,4),F(3,4)],G:[F(3),F(-1)],T:[F(4),F(-6)]};
const names=Object.keys(A);
const policies=names.flatMap(hi=>names.map(lo=>[hi,lo]));
// Symmetric diagnostic correctness q, common pre-source opportunity prior 1/2.
function value([highReport,lowReport],q){
 const h=A[highReport],l=A[lowReport],r=sub(ONE,q);
 return mul(HALF,add(add(mul(q,h[0]),mul(r,h[1])),add(mul(r,l[0]),mul(q,l[1]))));
}
function argmax(q){let best=null;for(const p of policies){let v=value(p,q);if(!best||cmp(v,best.value)>0)best={policy:p,value:v}}return best}
function bestValue(q){return argmax(q).value}
function predicted(q){
 if(cmp(q,F(9,16))<=0)return ONE;
 if(cmp(q,F(5,6))<=0)return sub(mul(F(2),q),F(1,8));
 return sub(mul(F(5),q),F(21,8));
}
function evaluate(){
 let checks=0;
 function eq(a,b,name){assert.equal(str(a),str(b),name);checks++}
 const qLow=F(3,5),qHigh=F(9,10),qMix=F(3,4);
 const stale=['T','S'],robust=['G','S'];
 eq(value(stale,qLow),F(3,8),'stale low');
 eq(value(stale,qHigh),F(15,8),'stale high');
 eq(value(robust,qLow),F(43,40),'robust low');
 eq(value(robust,qHigh),F(67,40),'robust high');
 eq(bestValue(qLow),F(43,40),'calibrated low');
 eq(bestValue(qHigh),F(15,8),'calibrated high');
 eq(bestValue(qMix),F(11,8),'unrevealed kernel mixture');
 eq(sub(bestValue(qLow),value(stale,qLow)),F(7,10),'stale regret');
 eq(sub(bestValue(qLow),ONE),F(3,40),'optional low q report gain');
 eq(sub(ONE,value(stale,qLow)),F(5,8),'stale policy harms retained production');
 eq(sub(mul(HALF,add(bestValue(qLow),bestValue(qHigh))),bestValue(qMix)),F(1,10),'ex ante full calibration EVPI');
 eq(sub(value(robust,F(5,6)),value(stale,F(5,6))),Z,'switch threshold');
 let robustV=null,robustPolicy=null;
 for(const p of policies){const worst=min(value(p,qLow),value(p,qHigh));if(!robustV||cmp(worst,robustV)>0){robustV=worst;robustPolicy=p}}
 eq(robustV,F(43,40),'minimax among all sixteen deterministic rules');
 assert.deepEqual(robustPolicy,robust);checks++;
 // For q in [1/2,1] the complete menu optimum equals the analytical piecewise envelope.
 for(let n=60;n<=120;n++)eq(bestValue(F(n,120)),predicted(F(n,120)),'grid q='+n+'/120');
 // For the two-world uncertainty set, no randomized rule can exceed W(qLow).
 // The deterministic robust policy attains W(qLow), so it is also randomized-minimax.
 assert.equal(policies.length,16);checks++;
 return {
  model:'synthetic qualified whole-network contribution, not robot field evidence',
  report_source_accuracy:'9/10',
  possible_target_accuracies:['3/5','9/10'],
  source_optimized_fixed_report_policy:stale,
  stale_policy_low:str(value(stale,qLow)),
  stale_policy_high:str(value(stale,qHigh)),
  calibrated_target_low:str(bestValue(qLow)),
  calibrated_target_high:str(bestValue(qHigh)),
  robust_policy:robustPolicy,
  robust_guarantee:str(robustV),
  no_report_retained_value:'1',
  previously_misclassified_low_world_regret:str(sub(bestValue(qLow),value(stale,qLow))),
  kernel_quality_revelation_before_report_value_ex_ante:str(sub(mul(HALF,add(bestValue(qLow),bestValue(qHigh))),bestValue(qMix))),
  analytical_switch:'q=5/6',
  exact_assertions:checks,
  physically_approved_target_trial:false,
  commercial_field_calibration:false
 };
}
if(require.main===module)process.stdout.write(JSON.stringify(evaluate(),null,2)+'\n');
module.exports={F,add,sub,mul,cmp,str,value,argmax,bestValue,predicted,evaluate};
