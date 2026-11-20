// CPU-only exact rational verification of conditional source-admission and coverage claims.
// No dataset downloaded, model trained, robot operated, or original customer observed.
function run(){
  let checks=0;
  const gcd=(a,b)=>{a=a<0n?-a:a;b=b<0n?-b:b;while(b){let t=a%b;a=b;b=t}return a};
  const f=(a,b=1)=>{a=BigInt(a);b=BigInt(b);if(b===0n)throw Error("zero denominator");if(b<0n){a=-a;b=-b}const g=gcd(a,b);return {n:a/g,d:b/g}};
  const add=(a,b)=>f(a.n*b.d+a.d*b.n,a.d*b.d);
  const sub=(a,b)=>f(a.n*b.d-a.d*b.n,a.d*b.d);
  const mul=(a,b)=>f(a.n*b.n,a.d*b.d);
  const div=(a,b)=>f(a.n*b.d,a.d*b.n);
  const str=a=>a.d===1n?String(a.n):`${a.n}/${a.d}`;
  const eq=(a,b)=>{checks++;if(a.n!==b.n||a.d!==b.d)throw Error(`${str(a)} != ${str(b)}`)};
  const one=f(1),half=f(1,2),ten=f(10);
  const episodeMean=f(1,2);
  const transitionMean=div(add(mul(f(1),f(1)),mul(f(9),f(0))),f(10));
  eq(episodeMean,half);eq(transitionMean,f(1,10));
  const w=half,rS=transitionMean,rT=one;
  const R=add(mul(w,rS),mul(sub(one,w),rT));
  const qS=div(mul(w,rS),R);
  const episodeBasedQ=div(mul(w,episodeMean),add(mul(w,episodeMean),mul(sub(one,w),rT)));
  eq(R,f(11,20));eq(qS,f(1,11));eq(episodeBasedQ,f(1,3));
  const B=ten,K=ten,cProposal=f(1,4),cUpdate=one;
  const acceptedFixedB=mul(B,R);
  const sAcceptedFixedB=mul(B,mul(w,rS));
  const proposalsFixedK=div(K,R);
  const sAcceptedFixedK=mul(K,qS);
  const costFixedB=add(mul(B,cProposal),mul(acceptedFixedB,cUpdate));
  const costFixedK=add(mul(proposalsFixedK,cProposal),mul(K,cUpdate));
  eq(acceptedFixedB,f(11,2));eq(sAcceptedFixedB,half);
  eq(proposalsFixedK,f(200,11));eq(sAcceptedFixedK,f(10,11));
  eq(costFixedB,f(8));eq(costFixedK,f(160,11));
  const pA=half,pB=half;
  const union=(joint)=>sub(add(pA,pB),joint);
  const uPositive=union(f(0)),uIndependent=union(f(1,4)),uCoupled=union(half);
  eq(uPositive,one);eq(uIndependent,f(3,4));eq(uCoupled,half);
  const qualifiedGross=u=>mul(f(4),u),embodimentGross=f(5,2);
  eq(qualifiedGross(uCoupled),f(2));eq(qualifiedGross(uIndependent),f(3));eq(qualifiedGross(uPositive),f(4));
  if(!(qualifiedGross(uCoupled).n*embodimentGross.d<embodimentGross.n*qualifiedGross(uCoupled).d))throw Error("coupled preference");
  if(!(qualifiedGross(uIndependent).n*embodimentGross.d>embodimentGross.n*qualifiedGross(uIndependent).d))throw Error("independent preference");
  checks+=2;
  for(let a=1;a<=20;a++)for(let b=1;b<=20;b++){
    const rt=f(a,a+b),rr=add(mul(half,rt),mul(half,one)),qq=div(mul(half,rt),rr);
    eq(qq,f(a,2*a+b));
    eq(add(qq,div(mul(half,one),rr)),one);
  }
  return {
    status:"exact-rational-conditional-synthetic",
    scoped_assertions:checks,episode_length_grid_cases:400,
    eligible_episode_mean:str(episodeMean),eligible_transition_mean:str(transitionMean),
    source_admitted_share_correct:str(qS),source_share_using_episode_mean_wrong:str(episodeBasedQ),
    all_source_retention:str(R),
    fixed_10_proposals:{expected_accepted:str(acceptedFixedB),expected_source_S_accepted:str(sAcceptedFixedB),expected_total_proposal_plus_update_cost:str(costFixedB)},
    fixed_10_accepted:{expected_proposals:str(proposalsFixedK),expected_source_S_accepted:str(sAcceptedFixedK),expected_total_proposal_plus_update_cost:str(costFixedK)},
    equal_marginal_two_unit_rare_context_coverage:{coupled:str(uCoupled),independent:str(uIndependent),anticorrelated:str(uPositive)},
    stipulated_original_customer_gross:{coupled:str(qualifiedGross(uCoupled)),independent:str(qualifiedGross(uIndependent)),anticorrelated:str(qualifiedGross(uPositive)),certified_generalist:str(embodimentGross)},
    empirical_robot_or_training_data:false,nov22_scientific_gate_passed:false
  };
}
console.log(JSON.stringify(run(),null,2));
