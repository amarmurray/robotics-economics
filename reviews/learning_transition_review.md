# Independent review of the learning transition

Review date: 25 October 2026. Reviewed root-owned [LEARNING_WALKTHROUGH.md](../LEARNING_WALKTHROUGH.md) and [THESIS_REGISTER.md](../THESIS_REGISTER.md) against [POST_RESEARCH_STAGING.md](../POST_RESEARCH_STAGING.md), the actual dashboard controls, the common engine, current scenario outputs and the accepted research dossiers. The observed repository state remains in ignored `sync_receipt.json`.

**Final disposition: suitable as interpretation aids for the verified early edition after the owner corrections rechecked below.** No remaining blocking false empirical claim, automatic stage activation or unexecutable exercise was found within this scope. Two control-interpretation issues and one implementation-status ambiguity were corrected by the document owner. This is not certification of completed intellectual mastery, a finished campaign, a calibrated deployment decision or a deployed physical coordination system.

Rechecked content SHA-256:

| Artifact | SHA-256 |
| --- | --- |
| Walkthrough | `d88f3ff9c45a18c5aa4dead2d530fa890208db91fda65f772b5bff7e5e626a60` |
| Thesis register | `41bc9cedd8f97bb468785f65379bfa1dcf69245890587fe13529b4e3e730f079` |
| Accepted staging plan | `3c3112ecd84f897f38eff04e25114dadc73075a492e1a522a9505f052f06e645` |
| Dashboard JavaScript | `a92f894e68b54dfdb82f2005c181e51b868ed85ee87eb27419b231fb5ffeb88c` |
| Common engine | `d31f2b93a639b24b288f9a4c5915a05bd342a63c28e02e75ff8407db2c411f0f` |
| Model assumptions | `a71044379485dfe1fd1fd87cfd81f6f5ecde80047911fbb8f843a9d30b82c965` |

## Corrections found and resolved

**Medium — changing a global support budget does not isolate a shock to an already-installed fleet.** The original walkthrough §2 asked the learner to reduce support and distinguish installed from supported robots without explaining that the control reruns the entire history. The actual control is `support_budget_hours` in `dashboard/app.js` under “Shared deployment resources”; every change posts a fresh scenario to `/api/run`. There is no time-indexed support-shock control.

I executed the reference with only support reduced from 12,000 to 3,500 hours/year. Final stock fell from 44 to approximately 11.23, while every positive-stock row retained a supported fraction of 1. The result demonstrates constrained admissions/commissioning in this run, not withdrawal of support from a fixed historical fleet. The owner now explicitly says the whole history is recalculated, admissions may fall, and a time-specific support shock is unimplemented. **Resolved.** The underlying installed-versus-supported distinction remains a valid accounting concept.

**Medium — the digital-first saved preset changes two channels.** The original §3 comparison could be read as isolating the improving human comparator. In `model/assumptions.json`, `digital_first` sets both `digital_efficiency = 0.35` and `coordination = 0.2`. The first changes human time in both the comparator and the robot site's retained work; the second changes robot output. A difference between the saved presets cannot identify either channel alone.

The owner now directs the learner to start from reference, change only **Human time reduction**, hold **Robot scheduling change** fixed, and trace both human-work effects before inspecting the combined preset. Those are actual UI controls. The two-channel qualification is explicit. **Resolved.** This remains scenario mechanism analysis, not causal identification from field data.

**Low — “reviewed executable design” could imply implemented treasury functionality.** Original thesis T6 used that phrase for a design proposal. `model/treasury_extension_design.md` explicitly says “Not implemented or calibrated”; its witnesses are specifications for future tests. The owner changed T6 to “reviewed implementation proposal and exact test witnesses.” The walkthrough already separates the monthly entrant from the annual shared-resource model and names the treasury extension as unimplemented. **Resolved.**

## Executability and model-boundary checks

I inspected the actual view names, control definitions, event handlers, evidence dialogs, preset definitions and reference-table scope in `dashboard/app.js`. I called the common CPU engine directly for the relevant examples, and the running localhost API returned the accepted evidence catalog and successfully recalculated both zero cash avoidability and reduced support. I did not repeat a visual/browser interaction audit; the existing [browser review](browser_review.md) is separate evidence for rendering and click behavior.

| Walkthrough exercise | Check result and boundary |
| --- | --- |
| Economic atlas and selected cells | **Pass.** The view exposes the six synthetic cells and separate observed employment/occupation references. The distinction between overlapping populations and unknown physical-work hours matches the atlas/model methods. Accepted service and buyer questions require interpretation of dossier evidence, not invented fields in the employment totals. |
| Delayed supply versus reference | **Pass.** Fresh engine outputs reproduce final stock 60 versus 44, but cumulative baseline-equivalent hours approximately 249,690 versus 376,256. These are synthetic source-engine results. The stated retirement/exposure explanation is consistent with the cohort model and the dashboard warning. The comparison button in “Scenarios & evidence” reports cumulative output; “Fleet & bottlenecks” provides stock/commissioning/retirement paths. |
| Cash avoidability set to zero | **Pass.** The real control is “Released labor value avoided as cash.” Direct and API runs return zero economic readiness and zero deployed stock for this reference, while the matched resource-cost table is unchanged. This demonstrates the scenario cash gate, not that released time can never have value. |
| Four-way comparison and interaction | **Pass.** `C01 − C11` and `C11 − C10 − C01 + C00` match `joint_comparisons` and METHODS.md. The annual-year selector does not change the fixed final-horizon table. A negative cost interaction has the stated complementary-cost interpretation; no causal estimate is claimed. |
| Customer profiles with technical controls fixed | **Pass.** Profiles change approval delay, site authority, cash ceiling, implementation slots and payback criterion. Fresh constrained/integrated runs change deployment while keeping the six matched resource-cost values unchanged. The label is not a productivity multiplier. |
| Commercial arrangements and same-robot entrant | **Pass.** Sale/lease/RaaS choices and ownership/cash-allocation records exist. The two saved RaaS cases give funding gaps of zero versus $116,000 under the synthetic $600,000 commitment. Their annual fleet results are identical to each other. The monthly entrant is a separate reference; later negative-cash rows remain conditional additional-funding paths, not executed solvent operations. |
| Hospital/TenneT evidence exercise | **Pass.** “Market deployment” exposes hospital denominator/conflict cards; “Embodiment & deployment” exposes the hospital and quadruped follow-ups. Accepted packages are present in the live catalog. Source dialogs/full records contain locators and limitations; evidence search can narrow the card lists. |
| Conceptual unfundable/funded-but-undeliverable examples | **Pass as explanation or hand calculation.** The question asks the learner to give cases, not run an implemented unified treasury. It must not be interpreted as proving shared entrant supply, default or provider cash reinvestment in the current engine. The surrounding text now preserves this limitation. |

For orientation, the saved scenario labels differ from some prose shorthand: `delayed_supply` appears as **Qualification and ramp delay**; `service_stress` as **Service and spare-parts stress**; `digital_first` as **Improved digital human baseline**. The intended presets exist; using these exact labels during a guided session avoids searching for nonexistent display names.

## Evidence, objections and staging

The register preserves the crucial evidence boundaries. T1 does not convert successful navigation into accepted measurement or removed staffing: PG&E's flight/imagery distinction, TenneT's selected instrument coverage and hospital handling/accompaniment are present in the accepted dossiers. T2 labels the four-way result synthetic and retains complementarity as a counterargument. T3 separates equal robot access from customer authority, retention and cash; it does not claim actual financing or obtainable market share. T4 treats pinned source code as interface evidence and explicitly withholds LLM uplift and incident-rate claims. T5 separates Cobalt's conditional compute charges from total data-production cost and retains DexWild's robot-grounding requirement. T6 does not treat synthetic financial witnesses as observed credit terms.

Every thesis has a substantive objection. No material missing counterargument requires blocking use: partial automation can have value; digital changes may complement robotics; entrants can redesign or serve unmet demand; conventional integration may already solve the coordination problem; collection may be the real bottleneck; and explicit financing can bridge a timing gap. These objections make the register useful for discussion rather than a predetermined employer, startup or acquisition case.

Two low-priority refinements would improve the next learning session without changing acceptance:

1. **Separate general accounting principles from empirical target hypotheses.** T1's service boundary and T6's cash/economic distinction are largely structural constraints. Their “what changes the view” observations can change a particular deployment choice, but cannot falsify the accounting distinction itself. When using walkthrough §6, add a target cell, alternative, outcome and predicted direction to one chosen thesis. For example, ask whether residual inspection work prevents a particular human visit from being removed, rather than whether motion and service are conceptually different. Keep the broad principle as a checklist and the narrowed statement as the testable thesis.
2. **Keep the local fixture's outcome inside its boundary.** T4's proposed local software fixture can establish state consistency and modeled performance under specified delays/failures. It cannot by itself establish physical accepted throughput or operator labor-cost savings. The register already withholds LLM uplift; make this source/target step explicit when selecting the eventual experiment.

The staging plan allows overlap and explicitly rejects a mandatory seven-day wait. The walkthrough appropriately starts comprehension with the available verified early edition while keeping the campaign and gaps open. Its conclusion does not initiate practitioner outreach, publish private work, select an employer or commit to a startup. The register likewise treats practitioner questions as preparation requiring separate authorization before contact. No stage 5–7 action, reminder deadline or presumed completion has been introduced.

## Scope of this review

The original inspected walkthrough hash was `3514cc73e8e6c67dc934b6bc2dcd43a2986af970d0f7c4811d3987dba4202fde`; original register hash was `c8709a71cc76f47ae38ae99c8bad8b2dc5e06c62077f752d747b7ce133ea15da`. The owner applied the three corrections above, and I re-read their final wording at the hashes listed first. I edited only this separate review artifact.

This review crosschecked the interpretation aids against accepted research and implementations. It did not independently re-certify every underlying external source, repeat hardware/benchmark experiments, run the future treasury tests, audit every crossfilter, or establish that Amar has completed an exercise. The requested Astra/Ultra configuration is not independently observable; no serving-model identity is claimed.
