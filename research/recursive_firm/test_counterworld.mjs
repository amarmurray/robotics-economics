import { strict as assert } from "node:assert";
import test from "node:test";
import { runForks } from "./counterworld.mjs";

function fixture(backlog, refuse = false) {
  const starts = [], cleaned = [], calls = [], days = [], diffs = [];
  const parent = {
    checkpoints: { create: async () => ({ id: "fixture-start" }) },
    forks: { create: async ({ from, name }) => {
      starts.push(from);
      return {
        interfaces: { connect: async () => ({ baseUrl: "https://fixture.invalid/" + name, accessToken: "fixture" }) },
        clock: { advance: async ({ days: count }) => days.push(count) },
        checkpoints: { create: async () => ({ id: name + "-end" }) },
        evaluate: async () => ({ passed: true, metrics: { gross_margin: 0, repeat_purchase_rate: 0, refund_rate: 0 }, violations: [] }),
        destroy: async () => cleaned.push(name),
      };
    } },
    inspect: { diff: async ({ from, to }) => { diffs.push([from, to]); return { summary: {} }; } },
  };
  async function fakeFetch(url, options) {
    assert.match(url, /^https:\/\/fixture\.invalid\//);
    calls.push(options.method);
    const orders = Array.from({ length: backlog }, (_, id) => ({ id, fulfillment_status: null }));
    const result = options.method === "GET" ? { orders } :
      { data: { discountAutomaticBasicCreate: { automaticDiscountNode: { id: "fixture-discount" }, userErrors: [] } } };
    return { ok: !(refuse && options.method === "POST"), status: 422, json: async () => result };
  }
  return { parent, fakeFetch, starts, cleaned, calls, days, diffs };
}

test("all arms fork the same state and wait for settlement", async () => {
  for (const backlog of [3, 12]) {
    const f = fixture(backlog);
    const result = await runForks(f.parent, "fixture-only", f.fakeFetch);
    assert.deepEqual(f.starts, ["fixture-start", "fixture-start", "fixture-start"]);
    assert.deepEqual(f.days, [30, 30, 30]);
    assert.deepEqual(result.reports.map(r => r.action.promotion_installed), [false, true, backlog <= 8]);
    assert.equal(f.calls.filter(c => c === "POST").length, backlog <= 8 ? 2 : 1);
    assert.equal(f.cleaned.length, 3);
    assert.equal(f.diffs.length, 2);
    assert.ok(result.passed);
  }
});

test("unsupported native operation fails and cleans the created forks", async () => {
  const f = fixture(2, true);
  await assert.rejects(() => runForks(f.parent, "fixture-only", f.fakeFetch), /HTTP 422/);
  assert.deepEqual(f.cleaned, ["no_promotion", "fixed_promotion"]);
});
