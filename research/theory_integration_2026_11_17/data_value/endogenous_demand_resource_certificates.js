/* 2026-11-19 exact synthetic pricing, grounding and capacity model.
   BigInt fractions; no measured robotics or customer economics. */
function model(){
 const gcd=(a,b)=>{a=a<0n?-a:a;b=b<0n?-b:b;while(b){let r=a%b;a=b;b=r;}return a||1n;};
 const f=(a,b=1n)=>{a=BigInt(a);b=BigInt(b);if(!b)throw Error("zero denominator");if(b<0n){a=-a;b=-b;}const g=gcd(a,b);return [a/g,b/g];};
 const add=(x,y)=>f(x[0]*y[1]+y[0]*x[1],x[1]*y[1]);
 const sub=(x,y)=>f(x[0]*y[1]-y[0]*x[1],x[1]*y[1]);
 const mul=(x,y)=>f(x[0]*y[0],x[1]*y[1]);
 const div=(x,y)=>f(x[0]*y[1],x[1]*y[0]);
 const cmp=(x,y)=>x[0]*y[1]<y[0]*x[1]?-1:x[0]*y[1]>y[0]*x[1]?1:0;
 const min=(x,y)=>cmp(x,y)<0?x:y;
 const max=(x,y)=>cmp(x,y)>0?x:y;
 const fmt=x=>x[1]===1n?String(x[0]):x[0]+"/"+x[1];
 let checks=0;
 const eq=(x,y)=>{checks++;if(cmp(x,y)!==0)throw Error(fmt(x)+" != "+fmt(y));};
 const assert=(b,label)=>{checks++;if(!b)throw Error(label);};
 const zero=f(0),one=f(1),two=f(2),eight=f(8),costX=f(3,2),costE=one;
 const revenue=(alpha,beta,q)=>sub(mul(alpha,q),mul(beta,mul(q,q)));
 const optimize=(alpha,beta,capacity)=>{const arg=min(capacity,div(alpha,mul(two,beta)));const q=max(zero,arg);return {q,value:revenue(alpha,beta,q)};};
 const x=(beta,C)=>optimize(add(eight,beta),beta,f(C));
 const r=(C)=>optimize(eight,two,f(C));
 eq(r(1).value,f(6));eq(r(2).value,f(8));
 const worlds={};
 for(const beta of [f(2),f(4)]){
  const v1=x(beta,1),v2=x(beta,2),key="beta_"+fmt(beta);
  worlds[key]={q1:fmt(v1.q),gross1:fmt(v1.value),q2:fmt(v2.q),gross2:fmt(v2.value),sourceOnlyNet:fmt(sub(v1.value,costX)),sourcePlusEmbodimentNet:fmt(sub(sub(v2.value,costX),costE)),sourceCapacityComplementarityVsRetained:fmt(sub(sub(v2.value,v1.value),sub(r(2).value,r(1).value)))};
  eq(v1.value,eight);
  const lambda=max(zero,sub(add(eight,beta),mul(two,mul(beta,f(2)))));
  const upper=add(mul(lambda,f(2)),div(mul(sub(add(eight,beta),lambda),sub(add(eight,beta),lambda)),mul(f(4),beta)));
  eq(v2.value,upper);
 }
 eq(x(f(2),2).value,f(12));eq(x(f(4),2).value,f(9));
 eq(x(f(2),2).q,two);eq(x(f(4),2).q,f(3,2));
 eq(sub(sub(x(f(2),2).value,costX),costE),f(19,2));
 eq(sub(sub(x(f(4),2).value,costX),costE),f(13,2));
 const withoutAudit=div(add(f(19,2),f(13,2)),two);
 const withPerfectAudit=div(add(f(19,2),f(7)),two);
 eq(withoutAudit,f(8));eq(withPerfectAudit,f(33,4));
 eq(sub(withPerfectAudit,withoutAudit),f(1,4));
 let previous=null;let slopeGrid=0,groundingGrid=0,finiteGrid=0;
 for(let k=0;k<=32;k++){
  const beta=f(16+k,8); // [2,6], evaluate restricted [2,4] below
  if(k<=16){
    const a=x(beta,1),b=x(beta,2);
    eq(a.value,eight);assert(cmp(b.q,one)>=0,"target anchor optimal quantity");assert(cmp(b.value,a.value)>=0,"capacity monotonic");
    if(previous!==null)assert(cmp(previous,b.value)>=0,"slope-envelope monotonicity");
    previous=b.value;slopeGrid++;
  }
  // More valuable capturable target qualification can complement a new physical slot
  const alpha=f(6+k,2),delta=f(1+k%4,2),v=f(1+k%5,2);
  const baseSmall=optimize(alpha,v,one).value,raisedSmall=optimize(add(alpha,delta),v,one).value;
  const baseLarge=optimize(alpha,v,two).value,raisedLarge=optimize(add(alpha,delta),v,two).value;
  assert(cmp(sub(raisedLarge,baseLarge),sub(raisedSmall,baseSmall))>=0,"grounding/embodiment increasing differences");
  groundingGrid++;
 }
 for(let i=1;i<=32;i++){
  const beta=f(16+i,8); // positivity and concavity sampled exactly
  const opt=x(beta,2);
  for(let j=0;j<=32;j++){
   const q=f(j,16);
   assert(cmp(opt.value,revenue(add(eight,beta),beta,q))>=0,"optimal production upper certificate");
   finiteGrid++;
  }
 }
 return {kind:"conditional synthetic uniform-price whole-service receipts, not observed robotics data",knownOneSlotPrice:"8",sourceDemandSlopeSet:["2","4"],retainedController:{capacityOneGross:"6",capacityTwoGross:"8",capacityTwoNetOfEmbodiment:"7"},sourceCost:"3/2",newEmbodimentCost:"1",worlds,policyAtCapacityOneSourceNet:"13/2",policyWithSourceAndNewBodyNetBounds:["13/2","19/2"],compareWithRetainedBodyNet:"7",perfectPreinvestmentAuditEqualPriorUpperValue:"1/4",independentSourceToEmbodimentComplementarityCanSwitchSign:true,slopeGrid,groundingGrid,finiteGrid,checks};
}
if(typeof module!=="undefined"){module.exports={model};if(require.main===module)console.log(JSON.stringify(model(),null,2));}
