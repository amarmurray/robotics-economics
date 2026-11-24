function run(){
 let checks=0,cases=0;const ok=x=>{if(!x)throw Error("check "+checks);checks++};
 const N=108,gross=340*60,net=310*60,nom=159,H=141,A=3000;
 const rates={gross_per_hour:3600*N/gross,net_per_hour:3600*N/net,nominal_per_hour:3600/nom,human_break_adjusted_per_hour:A/H,gross_seconds_per_motor:gross/N,net_seconds_per_motor:net/N,excluded_seconds_per_motor:(gross-net)/N,nominal_overhead_gross:gross/N-nom,threshold_q_seconds:A*gross/(3600*N)-H,per_operation_success:322/324,recorded_data_minutes:[8,20,4,9]};
 ok(gross-net===1800);ok(rates.gross_per_hour<rates.net_per_hour&&rates.net_per_hour<rates.human_break_adjusted_per_hour&&rates.human_break_adjusted_per_hour<rates.nominal_per_hour);ok(rates.threshold_q_seconds>0);
 // compare exact rational capacities by cross multiplication. Wall horizon T, worker budget A, robot clock r, human h, human robot-support l, QC q, demand D. 
 const less=(a,b)=>a[0]*b[1]<b[0]*a[1];const min=(...xs)=>xs.reduce((a,b)=>less(a,b)?a:b);const V=(T,A,r,l,q,D)=>min([T,r],[A,l+q],[D,1]);
 for(let T=1;T<=8;T++)for(let A=1;A<=T;A++)for(let r=1;r<=6;r++)for(let h=1;h<=6;h++)for(let l=1;l<=6;l++)for(let q=0;q<=6;q++)for(let D=1;D<=5;D++){
   const M=min([A,h+q],[D,1]),R=V(T,A,r,l,q,D);
   const strict=(T*(h+q)>A*r&&l<h&&D*(h+q)>A);
   ok(less(M,R)===strict);cases++;
 }
 const qExamples=[0,10,20,40].map(q=>({q,manual:A/(H+q),robot:Math.min(3600*N/gross,A/(60+q))}));
 ok(qExamples[0].robot<qExamples[0].manual&&qExamples[2].robot>qExamples[2].manual);
 // two improvements separately insufficient; joint crosses complementary bottlenecks
 const vals=[V(60,60,15,10,5,10),V(60,60,10,10,5,10),V(60,60,15,5,5,10),V(60,60,10,5,5,10)].map(x=>x[0]/x[1]);ok(vals.join(",")==="4,4,4,6");
 return {checks,cases,rates,qExamples,synthetic_complementarity:vals,field_costs_and_paid_service_identified:false};
}
if(typeof module!=='undefined')module.exports=run;
if(typeof require!=='undefined'&&typeof module!=='undefined'&&require.main===module)console.log(JSON.stringify(run(),null,2));
