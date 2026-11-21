/* Synthetic, CPU-only integer model; node qualification_gate_value.js */
const model = function model(){
 let assertions=0;const test=(x,m)=>{assertions++;if(!x)throw Error(m)};
 let samples=[];
 for(let j=0;j<=1000;j++){
   // Reliability r=j/1000; all values in exact units of 1/16000.
   let xlow=28000+130*j,xhigh=28000+150*j,g=28000+140*j,e=160000;
   let info=Math.max(xhigh,e)-Math.max(g,e); // value of audit in units 1/32000
   let piece=(j<=880?0:(35*j<=33000?150*j-132000:10*j));
   test(info===piece,"piecewise EVSI");
   test(xlow<=g&&g<=xhigh,"source/grounding ordering");
   test(Math.max(xlow,g,e)+Math.max(xhigh,g,e)-2*Math.max(g,e)===info,"pre/post optimization");
   for(let k=0;k<=16;k++){
     // t=k/256, conditional accepted-service reliability r.
     let X=448000+2080*j+20*j*k,G=448000+2240*j;
     test(X-G===20*j*(k-8),"X minus G common qualified service reliability");
   }
   if([0,800,880,900,943,1000].includes(j))samples.push({r:`${j}/1000`,xlow_over_16000:xlow,xhigh_over_16000:xhigh,g_over_16000:g,e_over_16000:e,EVSI_over_32000:info});
 }
 test(28000+150*880===160000,"embodiment crossover source");
 test(28000+140*33000/35===160000,"embodiment crossover grounding");
 test(448000+2080*900+20*900*16===2608000,"at r .9 t max source 163/16");
 test(103<168,"heterogeneous qualification counterworld X 103/16 < G 168/16");
 test((163-8)===155&&(163+8)===171,"5pp TV drift around X r=.9");
 return {title:"Qualified-production calibration gate for higher-order source information",synthetic_only:true,source_error_triple_parameter:"t in [0,1/16]",source_accuracy:"13/16+2t",grounding_accuracy:"7/8",service_margin_over_retained_R:10,retained_R:2,X_G_complete_cost:"1/4",E_net:10,qualification_reliability_thresholds:["22/25","33/35"],audit_value_formula:["0","(75r-66)/16","5r/16"],counterworld:{same_signal_t:"1/16",X_correct_service_reliability:"1/2",G_correct_service_reliability:"1",X_net:"103/16",G_net:"21/2"},transport_example:{r:"9/10",t:"1/16",shadow_X:"163/16",assumed_total_variation:"1/20",field_value_bounds:["155/16","171/16"]},sample_exact_grid:samples,exact_integer_assertions:assertions,archive_downloaded:false,robot_training:false,paid_customer_receipts:false};
};
if(typeof module!=='undefined'){if(require.main===module)process.stdout.write(JSON.stringify(model(),null,2)+'\n');module.exports=model;}
