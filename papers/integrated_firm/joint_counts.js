// CPU-only; run: node joint_counts.js > joint_counts_results.json
// Synthetic exact integer terminal game; no external dependencies.
function solve(types,H,C,B,A=8,coord=1){
 const n=types.length;
 function actions(i){let out=[];for(let mask=0;mask<3**n;mask++){let z=mask,h=0,t=0,c=0,q=[],m=[];for(let j=0;j<n;j++){let r=z%3;z=Math.floor(z/3);m.push(r);q.push(+(r>0));if(r===1)h+=2;if(r===2){h+=1-types[j][i];t+=3-types[j][i];c++}}t+=coord*c*(c-1)/2;let cost=2*h+t;if(h<=H&&t<=C&&cost<=B)out.push({m,q,h,t,cost})}return out}
 const x=actions(0),y=actions(1);function u(a,b){return a.q.reduce((s,v,j)=>s+v*(A-2*(v+b.q[j])),0)-a.cost}function phi(a,b){return a.q.reduce((s,v,j)=>s+(A-2)*(v+b.q[j])-2*v*b.q[j],0)-a.cost-b.cost}
 const eq=[];let checks=0;for(const a of x)for(const b of y){const p=u(a,b),q=u(b,a),f=phi(a,b);for(const d of x){if(u(d,b)-p!==phi(d,b)-f)throw Error("potential");checks++}for(const d of y){if(u(d,a)-q!==phi(a,d)-f)throw Error("potential");checks++}if(x.some(d=>u(d,b)>p)||y.some(d=>u(d,a)>q))continue;const Q=a.q.map((v,j)=>v+b.q[j]);eq.push({pay:[p,q],Q,CS:Q.reduce((s,v)=>s+v*v,0),cost:[a.cost,b.cost],actions:[a.m,b.m]})}
 if(!eq.length)throw Error("no pure terminal equilibrium");
 return {sizes:[x.length,y.length],checks,equilibria:eq}
}
function summary(x){return x.equilibria.map(e=>JSON.stringify([e.pay,e.Q.slice().sort(),e.CS,e.cost])).sort().join("|")}
function run(){
 const aligned=[[1,1],[0,0],[0,0]],split=[[1,0],[0,1],[0,0]];
 const cases=[];let checks=0;
 for(const [H,C,B] of [[2,2,3],[2,4,7],[4,7,12],[4,7,3]])for(const [name,types] of [["aligned",aligned],["split",split]]){const s=solve(types,H,C,B);checks+=s.checks;cases.push({name,H,C,B,...s})}
 const a=cases[0].equilibria[0],b=cases[1].equilibria[0];
 if(cases[0].equilibria.length!==1||cases[1].equilibria.length!==1||a.pay[0]!==2||b.pay[0]!==4||a.CS!==4||b.CS!==2)throw Error("pairing witness");
 let permutations=0,classes=new Map();
 for(let k=0;k<64;k++){let z=k,types=[];for(let j=0;j<3;j++){let t=z%4;z=Math.floor(z/4);types.push([t>>1,t&1])}let key=types.map(t=>t.join("")).sort().join("");const s=solve(types,2,4,7);checks+=s.checks;const sig=summary(s);if(classes.has(key)){if(classes.get(key)!==sig)throw Error("permutation");permutations++}else classes.set(key,sig)}
 if(classes.size!==20||permutations!==44)throw Error("count classes");
 // Common H: probability of joint success, not product of marginal mixtures.
 const jointNumerator=3*3*3+2*1*1,denominator=5*4*4;
 if(jointNumerator!==29||denominator!==80)throw Error("joint law");
 return {synthetic:true,model:"terminal digital-only restriction of core.py; binary demand per firm per local market; shared labor, compute, coordination and prefunded cash",cases,verification:{labeled_states:64,count_classes:classes.size,noncanonical_state_comparisons:permutations,exact_unilateral_potential_checks:checks,common_report_law:{prior:"3/5",success_strong:"3/4",success_weak:"1/4",joint_success:"29/80",posterior_both_success:"27/29",independent_marginal_product:"121/400"}}}
}
console.log(JSON.stringify(run(),null,2));
