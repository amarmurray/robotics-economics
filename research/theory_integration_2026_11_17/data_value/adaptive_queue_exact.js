'use strict';
// Exact synthetic conditional test; no customer records or field robot tests.
const assert = require('node:assert/strict');
let checks = 0;
const ck = (ok, message) => { checks++; assert.ok(ok, message); };
const gcd = (a,b) => { while(b!==0n){const r=a%b;a=b;b=r;} return a<0n?-a:a; };
const R=(a,b=1n)=>{a=BigInt(a);b=BigInt(b);assert.ok(b!==0n);if(b<0n){a=-a;b=-b;}const g=gcd(a,b);return [a/g,b/g];};
const add=(a,b)=>R(a[0]*b[1]+b[0]*a[1],a[1]*b[1]);
const neg=a=>R(-a[0],a[1]);
const sub=(a,b)=>add(a,neg(b));
const mul=(a,b)=>R(a[0]*b[0],a[1]*b[1]);
const cmp=(a,b)=>{const t=a[0]*b[1]-b[0]*a[1];return t<0n?-1:t>0n?1:0;};
const eq=(a,b)=>cmp(a,b)===0;
const max=(a,b)=>cmp(a,b)>=0?a:b;
const str=a=>a[1]===1n?String(a[0]):String(a[0])+'/'+String(a[1]);
const zero=R(0), one=R(1), half=R(1,2), threeQuarter=R(3,4);
const oldPaid=R(4), pilotCost=R(1,4), t2TargetGain=R(1,8);
const baselineSite3=mul(R(4,5),R(5,8));
const joint=z=>[
  {u:1,j:0,p:z},
  {u:1,j:1,p:sub(threeQuarter,z)},
  {u:0,j:0,p:sub(half,z)},
  {u:0,j:1,p:sub(z,R(1,4))}
];
function enumerateP(z,policy){
  let gain=zero;
  for(const d of [1,2]){
    for(const atom of joint(z)){
      const target=policy==='T' && d===1;
      const t2=target?t2TargetGain:zero;
      const t3=target ? (atom.u && !atom.j ? one:zero):baselineSite3;
      gain=add(gain,mul(mul(half,atom.p),add(t2,t3)));
    }
  }
  return add(sub(oldPaid,pilotCost),gain);
}
function analyticP(z,policy){
  const t2d1=policy==='T'?add(t2TargetGain,z):baselineSite3;
  return add(sub(oldPaid,pilotCost),add(mul(half,baselineSite3),mul(half,t2d1)));
}
const G=add(sub(oldPaid,R(21,50)),R(7,10));
const E=add(sub(oldPaid,R(3,5)),R(9,10));
ck(eq(baselineSite3,half),'R site-3 paid Q times original buyer demand');
ck(eq(G,R(107,25)),'G qualified grounded service full contribution');
ck(eq(E,R(43,10)),'E new hardware and worker full contribution');
const scenarios=[];
for(let k=16;k<=32;k++){
  const z=R(k,64), atoms=joint(z);
  ck(atoms.every(a=>cmp(a.p,zero)>=0),'no negative joint mass');
  ck(eq(atoms.reduce((s,a)=>add(s,a.p),zero),one),'joint distribution sums to 1');
  ck(eq(atoms.filter(a=>a.u===1).reduce((s,a)=>add(s,a.p),zero),threeQuarter),'joint buyer marginal');
  ck(eq(atoms.filter(a=>a.j===1).reduce((s,a)=>add(s,a.p),zero),half),'joint new recovery-job marginal');
  for(const policy of ['R','T']){
    ck(eq(enumerateP(z,policy),analyticP(z,policy)),'history enumeration and Bellman closed form agree');
  }
  const pR=enumerateP(z,'R'),pT=enumerateP(z,'T');
  const chosen=max(pR,pT);
  ck(eq(pR,R(17,4)),'retained R policy accessible under P');
  ck((cmp(pT,pR)>0)===(cmp(z,R(3,8))>0),'dispatch threshold');
  ck(eq(chosen,add(R(4),mul(half,max(half,add(t2TargetGain,z))))),'optimized P closed form');
  scenarios.push({z:str(z),P:str(chosen),dispatch:cmp(pT,pR)>0?'T':cmp(pT,pR)<0?'R':'tie'});
}
const low=R(1,4),high=R(1,2);
const pLow=max(enumerateP(low,'R'),enumerateP(low,'T'));
const pHigh=max(enumerateP(high,'R'),enumerateP(high,'T'));
ck(eq(pLow,R(17,4)),'low P'); ck(eq(pHigh,R(69,16)),'high P');
ck(cmp(pLow,G)<0 && cmp(G,E)<0 && cmp(E,pHigh)<0,'investment rankings reverse');
for(let i=0;i<=100;i++){
  const x=R(i,100);
  const lowValue=add(mul(sub(one,x),enumerateP(low,'R')),mul(x,enumerateP(low,'T')));
  const highValue=add(mul(sub(one,x),enumerateP(high,'R')),mul(x,enumerateP(high,'T')));
  ck(cmp((cmp(lowValue,highValue)<=0?lowValue:highValue),R(17,4))<=0,'ex ante implementable maximin bound');
}
const result={model:'adaptive_multijob_queue_demand_learning',synthetic:true,scenario_count:scenarios.length,assertions:checks,low_P:str(pLow),high_P:str(pHigh),grounding_G:str(G),embodiment_E:str(E),fallback_R:str(oldPaid),dispatch_cutoff_z:'3/8',observational_z_range:['1/4','1/2'],known_world_policy_values:scenarios,robust_fixed_policy:'R at date 2 when low/high law remains unidentified',real_qualified_original_buyer_data:false};
console.log(JSON.stringify(result,null,2));
