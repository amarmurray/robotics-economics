function run(){
 let checks=0,cases=0;const ok=x=>{if(!x)throw Error("check "+checks);checks++};
 const vals=[61,85,104,111,114,118],sizes=[4,8,16,32,64,96],init=95;
 const observed=vals.map((v,i)=>({robots:sizes[i],successes:v,trials:120,delta_vs_init:v-init}));
 const minutes=413, scheduled=96*minutes, active=65*minutes, inactive=scheduled-active,faultMinutes=498;
 ok(active+inactive===scheduled);ok(faultMinutes<inactive);ok(vals[0]<init&&vals[1]<init&&vals[2]>init);ok(vals[5]-init===23);ok(vals[5]-vals[2]===14);
 const v=(a,l)=>Math.min(a,l);
 for(let a=0;a<=12;a++)for(let l=0;l<=12;l++)for(let f=0;f<=6;f++)for(let h=0;h<=6;h++){
  cases++;const repair=v(a+f,l)-v(a,l),cross=v(a+f,l+h)-v(a,l+h)-repair,overlap=Math.max(0,Math.min(a+f,l+h)-Math.max(a,l));
  ok(repair===Math.min(f,Math.max(0,l-a)));ok(cross===overlap);ok(cross>=0&&cross<=Math.min(f,h));
 }
 let maskCases=0;
 for(let n=0;n<=7;n++)for(let f=0;f<(1<<n);f++)for(let o=0;o<(1<<n);o++){
   const count=x=>{let c=0;for(;x;x>>=1)c+=x&1;return c};
   const I=f|o,F=count(f),O=count(o),U=count(I),released=count(f&~o);
   ok(released===U-O);ok(released<=F);ok(released>=0);maskCases++;
 }
 return {checks,cases,maskCases,observed,source_clock:{window_minutes:minutes,scheduled_robot_hours:scheduled/60,approx_active_robot_hours:active/60,approx_inactive_robot_hours:inactive/60,active_fraction:65/96,fault_upper_robot_hours:faultMinutes/60,fault_upper_fraction_of_inactive:faultMinutes/inactive,max_fault_only_active_fraction:(active+faultMinutes)/scheduled},synthetic:{baseline:v(4,4),repair_only:v(6,4),label_only:v(4,6),combined:v(6,6),cross:2}};
}
if(typeof module!=='undefined')module.exports=run;
