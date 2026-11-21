import { pathToFileURL } from "node:url";

const startAt = "2026-03-01T09:00:00.000Z";
const weekEnd = "2026-03-08T09:00:00.000Z";
const arms = ["no_promotion", "fixed_promotion", "capacity_conditioned"];
const metrics = ["gross_margin", "repeat_purchase_rate", "refund_rate"];
const invariants = ["no_negative_inventory", "refunds_match_ledger"];

async function request(access, path, options, fetchImpl) {
  const response = await fetchImpl(access.baseUrl.replace(/\/$/, "") + path, {
    ...options,
    redirect: "error",
    headers: {
      "Content-Type": "application/json",
      "X-Shopify-Access-Token": access.accessToken,
    },
  });
  // Responses and credentials belong to the isolated agent interface.
  if (!response.ok) throw new Error(`Native interface returned HTTP ${response.status}`);
  return response.json();
}

async function act(access, arm, fetchImpl) {
  const orders = await request(access, "/admin/api/2026-01/orders.json?status=open&limit=50&fields=id,fulfillment_status",
    { method: "GET" }, fetchImpl);
  if (!Array.isArray(orders.orders)) throw new Error("Missing order records on native interface");
  if (orders.orders.some(order => !Object.hasOwn(order, "fulfillment_status"))) {
    throw new Error("Native order record lacks fulfillment status");
  }
  const backlog = orders.orders.filter(order => order.fulfillment_status !== "fulfilled").length;
  const promote = arm === "fixed_promotion" || (arm === "capacity_conditioned" && backlog <= 8);
  if (promote) {
    const query = `mutation PilotPromotion($input: DiscountAutomaticBasicInput!) {
      discountAutomaticBasicCreate(automaticBasicDiscount: $input) {
        automaticDiscountNode { id }
        userErrors { field message }
      }
    }`;
    const input = { title: "RoboEcon seven-day pilot", startsAt: startAt, endsAt: weekEnd,
      customerGets: { value: { percentage: 0.10 }, items: { all: true } } };
    const result = await request(access, "/admin/api/2026-01/graphql.json",
      { method: "POST", body: JSON.stringify({ query, variables: { input } }) }, fetchImpl);
    const mutation = result.data?.discountAutomaticBasicCreate;
    if (result.errors?.length || mutation?.userErrors?.length || !mutation?.automaticDiscountNode?.id) {
      throw new Error("The native discount mutation was unavailable or rejected in this world");
    }
  }
  return { backlog_sample_capped_at_50: backlog, promotion_installed: promote };
}

export async function runForks(parent, seed, fetchImpl = fetch) {
  const children = [];
  const reports = [];
  try {
    const start = await parent.checkpoints.create({ name: "before-retention-policy" });
    for (const arm of arms) {
      const child = await parent.forks.create({ from: start.id, name: arm });
      children.push(child);
      const access = await child.interfaces.connect("shopify-admin",
        { scopes: ["read_orders", "write_discounts"], expiresIn: "2h" });
      const action = await act(access, arm, fetchImpl);
      await child.clock.advance({ days: 30, mode: "until-idle" });
      const end = await child.checkpoints.create({ name: "after-settlement" });
      const report = await child.evaluate({ metrics, invariants });
      if (typeof report.passed !== "boolean" || metrics.some(key => !Number.isFinite(report.metrics?.[key]))) {
        throw new Error("Hosted evaluator did not return the specified business metrics and pass status");
      }
      reports.push({ arm, end: end.id, action, metrics: report.metrics, passed: report.passed,
        violations: report.violations });
    }
    const baseline = reports[0].end;
    for (const report of reports.slice(1)) {
      const diff = await parent.inspect.diff({ from: baseline, to: report.end });
      report.diff_from_no_promotion = diff.summary;
    }
    return { seed, start: start.id, startAt, horizon_days: 30, reports,
      passed: reports.every(report => report.passed) };
  } finally {
    // Destroy only disposable forks this invocation created, even if a later arm failed.
    const cleaned = await Promise.allSettled(children.map(child => child.destroy()));
    if (cleaned.some(outcome => outcome.status === "rejected")) {
      throw new Error("A disposable fork could not be removed; check the Counterworld project");
    }
  }
}

async function main() {
  const key = process.env.COUNTERWORLD_API_KEY;
  if (!key) throw new Error("No Counterworld project key is configured in this runtime");
  const { Counterworld, catalog, buyers, storeAdmins, warehouseOperators } = await import("@counterworld/sdk");
  const client = new Counterworld({ apiKey: key });
  const seed = process.argv[2] || "roboecon-retention-01";
  const parent = await client.worlds.create({ name: "roboecon-retention", seed,
    systems: [catalog.shopify(), catalog.stripe()],
    history: { years: 1, seed },
    population: [buyers({ count: 300, discountSensitivity: 0.65, returnPropensity: 0.18 }),
      storeAdmins({ count: 4, approvalDelayHours: 6 }),
      warehouseOperators({ count: 8, shiftCoverage: 0.82 })],
    clock: { startAt } });
  try {
    const report = await runForks(parent, seed);
    console.log(JSON.stringify(report, null, 2));
    if (!report.passed) process.exitCode = 2;
  } finally {
    await parent.destroy();
  }
}

if (process.argv[1] && import.meta.url === pathToFileURL(process.argv[1]).href) {
  main().catch(error => { console.error(error.message); process.exitCode = 1; });
}
