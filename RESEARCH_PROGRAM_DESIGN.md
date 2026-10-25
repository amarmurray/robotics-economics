# Physical labor, humanoid deployment, and the organization of production

Version 0.7 · 25 October 2026 · Research program design

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
- Treat ownership first as the ownership, governance, and organization of the customer adopting humanoids. Investigate how capital access and allocation, investment appetite, decision rights, implementation capacity, and value-chain position affect adoption by end market and stage.
- Preserve the distinct research on robotics business models, asset ownership, commercial arrangements, and value capture among providers, operators, integrators, and financiers. Customer structure and commercial arrangements interact; neither replaces the other.
- Compare incumbent adoption, acquisition/holdco transformation, and AI-native enterprise formation as customer development pathways. These are not mutually exclusive ownership categories. Permit coexistence and specialization across value-chain stages.
- Deliver a substantive written report, an interactive dashboard with meaningful toggles, reproducible supporting artifacts, and a continuing research roadmap after an initial seven-day campaign.

These requirements govern the design. Geographic defaults, coverage targets, forecasting horizons, and particular implementation choices below are revisable working assumptions, not additional user commitments. Preparing this design does not start the seven-day run or claim its outputs exist.

## 2. Organizing hierarchy and research boundaries

The primary analytical cell is:

`end market × value-chain stage × operating archetype × geography × time`

Within each cell, distinguish customer/adopter cohorts by ownership, governance, operating organization, and value-chain role. These attributes stratify the economic map; they do not replace its end-market organizing level. Parent, operating company, site operator, procurement buyer, and beneficiary may be different actors.

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
- How do customer ownership, capital allocation, automation appetite, operating authority, and implementation capacity change readiness, adoption depth, timing, and scale within a market-stage cell?
- How should a humanoid company sequence end markets and value-chain stages when opportunities compete for those shared resources?
- How do substitution, complementary productivity, demand expansion, and newly feasible services contribute differently?

### Waterfall and stock-flow structure

For each dated, matched cohort, show relevant physical work → capability-compatible work → feasible production configurations → economically attractive configurations → operationally ready demand → deliverable capacity → installed and retained productive capacity → realized useful output and labor effects.

A waterfall uses a consistent denominator within a panel. If the model changes from hours to sites, robots, output, or currency, expose the conversion and its assumptions in a linked panel. Conditional gates are not independent percentages. Model joint eligibility or explain conditional estimates for a matched cohort, and show which constraint binds.

Stratify adoption cohorts by customer profile where evidence supports it. Aggregate penetration using compatible activity weights, not unweighted counts of businesses or overlapping ownership labels. Compare fixed customer composition with explicit acquisition, entry, exit, and repositioning scenarios. Reclassifying an acquired operation does not create a second labor pool. Changes to ownership may change the feasible operating configuration; expose that mechanism rather than attaching a universal adoption multiplier to a label.

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

## 9. Workstream F: customer ownership, organization, and adoption

### Scope and questions

The primary subject is the business adopting humanoids to produce goods or services. Investigate its ownership and governance, financing relationships, operating organization, and location in the value chain. The customer's legal owner, economic sponsor, capital allocator, process controller, buyer, site operator, and beneficiary need not be the same actor.

- How do customer structures differ within an end market and value-chain stage, and which mechanisms change adoption readiness, timing, depth, and scale?
- Who can finance deployment, who wants to invest, who has authority to change the process, and who can implement the change? Keep these four questions distinct.
- How do investment horizons, competing capital demands, procurement, managerial incentives, risk appetite, and ability to retain gains affect the chosen deployment?
- How do incumbent adoption, acquisition/holdco transformation, and AI-native enterprise formation alter the customer's operating model and value-chain position?
- Which customer structures coexist, consolidate, enter, specialize, or move into adjacent stages as automation becomes feasible?

### Comparison and causal treatment

Describe ownership/control attributes, market tenure, enterprise formation or transformation, operating organization, and AI-native process design separately. A sponsor-backed holdco may acquire incumbents and also create a new operation. An incumbent may build a new facility; a new entrant may acquire existing assets. Franchise, public, family-controlled, holdco, and AI-native labels describe different dimensions and may overlap.

Test mechanisms from market conditions and customer structure through capital availability/allocation, appetite and investment criteria, authority over workflows and sites, benefit capture, and implementation capacity to deployment decisions and outcomes. These mechanisms can have opposing effects. Do not assume that sponsor backing implies faster adoption, that closely held ownership implies patience, or that organizational scale implies available capital. Evidence about willingness to automate should identify the observed decision or be labeled an assumption.

Compare customer profiles within matched market conditions and, for at least one comparison, a common technical/workload baseline. Then examine explicit redesign and value-chain repositioning scenarios. Keep an explanatory counterfactual separate from evidence of a causal effect: adopters can select into ownership structures, financing, technologies, and markets. Commercial terms from Workstream G can relax one constraint while shifting it to a different party.

Investigate feedback in both directions. Existing ownership and organization affect adoption; feasible automation may alter acquisition attractiveness, entry, outsourcing, vertical scope, and future customer composition. Track control and financing constraints at the relevant parent, operating-company, and site levels. The framework is multivariate and conditional on end market and value-chain stage.

### Output

Customer-structure maps, mechanism-based adoption comparisons, customer-cohort penetration scenarios, and views on value-chain repositioning, competitive structure, coexistence, and investment outcomes. Explain which mechanism changes the deployment decision and what evidence could reverse the conclusion.

## 10. Workstream G: robotics business models, asset ownership, and value capture

### Scope and questions

Preserve the program's prior inquiry into how robotics is supplied, operated, financed, and monetized. This is a distinct research area linked to customer adoption. It covers providers, operating companies, integrators, software/orchestration suppliers, asset owners, and financiers; it is not limited to robot purchase versus lease.

- Which arrangements fit a customer's operating requirements and constraints: equipment sales, leasing, robotics-as-a-service, usage or outcome pricing, integration, software licensing, managed operations, partnerships, or joint ventures?
- Who owns and controls robot assets, models, workflows, customer relationships, and data/learning rights; who funds deployment, bears operating and residual-value risks, and receives the gains?
- When should a robotics provider sell or partner, and when could owning or operating part of the productive business improve outcomes enough to justify capital and organizational demands?
- Where might durable returns accrue across hardware, integration, operation, software, learning, and finance, and what supports coexistence among integrated firms and specialists?

### Common comparison and connection to adoption

Compare arrangements against matched customer outcomes, with customer profiles from Workstream F held explicit. Include deployment investment, acquisition or greenfield capital where applicable, integration, transition time, utilization, support, working capital, financing, residual values, and customer acquisition. Separate value created from the cash flows and risks assigned to each participant. Anticipated improvement can already be reflected in acquisition prices or commercial terms.

Treat business ownership, robot-asset ownership, operational authority, and model/data rights as distinct fields. Leasing or RaaS can change upfront customer cash needs while creating provider or financier requirements; it does not eliminate system-wide capital constraints. Joint ventures can change both customer governance and commercial risk allocation. Record both effects rather than forcing the arrangement into one category.

Use one actor/role map across F and G. A vertically integrated provider can also be an operator or adopter; record its several roles without counting the activity, revenue, financing capacity, or learning gain twice. Customer value-chain repositioning belongs in F; the comparative economics and contractual/control allocation of supplying or operating robotics belongs in G. Reuse the same boundary decision and calculations where these meet.

### Output

Commercial-arrangement comparisons, asset/control/right maps, reconciled customer/provider/operator/financier economics, and conditional value-capture and integration strategies. Connect these results to customer adoption, fleet coordination, learning access, deployment capacity, and market structure.

## 11. Integrated interpretation and standards of progress

For each material conclusion, state the mechanism, supporting evidence, competing explanation, confidence, pivotal assumptions, and observation that would change the view. Distinguish a measured result from an inference and from a scenario.

Use one versioned data and calculation source for report tables, dashboard visuals, and exports. The dashboard must allow movement from an end-market conclusion to the source observations and assumptions behind it. A scenario change should recompute the affected outputs or explicitly explain why it does not.

The initial report should answer: where is physical labor concentrated; what can current systems plausibly serve; what improvements unlock further stages; what slows deployment after capability is available; how do fleets, learning, and digital coordination change sequencing; how do customer ownership and organization change adoption by market and stage; and which robotics business models and control arrangements create and capture value?

Measure research progress through improved explanations, validated mechanisms, better-constrained assumptions, and changed strategic judgments. Preserve disagreements and negative findings. Do not require a physical robot demonstration or a completed microeconomic case before the program can contribute.

The first week's executable specification is `WEEK_ONE_RESEARCH_SPEC.md`. Its launch text is `CODEX_GOAL.md`. Open questions and longer investigations live in `RESEARCH_ROADMAP.md`. Those files describe planned work until an actual campaign records evidence and outputs.

## 12. Initial source anchors

These are starting sources and methodological anchors checked during design preparation. The campaign must verify available vintages at kickoff, preserve the versions actually used, and expand the evidence base. This list does not constitute a completed literature review or market assessment.

- [BLS OEWS industry-specific tables](https://www.bls.gov/oes/2025/may/oessrci.htm) and [technical notes](https://www.bls.gov/oes/2025/may/oes_tec.htm): employment/wage baseline with scope and classification limits. Employment counts are not physical-work hours or full-time equivalents, and wages are not fully loaded compensation.
- [BLS National Employment Matrix](https://www.bls.gov/emp/tables/industry-occupation-matrix-industry.htm): alternative/supplementary coverage and industry-occupation relationships. Reconcile overlap with OEWS; distinguish historical base-year estimates from published projections.
- [O*NET database](https://www.onetcenter.org/database.html), [crosswalks](https://www.onetcenter.org/crosswalks.html), and [task-frequency definitions](https://www.onetcenter.org/dictionary/31.0/csv/task_categories.html): work descriptions and operating contexts. Frequency-category responses are not percentages of working time.
- [Data Scaling Laws in Imitation Learning for Robotic Manipulation](https://arxiv.org/html/2410.18647v3): evidence about particular manipulation-policy scaling experiments. Data diversity and demonstration counts need separate treatment; fitted domains and extrapolation must remain visible.
- [Open X-Embodiment / RT-X](https://arxiv.org/html/2310.08864): conditional transfer research. Specify source and target contexts rather than assuming cross-market generalization.
- [DataMIL](https://robin-lab.cs.utexas.edu/datamodels4imitation/): task- and policy-dependent data selection. A performance influence estimate requires a separate economic interpretation.
- [Using Goals in Codex](https://developers.openai.com/cookbook/examples/codex/using_goals_in_codex) and [long-running work](https://learn.chatgpt.com/docs/long-running-work): a goal needs observable outputs, verification, checkpoints, and explicit completion/blocker states. Actual continuation depends on the runtime, available resources, and goal state.

## 13. Decision record

Accepted correction: organize the research around physical labor end markets, value chains, staged deployment, evolving capability, learning/control, physical-digital coordination, and competing ownership routes. Superseded sequencing: mandatory warehouse-first case, second-market deferral, and dashboard only after that case. Preserved disciplines: dated evidence, transparent assumptions, consistent units and populations, conditional adoption gates, no double-counting, and separate implementation-repository scope.

Ownership clarification, 25 October 2026: customer ownership/organization is an explicit determinant of adoption, capital allocation, automation appetite, and value-chain position. The prior provider/asset/control/value-capture inquiry is retained as Workstream G under a distinct name. This expands the design to seven linked workstreams; it does not delete the earlier questions.

Prepared outcome: a revised program and a launchable first-week specification. Pending outcome: activation and execution of the research campaign in Codex, followed by the actual report, dashboard, model, and revised roadmap.
