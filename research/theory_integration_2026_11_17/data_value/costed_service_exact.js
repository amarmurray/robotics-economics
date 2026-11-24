function run(){
let checks=0,cases=0;const ok=x=>{if(!x)throw Error("check "+checks);checks++};
function ext(v,u,H,high){let slots=v.flatMap((x,i)=>Array(u[i]).fill(x)).sort((a,b)=>high?b-a:a-b);if(H<0||H>slots.length)throw Error("H");return slots.slice(0,H).reduce((a,b)=>a+b,0)}
function alloc(u,H,i=0,p=[]){if(i===u.length)return H===0?[p]:[];let out=[];for(let x=0;x<=Math.min(H,u[i]);x++)out.push(...alloc(u,H-x,i+1,[...p,x]));return out}
function value(v,r){return r.reduce((s,x,i)=>s+x*v[i],0)}
for(let a=0;a<=3;a++)for(let b=0;b<=3;b++)for(let c=0;c<=2;c++)for(let x=0;x<=3;x++)for(let y=0;y<=3;y++)for(let z=0;z<=3;z++){
let u=[a,b,c],v=[x,y,z],U=a+b+c;for(let H=0;H<=U;H++){let A=alloc(u,H).map(r=>value(v,r));ok(ext(v,u,H,false)===Math.min(...A));ok(ext(v,u,H,true)===Math.max(...A));cases++}
}
let v=[4,0],u=[3,3],P=2,G=4,C=3;
let independent=[ext(v,u,G,false)-ext(v,u,P,true)-C,ext(v,u,G,true)-ext(v,u,P,false)-C];
let nested=[ext(v,u,G-P,false)-C,ext(v,u,G-P,true)-C];
let A=alloc(u,P),B=alloc(u,G),diffs=[],nests=[];for(let p of A)for(let g of B){let d=value(v,g)-value(v,p)-C;diffs.push(d);if(g.every((x,i)=>x>=p[i]))nests.push(d)}
ok(independent[0]===Math.min(...diffs)&&independent[1]===Math.max(...diffs));ok(nested[0]===Math.min(...nests)&&nested[1]===Math.max(...nests));
let china={manual_lifecycle_cny:12633000,robot_lifecycle_cny:5705000,claimed_net:6928000};china.avoidance_break_even=china.robot_lifecycle_cny/china.manual_lifecycle_cny;china.net_40pct=china.manual_lifecycle_cny*.4-china.robot_lifecycle_cny;china.net_50pct=china.manual_lifecycle_cny*.5-china.robot_lifecycle_cny;china.geometric_labor=1102000*((1.03**10-1)/.03);china.trip_total=[10500,12565,13112,13658,14204,14751].reduce((a,b)=>a+b,0);
ok(china.manual_lifecycle_cny-china.robot_lifecycle_cny===china.claimed_net);ok(china.net_40pct<0&&china.net_50pct>0);ok(Math.abs(china.geometric_labor-china.manual_lifecycle_cny)<1000);
let poster={manual_tasks_3days:89+42+114,manual_cost:527684,robot_cost:1893965,manual_hours:1233.78,robot_hours:125.50};poster.delta_cost=poster.robot_cost-poster.manual_cost;poster.hours_saved=poster.manual_hours-poster.robot_hours;poster.icer=poster.delta_cost/poster.hours_saved;
ok(poster.manual_tasks_3days===245);ok(poster.delta_cost===1366281);ok(Math.round(poster.icer)===1233);
let abstract={program_cost_reported:1650000,hours_saved_reported:553,icer_reported:2984};abstract.ratio_of_rounded_inputs=abstract.program_cost_reported/abstract.hours_saved_reported;ok(abstract.icer_reported>poster.icer);
return {checks,cases,synthetic:{independent,nested,embodiment_increment:2},china,poster,abstract,source_costs_are_model_not_observed:true,field_data_program_contrast_identified:false,full_repository_ci:false};
}
console.log(JSON.stringify(run(),null,2));
