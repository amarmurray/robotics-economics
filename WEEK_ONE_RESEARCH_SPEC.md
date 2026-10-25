# Week-one research campaign specification

Version 1.5 · Active campaign · Late Workstream K scope, 25 October 2026

## 1. Purpose, organizing unit, and authority

Produce a defensible first edition of a research program that develops strategy and deployment judgment for work at a humanoid robotics company. Explain physical-labor end markets, evolving production capabilities, feasible deployment sequences, and alternative routes to industrial transformation. Connect deployment economics to learning, coordination, customer ownership/organization, and robotics business models and value capture. Customer ownership is a determinant of adoption; provider, robot-asset, and commercial arrangements remain a separate linked inquiry.

The organizing unit is **end market × value-chain stage × operating archetype × geography × time**. Tasks and task bundles provide diagnostic resolution when a mechanism requires it. A narrow warehouse case, a particular robot, or an initial task taxonomy is not a prerequisite for this campaign.

Default scope is a **United States quantitative labor anchor**, combined with global coverage of relevant providers, research, supply chains, financing, ownership models, and deployment evidence. Record these as revisable assumptions. Use the latest reasonably harmonized historical baseline, preserving each observation's actual year. Date each current-evidence snapshot, beginning at activation; use the design's observed baseline and conditional 0–2, 3–5, and 6–10-year horizons. Explicit calendar-year comparison points may be added without treating them as predictions. State currency base year, inflation treatment, time intervals, and conversion conventions explicitly.

The campaign extends CPU-first, docs-first work to a lightweight executable model and local dashboard in this repository. It does not authorize hardware purchases, GPU spending, paid data purchases, outreach, public posts, changes to another repository, or external dashboard hosting. Use public evidence and labeled scenarios; do not incorporate confidential employer material.

Workstream H is a substantial part of this same campaign. Read `LLM_ECOSYSTEM_RESEARCH_MODULE.md` for its detailed scope and evidence standards; this specification governs first-week acceptance. As a revisable planning default, devote approximately one-third of substantive research attention to H and its integration with the other workstreams, counting shared research once. Record material reallocations and their reasons; do not pad work to meet an effort percentage.

Workstream I, detailed in `ROBOTICS_SUPPLY_EMBODIMENT_ECOSYSTEM_MODULE.md`, makes humanoid/quadruped supply and value chains, components (including actuation, onboard compute and memory), manufacturing/qualification/ramp, embodiment choices, key players and layered openness substantial research subjects. Workstream J, detailed in `QUADRUPED_AND_DRONE_RESEARCH_MODULE.md`, makes quadruped deployments a major empirical module and uses drone deployment, operating, supply-chain and ecosystem evidence through bounded comparisons. Distinguish capability improvement, production cost learning, qualified supply, supported operational scale and economic penetration. Compare embodiments within the existing end-market map; trace time-indexed scale feasibility and preserve human, specialized-machine and mixed-fleet alternatives. SDKs, released weights, open hardware and commercial rights are separate. Use shared records and count activity, resources and benefits once.

This document prepares the campaign. Reading or publishing it does not start research or establish a running background process.

## 2. Activation, elapsed time, and continuation

At actual activation, record T0 as an ISO-8601 UTC timestamp, the input repository revision, runtime, and authorization reference. Define:

    deadline_utc = T0_utc + 168 hours

Display both endpoints in America/New_York with their applicable offsets. UTC elapsed time governs the deadline across daylight-saving transitions. Seven named phases, seven sessions, or seven rapid iterations do not constitute a seven-day campaign.

Persist activation, deadline, last substantive checkpoint, runtime status, and next bounded question in an ignored operational record. Check time at meaningful work boundaries. Never sleep, busy-poll, repeatedly refresh sources without a question, or manufacture activity to consume the window.

While execution is available before the deadline, continue productive work on the ranked question queue. An early working report and dashboard establish a usable baseline; they do not end the campaign. Further work should reduce consequential uncertainty, test a competing explanation, broaden neglected coverage, or improve a fragile inference.

Execution depends on actual runtime availability. If interrupted or paused, save a semantic checkpoint and state that work is paused. The wall-clock deadline continues unless Amar explicitly changes it. Do not claim that execution persists after a session ends. On resumption, recover the deadline and latest checkpoint before selecting work. If resumption occurs after the deadline, assemble the strongest defensible edition from completed work, disclose the interruption, and separate any later additions.

At the deadline, end expansion of first-edition research and deliver the report, dashboard, evidence/model package, acceptance audit, and unresolved roadmap. Material unknowns remain unknown. The deadline produces an edition, not a declaration that the research program is finished.

### Intended progression

These overlapping checkpoints describe elapsed hours from T0, not rigid departmental handoffs:

| Elapsed hours | Principal outcomes |
| --- | --- |
| 0–24 | Recover accepted context; establish definitions, taxonomy, sources, schemas, coverage register, and ranked questions. |
| 24–48 | Establish economy-wide screening coverage, initial labor baselines, provider/research evidence, and a runnable model skeleton. |
| 48–72 | Deepen contrasting market-stage cells; develop capability, ownership, and shared-resource mechanisms. |
| 72–96 | Produce connected adoption, economics, learning, and coordination scenarios; expose important unknowns. |
| 96–120 | Challenge rankings and mechanisms; investigate contradictions, transfer assumptions, and alternative pathways. |
| 120–144 | Integrate report and dashboard; review consistency and remaining high-value questions. |
| 144–168 | Resolve the best remaining bounded questions; finalize reproducibility, acceptance audit, and continuation roadmap. |

Use parallel researchers for independent questions with shared schemas and one writer per file. Rank questions by decision importance, uncertainty, tractability, and dependencies; explain rankings rather than presenting invented numerical precision. Every research block needs a question, evidence target, stopping condition, and expected decision consequence.

## 3. Breadth and depth requirements

Build a top-level classification that accounts for the economy's physical-labor activities, including production, construction, transport and trade, care, hospitality, infrastructure operation, maintenance, and household or public services where measurable. Target **10–15 end-market families**. Document classification crosswalks and boundary choices; reorganize families when evidence warrants.

Give every top-level category a coverage status: quantified, qualitatively screened, known evidence gap, not yet researched, or excluded with rationale. Show residual and unmapped activity. Economy-wide coverage means an explicit coverage map, not a claim that every activity has a calibrated forecast.

Develop **at least six contrasting market-stage cells across at least four end markets**, subject to accessible evidence. Contrast capital intensity, environmental variability, labor economics, fragmentation, demand, installed-asset constraints, and customer ownership/organization. For each, document the value chain, relevant systems and alternatives, economics, waterfall, bottlenecks, pathway comparison, learning links, and uncertainties.

Within at least two of those cells, seek comparisons between two plausible customer profiles and relevant commercial arrangements, subject to evidence. These are mechanism comparisons within the existing coverage target. Hold technical capability and workload fixed in a comparison, then distinguish any scenario that changes process design or value-chain position. A scenario is not proof of an ownership effect.

Screen AI-native operating-newco entry qualitatively across the end-market map. Within at least one of the deeper market-stage cells, develop a substantive entrant-versus-incumbent formation, funding, and deployment comparison. This uses the existing coverage target. Include equal access to robot technology, alternative incumbent adoption/response timing, and build/acquire/hybrid choices; use explicit scenarios where evidence cannot support calibration.

Do not invent inputs to satisfy coverage counts. A cell with insufficient evidence can be deeply investigated and still remain unquantified. Explain the resulting limitation in the acceptance audit and preserve the specific research needed.

Core question families are:

1. Where is physical work performed, what outcome does it support, and which resources constrain productive output?
2. Which existing or emerging systems could serve each market stage, under what operating conditions?
3. Which improvements would change feasibility, economics, penetration, or deployment order?
4. What limits installation, productive utilization, support, financing, and expansion across markets?
5. How do deployment experience, data aggregation, learning transfer, and coordination affect subsequent choices?
6. How do customer ownership, governance, capital allocation, automation appetite, implementation capacity, and value-chain position affect adoption, including incumbent/acquisition/newco pathways and coexistence?
7. Which robotics business models, asset/control arrangements, and roles for providers, operators, integrators, and financiers create and capture value, and how do they interact with customer adoption?
8. Which digital-AI ecosystem mechanisms transfer, and how do digital systems directly improve robots, organizations and robotics R&D?
9. How do components, qualified production, physical supply, embodiment choices and openness change feasible scale, timing, economics and entry?
10. What do actual quadruped deployments and bounded drone comparisons reveal about useful output, operating scale, business models and deployment sequence?

### Substantial digital-AI ecosystem module

Cover all seven digital-ecosystem subjects specified by Amar: development and physical supply; scaling and deployment/nondeployment; historical/prospective market effects; economic benchmarking; multi-agent coordination; model-producer competition for inputs/capital/customers and deploycos; and companies built on or linked to labs. Distinguish comparative analogies from direct technical contributions. Include inference economics, organizational complements, moving incumbent baselines, model dependence and rights, and shared physical-resource feedback.

The first edition must contain:

- One connected ecosystem dossier mapping physical inputs, model production, inference/distribution, agent/tooling layers, deployment firms, operating customers and dependent businesses. Use a dated coverage map rather than claiming every actor is covered.
- Two contrasting digital end-market/value-chain deployment dossiers connecting capability, actual use or nondeployment, economic outcomes and organizational conditions. Include retrospective methods and prospective implications; use source vintages correctly.
- Three direct-contribution maps: embodied capability/control; fleet/site/enterprise integration including ERP, routing/scheduling and operations systems; and robotics R&D. Distinguish observed results, announced products, conventional interfaces and proposed combinations.
- At least six explicit analogy tests spanning several subjects, including material nontransfer conditions or candidate counterexamples. A failed analogy can be a useful result; do not manufacture positive transfers.
- Benchmark cards across professional outputs, organizational workflows, agent coordination and embodied control, with system/harness versions, budgets, intervention and measurement limits.
- One transparent joint digital/physical mechanism scenario with matched output/quality and demand, evolving digital-improved human/incumbent comparators, identifiable interactions and source-linked assumptions. Labeled scenarios are acceptable when calibration is unsupported.
- A substantial report chapter integrated with the other workstreams and dedicated dashboard workspaces. Explain how the evidence changes or constrains at least three concrete research questions, deployment scenarios or organizational comparisons; rejected transfers and bounded null findings count.

Reuse connected dossiers across these requirements. Preserve unresolved coverage in the roadmap; a source directory or analogy list alone is insufficient. Model scope remains local CPU research, with no implied authority to run hardware or GPU experiments from cited papers.

### Substantial physical supply, embodiment, quadruped and drone modules

Read `ROBOTICS_SUPPLY_EMBODIMENT_ECOSYSTEM_MODULE.md` and `QUADRUPED_AND_DRONE_RESEARCH_MODULE.md`. I/J receive dedicated substantial analysis and outputs, integrated with A–H. Preserve H's approximately one-third attention default; count shared work once. Select cases that resolve several questions and reuse the existing six deeper market-stage cells. Do not silently expand this into an obligation to complete a separate market study for every robot family or component.

The first edition must contain:

- One connected humanoid/quadruped supply and value-chain map covering the component, manufacturing, software, deployment, service, finance and customer layers; a dated key-player coverage register with regional coverage, known relationships and unknowns. Include onboard compute/memory and separate training/remote-inference resources.
- Two sourced system/component configuration maps, one humanoid and one quadruped. Record unknown BOM quantities, costs, suppliers, yields and capacity explicitly; no fabricated cost breakdowns. Architecture and qualification differences must remain visible.
- At least two matched embodiment comparisons linked to existing deeper cells, considering human/digital-improved baselines and relevant simpler or mixed-system alternatives. Compare useful output/quality, whole-system economics, support, data and supply needs; mark infeasible options rather than manufacturing equivalence.
- One transparent time-indexed component → qualified production → commissioning → supported fleet scenario and scale-target backcast, integrated with the common engine. Test slower qualification/ramp, constrained supply or service, and a case where another constraint binds. Preserve inventory, yield boundaries, replacement/spare demand, shared allocations, financing and explicit uncertainty.
- At least five artifact/version-specific openness cards spanning a commercial platform such as Unitree, open hardware, middleware/interfaces, model/policy/data releases, and drone software. Separate access, source, reproducibility and commercial rights; explain economic hypotheses against the digital-model comparator.
- Three substantive quadruped deployment dossiers across at least two sectors, seeking at least one operator-supported routine-use case and one material limitation, nondeployment or stalled-use investigation. Cases may overlap those attributes. Record attempts and gaps if public evidence cannot establish the requested operating status; a vendor announcement does not fill that gap.
- Three contrasting drone comparison dossiers across at least two operating/business models, including a material constraint or negative finding. Use inspection, delivery, agricultural services or other cases selected for decision relevance. Distinguish measured activity/outcomes, modeled economics, regulatory conditions and vendor claims.
- At least four explicit physical-system transfer/nontransfer tests, including a failed or materially limited candidate, covering more than one of operational scaling, supply/industrial structure, openness, coordination and learning. These do not replace H's six digital analogy tests. Link direct complementarity or real shared inputs separately from analogy.
- Substantial report sections and two linked dashboard views for supply/production and embodiment/deployment comparisons. Explain how I/J evidence changes or constrains at least three concrete market, scale, architecture, customer-entry or provider strategy judgments. Negative findings count.

Dossiers are connected evidence packages, not six additional full market analyses. A single case can satisfy multiple perspectives transparently. If a minimum remains unsupported, preserve the attempted evidence route and consequence in the acceptance audit and roadmap; do not invent estimates or call a source directory a completed module.

### Late-added frontier robotics-model and economic layer

Read [FRONTIER_ROBOTICS_MODELS_RESEARCH_MODULE.md](FRONTIER_ROBOTICS_MODELS_RESEARCH_MODULE.md). Include model laboratories, model-to-embodiment integration, open and proprietary alternatives, hosted versus onboard inference, data/adaptation rights, deployment-led learning, capital, commercial terms and captured value. This is an authorized addition to the already-running campaign; do not reset T0, repeat completed work or spawn agents beyond the user's **single Astra Max** usage constraint.

Where remaining resources and evidence permit, seek a dated frontier model/OEM/open ecosystem roster, three contrasting dossiers including Physical Intelligence and Skild AI, evidence/version/rights cards, a four-architecture matched-service economic scenario, and three cross-workstream decision implications. Record unmet portions as partial continuing research without inventing evidence. Reuse existing six deeper market-stage cells, thirteen dashboard views and one calculation engine.

Distinct records: lab role/ownership; model and checkpoint version; compatible configured robot, control/harness and embodiment; training and adaptation inputs; inference architecture, on-device compute/memory and latency; access/license and data/fine-tune rights; evaluated versus actual productive field performance; provider/OEM/operator/customer economic roles, costs and cash transfers. Do not infer model quality equals economically accepted output.

## 4. Analytical and modeling requirements

### Economic activity and useful output

Separate employment, paid labor hours, physical-work hours, compensation, value added, end-market revenue, and provider revenue. Identify baseline automation and avoid counting the same intermediate activity in multiple end markets. Quantify labor addressability only where a defensible mapping exists.

Model equivalent accepted output and service quality. Distinguish time released, labor redeployed, payroll actually avoided, and capacity expanded. Added capacity creates revenue only with explicit demand and monetization assumptions. Keep displacement of existing work separate from demand expansion, newly feasible services, and any resulting additional labor.

Compare configured humanoids, quadrupeds and relevant alternatives, including wheeled/mobile manipulation, specialized/fixed automation, drones where outcomes overlap, process redesign, digital agents, and human–machine combinations. Quadrupeds are also studied as direct end-market deployments; drones can be substitutes, complements or bounded comparators depending on the mechanism. Provider coverage follows current evidence and market relevance; the old charter's reference roster is neither exhaustive nor compulsory.

### Capability trajectories and evidence-contingent response surfaces

Record system configuration, software version, environment, autonomy/control mode, assistance, metric denominator, measurement duration, and evidence date. Distinguish announcements, demonstrations, pilots, sustained operation, shipments, and installed productive fleets. Research benchmarks establish only the claims their conditions support.

Investigate improvement as a response surface conditional on experience coverage, data quality, training method, compute, embodiment, environment, integration, and coordination. Fit empirical relationships only where comparable observations support them. Report fit domain, uncertainty, confounding, and extrapolation limits.

Do not assume a universal scaling exponent, a monotonic data multiplier, or a calibrated relationship between benchmark scores and economic output. Where evidence is insufficient, implement clearly labeled mechanism-based scenarios or parameter bounds. Keep physical improvements, autonomy improvements, adaptation costs, intervention burden, and integration efficiency separable.

### Digital/physical comparisons, benchmarks, and direct-contribution claims

Define the digital source population and the robotics target separately. Each proposed analogy identifies a mechanism, required similarities, material differences, evidence on each side, target prediction, falsifier, and permitted use (question, qualitative prior, mechanism structure, or calibrated parameter). Numerical transfer needs target-specific justification. Keep a measured source effect separate from a hypothetical target coefficient.

A benchmark result is tied to a configuration, task/workflow distribution, evaluation method, budget, assistance, latency and failure definition. It does not by itself identify an occupation's automatable share, firm productivity, or adoption. Record outcome quality, intervention/recovery, repeated-workflow reliability and end-to-end costs. Historical studies remain dated; later changes in models, work selection or methodology can make an old estimate unsuitable for current inference.

For direct contributions, record the model's role, inputs/outputs, interface and execution substrate, timing, available state, authority and fallback, alternative implementation, effect on outcomes, and evidence setting. Distinguish simulated policy tests, live fleet data collection, enterprise product announcements, conventional system interfaces, and demonstrated integrated production. Do not compose separate papers into an observed end-to-end result.

At matched output quality and demand, compare: existing operations; digital improvement alone; robotic improvement at the existing digital baseline; and combined deployment/redesign. The combined effect need not equal the sum of individual effects. Track digital contributions to human-led operations as well as to robots, and avoid counting a shared foundation-model, scheduling or learning improvement twice. Explore different relative rates of digital capability, embodied policy, hardware, integration and organization change.

Research-acceleration cases require a fixed capability or engineering objective, baseline, human time, model/training/inference resources, failed experiments, validation and calendar time. A generated reward function or better simulated score is not automatically a quantified reduction in robotics development cost. Model potential feedback from robotics into AI infrastructure as conditional and resource-constrained.

### Conditional penetration waterfalls and adoption cohorts

For each cell and scenario, choose a common denominator: sites, accepted work units per period, or baseline-equivalent physical-labor hours. State conversion formulas, reference workload, coverage, and uncertainty. Robot-hours and human-hours cannot be substituted without supported throughput and staffing assumptions.

Track relevant activity through technical serviceability, economic attractiveness, organizational readiness, deliverability, commissioning, and realized productive output. Gates operate on matched cohorts and correlated conditions. Derive conditional shares from those cohorts; do not multiply arbitrary independent percentages. Unknown gate inputs cannot silently become zero, one, or an assumed midpoint.

Maintain stock-flow identities by installation cohort:

    active_stock[t] = active_stock[t−1] + commissioned[t] − retired[t]

Separate orders, shipments, commissioning, ramp-up, retained operation, replacement, expansion, and retirement. Model upgrades only for compatible cohorts and include validation, downtime, and retrofit costs. A new product announcement does not upgrade the installed base.

Translate active stock into productive capacity using workload, uptime, throughput, intervention, and process constraints. Aggregate only compatible units and periods. Preserve the distinction between addressable opportunity, adopted share, installed capacity, and realized output.

### Shared resources and financial feasibility

Allocate scarce hardware, components, integration crews, human support, maintenance, and capital across competing cells and providers. Existing fleets consume support capacity before incremental deployments. Use explicit resource coefficients and budgets:

    sum(resource_use[r,c,t] × deployment_activity[c,t]) ≤ available_resource[r,t]

Represent multi-period commissioning and support where material. A transparent allocation rule is acceptable; label whether it is a heuristic or optimization result. Do not let each market independently spend the same resource pool.

Reconcile customer, provider, asset-owner, and operator economics. Include deployment investment, integration, ramp losses, recurring support, collection timing, working capital, replacements, and financing boundaries. Accounting earnings are not deployable cash. Distinguish total value creation from its allocation among parties.

### Physical supply, embodiment and scale feasibility

Distinguish capability response, production learning/cost, qualified manufacturing capacity, supported field scale and economic penetration. Declare whether a target is annual production/shipments, cumulative units, retained active stock, useful output or economic share. Use the configured system and compatible component classes, not generic robot counts or pooled semiconductor/memory totals.

Conserve qualified components and finished systems across inventory, assembly starts, yield/rework, acceptance, shipments and commissioning. Model expansion/qualification lead times, funding and ramp; dates and output remain scenarios unless observed. Record whether a quantity is before or after yield so the same loss is not applied twice. Existing fleets consume spare parts, maintenance and human support; replacements are separate from net additions. A manufacturer announcement, nameplate capacity or supply agreement does not establish available qualified supply.

Join shared resource budgets to upstream component/facility/grade and geographic availability. Attribute demand from competing robot configurations and other sectors once; permit substitution only with explicit technical compatibility, qualification, cost and timing. Record supplier relationships, access terms and incomplete visibility. For each scale scenario, backcast necessary inputs and capacity milestones; feasible supply remains separate from economic demand, adoption and realized output.

Matched embodiment comparisons must preserve output/quality, workload and system boundaries, including payloads, software, site redesign, labor, maintenance, downtime and financing. Track complementary work and mixed fleets without duplicating addressable activity or information benefits. Performance/cost improvements may change both resource requirements and market eligibility; link those changes explicitly and separate compatible retrofits from new generations.

Classify openness by artifact/layer/version and verified rights/dependencies. A public SDK, model release or geometry file cannot mechanically assign an openness label or adoption/cost multiplier to an entire system. Compare practical reproducibility, integration, manufacturing, repair, qualification and governance, and preserve unresolved licensing/access conflicts.

Quadruped and drone dossiers distinguish successful missions/data collection, actionable findings, decisions/actions, realized business outcomes and labor/cash effects. Record robot/flight exposure, operator/reviewer/intervention/repair work, outages, failed attempts, route/site selection and censored or discontinued cases. Do not transfer drone regulatory conditions, cost curves or physical capabilities to ground robots without target evidence. I/J use the same analogy and evidence standards as H while preserving their own required coverage.

### Learning, data, and physical–digital coordination

Link deployments to experience exposure, datasets, training/validation, capability effects, and subsequent market opportunities. Separate operational experience from useful, accessible training data. Record collection, ownership, access, reuse, exclusivity, and commercialization rights without assuming that possession grants all of them.

Distinguish capability improvement, information that changes a later decision, and economic value captured by a particular party. Compare deployment policies with and without learning effects, including their costs and delays. Do not add a separate data premium when those same benefits already appear in future cash flows.

Model coordination among robots, digital agents, people, inventories, and shared infrastructure. Consider dispatch, scheduling, exception resolution, procurement, supervision, and workflow redesign. Include congestion, correlated failures, intervention queues, and coordination costs where relevant. Deployment changes experience; learning and coordination can change deployment feasibility and order.

### Customer ownership, organization, and adoption

Stratify customer cohorts within each market-stage cell by separately recorded ownership/control attributes, financing relationships, investment criteria, operating organization, and value-chain role. Distinguish parent, operating company, site, procurement buyer, process controller, and beneficiary. Incumbent/new entrant describes market position; acquisition/holdco transformation describes a development route; AI-native describes process design. These are overlapping dimensions, not mutually exclusive ownership bins.

Model the mechanisms connecting customer structure to ability to finance, appetite to invest, authority to change operations, implementation capacity, and retention of benefits. Link those mechanisms to adoption timing, depth, scale, and chosen configurations. Do not use an unexplained ownership-label multiplier or infer appetite from a label. Preserve opposing mechanisms and selection/confounding limits in empirical comparisons.

Use compatible activity weights to aggregate customer cohorts. Distinguish fixed customer composition from entry, acquisition, consolidation, outsourcing, and movement across value-chain stages. Reclassifying an acquired operation does not create new underlying work. Changed operating configurations require explicit costs, timing, and capability assumptions.

### AI-native customer entry, financing, and competitive response

The customer-side newco is an operating business selling an end-market product or service using humanoids and digital agents. Include standalone formation, a platform creating multiple newcos, acquisition-led transformation, and hybrid routes. A holdco may own either newly created or acquired operations. Preserve the distinction between a new parent company and genuinely new operating capacity.

Investigate operating-design advantage, adoption timing with widely available robots, and capacity/availability advantage as separate, potentially combined mechanisms. Compare against a human-led incumbent and an incumbent adopting the same technology; include digital-only or specialized automation where relevant. Evaluate quality-adjusted accepted output, full operating cost, reliable capacity, and the customer offer. Treat cheaper, more productive, or more abundant humanoids as conditions to test, not baseline facts.

Specify formation, commissioning, ramp, and expansion cash flows, including robot and complementary assets, integration, overhead, customer acquisition, working capital, and losses before repeatable operation. Identify funding requirements, runway, possible funding sources/terms, and milestone conditions. Separate unit economics, financeability, and actual capital access. Link enterprise funding to robot ownership/financing from the commercial-arrangement model without treating a lease as financing the whole business.

Distinguish installed productive capacity, demand won, delivered output, revenue, and retained contribution. For a matched period and service, delivered entrant output cannot exceed either productive capacity or demand it can serve. Reconcile incumbent and entrant activity, share transfers, unmet demand, and demand expansion. Do not convert a cost advantage directly into market share or count transferred work as additional market labor.

Model alternative incumbent responses and the duration of an adoption lead. Examine price competition, customer retention, imitation, partnership, acquisition, and convergence in robot performance where material. Funding may run out before steady-state economics become attractive. Identify what could remain differentiated after incumbents adopt and whether fleet learning benefits the entrant, its provider, or both.

Use the Thrive Holdings analogy to investigate capital formation, owned operating platforms, and embedded deployment engineering. Check the sources in the design at kickoff. Keep the physical/industrial extension and greenfield variant explicitly hypothetical. Public financing announcements for an analogy do not establish that a proposed entrant can raise money.

### Robotics business models, asset ownership, and value capture

Retain the distinct comparison of equipment sales, leases, robotics-as-a-service, usage/outcome pricing, integration, software, managed operations, partnerships, joint ventures, and provider vertical integration. Evaluate who supplies, operates, owns, finances, controls, bears risk, and retains gains for matched customer outcomes. Include acquisition or greenfield capital and transition time where relevant.

Join these arrangements to customer profiles. A commercial structure can change adoption constraints while moving cash requirements or risks to providers, operators, or financiers; reconcile all relevant resource and cash budgets. Joint ventures can affect both governance and commercial terms. One entity may fill several roles, so use a common actor/role map and eliminate internal transfers in any consolidated view. Keep underlying customer ownership distinct from robot-asset ownership and model/data rights.

Produce a cross-comparison of customer profiles and commercial arrangements, identifying which combination changes deployment feasibility, timing, productive scale, and value allocation. Preserve supplier integration, asset ownership, and value-capture questions as substantive research rather than reducing them to financing controls.

## 5. Compact data contracts

Use inspectable CSV and JSON before introducing a database. Every record has a stable ID, schema/version identifier, applicable geography and period, evidence references, and an explicit status. Quantitative fields require units and denominators. Use null plus a missingness reason; zero means measured or explicitly assumed zero.

The cell key joins market, chain stage, operating archetype, geography, and period. Keep it stable across competing system and ownership scenarios.

| Record | Minimum contract |
| --- | --- |
| Market | market_id; parent/classification codes; boundary; geography; economic baseline; coverage status; residual allocation. |
| Chain | chain_id; market_id; stage; upstream/downstream dependencies; actors; output; double-counting rule. |
| Work | work_id; cell key; useful output; baseline labor/resource requirements; diagnostic task links; conversion rules. |
| Adopter | adopter_id; parent/operator/site/buyer/beneficiary actor IDs; ownership/governance attributes; market tenure; operating organization; capital access/allocation; investment criteria and appetite evidence; process authority; implementation capacity; value-chain roles; effective dates. |
| Cohort | cohort_id; work_id; adopter_id; population, denominator and activity weight; operating conditions; system/pathway/arrangement IDs; commissioning period; stock-flow states. |
| System | system_id; provider; embodiment/configuration; hardware/software versions; availability; upgrade compatibility; alternatives. |
| Capability | capability_id; system/work/environment; metric/value/range/unit; exposure duration; assistance; evidence and deployment status. |
| Dataset | dataset_id; location/version/hash; composition; collection window; coverage; license/access/reuse rights; limitations. |
| Exposure | exposure_id; cohort/system/dataset links; workload; informative coverage; redundancy; observation process; collection cost. |
| Transfer | transfer_id; source exposure/capability; destination; mechanism; response/delay; training costs; rights; beneficiary; validation status. |
| Coordination | coordination_id; participants; mechanism; shared resources; information assumptions; costs; measured or scenario effects. |
| Pathway | pathway_id; adopter IDs; business origin and parent/platform links; incumbent expansion/acquisition/transformation/new-entry route; build/acquire/partner choices; origin/destination value-chain roles; transition costs and timing; cohort reclassification and activity conservation. |
| Entry case | entry_case_id; market/stage/adopter/pathway IDs; product and customer; proposed advantage; incumbent comparator and response; system/arrangement links; capability and economic thresholds; formation/ramp/expansion cash flows; funding assumptions and milestones; demand/retention/served-output constraints; entry window; disconfirming evidence. |
| Commercial arrangement | arrangement_id; actor/role map; system/cohort/adopter links; sale/lease/service/license/partnership/operation terms; robot/model/data/control rights; funder and risk allocation; pricing; cash and value allocation; effective dates. |
| Scenario | scenario_id/version; model/evidence snapshot; horizons; input overrides; dependencies; resource budgets; allocation and demand policies. |
| Digital ecosystem relationship | relationship_id; dated actor/asset/system IDs and value-chain roles; material/compute/cash/data/distribution/control link; capacity/commitment/availability status; terms; evidence; shared-resource budget links. |
| Benchmark card | benchmark_id/version; model/policy/harness/tool versions; population and tasks; evaluator; human comparator; budget; assistance; latency; costs; failure/recovery; result/uncertainty; operating applicability and limits. |
| Analogy test | analogy_id; source mechanism/population/evidence; target market-stage question; required similarities/differences; confounders; target prediction/falsifier; source and target statuses; permitted model use; affected scenario/question IDs. |
| Direct contribution | contribution_id; digital system/version; embodied/operations/R&D role; inputs/outputs/interfaces; execution/timing/state/authority; comparator; resources; evidence setting; effect/delay; target capability/cohort/scenario links. |
| Component/configuration | component_id/grade; system/version; role; units per assembly start; performance envelope; supplier/facility; qualification/substitutes; cost/price basis; evidence and unknowns. |
| Supply capacity | resource/facility/geography/time; nameplate vs qualified output; yield boundary; commitments and allocations; inventory; expansion/qualification/funding stage; lead time; evidence. |
| Production/service flow | starts, accepted completions, work in progress, finished inventory, shipments and commissioning; compatible cohort spares/replacements/repair/refurbishment/retirement; units and period. |
| Embodiment comparison | comparison_id; matched market/work/output/quality; system configurations and alternatives; fit, costs/resources and complements; infeasibility; break-even conditions; evidence/scenario links. |
| Openness artifact | artifact_id/layer/version/license/source; rights/dependency chain; access/reproducibility; interfaces; modification/manufacture/operation conditions; governance; unresolved conflicts. |
| Mission/outcome | deployment/cohort/system IDs; activity and exposure; autonomous/assisted mode; human work; data quality; actionable finding/decision/action/outcome links; comparator; failure/selection limits. |
| Frontier robotics model | lab/model/release/checkpoint IDs; policy/harness/embodiment context; data/training/adaptation/inference resources; access/license and use rights; eval/field availability; customer/OEM/operator terms; source/uncertainty. |
| Model architecture alternative | matched cell/output/quality; integrated OEM, independent licensed, open adapted and model-led operator structures; incremental full costs, benefits, data rights, infrastructure, payer, limits and evidence/scenario status. |
| Evidence | evidence_id; precise claim; URL/document locator; publisher; observation/publication/retrieval dates; scope; source class; limitations; conflicts. |
| Question | question_id; decision consequence; priority rationale; dependencies; evidence target; stopping condition; status; next action/owner. |

Separate source provenance from epistemic status. A manufacturer statement may be a sourced claim rather than independent observation. Tag current operating evidence, research evidence, historical evidence, interpretation, and scenario assumptions distinctly. Retain contradictory observations and superseded versions. Versioned scenarios must identify which evidence they accept and which inputs they deliberately override.

## 6. Deliverables and dashboard behavior

Produce a written report, executable local dashboard, CSV/JSON evidence package, versioned scenarios, reproducible model, acceptance audit, and durable roadmap. Register final artifact paths and versions in the repository manifest.

The **report** should aim for 8,000–15,000 substantive words as guidance, with charts and appendices where helpful. Include an executive argument, market/value-chain atlas, capability landscape, improvement scenarios, penetration and supply constraints, learning/coordination analysis, customer-structure/adoption comparisons, AI-native entry and financing cases with competitive response, robotics business models and value capture, a substantial digital-AI ecosystem/evidence/direct-contribution chapter, substantial physical supply/embodiment/openness and quadruped/drone evidence sections with time-indexed scale analysis, integrated strategic implications, and unresolved questions. Preserve disagreements and alternative explanations. Length and apparent certainty are not completion metrics.

Use **one authoritative calculation engine** for dashboard outputs, report tables, and scenario exports. Documentation must provide exact environment, build, run, and regeneration commands. Store locked dependencies where appropriate and use deterministic seeds when simulations require randomness. A fresh local launch should use the saved evidence snapshot without requiring new external credentials. No public deployment is required.

### Thirteen linked dashboard views

1. **Economic atlas:** end markets, value-chain stages, labor/value measures, coverage statuses, residual categories, and baseline automation.
2. **Market deployment explorer:** selected cell, workflow context, competing configurations, conditional waterfall, economic outcomes, and adoption timeline.
3. **Provider and system landscape:** versioned humanoid/quadruped/other-system capabilities, key-player and regional coverage, evidence conditions, deployment phase, supply/commercial relationships, openness artifacts, and alternatives.
4. **Improvement explorer:** empirical response surfaces where supported, scenario trajectories otherwise, sensitivities, benchmark/economic applicability, capability-to-use gaps, relative digital/embodied/hardware progress, and limits of extrapolation.
5. **Fleet and bottleneck view:** commissioning cohorts, active stock, productive output, retirements, shared resource use, and binding constraints.
6. **Learning and coordination view:** exposure, aggregation, directed transfer, physical–digital dependencies, rights, costs, and beneficiaries; robot/fleet/site/enterprise roles, ERP/WMS/MES and routing/scheduling interfaces, and separate robotics R&D contributions.
7. **Customer structure and adoption:** ownership/governance profiles, capital access/allocation, automation appetite, operational authority, implementation capacity, customer pathways, value-chain position, and adoption outcomes; linked newco entry, funding/runway, build/acquire/hybrid, demand/share, and incumbent-response comparisons.
8. **Robotics business models and value capture:** commercial arrangements, provider/operator/integrator/financier roles, asset/control/data rights, cash requirements, risk allocation, integration, and coexistence. Link to the selected customer profiles.
9. **Digital AI ecosystem:** physical inputs, model development and inference, cloud/distribution, tools/agents, deployment companies, dependent businesses and adopting end markets; dated resource, capital, data, control and commercial relationships. Qualitative edges remain distinct from measured flows.
10. **Analogy and direct-contribution workbench:** source/target mechanisms and evidence, required conditions, transfer limits, model-role/interface maps, benchmark cards, joint digital/physical comparisons and implications for existing research questions.
11. **Robotics supply and production:** component/facility/system relationships; input and memory/compute classes; capacity/qualification/ramp, inventory/yield/spares, shared allocations, cost and capability links, bottleneck timeline and scale-target backcast.
12. **Embodiment and deployment comparison:** market-stage fit, matched output/quality and economics, human/simpler/mixed-system alternatives, quadruped field dossiers, drone transfer/nontransfer evidence, openness layers and source maturity.
13. **Scenario and evidence workbench:** scenario comparison, assumption changes, confidence, source drilldowns, contradictory evidence, and export.

For Workstream K, link model lab/lineage, release, compatibility, license/access, OEM-versus-independent provider, data/control rights, inference/adaptation and model-led operating structure into existing relevant views. A new fourteenth view is not required in this resource-limited campaign.

Shared filters include market, stage, archetype, geography, period/horizon, system/model/harness, embodiment/configuration, component/resource/qualification class, openness layer, digital/physical value-chain layer, contribution role, customer profile, customer pathway, commercial arrangement, scenario, and source/target evidence status where applicable. Views must show their active scope. A filter may leave an explicitly labeled reference total unchanged, but must not silently mix selected and unselected populations.

Scenario controls should alter model inputs and recalculate dependent outputs. Include economically relevant controls for capability/intervention, integration, shared support/hardware/capital, learning/transfer, coordination, demand expansion, customer capital/investment criteria and implementation capacity, commercial terms, entrant funding/ramp, demand capture, incumbent response timing, relative digital/embodied progress, inference/coordination costs and integration availability, component allocation/qualification, yield/ramp/expansion lead times, memory/compute/power configuration, replacement/spares and support requirements when modeled. Customer-profile changes must expose the parameters or mechanisms changed; a label alone must not mechanically create an adoption advantage. Disable unsupported controls with a reason. Keep observed evidence visually and computationally separate from hypothetical overrides.

Display meaningful ranges and appropriate rounding. Show missing inputs and unavailable estimates explicitly. A synthetic example may demonstrate functionality, but must have persistent labeling and remain excluded from empirical aggregates.

## 7. Acceptance and verification

Run focused checks that address concrete analytical and interface risks:

- Validate stable IDs, joins, schemas, dimensions, conversion rules, missingness, and scenario versions.
- Reconcile cohort stock flows, compatible population totals, waterfall denominators, customer-cohort activity weights, ownership transitions, and shared resource budgets.
- Verify customer ownership/governance and robot-asset/commercial arrangements are separate dimensions; compare a customer-profile change at fixed technical capability and trace its adoption mechanism. Check a commercial-term change for the corresponding customer and provider/financier cash and capacity effects.
- Verify that displacement, demand expansion, provider revenue, and learning value are not double-counted.
- Check entry cases for matched output/quality, conserved market share/activity, explicit funding gaps, capacity versus served-demand constraints, and alternative incumbent responses. Confirm that a parent-company formation or acquisition is not counted as new underlying productive activity; show a same-robot-access counterfactual.
- Compare dashboard and report outputs with the authoritative engine on saved scenarios.
- Exercise representative crossfilters; verify consistent scope and denominators in every affected view.
- Change material scenario inputs; confirm actual recalculation, or explain a locally insensitive result through model constraints.
- Drill from a displayed result through its calculation and assumptions to specific evidence records and source locators.
- Confirm observed evidence remains fixed when scenario controls change; test unknown versus zero and insufficient-data states.
- Verify analogy source and target evidence remain distinct; unsupported transfers cannot silently set calibrated parameters. Trace direct-contribution claims to their demonstrated setting and interface.
- Exercise a joint digital/physical comparison, including an improved human-led baseline, shared resource limits and non-additive effects without duplicate benefits. Check that changing digital assumptions affects the intended roles and populations only.
- Reconcile component and finished-system inventories, assembly/qualification yields, work-in-progress timing, commissioning, replacement versus net additions, spares and shared resource allocations; exercise a delayed-qualification or constrained-service case.
- Check that the scale-target backcast uses declared units and necessary-condition logic; supply feasibility cannot silently become demand or adoption.
- Verify embodiment comparisons use matched output/quality and total configured costs; overlapping or complementary drone/quadruped/humanoid work cannot duplicate economic activity or gains.
- Verify artifact-level openness and drone/quadruped observation status; released code, missions, announced capacity and modeled economics remain distinct from realized productive outcomes.
- Check K comparisons for actual model/release and compatible hardware evidence, field versus benchmark status, permissioned data reuse, training versus onboard/inference resource differences, and no duplicated provider/OEM/operator/customer revenue or uncalibrated model gains.
- Export and reload a scenario; reproduce its outputs and confirm a documented local launch.

Use a small set of meaningful fixtures and adverse cases. Do not mirror every implementation detail with tests or repeat a passing test without a concrete reason. Record pass, partial, blocked, or failed for each acceptance requirement, with consequences and next action.

## 8. Durable progress, publication, and continuation

Checkpoint after substantive evidence batches, model changes, disagreements, or completed analyses. Preserve structural assumptions, user corrections, rejected approaches, outstanding mechanisms, artifact versions, and next questions. Avoid verbose chronology, duplicate summaries, and operational timestamp churn in accepted research artifacts.

At each substantive authorized publication milestone, inspect local status and remote state, validate scoped changes, update accepted artifacts, HANDOFF.md, and manifest hashes, then create a scoped commit and normal push according to repository guidance. Include only campaign-owned accepted changes. Never blanket-commit unrelated edits, force-push, erase conflicts, or automatically merge divergence. Preserve work and report the precise publication blockage while continuing unaffected research.

Keep manifest self-hashes, observed commit SHAs, receipts, and runtime logs in the appropriate ignored operational records. A successful push establishes publication, not consumption by another project. Final artifacts must identify their evidence/model/scenario versions and known input revision without self-referential commit claims.

The **multi-month roadmap** should retain every consequential unresolved question and organize subsequent work as dependency- and evidence-driven research waves. A provisional twelve-week view can aid planning, but does not promise completion dates or supersede the open-ended program. For each item, specify the mechanism, intended contribution, importance, evidence/access needs, dependencies, bounded next action, completion criterion, and conditions that would change priority. Separate uncertainty reducible with public research from questions requiring field access, experiments, or new authority.

At the deadline, report what the first edition establishes, what remains scenario-dependent, where coverage falls short, how to run the dashboard, and the highest-value next questions. Preserve the remaining program as executable research work rather than treating the week's deliverables as its endpoint.
