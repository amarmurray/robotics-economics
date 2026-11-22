#!/usr/bin/env node
/* Independent exact BigInt audit of Python Fraction queue model.
   No external libraries, no real robot observations. */
'use strict';
const assert = require('node:assert/strict');
let checks=0;
const atoms=[];
for(let j=0;j<=1;j++) for(let h=0;h<=1;h++) for(let y=0;y<=1;y++) atoms.push({j,h,y,even:((j+h+y)%2===0)});
const M=128n; // theta=k/128, atom mass numerator n/(4*M)
for(let k=0n;k<=M;k++){
 const wt=a=>a.even?k:(M-k);
 const mass=4n*M;
 const sum=(pred)=>atoms.reduce((acc,a)=>acc+(pred(a)?wt(a):0n),0n);
 assert.equal(sum(()=>true),mass);checks++;
 for(let i of ['j','h','y']){
   assert.equal(sum(a=>a[i]===1),mass/2n);checks++;
 }
 for(let [i,j] of [['j','h'],['j','y'],['h','y']]){
  for(let x=0;x<=1;x++)for(let y=0;y<=1;y++){
    assert.equal(sum(a=>a[i]===x && a[j]===y),mass/4n);checks++;
  }
 }
 const expected=(policy)=>{
   let total=0n;
   for(const a of atoms){
      // All rewards in units of 1/32 AFTER deducting P pilot cost 4/32.
      let reward;
      if(policy==='R') reward=10n; // R Q=7/8, Y=1/2, cost=1/8
      else {
        const b3=a.j+a.h;
        const site2Served=policy==='S' && b3===0;
        const newJob=site2Served?1:0;
        const b4=Math.max(0,b3-1)+newJob;
        reward=-4n + (site2Served?16n:0n)+(b4===0 && a.y===1?32n:0n);
      }
      total+=wt(a)*reward;
   }
   return total;
 };
 // expected*32*mass, exact numerators in a common denominator mass.
 assert.equal(expected('R'),10n*mass);checks++;
 assert.equal(expected('W'),4n*mass+8n*4n*k);checks++;
 assert.equal(expected('S'),16n*4n*k);checks++;
 const got=[expected('R'),expected('W'),expected('S')].reduce((a,b)=>a>b?a:b);
 const closed=10n*mass>16n*4n*k?10n*mass:16n*4n*k;
 assert.equal(got,closed);checks++;
 assert.equal(sum(a=>a.j===0 && a.h===0 && a.y===1), M-k);checks++;
}
console.log(JSON.stringify({assertions:checks,theta_grid_points:Number(M+1n),model:'independent JS BigInt physical backlog and full P menu, compared with closed forms',scaling:'rewards in exact thirty-second units; type mass denominator 4*128'},null,2));
