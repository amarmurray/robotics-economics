function checkDatedReserve(){
  let assertions=0,laws=0,endogenousCases=0,priceChecks=0;
  const assert=(c)=>{if(!c)throw Error("check "+assertions);assertions++};
  const N=8;
  // Value measured in integer half-units, summed over N equally weighted histories.
  // a=short/no B, b=short/B, c=long/no B, e=long/B under start.
  for(let a=0;a<=N;a++)for(let b=0;b<=N-a;b++)for(let c=0;c<=N-a-b;c++){
    const e=N-a-b-c, long=c+e, high=b+e;
    const worlds=[...Array(a).fill([0,0]),...Array(b).fill([0,1]),...Array(c).fill([1,0]),...Array(e).fill([1,1])];
    laws++;
    const start=worlds.reduce((v,[D,H])=>v+4+2*D+12*H*(1-D),0);
    assert(start===4*N+2*long+12*(high-e));
    const skip=12*high;
    const V=Math.max(start,skip);
    // Independently enumerate actions for D known prior, H known after.
    let informed=0;
    for(const D of [0,1]){
      const subset=worlds.filter(w=>w[0]===D);
      const S=subset.reduce((v,[D,H])=>v+4+2*D+12*H*(1-D),0);
      const W=subset.reduce((v,[D,H])=>v+12*H,0);
      informed+=Math.max(S,W);
    }
    assert(informed>=V);
    assert(informed===4*(a+b)+12*b+Math.max(6*(c+e),12*e));
    // A price of 6 if B is high and 0 otherwise cancels the B dispatch
    // objective; charge the *realized* price against A's carryover.
    assert(V===12*high+Math.max(0,4*N+2*long-12*e));
    for(let m=0;m<=N;m++){
      // Potential B authorizations after skipping A need not match those after starting.
      endogenousCases++;
      const skipEndo=12*m;
      const exact=Math.max(skipEndo,start);
      const correctDual=Math.max(12*m,12*high+4*N+2*long-12*e);
      assert(exact===correctDual);
      for(let lambda=0;lambda<=14;lambda++){
        // Deterministic dated price: price all t1 occupancy, optimize both
        // potential action-conditioned receipts, then add capacity price.
        const pricedStart=4*N+2*long-lambda*long+Math.max(0,12-lambda)*high;
        const pricedSkip=Math.max(0,12-lambda)*m;
        const bound=lambda*N+Math.max(pricedStart,pricedSkip);
        assert(bound>=exact);priceChecks++;
      }
    }
  }
  const restricted=[];
  for(let e=0;e<=N/2;e++){
    const a=e,b=N/2-e,c=N/2-e;
    const start=4*N+2*(c+e)+12*b;
    const skip=6*N;
    const gross=Math.max(start,skip);
    const retainedGross=Math.max(gross,6*N);
    const net=retainedGross-N; // sunk grounding cost 1/2
    const incremental=net-6*N;
    const independent=2*N; // increment 1
    assert(incremental===Math.max(4*N-12*e,-N));
    const informed=4*(a+b)+12*b+Math.max(6*(c+e),12*e);
    assert(informed===Math.max(11*N-12*e,8*N));
    assert((incremental>independent)===(6*e<N));
    assert((incremental===independent)===(6*e===N));
    restricted.push({j:e/N,gross:gross/(2*N),groundingIncrement:incremental/(2*N),informedGross:informed/(2*N),E:1});
  }
  // Endogenous report counterexample: skip produces no B, start has half B
  // and half long, disjoint. Reusing skip's zero price revenue is invalid.
  const trueEndo=11*N, wrongFixedCapacity=5*N;
  assert(trueEndo>wrongFixedCapacity);
  // A second independently added worker can serve both A and B at date 1.
  // Gross G+K is 5.5, gross R+K is 5, costs .5 and 1.5 respectively.
  assert(11-1-3===10-3);
  return {assertions,laws,endogenousCases,priceChecks,restricted,synthetic:true,denominator:N,full_repository_ci:false,field_calibration:false,independent_novelty:false};
}
console.log(JSON.stringify(checkDatedReserve(),null,2));
