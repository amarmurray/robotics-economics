"use strict";
// Synthetic 20-atom finite law. Program and action values are normalized and stipulated.
function makeCase(world,i){
  if(!["disjoint","nested"].includes(world)||i<0||i>=20||!Number.isInteger(i))throw Error("invalid law or state");
  if(world==="disjoint")return {arm:i>=5,mobile:i<5||i>=10,offer:i<10||i>=14,worker:i<14||i>=18};
  return {arm:i<15,mobile:i<15,offer:i<16,worker:i<16};
}
function evaluate(world){
 let sa=0,sc=0,sd=0,sw=0,joint=0,revenue=0;
 for(let i=0;i<20;i++){let o=makeCase(world,i),u=+o.arm,v=+o.mobile,d=+o.offer,w=+o.worker,hit=u*v*d*w; sa+=u;sc+=v;sd+=d;sw+=w;joint+=hit;revenue+=w+5*hit;}
 let actionM=revenue/20-0.6,actionS=2.1;
 return {world,states:20,marginals:{arm:sa/20,mobile:sc/20,original_offer:sd/20,worker_free:sw/20},joint_qualification_and_paid_service:joint/20,paid_M_value:actionM,paid_S_value:actionS,G_optimal_with_provenance:(actionS+Math.max(actionS,actionM))/2,competitors:{R:1.5,P:2,E:2.4},qualifying_T_action:actionM>actionS?"M":"S"};
}
function assertClose(a,b,label){if(Math.abs(a-b)>1e-12)throw Error(label+": "+a+" != "+b);}
function runChecks(){
 let lo=evaluate("disjoint"),hi=evaluate("nested"),testCount=0;
 for(let z of [lo,hi]){
  for(let [k,v] of Object.entries({arm:0.75,mobile:0.75,original_offer:0.8,worker_free:0.8})){assertClose(z.marginals[k],v,k);testCount++;}
  assertClose(z.paid_M_value,0.2+5*z.joint_qualification_and_paid_service,"consistent payoff");testCount++;
  if(z.joint_qualification_and_paid_service<0.1-1e-12||z.joint_qualification_and_paid_service>0.75+1e-12)throw Error("outside Frechet");testCount++;
  for(let j=0;j<20;j++){const o=makeCase(z.world,j);if(Object.values(o).some(x=>typeof x!=="boolean"))throw Error("not Boolean");testCount++;}
 }
 assertClose(lo.joint_qualification_and_paid_service,0.1,"Frechet lower");testCount++;
 assertClose(hi.joint_qualification_and_paid_service,0.75,"Frechet upper");testCount++;
 assertClose(lo.paid_M_value,0.7,"M low");testCount++;
 assertClose(hi.paid_M_value,3.95,"M high");testCount++;
 assertClose(lo.G_optimal_with_provenance,2.1,"G low");testCount++;
 assertClose(hi.G_optimal_with_provenance,3.025,"G high");testCount++;
 const thresholdT=(2.1-0.2)/5,thresholdInvest=((2*2.4-2.1)-0.2)/5;
 assertClose(thresholdT,0.38,"T action");testCount++;
 assertClose(thresholdInvest,0.5,"G/E ranking");testCount++;
 // For every candidate joint success probability in its sharp admissible interval,
 // every possible t3 action policy has the stated piecewise-affine value.
 for(let i=0;i<=65;i++){
   const p=0.1+i/100, m=0.2+5*p,s=2.1;
   let g1=(s+Math.max(s,m))/2;
   let g2=Math.max((s+s)/2,(s+m)/2);
   assertClose(g1,g2,"policy maximum at "+p);testCount++;
   if(g1+1e-12<2.1)throw Error("old G action lost");testCount++;
 }
 return {provenance_eligible_history_share:0.5,source_signature:["F","T"],worker_slots:1,programs:{R:1.5,P:2,E:2.4},G_supported_S:2.1,G_M_interval:[0.7,3.95],joint_interval:[0.1,0.75],threshold_use_M_T:thresholdT,threshold_G_outperforms_E:thresholdInvest,low:lo,high:hi,assertions:testCount};
}
const result=runChecks();
if(typeof module!=="undefined"){module.exports={makeCase,evaluate,runChecks};if(require.main===module)console.log(JSON.stringify(result,null,2));}
