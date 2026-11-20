"use strict";

function runJointNetworkModel() {
  const arms=["RR","RG","GR","GG","E"], assignable=["RR","GG","E"];
  let assertions=0;
  function check(p,message){if(!p)throw Error("Failed: "+message); assertions++;}
  function net(arm,budget,veto=false){
    if(arm==="X")throw Error("Unapproved X is excluded");
    const op={RR:[2,2],RG:[2,1],GR:[1,2],GG:[1,1],E:[2,2]}[arm];
    if(!op)throw Error("Undefined whole policy "+arm);
    const cap=arm==="E"?4:2;
    let best=0;
    for(let mask=0;mask<4;mask++){
      if(arm==="GG"&&veto&&mask===3)continue;
      const price=((mask&1)?4:0)+((mask&2)?3:0);
      const load=((mask&1)?op[0]:0)+((mask&2)?op[1]:0);
      if(price<=budget && load<=cap)best=Math.max(best,price);
    }
    return best-(arm==="E"?1:0);
  }
  function fraction(n,d=1n){
    n=BigInt(n);d=BigInt(d);
    if(!d)throw Error("zero denominator");
    if(d<0n){n=-n;d=-d;}
    let a=n<0n?-n:n,b=d;
    while(b){const t=a%b;a=b;b=t;}
    return {n:n/a,d:d/a};
  }
  function plus(a,b){return fraction(a.n*b.d+b.n*a.d,a.d*b.d);}
  function minus(a,b){return fraction(a.n*b.d-b.n*a.d,a.d*b.d);}
  function times(a,b){return fraction(a.n*b.n,a.d*b.d);}
  function str(x){return x.n.toString()+"/"+x.d.toString();}
  const budgets=[6,6,8,8];
  function truth(veto){return budgets.map((budget,i)=>({cluster_id:"S"+(i+1),original_orders:["A","B"],pre_assignment_parent_budget:budget,oracle_y:Object.fromEntries(assignable.map(a=>[a,net(a,budget,veto)]))}));}
  function moments(rows,a,b) {
    let sum=0n,sumsq=0n,cases=0n;
    for(let code=0;code<81;code++){
      let k=code,numerator=0n;
      for(let i=0;i<4;i++){const arm=assignable[k%3];k=Math.floor(k/3);
        if(arm===a)numerator+=3n*BigInt(rows[i].oracle_y[a]);
        if(arm===b)numerator-=3n*BigInt(rows[i].oracle_y[b]);
      }
      sum+=numerator;sumsq+=numerator*numerator;cases++;
    }
    const mean=fraction(sum,4n*cases);
    const e2=fraction(sumsq,16n*cases);
    const variance=minus(e2,times(mean,mean));
    const truth=fraction(rows.reduce((s,r)=>s+r.oracle_y[a]-r.oracle_y[b],0),4);
    check(mean.n===truth.n&&mean.d===truth.d,"whole-cluster HT unbiased for "+a+"-"+b);
    return {assignments:Number(cases),true_contrast:str(truth),design_expectation_HT:str(mean),design_variance_HT:str(variance)};
  }
  for(const budget of [6,8]){
    for(const arm of ["RR","RG","GR"])check(net(arm,budget)===4,"single slot");
    check(net("GG",budget)===(budget===8?7:4),"joint GG");
    check(net("GG",budget,true)===4,"joint procurement veto");
    check(net("E",budget)===(budget===8?6:3),"embodiment");
  }
  let excluded=false;try{net("X",8);}catch(e){excluded=true;}check(excluded,"X excluded");
  const high=truth(false),low=truth(true);
  for(const [name,rows,total] of [["high GG",high,22],["low GG",low,16]]){
    check(rows.reduce((s,r)=>s+r.oracle_y.GG,0)===total,name);
  }
  check(high.reduce((s,r)=>s+r.oracle_y.E,0)===18,"E sum");
  check(high.reduce((s,r)=>s+r.oracle_y.RR,0)===16,"R sum");
  let mixedCases=0;
  for(let code=0;code<16;code++){
    let sumHigh=0,sumLow=0;
    for(let i=0;i<4;i++){const arm=(code&(1<<i))?"RG":"GR";sumHigh+=net(arm,budgets[i],false);sumLow+=net(arm,budgets[i],true);}
    check(sumHigh===16&&sumLow===16,"mixed-only indistinguishability");mixedCases++;
  }
  const highMoments={},lowMoments={};
  for(const [a,b] of [["GG","RR"],["E","RR"],["GG","E"]]){
    highMoments[a+"-"+b]=moments(high,a,b);
    lowMoments[a+"-"+b]=moments(low,a,b);
  }
  check(highMoments["GG-RR"].true_contrast==="3/2","high G-R");
  check(lowMoments["GG-RR"].true_contrast==="0/1","low G-R");
  check(highMoments["GG-E"].true_contrast==="1/1","high G-E");
  check(lowMoments["GG-E"].true_contrast==="-1/2","low G-E");
  for(const budget of [6,8])for(const arm of ["RR","RG","GR","E"])check(net(arm,budget,false)===net(arm,budget,true),"no on-support buyer information");
  const half=fraction(1,2),e=fraction(9,2),grossHigh=fraction(11,2),grossLow=fraction(4);
  const gHigh=minus(grossHigh,half),gLow=minus(grossLow,half);
  const gPrior=times(plus(gHigh,gLow),half);
  const vNo=e.n*gPrior.d>=gPrior.n*e.d?e:gPrior;
  const vInfo=times(plus(gHigh,e),half);
  check(str(vNo)==="9/2"&&str(vInfo)==="19/4"&&str(minus(vInfo,vNo))==="1/4","binding target decision value");
  return {
    scope:"EXCLUSIVELY SYNTHETIC two-order procurement/operator network. Not empirical robotics economics or physical admission.",
    created_at_utc:"2026-11-20",
    original_market:"One procurement parent with original eligible orders A(price4), B(price3); common budget 6 or 8; common operator pool; prices and net contributions stipulated equal, except E one-time cost.",
    policies:{RR:"old A=2 op,B=2 op, shared capacity2",RG:"old A=2,grounded B=1,capacity2",GR:"grounded A=1,old B=2,capacity2",GG:"grounded A=1,grounded B=1,capacity2, only if JOINT signed",E:"new embodiment allows 4 operator units, cost 1 charged once",X:"unapproved source-trained whole policy explicitly excluded"},
    oracle_high_world:high,oracle_joint_veto_world:low,
    mixed_only:{available_arms:["RG","GR"],individual_order_grounded_probability:"1/2",whole_policy_GG_probability:"0/1",identical_original_market_receipt:"4/1",observationally_identical_worlds:true},
    full_policy_randomization:{unit:"whole parent/robot/operator cluster",only_if_physically_approved:true,each_arm_probability:"1/3",exact_assignments_enumerated:81,high:highMoments,low:lowMoments},
    conditional_optional_GG_gross_mean_interval:["4/1","11/2"],
    hypothetical_buyer_data_value:{two_world_prior:["1/2","1/2"],G_certification_cost:"1/2",E_embodiment_cost:"already counted once",no_target_signal:str(vNo),perfect_binding_joint_menu_signal:str(vInfo),gross_information_gain:str(minus(vInfo,vNo)),routine_only_data_information_gain_about_joint_menu:"0/1"},
    scoped_integer_assertions:assertions,real_physical_signature:false,actual_customer_records:false,approved_live_assignments:false,source_X_admitted:false,independent_novelty_review:false
  };
}

const record = runJointNetworkModel();
if (typeof module !== "undefined") module.exports = {runJointNetworkModel};
if (typeof require !== "undefined" && require.main === module) process.stdout.write(JSON.stringify(record,null,2)+"\n");
