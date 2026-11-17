"use strict";
const assert=require("node:assert/strict"),x=require("./contingent_claims.js");
let count=0;
const ok=(a)=>{assert.ok(a);count++;};
const is=(a,b)=>{assert.equal(x.fmt(a),b);count++;};
const reject=(f)=>{assert.throws(f);count++;};
const {F,metrics,scenario}=x;
is(x.add(F(1,3),F(1,6)),"1/2");is(x.mul(F(3,4),F(9,10)),"27/40");
const a=metrics("shared"),b=metrics("specialist");
for(const [v,s] of [[a.shortfall,"12"],[b.shortfall,"20"],[a.privateGain,"67/100"],[b.privateGain,"301/250"],
[a.invoices,"513/25"],[b.invoices,"3078/125"],[a.pledge,"513/50"],[b.pledge,"1539/125"],
[a.surplus,"342/25"],[b.surplus,"2052/125"]])is(v,s);
ok(x.lt(a.pledge,a.shortfall));ok(x.lt(b.pledge,b.shortfall));
ok(!x.lt(b.jointFunding,b.shortfall));
const sa=scenario("shared",F(12),F(0)),sp=scenario("specialist",F(12),F(8));
for(const [v,s] of [[sa.prob,"1"],[sp.prob,"1"],[sa.provider,"1267/100"],[sp.provider,"3301/250"],
[sa.buyer,"42/25"],[sp.buyer,"552/125"],[sa.lender,"0"],[sp.lender,"0"],
[sp.claim,"500/1539"],[sa.min,"0"],[sp.min,"0"],[sa.joint,"287/20"],[sp.joint,"881/50"]])is(v,s);
ok(x.lt(sa.provider,sp.provider));ok(x.lt(sa.buyer,sp.buyer));
reject(()=>scenario("shared",F(0),F(12)));
reject(()=>scenario("specialist",F(12),F(0)));
reject(()=>scenario("shared",F(14),F(0)));
for(const k of ["shared","specialist"]){
 const s=scenario(k,F(12),k==="shared"?F(0):F(8));
 for(const z of s.rows)ok(!x.lt(z.min,F(0)));
}
const rsh=scenario("shared",F(12),F(0),true),rsp=scenario("specialist",F(12),F(8),true);
is(rsh.provider,"967/100");is(rsh.buyer,"117/25");
is(rsp.provider,"3001/250");is(rsp.buyer,"702/125");
is(rsh.joint,"287/20");is(rsp.joint,"881/50");
is(rsh.min,"0");is(rsp.min,"0");
ok(x.lt(rsh.provider,rsp.provider));ok(x.lt(rsh.buyer,rsp.buyer));
for(const v of [rsh,rsp])for(const z of v.rows)ok(!x.lt(z.min,F(0)));
console.log("PASS "+count+" exact assertions");