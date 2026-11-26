// Exact block-restricted extension of the accepted service_window.js.
// Run node staggered_window.js [variant]; full replay by default.
const fs=require('fs'),path=require('path'),crypto=require('crypto');
const expected=require('./staggered_window_results.json');
const edits=[
  [
    "developBase=2}",
    "developBase=2,entry=2,concurrent=false,kitPrice=500,early=[1,1,1]}"
  ],
  [
    "if(!Number.isInteger(N)||N<1||10000<12*N+3*620||!quotient)",
    "if(![N,...early].every(x=>Number.isInteger(x)&&x>=1)||early.length!==3||10000<12*(N+early.reduce((a,b)=>a+b,0))+3*620||!quotient)"
  ],
  [
    "parts=[1,500]",
    "parts=[1,kitPrice]"
  ],
  [
    "L=h=>h?12*N+620*(h-1):0",
    "shifts=h=>h===1?N:early[4-h],L=h=>h?12*N+early.slice(4-h).reduce((a,b)=>a+620+12*(b-1),0):0"
  ],
  [
    "d1<3",
    "d1<(5-h>=entry?3:1)"
  ],
  [
    "if(r[0]!==\"none\"&&b[0]!==\"none\")continue;",
    "if(!concurrent&&r[0]!==\"none\"&&b[0]!==\"none\")continue;"
  ],
  [
    "cost=2*hh+cc+r[3]+b[3]+g+2* +(!g&&ng)",
    "cost=2*hh+cc+r[3]+b[3]+g+2* +(!g&&ng)+(shifts(h)-1)*(2*human+compute+g)"
  ],
  [
    "if(cost>(h===1?12:620))",
    "if(cost>(h===1?12*N:620+12*(shifts(h)-1)))"
  ],
  [
    "let a={q,modes:",
    "let a={q,shifts:shifts(h),modes:"
  ],
  [
    "return R}",
    "return R*a.shifts}"
  ],
  [
    "scale*(R-a.cost)*(h===1?c.N:1),scale*(Z-b.cost)*(h===1?c.N:1)",
    "scale*(R-a.cost),scale*(Z-b.cost)"
  ],
  [
    "2*hh+cc+a.r[3]+a.b[3]+s[8]+2* +(!s[8]&&a.ng)",
    "2*hh+cc+a.r[3]+a.b[3]+s[8]+2* +(!s[8]&&a.ng)+(shifts(h)-1)*(2*(hh-a.r[1]-a.b[1])+cc-a.r[2]-a.b[2]-pop(a.keep)+s[8])"
  ],
  [
    "row[\"net\"+i]+=wt*(R[i]-cost)*(h===1?c.N:1)",
    "row[\"net\"+i]+=wt*(R[i]-cost)"
  ],
  [
    "z[6]+=(R[i]-a.cost)*(h===1?c.N:1)",
    "z[6]+=R[i]-a.cost"
  ]
];
function transform(source,edits){for(const [a,b] of edits){if(!source.includes(a))throw Error("source mismatch "+a);source=source.replace(a,b)}return source.replaceAll("(h===1?c.N:1)","shifts(h)")}
const compact=x=>({name:x.name,status:x.status,rule:x.rule,wealth:x.wealth,wealth_numerator:x.wealth_numerator,wealth_denominator:x.wealth_denominator,reason:x.reason,profiles:x.profiles,states:x.states,deviations:x.deviations,dated:x.dated});
const src=fs.readFileSync(path.join(__dirname,'service_window.js'),'utf8');
if(crypto.createHash('sha256').update(src).digest('hex')!==expected.base_source_sha256)throw Error('base source changed');
const study=new Function(transform(src,edits)+'\nreturn windowStudy')();
function reproduce(name){let vv=expected.variants.filter(v=>!name||v.name===name);if(!vv.length)throw Error('unknown variant');return vv.map(v=>{let results=study({...expected.common,...v.opts}).results.map(compact);if(JSON.stringify(results)!==JSON.stringify(v.results))throw Error('mismatch '+v.name);return {...v,results}})}
module.exports={reproduce};if(require.main===module)console.log(JSON.stringify(reproduce(process.argv[2]),null,2));
