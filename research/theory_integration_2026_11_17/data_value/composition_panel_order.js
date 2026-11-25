// Reproducible arithmetic and finite-order checker; no field causal inference.
function run(){
 let checks=0; const assert=(x)=>{if(!x)throw Error("check "+checks);checks++};
 const raw=[[1.01,.43,22.7,.81,24.9,1.94,40.9,.60,2.46,3.42,.80],[1.22,1.56,27.5,1.95,25.1,2.35,26.8,1.46,5.94,4.13,1.90],[2.37,.20,19.9,.39,12.1,1.14,42.5,.63,3.04,16.3,1.51]];
 const sums=raw.map(r=>r.reduce((s,v)=>s+v,0)), z=raw.map((r,i)=>r.map(v=>v/sums[i]));
 const d=z.slice(1).map(r=>r.map((v,i)=>v-z[0][i]));
 const minor=d[0][6]*d[1][9]-d[0][9]*d[1][6];
 assert(d.every(r=>Math.abs(r.reduce((s,v)=>s+v,0))<1e-12));assert(minor<-.018);
 const perms=(a)=>a.length===0?[[]]:a.flatMap((v,i)=>perms(a.filter((_,j)=>i!==j)).map(p=>[v,...p]));
 const orders=perms([0,1,2]);
 function edges(y,sign){return y.flatMap((row,j)=>row.flatMap((a,i)=>row.flatMap((b,k)=>sign[j]*(b-a)>0?[[i,k]]:[])))}
 function acyclic(e){let left=[0,1,2];while(left.length){let a=left.find(i=>!e.some(([u,v])=>v===i&&left.includes(u)));if(a===undefined)return false;left=left.filter(i=>i!==a)}return true}
 function fits(y,sign,p){return y.every((r,j)=>p.slice(1).every((v,i)=>sign[j]*(r[v]-r[p[i]])>=0))}
 let cases=0;for(let a=0;a<27;a++)for(let b=0;b<27;b++)for(let s of [1,-1]){const row=n=>[n%3,Math.floor(n/3)%3,Math.floor(n/9)];const y=[row(a),row(b)],sign=[1,s];assert(acyclic(edges(y,sign))===orders.some(p=>fits(y,sign,p)));cases++}
 const nmp=[[46,59.9,65.9],[-3.9,-42.7,-31.4]];
 assert([1,-1].every(s=>!acyclic(edges(nmp,[1,s]))));
 // Scalar smooth finite-data interpolation, not a fitted scientific model.
 function lagrange(t,x,y){return x.reduce((v,xi,i)=>v+y[i]*x.reduce((p,xj,j)=>i===j?p:p*(t-xj)/(xi-xj),1),0)}
 const projection=[0,1,2];for(let r of nmp)for(let i=0;i<3;i++)assert(Math.abs(lagrange(projection[i],projection,r)-r[i])<1e-9);
 return {checks,cases,remix:{rawPercent:raw,rowSums:sums,rt1TotoDirectionCoordinates:d.map(r=>[r[6],r[9]]),minor},nmpPointEstimates:nmp,fieldCalibration:false,fullRepositoryCI:false};
}
if(typeof module!=="undefined") module.exports={run};
if(typeof require!=="undefined"&&require.main===module) console.log(JSON.stringify(run(),null,2));
