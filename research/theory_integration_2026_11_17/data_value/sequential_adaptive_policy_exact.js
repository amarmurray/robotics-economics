// Synthetic nonanticipative G-specific t3 choice and t4 buyer/recovery response.
// Not a field calibration. Node 18+ or plain ECMAScript.
'use strict';
function must(x,msg){ if(!x) throw Error(msg); checks++; }
let checks=0;
const arr=[];
for(const u of [0,1]) for(const v of [0,1]){
 const S={a3:1,d4:Number(Boolean(u||v)),l4:1-u};
 const H={a3:0,d4:u,l4:u};
 const L={a3:0,d4:u,l4:1-u};
 arr.push({u,v,S,H,L});
}
function n(rows,select){return rows.reduce((a,r)=>a+select(r),0);}
function val(rows,k){return 0.5+(k==='S'?0.5:0)+4*n(rows,r=>r[k].d4*r[k].l4)/rows.length;}
for(const row of arr){
 must(row.S.d4>=row.H.d4,'S buyer demand monotone relative to M');
 must(row.S.a3===1&&row.H.a3===0&&row.L.a3===0,'t3 single worker');
 must([row.S,row.H,row.L].every(x=>1+x.d4*x.l4<=2),'C two-unit lifetime budget');
}
must(n(arr,r=>r.S.d4*r.S.l4)===1,'observed S joint 1/4');
must(n(arr,r=>r.H.d4*r.H.l4)===2,'high M joint 1/2');
must(n(arr,r=>r.L.d4*r.L.l4)===0,'low M joint zero');
for(const f of ['d4','l4']){
 must(n(arr,r=>r.H[f])===2,'high M marginal '+f);
 must(n(arr,r=>r.L[f])===2,'low M marginal '+f);
}
must(val(arr,'S')===2,'safe S net 2');
must(val(arr,'H')===2.5,'high M net 5/2');
must(val(arr,'L')===0.5,'low M net 1/2');
const E=2.2,P=2.1,R=1.9;
must(E>P && P>val(arr,'S') && val(arr,'S')>R,'fixed program ordering');
const gainHigh=val(arr,'H')-E,lossLow=E-val(arr,'L');
const fraction=gainHigh/(gainHigh+lossLow);
const regret=Math.max(gainHigh*(1-fraction),lossLow*fraction);
must(Math.abs(fraction-3/20)<1e-12,'minimax share 3/20');
must(Math.abs(regret-51/200)<1e-12,'minimax regret 51/200');
for(let k=0;k<=1000;k++){
 const x=k/1000, worst=Math.max(gainHigh*(1-x),lossLow*x);
 must(worst+1e-10>=regret,'minimax global on grid');
}
const result={
 kind:'stipulated synthetic t2-G service, t3 one-worker A service versus maintenance, t4 original C buyer and worker availability',
 t2_C_paid:'1',G_program_cost:'1/2',t3_A_paid_if_S:'1/2',t4_C_paid:'4',
 buyer_response:'D4(S)=U OR V, D4(M)=U, so accepted t3 A service weakly increases original t4 C demand unitwise',
 worker_response:'L4(S)=1-U; L4(M)=U in high world or 1-U in low world',
 action_information:'U and V unobserved at t3; M not in historical action support',
 obs_S_joint:'1/4',M_D_marginal:'1/2',M_L_marginal:'1/2',
 M_joint_low:'0',M_joint_high:'1/2',
 programs:{R:'19/10',P:'21/10',E:'11/5',G_S:'2',G_M_low:'1/2',G_M_high:'5/2'},
 decision:{minimax_G_M_fraction:'3/20',minimax_E_fraction:'17/20',minimax_regret:'51/200'},
 assertions:checks,
 caveat:'No field customer records, G assignment or lawful M intervention; no established novelty.'
};
console.log(JSON.stringify(result,null,2));
