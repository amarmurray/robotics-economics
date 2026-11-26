// Reproduce the four-date matched comparison using both continuation implementations.
const {cohortStudy}=require("./cohort_embodied.js");
const compact=x=>x.results.flatMap(c=>c.results.map(y=>({cap:c.parameters.cap,rule:y.rule,status:y.status,wealth:y.wealth,profiles:y.profiles,states:y.states,successors:y.dated?.map(d=>d.successor)})));
const opts={fourDatesOnly:true,profileBudget:12000000};
const baseline=compact(cohortStudy(opts)),projected=compact(cohortStudy({...opts,terminalProjection:true}));
for(let i=0;i<baseline.length;i++){let a=baseline[i],b=projected[i];if(a.status!=="solved"||b.status!=="solved"||JSON.stringify(a.wealth)!==JSON.stringify(b.wealth)||JSON.stringify(a.successors)!==JSON.stringify(b.successors))throw Error("projection mismatch");}
console.log(JSON.stringify({synthetic:true,profile_budget:opts.profileBudget,baseline,projected},null,2));
