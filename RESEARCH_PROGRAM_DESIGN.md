# Physical labor, humanoid deployment, and the organization of production

Version 0.6 · 25 October 2026 · Research program design

## 1. Purpose and accepted direction

Develop the understanding, evidence, and models Amar needs to help shape strategy and staged deployment at a humanoid robotics company. The program begins with physical labor across the economy, organized by end markets and value chains, and asks how changing humanoid capabilities, learning systems, data aggregation, physical-digital coordination, and organizational structures alter the paths to productive deployment.

The central question is:

**Where, how, and in what sequence can humanoids and digital agents transform physical production and services, what must improve for each stage to become viable, and which deployment and ownership arrangements can create and capture the resulting value?**

Amar's 25 October 2026 clarification establishes these requirements:

- End markets and value-chain stages organize discovery, synthesis, models, and the dashboard. The earlier warehouse/carton-handling first case is superseded.
- Tasks and task bundles supply explanatory detail about capability, operating conditions, and bottlenecks. They are not the primary discovery unit or an entry gate to broader research.
- Begin with qualitative views of physical labor, substitution opportunities, deployment pathways, bottlenecks, and data aggregation; develop staged penetration waterfalls as evidence supports them.
- Connect current provider/system capabilities to plausible future progress, including an explicit investigation of humanoid improvement and scaling relationships.
- Give learning, control, and coordination substantive treatment. Physical robots and digital agents can jointly reorganize productive processes.
- Study both directions of causation: capabilities and coordination shape deployment choices; deployments, experience, and operating arrangements shape later capabilities.
- Compare incumbent adoption, acquisition and transformation through a holding company, and new enterprises designed around physical and digital AI. Permit coexistence and specialization across value-chain stages.
- Deliver a substantive written report, an interactive dashboard with meaningful toggles, reproducible supporting artifacts, and a continuing research roadmap after an initial seven-day campaign.

These requirements govern the design. Geographic defaults, coverage targets, forecasting horizons, and particular implementation choices below are revisable working assumptions, not additional user commitments. Preparing this design does not start the seven-day run or claim its outputs exist.

## 2. Organizing hierarchy and research boundaries

The primary analytical cell is:

`end market × value-chain stage × operating archetype × geography × time`

Examples of operating archetypes include a large standardized facility, a small dispersed service business, a variable outdoor site, and a mixed physical-digital operation. These categories are starting distinctions to refine with evidence.

The hierarchy is economy → end market → value chain → productive process/operating archetype → physical and digital work → capability and coordination requirements → candidate system and organizational configurations. Task-level detail enters at the resolution necessary to explain a market-stage conclusion.

Keep three connected views:

1. **Demand and production:** what useful outcomes people and businesses need, how those outcomes are produced, and where physical labor and digital work occur.
2. **Capability and delivery:** which robot/model/integration configurations can serve that work, with what assistance, resources, reliability, and delivery capacity.
3. **Organization and value capture:** which actors own assets, control workflows, supply technology, access data, assume risk, and retain gains.

Describe market-level opportunities through production and service systems. A task demonstration is one observation relevant to capability, not a sufficient description of an end market. A broad industry label alone also cannot explain the heterogeneity of its operating environments. Retain both the broad organizing map and the supporting mechanisms.

The program is independent research. Ixion can supply questions and later consume useful methods, but its existing architecture does not determine the research's conclusions. Changes to `robotics-vp/robotics-vp-core` remain separately scoped.

## 3. Initial scope and defaults

Use the United States as the first quantitative labor-data anchor, with explicit coverage limits. Keep provider capabilities, robotics research, manufacturing, supply chains, and competitive structures global. Add international comparisons where differences in wages, industrial organization, labor supply, or deployment conditions materially affect conclusions. Do not label a US denominator as the global opportunity.

Use the actual campaign kickoff as the research as-of date and preserve observation/publication/retrieval dates separately. Start with an observed baseline and scenario horizons of 0–2, 3–5, and 6–10 years from that baseline. Calendar dates are conditional scenario displays; capability milestones and deployment conditions provide the explanation. Longer horizons may remain predominantly qualitative.

Screen the full economy through an explicit classification crosswalk and disclose exclusions, unallocated activity, and partial coverage. An initial practical target is 10–15 end-market families and six contrasting market-stage analyses across at least four end markets. Counts are coverage aids, not evidence substitutes. Document why a lower defensible coverage level was unavoidable rather than manufacturing estimates to meet a target.

Potential families include agriculture/food systems, manufacturing, construction and the built environment, logistics/distribution, retail, hospitality/food service, healthcare/support services, facilities/cleaning/maintenance, utilities/infrastructure, waste/material recovery, and household/personal services. Research should revise this taxonomy. Cross-cutting functions such as logistics or maintenance need allocation rules so they do not become duplicate labor pools when viewed by served end market.

Public evidence, transparent CPU calculations, and a local dashboard are sufficient for the first campaign. New hardware, GPU training, paid data subscriptions, public deployment, and external outreach are not prerequisites. Treat unavailable resources as specific research gaps.

## 4. Workstream A: map physical labor and productive processes

### Questions

- Where are physical labor, compensation, productive output, and operating constraints concentrated by end market and value-chain stage?
- Which work is performed internally, outsourced, subcontracted, or supplied through shared service networks?
- Which operating environments differ in variability, standardization, scale, fragmentation, asset intensity, and customer access?
- Where would humanoids substitute for existing labor, complement people, relieve an output constraint, enable additional service, or support process redesign?
- Which digital workflows must change alongside physical deployment, and which can improve independently?

### Required treatment

Build industry/occupation crosswalks as an accounting and evidence foundation. Preserve classification vintages and parent/child relationships. Occupations are an access route to labor data; the user-facing research remains organized by end market and value-chain stage.

Distinguish measured employment, hours worked, estimated physical-work shares, wages, employer compensation, and useful output. If physical hours are estimated as employment × annual hours × physical-work share, give each factor its own evidence or assumption and range. Unknown hours or work shares remain visible. Do not infer time shares from task counts or importance ratings.

Define allocation weights for outsourced work and activities shared across markets. Within one accounting view, weights must reconcile, including an explicit unallocated share where necessary. A 3PL's employment and the same work viewed as part of a customer's value chain are alternative descriptions of one underlying activity. Industry revenues, intermediate sales, value added, labor spending, and robotics-provider revenue remain distinct measures.

### Output

An end-market atlas with dated denominators, value-chain maps, operating archetypes, qualitative deployment theses, coverage status, and a documented route from source data to each interpretation.

## 5. Workstream B: current capabilities and improvement pathways

### Questions

- Which configured humanoid systems can currently serve relevant work, and what is known about sustained productive operation?
- Which dimensions prevent further entry: manipulation, payload, mobility, endurance, long-horizon reliability, recovery, adaptation, integration effort, or human intervention?
- How could data diversity, training/inference compute, model design, hardware, control, simulation, and workflow redesign change those dimensions?
- Which improvements transfer across embodiments, environments, software generations, and customer sites?
- Where do specialized robots, mobile manipulators, fixed automation, environmental changes, or human-machine combinations remain stronger alternatives?

### Evidence and scaling design

Use a provider/system registry with separate hardware, software, autonomy, integration, and evidence versions. Keep demonstrations, trials, production operations, orders, shipments, and planned capacity distinct. Record the population and conditions each observation supports. Do not promote undisclosed teleoperation or setup assistance into an autonomous capability claim.

Investigate scaling as a family of conditional response relationships. Relevant inputs can include effective experience, diversity, model/training resources, embodiment, control architecture, and deployment context; outputs include reliability, intervention burden, adaptation effort, useful throughput, and reachable work.

Maintain three explicit categories:

1. **Empirical relationship:** estimated from comparable observations, with tested domain, fit method, uncertainty, and held-out checks where feasible.
2. **Mechanistic relationship:** a specified causal or operating model whose assumptions can be examined.
3. **Scenario assumption:** an uncalibrated trajectory used to explore consequences.

Fit a power law only where the data and comparison support it. Also consider thresholds, saturation, diminishing returns, hardware limits, distribution shift, and correlated failures. A benchmark trend is not a universal humanoid improvement exponent or an automatic commercial productivity forecast.

The linkage is explicit: an assumed improvement changes particular capability requirements, which changes eligible market-stage configurations, operating outcomes, costs, and subsequent adoption. Preserve an unchanged-capability case and cases with limited transfer. Retrofit and software compatibility determine whether existing fleets share in an improvement.

### Output

A capability evidence map, a scaling-literature assessment, alternative progress scenarios, and market-stage threshold maps stating what must improve before each deployment stage becomes plausible.

## 6. Workstream C: staged penetration and deployment portfolios

### Questions

- What fraction of relevant physical work is serviceable under each specified system and process configuration?
- Which configurations are economically attractive to both the customer and provider, and which customers are ready to implement them?
- What limits actual rollout: robot supply, installation/integration teams, service coverage, human support, working capital, financing, or buyer readiness?
- How should a humanoid company sequence end markets and value-chain stages when opportunities compete for those shared resources?
- How do substitution, complementary productivity, demand expansion, and newly feasible services contribute differently?

### Waterfall and stock-flow structure

For each dated, matched cohort, show relevant physical work → capability-compatible work → feasible production configurations → economically attractive configurations → operationally ready demand → deliverable capacity → installed and retained productive capacity → realized useful output and labor effects.

A waterfall uses a consistent denominator within a panel. If the model changes from hours to sites, robots, output, or currency, expose the conversion and its assumptions in a linked panel. Conditional gates are not independent percentages. Model joint eligibility or explain conditional estimates for a matched cohort, and show which constraint binds.

Pair the waterfall with deployment stages: bounded assisted operation, repeatable productive operation, integrated multi-robot workflows, coordinated physical-digital processes, and more extensive enterprise redesign. These are analytical stage labels, not a mandatory universal ladder. Markets can enter through different configurations, pause, regress, or skip an arrangement.

Track installations, ramp, active capacity, replacements, retirement, and retention separately. Apply common supply and support budgets across all market allocations. Useful output depends on utilization, reliability, process bottlenecks, and demand. Avoid independently forecasting each market as if it had exclusive access to the same hardware, capital, integration, and supervision capacity.

Keep a fixed-baseline substitution view separate from demand expansion and new services. Displaced activity, reassigned human time, removed payroll, customer savings, provider revenue, and total economic surplus require distinct calculations. Financing feasibility and cash timing can limit otherwise attractive expansion.

### Output

Reproducible scenario waterfalls, capability-dependent stage maps, constrained deployment portfolios, and conclusions about which sequences are attractive under which conditions.

## 7. Workstream D: data aggregation, learning, and control

### Questions

- Which market-stage deployments produce experience that is useful for other deployments?
- Which observations, demonstrations, corrections, failures, and simulations are worth acquiring at the margin?
- Who can collect, combine, train on, reuse, and commercialize that experience?
- How do standardized interfaces and evaluation conditions affect the usefulness of aggregated fleet data?
- When should immediate production, experimentation, evidence acquisition, and policy improvement receive scarce resources?

### Required treatment

Represent directed transfer between source and receiving capabilities/system contexts. Separate data quantity, diversity, novelty, quality, learning effect, operating effect, and captured economic value. Semantic similarity alone does not establish transfer. Unknown edges remain unknown; a no-transfer scenario is an explicit assumption, not a claim of observed zero transfer.

Compare deployment policies with and without the proposed learning opportunity, including collection, processing, training, evaluation, and implementation costs. If learning benefits already change future cash flows, do not add a second data-value premium. Distinguish capability improvement from information that changes a later investment decision.

Model both directions: current capabilities and control arrangements determine where deployment is possible; deployment choices determine the experience available for later improvement. Include negative feedback such as additional exceptions, distribution shift, maintenance, and operator congestion.

### Output

An evidence-labeled deployment/learning network, candidate data-aggregation arrangements, and scenarios showing when learning changes the preferred market-entry sequence.

## 8. Workstream E: physical-digital fleets and productive coordination

### Questions

- Which market-stage processes benefit from robots and software agents acting as a coordinated system?
- What should be decided locally, at workcell/fleet level, or by enterprise-wide resource allocation?
- How do digital agents change planning, order handling, inventory, procurement, dispatch, exception handling, maintenance, and evaluation?
- When do shared supervision, queues, communication, correlated failure, and recovery limit fleet productivity?
- How does the preferred process design change as physical and digital capabilities improve at different rates?

### Required treatment

Compare the same process under human-led operation, digital-agent assistance, isolated robotic deployment, mixed fleets, and coordinated physical-digital operation where relevant. Specify dependencies and shared resources. Avoid adding a digital productivity uplift and a robot uplift when both describe the same removed work or bottleneck.

Define the decision architecture, evidence available to each participant, operating objectives, constraints, and feedback. Compare simple rules, centralized scheduling, hierarchical control, and decentralized allocation where they answer the question. A named swarm architecture is a design candidate until its productive contribution is established.

Treat coordination effectiveness as a scenario variable separate from robot competence and learning transfer. A larger fleet can increase output and also create congestion or shared failure exposure. Evaluate reliability and operating slack alongside average utilization.

### Output

Physical-digital process maps, coordination archetypes by end market, and at least one transparent mechanism model connecting coordination to productive capacity and deployment economics.

## 9. Workstream F: ownership, competitive structure, and investment

### Questions

- Where are incumbents best positioned to adopt, and which assets or constraints explain that position?
- When does acquiring and transforming an existing business offer access, cash flow, data, and process control worth the acquisition and transformation costs?
- When can a new enterprise designed around AI gain share or create new demand despite customer acquisition, asset, and financing requirements?
- How can these structures coexist within an end market or occupy different value-chain stages?
- Where should a humanoid provider sell equipment, provide a service, partner with an operator, or own parts of the operating system?

### Common comparison

Compare incumbent adoption, acquisition/holdco transformation, and newco formation against matched customer outcomes. Treat provider-owned robotics-as-a-service, leasing, partnerships, and platform roles as arrangements that can overlay these routes; they are not always mutually exclusive categories.

Evaluate capital intensity, asset specificity, brownfield conversion, process standardization, customer/distribution access, market fragmentation, data/learning rights, financing, residual values, integration burden, and demand uncertainty. Include the time and resources required for transition, not only an imagined steady state.

Separate value creation from value capture. Identify the owner of operating assets, robot assets, models, data access, and customer relationships. Acquisition price may already reflect part of the expected improvement; new enterprises may need to fund customer acquisition and spare capacity. Robotics providers and end-market operators can have different preferred arrangements.

The output is a conditional view of which structures are advantaged and when. It is not a universal winner, a recommendation to acquire a specific business, or a claim that value created necessarily becomes investor return.

### Output

Market-stage comparisons of deployment/ownership routes, coexistence scenarios, capital and control maps, and strategic implications for a humanoid company.

## 10. Integrated interpretation and standards of progress

For each material conclusion, state the mechanism, supporting evidence, competing explanation, confidence, pivotal assumptions, and observation that would change the view. Distinguish a measured result from an inference and from a scenario.

Use one versioned data and calculation source for report tables, dashboard visuals, and exports. The dashboard must allow movement from an end-market conclusion to the source observations and assumptions behind it. A scenario change should recompute the affected outputs or explicitly explain why it does not.

The initial report should answer: where is physical labor concentrated; what can current systems plausibly serve; what improvements unlock further stages; what slows deployment after capability is available; how do fleets, learning, and digital coordination change sequencing; and which organizational structures are advantaged by market and stage?

Measure research progress through improved explanations, validated mechanisms, better-constrained assumptions, and changed strategic judgments. Preserve disagreements and negative findings. Do not require a physical robot demonstration or a completed microeconomic case before the program can contribute.

The first week's executable specification is `WEEK_ONE_RESEARCH_SPEC.md`. Its launch text is `CODEX_GOAL.md`. Open questions and longer investigations live in `RESEARCH_ROADMAP.md`. Those files describe planned work until an actual campaign records evidence and outputs.

## 11. Initial source anchors

These are starting sources and methodological anchors checked during design preparation. The campaign must verify available vintages at kickoff, preserve the versions actually used, and expand the evidence base. This list does not constitute a completed literature review or market assessment.

- [BLS OEWS industry-specific tables](https://www.bls.gov/oes/2025/may/oessrci.htm) and [technical notes](https://www.bls.gov/oes/2025/may/oes_tec.htm): employment/wage baseline with scope and classification limits. Employment counts are not physical-work hours or full-time equivalents, and wages are not fully loaded compensation.
- [BLS National Employment Matrix](https://www.bls.gov/emp/tables/industry-occupation-matrix-industry.htm): alternative/supplementary coverage and industry-occupation relationships. Reconcile overlap with OEWS; distinguish historical base-year estimates from published projections.
- [O*NET database](https://www.onetcenter.org/database.html), [crosswalks](https://www.onetcenter.org/crosswalks.html), and [task-frequency definitions](https://www.onetcenter.org/dictionary/31.0/csv/task_categories.html): work descriptions and operating contexts. Frequency-category responses are not percentages of working time.
- [Data Scaling Laws in Imitation Learning for Robotic Manipulation](https://arxiv.org/html/2410.18647v3): evidence about particular manipulation-policy scaling experiments. Data diversity and demonstration counts need separate treatment; fitted domains and extrapolation must remain visible.
- [Open X-Embodiment / RT-X](https://arxiv.org/html/2310.08864): conditional transfer research. Specify source and target contexts rather than assuming cross-market generalization.
- [DataMIL](https://robin-lab.cs.utexas.edu/datamodels4imitation/): task- and policy-dependent data selection. A performance influence estimate requires a separate economic interpretation.
- [Using Goals in Codex](https://developers.openai.com/cookbook/examples/codex/using_goals_in_codex) and [long-running work](https://learn.chatgpt.com/docs/long-running-work): a goal needs observable outputs, verification, checkpoints, and explicit completion/blocker states. Actual continuation depends on the runtime, available resources, and goal state.

## 12. Decision record

Accepted correction: organize the research around physical labor end markets, value chains, staged deployment, evolving capability, learning/control, physical-digital coordination, and competing ownership routes. Superseded sequencing: mandatory warehouse-first case, second-market deferral, and dashboard only after that case. Preserved disciplines: dated evidence, transparent assumptions, consistent units and populations, conditional adoption gates, no double-counting, and separate implementation-repository scope.

Prepared outcome: a revised program and a launchable first-week specification. Pending outcome: activation and execution of the research campaign in Codex, followed by the actual report, dashboard, model, and revised roadmap.
