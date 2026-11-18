'use strict';
// Exact rational finite decision check; all data synthetic; run: node passive_support_decision.js
const runModel = function runModel(){
  let assertions=0;
  const assert=(ok,msg)=>{assertions++;if(!ok)throw new Error("Assertion failed: "+msg);};
  const gcd=(x,y)=>{x=x<0n?-x:x;y=y<0n?-y:y;while(y){const z=x%y;x=y;y=z;}return x||1n;};
  const f=(a,b=1n)=>{a=BigInt(a);b=BigInt(b);if(b<0n){a=-a;b=-b;}if(b===0n)throw new Error("denominator zero");const g=gcd(a,b);return {n:a/g,d:b/g};};
  const add=(a,b)=>f(a.n*b.d+b.n*a.d,a.d*b.d);
  const neg=a=>f(-a.n,a.d);
  const sub=(a,b)=>add(a,neg(b));
  const mul=(a,b)=>f(a.n*b.n,a.d*b.d);
  const div=(a,b)=>f(a.n*b.d,a.d*b.n);
  const equal=(a,b)=>a.n===b.n&&a.d===b.d;
  const fmt=a=>a.d===1n?String(a.n):`${a.n}/${a.d}`;
  const num=a=>Number(a.n)/Number(a.d);
  const zero=f(0),one=f(1), L=f(7,20),H=f(9,20),eps=f(1,5),oneLess=sub(one,eps);
  const p=div(H,add(L,H)),r0=mul(L,p),r1=mul(H,sub(one,p));
  assert(equal(p,f(9,16)),"passive probability");
  assert(equal(r0,f(63,320))&&equal(r0,r1),"passive risk");
  const a=one,b=f(2,37);
  const noisyBad=mul(L,add(mul(eps,a),mul(oneLess,b)));
  const noisyGood=mul(H,add(mul(oneLess,sub(one,a)),mul(eps,sub(one,b))));
  assert(equal(noisyBad,f(63,740))&&equal(noisyGood,noisyBad),"noisy saddle candidate");
  const lambda=f(9,37);
  const slopeB=sub(mul(mul(lambda,L),oneLess),mul(mul(sub(one,lambda),H),eps));
  const slopeA=sub(mul(mul(lambda,L),eps),mul(mul(sub(one,lambda),H),oneLess));
  assert(equal(slopeB,zero)&&slopeA.n<0n,"dual supporting weights");
  const weightedAtA1B0=add(mul(lambda,mul(L,eps)),mul(sub(one,lambda),mul(H,eps)));
  assert(equal(weightedAtA1B0,f(63,740)),"dual lower bound");
  const reduction=sub(f(63,320),f(63,740));
  assert(equal(reduction,f(1323,11840)),"diagnostic cost frontier");
  const deterministicWorst=mul(H,eps);
  assert(equal(deterministicWorst,f(9,100)),"deterministic noisy upper");
  const threshold=f(7,8), netA=x=>add(f(1,20),mul(f(2,5),x));
  const diff=x=>sub(netA(x),f(2,5));
  assert(equal(diff(zero),neg(L))&&equal(diff(f(2)),H)&&equal(diff(threshold),zero),"reuse previous shadow interval");
  const shadowLearningDelta=L;
  assert(equal(add(diff(zero),shadowLearningDelta),zero),"learning but not identification");
  const gridN=60;
  let passiveViolations=0,noisyViolations=0;
  for(let i=0;i<=gridN;i++){
    const pi=i/gridN;
    const rBad=num(L)*pi, rGood=num(H)*(1-pi);
    if(Math.max(rBad,rGood)+1e-12<num(f(63,320)))passiveViolations++;
    for(let j=0;j<=gridN;j++){
      const aa=pi,bb=j/gridN;
      const nb=num(L)*(0.2*aa+0.8*bb);
      const ng=num(H)*(0.8*(1-aa)+0.2*(1-bb));
      if(Math.max(nb,ng)+1e-12<num(f(63,740)))noisyViolations++;
    }
  }
  assert(passiveViolations===0&&noisyViolations===0,"grid lower bounds");
  return {model:"Passive F support vs safe target diagnostic under retained qualified-service value",scope:"two endpoint worlds; noiseless source identification absent; hypothetical error 1/5; no field safety claim",regime_low:{a_minus_s:fmt(neg(L))},regime_high:{a_minus_s:fmt(H)},shadow_unsupported_value:"x in [0,2]",threshold_x:fmt(threshold),passive:{p_admit_A:fmt(p),minimax_regret:fmt(r0)},synthetic_diagnostic:{error_each_world:fmt(eps),p_A_given_positive:fmt(a),p_A_given_negative:fmt(b),minimax_regret:fmt(noisyBad),weighted_dual_low_world:fmt(lambda),deterministic_rule_max_regret:fmt(deterministicWorst)},regret_reduction_before_cost:fmt(reduction),development_counterexample:{verified_delta_assumed:fmt(shadowLearningDelta),new_low_world_difference:fmt(add(diff(zero),shadowLearningDelta))},checks:{exact_assertions:assertions,grid_points:(gridN+1)**2,passive_grid_violations:passiveViolations,noisy_grid_violations:noisyViolations}};
};
const result = runModel();
console.log(JSON.stringify(result, null, 2));
