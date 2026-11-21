/* Synthetic original-buyer paid-program occupation support audit.
   Run: node policy_occupancy_pooling.js. Numerical checks, NOT mathematical proof. */
(function(){
 "use strict";
 let checks=0,one=0,two=0;
 function assert(x,msg){checks++;if(!x)throw Error(msg)}
 for(let ps=0;ps<=10;ps++)for(let pr=0;pr<=10;pr++)
 for(let qs=0;qs<=10;qs++)for(let qr=0;qr<=10;qr++){
  const i=ps>=pr?0:1,j=qs>=qr?0:1;
  const ap=Math.abs((i===0?ps:pr)-(i===0?qs:qr));
  const aq=Math.abs((j===0?ps:pr)-(j===0?qs:qr));
  const D=Math.max(ps,pr)-Math.max(qs,qr);
  assert(D<=ap,"upper");assert(-D<=aq,"lower");
  assert(Math.abs(D)<=Math.max(ap,aq),"optimized");
  const m=(99*Math.abs(ps-qs)+Math.abs(pr-qr))/100;
  const C=(i||j)?100:100/99;
  assert(Math.max(ap,aq)<=C*m+1e-10,"occupancy support");
  one++;
 }
 for(let p1=0;p1<=10;p1++)for(let p2=0;p2<=10;p2++)
 for(let q1=0;q1<=10;q1++)for(let q2=0;q2<=10;q2++){
  assert(Math.abs(p1*p2-q1*q2)<=10*Math.abs(p1-q1)+q1*Math.abs(p2-q2),"two-step");
  two++;
 }
 assert(45-(-15)===60,"third dividend");
 assert(Math.max(40,0)===40&&Math.max(40,100)===100,"retained fallback");
 assert(Math.max(55,55)===55,"E");
 assert(1/100<60/100,"naive invalid");
 assert(100*(1/100)>=60/100,"correct coverage");
 const record={scope:"synthetic one-original-buyer paid outcome only",one_stage_cases:one,two_stage_cases:two,assertions:checks,passed:true,cohort:{D2:-0.15,Dall:0.45,unmeasured_tail:0.60,SG_low:0.40,SG_full:1,E:0.55},support:{logging_risky:0.01,logged_TV:0.01,optimizer_density_ratio:100,valid_upper_error:1}};
 if(typeof module!=="undefined"&&typeof require!=="undefined"&&require.main===module)console.log(JSON.stringify(record,null,2));
 return record;
})()

