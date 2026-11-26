// Run: node joint_game.js > joint_game_results.json
const K=require('./joint_transition.js')();
function run(K){
 const gcd=(a,b)=>b?gcd(b,a%b):a<0n?-a:a;
 const F=(n,d=1n)=>{if(d<0n){n=-n;d=-d}const g=gcd(n,d);return [n/g,d/g]};
 const add=(a,b)=>F(a[0]*b[1]+b[0]*a[1],a[1]*b[1]);
 const mul=(a,b)=>F(a[0]*b[0],a[1]*b[1]);
 const cmp=(a,b)=>{const x=a[0]*b[1]-b[0]*a[1];return x>0n?1:x<0n?-1:0};
 const fmt=a=>a.join("/");
 function solve(initial,horizon,cap,rule,budget=160000){
  const memo=new Map(),stats={states:0,terminal_classes:0,profiles:0,deviations:0,mixed:0,missing:0},summaries=[];
  function equilibria(A){
   const R=A.length,C=A[0].length,br0=Array(C).fill(null),br1=Array(R).fill(null),eq=[];
   for(let i=0;i<R;i++)for(let j=0;j<C;j++){let v=A[i][j];if(!br0[j]||cmp(v[0],br0[j])>0)br0[j]=v[0];if(!br1[i]||cmp(v[1],br1[i])>0)br1[i]=v[1]}
   for(let i=0;i<R;i++)for(let j=0;j<C;j++)if(!cmp(A[i][j][0],br0[j])&&!cmp(A[i][j][1],br1[i]))eq.push({p:[[i,F(1n)]],q:[[j,F(1n)]],v:A[i][j]});
   if(!eq.length){
    // A verified 2x2 support search, not a general mixed equilibrium solver.
    const sub=(a,b)=>add(a,F(-b[0],b[1]));
    const div=(a,b)=>F(a[0]*b[1],a[1]*b[0]);
    const between=x=>cmp(x,F(0n))>0&&cmp(x,F(1n))<0;
    const val=(x,y,z)=>add(mul(x,z),mul(y,sub(F(1n),z)));
    outer:for(let i=0;i<R;i++)for(let k=i+1;k<R;k++)for(let j=0;j<C;j++)for(let l=j+1;l<C;l++){
     const a=sub(A[i][j][0],A[k][j][0]),b=sub(A[i][l][0],A[k][l][0]),c=sub(A[i][j][1],A[i][l][1]),d=sub(A[k][j][1],A[k][l][1]);
     if(!cmp(a,b)||!cmp(c,d))continue;
     const q=div(F(-b[0],b[1]),sub(a,b)),p=div(F(-d[0],d[1]),sub(c,d));if(!between(p)||!between(q))continue;
     const u=val(A[i][j][0],A[i][l][0],q),v=val(A[i][j][1],A[k][j][1],p);
     if(A.some(row=>cmp(val(row[j][0],row[l][0],q),u)>0))continue;
     if(A[i].some((_,x)=>cmp(val(A[i][x][1],A[k][x][1],p),v)>0))continue;
     eq.push({p:[[i,p],[k,sub(F(1n),p)]],q:[[j,q],[l,sub(F(1n),q)]],v:[u,v]});stats.mixed++;break outer;
    }
   }
   for(const e of eq){for(let i=0;i<R;i++){let u=e.q.reduce((a,[j,p])=>add(a,mul(p,A[i][j][0])),F(0n));if(cmp(u,e.v[0])>0)throw Error("player 0 deviation");stats.deviations++}for(let j=0;j<C;j++){let u=e.p.reduce((a,[i,p])=>add(a,mul(p,A[i][j][1])),F(0n));if(cmp(u,e.v[1])>0)throw Error("player 1 deviation");stats.deviations++}}
   return eq;
  }
  function select(eq){return eq.reduce((a,b)=>{const c=cmp(add(b.v[0],b.v[1]),add(a.v[0],a.v[1]));return rule*c>0||(c===0&&cmp(b.v[0],a.v[0])>0)?b:a})}
  const show=x=>({service:x.p.m,retain:x.p.r,research:x.r.kind,target:x.r.target,method:x.r.method,lab:x.lab,build:x.build,cost:x.cost});
  function V(s,h,root=false){
   s=K.sortState(s);
   const key=h===1?JSON.stringify([h,s.sites.map(x=>x.map(y=>y[0])),s.firms.map(f=>[f.B,f.lab,f.ref]),s.market]):JSON.stringify([h,s]);
   if(memo.has(key))return memo.get(key);
   stats.states++;if(h===1)stats.terminal_classes++;
   const aa=K.actions(s,0,h===1,cap),bb=K.actions(s,1,h===1,cap);
   const A=aa.map(a=>bb.map(b=>{
    if(++stats.profiles>budget)throw Error("profile budget reached");
    if(h===1){const direct=[a,b].map((x,i)=>F(BigInt(s.firms[i].B+s.firms[i].ref-x.cost+x.p.m.reduce((v,m,j)=>v+(m===-2?0:(s.market?12:8)-2*(1+ +([b,a][i].p.m[j]!==-2))),0))));if(K.checked){const t=K.reference(s,[a,b],true);if(t.map.size!==1)throw Error("terminal random");const [key,w]=[...t.map][0];const z=JSON.parse(key);if(w!==t.den||direct.some((x,i)=>x[0]!==BigInt(z.firms[i].B+z.firms[i].ref)||x[1]!==1n))throw Error("terminal accounting");K.checked();}return direct;}
    const q=K.kernel(s,[a,b]);const w=[F(0n),F(0n)];let mass=0n;
    for(const [k,n] of q.map){mass+=n;const v=V(JSON.parse(k),h-1);for(let i=0;i<2;i++)w[i]=add(w[i],mul(F(n,q.den),v[i]))}
    if(mass!==q.den)throw Error("mass");
    return w;
   }));
   const eq=equilibria(A);
   if(!eq.length){stats.missing++;throw Error("no pure or verified 2x2 equilibrium at "+JSON.stringify({h,s,actions:[aa.length,bb.length]}))}
   const e=select(eq);memo.set(key,e.v);
   if(root)summaries.push({action_counts:[aa.length,bb.length],pure_count:eq.filter(e=>e.p.length===1&&e.q.length===1).length,selected:e.v.map(fmt),payoff_set:[...new Set(eq.map(x=>x.v.map(fmt).join(",")))],all_root_research_pairs:[...new Set(eq.map(x=>x.p.map(([i])=>aa[i].r.kind).join("+")+" / "+x.q.map(([j])=>bb[j].r.kind).join("+")))],selected_actions:[e.p.map(([i,p])=>({prob:fmt(p),...show(aa[i])})),e.q.map(([j,p])=>({prob:fmt(p),...show(bb[j])}))]});
   return e.v;
  }
  try{V(initial,horizon,true);return {horizon,cap,rule:rule===1?"max total private terminal wealth":"min total private terminal wealth",status:"solved",...stats,...summaries[0]}}catch(e){return {horizon,cap,rule:rule===1?"max total private terminal wealth":"min total private terminal wealth",status:"open",reason:String(e),...stats}}
 }
 const state=(B,n,market=0,psi=1,local=1)=>({sites:Array.from({length:n},()=>[[0,local,1],[0,local,1]]),firms:[{B,psi,lab:1,phys:1,ref:0},{B,psi,lab:1,phys:1,ref:0}],odds:["3","2"],market});
 const cases=[];
 for(const [name,s,h,caps] of [["two_target_low_cash",state(5,2),2,[1,2]],["two_target_high_demand",state(9,2,1),2,[1,2]],["three_target_low_cash",state(7,3),2,[2]],["one_target_three_period",state(4,1,0,1,0),3,[1,2]],["one_target_funded_three_period",state(6,1,0,1,1),3,[1,2]]]){
  const results=[];for(const cap of caps)for(const rule of [1,-1])results.push(solve(s,h,cap,rule));
  cases.push({name,initial:s,results});
 }
 return {synthetic:true,terminal:"cash plus one salvage tick per retained reference; no dividends; all other noncash stocks zero salvage",selection:"among all pure equilibria maximize/minimize sum then maximize firm 0 wealth; if none, first verified 2x2 support, not full mixed correspondence",cases};
}
if(typeof module!=="undefined")module.exports=run;
if(typeof require!=="undefined"&&require.main===module){if(process.argv.includes("--reference")){let checks=0;const r=run({...K,kernel:K.reference,checked:()=>checks++});console.log(JSON.stringify(r,null,2));console.error("terminal accounting checks: "+checks);}else console.log(JSON.stringify(run(K),null,2));}
