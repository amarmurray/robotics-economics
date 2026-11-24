"use strict";
const run = function(){
let checks=0;const ck=(x,m)=>{checks++;if(!x)throw Error(m)};
const N=8;let laws=0,low=99,high=-99,shortLow=99,shortHigh=-99;
const extrema={p1:[Infinity,-Infinity],p4:[Infinity,-Infinity],short4:[Infinity,-Infinity],audit4:[Infinity,-Infinity]};
const record=(key,v)=>{extrema[key][0]=Math.min(extrema[key][0],v);extrema[key][1]=Math.max(extrema[key][1],v)};
const payoff=(p,q,shortq)=>({R:5*N,B:4*N+p*q,D:N/2+p*N,X:7*N/2+p*3,E:11*N/2,shortB:4*N+p*shortq});
function recurse(a,remaining){
if(a.length<7){for(let j=0;j<=remaining;j++)recurse([...a,j],remaining-j);return}
a=[...a,remaining];
const marg=[1,2,4].map(b=>a.reduce((s,c,i)=>s+((i&b)?c:0),0));
if(marg.some(x=>x!==6))return;
laws++;const q=a[7],qa=a[3]+a[7];
ck(q>=2&&q<=6,"Frechet triple");ck(qa>=4&&qa<=6&&qa>=q,"shortened queue coupled event");
low=Math.min(low,q);high=Math.max(high,q);shortLow=Math.min(shortLow,qa);shortHigh=Math.max(shortHigh,qa);
for(let p=0;p<=12;p++){
const v=payoff(p,q,qa);
const g=Math.max(v.R,v.B,v.D),xs=Math.max(v.R,v.X),e=Math.max(v.R,v.E),all=Math.max(g,xs,e);
ck(g>=v.R&&all>=g&&all>=xs&&all>=e,"optional baseline");
ck(v.shortB>=v.B,"coupled clearance");
ck(v.B-v.E===p*q-12,"threshold");
if(p===1){ck(g===40&&all===44,"incumbent audit identical");record("p1",g)}
if(p===4){record("p4",g);record("short4",Math.max(v.R,v.D,v.shortB));if(q>=4){ck(g-e>=4,"joint audit cert");record("audit4",g)}}
if(p===6)ck(v.D>v.E,"deliberate choice possible");
}
}
recurse([],N);
ck(low===2&&high===6&&shortLow===4&&shortHigh===6,"sharp attained");
ck(extrema.p4[0]===40&&extrema.p4[1]===56,"grounding range");
ck(extrema.short4[0]===48&&extrema.short4[1]===56,"queue range");
ck(extrema.audit4[0]===48,"audit lower");
for(let q=2;q<=6;q++){
let b=32+4*q,k=32+4*(8-q);ck(Math.max(b,k)>=48,"law-informed lower");ck((b+k)/2===48,"mixture only if admitted");
}
return {synthetic:true,denominator:N,compatible_integer_laws:laws,assertions:checks,original_joint_range:[low,high].map(x=>x/N),short_queue_joint_range:[shortLow,shortHigh].map(x=>x/N),grounding_p1:extrema.p1.map(x=>x/N),grounding_p4:extrema.p4.map(x=>x/N),short_queue_p4:extrema.short4.map(x=>x/N),audited_p4:extrema.audit4.map(x=>x/N),independent_E:5.5,robust_audit_margin:0.5};
};
console.log(JSON.stringify(run(),null,2));
