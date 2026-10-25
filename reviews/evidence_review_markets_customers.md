# Independent evidence review: markets and customer organization

Review date: 2026-10-25. Reviewer: capability/learning specialist, independent of the A/C and F/G authors. Reviewed `research/economic_atlas.md`, `data/market_evidence.json` v0.1.1, `research/customer_value.md`, and `data/customer_evidence.json`. This review does not assess the reviewer's B/D/E files or certify the common numerical engine. Requested Astra Ultra settings remain unverifiable from the delegated runtime.

**Disposition: no high- or medium-severity correction found in the material claims checked.** The sources support the dossiers' bounded conclusions, with explicit limits on labor conversion, hospital generalization, rights, financing and productive capacity. Two low-severity precision improvements were sent to the authors and lead. Unresolved source conflicts remain unresolved; they were not silently corrected.

## Findings requiring precision, not a change in conclusion

| ID / severity | Finding | Requested disposition |
| --- | --- | --- |
| ACFG-01 / low | `accounting.rounding_residual_thousands = 0.0` matches the all-jobs reconciliation. The wage/salary subtotal is 160,458.5 thousand versus the displayed BLS total of 160,458.6, a difference of −0.1 thousand. The narrative correctly discloses that rounding tolerance, but the single field could be misread as applying to both comparisons. | Prefer separate named wage/salary and all-jobs residuals, or an explicit denominator for the existing field. No market employment value needs correction. |
| ACFG-02 / low | BrainOS agreement §5.2 excludes aggregated data not linked to the end user from the defined term “Operational Data.” End-user ownership therefore should not be read as extending to every derived or aggregated dataset. Existing text correctly separates ownership from improvement rights and practical access. | Add this definition boundary to FG-E008 or the rights discussion. Preserve the conclusion that title does not establish exclusivity or a realized learning benefit. |

Both findings were delivered to the relevant author and lead before review completion. They do not invalidate the present first-wave conclusion or authorize automatic model coefficients.

**Closure check:** the authors applied both precision improvements, and the reviewer inspected the resulting fields/text. A/C v0.1.2 records a wage/salary residual of **+0.1 thousand** with the explicit convention **reported total minus displayed components**, and an all-jobs residual of zero. This is the opposite sign convention to the subtotal-minus-reference comparison above, with the same arithmetic. F/G v0.1.1 records the aggregated/unlinked-data exclusion and excludes personal data from Operational Data. Both low findings are closed; no material claim or numerical baseline changed.

## BLS source, scope and arithmetic checks

Independently retrieved the [major-industry sector table](https://www.bls.gov/emp/tables/employment-by-major-industry-sector.htm), [detailed industry table](https://www.bls.gov/emp/tables/industry-employment-and-output.htm), and [OEWS Table 1](https://www.bls.gov/news.release/ocwage.t01.htm) directly on 2026-10-25. Also checked [definitions](https://www.bls.gov/emp/documentation/definitions.htm) and the [May 2025 OEWS technical note](https://www.bls.gov/oes/2025/may/oes_tec.htm) through primary-page retrieval. Locators: Tables 2.1 and 2.2, retained matrix codes in the JSON; Table 1 named major occupation rows; technical note scope, occupational/industry coding, wage and estimation sections. These are 2025 employment estimates with 2035 projections in adjacent columns; the future columns are not realized output.

A separate parser compared **all 59 retained sector/detail employment rows** against freshly downloaded source HTML: zero mismatches. It recomputed all **15 market aggregations and three explicit residual aggregations** using the saved source-row references: zero mismatches or missing references. The results, in thousand jobs, are:

```text
15 selected market families                       128,979.5
Other business industries (51, 52, 53, 54, 55)      25,460.8
Other administrative/support                        6,018.2
Wage/salary reconstruction                        160,458.5
Displayed BLS wage/salary total                   160,458.6
Unallocated unincorporated self-employment           9,822.3
Reconstructed all-jobs total                      170,280.8
Displayed BLS all-jobs total                      170,280.8
```

The ownership crosswalk is appropriate: M10 uses **private** healthcare/social assistance; M14 includes private education plus federal and state/local government. The detailed hospital context, 6,818.4 thousand all-ownership jobs, decomposes into 5,653.8 private and 1,164.6 state/local. It is marked nonadditive and is not added to both markets. M08's codes are 48, 492 and 493, preserving the source's exclusion of postal service from this sector. M11's facilities-support plus buildings/dwellings aggregate is broader than floor cleaning, as disclosed. Outsourced service activity remains at the employer industry until a destination allocation exists; it is not counted again at the customer.

All eight selected OEWS employment and mean-hourly-wage pairs match the source. Their sum is **61,320,140**, divided by **155,495,730**, or **39.4352565%**. This is an analyst-selected occupation screen, not measured physical hours, exclusively physical employment, or an automatable share. OEWS uses 2018 SOC and 2022 NAICS and six panels from November 2022 through May 2025. It excludes most agriculture, private households, self-employment and unpaid family work; it includes full- and part-time jobs. Straight-time wages omit employer benefits and several premiums. The 2,080-hour wage annualization convention is not evidence of actual annual hours. The dossiers preserve those boundaries; all 15 market physical-work-hour fields and all eight occupation physical-share fields remain null. There is no justified employment-to-robot-hour conversion in this edition.

## Hospital capability, urgency and support

Independently retrieved both operator-authored papers on 2026-10-25:

- [Birkhoff et al., 2024-12-01](https://pmc.ncbi.nlm.nih.gov/articles/PMC11892717/), Abstract, Design and Sample, Results, and autonomy/functionality themes. The observation period is November–December **2022**, not 2024 or 2026. The purposeful qualitative sample covers 23 sessions, 33 observer-hours and 89 end-to-end deliveries at one 900-bed hospital. The paper reports 107 interventions; the listed categories are 72 elevator, 20 door, 4 obstacle, 7 staff-use, 7 mislocalization and 1 unloading-staff event, totaling **111**. Overlap or reporting error is not resolved by the paper. The dossier correctly retains both and does not calculate a current platform intervention rate. Dedicated Clinical Robot Associate assistance, staff loading/unloading and elevator/door support are real complements. Observer-hours are not automatically fleet operating-hours or paid support-hours.
- [Smith and Weber, 2026-03-31](https://pmc.ncbi.nlm.nih.gov/articles/PMC13048758/), Abstract, Nurses Shaping Robotic Innovation, and the paragraph beginning “By the end of the grant period.” The retrospective 2022–2025 pilot describes three cobots, more than 80 patient-care areas and more than 48,600 cumulative deliveries. It explicitly distinguishes value in high-volume, **nonurgent** medication/equipment delivery from inability to meaningfully augment complex, time-sensitive nursing workflows. Nurses infrequently initiated requests because urgency and informal coordination were difficult to automate. The $1.5 million is grant-program funding, not a robot purchase price or complete cost estimate.

Neither paper establishes nursing payroll reduction, a generally applicable support ratio, audited unit economics, current 2026 retained productive fleet, or a controlled human-versus-robot cost comparison. The positive cumulative delivery count and the workflow limitation coexist. The dossier represents both rather than selecting only the favorable count or only the early support burden.

## Commercial terms and data rights

Independently retrieved [ABM FY2025 Form 10-K Note 2](https://www.sec.gov/Archives/edgar/data/771497/000077149725000031/R10.htm) on 2026-10-25. Locator: Revenue Recognition, Identifying the Contract. The text says most contracts are cancellable by either party without substantive penalty and the majority have **30–90 days' notice**. Where a cancellation clause exists, remaining accounting contract term is limited to the termination-notice period. This supports an asset/customer-commitment mismatch mechanism. It does not establish observed customer lifetime, a robot supplier's contract duration, or the terms of an ISS or GXO customer. The dossier explicitly retains these distinctions.

Independently fetched the [Kärcher-hosted BrainOS Subscription Agreement](https://s1.kaercher-media.com/media/file/261106/kira-b100-eula-2-2025.pdf), including direct PDF download and metadata inspection, on 2026-10-25. Locators: §§4.1–4.3, 5.2, 6 and 10.3. Software is licensed rather than sold; the license depends on service access. Section 5.2 gives the end user ownership of defined Operational Data while granting Brain limited-purpose, perpetual, nonexclusive, sublicensable, transferable, irrevocable worldwide storage/use/copy rights for service obligations and development/improvement of software, services, robots and other products/services. Other use requires prior written consent. Data export is not automatically assured; it depends on the subscription schedule. The aggregated/unlinked exclusion is ACFG-02 above.

PDF metadata independently confirms title `Brain Corp - EULA_Karcher Subscription Agreement v2021_12`, creation **2022-03-31 17:10:04 UTC**, and modification **2025-02-18 22:05:44 UTC**. Those artifact timestamps explain neither a legally effective version nor a customer's executed terms. The filename `2-2025` and metadata must not be used to invent an effective date. FG-E008 correctly keeps publication/effective date unresolved and does not apply this standard form to Digit, GXO, ISS or every Tennant agreement. Improvement permission proves neither useful data nor improved performance nor exclusive value capture.

## Company-stage and financing boundaries

Primary company disclosures retrieved independently on 2026-10-25:

| Source and locator | What is supported | Boundary preserved by the dossier |
| --- | --- | --- |
| [OpenAI, 2025-12-01](https://openai.com/index/thrive-holdings/), opening partnership paragraphs | Ownership stake, embedded technical collaboration, and Thrive investing in, acquiring and building businesses; initial accounting/IT focus. | No disclosed stake size, governance, data exclusivity, realized productivity or physical-robot economics. |
| [Thrive, 2026-08-12](https://www.thriveholdings.com/thrive-holdings-fundraise), first four substantive paragraphs | Issuer reports >$2 billion new capital at $12 billion valuation, >$3 billion cumulative capital and >70 owned/operated businesses; new built-environment technical/regulatory platform. | Valuation is not cash or return; acquisitions are not automatically new productive capacity; technical/regulatory services are not robotic construction. No financing parameter for a hypothetical newco follows. |
| [Hadrian, 2025-07-17](https://www.hadrian.co/blog/series-c), financing paragraphs, expansion bullets and About | Issuer-described operating Torrance factory, proprietary Opus stack, $260 million financing headline and expansion loan facility; Arizona expansion and January 2026 operational timing announced prospectively. | This historical announcement does not verify achieved January 2026 ramp or current exposure. Ambiguous equity/debt wording does not justify adding an invented loan amount to the headline. Defense programs/proprietary technology limit the common-robot analogy. |

The customer comparisons hold technical service/output conditions fixed and identify organizational mechanisms rather than ownership multipliers. The synthetic entrant case is labeled a scenario, with normalized service units and no automatically available future financing. The narrative distinguishes contribution, cash survival and actual capital availability; acquired output, incumbent-share transfer and new demand are not conflated. Provider payment cancels correctly in the displayed consolidated identity; depreciation is not duplicated as cash. The common engine's implementation of these statements remains a separate model review.

## Join checks, reviewed snapshot and limits

Read-only checks found all 66 A/C evidence references resolved. F/G checks resolved 90 evidence references, 29 cell joins and 12 actor-role joins. These checks establish referential integrity, not truth of every field.

Reviewed input SHA-256 values before optional author precision edits:

```text
research/economic_atlas.md   48664447e5af98543d36debebecb023cde9f14c45c2d5e34e9a0bb040857e6b5
data/market_evidence.json    200339dc49776aee44f403cec0d64d11e93e549e8439aceb413cc81e54ecf477
research/customer_value.md   369535c2194521bab7d6188feb9e9248d15dd30e9248714dc6787994450e509b
data/customer_evidence.json  664457e023083276cb2922677cdc4813e97f2dd83c1b2a1efc0821f48ab67de9
```

After the inspected precision corrections, changed-file hashes are:

```text
data/market_evidence.json    1e07ecc6af0cf46b2aac63cb89727cdd4d056b5a1eb5d81e94e25aa2229ed6b2
research/customer_value.md   408be6c9256324910a540287a40e9f0bc0c0b245e38042702052907f60131bca
data/customer_evidence.json  e6cc60fcea1975808f6a812ed3e5d71b6941b7a36885ba8769eced852cb89af6
```

This bounded review stops after the assigned material claims. It does not certify all market screens, every secondary citation, current commercial renewal/termination, private financing availability or undisclosed contract terms. Raw downloaded sources were used for verification and are not republished in tracked files. No reviewed dossier, evidence file, model or shared integration artifact was edited by this review.
