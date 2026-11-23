"use strict";
const run = function run(){
 let checks=0;const ck=(b,m)=>{checks++;if(!b)throw Error(m)};
 // 64 original clusters; all quantities stored in sixty-fourths.
 const laws=[];
 for(let m=8;m<=24;m++)for(let x=Math.max(0,m-16);x<=Math.min(m,16);x++){
  const atoms=[{h:"F",s:1,n:x},{h:"F",s:0,n:m-x},{h:"K",s:1,n:16-x},{h:"K",s:0,n:16-m+x},{h:"none",s:0,n:32}];
  // K generates report after first accepted A; G may consume the final worker slot.
  function value(qF,qK,free=false){
   let total=0;
   for(const a of atoms){const q=a.h==="F"?qF:a.h==="K"?qK:0;
    const no=3+2-(free?0:1),yes=3+8*a.s-(free?0:1);
    total+=a.n*((1-q)*no+q*yes);
   }
   return total;
  }
  ck(atoms.every(a=>a.n>=0)&&atoms.reduce((s,a)=>s+a.n,0)===64,"law");
  const vals=[value(0,0),value(1,0),value(0,1),value(1,1)];
  ck(vals[0]===256&&vals[3]===320,"same aggregate");
  ck(vals[1]===256+8*x-2*m,"F occupancy contrast");
  ck(vals[2]===320+2*m-8*x,"K occupancy contrast");
  ck(vals[1]+vals[2]===576,"common-law contrast sum");
  ck(value(1,1,true)===384&&value(1,0,true)===vals[1]+64,"free P");
  laws.push({m,x,values:vals,oracle:Math.max(...vals)});
 }
 const target=laws.map(w=>w.values[1]);
 ck(Math.min(...target)===224&&Math.max(...target)===352,"sharp target");
 const audit=laws.filter(w=>w.x>=15&&w.m<=18);
 ck(Math.min(...audit.map(w=>w.values[1]))===340,"joint audit");
 const perfect=laws.filter(w=>w.x===w.m);
 ck(perfect.find(w=>w.m===8).values[1]===304&&perfect.find(w=>w.m===16).values[1]===352,"conditional rate alone");
 const end=laws.filter(w=>w.m===16&&(w.x===0||w.x===16));
 ck(end.length===2&&end.every(w=>w.oracle===352),"oracle endpoints");
 let robust=-Infinity;
 for(let f=0;f<=16;f++)for(let k=0;k<=16;k++){
   const worst=Math.min(...end.map(w=>256*16+f*(w.values[1]-256)+k*(w.values[2]-256)));
   ck(worst<=320*16,"no oracle policy");
   robust=Math.max(worst,robust);
 }
 ck(robust===320*16,"robust endpoint");
 ck(3*4+2*4+9-8===21,"independent E");
 ck(3*4+Math.max(8,9)-8===13,"shared E committed");
 ck(Math.max(20,13)===20,"optional E shared");
 return {synthetic:true,checks,laws_count:laws.length,units:"1/64",target_bounds:[224,352],aggregate_GK:320,retained_R:320,robust_K_family:320,oracle_endpoint:352,joint_audit_lower:340,assumed_independent_E:336,free_P_all_align:384,shared_E_committed:208,shared_E_optional:320,perfect_report_examples:[{m:8,x:8,value:304},{m:16,x:16,value:352}],laws};
};
if(typeof module!=="undefined"&&require.main===module) console.log(JSON.stringify(run(),null,2));
if(typeof module!=="undefined")module.exports=run;
