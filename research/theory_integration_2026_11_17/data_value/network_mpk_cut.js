// Exact finite directed-flow checks. All inputs synthetic.
function run(){
 let checks=0, networks=0, comparisons=0, dynamicCases=0;
 const assert=(x)=>{if(!x)throw Error("check "+checks);checks++};
 function cuts(n,edges,c){
   const out=[];
   for(let mask=0;mask<1<<(n-2);mask++){
     const inS=i=>i===0 || (i!==n-1 && ((mask>>(i-1))&1)===1);
     const ids=edges.map(([u,v],i)=>inS(u)&&!inS(v)?i:-1).filter(i=>i>=0);
     out.push({ids,cap:ids.reduce((s,i)=>s+c[i],0)});
   }return out;
 }
 function maxflow(n,edges,c){
   const r=Array.from({length:n},()=>Array(n).fill(0));
   edges.forEach(([u,v],i)=>r[u][v]+=c[i]);
   let value=0;
   while(true){
     const par=Array(n).fill(-1),q=[0];par[0]=0;
     for(let l=0;l<q.length&&par[n-1]===-1;l++){
       const u=q[l];
       for(let v=0;v<n;v++)if(par[v]===-1&&r[u][v]>0){par[v]=u;q.push(v)}
     }
     if(par[n-1]===-1)return value;
     let b=Infinity;
     for(let v=n-1;v!==0;v=par[v])b=Math.min(b,r[par[v]][v]);
     for(let v=n-1;v!==0;v=par[v]){r[par[v]][v]-=b;r[v][par[v]]+=b}
     value+=b;
   }
 }
 const min=a=>Math.min(...a);
 const templates=[
   {n:4,e:[[0,1],[0,2],[1,2],[1,3],[2,3]]},
   {n:5,e:[[0,1],[1,2],[1,3],[2,4],[3,4],[2,3]]}
 ];
 for(const {n,e} of templates){
   for(let z=0;z<4**e.length;z++){
     const c=e.map((_,i)=>Math.floor(z/4**i)%4),cs=cuts(n,e,c),f=maxflow(n,e,c);
     networks++;assert(f===min(cs.map(x=>x.cap)));
     for(let j=0;j<e.length;j++){
       const a=min(cs.filter(x=>x.ids.includes(j)).map(x=>x.cap)),b=min(cs.filter(x=>!x.ids.includes(j)).map(x=>x.cap));
       for(let d=1;d<=2;d++){
         const c1=c.map((v,i)=>v+(i===j?d:0)),f1=maxflow(n,e,c1);
         const pred=Math.min(a+d,b)-Math.min(a,b);
         assert(f1-f===pred);
         if(Number.isFinite(a))assert(pred===Math.min(d,Math.max(0,b-a)));
         if(d===1)assert(pred===Number(cs.filter(x=>x.cap===f).every(x=>x.ids.includes(j))));
         comparisons++;
       }
     }
     const delta=c.map((v,i)=>i%3===0?1:i%3===1?-Math.min(1,v):0);
     const f2=maxflow(n,e,c.map((v,i)=>v+delta[i]));
     assert(f2-f===min(cs.map(x=>x.cap-f+x.ids.reduce((s,i)=>s+delta[i],0))));
     const ub0=cs[0].cap,ub2=cuts(n,e,c.map((v,i)=>v+delta[i]))[0].cap;
     assert(f2-ub0<=f2-f&&f2-f<=ub2-f);
   }
 }
 for(let k=0;k<4;k++)for(let down=0;down<4;down++)for(let b=0;b<4;b++)
 for(let rate=0;rate<3;rate++)for(let m=0;m<3;m++)for(let betaNum=0;betaNum<3;betaNum++){
   const q0=Math.min(k,down),q1=Math.min(k+1,down);
   const future=(K,q)=>Math.min(K,b+rate*q);
   const V=(K)=>Math.max(...Array.from({length:Math.min(K,down)+1},(_,q)=>2*m*q+betaNum*future(K,q)));
   assert(V(k)===2*m*q0+betaNum*future(k,q0));
   assert(V(k+1)-V(k)===2*m*(q1-q0)+betaNum*(future(k+1,q0)-future(k,q0))+betaNum*(future(k+1,q1)-future(k+1,q0)));
   dynamicCases++;
 }
 const serial=(a,b)=>Math.min(a,b),parallel=(a,b,d)=>Math.min(a+b,d);
 const examples={remoteComplement:{baseline:[serial(1,1),serial(1,2)],marginal:[serial(2,1)-serial(1,1),serial(2,2)-serial(1,2)]},remoteSubstitute:{baseline:[parallel(1,0,2),parallel(1,1,2)],marginal:[parallel(2,0,2)-parallel(1,0,2),parallel(2,1,2)-parallel(1,1,2)]},dynamic:{P:1,G:2,incumbentSnapshotFutureMPK:0,netAtCost1point5:[-.5,.5]}};
 assert(examples.remoteComplement.marginal.join()==="0,1");
 assert(examples.remoteSubstitute.marginal.join()==="1,0");
 const p=k=>k+Math.min(k,1),g=k=>k+Math.min(k,k);
 assert(p(2)-p(1)===1&&g(2)-g(1)===2);
 return {checks,networks,comparisons,dynamicCases,examples,fieldCalibration:false,fullRepositoryCI:false};
}
console.log(JSON.stringify(run(),null,2));
