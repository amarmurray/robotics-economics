# Hospital logistics: what the support denominators actually measure

Bounded second-wave findings · 25 October 2026 · Version 0.1.1
Evidence and reproducible arithmetic: [field_support_denominators.json](../data/field_support_denominators.json). The existing [capability dossier](capability_learning.md) and its evidence package remain frozen. Requested Astra Ultra settings cannot be independently verified from this delegated runtime.

Two additional primary hospital studies improve the evidence beyond cumulative delivery announcements. One identifies the people present during a mission while defining success as occurring without any human intervention; that wording needs interpretation alongside the staffed workflow. The other compares transport phases with manual delivery over six months. Neither yet supplies a verified, complete labor-cost denominator. The useful advance is a sharper distinction between **a mission without correction, a delivery with human handling and supervision, and a service with lower total paid support**.

The endoscope study's published means support two arithmetic contrasts: AMR-assisted distribution is **56.41 seconds, or 33.48%, lower** than the manual distribution mean; retrieval is **21.36 seconds, or 23.39%, lower**. These are transport-phase comparisons, not staffing savings. The medication-delivery study also exposes a new internal count conflict: 108 completed missions out of 122 eligible implies 88.52%, whereas the paper reports 87.03% overall success. Both numbers are retained; neither is silently repaired into a calibration input.

The cases concern specialized wheeled transport in South Korea and China. They inform the mechanisms and comparator for the US hospital-logistics cell, `CELL-M10-hospital-logistics-US-2025`; their measured values are not transferred to US nursing labor or humanoid performance. No common-model parameter changes are made.

## 1. Guro medication delivery: corrective intervention is only one part of support

[Lee et al., Digital Health](https://pmc.ncbi.nlm.nih.gov/articles/PMC13039597/) studied one DOGU IROI robot on a pharmacy-to-emergency-department route at Korea University Guro Hospital. A web request, secure medication drawer and communication module integrated the robot with a shared, staff-only TK50M elevator. The robot moved from the pharmacy at B2F to the emergency department at 1F. This configured route is the unit of evidence—not hospital-wide material handling.

The primary full text and [public JATS record](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC13039597/fullTextXML) were retrieved and inspected. The JATS electronic publication date is **31 March 2026**. Search/DOI metadata giving February 2026 is not used as the authoritative publication date. Observation occurred **18–29 June 2025**.

### The matched mission cohort

Section 2.4 reports 135 logged delivery requests and excludes 13 urgent runs, leaving 122 eligible nonurgent missions: 80 weekday and 42 weekend missions. Missions were selected to cover high- and low-congestion conditions; they followed clinical demand, with inter-mission gaps ranging from six to 1,044 minutes. These are sampled missions over a calendar window. They do not establish continuously staffed robot-hours, full-fleet utilization, or a fixed number of deliveries per shift.

Section 2.4 defines success literally as the robot “completing the entire route and handing over the medication without any human intervention.” Our distinction between **corrective assistance and routine handling or safety presence** is a contextual interpretation of the human roles disclosed in sections 2.3–2.4. The paper does not formally delimit its intervention term, so the tension between that wording and the staffed workflow remains explicit. Failure includes remaining stationary for more than one minute **or** requiring manual assistance because of passenger/cargo obstruction. Consequently, a failed mission is not automatically an intervention event, and the number of failures cannot be multiplied by an assumed recovery duration.

The source identifies the human work more explicitly than most deployment announcements:

| Role or activity | What the study establishes | Missing economic denominator |
| --- | --- | --- |
| Trained accompanying operator | Accompanied the robot for medication-handling safety and recorded passenger/cargo observations. Presence also applied during the study's no-correction workflow. | Time devoted to accompaniment versus research annotation; whether/how accompaniment could be removed after validation; paid staffing allocation. |
| Pharmacist | Prepared medication, loaded the drawer and initiated delivery. | Incremental loading/interface time versus the existing courier workflow. |
| Support staff | Requested/dispatched the robot and usually retrieved medication at the destination before handing it to a nurse. | Dispatch, monitoring, retrieval and transfer minutes; concurrent work and avoidable paid time. |
| Nurse | Sometimes retrieved medication directly when support staff were unavailable. | Frequency and duration of the additional walk/interface/verification tasks. |
| Exception response | Corridor, communication and elevator-blockage failures were classified. | Recovery time, number of people, repeated attempts and ultimate medication delivery after a failed mission. |

A safety observer in a research trial does not prove permanent commercial escort requirements. It does prove that “no corrective intervention” cannot be read as “no person present” or “zero human support” for this observed sample. Conversely, keeping an escort in the cost boundary forever without further evidence would also overstate what the study establishes.

### What can be calculated—and what cannot

Section 3.2 reports 14 failures: eight elevator blockages, two elevator-call communication errors and four corridor-navigation failures. These categories sum correctly. Thus **8/14 = 57.14% of classified failures were elevator blockages**. That is a failure-composition statistic, not an intervention rate or a share of staff time. The study-selection calculation **122/135 = 90.37%** also holds for the logged request cohort; it does not estimate the eligible share of all hospital transport demand.

The overall success figures conflict. Section 2.4 gives 122 eligible missions, section 3.2 gives 14 failures, and section 3.4 analyzes 108 completed trials. Those counts are internally consistent with each other, and **108/122 = 88.52%**. Section 3.1 nevertheless states **87.03%** overall success, a difference of about 1.49 percentage points. The source does not explain a different denominator or additional exclusions. The JSON records the count-implied percentage as an **audit calculation only** and leaves the selected success probability null. Arithmetic alone cannot establish which published field is erroneous.

Another boundary remains uncertain: sections 2.6–2.6.1 describe questionnaires after a four-week testing phase, whereas mission dates span June 18–29. The relationship between these phases is not explained. No four-week robot exposure is reconstructed from the survey wording.

### Service quality and the proposed dispatch improvement

The fitted elevator-operating-rate threshold is 59.01%, and the paper reports 95.52% success in the selected lower-congestion subgroup. This is an association and a threshold fitted in the study sample. It is not a prospective experiment demonstrating the causal effect of a congestion-aware dispatch policy. Restricting dispatch to quiet periods may defer useful work or shift urgent deliveries to people. Filtering out non-elevator failures to reach approximately 100% is particularly unsuitable as an all-cause service-success claim.

Elevator waiting and travel analyses use the **108 completed trials**. Their delay relationships therefore omit the failed-mission burden and cannot determine end-to-end service time. Table 1's temporal definitions and section 3.4's shorthand are not fully identical; the package does not rebuild a mission cycle from those plots. The public paper says the underlying datasets are available from the corresponding author on request, rather than providing a retrieved mission-level dataset. No outreach was made.

The 22 survey respondents comprise seven pharmacists, seven support staff and eight nurses. Support staff report higher usability, while nurses and pharmacists acquire small handling/interface tasks. Overall NASA-TLX scores do not differ significantly across the groups. These are subjective workload comparisons, not a before/after time-and-motion estimate of labor removed. The next useful experiment would measure normal handling, accompaniment and exception recovery alongside all requested services, including urgent/manual fallbacks and deferrals.

## 2. Qilu endoscope transport: a genuine comparator with an incomplete cost boundary

[Shi et al., Gastrointestinal Endoscopy](https://www.giejournal.org/article/S0016-5107(25)02075-9/fulltext), also indexed in [PubMed](https://pubmed.ncbi.nlm.nih.gov/41076017/), reports a prospective comparison at Qilu Hospital of Shandong University. Direct [PubMed metadata](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=41076017&retmode=xml) records electronic publication on **10 October 2025** and the journal issue in May 2026. An earlier indexed publisher-history extract gave October 9, but that history was not reproduced by the current fetch; it remains a metadata discrepancy, while the directly verified PubMed date is selected. The study itself ran **21 May–21 November 2024**.

One day in each five-day week was randomly assigned to manual transport; the remaining four used AMR-assisted transport. The study included 5,393 manual and 21,048 AMR-assisted endoscope deliveries and describes a system of eight AMRs. This provides an actual manual comparator with a stated allocation procedure, unlike a robot-only cumulative counter. It is randomization by day, however; the accessible abstract does not expose adjustment for clustered observations, route mix, daily workload or within-day service conditions.

| Reported phase | Manual mean | AMR-assisted mean | Arithmetic contrast |
| --- | ---: | ---: | ---: |
| Distribution | 168.48 seconds | 112.07 seconds | 56.41 seconds lower; 33.48% of manual mean |
| Retrieval | 91.32 seconds | 69.96 seconds | 21.36 seconds lower; 23.39% of manual mean |

The abstract reports `P < .001` for each phase comparison. The calculations above simply subtract the published means and divide by the corresponding manual mean. They do not reconstruct a new significance test, a labor-saving estimate or a service throughput rate. The phases are not added together to claim person-time savings: matched pairing, failure handling and phase sample counts are unavailable from the retrieved text.

The AMR-assisted group reports a rounded delivery-failure rate of **0.15%**, compared with no unsuccessful manual deliveries. This is relevant counterevidence to reading lower mean time as dominance on every service dimension. The exact failed-delivery numerator is not reconstructed by multiplying 0.15% by 21,048; that creates a fractional count and presumes an unverified denominator. The abstract also does not reveal whether the included deliveries denote attempts or accepted completions, how failed cases enter the timing calculations, or the detailed acceptance and adverse-event rules. It does not establish autonomous endoscope reprocessing or clinical-quality equivalence merely by transporting endoscopes.

The authors report **2.18 FTE of transport workload reduction** and approximately **12.8% ROI**. These are retained as attributed findings with unaudited methods, rather than silently discarded or accepted as inputs. The public publisher page, despite its `/fulltext` path, exposed the abstract and references through retrieval; direct retrieval returned HTTP 403. The detailed FTE-hours convention, measured support tasks, maintenance allocation, price, depreciation/financing boundary and ROI horizon were not verified. Workload expressed in FTE also does not prove that payroll positions were removed.

For a customer/operator comparison, the missing bridge is now concrete: identify all loading, unloading, monitoring, cleaning, recovery and maintenance person-minutes for the same transport population, then show which paid hours can actually be avoided. Until then, this study supports a specialized-transport time benchmark and a promising cost-evaluation lead. It does not calibrate a humanoid or a US hospital staffing model.

## The ChristianaCare discrepancy remains open

The earlier [ChristianaCare observation](https://pmc.ncbi.nlm.nih.gov/articles/PMC11892717/) retains its stated 107 interventions and its categories totaling 111. Its 33 hours are observer-hours from 23 sessions, with 89 end-to-end deliveries. No matched intervention-duration series has been found, and the discrepancy is not resolved by comparing it with later cumulative delivery totals.

The [operator's blueprint landing page](https://christianacare.org/us/en/for-health-professionals/nursing/nurse-led-innovation) points to [Charting Nurse-led Innovation](https://issuu.com/christianacare/docs/charting_nurse-led_innovation), whose publisher record is dated 19 December 2025. This is the follow-up report referenced by the later hospital perspective. Its existence and metadata were verified, but the report's body was not retrieved: indexed extraction exposed only its title/description, and direct report/embed access returned 403. The package makes no claim about unseen contents. The 107-versus-111 conflict, and the lack of a matched support denominator for more than 48,600 later cumulative deliveries, remain explicit.

## Model implication and stopping decision

Three additions are justified now. First, separate **normal handling, safety presence and exception correction** in the service model. A single intervention rate misses two of these. Second, retain service eligibility and demand displacement: a low-congestion or nonurgent robot schedule must account for deliveries deferred or completed by people. Third, use the specialized endoscope system as evidence that process-time improvement is measurable with a comparator, while requiring a separate paid-labor bridge before claiming savings.

The next evidence packet must join request IDs, accepted receipt and timing, robot active/down hours, staff task-duration logs and failed/manual fallback outcomes. The appropriate economic quantity is total relevant person-minutes per accepted service, compared at matched urgency, payload, route and quality. Neither calendar time nor cumulative deliveries supplies that quantity by itself.

This wave stops after two empirical case audits and bounded follow-up access attempts. The Guro supplement was sought through its publisher link, PMC attachment and public EuropePMC supplementary archive; attempts returned a preparation HTML page or timed out, including a 45-second archive retry with zero bytes received. The Qilu full methods and ChristianaCare report body were not accessible through the attempted primary routes. No paid access, correspondence, broad new search campaign or invented calibration was used. The JSON contains five transparent arithmetic checks, three unresolved source conflicts and the missing-denominator requirements. Existing checkpoint artifacts and common-model assumptions remain unchanged.
