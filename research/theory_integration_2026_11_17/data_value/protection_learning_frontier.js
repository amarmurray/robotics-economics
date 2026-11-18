"use strict";
function run() {
  let assertions=0;
  function eq(a,b,name){assertions++;if(Math.abs(a-b)>1e-9)throw Error(name+" "+a+" ≠ "+b)}
  function topK(arr,k){return arr.slice().sort((a,b)=>b-a).slice(0,k).reduce((a,b)=>a+b,0)}
  const b=[1.2,.6,.2],r=[.35,.05,.02],cost=[.2,.1,.05],total=topK(b,1);
  const rows=[];
  function W(mask,k){return topK(b,k)-topK(b.filter((_,i)=>!(mask>>i&1)),k)}
  for(let m=0;m<8;m++){
    let a=2.4,c=.4,left=[];
    for(let j=0;j<3;j++){if(m>>j&1){a-=2*r[j];c+=cost[j]}else left.push(b[j]);}
    const D=topK(left,1),lower=a-c-D;
    rows.push({protected_mask:m,remaining_b:left,max_loss:D,accepted_A_increment:+a.toFixed(10),incremental_cost:+c.toFixed(10),certified_lower:+lower.toFixed(10)});
    eq(W(m,1),total-D,"loss reduction identity");
    for(let k=0;k<=3;k++){eq(W(m,k),topK(b,k)-topK(left,k),"all k loss identity")}
  }
  eq(rows[0].certified_lower,.8,"no-protection lower");
  eq(rows[1].certified_lower,.5,"B1 protection");
  eq(rows[7].certified_lower,.81,"all protection");
  eq(W(1,1),.6,"B1 loss reduction");
  eq(W(2,1),0,"B2 lone cut");
  eq(W(3,1),1,"B1 B2 complement");
  for(let k=0;k<=3;k++)for(let A=0;A<8;A++)for(let B=0;B<8;B++){
    if((A&B)!==A)continue;
    for(let j=0;j<3;j++){
      if(B>>j&1)continue;
      const da=W(A|1<<j,k)-W(A,k),db=W(B|1<<j,k)-W(B,k);
      assertions++;if(da>db+1e-9)throw Error("violated supermodularity at "+[k,A,B,j,da,db]);
    }
  }
  const shared=2.4, pinCost=.6, specialistUpper=.9;
  const rPin=.25,K=2,Mdelta=.2;
  const pinLower=shared-(K*rPin+Mdelta)-pinCost;
  eq(pinLower,1.1,"pin with transfer bound");
  eq(shared-pinCost,1.8,"ideal pin");
  eq(shared-(K*rPin+.4)-pinCost,specialistUpper,"threshold");
  eq(1.7-.6-.6,.5,"protected account");
  const indicator=u=>u>=1-1e-12?2.4:0;
  eq(indicator(1)-indicator(.99),2.4,"threshold discontinuity");
  const max=Math.max(...rows.map(x=>x.certified_lower));
  eq(max,.81,"synthetic max");
  return {date:"2026-11-18",study:"protection-learning frontier: conditional exact checks",assertions,baseline:7,shared_no_cut:rows[0].certified_lower,protect_B1:rows[1].certified_lower,max_protection_subset:rows.filter(x=>x.certified_lower===max).map(x=>x.protected_mask),table:rows,resource_TV_bridge:{r:rPin,K,Mdelta,pinned_lower:pinLower,specialist_upper:specialistUpper,strict_advantage_assumed:true},discrete_qualification_cliff:{resource_before:1,resource_after:.99,accepted_A_drop:2.4},limitations:["synthetic normalized service margins and policy-specific A/cost effects","verified policy-uniform loss cut not observed","full accepted-service TV/capacity response not estimated","no physical certification, empirical robot intervention or independent scientific review"]};
}
if (typeof require !== "undefined" && require.main === module) console.log(JSON.stringify(run(),null,2));
if (typeof module !== "undefined") module.exports={run};
