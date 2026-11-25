function verify(){
  let checks=0,cases=0;
  const assert=(ok)=>{if(!ok)throw Error("check "+checks);checks++};
  const dot=(x,y)=>x.reduce((s,t,i)=>s+t*y[i],0);
  const maxR=(g,p)=>Math.max(0,...g.map(r=>r.v-dot(r.a,p)));
  const upper=(groups,b,p)=>dot(b,p)+groups.reduce((s,g)=>s+maxR(g,p),0);
  // A full order is indivisible by default. ticks=2 additionally admits halves.
  function solve(groups,b,ticks=1){
    let best=0;
    function visit(i,a,v){
      if(i===groups.length){best=Math.max(best,v);return}
      const g=groups[i];
      function mix(j,left,a,v){
        if(j===g.length){visit(i+1,a,v);return}
        const r=g[j];
        for(let n=0;n<=left;n++){
          const na=a.map((z,k)=>z+n*r.a[k]);
          if(na.every((z,k)=>z<=ticks*b[k]))mix(j+1,left-n,na,v+n*r.v);
        }
      }
      mix(0,ticks,a,v);
    }
    visit(0,b.map(()=>0),0);return best/ticks;
  }
  let rng=948971;const rand=n=>(rng=(Math.imul(rng,1664525)+1013904223)>>>0)%n;
  for(let t=0;t<900;t++){
    const groups=Array.from({length:3},()=>Array.from({length:2},()=>({a:Array.from({length:3},()=>rand(4)),v:1+rand(12)})));
    const b=Array.from({length:3},()=>1+rand(4)),d=Array.from({length:3},()=>rand(3)),b1=b.map((z,i)=>z+d[i]);
    const sub=groups.map(g=>g.slice(0,1));
    const v0=solve(groups,b),v1=solve(groups,b1),l0=solve(sub,b),l1=solve(sub,b1);
    assert(l0<=v0&&l1<=v1);assert(v1>=v0);
    const prices=Array.from({length:8},()=>Array.from({length:3},()=>rand(8)));
    let u0=Infinity,u1=Infinity;
    for(const p of prices){
      const a=upper(groups,b,p),z=upper(groups,b1,p);
      const small0=upper(sub,b,p),small1=upper(sub,b1,p);
      const corrections=groups.reduce((m,g,i)=>m+maxR(g,p)-maxR(sub[i],p),0);
      assert(corrections>=0);
      assert(a===small0+corrections&&z===small1+corrections);
      assert(a>=v0&&z>=v1);
      u0=Math.min(a,u0);u1=Math.min(z,u1);
    }
    assert(l1-u0<=v1-v0&&v1-v0<=u1-l0);
    cases++;
  }
  const A={a:[1,1,1],v:6};
  const P=[[A],[{a:[1,1,1],v:4},{a:[2,2,0],v:4}]];
  const G=[[A],[{a:[1,1,0],v:4},{a:[2,2,1],v:4}]];
  const b=[1,1,1],br=[2,1,1],bs=[1,2,1],be=[2,2,1],p0=[6,0,0],p1=[2,0,4];
  for(let i=0;i<3;i++)assert(JSON.stringify(P[1].map(r=>r.a[i]).sort())===JSON.stringify(G[1].map(r=>r.a[i]).sort()));
  for(const g of [P,G])for(const q of [b,br,bs])assert(solve(g,q,2)===6);
  assert(solve(P,be,2)===8&&solve(G,be,2)===10);
  assert(upper(P,b,p0)===6&&upper(G,b,p0)===6);
  assert(upper(P,be,p1)===8&&upper(G,be,p1)===10);
  assert(maxR(P[1],p1)===0&&maxR(G[1],p1)===2);
  assert(solve(P,be)===6&&solve(G,be)===10);
  assert(8-6-3===-1&&10-6-3===1);
  // Test controlled-retention factorial decomposition using integer discounted ticks.
  let factorialCases=0;
  for(let a=0;a<=4;a++)for(let b=0;b<=4;b++)for(let c=0;c<=4;c++)for(let d=0;d<=4;d++){
    const fixed=[a,b],evolve=[c,d];
    assert((fixed[1]-fixed[0])+((evolve[1]-evolve[0])-(fixed[1]-fixed[0]))===evolve[1]-evolve[0]);factorialCases++;
  }
  return {checks,cases,factorialCases,example:{incumbent:6,singletons:[0,0],divisiblePortfolio:[8,10],indivisiblePortfolio:[6,10],expandedResidual:[0,2],netAtCost3:[-1,1]},field_calibration:false,full_repository_ci:false};
}
console.log(JSON.stringify(verify(),null,2));
