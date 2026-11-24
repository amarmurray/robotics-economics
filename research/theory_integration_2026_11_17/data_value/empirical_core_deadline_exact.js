function run(){
  let checks=0,laws=0;
  const assert=(c)=>{if(!c)throw Error("assertion "+checks);checks++};
  // Integer test of the moment inequalities: weights sum to n, total time S,
  // p is a count of timely observations; support integer 0..B.
  for(let B=3;B<=8;B++)for(let n=2;n<=6;n+=2){
    const w=Array(B+1).fill(0);
    function visit(i,left){
      if(i===B){w[i]=left; const S=w.reduce((a,x,j)=>a+x*j,0);
        for(let m=0;m<B;m++){
          if(w.slice(0,m+1).reduce((a,x)=>a+x,0)<n/2||w.slice(m).reduce((a,x)=>a+x,0)<n/2)continue;
          for(let t=m+1;t<B;t++){
            const k=w.slice(0,t+1).reduce((a,x)=>a+x,0);laws++;
            assert(2*k>=n);
            assert(2*S>= (2*k-n)*m+2*(n-k)*t);
            assert(2*S<= n*m+(2*k-n)*t+2*(n-k)*B);
          }
        }return;}
      for(let k=0;k<=left;k++){w[i]=k;visit(i+1,left-k);}
    }
    visit(0,n);
  }
  function bounds(mu,m,t,B){
    return [Math.max(.5,(t-m/2-mu)/(t-m)),Math.min(1,(B+(m-t)/2-mu)/(B-t))];
  }
  function stat(a){
    const p=a.reduce((s,[w,x])=>s+w,0);const mean=a.reduce((s,[w,x])=>s+w*x,0)/p;
    const med=a.find(([w,x],i)=>a.slice(0,i+1).reduce((s,[z])=>s+z,0)>=p/2)[1];
    const variance=a.reduce((s,[w,x])=>s+w*(x-mean)**2,0)/p;
    return {mean,med,variance,onTime:a.filter(([w,x])=>x<=120).reduce((s,[w])=>s+w,0)/p}
  }
  const world1={P:stat([[51,112],[49,(12264-51*112)/49]]),G:stat([[51,101],[49,(10672-51*101)/49]])};
  const world2={P:stat([[51,112],[39,119],[10,(12264-51*112-39*119)/10]]),G:stat([[49,92],[2,101],[49,(10672-49*92-2*101)/49]])};
  for(const w of [world1,world2]){assert(Math.abs(w.P.mean-122.64)<1e-9);assert(Math.abs(w.G.mean-106.72)<1e-9);assert(w.P.med===112&&w.G.med===101);assert(w.G.variance<w.P.variance);}
  assert(world1.G.onTime>world1.P.onTime);assert(world2.G.onTime<world2.P.onTime);
  const P=bounds(122.64,112,120,200),G=bounds(106.72,101,120,200);
  assert(Math.abs(P[1]-.917)<1e-9);assert(G[0]===.5&&G[1]===1);
  return {checks,laws,conditional_cap:200,illustrative_deadline:120,P,G,contrast:[G[0]-P[1],G[1]-P[0]],world1,world2,reported_mean_change_minutes:122.64-106.72,reported_mean_change_fraction:(122.64-106.72)/122.64,field_causal_data_value:false,full_repository_ci:false};
}
console.log(JSON.stringify(run(), null, 2));
