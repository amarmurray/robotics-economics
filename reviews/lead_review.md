# Lead integration review — checkpoint 0.1

This is the integrator's review, not a substitute for the independent specialist reviews. Reviewed scope: early common-engine design, source-version consistency, and infrastructure source implications. The campaign remains in progress.

## Corrections requested and disposition

| Finding | Why it matters | Disposition |
| --- | --- | --- |
| Model originally valued released human time as customer cash savings without a separate avoidability assumption | Released time does not establish removed staffing or cash; this changes economic eligibility and payback | Implementation owner added explicit synthetic `labor_avoidability` control, default0.75; observed payroll removal remains unknown. Independent code review and adverse tests still required. |
| Continuous fractional robots/sites could be mistaken for a physically executable fleet plan | A cohort relaxation supports comparative mechanisms but not integer commissioning decisions | Implementation owner agreed to persistent continuous-relaxation labeling and methods disclosure. |
| Annual capital budgets could be mistaken for endogenous reinvestment from operating cash | Fresh exogenous funding and internally generated deployable cash are different constraints | Implementation owner disclosed fixed annual envelopes and lack of operating-cash reinvestment as a limitation. This remains partial against the full dynamic-financing scope. |
| H agent-coordination source changed between January blog and July peer-reviewed paper | Earlier sample/model statistics cannot be silently used as the current result | Lead independently fetched July24 Nature article, DOI10.1038/s42256-026-01268-y. Confirmed260 configurations/six benchmarks, CV R²0.373/0.413,87% within-domain architecture selection and94% sign prediction in16 validation configurations. The ~45% rule is not a universal scaling law; underlying interaction fails cluster-robust correction. H owner preserving correction. |
| Infrastructure numerical specs were in prose but absent from structured quantity arrays | Export and machine inspection could miss units, population and manufacturer-spec status | Independent reviewer flagged; lead added memory/bandwidth and module-power arrays to HI-003/004/005, with all HI quantities carrying population and period. No scenario coefficient assigned. |
| Atlas arithmetic must be reproducible from saved source rows | A narrative aggregate should not become a second opaque calculation source | Implementation owner asked to validate/export employment/residual and occupation-screen calculations from saved evidence. Pending. |

## Source/inference boundaries accepted

IEA485TWh for2025 is a historical estimate of total data-center electricity use;950TWh in2030 is a central projection. TSMC expenditure and wafer-equivalent shipments are not robot-component allocations. Micron deposits and future revenue are not additive value, and initial fab output differs from subsequent ramp. Orin/T5000/H200 specifications describe different memory/configuration classes; headline compute numbers do not establish matched robotics throughput.

The independent reviewers must inspect the underlying field and contractual sources, not just count records. In particular, the hospital intervention category discrepancy, trial-versus-routine-use classification, PG&E image acceptance, and artifact-specific rights remain consequential checks. Synthetic outputs must remain excluded from empirical labor and deployment aggregates.

## Publication metadata boundary

At integration, the lead replaced the exact observed launch repository commit in shared research/model metadata with a pointer to ignored `sync_receipt.json`, following AGENTS.md's operational-record rule. No source claim, numerical assumption or engine calculation changed. Exports were regenerated because catalog/evidence fingerprints changed. Initial and recheck hashes in independent reviews identify their reviewed snapshots; the publication manifest supplies final artifact hashes after this metadata-only cleanup and trailing-whitespace normalization. CSV export uses LF line endings; values and parsing are unchanged. The durable campaign T0/deadline remain in the handoff so resumption cannot silently restart the week.
