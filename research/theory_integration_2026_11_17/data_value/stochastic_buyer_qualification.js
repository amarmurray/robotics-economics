// Original buyer stochastic menu/qualification theory (20 November 2026 UTC).
// Exact integer arithmetic; no real robot or customer evidence.
function run(){
  let assertions=0, sixCellLaws=0, fixedResponseLaws=0;
  function check(value,msg){assertions++;if(!value)throw new Error(msg);}
  // Original buyer choice potential outcomes under two disclosed operator capacity policies.
  // Six atoms: N_1 in {0,1} and N_2 in {0,1,2}; exhaustive laws with denominator 7.
  const cells=[[0,0],[0,1],[0,2],[1,0],[1,1],[1,2]];
  function visit(i,left,a){
    if(i===5){
      a[i]=left;sixCellLaws++;
      let n1=0,n2=0,p11=0,p21=0,p22=0;
      for(let j=0;j<6;j++){
        const [v1,v2]=cells[j],w=a[j];n1+=w*v1;n2+=w*v2;
        if(v1>=1)p11+=w;if(v2>=1)p21+=w;if(v2>=2)p22+=w;
      }
      check(n2-n1===p21-p11+p22,"capacity-policy buyer-response identity");
      check(p22<=p21,"tail feasibility");
      return;
    }
    for(let w=0;w<=left;w++){a[i]=w;visit(i+1,left-w,a)}
  }
  visit(0,7,Array(6).fill(0));
  for(let a=0;a<=9;a++)for(let b=0;b<=9-a;b++){
    const c=9-a-b;fixedResponseLaws++;
    const h1=b+c, h2=b+2*c;
    check(h2-h1===c,"fixed-response second-slot tail");
    check(h2>=h1,"fixed-response monotonicity");
  }
  function purchase(price,secondValue,slots){
    const valuations=[7,secondValue];
    let best=-Infinity,bestUnits=0,bestMask=0;
    for(let mask=0;mask<4;mask++){
      const n=((mask&1)?1:0)+((mask&2)?1:0);
      if(n>slots || price*n>8)continue;
      let u=-price*n;for(let j=0;j<2;j++)if(mask&(1<<j))u+=valuations[j];
      if(u>best || (u===best && n>bestUnits)){best=u;bestUnits=n;bestMask=mask}
    }
    check(best>=0,"no-purchase outside feasible");
    return {units:bestUnits,mask:bestMask};
  }
  function policy(value2,slots,costNumerator2){
    let best=null;
    for(const price of [4,5,6]){
      const sales=purchase(price,value2,slots).units;
      const net2=price*sales-costNumerator2; // high market occurs with probability 1/2
      if(!best||net2>best.net2)best={price,sales,net2};
    }
    return best;
  }
  const worlds={
    secondValue3:{X:policy(3,1,0),G:policy(3,2,1),E:policy(3,2,4),R:{net2:4}},
    secondValue5:{X:policy(5,1,0),G:policy(5,2,1),E:policy(5,2,4),R:{net2:4}}
  };
  check(worlds.secondValue3.X.net2===6&&worlds.secondValue5.X.net2===6,"equal X incumbent");
  check(worlds.secondValue3.G.net2===5&&worlds.secondValue5.G.net2===7,"stochastic parent-choice reversal");
  check(worlds.secondValue3.E.net2===2&&worlds.secondValue5.E.net2===4,"body investment compare");
  check(worlds.secondValue3.G.price===6&&worlds.secondValue5.G.price===4,"endogenous menu switching");
  const thresholds=[];
  for(let a=0;a<=8;a++){
    const G8=Math.max(20,12+2*a),X8=24; // q=1/2, kG=1/2, a is conditional second purchase probability in eighths
    check((G8>X8)===(a>6),"sharp second-purchase threshold");
    thresholds.push({conditional_second_purchase_eighths:a, G_net_eighths:G8, X_net_eighths:X8});
  }
  // Joint second-unit buyer purchase C and incremental G qualification Q.
  // Only marginal probabilities known: P(C)=4/10, P(Q)=5/10, P(H)=5/10, C subset H.
  // The Fréchet sharp range is P(C&Q) in [0,4/10].
  const jointWorlds=[
    {label:"misaligned",H:5,C:4,Q:5,CandQ:0},
    {label:"aligned",H:5,C:4,Q:5,CandQ:4}
  ];
  for(const w of jointWorlds){
    check(w.CandQ>=Math.max(0,w.C+w.Q-10)&&w.CandQ<=Math.min(w.C,w.Q),"joint eligibility legal");
    const G10=Math.max(6*w.H,4*(w.H+w.CandQ))-5; // 1/2 cost in tenths
    const X10=6*w.H,E10=Math.max(6*w.H,4*(w.H+w.C))-20,R10=20;
    w.net_tenths={X:X10,G:G10,E:E10,R:R10};
  }
  check(jointWorlds[0].net_tenths.G===25&&jointWorlds[1].net_tenths.G===31,"joint gate changed ranking");
  check(jointWorlds[0].net_tenths.X===30&&jointWorlds[1].net_tenths.X===30,"source unaffected");
  check(jointWorlds[0].net_tenths.E===16&&jointWorlds[1].net_tenths.E===16,"embodiment unaffected");
  const informativeAudit=[];
  for(let mistakes=0;mistakes<=8;mistakes++){
    // Equiprobable two utility worlds. Conditional signal accuracy (8-mistakes)/8.
    // Compare optimal expected value of conditionally choosing G or X with blind max=3.
    const evsiNumerator16=Math.abs(4-mistakes);
    const directNumerator16=Math.max(4-mistakes,mistakes-4);
    check(evsiNumerator16===directNumerator16&&evsiNumerator16>=0,"Bayes signal decision value");
    informativeAudit.push({symmetric_error_eighths:mistakes,EVSI_sixteenths:evsiNumerator16});
  }
  // Independent knapsack limitation for non-uniform prices and buyer budgets: unit-slot values need not be concave.
  const items=[{price:3,margin10:11},{price:1,margin10:10},{price:1,margin10:10},{price:1,margin10:10}];
  const capacities=[0,1,2,3],capValues=[];
  for(const h of capacities){
    let best=0;
    for(let mask=0;mask<16;mask++){
      let count=0,price=0,margin10=0;
      for(let i=0;i<4;i++)if(mask&(1<<i)){count++;price+=items[i].price;margin10+=items[i].margin10}
      if(price<=3&&count<=h)best=Math.max(best,margin10);
    }
    capValues.push(best);
  }
  check(JSON.stringify(capValues)===JSON.stringify([0,11,20,30]),"budget knapsack nonconcavity");
  check(capValues[3]-capValues[2]>capValues[2]-capValues[1],"increment increases after falling");
  return {status:"synthetic-conditional-only",method:"integer exact numerator enumeration; not scientific field evidence or mathematical proof",
    six_cell_laws:sixCellLaws,fixed_response_laws:fixedResponseLaws,assertions,
    worlds,thresholds,jointWorlds,informativeAudit,
    budget_knapsack_capacity_values_tenths:capValues,
    evidence:{actual_customer_choice_records:false,actual_robot_qualification:false,validated_spillover_envelope:false,full_repo_CI:false,independent_novelty:false}};
}
if (typeof module !== 'undefined' && require.main === module) console.log(JSON.stringify(run(),null,2));
module.exports={run};
