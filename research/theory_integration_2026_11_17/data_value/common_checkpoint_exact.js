function run(){
 let checks=0; const ok=x=>{if(!x)throw Error("assertion "+checks);checks++};
 // observed paired technical results: task, round, HITL count, curated segments, HITL vs mixed tasks/hour, success percent
 const rows=[["refrigerator",1,201,100,14,19,35,45],["refrigerator",2,242,117,33,42,60,80],["microplate",1,168,173,16,18,40,45],["microplate",2,134,116,25,42,60,90],["test tube",1,352,142,19,20,45,55],["test tube",2,300,141,28,37,70,95],["stirrer",1,230,334,83,112,70,90]];
 const derived=rows.map(([task,round,h,c,a,b,p,q])=>{ok(h>0&&c>0&&b>a&&q>p);return {task,round,recovery_count:h,curated_count:c,throughput_difference:b-a,success_pp:q-p};});
 // C and H fixed programs; first states differ. H at the C anchor is observed, H at its own state is unsupported.
 // stage-one rewards are zero; stage-two terminal economic contribution is in integer [L,U]; common C result v.
 let cases=0;
 for(let L=0;L<=4;L++)for(let U=L;U<=7;U++)for(let v=0;v<=7;v++)for(let kC=0;kC<=3;kC++)for(let kH=0;kH<=3;kH++){
   const diffs=[];for(let h=L;h<=U;h++){const C=v-kC,H=h-kH;diffs.push(C-H);ok(Math.max(C,H)>=H)}
   ok(Math.min(...diffs)===v-U-kC+kH);ok(Math.max(...diffs)===v-L-kC+kH);cases++;
 }
 const worlds=[0,4].map(h=>({H_terminal:h,C_terminal:2,C_minus_H:2-h}));
 ok(worlds[0].C_minus_H>0&&worlds[1].C_minus_H<0);
 return {checks,cases,observed_technical:derived,synthetic_worlds:worlds,field_economic_effect_identified:false,full_repository_ci:false};
}
if(typeof module!=="undefined")module.exports=run;
if(typeof require!=="undefined"&&typeof module!=="undefined"&&require.main===module)console.log(JSON.stringify(run(),null,2));
