# Utility inspection service and residual visits

Version: `utility-inspection/0.1`. Implementation: [utility_inspection.py](utility_inspection.py). Results: [eighteen complete worlds](results/utility_inspection.json). This is bounded DE-CF03, separate from annual cleaning-zone and courier units. Every numerical input is synthetic. No source count, wage, robot specification or advertised saving calibrates it.

## Service, identities and time

The default cohort contains twelve required point identities in four separate due windows. A point represents a specified measurement at a specified asset, with a declared quality and reviewer-disposition requirement. It is not a photograph, a robot mission, a maintenance action or an employee. Inputs may explicitly change the inventory, but point identities must remain unique and all channel references must resolve. There is no carryover: a later reading cannot fill a missed prior window.

The fixed and mobile channels have separately declared coverage, configuration qualification, quality failures, capture time and repeat count. These are assumed mission schedules, not optimized routes or empirically measured success probabilities. A fixed camera covering every synthetic point is a conditional alternative, not a claim that one particular thermal camera covers all real inspection tasks. A mobile channel does not assert that wheeled, quadruped and humanoid configurations are interchangeable.

Remote observations are processed in capture-time/identity order. A qualified observation consumes the specified expert minutes when a funded reviewer has capacity and can finish by the decision cutoff. Quality rejection consumes those minutes. An unqualified configuration is rejected without expert processing. Once a point is accepted, later duplicate observations cannot increase accepted output or consume redundant review; their capture resource bills remain. Duplicate suppression is a competent digital baseline, not an attributed model breakthrough. Review ordering is declared and deterministic, not an optimal joint sensor scheduler. No LLM is executed.

For window `w`, with required set `R` and accepted remote set `A_w`, residual readings are `R − A_w`. A visit is required if that set is nonempty, a separately declared field duty is due, or the assumed policy requires human presence. Replacement authority is a scenario input, not a legal or safety conclusion about any utility.

## Human fallback and retained commitments

A complete visit needs qualified human capacity, timely completion and funded resource bills. Human qualification and the ability to inspect every residual point are explicit fixture premises; the engine does not infer them from a robot's qualification. The default human route is an organized digital-recording baseline. It does not assume a measured AI productivity uplift.

Requested field person-minutes are:

`crew_size × (travel_elapsed + setup_elapsed + residual_points × point_elapsed) + separate_field_duty_person_minutes`.

Elapsed completion uses the corresponding crew time. Travel/setup/per-point work is assumed simultaneous across the crew; field-duty person-minutes divide across the crew under this bounded premise. If capacity or the deadline fails, this fixture starts no partial visit, preserves due work, and charges no conditional visit resource bill. It is a full-visit admission rule, not proof a real crew could never complete a subset. Remote points already accepted remain, but the whole-window service can still fail. With remote channels enabled, fallback starts at the declared decision cutoff; the human-only baseline can start at window opening. A future scheduler could prebook or launch people earlier, with different paid commitments. The late-fallback case deliberately tests this declared policy, not an inevitable disadvantage of robots.

`committed` staffing purchases the stated capacity and bills the crew every window even when no visit is needed. `per_visit` has an actually avoidable crew bill only when a funded visit starts. Neither contract claims a headcount reduction. Released task minutes, used person-minutes, purchased capacity and cash paid are separate fields. Review and provider support add person-time at their own resource boundaries. A field-duty case must be compared with the human baseline containing the same field duty; `human_field_duty` supplies that matched world.

Complete window service requires every reading and each declared physical duty/presence obligation. Raw captures and accepted point-windows remain separately visible. There is no cost-per-success ranking that silently drops failed due windows.

## Cash and operational resources

The unchanged [Treasury core](TREASURY_CORE.md) supplies immutable accounts, exact cents, invoices, settlements, cancellations and conservation checks. Its `Moment.month` field is a monotonically increasing **transaction sequence** here, not a financial month. Inspection windows and minute deadlines are separate explicit fields. This adapter does not claim integration with the monthly fleet, loan or enterprise demand ledger.

The operator first pays a committed field-crew bill when applicable, then the committed expert-review bill for an enabled monitoring service, then the fixed and mobile service fees in declared order. The provider subsequently funds its configured initial resources, recurring support and every planned capture before that channel operates. A paid customer fee cannot create an unfunded provider resource. Initial resources must actually be purchased before first operation; a failed initial attempt does not waive their cost in later windows. Support person-minutes are used only when the resource batch is funded, including when the resulting measurements fail acceptance.

Customer fees and fixed staffing/review bills are committed for the modeled window. Unpaid amounts remain obligations. Provider operating resources and visit bills are conditional batches: they settle all or none, with no partial cash stranded when the batch cannot be funded. The trace records the failed admission and cancelled conditional invoices. Existing committed arrears are retained; there is no invented creditor cross-default, automatic refund, collection or bankruptcy policy. Prepaid fees held by a nonperforming provider are cash, not earned profit. Actual refund/service-credit terms are unknown.

The fixed consolidation perimeter contains the operator and monitor provider. Their fees cancel. Field crew, expert review, travel supplies and technical-resource suppliers are external:

`operator cash outlay − provider net cash increase = external resource cash paid`.

All actor opening/closing cash reconciles and no account becomes negative. The external-resource bills are synthetic window cash proxies, not all underlying labor/material quantities. Provider support time is a physical resource annotation on its technical-resource bill and is not priced again. Equipment manufacture, asset lifecycle/replacement, capital opportunity cost, taxes, financing, failure losses and avoided outages are outside this module. Do not interpret provider cash accumulation as net enterprise profit or compute empirical ROI.

## Exact switches and limitations

With default fees, complete mobile coverage under the avoidable-visit contract costs the operator $560 over four windows. The human comparator costs `4 × (crew visit bill + $20 travel)`. The cash equality is a $120 crew bill per visit, conditional on equal complete service and every other stated premise. One cent either side changes the four-window difference by four cents. With one residual point, the mobile fee is added while every human visit remains; this threshold ceases to remove visits.

Twelve good readings need 24 review person-minutes per window. A capacity of 23 accepts eleven points under the specified ordering and retains the visit. The default capture time of minute 10 similarly needs a cutoff of at least minute 34. These are exact fixture boundaries, not empirical service standards.

The public evidence constrains what should be measured. It does not provide the target's full due inventory, real qualification matrix, accepted-output denominator, support/roster changes, contract rights or lifecycle cost. No population employment or deployment penetration is inferred. The model does not optimize a multi-site route, asset inspection intervals, damage prevention, maintenance dispatch or a mixed fleet. A future decision could favor increased monitoring without removing any visit, but this module deliberately assigns no avoided-failure value.

## Replay

Run `python3 scripts/export_utility_inspection.py`, or use `--check` to compare the saved artifact with current source and complete inputs. Use `--case saved.json --output replay.json` for a complete replay. `run_inspection_case` provides bounded shortcuts; `run_inspection` accepts the complete inventory and contracts; `replay_inspection` recomputes from saved inputs and ignores stored outcomes/hashes. Source hashes cover this module and the Treasury dependency. Money and counts require exact nonnegative integers, Booleans are not numbers, unknown fields/identities fail closed, and quantities are bounded.

The local `/api/utility-inspection` GET returns all witnesses. POST accepts exactly `inputs` or `saved_case`. The embodiment view offers applied controls, last-valid export, pending/error feedback, stale-response suppression and complete import. The panel has its own utility service boundary and does not relabel a selected annual scenario's units.
