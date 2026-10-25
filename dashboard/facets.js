/* Exact recorded-field filters. No substring inference or cross-record joins. */
(function (root) {
 'use strict';
 const definitions = [
  {id:'geography',label:'Recorded geography',fields:['geography']},
  {id:'system',label:'Recorded system / configuration',fields:['system_id','system','systems']},
  {id:'embodiment',label:'Recorded embodiment',fields:['embodiment']},
  {id:'harness',label:'Recorded harness',fields:['harness','declared_harness']},
  {id:'openness',label:'Openness artifact layer',fields:['layer'],opennessOnly:true},
  {id:'license',label:'Artifact license label',fields:['license'],opennessOnly:true},
 ];
 function values(record,definition,key='') {
  if(definition.opennessOnly&&record.schema_version!=='openness-1.0')return [];
  const found=[];
  for(const field of definition.fields){
   const raw=record[field];
   for(const item of Array.isArray(raw)?raw:[raw]){
    if(typeof item==='string'&&item.trim())found.push(item);
   }
  }
  return [...new Set(found)];
 }
 function matches(record,selections,key=''){
  return definitions.every(d=>{
   const choice=selections[d.id]||'';if(!choice)return true;
   const recorded=values(record,d,key);
   return choice==='missing'?recorded.length===0:choice.startsWith('v:')&&recorded.includes(choice.slice(2));
  });
 }
 function options(records,definition){
  const counts=new Map();let missing=0;
  for(const r of records){
   const recorded=values(r.value,definition,r.key);
   if(!recorded.length)missing++;
   for(const value of recorded)counts.set(value,(counts.get(value)||0)+1);
  }
  return {missing,values:[...counts].sort((a,b)=>a[0].localeCompare(b[0]))};
 }
 const api={definitions,values,matches,options};
 if(typeof module!=='undefined'&&module.exports)module.exports=api;
 else root.EvidenceFacets=api;
})(typeof window==='undefined'?globalThis:window);
