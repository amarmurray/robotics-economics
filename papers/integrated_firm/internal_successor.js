// Run node internal_successor.js [case_name]; default runs every case.
const {windowStudy}=require('./service_window.js');
const expected=require('./internal_successor_results.json');
function reproduce(name){const runs=expected.cases.filter(c=>!name||c[0]===name);if(!runs.length)throw Error('unknown case');return runs.map(([name,opts,want])=>{const r=windowStudy(opts);if(r.results.some(x=>x.status!=='solved'))throw Error('open '+name);const got=r.results.map(x=>[...x.wealth,x.dated.at(-1).jobs,...['develop','licenses','contract_develop'].map(k=>x.dated.reduce((s,d)=>s+d[k],0)),x.profiles]);if(JSON.stringify(got)!==JSON.stringify(want))throw Error('mismatch '+name);return {name,opts,...r};});}
module.exports={reproduce};if(require.main===module)console.log(JSON.stringify(reproduce(process.argv[2]),null,2));
