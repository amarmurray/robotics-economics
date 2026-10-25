/* Input preservation only. All bounds and numerical calculations live in Python. */
(function(root){
 'use strict';
 const channels=['digital_efficiency','coordination','digital_cost_usd'];
 function annualPaths(baseYear,fields){
  const paths={schema_version:'digital-annual-paths/0.1',base_year:baseYear,epistemic_status:'synthetic_assumption'};
  for(const key of channels){
   const text=(fields[key]||'').trim();if(!text)continue;
   const parts=text.split(',').map(v=>v.trim());
   if(parts.some(v=>!v||!Number.isFinite(Number(v))))throw Error(`${key}: enter finite annual numbers separated by commas.`);
   paths[key]=parts.map(Number);
  }
  return channels.some(key=>Object.hasOwn(paths,key))?paths:null;
 }
 function savedInput(saved,presets){
  if(!saved||typeof saved!=='object'||Array.isArray(saved))throw Error('Expected a saved scenario object.');
  const preset=saved.preset||'reference';
  if(!Object.hasOwn(presets,preset))throw Error('Unknown saved scenario preset.');
  const overrides=saved.parameters??saved.overrides??{};
  if(!overrides||typeof overrides!=='object'||Array.isArray(overrides))throw Error('Scenario parameters must be an object.');
  if(saved.resolved_digital_paths&&!Object.hasOwn(saved,'digital_paths'))throw Error('Saved annual scenario is missing its original digital_paths input.');
  return {preset,overrides,digital_paths:saved.digital_paths??null};
 }
 const api={channels,annualPaths,savedInput};
 if(typeof module!=='undefined'&&module.exports)module.exports=api;
 else root.ScenarioIO=api;
})(typeof globalThis!=='undefined'?globalThis:this);
