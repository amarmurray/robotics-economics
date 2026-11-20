// Exact synthetic independent-qualification/source diversity and embodiment timing model.
// All numbers are stipulated normalized customer contribution, not field evidence.
function exactModel(){
  let assertions=0, grids=0;
  const check=(v,msg)=>{if(!v)throw Error(msg);assertions++};
  const gcd=(a,b)=>b?gcd(b,a%b):a;
  const fraction=(n,d)=>{const g=gcd(Math.abs(n),d);return d/g===1?String(n/g):`${n/g}/${d/g}`};
  const evaluate=(den,i,j,k,a,mode)=>{
    const counts=[den-i-j+k,i-k,j-k,k];
    const payoff=mode==="flex"?[40,20+2*a,20+2*a,4*a]:
       mode==="locked"?[40,20+2*a,20+2*a,20+2*a]:
       [40,40,40,4*a];
    const numerator=counts.reduce((s,c,t)=>s+c*payoff[t],0);
    const analytic=mode==="flex"?40*den+(2*a-20)*(i+j):
       mode==="locked"?40*den+(2*a-20)*(i+j-k):
       40*den+(4*a-40)*k;
    check(numerator===analytic,`formula ${den}/${i}/${j}/${k}/${a}/${mode}`);
    return numerator;
  };
  for(const den of [2,3,4,5,6,7,8,9,10,11,12]){
    for(let i=0;i<=den;i++)for(let j=0;j<=den;j++){
      for(let k=Math.max(0,i+j-den);k<=Math.min(i,j);k++){
        const cells=[den-i-j+k,i-k,j-k,k];
        check(cells.every(v=>v>=0)&&cells.reduce((a,b)=>a+b,0)===den,"four-cell law");
        check(cells[1]+cells[3]===i && cells[2]+cells[3]===j,"marginal qualification rates");
        for(const a of [10,15,18,20]){
          const flex=evaluate(den,i,j,k,a,"flex");
          const locked=evaluate(den,i,j,k,a,"locked");
          const bundle=evaluate(den,i,j,k,a,"bundle");
          check(flex-locked===(2*a-20)*k,"configuration option identity");
          check(flex>=locked,"retained menu monotonicity");
          grids++;
        }
      }
    }
  }
  const den=25,i=15,j=15,a=15,lo=5,hi=15;
  const examples={};
  for(const k of [lo,9,hi]){
    const flex=evaluate(den,i,j,k,a,"flex");
    const locked=evaluate(den,i,j,k,a,"locked");
    const bundle=evaluate(den,i,j,k,a,"bundle");
    const entry={flex:fraction(flex,20*den),locked:fraction(locked,20*den),bundle:fraction(bundle,20*den),
      gross_flexibility:fraction(flex-locked,20*den),
      net_flexibility_after_cost_1_5:fraction(flex-locked-20*den/5,20*den)};
    examples[fraction(k,den)]=entry;
  }
  check(examples["1/5"].locked==="5/2"&&examples["3/5"].locked==="23/10","prelock endpoints");
  check(examples["1/5"].bundle==="11/5"&&examples["3/5"].bundle==="13/5","paired-certificate endpoints");
  const aligned=[["A","A"],["B","B"]].reduce((s,[theta,qual])=>s+Math.max(2,theta===qual?4:0),0)/2;
  const anti=[["A","B"],["B","A"]].reduce((s,[theta,qual])=>s+Math.max(2,theta===qual?4:0),0)/2;
  check(aligned===4&&anti===2,"endogenous regime counterworld");
  return {scope:"conditional synthetic paid-production proxy, no empirical qualification/payment/safety evidence",
    alpha:"3/4",pA:"3/5",pB:"3/5",sharp_joint_qualification_bounds:["1/5","3/5"],
    examples, endogenous_regime_counterworld:{pA:"1/2",pB:"1/2",joint_success:"0",perfect_report:true,aligned,anti},
    enumerated_joint_laws_by_grid:grids/4, architecture_cases:grids, exact_integer_assertions:assertions,
    no_actual_physical_admission:true,no_actual_buyer_panel:true,no_full_repository_CI:true};
}
if (typeof console !== "undefined") console.log(JSON.stringify(exactModel(), null, 2));
