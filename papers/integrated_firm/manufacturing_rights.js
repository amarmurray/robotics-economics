// Exact CPU-only extension of cohort_rights.js at e0208e9f. Run node manufacturing_rights.js.
function rightsStudy({budget=3000000,projection=true,quotient=true,only=null,rules=[1,-1]}={}){
 const H=3,C=5,A=[18,14,14],parts=[1,2],pop=m=>+(!!(m&1))+(!!(m&2))+(!!(m&4)),swap=m=>(m&1)|((m&2)<<1)|((m&4)>>1),L=h=>h?12+42*(h-1):0;
 const cases=["mobile","armkit","kit","empty"].flatMap(kind=>[0,1].map(R=>({name:kind+"_"+R,T:3,B:120,K:kind==="mobile"?[0,1,0,0]:kind==="armkit"?[1,0,0,1]:kind==="kit"?[0,0,0,1]:[0,0,0,0],M:[2,2],D:[0,0],R,g:1,p:2,cap:2,outside:18,buy:10})));
 function solve(c,rule){
 let memo=new Map(),menus=new Map(),profiles=0,dev=0;
 const S=c.M.map((m,i)=>[...c.K,m,c.p,c.B,c.D[i],c.g]),sal=s=>s[0]+2*s[1];
 function canon(s,z,h){
  let a=s.slice(),b=z.slice(),flip=false;
  // Active scope has a current operating bill, hence NOT projected out.
  if(projection&&h===1)for(const x of [a,b]){x[2]=x[3]=x[5]=x[7]=0}
  if(quotient){
   for(const x of [a,b])x[6]=Math.min(x[6],L(h));
   let k=[a[4],a[7],b[4],b[7]].join(),l=[swap(a[4]),swap(a[7]),swap(b[4]),swap(b[7])].join();
   if(swap(c.R)===c.R&&l<k){for(const x of [a,b]){x[4]=swap(x[4]);x[7]=swap(x[7])}flip=true}
  }return [a,b,flip];
 }
 function menu(s,h){
  let id=[h,...s].join();if(menus.has(id))return menus.get(id);
  let [ka,kb,ia,ib,m,p,B,D,g]=s,rs=[["none",0,0,0,0,-1]],bs=[["none",0,0,0,-1,0]];
  if(h>1){
   for(let old=0;old<=p;old++){
    for(let j=0;j<3;j++)if(!(m&(1<<j))){
     if(g&&(D&(1<<j)))rs.push(["train",1,2,0,2+old,j]);
     rs.push(["contract",1,0,c.outside??5,2+old,j]);
    }
    if(p<c.cap&&!(projection&&quotient&&h===2&&B>=L(h))){
     if(g)rs.push(["develop",1,3,0,2+old,3]);
     rs.push(["contract_develop",1,0,6,2+old,3]);
    }
   }
   if(p<c.cap&&!(projection&&quotient&&h===2&&B>=L(h)))rs.push(["license",1,0,10,4,3]);
   if(h>=3)for(let j=0;j<3;j++)if(!(D&(1<<j))&&!(m&(1<<j)))rs.push(["buy_archive",1,0,c.buy??2,4,j]);
   if(!c.fixedHardware)for(let j=0;j<2;j++)if(!s[j]){if(s[j+2])bs.push(["assemble",1,1,0,j,1]);else if(h>2)bs.push(["order",0,0,parts[j],j,0])}
  }
  let out=new Map();
  for(let pr=0;pr<4;pr++){
   if(pr===2&&!ka||pr===3&&!kb)continue;
   for(let d1=0;d1<3;d1++)for(let d2=0;d2<3;d2++){
    let q=(pr?1:0)|(d1?2:0)|(d2?4:0),auto=(pr>=2?1:0)|(d1===2?2:0)|(d2===2?4:0),copies=pop(auto);
    for(let use=0;use<8;use++){
     if(use&~(m&auto))continue;
     let human=[0,3,2- +(!!(use&1)),1- +(!!(use&1))][pr]+(d1===1?2:d1===2?1- +(!!(use&2)):0)+(d2===1?2:d2===2?1- +(!!(use&4)):0);
     let compute=copies+copies*(copies-1)/2+2*copies-pop(use);
     let ret=[0];if(h>=3)for(let j=0;j<3;j++)if((q&c.R&~D&~m)&(1<<j))ret.push(1<<j);
     // Funded own final menus share the same feasibility; closure saves its additive operating bill.
     let scopes=h===1?[g]:projection&&quotient&&h===2&&B>=L(h)?[0]:[0,1];
     for(const r of rs)for(const b of bs)for(const keep of ret)for(const ng of scopes){
      if(r[0]==="buy_archive"&&(keep&(1<<r[5])))continue;
      let hh=human+r[1]+b[1],cc=compute+r[2]+b[2]+pop(keep),cost=2*hh+cc+r[3]+b[3]+g+2* +(!g&&ng);
      if(hh>H||cc>C||cost>B)continue;
      if(cost>(h===1?12:42))throw Error("outlay bound");
      let a={q,modes:[pr,d1,d2],use,copies,hh,cc,cost,r,b,keep,ng};
      let key=[q,r[0]==="buy_archive"?"buy":r[4],r[5],b[4],b[5],keep,ng,(h===1||quotient&&B>=L(h))?0:cost].join();
      if(!out.has(key)||out.get(key).cost>cost)out.set(key,a);
     }
    }
   }
  }
  if(B===0&&g)out.set("suspend",{q:0,modes:[0,0,0],use:0,copies:0,hh:0,cc:0,cost:0,r:rs[0],b:bs[0],keep:0,ng:0});
  let v=[...out.values()];if(!v.length)throw Error("empty menu");menus.set(id,v);return v;
 }
 function rev(a,b){let R=0;for(let j=0;j<3;j++)if(a.q&(1<<j))R+=A[j]-2-2* +(!!(b.q&(1<<j)));return R}
 function next(s,a,R){
  let z=s.slice();z[6]+=R-a.cost;z[7]|=a.keep;z[8]=a.ng;
  let j=a.b[4];if(j>=0){if(a.b[5]){z[j]=1;z[j+2]=0}else z[j+2]=1}
  let w=z.slice(),k=a.r[5];if(a.r[0]==="buy_archive")w[7]|=1<<k;else if(k===3)w[5]++;else if(k>=0)w[4]|=1<<k;
  return a.r[4]===0?[[z,4]]:a.r[4]===4?[[w,4]]:[[z,4-a.r[4]],[w,a.r[4]]];
 }
 function V(s,z,h){
  [s,z]=canon(s,z,h);let id=[h,...s,...z].join();if(memo.has(id))return memo.get(id);
  let aa=menu(s,h),bb=menu(z,h),br0=bb.map(()=>-Infinity),br1=aa.map(()=>-Infinity),mat=[],scale=16**h,ta=new Map(),tb=new Map();
  for(let i=0;i<aa.length;i++){let a=aa[i],row=[];for(let j=0;j<bb.length;j++){
   if(++profiles>budget)throw Error("profile budget");
   let b=bb[j],R=rev(a,b),Z=rev(b,a),v=[scale*(R-a.cost),scale*(Z-b.cost)];
   if(h===1){v[0]+=scale*sal(s);v[1]+=scale*sal(z)}
   else{
    let k=i+","+b.q,l=j+","+a.q;if(!ta.has(k))ta.set(k,next(s,a,R));if(!tb.has(l))tb.set(l,next(z,b,Z));
    for(let [x,w] of ta.get(k))for(let [y,u] of tb.get(l)){let t=V(x,y,h-1).v;v[0]+=w*u*t[0];v[1]+=w*u*t[1]}
   }
   if(!v.every(Number.isSafeInteger))throw Error("integer precision");
   br0[j]=Math.max(br0[j],v[0]);br1[i]=Math.max(br1[i],v[1]);row.push(v);
  }mat.push(row)}
  let e=null,n=0;for(let i=0;i<aa.length;i++)for(let j=0;j<bb.length;j++){let v=mat[i][j];if(v[0]!==br0[j]||v[1]!==br1[i])continue;n++;
   if(!e||rule*(v[0]+v[1]-e.v[0]-e.v[1])>0||v[0]+v[1]===e.v[0]+e.v[1]&&v[0]>e.v[0])e={v,i,j}}
  if(!e){
   if(h!==c.T||c.name!=="armkit_1"||rule!==1||!projection||!quotient)throw Error("no pure equilibrium "+id);
   // Candidate support found by fictitious play; validity is determined only by exact full-menu inequalities.
   const r=[132,135],k=[132,135],d0=mat[r[0]][k[0]][0]-mat[r[1]][k[0]][0],d1=mat[r[0]][k[1]][0]-mat[r[1]][k[1]][0],f0=mat[r[0]][k[0]][1]-mat[r[0]][k[1]][1],f1=mat[r[1]][k[0]][1]-mat[r[1]][k[1]][1];
   const gcd=(x,y)=>y?gcd(y,x%y):Math.abs(x);function fraction(n,d){if(d<0){n=-n;d=-d}let g=gcd(n,d);if(!(n>0&&n<d))throw Error("invalid mixed support");return [n/g,d/g]}
   const q=fraction(-d1,d0-d1),p=fraction(-f1,f0-f1),val0=i=>q[0]*mat[i][k[0]][0]+(q[1]-q[0])*mat[i][k[1]][0],val1=j=>p[0]*mat[r[0]][j][1]+(p[1]-p[0])*mat[r[1]][j][1];
   const best0=Math.max(...aa.map((_,i)=>val0(i))),best1=Math.max(...bb.map((_,j)=>val1(j)));
   if(!r.every(i=>val0(i)===best0)||!k.every(j=>val1(j)===best1))throw Error("mixed deviation");
   dev+=aa.length+bb.length;
   const den=p[1]*q[1],mix=r.flatMap((i,x)=>k.map((j,y)=>({a:aa[i],b:bb[j],w:(x?p[1]-p[0]:p[0])*(y?q[1]-q[0]:q[0])})));
   const num=[best0*p[1],best1*q[1]];
   const cert={p,q,scale,den,num,matrix:r.map(i=>k.map(j=>mat[i][j])),menuSizes:[aa.length,bb.length],best0,best1,pureProfiles:0};
   const result={v:num.map(x=>x/den),num,mix,cert,n:0};memo.set(id,result);return result;
  }
  for(let i=0;i<aa.length;i++){if(mat[i][e.j][0]>e.v[0])throw Error("dev0");dev++}
  for(let j=0;j<bb.length;j++){if(mat[e.i][j][1]>e.v[1])throw Error("dev1");dev++}
  let result={v:e.v,a:aa[e.i],b:bb[e.j],n};memo.set(id,result);return result;
 }
 try{
  let root=V(...S,c.T),mixDen=root.cert?.den??1,dist=new Map([[S.flat().join(),1]]),dated=[];
  for(let t=0;t<c.T;t++){
   let h=c.T-t,nd=new Map(),row={date:t+1,jobs:0,customer_surplus:0,retain:0,internal:0,contract:0,buy:0,successor:0,lab:0,entry:0,exit:0,assembly:0,orders:0,net0:0,net1:0};
   for(let [k,baseWeight] of dist){
    let a=k.split(",").map(Number),ss=[a.slice(0,9),a.slice(9)],cs=canon(...ss,h),e=memo.get([h,...cs.slice(0,2).flat()].join());
    for(const profile of e.mix??[{a:e.a,b:e.b,w:1}]){let w=baseWeight*profile.w;
    let actions=[profile.a,profile.b].map(a=>{if(!cs[2])return a;let r=a.r.slice();if(r[5]===1||r[5]===2)r[5]=3-r[5];return {...a,q:swap(a.q),use:swap(a.use),keep:swap(a.keep),modes:[a.modes[0],a.modes[2],a.modes[1]],r}});
    let wt=w/(mixDen*16**t),R=actions.map((a,i)=>rev(a,actions[1-i]));
    for(let i=0;i<2;i++){
     let a=actions[i],s=ss[i],[pr,d1,d2]=a.modes,auto=(pr>=2?1:0)|(d1===2?2:0)|(d2===2?4:0),n=pop(auto);
     let hh=[0,3,2- +(!!(a.use&1)),1- +(!!(a.use&1))][pr]+[0,2,1- +(!!(a.use&2))][d1]+[0,2,1- +(!!(a.use&4))][d2]+a.r[1]+a.b[1];
     let cc=n*(n+1)/2+2*n-pop(a.use)+a.r[2]+a.b[2]+pop(a.keep);
     let cost=s[6]===0&&s[8]?0:2*hh+cc+a.r[3]+a.b[3]+s[8]+2* +(!s[8]&&a.ng);
     if(cost!==a.cost||hh!==a.hh||cc!==a.cc||hh>H||cc>C||cost>s[6]||a.keep&~(a.q&c.R&~s[7]&~s[4])||a.use&~(s[4]&auto)||pr>=2&&!s[pr-2])throw Error("ledger infeasible");
     if(a.r[0]==="train"&&(!s[8]||!(s[7]&(1<<a.r[5]))))throw Error("archive timing");
     if(a.r[0]==="develop"&&!s[8])throw Error("scope");
     row.jobs+=wt*pop(a.q);row.retain+=wt*pop(a.keep);row.internal+=wt* +(a.r[0]==="train");row.contract+=wt* +(a.r[0]==="contract");row.buy+=wt* +(a.r[0]==="buy_archive");row.successor+=wt* +(a.r[5]===3);row.lab+=wt*s[8];row.entry+=wt* +(!s[8]&&a.ng);row.exit+=wt* +(s[8]&&!a.ng);row.assembly+=wt* +(a.b[0]==="assemble");row.orders+=wt* +(a.b[0]==="order");row["net"+i]+=wt*(R[i]-cost);
    }
    for(let j=0;j<3;j++){let Q=+(!!(actions[0].q&(1<<j)))+ +(!!(actions[1].q&(1<<j)));row.customer_surplus+=wt*Q*Q}
    for(let u=0;u<4;u++)for(let v=0;v<4;v++){
     let y=ss.map((s,i)=>{let a=actions[i],z=s.slice(),j=a.b[4];z[6]+=R[i]-a.cost;z[7]|=a.keep;z[8]=a.ng;
      if(j>=0){if(a.b[5]){if(!s[j+2]||s[j])throw Error("kit ledger");z[j]=1;z[j+2]=0}else{if(s[j+2]||s[j])throw Error("order ledger");z[j+2]=1}}
      if((i?v:u)<a.r[4]){let j=a.r[5];if(a.r[0]==="buy_archive")z[7]|=1<<j;else if(j===3)z[5]++;else z[4]|=1<<j}return z}).flat().join();
     nd.set(y,(nd.get(y)||0)+w);
    }
   }}if([...nd.values()].reduce((a,b)=>a+b,0)!==mixDen*16**(t+1))throw Error("mass");dist=nd;dated.push(row);
  }
  let den=mixDen*16**c.T,wealth=[0,0],cash=[0,0];for(let [k,w] of dist){let x=k.split(",").map(Number);for(let i=0;i<2;i++){let s=x.slice(9*i,9*i+9);wealth[i]+=w*(s[6]+sal(s));cash[i]+=w*s[6]}}
  for(let i=0;i<2;i++)if(wealth[i]!==(root.num??root.v)[i]+c.B*den||Math.abs(cash[i]/den-c.B-dated.reduce((x,r)=>x+r["net"+i],0))>1e-9)throw Error("cash replay");
  return {name:c.name,status:"solved",rule,wealth:wealth.map(x=>x/den),root:root.mix??[root.a,root.b],mixed_certificate:root.cert??null,wealth_numerator:wealth,wealth_denominator:den,dated,profiles,states:memo.size,deviations:dev};
 }catch(e){if(!String(e).includes("profile budget")&&!String(e).includes("no pure equilibrium"))throw e;return {name:c.name,status:"open",rule,reason:String(e),profiles,states:memo.size}}
 }
 return {synthetic:true,projection,quotient,budget,cases:cases.filter(c=>!only||only.includes(c.name)),results:cases.filter(c=>!only||only.includes(c.name)).flatMap(c=>rules.map(r=>solve(c,r)))};
}
function reproduce(){return rightsStudy({budget:6000000});}
if(typeof module!=='undefined'&&module.exports){module.exports={rightsStudy,reproduce};if(require.main===module)console.log(JSON.stringify(reproduce(),null,2));}
