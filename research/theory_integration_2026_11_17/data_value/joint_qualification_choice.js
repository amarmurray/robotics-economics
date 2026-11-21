/** Reproducible exact-integer conditional counterworlds. Node 18+; no dependencies. **/
const run = function run(){
  let assertions=0;
  const assert=(test,msg)=>{assertions++;if(!test)throw new Error(msg);};
  const p=[8,10,10,12]; // 20ths; A and B margins identical in each arm
  const labels=["R","S","G","SG"];
  const lower=p.map(x=>Math.max(0,2*x-20)), upper=p.slice();
  const gross=(i,q,k=8)=>4*p[i]+k*q; // scaled by 20; 2pA+2pB+k P(A&B)
  const netCosts=[0,10,10,20]; // 20ths
  const policyMenu=q=>{
    const out={};
    for(let i=0;i<4;i++){
      out[labels[i]]=gross(i,q[i])-netCosts[i];
      out[labels[i]+"+E"]=Math.max(gross(i,q[i]),100)-netCosts[i]-20;
    }
    return out;
  };
  const winner=menu=>Object.keys(menu).reduce((best,key)=>menu[key]>menu[best]?key:best);
  let n=0, mn=Infinity, mx=-Infinity;
  for(let q0=lower[0];q0<=upper[0];q0++)
   for(let q1=lower[1];q1<=upper[1];q1++)
    for(let q2=lower[2];q2<=upper[2];q2++)
     for(let q3=lower[3];q3<=upper[3];q3++){
       n++;const z=q3-q1-q2+q0;
       mn=Math.min(mn,z);mx=Math.max(mx,z);
       assert(q3>=4 && q3<=12,"Fréchet joint SG range");
     }
  assert(n===9801 && mn===-16 && mx===20,"sharp Frechet cross interaction");
  const worlds={};
  for(const [name,q3,expected,delta] of [["complementary_lineage",10,"SG",32],["substitutive_lineage",4,"R+E",-16]]){
    const q=[4,5,5,q3];
    for(let i=0;i<4;i++)assert(q[i]>=lower[i]&&q[i]<=upper[i],"joint law feasible");
    const menu=policyMenu(q), w=winner(menu);
    assert(w===expected,`winner ${name}: ${w}`);
    const cross=gross(3,q3)-gross(1,q[1])-gross(2,q[2])+gross(0,q[0]);
    assert(cross===delta,`cross ${name}`);
    const oneSlotCross=gross(3,q3,-2)-gross(1,q[1],-2)-gross(2,q[2],-2)+gross(0,q[0],-2);
    assert(oneSlotCross===-delta/4,"substitute-demand reversal");
    worlds[name]={qAB_twentieths:q,gross_twentieths:labels.map((_,i)=>gross(i,q[i])),
      net_program_twentieths:menu,winner:w,winning_net_twentieths:menu[w],interaction_twentieths:cross,
      one_slot_interaction_twentieths:oneSlotCross};
  }
  const switchByQ11=[];
  for(let q11=4;q11<=12;q11++){
    const w=winner(policyMenu([4,5,5,q11]));
    assert(w===(q11>=7?"SG":"R+E"),`threshold policy at q=${q11}`);
    switchByQ11.push([q11,w]);
  }
  assert(gross(3,10)-gross(3,4)===48,"gross joint leverage");
  return {model:"hypothetical closed learner/whole network source-grounding-embodiment",
    scale:"all rewards and probabilities in 20ths; no real customer currency",
    independent_joint_marginal_bounds_twentieths:lower.map((x,i)=>[x,upper[i]]),
    exact_feasible_integer_grid_worlds:n,sharp_delta_joint_twentieths:[mn,mx],
    sharp_delta_gross_twentieths:[8*mn,8*mx],cross_marginal_A_B_twentieths:0,
    worlds,threshold_joint_q11:"13/40 (strictly above: SG beats E)",switchByQ11,
    scoped_assertions:assertions,physical_data_or_paid_receipts:false};
};
if(typeof module!=='undefined' && require.main===module)console.log(JSON.stringify(run(),null,2));
module.exports={run};
