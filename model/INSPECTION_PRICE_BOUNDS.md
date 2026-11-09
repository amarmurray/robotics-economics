# Matched inspection service and window cash bounds

The [implementation](inspection_price_bounds.py) derives eight comparisons from the eighteen unchanged [inspection executions](results/utility_inspection.json). It adds no deployment world, measured price, maintenance value or failure probability. Both complete inspection inputs are recomputed. Saved eligibility, costs, executions and hashes never substitute for replay.

## Qualify the comparison first

Match the due point/property identities, number of windows, final deadline, physical-duty schedule/content and required presence. Identity order does not change the obligation; a different duty or deadline does. Both executions must complete every due window and have no unpaid committed bills. Every enabled monitoring channel's fee and resource booking must be funded. Whole service delivered by customer fallback does not establish fulfillment of an unfunded provider booking. An alternative with no monitoring service has no monitoring-fee bound.

Ineligible comparisons retain their actual cash and exact reasons, but the bound is null. A missing or unmatched service is not assigned zero cost or priced as an equivalent offer. Qualification here concerns the declared synthetic property identities. It does not establish that a real camera, mobile sensor and human method measure the same thing. The empirical measurement-equivalence gate remains separate.

## Customer, provider and consolidated boundaries

Let B be the complete baseline and A the complete alternative. All values are exact cents across the same complete window, not annual prices or per-success denominators. Let C be customer outlay, F the internal monitoring fee, P the provider's paid external resources, and G its net cash change. Existing Treasury histories establish `P = F − G`; customer nonfee outlay is `C − F`. Both legal payers' external payments remain visible.

With no additional downstream value assigned, the customer's total-fee ceiling is `C_B − (C_A − F_A)`. The provider's recorded-resource recovery amount is `P_A`. The difference between those bounds is:

`width = C_B − (C_A − F_A) − P_A = G_B − (R_A − R_B)`,

where R is consolidated external-resource cash. Baseline provider cash change therefore separates the buyer-facing interval from consolidated resource savings. Fees are not added to the same provider resources. Cash accumulation is not enterprise profit, and no actual margin requirement is inferred.

A negative fee ceiling is retained: even a free monitoring service would leave additional customer-side cost under those fixed realized inputs. A nonnegative width supplies only a necessary aggregate window-cash condition. It is not a feasible quote or a sufficient funding proof. Changing fee amount or timing requires replaying the complete service; it can change which work is funded and therefore the costs themselves.

The output reports three required-but-unproven net-value thresholds: at the recorded customer fee, at provider recorded-resource recovery, and for consolidated resources. Each is the positive part of the relevant cost difference. They assign no benefit. Any later claimed value must be net of extra intervention, review, failure exposure and other downstream costs at the same boundary. Identical accepted readings alone establish no changed maintenance action.

## Limitations and reproduction

These window bills exclude full equipment lifecycle, capital opportunity cost, taxes, financing, terminal assets, contract remedies and profit. They are inherited synthetic assumptions, not current rights or commercial terms. Paid staffing follows the explicit existing contract and is not measured payroll removal. A cost-recovery bound is not ROI, a competitive equilibrium or a pricing recommendation.

Run `python3 scripts/export_inspection_price_bounds.py` and then `--check`. Replay a complete pair with `--case FILE --output FILE`. Run `python3 -m unittest tests.test_inspection_price_bounds -v`. The existing utility panel adds saved-pair selection, explicit comparison of the currently applied inspection with a reference, complete export/import and stale-response protection. Annual scenario edits and source filters do not rewrite an applied pair.
