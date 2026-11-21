// Conditional exact-utility partial-ID experiment comparison. No physical robot data.
// Run: node decision_sufficient_evidence.js
const researchModel = function researchModel(){
  let assertions=0;
  const gcd=(a,b)=>{while(b){let t=a%b;a=b;b=t;}return a<0n?-a:a;};
  const frac=(n,d=1n)=>{n=BigInt(n);d=BigInt(d);if(d<0n){n=-n;d=-d;}if(d===0n)throw Error("zero denominator");let g=gcd(n,d);return {n:n/g,d:d/g};};
  const fm=f=>f.d===1n?String(f.n):`${f.n}/${f.d}`;
  const compare=(x,y)=>x.n*y.d-y.n*x.d;
  const greater=(x,y)=>compare(x,y)>=0n?x:y;
  const equal=(x,y)=>{assertions++;if(compare(x,y)!==0n)throw Error(`expected ${fm(y)} got ${fm(x)}`);};
  const measure=(al,au,bl,bu,mixed=true)=>{
    if(!(al<=au&&bl<=bu))throw Error("bad interval");
    const U=Math.max(0,au-bl),V=Math.max(0,bu-al);
    return mixed?(U+V?frac(BigInt(U)*BigInt(V),BigInt(U+V)*24n):frac(0n)):frac(BigInt(Math.min(U,V)),24n);
  };
  const A=[-24,120],B=[72,120];
  const baseMix=measure(...A,...B),baseDet=measure(...A,...B,false);
  let maxA=frac(0n),argA=[],maxB=frac(0n),argB=[],detA=frac(0n),detB=frac(0n);
  for(let a=A[0];a<=A[1];a++){
    let m=measure(a,a,...B),d=measure(a,a,...B,false);
    if(compare(m,maxA)>0){maxA=m;argA=[a];}else if(compare(m,maxA)===0)argA.push(a);
    detA=greater(detA,d);
    assertions++;
    if(a<=72){equal(m,frac(0n));}
    else{equal(m,frac(BigInt(a-72)*BigInt(120-a),48n*24n));}
  }
  for(let b=B[0];b<=B[1];b++){
    let m=measure(...A,b,b),d=measure(...A,b,b,false);
    if(compare(m,maxB)>0){maxB=m;argB=[b];}else if(compare(m,maxB)===0)argB.push(b);
    detB=greater(detB,d);
    equal(m,frac(BigInt(120-b)*BigInt(b+24),144n*24n));assertions++;
  }
  equal(baseMix,frac(3n,2n));equal(baseDet,frac(2n));
  equal(maxA,frac(1n,2n));equal(maxB,frac(4n,3n));
  equal(detA,frac(1n));equal(detB,frac(2n));
  if(argA.join(",")!=="96"||argB.join(",")!=="72")throw Error("incorrect sharp argmax");
  assertions+=2;
  // Direct all-corner policy checks, without calling the minimax formula.
  const brute=(al,au,bl,bu)=>{
    let best=null,at=[];
    for(let k=0;k<=96;k++){
      let worst=0;
      for(const a of [al,au])for(const b of [bl,bu]){
        const numerator=a>=b?(96-k)*(a-b):k*(b-a);
        worst=Math.max(worst,numerator);
      }
      const r=frac(BigInt(worst),96n*24n);
      if(best===null||compare(r,best)<0){best=r;at=[k];}
      else if(compare(r,best)===0)at.push(k);
      assertions++;
    }
    return {value:best,probability_ticks:at};
  };
  const checks=[{ranges:[...A,...B],v:frac(3n,2n),p:24},{ranges:[96,96,...B],v:frac(1n,2n),p:48},{ranges:[...A,72,72],v:frac(4n,3n),p:32}];
  for(const z of checks){const q=brute(...z.ranges);equal(q.value,z.v);if(!q.probability_ticks.includes(z.p))throw Error("policy optimizer failed");assertions++;}
  // Same Pr(qualified)=Pr(buyer willing)=1/2; opposite joint paid-service performance.
  const worlds=[[[0,0,1],[1,1,1]],[[0,1,1],[1,0,1]]];
  const worldOut=worlds.map(world=>{
    const n=world.reduce((s,r)=>s+r[0]*r[1]*r[2],0);
    const qualified=world.reduce((s,r)=>s+r[0]*r[2],0);
    const willing=world.reduce((s,r)=>s+r[1]*r[2],0);
    if(qualified!==1||willing!==1)throw Error("marginal mismatch");assertions+=2;
    return {p_qualified:"1/2",p_buyer_willing:"1/2",p_joint_paid:fm(frac(BigInt(n),2n)),SG_net:fm(frac(12n*BigInt(n),2n).n?frac(6n*BigInt(n)-1n):frac(-1n))};
  });
  equal(frac(BigInt(worldOut[0].SG_net)),frac(5n));
  equal(frac(BigInt(worldOut[1].SG_net)),frac(-1n));
  return {type:"conditional_synthetic_not_robotics_evidence",economic_bounds:{SG_net:[-1,5],E_net:[3,5]},units:"normalized whole original-buyer accepted-paid contribution",oracle_test:"reveals exact program-average contribution, not a finite sample",randomized_cluster_menu:{no_test_worst_regret:fm(baseMix),SG_joint_paid_oracle_worst_regret:fm(maxA),E_whole_program_oracle_worst_regret:fm(maxB),SG_max_at:fm(frac(BigInt(argA[0]),24n)),E_max_at:fm(frac(BigInt(argB[0]),24n)),baseline_probability_SG:"1/4",SG_oracle_cost_ceiling_vs_none:"1",E_oracle_cost_ceiling_vs_none:"1/6",SG_minus_E_test_cost_difference_limit:"5/6"},deterministic_menu:{no_test_worst_regret:fm(baseDet),SG_joint_paid_oracle_worst_regret:fm(detA),E_whole_program_oracle_worst_regret:fm(detB)},buyer_coupling_counterworlds:worldOut,checked_perfect_SG_reports:145,checked_perfect_E_reports:49,corner_policy_grid_checks:291,assertions};
};
const result = researchModel();
if (typeof module !== "undefined") module.exports = {researchModel};
if (typeof require !== "undefined" && require.main === module) console.log(JSON.stringify(result,null,2));
