function check(){
 const n=3,T=3,weights=[12,8,6],diff=[4,2,6],pop=m=>[0,1,2].filter(i=>m>>i&1).length;
 const val=(m,k)=>weights.filter((_,i)=>m>>i&1).slice(0,k).reduce((a,b)=>a+b,0);
 let cases=0,assertions=0;
 function verify(x){if(!x)throw Error("failed "+assertions);assertions++}
 for(const k of [1,2])for(let a=0;a<8;a++)for(let b=0;b<8;b++)for(let c=0;c<8;c++){
  const log=[a,b,c];if(log.some(s=>pop(s)>k))continue;
  const groups=new Map(),marg=new Map();
  for(let x=0;x<8;x++)for(let y=0;y<8;y++)for(let z=0;z<8;z++){
   const r=[x,y,z];if(r.some((v,t)=>(v&log[t])!==log[t]))continue;
   const rows=[...new Set(log)].sort((a,b)=>a-b).map(s=>({s,q:log.filter(t=>t===s).length,p:[0,1,2].map(i=>r.filter((v,t)=>log[t]===s&&!(s>>i&1)&&(v>>i&1)).length)}));
   const key=rows.map(o=>o.p.join(",")).join(";"),m=[0,1,2].map(i=>r.filter(v=>v>>i&1).length).join(",");
   const value=r.reduce((u,v,t)=>u+val(v,k)-val(log[t],n),0);
   let lo=0,hi=0;
   for(const {s,q,p} of rows)for(let j=0;j<n;j++){let h=k-pop(s&((1<<(j+1))-1)),pfx=p.slice(0,j+1);lo+=diff[j]*[...pfx].sort((a,b)=>b-a).slice(0,h).reduce((a,b)=>a+b,0);hi+=diff[j]*Math.min(h*q,pfx.reduce((a,b)=>a+b,0))}
   verify(value>=lo&&value<=hi);cases++;
   const g=groups.get(key)||[Infinity,-Infinity,lo,hi,m];g[0]=Math.min(g[0],value);g[1]=Math.max(g[1],value);groups.set(key,g);
   const f=marg.get(m)||[Infinity,-Infinity,Infinity,-Infinity];f[0]=Math.min(f[0],value);f[1]=Math.max(f[1],value);f[2]=Math.min(f[2],lo);f[3]=Math.max(f[3],hi);marg.set(m,f)
  }
  for(const [l,u,lo,hi] of groups.values())verify(l===lo&&u===hi);
  for(const [l,u,lo,hi] of marg.values())verify(l===lo&&u===hi);
 }
 const s=2,r=3,k=1;
 verify(val(r,k)-val(s,n)===4);
 return {cases,assertions,illustration:{accepted:8,oracle:12,regret:4},field_calibration:false,full_repository_ci:false};
}
console.log(JSON.stringify(check(),null,2));
