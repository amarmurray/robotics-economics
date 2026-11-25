// Numerical finite primal/dual LP checks, synthetic only.
function model(){
  const dot=(a,b)=>a.reduce((s,v,i)=>s+v*b[i],0), eps=1e-7;
  function comb(n,k){const out=[];function visit(a,start){if(a.length===k){out.push(a);return;}for(let i=start;i<=n-k+a.length;i++)visit([...a,i],i+1)}visit([],0);return out}
  function solve(A,b){let n=b.length,m=A.map((a,i)=>[...a,b[i]]);for(let i=0;i<n;i++){let p=i;for(let j=i+1;j<n;j++)if(Math.abs(m[j][i])>Math.abs(m[p][i]))p=j;if(Math.abs(m[p][i])<eps)return null;[m[p],m[i]]=[m[i],m[p]];let v=m[i][i];for(let k=i;k<=n;k++)m[i][k]/=v;for(let j=0;j<n;j++)if(j!==i){v=m[j][i];for(let k=i;k<=n;k++)m[j][k]-=v*m[i][k]}}return m.map(row=>row[n])}
  function vertices(A,b){let n=A[0].length;let C=A.concat(Array.from({length:n},(_,i)=>Array.from({length:n},(_,j)=>i===j?-1:0))),d=b.concat(Array(n).fill(0));return comb(C.length,n).map(I=>solve(I.map(i=>C[i]),I.map(i=>d[i]))).filter(x=>x&&C.every((row,i)=>dot(row,x)<=d[i]+eps))}
  function primal(A,b,w){return Math.max(...vertices(A,b).map(x=>dot(x,w)))}
  function dual(A,w){return vertices(w.map((_,j)=>A.map(row=>-row[j])),w.map(x=>-x))}
  const plus=(a,b,s=1)=>a.map((v,i)=>v+s*b[i]);let checks=0,cases=0;const assert=x=>{if(!x)throw Error("failed "+checks);checks++},eq=(a,b)=>Math.abs(a-b)<eps;
  let seed=73939;function rand(n){seed=(Math.imul(seed,1664525)+1013904223)>>>0;return (seed>>>16)%n}
  for(let k=0;k<400;k++){const A=Array.from({length:3},()=>[rand(4),rand(4)]).concat([[1,0],[0,1]]);const b=Array.from({length:5},()=>1+rand(4));const w=[1+rand(9),1+rand(9)];const ds=dual(A,w);const val=primal(A,b,w);const V=x=>Math.min(...ds.map(y=>dot(y,x)));assert(eq(val,V(b)));const face=ds.filter(y=>eq(dot(y,b),val));const d=[1,0,0,0,0],e=[0,1,0,0,0],u=plus(d,e);let slope=x=>Math.min(...face.map(y=>dot(y,x)));assert(slope(u)+eps>=slope(d)+slope(e));const h=1e-5;for(const v of [d,e,u,[1,1,1,0,0]]){let b2=plus(b,v),value=primal(A,b2,w),increment=value-val;assert(eq(value,V(b2)));assert(eq(increment,Math.min(...ds.map(y=>dot(y,b)-val+dot(y,v)))));let f2=ds.filter(y=>eq(dot(y,b2),value));assert(increment<=slope(v)+eps);assert(increment+eps>=Math.max(...f2.map(y=>dot(y,v))));assert(Math.abs((V(plus(b,v,h))-val)/h-slope(v))<1e-5)}cases++}
  const A0=[[1,1],[1,1],[1,1],[1,0],[0,1]],A1=[[1,1],[1,1],[1,0],[1,0],[0,1]],b=[1,1,1,1,1],w=[6,4],d=[1,0,0,0,0],e=[0,1,0,0,0];const result=A=>[b,plus(b,d),plus(b,e),plus(plus(b,d),e)].map(b=>primal(A,b,w));const P=result(A0),G=result(A1);assert(JSON.stringify(P)==="[6,6,6,6]");assert(JSON.stringify(G)==="[6,6,6,10]");assert(G[3]-G[0]-3-.5===.5);
  const sub=[[1,0],[0,1],[1,1]],B=[1,1,3],W=[1,1],subV=[B,[2,1,3],[1,2,3],[2,2,3]].map(b=>primal(sub,b,W));assert(JSON.stringify(subV)==="[2,3,3,3]");assert(subV[3]-subV[2]-subV[1]+subV[0]===-1);
  return {checks,cases,seed:73939,portfolio:{P,G,cost_per_body:1.5,grounding_cost:.5,net_combined_G:.5},finite_substitution:subV,field_calibration:false,full_repository_ci:false}
}
console.log(JSON.stringify(model(),null,2));
