// CPU-only exact conditional transition benchmark. Run: node joint_transition.js > joint_transition_results.json
function makeKernel(){
 const cp=x=>JSON.parse(JSON.stringify(x)),key=x=>JSON.stringify(x);
 const gcd=(a,b)=>b?gcd(b,a%b):a;
 const odds=(a,b)=>{let d=gcd(a,b);if(!d)throw Error("zero posterior");return [String(a/d),String(b/d)]};
 const sortState=s=>({...cp(s),sites:cp(s.sites).sort((a,b)=>key(a)<key(b)?-1:key(a)>key(b)?1:0)});
 const opt={H:4,C:7,cap:2};
 // A site consists of [firm 0 [model, archive, right], firm 1 [...]].
 // An agent can use any previously qualified version, not just the latest.
 function recipes(s,i,last=false){
  const n=s.sites.length,out=[];
  function rec(j,m,r,h,c,copies){
   if(j===n){c+=copies*(copies-1)/2;if(h<=opt.H&&c<=opt.C)out.push({m,r,h,c,copies});return}
   const [v,d,right]=s.sites[j][i];
   const variants=[[-2,0,0,0],[-1,2,0,0],...Array.from({length:v+1},(_,v)=>[v,Math.max(0,1-v),3-v,1])];
   for(const [x,hh,cc,k] of variants)for(const retain of (!last&&x!==-2&&!d&&right?[0,1]:[0]))rec(j+1,[...m,x],[...r,retain],h+hh,c+cc,copies+k);
  }
  rec(0,[],[],0,0,0);return out;
 }
 function research(s,i,last=false,cap=2){
  const f=s.firms[i],rs=[{kind:"none",target:-1,method:0,h:0,c:0,fee:0,law:null}];
  if(last)return rs;
  function add(kind,target,method,h,c,fee,law){rs.push({kind,target,method,h,c,fee,law})}
  for(let j=0;j<s.sites.length;j++){
   const [v,d]=s.sites[j][i];
   if(v<1)for(const src of ["physical","local"]){
    if(src==="physical"?!f.phys:!d)continue;
    for(let k=0;k<=f.psi;k++){
     const good=10+5*k,law=[good,src==="physical"?5:good];
     if(f.lab)add("train_"+src,j,k,1,2,0,law);
     add("contract_train_"+src,j,k,1,0,5,law);
    }
   }
   if(!d)add("buy_local",j,0,1,0,6,null);
  }
  const dd=s.sites.some(x=>x[i][1]);
  if(f.psi<cap&&(f.phys||dd)){
   for(let k=0;k<=f.psi;k++){
    const p=5+5*k+5*+(f.phys&&dd);
    if(f.lab)add("develop",-1,k,1,3,0,[p,p]);
    add("contract_develop",-1,k,1,0,6,[p,p]);
   }
   add("license",-1,0,1,0,10,null);
  }
  if(s.odds.every(x=>BigInt(x)>0n)){
   let p=f.ref?20:15;
   if(f.lab)add("audit",-1,0,1,1,0,[p,20-p]);
   add("contract_audit",-1,0,1,0,3,[p,20-p]);
   add("exact_audit",-1,0,1,0,6,[20,0]);
  }
  if(!f.phys)add("buy_physical",-1,0,1,0,6,null);
  return rs;
 }
 function actions(s,i,last=false,cap=2){
  const f=s.firms[i],out=[];
  for(const p of recipes(s,i,last))for(const r of research(s,i,last,cap))
   for(const lab of last?[f.lab]:[f.lab,1-f.lab])
    for(const build of !last&&!f.ref?[0,1]:[0]){
     const h=p.h+r.h+build,c=p.c+r.c;
     const cost=2*h+c+r.fee+3*build+f.lab+(lab===f.lab?0:lab?4:1)+p.r.reduce((a,b)=>a+b,0);
     if(h<=opt.H&&c<=opt.C&&cost<=f.B)out.push({p,r,lab,build,h,c,cost});
    }
  if(f.lab)out.push({p:{m:s.sites.map(()=>-2),r:s.sites.map(()=>0),h:0,c:0,copies:0},r:research(s,i,true)[0],lab:0,build:0,h:0,c:0,cost:0,close:true});
  return out;
 }
 function deterministicBase(s,a){
  const n=cp(s),A=s.market?12:8;
  for(let i=0;i<2;i++){
   const x=a[i],f=n.firms[i];let rev=0;
   for(let j=0;j<n.sites.length;j++)if(x.p.m[j]!==-2)rev+=A-2*(1+ +(a[1-i].p.m[j]!==-2));
   if(x.cost>f.B)throw Error("prefunding");
   f.B+=rev-x.cost;f.lab=x.lab;f.ref+=x.build;
   if(x.r.kind==="buy_physical")f.phys=1;
   if(x.r.kind==="buy_local")n.sites[x.r.target][i][1]=1;
   if(x.r.kind==="license")f.psi++;
  }
  return n;
 }
 function events(s,a,last=false){
  const ev=[];
  for(let i=0;i<2;i++){
   const x=a[i],r=x.r;
   if(r.law)ev.push({i,j:r.target,kind:r.kind,p:r.law});
   for(let j=0;j<s.sites.length;j++)if(x.p.r[j]){
    const v=x.p.m[j],p=v===-1?3:15-5*v;
    ev.push({i,j,kind:"case",p:[p,p]});
   }
  }
  if(!last)ev.push({i:-1,j:-1,kind:"market_stays",p:[15,15]});
  return ev;
 }
 function apply(s,e,v){
  if(e.kind==="market_stays"){if(!v)s.market=1-s.market;return}
  if(!v)return;
  if(e.kind==="case")s.sites[e.j][e.i][1]=1;
  else if(e.kind.includes("train"))s.sites[e.j][e.i][0]++;
  else if(e.kind.includes("develop"))s.firms[e.i].psi++;
 }
 // Exact observed-history law. For a report vector, multiply conditional
 // likelihoods FIRST; only then mix by the single prior and update it.
 function kernel(s,a,last=false,canonical=true){
  const es=events(s,a,last),base=deterministicBase(s,a),prior=s.odds.map(BigInt);
  const den=(prior[0]+prior[1])*20n**BigInt(es.length),map=new Map();
  function walk(k,n,l1,l0){
   if(k===es.length){
    const u=prior[0]*l1,v=prior[1]*l0,w=u+v;if(!w)return;
    n.odds=odds(u,v);const st=canonical?sortState(n):n,k=key(st);
    map.set(k,(map.get(k)||0n)+w);return
   }
   for(const y of [0,1]){const e=es[k],t=cp(n);apply(t,e,y);
    walk(k+1,t,l1*BigInt(y?e.p[0]:20-e.p[0]),l0*BigInt(y?e.p[1]:20-e.p[1]));}
  }
  walk(0,base,1n,1n);return {den,map};
 }
 // Independently reconstruct by enumerating latent regime first, then
 // all labeled bitmask histories, maintaining separate regime mass per
 // observed history. Does not call events, apply or deterministicBase.
 function reference(s,a,last=false){
  const channels=[];
  for(let i=0;i<2;i++){
   if(a[i].r.law)channels.push({i,j:-1,p:a[i].r.law});
   a[i].p.r.forEach((r,j)=>{if(r)channels.push({i,j,p:[1,0].map(()=>a[i].p.m[j]===-1?3:15-5*a[i].p.m[j])})});
  }
  if(!last)channels.push({i:-1,j:-1,p:[15,15]});
  const prior=s.odds.map(BigInt),D=(prior[0]+prior[1])*20n**BigInt(channels.length);
  const obs=Array.from({length:2**channels.length},()=>[0n,0n]);
  for(let h=0;h<2;h++)for(let mask=0;mask<obs.length;mask++){
   let mass=prior[h];channels.forEach((c,k)=>mass*=BigInt(mask>>k&1?c.p[h]:20-c.p[h]));obs[mask][h]=mass;
  }
  const map=new Map();
  for(let mask=0;mask<obs.length;mask++){
   const [u,v]=obs[mask];if(!u&&!v)continue;
   const n=cp(s);n.odds=odds(u,v);
   for(let i=0;i<2;i++){
    const x=a[i],f=n.firms[i],r=x.r;
    f.B=s.firms[i].B-x.cost+x.p.m.reduce((sum,m,j)=>sum+(m===-2?0:(s.market?12:8)-2*(1+ +(a[1-i].p.m[j]!==-2))),0);
    f.ref=s.firms[i].ref+x.build;f.lab=x.lab;
    if(r.kind==="buy_physical")f.phys=1;
    if(r.kind==="buy_local")n.sites[r.target][i][1]=1;
    if(r.kind==="license")f.psi++;
   }
   channels.forEach((c,k)=>{
    let y=mask>>k&1;
    if(c.i===-1){n.market=y?s.market:1-s.market;return}
    if(!y)return;
    if(c.j>=0){n.sites[c.j][c.i][1]=1;return}
    const r=a[c.i].r;
    if(r.kind.endsWith("develop"))n.firms[c.i].psi++;
    if(r.kind.includes("train"))n.sites[r.target][c.i][0]++;
   });
   const k=key(sortState(n));map.set(k,(map.get(k)||0n)+u+v);
  }
  return {den:D,map};
 }
 function equal(x,y){
  if(x.map.size!==y.map.size)throw Error("support");
  for(const [k,v] of x.map)if(!y.map.has(k)||v*y.den!==y.map.get(k)*x.den)throw Error("mass");
 }
 function martingale(s,x){
  let total=0n,num=0n,den=1n;
  for(const [k,w] of x.map){total+=w;const [a,b]=JSON.parse(k).odds.map(BigInt),d=a+b;
   num=num*d+w*a*den;den*=d;const g=gcd(num,den);num/=g;den/=g;
  }
  if(total!==x.den)throw Error("normalization");
  const [a,b]=s.odds.map(BigInt);
  if(num*(a+b)!==den*x.den*a)throw Error("posterior martingale");
 }
 function permute(s,a,p){
  const t=cp(s),b=cp(a);t.sites=p.map(j=>s.sites[j]);
  for(let i=0;i<2;i++){
   b[i].p.m=p.map(j=>a[i].p.m[j]);b[i].p.r=p.map(j=>a[i].p.r[j]);
   if(b[i].r.target>=0)b[i].r.target=p.indexOf(b[i].r.target);
  }
  return [t,b];
 }
 function run(){
  const s={sites:[[[0,0,1],[0,0,1]],[[1,0,1],[0,1,1]],[[0,1,0],[1,0,1]]],firms:[{B:16,psi:1,lab:1,phys:1,ref:0},{B:16,psi:0,lab:1,phys:1,ref:0}],odds:["3","2"],market:0};
  const scenarios=[s,{...cp(s),odds:["1","0"]},{...cp(s),odds:["0","1"]},{...cp(s),firms:[{...s.firms[0],B:3,lab:0},{...s.firms[1],B:5,lab:0}],market:1}];
  let checks=0,perm=0,terminal=0,maxSupport=0;const cases=[];
  for(const st of scenarios){
   const aa=actions(st,0),bb=actions(st,1);
   // Stratify by research kind so rare contracts and scope actions are exercised.
   function sample(xs){let m=new Map();for(const a of xs){const k=a.r.kind+":"+a.r.method+":"+a.build+":"+a.lab+":"+ +(a.p.r.some(Boolean));if(!m.has(k))m.set(k,a)}return [...m.values()]}
   const x=sample(aa),y=sample(bb);
   for(let i=0;i<x.length;i++){
    // Deterministic spread over rival options; include concurrent research and retention.
    for(const j of [...new Set([i%y.length,(i*13+7)%y.length,(i*31+3)%y.length])]){
     const a=[x[i],y[j]],k=kernel(st,a);equal(k,reference(st,a));martingale(st,k);checks++;
     maxSupport=Math.max(maxSupport,k.map.size);
     for(const p of [[2,0,1],[1,2,0],[1,0,2]]){const [t,b]=permute(st,a,p);equal(k,kernel(t,b));perm++}
    }
   }
   const z0=actions(st,0,true),z1=actions(st,1,true);
   for(const a of z0)for(const b of z1){const k=kernel(st,[a,b],true);equal(k,reference(st,[a,b],true));martingale(st,k);terminal++}
   cases.push({odds:st.odds,cash:st.firms.map(f=>f.B),action_counts:[aa.length,bb.length],sample_counts:[x.length,y.length]});
  }
  // Two concurrent cross-domain reports: method 1 and 0, respectively.
  // Success laws [3/4,1/4] and [1/2,1/4]. Both success = 1/4;
  // posterior odds = 9:1, rather than combining separate marginal probabilities.
  const a=actions(s,0).find(a=>a.r.kind==="train_physical"&&a.r.method===1&&a.r.target===0&&a.p.m.every(x=>x===-2)&&!a.build&&a.lab===1);
  const b=actions(s,1).find(a=>a.r.kind==="train_physical"&&a.r.method===0&&a.r.target===0&&a.p.m.every(x=>x===-2)&&!a.build&&a.lab===1);
  const k=kernel(s,[a,b]);let mass=0n;
  for(const [st,w] of k.map)if(JSON.parse(st).odds.join(":")==="9:1")mass+=w;
  if(4n*mass!==k.den)throw Error("joint success witness");
  // Retained records appear only next period; no same-period local training
  // from a target whose inherited archive is absent.
  if(actions(s,0).some(a=>a.r.kind.endsWith("train_local")&&a.r.target===0))throw Error("lookahead");
  // A successor can be developed only from inherited method; old method remains.
  if(!actions(s,0).some(a=>a.r.kind==="develop"&&a.r.method===0)||!actions(s,0).some(a=>a.r.kind==="develop"&&a.r.method===1))throw Error("old method");
  return {synthetic:true,restriction:"digital binary recipient sites, fixed physical archive endowment, reference construction and lab scope; common public transfer regime",cases,checks:{joint_profiles_independent_latent_first:checks,permuted_profiles:perm,terminal_profiles:terminal,max_next_state_support:maxSupport},joint_report_witness:{probability_both_success:"1/4",posterior_odds:"9:1",note:"method 1 and method 0, weak law 1/4 for both"},status:"Exact kernel and action generator tested; longer game equilibrium not yet solved."};
 }
 return {actions,kernel,reference,sortState,run};
}
if(typeof module!=='undefined')module.exports=makeKernel;
if(typeof require!=='undefined'&&require.main===module)console.log(JSON.stringify(makeKernel().run(),null,2));
