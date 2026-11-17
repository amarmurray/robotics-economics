"use strict";const assert=require("node:assert/strict"),m=require("./participation_coupling.js");
const {F,fmt,bounds,contract,minCash}=m;let n=0;
function eq(x,y){assert.equal(fmt(x),fmt(y));n++;}
const a=bounds("shared"),b=bounds("specialist");
for(const [x,y] of [[a.n,F(57,40)],[a.lo,F(98,5)],[a.hi,F(114,5)],[a.ind,F(513,25)],[a.umin,F(57,5)],[a.mmin,F(49,5)],[a.capacity,F(106,5)],[a.real,F(227,20)],
[b.n,F(171,100)],[b.lo,F(604,25)],[b.hi,F(684,25)],[b.ind,F(3078,125)],[b.umin,F(342,25)],[b.mmin,F(302,25)],[b.capacity,F(644,25)],[b.real,F(881,50)]])eq(x,y);
for(const [name,P,L] of [["shared",F(11),F(4)],["specialist",F(12),F(8)]]){
 const c=contract(name,P,L);eq(c.lenderMin,F(0));eq(minCash(name,P,L),F(0));eq(minCash(name,P,L,true),F(0));
 assert.ok(c.buyerMin.n>=0n&&c.providerMin.n>=0n);n++;
}
assert.throws(()=>contract("shared",F(12),F(3)));n++;assert.throws(()=>contract("specialist",F(12),F(13)));n++;
const high=bounds("shared",F(10));eq(high.real,F(87,20));assert.ok(high.capacity.n/high.capacity.d<22n);n++;
assert.throws(()=>contract("shared",F(14),F(8),false,F(10)));n++;
const c=contract("shared",F(14),F(8),true,F(10));
for(const [x,y] of [[c.D,F(22)],[c.providerMin,F(1,4)],[c.buyerMin,F(9,10)],[c.lenderMin,F(0)],[c.share,F(20,49)],[minCash("shared",F(14),F(8),true,F(10)),F(0)]])eq(x,y);
console.log("PASS",n,"exact scoped checks");
