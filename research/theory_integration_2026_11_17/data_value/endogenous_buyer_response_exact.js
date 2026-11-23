// Exact synthetic common-law buyer-response audit; Node 18+; no dependencies.
// Run: node endogenous_buyer_response_exact.js
'use strict';
function runExact() {
  let checks=0, laws=0;
  const check=(ok,msg)=>{checks++; if(!ok) throw Error(msg);};
  const values=[];
  for (let k=0;k<=10;k++) {
    // D and baseline C_R are independent fair offers. Conditional probabilities
    // of C_G=1 are k/10 if D=1 and (10-k)/10 if D=0.
    // Each atom below carries weight /40, giving one common potential-outcome law.
    let total=0, rBoth=0, gBoth=0, gD=0, gC=0, gPaid=0;
    for (let d=0;d<=1;d++) for(let cr=0;cr<=1;cr++) for(let cg=0;cg<=1;cg++){
      const p1=d===1 ? k : (10-k);
      const weight=cg===1 ? p1 : (10-p1);
      total+=weight;
      if(d===1 && cr===1) rBoth+=weight;
      if(d===1 && cg===1) gBoth+=weight;
      if(d===1) gD+=weight;
      if(cg===1) gC+=weight;
      gPaid+=weight*Math.max(2*d,3*cg);
    }
    check(total===40,'normalization k='+k);
    check(rBoth===10,'full baseline paired demand fixed k='+k);
    check(gBoth===2*k,'G joint D,C k='+k);
    check(gD===20 && gC===20,'G half marginals k='+k);
    check(gPaid===100-4*k,'paid production k='+k);
    check(4*(25-k)===100-4*k,'closed form k='+k);
    values.push({k,xG:[k,20],Gskip:[25-k,10],baselinePaired:[1,4]});
    laws++;
  }
  // All these comparisons use integer arithmetic in a common unit /20 or /10.
  check(16+24===40,'P: 4/5 plus 3*(1/2)*(4/5) equals 2');
  check(10+15-4===21,'E: 2*(1/2)+3*(1/2)-2/5 equals 21/10');
  check(16+15===31,'G serve: 4/5+3*(1/2)*(1/2)=31/20');
  check(2*1===2,'R: b*Pr(D)=1');
  check((2+3+3+0)===8,'G under pre-offer exclusion equals 2');
  const feasible=values.filter(v=>v.k>=2 && v.k<=8);
  check(feasible.length===7,'bounded law count');
  check(25-feasible[0].k===23,'G upper 23/10');
  check(25-feasible[6].k===17,'G lower 17/10');
  let best=999999, bestM=-1;
  for(let m=0;m<=60;m++){
    // G share q=m/60; regrets in units /600.
    const regretF=(60-m)*2, regretH=m*4;
    const worst=Math.max(regretF,regretH);
    check(worst>=80,'minimax certificate m='+m);
    if(worst<best){best=worst;bestM=m;}
  }
  check(best===80 && bestM===20,'minimax G=1/3 regret 2/15');
  check((23+21)-2*21===2,'precommitment perfect report gross VOI=1/10');
  return {type:'conditional synthetic rational/integer construction, not field evidence',
    laws,checks,baseline_overlap:'1/4',P:'2',E:'21/10',R:'1',
    G_preoffer_exclusion:'2',G_range_without_response_restriction:['3/2','5/2'],
    assumed_overlap_radius:'3/20',G_conditional_range:['17/10','23/10'],
    regret_optimal_G_share:'1/3',regret_optimum:'2/15',
    hypothetical_perfect_early_report_VOI:'1/10',values};
}
if (typeof module!=='undefined' && require.main===module) console.log(JSON.stringify(runExact(),null,2));
