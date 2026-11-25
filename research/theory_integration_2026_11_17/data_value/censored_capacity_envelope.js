function verify(){
  const n=3,T=4,w=[12,8,6],D=w.map((x,i)=>x-(w[i+1]||0));let checks=0,worlds=0,groups=0;
  const assert=(b,msg)=>{if(!b)throw Error(msg);checks++};
  const has=(a,i)=>(a>>i)&1, count=a=>Array.from({length:n},(_,i)=>has(a,i)).reduce((a,b)=>a+b,0);
  const top=(a,k)=>{let s=0;for(let i=0;i<n;i++)if(has(a,i)&&k>0){s|=1<<i;k--}return s};
  const val=a=>w.reduce((s,x,i)=>s+x*has(a,i),0);
  const pof=xs=>w.map((_,i)=>xs.reduce((s,a)=>s+has(a,i),0));
  const hidden=(s,k)=>{if(count(s)<k)return 0;let last=-1;for(let i=0;i<n;i++)if(has(s,i))last=i;return ((1<<n)-1)^((1<<(last+1))-1)};
  function envelope(log,p,k,l){
    const types=[...new Set(log)].map(s=>({s,q:log.filter(v=>v===s).length,e:hidden(s,k),x:Array(n).fill(0)}));
    const observed=pof(log),r=p.map((x,i)=>x-observed[i]);
    let lo=Infinity,hi=-Infinity;
    function evaluate(){
      let lower=0,upper=0;
      for(const t of types)for(let j=0;j<n;j++){
        const x=t.x.slice(0,j+1).sort((a,b)=>b-a);
        lower+=D[j]*x.slice(0,l).reduce((a,b)=>a+b,0);
        upper+=D[j]*Math.min(l*t.q,x.reduce((a,b)=>a+b,0));
      }
      lo=Math.min(lo,lower);hi=Math.max(hi,upper);
    }
    function assign(i,g,left){
      if(i===n){evaluate();return}
      if(g===types.length){if(left===0)assign(i+1,0,r[i+1]||0);return}
      const t=types[g],max=has(t.e,i)?Math.min(t.q,left):0;
      for(let x=0;x<=max;x++){t.x[i]=x;assign(i,g+1,left-x)}
    }
    if(r.some((v,i)=>v<0||v>types.reduce((s,t)=>s+t.q*has(t.e,i),0)))return null;
    assign(0,0,r[0]);return [lo,hi];
  }
  for(let k=1;k<n;k++)for(let l=1;l<=n-k;l++){
    const obs=new Map();
    for(let a=0;a<8;a++)for(let b=0;b<8;b++)for(let c=0;c<8;c++)for(let d=0;d<8;d++){
      const A=[a,b,c,d],log=A.map(x=>top(x,k)),p=pof(A);
      const inc=A.reduce((s,x,i)=>s+val(top(x,k+l))-val(log[i]),0);
      const gross=A.reduce((s,x)=>s+val(x),0),current=log.reduce((s,x)=>s+val(x),0);
      const overflow=A.reduce((s,x)=>s+val(x&~top(x,k)),0);
      assert(gross-current===overflow,"weighted overflow identity");
      const key=log.join(",")+";"+p.join(",");
      let z=obs.get(key);if(!z)obs.set(key,z={log,p,lo:Infinity,hi:-Infinity});
      z.lo=Math.min(z.lo,inc);z.hi=Math.max(z.hi,inc);worlds++;
    }
    for(const {log,p,lo,hi} of obs.values()){
      const predicted=envelope(log,p,k,l);
      assert(predicted[0]===lo&&predicted[1]===hi,"conditional envelope");
      groups++;
    }
  }
  const log=[1,1,1,1],p=[4,2,2],b=envelope(log,p,1,1).map(x=>x/T);
  assert(b[0]===4&&b[1]===7,"capacity example");
  assert(envelope(log,[3,2,2],1,1)===null,"invalid reported marginals");
  assert(envelope([0,0,0,0],[0,1,0],1,1)===null,"idle excludes latent readiness");
  return {checks,worlds,groups,example:{current:12,weightedQualificationPotential:19,weightedOverflow:7,extraSlotGross:b,extraSlotCost:5,extraSlotNet:b.map(x=>x-5),twoSlotsGross:envelope(log,p,1,2).map(x=>x/T)},fieldCalibration:false,fullRepositoryCI:false};
}
console.log(JSON.stringify(verify(),null,2));
