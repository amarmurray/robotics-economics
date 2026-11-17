"use strict";
const gcd=(a,b)=>{a=a<0n?-a:a;b=b<0n?-b:b;while(b){const t=a%b;a=b;b=t;}return a;};
function F(a,b=1){a=BigInt(a);b=BigInt(b);if(!b)throw Error("zero");if(b<0n){a=-a;b=-b;}const g=gcd(a,b);return {n:a/g,d:b/g};}
const add=(a,b)=>F(a.n*b.d+b.n*a.d,a.d*b.d),sub=(a,b)=>add(a,F(-b.n,b.d));
const mul=(a,b)=>F(a.n*b.n,a.d*b.d),div=(a,b)=>F(a.n*b.d,a.d*b.n);
const lt=(a,b)=>a.n*b.d<b.n*a.d, min=(a,b)=>lt(a,b)?a:b,max=(a,b)=>lt(a,b)?b:a;
const fmt=a=>a.d===1n?""+a.n:a.n+"/"+a.d,Z=F(0),ONE=F(1);
const t={s:F(9,10),r2:F(9,10),r3:F(9,10),R:F(16),V:F(24),k:F(2),theta:F(1,2)};
const routes={shared:{p:F(3,4),K:F(13),d:F(4),a:F(3),q1:1},specialist:{p:F(9,10),K:F(20),d:Z,a:Z,q1:2}};
const overlap=(x,y)=>max(Z,sub(add(x,y),ONE));
function bounds(name,aOverride){
 const j=routes[name],a=aOverride===undefined?j.a:aOverride,ps=mul(j.p,t.s),n=add(j.p,ps);
 const lo=mul(t.R,add(overlap(j.p,t.r2),overlap(ps,t.r3)));
 const hi=mul(t.R,add(min(j.p,t.r2),min(ps,t.r3)));
 const ind=mul(t.R,add(mul(j.p,t.r2),mul(ps,t.r3)));
 const umin=sub(mul(t.V,n),hi),mmin=mul(t.theta,lo);
 const real=sub(sub(mul(sub(t.V,t.k),n),add(j.K,j.d)),a);
 const margin2=sub(mul(mul(sub(ONE,t.theta),t.R),overlap(j.p,t.r2)),mul(t.k,j.p));
 const margin3=sub(mul(mul(sub(ONE,t.theta),t.R),overlap(ps,t.r3)),mul(t.k,ps));
 return {n,lo,hi,ind,umin,mmin,capacity:add(umin,mmin),real,margin2,margin3};
}
function contract(name,P,L,refundable=false,aOverride){
 const j=routes[name],a=aOverride===undefined?j.a:aOverride,b=bounds(name,a);
 const D=add(sub(add(j.K,F(j.q1)),F(2)),a),effective=mul(P,refundable?j.p:ONE);
 if(lt(P,Z)||lt(L,Z)||lt(add(P,L),D)||lt(b.umin,effective)||lt(b.mmin,L))throw Error("robust funding/participation fails");
 const share=lt(Z,L)?div(L,b.lo):Z;
 if(lt(t.theta,share)||lt(b.margin2,Z)||lt(b.margin3,Z))throw Error("B service incentive fails");
 const providerCore=sub(sub(sub(mul(sub(ONE,share),b.lo),mul(t.k,b.n)),add(j.K,j.d)),a);
 return {D,P,L,share,refundable,a,providerMin:add(providerCore,add(effective,L)),
   buyerMin:sub(b.umin,effective),lenderMin:sub(mul(share,b.lo),L)};
}
function minCash(name,P,L,refundable=false,aOverride){
 const j=routes[name],f=contract(name,P,L,refundable,aOverride);let mn=null;
 for(let q=0;q<2;q++)for(let s=0;s<2;s++)for(let y2=0;y2<2;y2++)for(let y3=0;y3<2;y3++){
  const b2=q,b3=q*s;let cash=F(4);
  const record=()=>{mn=mn===null?cash:min(mn,cash);};record();
  cash=sub(cash,F(2));record();
  cash=sub(add(cash,add(P,L)),add(add(F(j.q1),j.K),f.a));record();
  cash=sub(add(cash,F(12)),add(F(2),mul(t.k,F(b2))));record();
  cash=sub(add(add(cash,F(j.q1===1?7:12)),mul(mul(F(b2*y2),t.R),sub(ONE,f.share))),add(F(2),mul(t.k,F(b3))));record();
  cash=add(add(cash,F(12)),mul(mul(F(b3*y3),t.R),sub(ONE,f.share)));record();
  cash=add(cash,F(12));record();
  if(refundable&&!q){cash=sub(cash,P);record();}
 }return mn;
}
function snapshot(){
 const policies=[["shared",F(11),F(4),false,undefined],["specialist",F(12),F(8),false,undefined],["shared",F(14),F(8),true,F(10)]];
 const pack=obj=>Object.fromEntries(Object.entries(obj).map(([k,v])=>[k,v&&typeof v==="object"&&"n"in v?fmt(v):v]));
 return policies.map(([name,P,L,refund,a])=>({name,case:a===undefined?"base":"A_customer_value_10",
   bounds:pack(bounds(name,a)),contract:pack(contract(name,P,L,refund,a)),minCash:fmt(minCash(name,P,L,refund,a))}));
}
module.exports={F,fmt,bounds,contract,minCash,snapshot,routes,t};
