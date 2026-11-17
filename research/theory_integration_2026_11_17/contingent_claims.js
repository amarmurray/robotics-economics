"use strict";
/* Synthetic complete-order qualification/financing comparator, 2026-11-17.
   No industrial calibration. All claim transfers risk-neutral at zero discount. */
function gcd(a,b){a=a<0n?-a:a;b=b<0n?-b:b;while(b){let t=a%b;a=b;b=t;}return a;}
function F(a,b=1){a=BigInt(a);b=BigInt(b);if(!b)throw Error("zero denominator");if(b<0n){a=-a;b=-b;}let g=gcd(a,b);return {n:a/g,d:b/g};}
const add=(a,b)=>F(a.n*b.d+b.n*a.d,a.d*b.d),sub=(a,b)=>add(a,F(-b.n,b.d));
const mul=(a,b)=>F(a.n*b.n,a.d*b.d),div=(a,b)=>F(a.n*b.d,a.d*b.n);
const lt=(a,b)=>a.n*b.d<b.n*a.d,eq=(a,b)=>a.n===b.n&&a.d===b.d;
const fmt=(a)=>a.d===1n?""+a.n:a.n+"/"+a.d;
const Z=F(0),I=F(1);
const terms={R:F(16),V:F(24),cost:F(2),pay:F(9,10),survive:F(9,10),eligible:F(1,2)};
const routes={shared:{p:F(3,4),cost:F(13),loss:F(4),q1:1},
              specialist:{p:F(9,10),cost:F(20),loss:F(0),q1:2}};
function metrics(name){
 const r=routes[name];if(!r)throw Error("unknown route");
 const n=add(I,terms.survive);
 const invoices=mul(mul(mul(r.p,n),terms.pay),terms.R);
 const surplus=mul(mul(r.p,n),sub(terms.V,mul(terms.pay,terms.R)));
 const privateGain=sub(mul(mul(r.p,n),sub(mul(terms.pay,terms.R),terms.cost)),add(r.cost,r.loss));
 const shortfall=sub(add(F(r.q1),r.cost),F(2));
 const incentiveCap=sub(I,div(terms.cost,mul(terms.pay,terms.R)));
 const cap=lt(terms.eligible,incentiveCap)?terms.eligible:incentiveCap;
 return {invoices,surplus,privateGain,shortfall,cap,pledge:mul(cap,invoices),jointFunding:add(surplus,mul(cap,invoices))};
}
const events=p=>[[false,sub(I,p)],[true,p]];
function scenario(name,deposit=Z,loan=Z,refundOnFailure=false){
 const r=routes[name],m=metrics(name);
 if(lt(deposit,Z)||lt(loan,Z)||lt(m.surplus,deposit)||lt(add(deposit,loan),m.shortfall))throw Error("deposit/credit infeasible");
 const claim=eq(loan,Z)?Z:div(loan,m.invoices);
 if(lt(m.cap,claim))throw Error("claims exceed eligible share/operating incentives");
 const rows=[];
 for(const [qual,pq] of events(r.p))
 for(const [active,ps] of events(terms.survive))
 for(const [paid2,p2] of events(terms.pay))
 for(const [paid3,p3] of events(terms.pay)){
  const prob=mul(mul(pq,ps),mul(p2,p3));
  const b2=qual?1:0,b3=qual&&active?1:0;
  const y2=b2&&paid2?1:0,y3=b3&&paid3?1:0;
  let cash=F(4),min=cash;
  const check=()=>{if(lt(cash,min))min=cash;};
  cash=sub(cash,F(2));check(); // t0 pay A cost
  cash=sub(add(cash,add(deposit,loan)),add(F(r.q1),r.cost));check(); // t1 qualify
  cash=sub(add(cash,F(12)),add(F(2),mul(F(b2),terms.cost)));check(); // t2 receive t0 A
  const kept=mul(sub(I,claim),terms.R);
  cash=sub(add(add(cash,F(r.q1===1?7:12)),mul(F(y2),kept)),add(F(2),mul(F(b3),terms.cost)));check(); // t3
  cash=add(add(cash,F(12)),mul(F(y3),kept));check(); // t4
  cash=add(cash,F(12)); // t5 settle t3 A
  if(refundOnFailure&&!qual){cash=sub(cash,deposit);check();} // return conditional pilot deposit after failed qualification
  const paid=mul(F(y2+y3),terms.R);
  const lender=sub(mul(claim,paid),loan);
  const buyer=sub(sub(mul(F(b2+b3),terms.V),paid),refundOnFailure&&!qual?Z:deposit);
  rows.push({prob,provider:cash,lender,buyer,min,orders:b2+b3,paidOrders:y2+y3,qualified:qual});
 }
 const sum=(k)=>rows.reduce((a,x)=>add(a,mul(x.prob,x[k])),Z);
 const prob=rows.reduce((a,x)=>add(a,x.prob),Z);
 const min=rows.reduce((a,x)=>lt(x.min,a)?x.min:a,F(4));
 return {claim,prob,rows,provider:sub(sum("provider"),F(44)),buyer:sum("buyer"),
   lender:sum("lender"),joint:sub(add(add(sum("provider"),sum("buyer")),sum("lender")),F(44)),min};
}
function snapshot(){
 const pack=(name,dep,loan)=>{
  const m=metrics(name),s=scenario(name,dep,loan),fields=["invoices","surplus","privateGain","shortfall","pledge","jointFunding"];
  const row=Object.fromEntries(fields.map(k=>[k,fmt(m[k])]));
  return {...row,claimFraction:fmt(s.claim),providerAfterFunding:fmt(s.provider),
    buyerAfterFunding:fmt(s.buyer),lenderAfterFunding:fmt(s.lender),jointValue:fmt(s.joint),minCash:fmt(s.min)};
 };
 const rs=scenario("shared",F(12),Z,true),rp=scenario("specialist",F(12),F(8),true);
 return {refundablePilot:{sharedProvider:fmt(rs.provider),sharedBuyer:fmt(rs.buyer),specialistProvider:fmt(rp.provider),specialistBuyer:fmt(rp.buyer),sharedMin:fmt(rs.min),specialistMin:fmt(rp.min),jointShared:fmt(rs.joint),jointSpecialist:fmt(rp.joint)},
  parameters:{payment:fmt(terms.pay),survival:fmt(terms.survive),pledgeCap:fmt(terms.eligible),
     price:fmt(terms.R),buyerValue:fmt(terms.V)},
     shared:pack("shared",F(12),Z),specialist:pack("specialist",F(12),F(8))};
}
module.exports={F,add,sub,mul,div,lt,eq,fmt,metrics,scenario,snapshot,terms,routes};