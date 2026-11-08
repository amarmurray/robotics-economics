# Hospital logistics: what the support denominators actually measure

**Edition 0.34:** the [economic-claim audit below](#hospital-economic-claims-edition-034) adds four primary source records and ten reproducible calculations. It leaves earlier studies and scenarios unchanged and does not close whole-service cost or paid-staffing evidence gaps.

**7 November continuation:** FSD-E005 adds a bounded WSNA worker-experience account to the [hospital decision pack](deployment_entry_decisions.md#hospital-logistics--qualify-the-entire-obligation). Its reported escort burden is qualitative testimony; its reported MultiCare exit is not independently operator-verified here. The original studies, arithmetic and conflicts below are unchanged.

**8 November continuation:** [The hospital support audit](hospital_support_contracts.md) adds procurement and repair/exit boundaries to the decision pack. It leaves the studies, numerical findings and unresolved conflicts below unchanged.

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

## Hospital economic claims, edition 0.34

The decision changes when a proposal promises cash savings but the evidence measures time released, or when a projected saving omits the work needed to keep service complete. The existing hospital pack therefore retains its conditional proceed/wait/reject gates. A bounded, authorized evaluation can test service and workforce consequences; a payroll-funded rollout must wait for its own staffing and cost bridge. Reject a business case that uses selected robot tasks as the entire hospital obligation or treats a modeled staff reduction as an observed one.

### Preserve the two Taiwan versions

The official ISPOR EE102 [abstract](https://www.ispor.org/conferences-education/conferences/past-conferences/ispor-2026/program/program/presentation/ispor-2026/poster-session-1-4/cost-effectiveness-of-an-automated-delivery-robot-program-to-reduce-nursing-transport-burden-in-an-intensive-care-unit-a-hospital-provider-perspective) describes time-motion observations and robot logs. Its annual released-time and cost-per-hour estimates differ materially from the [linked poster](https://www.ispor.org/docs/default-source/cti-meeting-21463-documents/5d45abe7-6936-416a-a174-e7fb62b3d120.pdf?sfvrsn=7824ce7f_0), which models robot operation against three days of manual observations. Both belong to the May 2026 conference; a verified revision chronology is unavailable. FSD-E006 and FSD-E007 preserve them separately.

Reproducing each equation does not reconcile the intervention, observation clock or methods. Do not combine one version's favorable time denominator with the other's cost numerator. The poster's annual robot-minus-manual cost equals its narrative increment, while its table differs by one Taiwan dollar; the record retains all three values. This small display discrepancy does not explain the much larger abstract/poster difference. Hidden precision is unknown. Neither version establishes a target staffing reduction or a defensible hospital-wide return.

### A cost projection is a different observation period

The [Shaanxi Scientific Reports study](https://pmc.ncbi.nlm.nih.gov/articles/PMC13276296/) uses June–November 2025 routine daytime transport observations and projects costs over ten years. Emergency/off-duty service is excluded. Its staffing-replacement attribution is not accompanied here by a verified payroll transition. Dispatch, handling, system management, maintenance and fault recovery remain work. The raw operating data are confidential and available only by author request; no request was made. See FSD-E008.

Our arithmetic audit reproduces the projected cost difference. It also finds that the published maintenance sensitivity total equals increasing the entire robot-cost total by the stated percentage. A separate diagnostic holds initial capital fixed and applies that change only to the noncapital residual. That is deliberately **not a repaired forecast**: the residual is not verified to consist entirely of maintenance, and the source does not identify every simultaneous change. The difference identifies a replication question; it establishes neither the correct target projection nor invalidity of the observed transport results.

### A useful planning hypothesis still needs operating evidence

The [Charité whitepaper](https://medinfo.charite.de/fileadmin/user_upload/microsites/m_cc01/medinfo/Events_Meldungen/Charit%C3%A9_Whitepaper_Robotische_Automatisierung.pdf), [released 20 August 2026](https://medinfo.charite.de/en/metas/news/artikel/detail/robotic_automation_in_hospitals_white_paper_provides_practical_guidance/), is an Elvio-funded model hypothesis without original operating quantity, time or cost data. Its immediate staff-cost removal and fault-free operation exclude transition overlap and fallback. The described service guarantee concerns assigned tasks. FSD-E009 records these boundaries. The referenced Excel annex was not retrieved from the inspected official release or PDF; no external/embedded PDF link supplied it.

The central diligence question is therefore whether the operating organization can realize the proposed staffing transition while covering the same required service. Vacancy coverage can be valuable without reducing current payroll. A monthly supplier fee belongs in customer cash; it does not disclose supplier margin or eliminate retained internal work. Adding that fee to the provider's resource expense in a consolidated total would double count the transfer. No source price or staffing ratio is transferred into the US hospital cell, other decision packs or synthetic scenarios.

### Evidence that would change the recommendation

FSD-AUDIT-ECON-01 makes four checks explicit: source/configuration identity, complete required service, staffing transition, and payment/support obligations. Use the same request cohort and clock for human, improved human-dispatch, specialist robot and feasible mixed alternatives. Include declined jobs, urgent/off-duty work, travel/handling, observation, cleaning, repair, fallback and overlap. Distinguish an employee's released minutes from reassignment, avoided hiring/overtime and actual paid staffing removed. Identify who funds and performs every retained activity, plus dates and enforceable obligations; do not assume a service fee covers an unpriced responsibility.

The [source export](../model/results/observed_research_summary.json) reproduces ten calculations with equations and input IDs under separate versions and currencies. Five target outcomes remain explicitly unknown: paid labor removed, complete-service cost, ROI, provider margin and service coverage. Existing hospital procurement/repair evidence and the [stronger human-dispatch comparator](conventional_coordination.md#empirical-challenge-a-human-dispatcher-with-better-information) remain complementary. This tranche neither closes empirical acceptance nor favors a generalist intelligence architecture over specialized transport.

## Employment, operating windows and fallback, edition 0.36

A hospital can reduce manual transport while continuing to pay the people who previously performed it. That outcome may improve service, avoid future hiring or reduce physical strain, but its cash and capacity consequences require separate evidence. The new source audit tests the organizational premise behind the [shared-crew execution](shared_workforce.md): who supplies every remaining duty, including fallback, after work is reassigned?

### The observed organization is more specific than a robot count

[Lloyd and Payne (2021)](https://doi.org/10.1111/irj.12323) report qualitative research in three Norwegian and two Scottish hospitals: 26 interviews with 34 participants in 2018–2019, accompanied by site tours. All cases involve complete or partial new builds. FSD-E010 preserves the anonymous identifiers, Table 1 configurations and observation period. This is not a matched payroll or all-request service panel, nor evidence of current performance.

The authors report estimates that, without AGVs, N-1 would need 15–20 additional workers, N-2 15 and S-2 30. Those are attributed counterfactual staffing estimates; the study does not establish those numbers as actual hires avoided, jobs eliminated or FTEs. It describes redeployment into other work, with some retirement and transfers, while services expanded. Managers had not measured realized financial savings. The appropriate counterfactual also includes the new hospital's distances, logistics and demand, rather than assuming the former building's staffing can serve an unchanged obligation. [FSD-E010]

The source separates provider arrangements that a generic ownership label would obscure. Four cases report hospital-owned and managed AGVs. S-2 uses an outsourced provider across portering, catering and cleaning; the exception does not explicitly establish robot asset title. Separately, S-1 outsources most maintenance. These are different arrangements, not evidence that the same party always owns the machine, employs the retained staff, controls repair and bears downtime costs. The paper is available under Creative Commons Attribution; [Cardiff's repository record](https://orca.cardiff.ac.uk/id/eprint/139408/) confirms that license. [FSD-E010]

### A system window is not measured exposure

Table 1 reports 12 hours per day on five days for N-1 and N-2, 13 hours on five days for N-3, and 24 hours on seven days for S-1 and S-2. Multiplication yields weekly system windows of 60, 60, 65, 168 and 168 hours. It does not identify each robot's active time, uptime, accepted deliveries, worker-hours or required service outside the window. The audit therefore keeps the five configurations separate and never multiplies their schedules by fleet size to manufacture observed exposure. [FSD-E010, Table 1]

The study also identifies work that persists around automation: control-room monitoring, dispatch, cart placement, loading, residual lifting and first-line intervention. Authority to reset or clean a robot differs from authority to repair it. Software, doors, lifts, connectivity, cart compatibility and inventory changes created implementation problems over multiple years. Broader service-assistant roles also reflected changes beyond AGVs. These findings motivate a target work-and-authority map; they do not calibrate a modern humanoid's reliability, learning gain or ramp duration. [FSD-E010, sections 4.2–4.4]

### Redeployment and contingency can claim the same person

The [Scottish Government's 2011 estate report, published 10 February 2012](https://www.gov.scot/publications/state-nhsscotland-estate-2011/pages/6/), describes 13 AGVs at Forth Valley Royal Hospital. It estimates work equivalent to around 12 staff and explicitly says those staff moved to other duties. It also identifies manual or electric-vehicle trolley movement with redeployed porters as the system-failure contingency. The account supplies a fallback method, not a measured response time, staffed reserve, duty calendar or guarantee of complete service. [FSD-E011, Annex A case study 10]

The report's approximate £1 million system cost, roughly £50,000 per AGV and claimed three-to-four-year payback remain reported historical figures. Their cash-flow basis and full cost allocation are unavailable; no realized payback or payroll saving is reconstructed. The named hospital is not identified with S-2 merely because both sources list 13 AGVs and a similar introduction period. The government text is attributed under its Open Government Licence. [FSD-E011]

Our inference is that reassignment and fallback must share a feasible duty calendar. If a porter now performs another required service, recalling that person during a robot outage may leave that service uncovered. The evidence does not demonstrate that such a failure occurred in these hospitals; it identifies the record a decision needs. A staffing reduction further changes the available fallback set and its funding. The synthetic notice rule remains an explicit assumption, not a transition authorized or validated by these sources.

### Consequences for deployment and entry

For the hospital pack, proceed only to a bounded comparison that specifies the same required service, operating window, receiving duties, supervision, repair authority and funded contingency. Wait on a staffing-funded rollout until actual paid schedules, transition authority and payment records support it. Reject a proposal that books a reassigned worker twice, equates a schedule with uptime, treats an outsourced service as proof of asset title, or converts an estimated staffing counterfactual into observed cash savings.

For utility inspection and automotive service, carry across the questions about residual routes, production duties, staffed response and distinct provider obligations. None of the hospital schedules, staffing counts, historical costs or institutional arrangements transfers numerically. Substantial H is expressed through the actual dispatch, inventory, interface and authority requirements; software access or a more capable model does not itself supply a person authorized and available to act.

FSD-AUDIT-WORK-01 exposes five schedule calculations, six decision gates and eight explicit unknowns, with source/input lineage in the [accepted export](../model/results/observed_research_summary.json). The publisher PDF route returned HTTP 403 and was not retried; full publisher HTML and institutional license metadata were accessible. Existing restricted routes remain closed. No new synthetic worlds, source-calibrated coefficients, target ROI or empirical acceptance claim is added.
