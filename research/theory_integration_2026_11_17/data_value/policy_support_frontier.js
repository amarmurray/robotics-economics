// Conditional synthetic model. Node.js: node policy_support_frontier.js
function calculate(){
 const gcd=(a,b)=>{while(b!==0n){const x=a%b;a=b;b=x}return a<0n?-a:a};
 const F=(n,d=1)=>{n=BigInt(n);d=BigInt(d);const g=gcd(n<0n?-n:n,d);return {n:n/g,d:d/g}};
 const add=(a,b)=>F(a.n*b.d+b.n*a.d,a.d*b.d),mul=(a,b)=>F(a.n*b.n,a.d*b.d),sub=(a,b)=>add(a,F(-b.n,b.d)),show=a=>a.d===1n?a.n.toString():`${a.n}/${a.d}`;
 const val=(c,u,cost,q=F(1,4))=>sub(add(mul(sub(F(1),q),c),mul(q,u)),cost);
 return {base:[show(val(F(2),F(0),F(1,10))),show(val(F(2),F(4),F(1,10)))],copy:[show(val(F(3),F(0),F(3,20))),show(val(F(3),F(4),F(3,20)))],ground:[show(val(F(2),F(3),F(3,20))),show(val(F(2),F(4),F(3,20)))],body:show(sub(F(11,5),F(1,4))),shifted:show(val(F(3),F(0),F(3,20),F(1,2))),specialist:show(F(2)),retained:show(F(1))};
}
function test(){
 const a=calculate(),b={base:["7/5","12/5"],copy:["21/10","31/10"],ground:["21/10","47/20"],body:"39/20",shifted:"27/20",specialist:"2",retained:"1"};let n=0;
 for(const [k,v]of Object.entries(b)){if(Array.isArray(v)){v.forEach((item,i)=>{if(a[k][i]!==item)throw Error(k+" "+i);n++})}else{if(a[k]!==v)throw Error(k);n++}}
 for(let y=0;y<=4;y++){const base=.75*2+.25*y-.1,copy=.75*3+.25*y-.15,ground=.75*2+.25*y-.15;if(Math.abs(copy-base-.7)>1e-10)throw Error("uplift");if(y>=3&&ground<2.1-1e-10)throw Error("ground");n+=2}
 return {date:"2026-11-18",checks:n,results:a,interpretation:"exact synthetic fractions and five bounded continuation comparisons",field_data:false,approval:false,novelty:false};
}
if(typeof require!== 'undefined' && require.main===module) console.log(JSON.stringify(test(),null,2));
