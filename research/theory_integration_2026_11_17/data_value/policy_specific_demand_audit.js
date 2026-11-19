"use strict";
// Self-contained exact arithmetic: node policy_specific_demand_audit.js
const economicCertificate = function economicCertificate(){
 const gcd=(a,b)=>{a=a<0n?-a:a;b=b<0n?-b:b;while(b){const t=a%b;a=b;b=t;}return a||1n;};
 const Q=(n,d=1n)=>{n=BigInt(n);d=BigInt(d);if(d<0n){n=-n;d=-d;}const k=gcd(n,d);return[n/k,d/k];};
 const add=(a,b)=>Q(a[0]*b[1]+b[0]*a[1],a[1]*b[1]);
 const neg=a=>Q(-a[0],a[1]),sub=(a,b)=>add(a,neg(b));
 const mul=(a,b)=>Q(a[0]*b[0],a[1]*b[1]),div=(a,b)=>Q(a[0]*b[1],a[1]*b[0]);
 const cmp=(a,b)=>{const x=a[0]*b[1]-b[0]*a[1];return x<0n?-1:x>0n?1:0;};
 const fmt=a=>a[1]===1n?String(a[0]):String(a[0])+"/"+String(a[1]);
 const two=Q(2),three=Q(3),four=Q(4),quarter=Q(1,4),retained=Q(7);
 const X=g=>add(add(Q(19,4),div(g,two)),div(mul(sub(three,g),sub(three,g)),sub(four,mul(two,g))));
 const G=g=>sub(div(sub(Q(65),g),Q(8)),Q(11,10));
 const E=g=>sub(sub(Q(9),div(g,four)),Q(11,5));
 const D=g=>sub(X(g),G(g));
 const check=(x,m)=>{if(!x)throw Error(m);};
 check(fmt(X(quarter))==="197/28","X r=+1/2 lower");
 check(fmt(G(quarter))==="1119/160","G r=+1/2 upper");
 check(fmt(E(quarter))==="539/80","E r=+1/2 upper");
 check(fmt(G(neg(quarter)))==="1129/160","G r=-1/2 lower");
 check(fmt(X(neg(quarter)))==="251/36","X r=-1/2 upper");
 check(fmt(E(Q(-3,4)))==="559/80","E r=-1/2 upper");
 check(cmp(X(quarter),G(quarter))>0&&cmp(X(quarter),E(quarter))>0&&cmp(X(quarter),retained)>0,"X certificate");
 check(cmp(G(neg(quarter)),X(neg(quarter)))>0&&cmp(G(neg(quarter)),E(Q(-3,4)))>0&&cmp(G(neg(quarter)),retained)>0,"G certificate");
 check(fmt(X(Q(-1)))==="83/12"&&fmt(G(Q(1)))==="69/10"&&fmt(E(Q(1)))==="131/20","no transport bounds");
 let checks=9,gridCases=0;
 for(let j=-6;j<=6;j++){
   const r=Q(j,8),lo=sub(r,quarter),hi=add(r,quarter),dLo=D(lo),dHi=D(hi);
   for(let k=0;k<=4;k++)for(let l=0;l<=4;l++){
     const gx=add(lo,Q(k,8)),gg=add(lo,Q(l,8)),actual=sub(X(gx),G(gg));
     check(cmp(actual,dLo)>=0&&cmp(actual,dHi)<=0,"bound on rectangular shocks");
     checks++;gridCases++;
   }
   check(cmp(D(lo),dLo)===0&&cmp(D(hi),dHi)===0,"sharp endpoint equality");
   checks+=2;
 }
 check(fmt(sub(X(quarter),retained))==="1/28","X improvement");
 check(fmt(sub(G(neg(quarter)),retained))==="9/160","G improvement");
 checks+=2;
 return {
  context:"Conditional normalized synthetic buyer markets; price anchors and physical policy validity assumed",
  arithmetic:"BigInt exact fractions",checks,gridCases,
  no_transport:{min_X:fmt(X(Q(-1))),min_G:fmt(G(Q(1))),min_E:fmt(E(Q(1))),R:fmt(retained)},
  r_positive:{benchmark_r:"1/2",delta:"1/4",X_lower:fmt(X(quarter)),G_upper:fmt(G(quarter)),E_upper:fmt(E(quarter)),R:fmt(retained),X_gain_before_audit:fmt(sub(X(quarter),retained))},
  r_negative:{benchmark_r:"-1/2",delta:"1/4",G_lower:fmt(G(neg(quarter))),X_upper:fmt(X(neg(quarter))),E_upper:fmt(E(Q(-3,4))),R:fmt(retained),G_gain_before_audit:fmt(sub(G(neg(quarter)),retained))},
  sharp_difference:"[D(clamp(L-delta)), D(clamp(U+delta))]",
  limitations:"Finite arithmetic checks are not analytic proof, observed robot economics or independent novelty review."
 };
};
const result=economicCertificate();
if (typeof module!=="undefined") module.exports={economicCertificate};
if(typeof require!=="undefined" && require.main===module) process.stdout.write(JSON.stringify(result,null,2)+"\n");
