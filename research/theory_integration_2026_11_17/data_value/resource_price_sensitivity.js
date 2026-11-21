// Exact grid corroboration of conditional approximate-invariance theorem.
// Reproducible synthetic original-buyer/operator calculation. Node 18+ or V8.
function fraction(n,d) {
  function gcd(a,b){while(b){let t=a%b;a=b;b=t}return a}
  const g=gcd(n,d);return (d/g===1)?String(n/g):String(n/g)+"/"+String(d/g);
}
function run() {
  let checks=0;const rows=[];
  for(let k=0;k<=8;k++){
    let lo=Infinity,hi=-Infinity,num=0;
    for(let a=0;a<=16;a++) for(let b=0;b<=16;b++) for(let c=0;c<=16;c++){
      if(Math.max(a,b,c)-Math.min(a,b,c)>2*k)continue;
      // a,b,c: original paid outside-job contributions in 1/32 units.
      // P=[2(16-a)+c]/128, N=(8+b)/128, L=min(P,N).
      const L=Math.min(2*(16-a)+c,8+b);
      lo=Math.min(lo,L);hi=Math.max(hi,L);num++;
    }
    const knownLo=Math.min(8,Math.max(0,16-2*k));
    const knownHi=Math.min(24,20+2*k);
    if(lo!==knownLo||hi!==knownHi)throw Error("endpoint mismatch "+k);
    checks+=num;
    rows.push({epsilon:fraction(k,32),min:fraction(lo,128),max:fraction(hi,128),feasible_grid_laws:num});
  }
  if(checks!==22185)throw Error("grid-count mismatch");
  return {case:"shared-outside-opportunity approximate invariance",
    assumptions:"lambda_y in [0,1/2], max pairwise spread <=2epsilon; unchanged original signed A/B rewards, predecision report probabilities, fixed learner and legally permitted network menu",
    exact_grid_laws_evaluated:checks,rows,
    status:"exact enumeration corroborates analytic constructive endpoints; synthetic only"};
}
if(typeof process!=="undefined"&&process.stdout) process.stdout.write(JSON.stringify(run(),null,2)+"\n");
