// Exact finite synthetic diagnostic for adaptive qualification menus.
// No field calibration, no device actuation, and no safety approval.
const model = (function main() {
 "use strict";
 function gcd(a,b){a=a<0n?-a:a;while(b){let z=a%b;a=b;b=z;}return a;}
 class F{
   constructor(n,d=1n){n=BigInt(n);d=BigInt(d);if(d===0n)throw Error("zero denominator");if(d<0n){n=-n;d=-d;}let g=gcd(n,d);this.n=n/g;this.d=d/g;}
   add(x){return new F(this.n*x.d+x.n*this.d,this.d*x.d);}
   sub(x){return new F(this.n*x.d-x.n*this.d,this.d*x.d);}
   mul(x){return new F(this.n*x.n,this.d*x.d);}
   div(x){return new F(this.n*x.d,this.d*x.n);}
   cmp(x){let z=this.n*x.d-x.n*this.d;return z<0n?-1:z>0n?1:0;}
   str(){return this.n.toString()+"/"+this.d.toString();}
 }
 const f=(n,d=1)=>new F(n,d),zero=f(0),one=f(1),two=f(2),four=f(4),c=f(1,5);
 const max=(a,b)=>a.cmp(b)>=0?a:b, min=(a,b)=>a.cmp(b)<=0?a:b;
 let assertions=0, cases=0;
 const eq=(a,b,label)=>{assertions++;if(a.cmp(b)!==0)throw Error(label+": "+a.str()+" != "+b.str());};
 function enumerate(p,q,t){
  // P11=t, P10=p-t, P01=q-t, P00=1-p-q+t.
  const P=[one.sub(p).sub(q).add(t),q.sub(t),p.sub(t),t];
  if(P.some(x=>x.cmp(zero)<0))throw Error("negative mass");
  eq(P.reduce((a,b)=>a.add(b),zero),one,"mass");
  const pay=[two,four,four,four];
  const upfront=P.reduce((v,m,i)=>v.add(m.mul(pay[i])),zero).sub(c.mul(two));
  const only=two.add(two.mul(p)).sub(c);
  const secondPay=P[1].mul(two).sub(P[0].add(P[1]).mul(c));
  const staged=only.add(max(zero,secondPay));
  // Analytic formulas including a competent fallback and testing costs.
  const ahead=two.add(two.mul(p)).add(two.mul(q)).sub(two.mul(t)).sub(c.mul(two));
  const astaged=two.add(two.mul(p)).sub(c).add(max(zero,two.mul(q.sub(t)).sub(c.mul(one.sub(p)))));
  eq(upfront,ahead,"upfront identity"); eq(staged,astaged,"stage identity");
  if(staged.cmp(only)<0||staged.cmp(upfront)<0)throw Error("nested feasible menu not dominating");
  cases++;
  return {t:t.str(),one:only.str(),upfront:upfront.str(),staged:staged.str()};
 }
 const p=f(1,2),q=f(1,2);
 const twoWorlds={disjoint:enumerate(p,q,zero),independent:enumerate(p,q,f(1,4)),concordant:enumerate(p,q,f(1,2))};
 eq(f(37,10),twoWorlds.disjoint?f(37,10):zero,"sentinel");
 if(twoWorlds.disjoint.staged!=="37/10"||twoWorlds.concordant.staged!=="14/5"||twoWorlds.disjoint.upfront!=="18/5"||twoWorlds.concordant.upfront!=="13/5")throw Error("two-world outcome mismatch");
 for(let i=0;i<=4;i++)for(let j=0;j<=4;j++){
   const pp=f(i,4),qq=f(j,4);
   for(let k=Math.max(0,i+j-4);k<=Math.min(i,j);k++)enumerate(pp,qq,f(k,4));
 }
 function parity(val){
   const states=[];
   for(let i=0;i<8;i++){let b=[(i>>2)&1,(i>>1)&1,i&1];if((b[0]+b[1]+b[2])%2===val)states.push(b);}
   const n=BigInt(states.length);
   const marg=[0,1,2].map(i=>f(states.filter(b=>b[i]).length,n));
   const pairs=[[0,1],[0,2],[1,2]].map(([i,j])=>f(states.filter(b=>b[i]&&b[j]).length,n));
   const union=f(states.filter(b=>b.some(Boolean)).length,n);
   marg.forEach(v=>eq(v,f(1,2),"parity marginal"));
   pairs.forEach(v=>eq(v,f(1,4),"parity pair"));
   return {support:states.map(v=>v.join("")),marginal:marg.map(v=>v.str()),pair:pairs.map(v=>v.str()),union:union.str(),three_test_menu:two.add(two.mul(union)).sub(c.mul(f(3))).str()};
 }
 const even=parity(0),odd=parity(1);
 if(even.three_test_menu!=="29/10"||odd.three_test_menu!=="17/5")throw Error("parity mismatch");
 return {model:"synthetic policy-closed whole-network accepted-service menu",prices:"normalized hypothetical whole-service contribution; no benchmark-to-dollar mapping",two_worlds:twoWorlds,three_policy_couplings:{even,odd},checks:{exact_fraction_assertions:assertions,pairwise_grid_cases:cases,field_data:false,physical_approval:false}};
})()

if (typeof process !== 'undefined' && typeof console !== 'undefined') console.log(JSON.stringify(model,null,2));
