"use strict";
// Synthetic policy-uniform influence and admission audit. No robotics field calibration.
const EPS=1e-11;
let tests=0;
function check(q,m){tests++;if(!q)throw Error(m);}
function close(a,b,m){check(Math.abs(a-b)<EPS,m+": "+a+" versus "+b);}
function step(C,e,b){return e.map((_,i)=>b[i]+C[i].reduce((s,c,j)=>s+c*e[j],0));}
function network(shock,coefficient){
  const z=[0,0,0],zero=[[0,0,0],[0,0,0],[0,0,0]];
  const e1=step(zero,z,[0,shock,0]);
  const C=[[0,0,0],[0,0,0],[0,coefficient,0]];
  const e2=step(C,e1,[0,0,0]);
  return {controller_e1:e1[1],customer_B_e2:e2[2],weighted_B_loss:3*e2[2],per_B_loss:10*e2[2]};
}
function policy(p){
  const omitted=network(p.shock,p.link);
  const gain=.7*p.A_gain-.3*p.local_B_upper-p.own_residual-p.cost-omitted.weighted_B_loss;
  return {omitted,gain,full_lower:7+gain,margin_over_specialist:7+gain-7.08};
}
function tail(beta,d,alpha,r,T){
  let s=0;for(let k=r+1;k<=T;k++)s+=beta*Math.pow(d*alpha,k);return s;
}
function admissionTrace(seq,cap=1){
  let busy=0,accepted=0,rejected=0;
  for(const op of seq){
    if(op===1){if(busy<cap){busy++;accepted++;}else rejected++;}
    if(op===2)busy=Math.max(0,busy-1);
    check(busy>=0&&busy<=cap,"semaphore invariant");
  }
  return {accepted,rejected,final_busy:busy};
}
function run(){
  const open=policy({shock:.05,link:.4,A_gain:.5,local_B_upper:.6,own_residual:.02,cost:.03});
  const serial=policy({shock:.015,link:.25,A_gain:.44,local_B_upper:.45,own_residual:.02,cost:.045});
  close(open.omitted.customer_B_e2,.02,"open e_B");
  close(open.omitted.weighted_B_loss,.06,"open omission");
  close(open.gain,.06,"open lower");
  close(serial.omitted.customer_B_e2,.00375,"serial e_B");
  close(serial.omitted.weighted_B_loss,.01125,"serial omission");
  close(serial.gain,.09675,"serial lower");
  close(serial.margin_over_specialist,.01675,"serial specialist");
  check(open.margin_over_specialist<0,"open not specialist certified");
  check(serial.margin_over_specialist>0,"serial beats specialist only with safety assumption");
  close(tail(.05,2,.2,1,4),.01248,"finite path tail");
  close(.05*Math.pow(.4,2)/(1-.4),1/75,"infinite tail");
  for(let i=0;i<=20;i++){
    for(let j=0;j<=20;j++){
      const b=i/400,c=j/50;
      const e=network(b,c);
      close(e.customer_B_e2,b*c,"path product");
      close(e.weighted_B_loss,3*b*c,"linear reward");
      check(e.customer_B_e2>=0&&e.customer_B_e2<=1,"probability upper");
    }
  }
  for(let code=0;code<729;code++){
    let x=code,seq=[];for(let j=0;j<6;j++){seq.push(x%3);x=Math.floor(x/3);}
    admissionTrace(seq,1);
  }
  return {date:"2026-11-18",synthetic:true,units:"normalized contribution, not measured dollars",
   network_open:open,network_serial_admission:serial,specialist_upper:7.08,old_controller:7,
   path_tail_4_horizon:tail(.05,2,.2,1,4),path_tail_infinite_bound:1/75,
   semaphore_enumerated_sequences:729,checks:tests,
   caveat:"Semaphores establish only a software invariant if all recovery consumers honor admission and a separately verified fail-safe stop exists; physical support unverified."};
}
if(typeof module!=="undefined"&&module.exports){module.exports={run,network,policy,tail,admissionTrace};if(require.main===module)console.log(JSON.stringify(run(),null,2));}
