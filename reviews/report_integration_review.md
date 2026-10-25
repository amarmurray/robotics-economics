# Independent review of follow-up integration into the full report

Review date: 25 October 2026. Reviewer: capability/learning lane. Scope is limited to the four follow-ups added by `scripts/build_report.py`, the resulting additions to `REPORT.md`, and the final two sections of `research/integrated_decisions.md`: “What the deeper investigations change” and “Decisions to make next, and the evidence that could reverse them.” The remainder of the approximately 32,483-word report was not given a new substantive source audit in this review.

**Disposition: pass. No material support, boundary or link correction is required for these integration changes.** The new executive synthesis is supported by the accepted dossiers and preserves the limitations that constrain its conclusions. The builder retains the complete follow-up analyses within relevant chapters. It does not replace unresolved evidence with numerical assumptions or represent local software tests as validation of a deployed physical system.

## Synthesis checked against accepted analysis

| Integrated finding | Supporting dossier | Boundary preserved |
| --- | --- | --- |
| Hospital service eligibility, residual human work and unresolved reliability denominator | `research/field_support_denominators.md` | Guro excludes urgent requests and retains routine handling plus an accompanying operator. The conflicting published percentage and count-implied percentage remain unresolved. Qilu's distribution/retrieval means do not establish full-shift labor savings; FTE/ROI methods remain unverified. |
| Non-Spot inspection coverage is narrower than navigation or market adoption | `research/quadruped_operator_followup.md` | Room-specific visibility, closed doors, energized-area restrictions and unfinished integration qualify the offshore result. Later pilot windows and mission repertoires do not identify productive exposure, retention, avoided human visits or full cost. Lack of a retention record is not evidence of abandonment. |
| Collection-stage economy differs from the cost of validated capability | `research/learning_data_economics.md` | Cobalt's conditional cloud-resource calculation is separated from collection labor, curation, training and physical evaluation. DexWild's dataset-size changes and within-batch sampling ratios remain distinct, with robot grounding and recovery coverage still needed. |
| Benchmark cost and clock denominators cannot price physical orchestration directly | `research/coordination_reproducibility.md` | TAC displayed costs include non-perfect results, while Astranomy's conditional cost covers a successful subset. Missing infrastructure, other model calls, unsuccessful episodes and exact executed budget configuration remain limitations. Paused simulation does not establish elapsed-time service in a changing physical environment. |
| Admission, assignment, execution and reconciliation require separate authority | `research/coordination_reproducibility.md` | Request acceptance and cancellation acknowledgement do not establish completed work, physical stop or reversal of business effects. Durable identifiers do not by themselves make external effects and local state one atomic transaction. Target installation and operating evidence remain necessary. |

The hospital paragraph also avoids reintroducing the earlier wording ambiguity: it describes the observed staff arrangement and conflict without claiming that the source formally defines intervention as only corrective assistance. The full integrated follow-up retains the literal “without any human intervention” definition and labels the corrective-versus-routine distinction as contextual interpretation. It likewise retains the separate ChristianaCare 107-versus-111 discrepancy and the absence of matched support exposure for later cumulative deliveries.

The quadruped synthesis does not merge the offshore and later onshore episodes into a retained fleet. It does not convert room coverage into inspection reliability or labor substitution, and does not assign combined fixed-sensor, drone or digital-maintenance benefits to the quadruped.

The learning paragraph makes no universal scaling or cost coefficient. Its proposed fixed-target, full-cost experiment is an analytical next step consistent with the dossier's missing collection, processing, training and validation denominators; it is not presented as an experiment already performed.

The coordination paragraph's statement that local fault tests **can** establish software behavior under declared assumptions is conditional. It does not assert that this report already validates an installed Open-RMF stack, a complete transaction system, safety-rated robot control or LLM productivity uplift. The four follow-ups' separate source and test boundaries survive their placement in a larger report.

## Decision recommendations and implementation boundary

The added decision section is a synthesis of mechanisms, not a new empirical ranking. It asks for a matched service, credible alternatives, process authority, residual work and the evidence that could reverse a preferred course. Specialized machinery, digitally improved human processes, prompt incumbent response and support burden remain valid counterexamples rather than being assumed away.

The section explicitly separates economic value, commercial allocation and dated liquidity. It says the current annual fleet and separate monthly entrant resource pools do **not** establish joint financeability. That is the correct boundary while the next treasury stage is still being built and reviewed. A later standalone ledger test would not, by itself, close the shared physical-resource integration gap.

Practitioner validation is described as a possible separately authorized follow-on, not authorization to contact anyone. The learning sequence asks the user to explain and challenge the evidence; it does not infer understanding from the report/dashboard or prescribe a startup, employer or investment. The referenced thesis register and guided walkthrough exist in the repository.

## Assembly and navigation checks

Read-only checks imported the report builder without invoking its write routine. Each follow-up's source text, after the builder's documented heading and relative-link transformation, appears **exactly once** in the current generated report. The two executive additions also appear exactly as transformed. Placement is:

- Learning-data economics follows the capability/learning chapter.
- Hospital support denominators follows the customer/adoption chapter.
- Benchmark reproducibility and transaction authority follows the digital-ecosystem chapter.
- Non-Spot operator evidence follows the physical-supply/embodiment chapter.

All four paired JSON packages are explicitly marked accepted in `data/package_index.json`. This index check establishes integration status, not source truth; the source dossiers have their own reviews.

The generated report contains 34 local Markdown link occurrences with 29 distinct local file targets; all resolve. Follow-up links to `../data/` are correctly rebased to the report root, and research-chapter links point into `research/`. The report includes a direct authoritative-analysis link for each inserted follow-up. External primary URLs are preserved from the accepted chapters; their current network availability was not independently retested in this integration review.

The report remains identified as an interim campaign edition. Full inclusion of the follow-ups does not claim completion of the seven-day program, uninterrupted compute, calibrated market productivity or unavailable operating-cost evidence. The full-source treatment satisfies the requested fuller report format without changing those evidentiary qualifications.

## Reviewed file identities and limits

SHA-256 of the integration artifacts inspected before the later experimental-section edit:

```text
scripts/build_report.py           19cca35cf69147ca3aedb3495bc041ee0aab03b3b8054d6a7a4fb6e09079772e
research/integrated_decisions.md   5b7f6b6fe46803a0234e9d4cf85f18bbce32c7e6f427f13d021ef73a4515e05c
REPORT.md                        c3f6c85643a1fe34dbe53e17aa276d2b31431c9f29cc12a3a84d870ad1baa4aa
```

During review closure, the lead added a separate experimental section to the builder. The resulting builder hash is `2cfa5cdaa144e22809c945d3bea71f75fdded114920a422342d908894269fa3c`; `REPORT.md` and the executive chapter remained at the hashes above. A read-only recheck confirmed the original four follow-up transformations still match the report exactly once. The new experimental builder block was not yet materialized in the report and is excluded from this disposition; its wording and exported witnesses require the separate treasury/coordination review handoff.

This is an integration review against accepted dossiers, not a new primary-source review of every underlying assertion. It does not certify untouched chapters, current scenario numerical outputs, later treasury/coordination execution results, complete shared-engine validation, or publication. No builder, report, executive chapter or source dossier was edited by the reviewer, and no report rebuild or publication was performed. The requested serving model/reasoning configuration remains independently unverifiable.

## Addendum: materialized experimental section

The lead subsequently authorized review of section 9, now present in the **33,391-word** report. This addendum supersedes the earlier exclusion of that section only. **Disposition: pass after one low-severity wording correction.** The rest of the original scope and its source-audit limits remain unchanged.

The lead changed “a profitable order” to “a positive assumed spread can coexist with a cash shortfall” at the reviewer's request. This accurately describes the hypothetical start/sale difference without implying lifecycle profit or produced physical output. The section now explicitly notes the missing automatic payment scheduler, credit-maturity collection/default and interest accrual, in addition to shared physical allocation, service withdrawal, recovery and reinvestment.

The separate [treasury review](treasury_core_review.md) passed 22 owner tests and nine independent adversarial tests. Section 9's six selected-actor closing balances match the stored financial snapshots: 30,000; 50,000; 88,000; 30,000; 8,000; and zero USD. It labels funded and unfunded paths as alternative worlds and identifies yield and fee cases as financial portions only. An invoice naming an accepted sale is a stipulated financial fixture, not a simulated acceptance test. The text does not claim a shared physical engine or available real financing.

The coordination interpretation was checked against [the accepted fixture methods](../model/COORDINATION_TRANSACTION_FIXTURE.md) and [its independent review](coordination_fixture_review.md). Its eight displayed traces agree with the exports. The weak naive baseline, added authoritative lookup and dispatch-finality assumptions, null naive completion credit, retained uncertainty, irreversible partial effects and absence of RMF/ROS execution remain explicit. This addendum independently reproduced the exported results but did not redo the other reviewer's full protocol/fault audit. It assigns no incident probability, physical output, elapsed time, wage saving or deployment benefit to the synthetic effect units.

The short calculation-trace paragraph is supported by [the independent lineage review](lineage_review.md). It preserves the four matched annual-site branches at the final horizon, excludes learned increments, distinguishes the display year from the traced comparison, and acknowledges incomplete result-specific lineage elsewhere. The cited reviewer independently tested the stale-scenario race correction. This integration review did not repeat the browser/layout or API security checks and does not extend those findings to the underlying economic assumptions.

Read-only reproduction called `scripts/export_experiments.exports()` without invoking its file writer. Both saved packets exactly match fresh results after JSON normalization, and their recorded source hashes match current code bytes. The builder checks those hashes before including experiment results. That check detects a changed source file against a retained packet; it is not a signature, a complete provenance chain, or protection against concurrent code replacement. No new financial or coordination formula appears in the builder; finance amounts are formatted from integer-cent balances.

The four complete follow-up transformations still each occur exactly once after expansion. The final report has **40 local Markdown link occurrences and 35 distinct local file targets**; all resolve after creation of the linked treasury review. The executive chapter is unchanged at its earlier reviewed hash. No source conflict, denominator limitation or calibrated numeric assumption was changed by these additions.

Final integration snapshot SHA-256:

```text
scripts/build_report.py                 724fd07acd99b46b40f0f05dc0dcddc39a8ed5a960160879af1747d974447d94
scripts/export_experiments.py           5382d46397fb902cf45f96b75610de0cc8ca558f27324db25e51446ff3c5bc38
REPORT.md                              ab26396fabdf64ae5e843023e5d0d6e8be79e283c40aa5ec6ff38e7f4e675e81
research/integrated_decisions.md        5b7f6b6fe46803a0234e9d4cf85f18bbce32c7e6f427f13d021ef73a4515e05c
model/results/treasury_witnesses.json   3818ca949adf6d2bc8cf981ca105dd2092fcf15713a3aded18ac3cbff3765a36
model/results/coordination_witnesses.json 02dc502e2dd17cceede6009dc1c89f356ec2ae0b1afb7ab3ad611175b34b62b4
reviews/coordination_fixture_review.md  86458201894d4d85a37ce23a7aaa69e48efda3284681ec694f0a4af738717812
```

No report, builder, exporter, implementation or source dossier was edited by this reviewer. This is acceptance of accurate integration at the recorded snapshot, not publication or completion of the campaign.

## Final addendum: edition 0.4 integration

The lead authorized a final bounded recheck of the **36,045-word edition 0.4**: the onboard-workload follow-up and one new executive paragraph; section 8's high-memory correction and proposed digital trajectories; section 9's six monthly-deployment rows and interpretation; and the evidence-filter note. **Disposition: pass. No integration correction is required.** This supersedes the earlier snapshot hashes and counts for these integration artifacts, without expanding into a new source audit of every report chapter.

The onboard analysis appears in full exactly once within the digital-infrastructure chapter. Its paired package is explicitly accepted. The executive paragraph accurately describes an inspectable recipe and vendor-reported component-sum speed improvement while preserving missing sustained sensor-to-actuator deadlines, runtime memory headroom, environmental conditions and target accepted service. It does not transfer the benchmark to a named Unitree configuration or infer robot throughput from the reciprocal median.

The integrated follow-up retains the tutorial-versus-patch timing conflict, separate `libero_10` timing and LIBERO Spatial success populations, repeated-observation default, warm-up discrepancy, incomplete run provenance, disk-storage versus runtime-memory distinction, and PyTorch-server/TensorRT-wrapper limitation. Static patch applicability remains separate from runtime reproduction. This recheck read the accepted dossier and [its independent primary-source review](onboard_qualification_review.md); no primary source was fetched again.

Section 8 accurately reports the accepted correction to the synthetic high-memory comparison: an omitted 800 USD annual charge is restored to C10, reducing the overstated interaction by the same amount. The conditional 832 USD witness includes 2,000 hours of additional power at the specified rate; it is not a measured board cost. The report distinguishes unchanged standard-preset numerical fields from regenerated version/provenance hashes. These statements match [the independent correction review](high_memory_cost_review.md), whose corrected engine hash matches the current engine.

The trajectory paragraph correctly calls the next extension a reviewed design with point witnesses and **no implemented annual trajectory runner**. It preserves three separate paths—human time reduction, signed robot coordination and robot digital-service expense—and requires contemporaneous values throughout admission and operation. It does not claim token-use, failed-attempt or latency economics. Constant-path compatibility, stock preservation, adverse/nonmonotone paths and separation from deployment-mediated learning remain requirements for future implementation. The all-vintage upgrade convention, current-condition screening and separate initial-year commercial/monthly-entry reference remain limitations. This conclusion relies on [the independent design review](digital_trajectory_design_review.md), not on a new execution of the proposed paths.

The monthly section agrees with [the completed stage 2 review](monthly_deployment_review.md). All six table rows exactly reproduce final-month physical stocks, provider cash and per-operator rational output from the exported artifact. The heading says **last-month** output, so witness 8's table value 100 does not conflict with the separately explained first-month output 25. The static allocation table's incumbent 250 and entrant 25 are separate operator outputs in one common stock pool; each table row remains an alternative constructed world rather than additive fleet evidence.

The interpretation preserves paid start/acceptance/shipment/commissioning phases, sunk rejected-unit costs, zero output from unfunded transit, one first-month ramp, strict existing-support priority and the phase-4 receipt restriction. It distinguishes cancellable unperformed prepayments from previously earned obligations. Static assignment is explicitly separate from ENTRY-FG-01, customer competition and entrant returns. The text does not turn paid physical progress into a company-wide mandatory-payment/default/recovery scheduler, operator-cash model, title contract or autonomous investment policy. The full shared-treasury/entrant requirement remains partial.

The evidence-filter paragraph matches [the independent facet review](evidence_facets_review.md) and the filter methods. It describes exact source fields, selectable missingness and compound values, preserves artifact-license limits, and makes no scenario-population or empirical-value change. Dedicated resource-grade filtering and comprehensive typed joins remain incomplete.

Read-only checks confirmed:

- All **five complete follow-ups** and the current executive chapter each appear exactly once after the builder's documented transformation.
- All **three experiment packets** exactly equal fresh authoritative function results after JSON normalization. Their primary code hashes and every declared dependency hash match current files. The monthly packet explicitly includes both `monthly_deployment.py` and `treasury.py`.
- Every one of the **six monthly table rows** matches the exported final-month stocks, cash and exact rational service, without a new economic formula in the builder.
- All **49 local Markdown link occurrences**, comprising **43 distinct local file targets**, resolve.

The exporter was imported and its return values compared without invoking its file writer. The report was not rebuilt by this reviewer. The builder's hash checks detect changed declared code/dependency bytes against these packets; they do not authenticate artifacts, establish complete transitive dependencies for arbitrary future modules, or guarantee an atomic hot-reload snapshot.

Final edition 0.4 SHA-256 identities:

```text
REPORT.md                               f70a6a72ad5126b055ac7ba61d5be95b12459802410ae1948d2733cace3c85bc
scripts/build_report.py                  7280630b7fc836e3041726ba447dc15b3d11fa8873422ef4173d68a2f12f0337
scripts/export_experiments.py            ee31b252baad52634face201b46536b17b313ca2d64461bfd73607f479508a1e
research/integrated_decisions.md         f7d8e2ceab3974773666f1ecd6a1408b0915d2c889031ba92178ec57b4889e42
research/onboard_workload_qualification.md ce6a6a7a6d067eb78b55760efcf45c92fa2d349734b9bab91f33d3ce9eaace32
research/digital_trajectory_design.md    142ca7bfb5b478f2ef1885700b6809720cb0c8232cb22e4fd44206ec9eb5d16f
model/engine.py                         0c35c6f2602d29a60a6bc187c013c0e4dd9a3597064cf67bed5a1ecc616a8d07
model/results/treasury_witnesses.json    164ed55dc23dbee6d65d62d2e46f9fbd1d04ff43602474680d3b3721fdc5b9cc
model/results/coordination_witnesses.json 9e3a63f4368a3c21f4ec1cd0f55e6b51ea30402facc1e66ac7b45a983b774fd5
model/results/monthly_deployment_witnesses.json 4a388bff561ed890460a048787a38e3882f5aebe63ea0cf7aadd5a725fc20e15
dashboard/EVIDENCE_FILTERS.md            6283d764dca6369eaaf3f35fac444f9fc17c8ad2c21a0a86e068640c6babdfff
```

This final addendum accepts the specified report integration at the recorded snapshot. It does not claim a new whole-report primary-source audit, a completed trajectory implementation, full company/physical-engine validation, empirical calibration, browser certification or publication. No further work is required for this bounded integration review.
