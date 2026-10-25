# Independent evidence review: physical supply and field cases

Review version 0.2 · 25 October 2026 · Reviewer: A/C specialist, independent of I/J authorship · Input repository `campaign launch snapshot (see ignored sync_receipt.json)`.

**Disposition: pass after targeted corrections. All five findings below were addressed in I/J edition 0.2 and rechecked.** No fabricated cost estimate, blanket platform-open-source classification, or unsupported numerical transfer was found in the checked claims. The most consequential addition is adverse Rwanda cost evidence and clarification of its road-service counterfactual. This is a bounded review, not an audit of every source or an independent validation of manufacturer specifications.

Reviewed artifacts before corrections:

- `research/physical_supply_field.md`, SHA256 `38cd594f204567f9cfe8627a817e82c226b0b38cd498506e976aa029c055e82b`.
- `data/physical_evidence.json`, SHA256 `c92bbca24b7ce51acb755852ab47684103a54a45ed972ca2c103e1dff9ffbdaa`.

Independent retrieval on 25 October 2026 used direct HTTPS for the full PG&E PDF, Missouri article, Unitree product pages and three commit-pinned licenses, with GitHub commit API checks for dates. PG&E was read with `pdftotext -layout`, including later demonstrations. The full Lancet article's primary indexed text was recovered through Exa searches, separately from the PubMed abstract. No test flight, robot execution, license dependency audit or independent field telemetry was available.

## Findings requiring correction

### PHY-R01 — Medium: preserve Rwanda's adverse cost direction and service counterfactual

**Records:** `PHY-E05`, `PHY-D02`, `PHY-C02`; Rwanda narrative.

The main dossier correctly says cost-effectiveness remains unresolved and avoids claiming provider profit. The full article additionally states that drone delivery was more expensive than road delivery in Rwanda at the time. This is a consequential adverse observation for a business-model comparison and should accompany the unresolved cost-effectiveness statement. It is an author statement without a complete priced cost table; do not turn it into a calibrated cost ratio or current-price claim.

The road comparison also changes with operating organization. Hospitals' own vehicles made a full round trip in the main comparator. A sensitivity analysis assumes a delivery service based at the blood-transfusion center, requiring only a one-way trip. It reports median drone advantages of 19 minutes against the center's driving estimate and 28.5 minutes against Google Maps. These are much smaller than the headline 79/98-minute comparisons. The relevant insight is partly network/dispatch design, not an aircraft-only productivity coefficient.

**Primary locator:** [Lancet full text](https://www.thelancet.com/journals/langlo/article/PIIS2214-109X(22)00048-1/fulltext), Results paragraphs beginning “As hospitals use their vehicles”; Table 2 sensitivity; Discussion final paragraph beginning “Given our findings”. DOI `10.1016/S2214-109X(22)00048-1`.

**Suggested correction:** Add historical adverse cost direction, distinguish round-trip existing practice from one-way alternative, and retain no causal mortality/ROI inference. Resolved in edition 0.2; corrected narrative and evidence record independently rechecked.

### PHY-R02 — Medium: distinguish Rwanda timing statistics, sample and acceptance status

**Records:** `PHY-E05`, `PHY-D02` metrics and accepted outcome.

The full text reports a mean of 49.6 minutes including order preparation/packaging. Its Table 1 comparison uses a 41-minute median excluding that preparation, alongside road medians of 120 and 139 minutes. Therefore the 79/98-minute differences must not be described as arithmetic differences between the reported 49.6-minute mean and an otherwise matched road mean. The abstract compresses this distinction; the full article is the safer source for modeling.

The study's timing analysis concerns emergency orders, while 12,733 is the total delivered-order count and 5,517 is the emergency subset. Record this scope rather than implying the same statistic applies to all resupply activity. A delivery count does not establish that every order met the clinically required deadline. The JSON's “clinically usable time” should be explicitly an intended acceptance rule with the observed SLA pass fraction unknown.

The reported 67% reduction is an interrupted-time-series expiration estimate at 12 months, with no control group. Preserve its interpretation as historical observational evidence and avoid conflating reduced expiration with proven health outcomes. The source reports an immediate change of 7.1 fewer expirations per facility per month, 95% CI −11.8 to −2.4; the subsequent slope reduction was not significant.

**Primary locator:** same full text, Methods delivery-time calculation; Results paragraph beginning “Table 1 shows”; Results expiration paragraph; Discussion limitations. Source explicitly notes actual road-time collection was prevented by COVID restrictions, leading to estimated road comparators.

**Suggested correction:** Add timing/sample definitions and unknown SLA fraction; update `access` from an undifferentiated full-text claim to the actual retrieval path. Electronic publication is 15 March 2022; April 2022 is the journal issue. Resolved in edition 0.2; corrected narrative and structured records independently rechecked.

### PHY-R03 — Medium: include PG&E's later mixed results and deferred integration

**Records:** `PHY-E04`, `PHY-D01`; PG&E narrative.

Tables 3/4 support the existing claim that successful flight did not deliver accepted inspection imagery. Later sections materially sharpen the account. Vendor A was disqualified before Demonstration 3. Vendor B's Templeton flight criteria were met, while Silverado's were not; image capture was not evaluated because the known sensor hardware did not meet PG&E standards. Distribution-alert integration could not be completed and was deferred to potential EPIC 4 work.

These later findings strengthen the output-quality/integration argument while preserving successful flight results in another setting. They prevent a reader from interpreting the final project as a single uniform failed flight test or treating later remote flight as remediation of the image-quality problem. The report also claims travel/safety benefits qualitatively; it does not provide the matched accepted-inspection cost denominator needed to calibrate savings.

**Primary locator:** [PG&E EPIC 3.41 final report v1.0, 27 May 2025](https://www.pge.com/assets/pge/docs/about/corporate-responsibility-and-sustainability/pge-epic-project-3.41.pdf), printed pp.17–20, sections 4.4–4.5, Tables 5/6; physical PDF pp.21–24.

**Suggested correction:** Add a concise later-results paragraph and keep no generalized reliability percentage. Resolved in edition 0.2; corrected narrative and structured records independently rechecked.

### PHY-R04 — Low: correct PG&E physical PDF locators

The dossier/evidence record gives printed pp.15–16 as PDF pp.18–19. Independent PDF extraction places them at **physical PDF pp.19–20**; Table 4 continues on printed p.17 / PDF p.21. The printed locators were correct. Correct the PDF offsets, including later-result references, so a reviewer reaches the actual tables.

### PHY-R05 — Low: sharpen agricultural metric provenance in structured records

The North Dakota/Missouri narrative keeps populations distinct correctly, but `PHY-D03` repeats the combined geography and period on each metric. For machine consumers, tag North Dakota licensed-applicator/acreage observations as North Dakota 2025 and Missouri cost scenarios as hypothetical March-2025 budgets. Keep a composite dossier grouping while giving each metric its actual population.

The Missouri values are verified: $12.27/applied acre at 1,000 acres/year and $7.39 at 4,000 acres/year; allocated investment $56,000 and $94,500. The source assumes one versus two aircraft, one versus two crew members, and different travel/cleaning burdens. These are not a pure scale comparison holding the production system fixed. Record those configuration differences if the models later use these budgets.

**Primary locator:** [Missouri Extension G1274](https://extension.missouri.edu/publications/g1274), March 2025, Tables 1–3 and Recommendations. The publication indeed contains inconsistent wording: the recommendation associates 980 acres with a $16 custom-hire comparator, while the later cost-by-acreage discussion associates it with a $12.50 target and reports $12.43 at 980 acres. The dossier already preserves this conflict and correctly declines to adopt a verified break-even. No new correction to that conclusion is needed.

## Checks that passed

| Check | Independent evidence and result |
| --- | --- |
| PG&E flight versus imagery | Table 3's Vendor A flight criteria are met while image criteria fail. Table 4 documents Vendor B signal loss, waypoint drift and low image resolution. Flight activity is correctly not converted to accepted inspection output or savings. |
| Rwanda observed quantities | Full article supports 20 facilities, 12,733 total orders, 5,517 emergencies, historical 2017–19 delivery window, faster estimated delivery and lower modeled expiration. Foreign/interfacility scope is clearly separated from US indoor hospital work. |
| Missouri modeled costs | Tables 1–3 support costs/investments as hypothetical scenario budgets. No operator margin or actual North Dakota unit cost is claimed. Threshold conflict is preserved. |
| Unitree G1 base configuration | Direct product table supports 23 joint DOF, 8-core CPU, depth camera/3D lidar, 9,000 mAh pack, 54V/5A charger and no base high-compute module. EDU options are not silently assigned to base G1. |
| Unitree Go2 EDU configuration | Direct table supports 12 motor sets, EDU 15,000 mAh battery, 33.6V/9A charger, foot-force/depth sensors, docking compatibility and unspecified high-compute module options including Orin 40–100 TOPS. Exact board/memory and field endurance remain unknown appropriately. |
| Unitree SDK2 rights | [Pinned LICENSE](https://raw.githubusercontent.com/unitreerobotics/unitree_sdk2/d1abf001220d3e5f59e00a0c4aaa595e00089a4a/LICENSE) is BSD-3-Clause; commit API confirms 15 October 2026. Rights are confined to the artifact, with complete robot/firmware/operating rights separately unresolved. |
| UniFoLM-WMA rights | [Pinned LICENSE](https://raw.githubusercontent.com/unitreerobotics/unifolm-world-model-action/3e198de68de55f93f24b3ad623dd499390aaee45/LICENSE) is CC BY-NC-SA 4.0; commit API confirms 18 March 2026. Noncommercial restrictions are explicit and not overridden by SDK licensing. |
| ODRI hardware-documentation rights | [Pinned LICENSE](https://raw.githubusercontent.com/open-dynamic-robot-initiative/open_robot_actuator_hardware/66af1522b4fba0ec4a1d7790e66f5e4652208d30/LICENSE) is BSD-3-Clause; commit API confirms 6 September 2022. No manufacture-yield, qualification or complete-platform freedom is inferred. |
| Matched service boundaries | Inspection alternatives must meet equal measurement quality/coverage/interval; medical delivery alternatives must preserve timing/handling. Numeric cost rankings remain unavailable. Shared output and inventory/learning benefits are not duplicated. |

## Residual review limits and publication condition

This review did not independently verify all other ecosystem actors, ROS/PX4/Octo license dependencies, underlying aircraft telemetry, component suppliers, certification documents, or unpublished prices. Product pages remain manufacturer specifications; configuration SKU/serial-version and rights dependencies are still open. Rwanda's exact commercial contract prices and accepted-SLA distribution are not available from the inspected article. PG&E scorecards are categorical test outcomes, not a representative fleet reliability estimate.

The publication condition is satisfied for this bounded review: PHY-R01–R05 were incorporated and the changed passages/records rechecked against the independent source extracts. April 2022 is now explicitly typed as the journal issue date; retaining that verified issue date is acceptable without asserting an independently verified electronic date. The delivery-time sample size remains unknown rather than forcing all 12,733 or exactly 5,517 into its denominator. Re-running every source fetch or broadening to additional cases would not add necessary assurance for this bounded review.


## Correction recheck receipt

I/J edition 0.2 was rechecked on 25 October 2026. R01 adverse historical cost and round-trip/one-way counterfactual, R02 preparation/statistic/sample/SLA boundaries and access history, R03 later mixed PG&E results, R04 physical PDF locators, and R05 per-metric agricultural provenance/configuration differences are all resolved. The residual limitations above remain research gaps rather than unresolved review defects.

Accepted reviewed hashes:

- `research/physical_supply_field.md`: `47f754f876dce6df072a96a50cadcd697ff883641ed9cc4cb2faf8ed3588b54f`.
- `data/physical_evidence.json`: `17560b4e78e01603f12628f8e71f03288ab708ef874c8ec7320965675f1da2ea`.
