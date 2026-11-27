'use strict';

// Read the existing funded game's payoff matrices at its accepted cap-2 calibration.
// The observer records comparisons after backward induction values a matrix.
const assert = require('node:assert/strict');
const crypto = require('node:crypto');
const fs = require('node:fs');
const path = require('node:path');

const directory = path.join(__dirname, '..', 'papers', 'integrated_firm');
const source = fs.readFileSync(path.join(directory, 'funded_embodied.js'), 'utf8');
assert.equal(crypto.createHash('sha256').update(source).digest('hex'),
    '23cd1539486d25b2fc9ad8a5be0876b0ebdcaa8045b5f3359a1ef29adc77a6ca');
const archive = JSON.parse(fs.readFileSync(path.join(directory, 'funded_embodied_results.json'), 'utf8'));
const accepted = archive.cases.find(c => c.parameters.cap === 2);
const pairsByMenu = new WeakMap();

function qualificationPairs(menu, procedure) {
    if (pairsByMenu.has(menu)) return pairsByMenu.get(menu);
    const groups = new Map();
    for (const [index, action] of menu.entries()) {
        const target = action.r[5];
        if (target !== 4 && target !== 5) continue; // Only local execution qualification.
        const key = [action.q, target, action.b[4], action.b[5]].join('/');
        if (!groups.has(key)) groups.set(key, []);
        groups.get(key).push(index);
    }
    const pairs = [];
    for (const group of groups.values()) {
        group.sort((a, b) => menu[a].r[4] - menu[b].r[4]);
        assert.equal(group.length, procedure + 1);
        assert.equal(menu[group[0]].r[4], 2);
        for (let n = 1; n < group.length; n++) {
            const low = menu[group[n - 1]], high = menu[group[n]];
            assert.equal(high.r[4], low.r[4] + 1); // Probabilities in quarters.
            // The public outcome probability is the only difference, including outlay.
            const sameChance = {...high, r: high.r.map((v, k) => k === 4 ? low.r[4] : v)};
            assert.deepEqual(low, sameChance);
            pairs.push([group[n - 1], group[n]]);
        }
    }
    pairsByMenu.set(menu, pairs);
    return pairs;
}

const byRule = new Map();
function observe(rule, h, states, menus, matrix, scale) {
    if (h === 1) return;
    if (!byRule.has(rule)) {
        byRule.set(rule, {higher: 0, tied: 0, lower: 0, firstLoss: null});
    }
    const counts = byRule.get(rule);
    for (const [firm, ownMenu] of menus.entries()) {
        const procedure = states[firm][6];
        if (procedure === 0) continue;
        const rivalMenu = menus[1 - firm];
        for (const [low, high] of qualificationPairs(ownMenu, procedure)) {
            for (const [rival, rivalAction] of rivalMenu.entries()) {
                const difference = firm === 0
                    ? matrix[high][rival][0] - matrix[low][rival][0]
                    : matrix[rival][high][1] - matrix[rival][low][1];
                assert(Number.isSafeInteger(difference));
                if (difference > 0) counts.higher++;
                else if (difference === 0) counts.tied++;
                else {
                    counts.lower++;
                    if (!counts.firstLoss) {
                        counts.firstLoss = {h, firm, states, low: ownMenu[low], high: ownMenu[high],
                            rival: rivalAction, higherMinusLower: difference / scale};
                    }
                }
            }
        }
    }
}

// The published script is self-contained with private functions. Attach one read-only
// observer to the pinned source in memory and request only the archived cap-2 cases.
const observedSource = source
    .replace('let e=null,eq=0;', 'observe(rule,h,[s,z],[aa,bb],mat,pow[h]); let e=null,eq=0;')
    .replace('cases:cases.map(', 'cases:cases.filter(c=>c.cap===2).map(')
    .replace('console.log(JSON.stringify(embodied(),null,2));', 'return embodied();');
const replay = new Function('observe', observedSource)(observe);
assert.deepEqual(replay.cases, [accepted]); // Includes both selectors, all deviations and dated cash.
assert.equal(byRule.size, 2);
for (const [rule, counts] of byRule) {
    const comparisons = counts.higher + counts.tied + counts.lower;
    console.log(JSON.stringify({rule, comparisons, ...counts}));
    assert.deepEqual([counts.higher, counts.tied, counts.lower], [413584, 239456, 0]);
}
