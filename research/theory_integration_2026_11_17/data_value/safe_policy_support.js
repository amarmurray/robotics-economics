"use strict";

function gcd(a,b){a=a<0n?-a:a;b=b<0n?-b:b;while(b!==0n){const t=a%b;a=b;b=t;}return a;}

function F(n,d=1n){n=BigInt(n);d=BigInt(d);if(d===0n)throw Error("denominator zero");if(d<0n){n=-n;d=-d;}const g=gcd(n,d);return [n/g,d/g];}

function plus(a,b){return F(a[0]*b[1]+b[0]*a[1],a[1]*b[1]);}

function times(a,b){return F(a[0]*b[0],a[1]*b[1]);}

function minus(a,b){return F(a[0]*b[1]-b[0]*a[1],a[1]*b[1]);}

function txt(a){return a[1]===1n?String(a[0]):String(a[0])+"/"+String(a[1]);}

function cmp(a,b){const x=a[0]*b[1]-b[0]*a[1];return x===0n?0:x>0n?1:-1;}

function core(){
const z=F(0),one=F(1);
const rows=[
{name:"A",w:F(3,5),e:one,delta:F(3,10),R:F(2)},
{name:"B",w:F(2,5),e:F(1,4),delta:F(1,10),R:F(2)}];
let covered=z,missing=z,unknown=z;
for(const r of rows){covered=plus(covered,times(times(r.w,r.e),r.delta));const q=times(r.w,minus(one,r.e));missing=plus(missing,q);unknown=plus(unknown,times(q,r.R));}
const bounds=[minus(covered,unknown),plus(covered,unknown)];
const anchoredUncertainty=times(missing,F(1));
const anchored=[minus(covered,anchoredUncertainty),plus(covered,anchoredUncertainty)];
const isolated=minus(covered,F(2,25));
const netCost=minus(isolated,F(3,20));
let low=bounds[1],high=bounds[0],alow=anchored[1],ahigh=anchored[0],states=0;
for(let yp=0;yp<=2;yp++)for(let ys=0;ys<=2;ys++){const d=plus(covered,times(missing,F(yp-ys)));if(cmp(d,low)<0)low=d;if(cmp(d,high)>0)high=d;if(ys===1){if(cmp(d,alow)<0)alow=d;if(cmp(d,ahigh)>0)ahigh=d;}states++;}
const yP=[2,1,2,0],yS=[1,1,1,1];let sumsP=z,sumsS=z,assignments=0;
for(let m=0;m<16;m++){let htp=z,hts=z;for(let i=0;i<4;i++){if((m&(1<<i))!==0)htp=plus(htp,F(yP[i],2));else hts=plus(hts,F(yS[i],2));}sumsP=plus(sumsP,htp);sumsS=plus(sumsS,hts);assignments++;}
const HTp=times(sumsP,F(1,16)),HTs=times(sumsS,F(1,16));
const directP=F(yP.reduce((a,b)=>a+b,0),4),directS=F(yS.reduce((a,b)=>a+b,0),4);
const expected={covered:"19/100",missing:"3/10",missingWidth:"3/5",globalLow:"-41/100",globalHigh:"79/100",anchoredLow:"-11/100",anchoredHigh:"49/100",isolationLower:"11/100",afterCost:"-1/25",htP:"5/4",htS:"1",htDiff:"1/4"};
const actual={covered:txt(covered),missing:txt(missing),missingWidth:txt(unknown),globalLow:txt(bounds[0]),globalHigh:txt(bounds[1]),anchoredLow:txt(anchored[0]),anchoredHigh:txt(anchored[1]),isolationLower:txt(isolated),afterCost:txt(netCost),htP:txt(HTp),htS:txt(HTs),htDiff:txt(minus(HTp,HTs))};
let checks=0;for(const k of Object.keys(expected)){if(actual[k]!==expected[k])throw Error(k+"="+actual[k]+" expected "+expected[k]);checks++;}
for(const [a,b] of [[low,bounds[0]],[high,bounds[1]],[alow,anchored[0]],[ahigh,anchored[1]],[HTp,directP],[HTs,directS]]){if(cmp(a,b)!==0)throw Error("boundary/effect enumeration mismatch");checks++;}
const sequence={G_then_R:9+13,R_then_G:10+9,R_then_R:10+10,naive_G_period:9,naive_R_period:13};if(!(sequence.G_then_R>sequence.R_then_R&&sequence.naive_G_period<sequence.naive_R_period))throw Error("carryover reversal missing");checks++;
if(!(cmp(covered,F(0))>0&&cmp(bounds[0],F(0))<0&&cmp(anchored[0],F(0))<0&&cmp(isolated,F(0))>0&&cmp(netCost,F(0))<0))throw Error("sign case mismatch");checks++;
return {version:"2026-11-18",scope:"synthetic exact fractions; no field calibration or physical safety",inputs:{strata:rows.map(r=>({name:r.name,target_weight:txt(r.w),safe_covered_share:txt(r.e),covered_policy_difference:txt(r.delta),whole_service_payoff_range:txt(r.R)})),residual_bound:"2/25",additional_cost:"3/20"},results:actual,verified_extreme_states:states,assignment_vectors_enumerated:assignments,checks,carryover:sequence,notes:["The worldwide policy on unsupported cells is a hypothetical estimand, not a physically admissible choice without separate certification.","Only pre-assignment customer/pool strata are conditioned upon; post-policy demand enters whole-service Y.","Positive policy mean effect does not establish per-regime dominance or pathwise operator safety."]};
}

if (typeof module !== "undefined" && module.exports) module.exports = { core };
if (typeof require !== "undefined" && typeof module !== "undefined" && require.main === module) process.stdout.write(JSON.stringify(core(), null, 2)+"\n");
