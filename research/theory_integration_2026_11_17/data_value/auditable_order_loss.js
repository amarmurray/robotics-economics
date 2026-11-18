/* Exact synthetic arithmetic; integer tenths avoid floating loss accumulation. Run: node auditable_order_loss.js */
const orderLossResearch=function orderLossResearch(){
  let checks=0;
  const assert=(condition,msg)=>{if(!condition)throw Error(msg);checks++;};
  const b=[12,6,2]; // integer tenths of synthetic captured customer contribution
  const topK=(values,k)=>{
    const v=[...values].sort((a,z)=>z-a);
    assert(k>=0&&k<=v.length,"k feasible");
    const n=Math.floor(k),fraction=k-n;
    return v.slice(0,n).reduce((a,z)=>a+z,0)+(n<v.length?fraction*v[n]:0);
  };
  const maxEnumerated=(values,k,protectedIndices=[])=>{
    let max=0,count=0;
    for(let mask=0;mask<(1<<values.length);mask++){
      const lost=values.map((_,i)=>(mask>>i)&1);
      const sumLost=lost.reduce((a,z)=>a+z,0);
      if(sumLost>k||protectedIndices.some(i=>lost[i]))continue;
      count++;
      const val=lost.reduce((a,z,i)=>a+z*values[i],0);
      if(val>max)max=val;
    }
    return {max,count};
  };
  const table=[
    {name:"routine_source",increment:11,cost:3,k:0},
    {name:"grounding_shared",increment:24,cost:4,k:1},
    {name:"new_embodiment",increment:35,cost:10,k:2},
    {name:"competent_specialist",increment:10,cost:1,k:0},
    {name:"grounding_pinned",increment:24,cost:6,k:0}
  ].map(x=>({...x,worstLoss:topK(b,x.k),lower:(x.increment-x.cost-topK(b,x.k))/10,upper:(x.increment-x.cost)/10}));
  const expected=[
    ["routine_source",0,0.8,0.8],
    ["grounding_shared",12,0.8,2],
    ["new_embodiment",18,0.7,2.5],
    ["competent_specialist",0,0.9,0.9],
    ["grounding_pinned",0,1.8,1.8]
  ];
  table.forEach((row,i)=>{
    const e=expected[i];assert(row.name===e[0],"policy label "+i);
    assert(row.worstLoss===e[1],"max loss "+i);
    assert(Math.abs(row.lower-e[2])<1e-12,"lower "+i);
    assert(Math.abs(row.upper-e[3])<1e-12,"upper "+i);
    const emax=maxEnumerated(b,row.k);
    assert(row.worstLoss===emax.max,"integer extreme "+i);
  });
  assert(topK(b,1.5)===15,"fractional top-k LP");
  const full=maxEnumerated(b,1);
  const protectedB1=maxEnumerated(b,1,[0]);
  assert(full.max===12,"all B exposed");
  assert(protectedB1.max===6,"B1 protected");
  const groundingProtected=(24-4-protectedB1.max)/10;
  const groundingProtectedWithNewCutCost=(24-4-2-protectedB1.max)/10;
  assert(Math.abs(groundingProtected-1.4)<1e-12,"audit improvement");
  assert(Math.abs(groundingProtectedWithNewCutCost-1.2)<1e-12,"costed cut");
  const gPinThreshold=(6+9)/10;
  assert(gPinThreshold===1.5,"specialist comparison threshold");
  // A two-row budgeted-loss polytope (l1+l2<=1, l2+l3<=1) has exact integer max b1+b3=14.
  let networkBest=0;
  for(let m=0;m<8;m++){
    const l=[m&1,(m>>1)&1,(m>>2)&1];
    if(l[0]+l[1]<=1&&l[1]+l[2]<=1)networkBest=Math.max(networkBest,l.reduce((s,x,i)=>s+x*b[i],0));
  }
  assert(networkBest===14,"two overlapping groups primal exact");
  // Feasible dual certificate lambda=(12,2), mu=(0,0,0): H^T lambda=(12,14,2)>=b
  const dualConstraints=[12,14,2];
  dualConstraints.forEach((v,i)=>assert(v>=b[i],"dual variable feasibility "+i));
  assert(12+2===networkBest,"dual and primal identical");
  // Same loss marginals can yield identical expected additive lost contribution with opposite correlation.
  const anti=[{l:[1,0],p:0.5},{l:[0,1],p:0.5}];
  const pro=[{l:[1,1],p:0.5},{l:[0,0],p:0.5}];
  const expectedLinear=(law)=>law.reduce((s,z)=>s+z.p*(b[0]*z.l[0]+b[1]*z.l[1]),0);
  const expectedJoint=(law)=>law.reduce((s,z)=>s+z.p*z.l[0]*z.l[1],0);
  assert(expectedLinear(anti)===expectedLinear(pro),"additive mean needs only marginals");
  assert(expectedLinear(anti)===9,"linear mean value");
  assert(expectedJoint(anti)===0&&expectedJoint(pro)===0.5,"joint outcomes require copula");
  const robustPick=table.reduce((best,row)=>row.lower>best.lower?row:best,table[0]);
  assert(robustPick.name==="grounding_pinned","menu maximin");
  const robustUnpinned=table.filter(x=>x.name!=="grounding_pinned").reduce((best,row)=>row.lower>best.lower?row:best);
  assert(robustUnpinned.name==="competent_specialist","unpinned menu maximin");
  assert(table[2].increment>table[1].increment&&table[2].lower<table[1].lower,"technical vs economics");
  return {scope:"synthetic normalized complete-service contribution; no empirical calibration",date:"2026-11-18",
    baseline:{A:5,B:b.map(x=>x/10),total:7},table,allBOneLossMax:full.max/10,
    protectedHighMarginOneLossMax:protectedB1.max/10,
    groundingWithVerifiedProtectedB1Lower:groundingProtected,
    groundingWithNewCostlyCutLower:groundingProtectedWithNewCutCost,
    pinnedGroundingIncrementThresholdAgainstSpecialist:gPinThreshold,
    twoOverlappingGroups:{primalWorstLoss:networkBest/10,feasibleDualWorstLoss:(12+2)/10,dualLambda:[1.2,0.2]},
    additiveVersusJoint:{meanLinearLoss:expectedLinear(anti)/10,simultaneousLossProbabilityAnti:expectedJoint(anti),simultaneousLossProbabilityPro:expectedJoint(pro)},
    bestWorstCaseWithPinned:robustPick.name,bestWorstCaseWithoutPinned:robustUnpinned.name,
    checkCount:checks};
};
const result=orderLossResearch();
console.log(JSON.stringify(result,null,2));
