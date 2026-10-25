# Robotics economics research roadmap

Version 1.0 · Prepared 25 October 2026. **All 24 questions below are OPEN.** This document specifies investigations; it does not claim completed research or execution.

[RESEARCH_PROGRAM_DESIGN.md](RESEARCH_PROGRAM_DESIGN.md) defines the program. [WEEK_ONE_RESEARCH_SPEC.md](WEEK_ONE_RESEARCH_SPEC.md) defines the initial report, dashboard, and supporting artifacts. This roadmap supplies the continuing question portfolio.

Research begins with end markets, value chains, and physical labor organization. Task decomposition supports measurement and explanations; a warehouse case is not a prerequisite for broader investigation.

## Scope and priority

**W1** means a bounded first-week answer, map, or scaffold using accessible evidence. **Deeper** requires additional evidence, validation, or modeling, without a promised calendar date. Scaffolds expose missing inputs and blocked decisions; they are not empirical answers.

Prioritize by decision impact, resolvable uncertainty, tractability and data availability, and dependencies. Record separate judgments and a reasoned ordering, not an allegedly objective weighted sum. Prefer questions clarifying several downstream decisions; retain valuable inaccessible questions.

Dependencies reference stable question IDs. “Complete” means bounded completion with sources, counterarguments, limitations, and a next trigger, never permanent settlement.

## 1. Physical labor, end markets, and value chains

| ID and question | Decision relevance | Evidence and method | Boundary, dependencies, and completion trigger |
| --- | --- | --- | --- |
| RQ-PL-01: Where does physical labor sit across major end markets and value-chain stages? | Establish the opportunity universe before selecting deployments. | Combine industry, occupation, hours, and workflow evidence; reconcile overlapping populations. | W1 map. No prerequisite. Complete when coverage, denominator choices, and material gaps are visible. |
| RQ-PL-02: Which activities recur across otherwise different value chains? | Identify shared capabilities without erasing environmental differences. | Compare handling, inspection, movement, setup, cleaning, and recovery across markets; document exceptions. | W1 taxonomy after PL-01. Deeper validation when comparable operating observations become available. |
| RQ-PL-03: Who buys, performs, and benefits from each activity? | Prevent duplicated labor pools and misplaced revenue estimates. | Trace customers, contractors, site operators, and beneficiaries; reconcile hours, spending, and output. | W1 bounded accounting after PL-01. Complete with worked cross-market reconciliation and unresolved allocation rules. |
| RQ-PL-04: Where would process redesign alter the opportunity more than worker substitution? | Compare existing operations with purpose-built production arrangements. | Map workflows, complements, demand limits, and redesign costs; compare equivalent useful outputs. | Deeper, after PL-02/03. Advance when two contrasting processes have defensible baselines. |

## 2. Humanoid capability progression and scaling

| ID and question | Decision relevance | Evidence and method | Boundary, dependencies, and completion trigger |
| --- | --- | --- | --- |
| RQ-HC-01: What capabilities are demonstrated for dated system configurations? | Separate available capabilities from announcements and aspirations. | Build versioned observations of autonomy, throughput, reliability, recovery, and assistance; retain test conditions. | W1 evidence matrix in parallel with PL-01/02; iteratively join the evolving market map. Complete with explicit unknowns and comparison limits. |
| RQ-HC-02: Which capability improvements unlock new workflow coverage? | Identify discontinuities in addressability rather than extrapolating headline specifications. | Map capability requirements and complementary thresholds; test alternative progression sequences. | W1 hypothesis scaffold after HC-01. Deeper upon repeated, comparable performance evidence. |
| RQ-HC-03: What limits scaling from demonstrations to sustained operation? | Distinguish software improvement from durability, power, support, manufacturing, and integration constraints. | Analyze failure, intervention, uptime, yield, and maintenance evidence; model interacting bottlenecks. | Deeper after HC-01. Complete a bounded comparison when exposure denominators and failure conditions are available. |
| RQ-HC-04: How portable are improvements across bodies, software versions, and environments? | Estimate upgrade value and avoid treating every installed robot as current-generation capacity. | Compare transfer evaluations, compatibility, retraining, validation, and retrofit requirements. | Deeper after HC-01/02. Trigger on comparable version changes; retain no-transfer scenarios. |

## 3. Staged penetration and shared constraints

| ID and question | Decision relevance | Evidence and method | Boundary, dependencies, and completion trigger |
| --- | --- | --- | --- |
| RQ-SP-01: What distinguishes successive penetration stages in each value chain? | Define testable transitions from isolated activity to integrated production. | Specify capability, economics, organizational, and evidence gates; distinguish deployment depth from adoption breadth. | W1 stage map after PL-01 and HC-02. Complete when transition criteria are observable. |
| RQ-SP-02: Which constraints bind several markets simultaneously? | Prevent independent adoption forecasts from consuming the same scarce resources. | Map manufacturing, capital, integration, service, energy, and operator capacity; reconcile allocations. | W1 constraint scaffold after SP-01. Deeper quantification requires capacity and utilization evidence. |
| RQ-SP-03: How do learning, cash generation, and capacity expansion interact? | Explain acceleration, congestion, and stalled rollout. | Build conditional stock-flow scenarios with installation, retirement, reinvestment, and support limits. | Deeper after SP-02 and DL-04. Complete when conservation checks and adverse scenarios hold. |
| RQ-SP-04: Where do humans and specialized automation remain complements or preferred alternatives? | Avoid equating humanoid feasibility with adoption or displacement. | Compare matched outcomes, flexibility, process changes, and switching costs by cohort. | W1 competing hypotheses after PL-02 and HC-01. Deepen where evidence could reverse a penetration scenario. |

## 4. Data aggregation, transfer, and deployment selection

| ID and question | Decision relevance | Evidence and method | Boundary, dependencies, and completion trigger |
| --- | --- | --- | --- |
| RQ-DL-01: Who can collect, aggregate, reuse, and learn from deployment data? | Identify feasible learning networks and beneficiaries. | Trace contractual rights, access boundaries, formats, incentives, and demonstrated reuse. | W1 rights map. Public disclosure gaps remain pending; contracts or authorized interviews trigger revision. |
| RQ-DL-02: Which experience transfers across value chains, and why? | Distinguish fleet size from useful learning diversity. | Construct directed transfer hypotheses; seek held-out evaluations, negative transfer, and embodiment controls. | W1 hypotheses after PL-02 and HC-04 scope definition. Deeper validation requires comparative data. |
| RQ-DL-03: When does aggregation improve learning more than local specialization? | Evaluate shared models, data pooling, and local adaptation. | Compare coverage, redundancy, label quality, distribution shift, and aggregation costs. | Deeper after DL-01/02. Complete a bounded result only with comparable evaluation conditions. |
| RQ-DL-04: Which deployments should be selected for production and learning together? | Evaluate current output against future capability and information gains. | Compare deployment portfolios with no-learning baselines, incremental costs, and alternative explanations. | W1 decision scaffold after DL-01/02. Deeper modeling when gains can be bounded without double counting. |

## 5. Physical and digital fleet coordination

| ID and question | Decision relevance | Evidence and method | Boundary, dependencies, and completion trigger |
| --- | --- | --- | --- |
| RQ-FD-01: Where do digital agents and physical robots share a production workflow? | Locate complementary planning, transaction, sensing, and execution work. | Map information and material flows, handoffs, authorities, and customer outcomes. | W1 architecture map after PL-02/03. Complete with concrete cross-market examples and evidence labels. |
| RQ-FD-02: Which decisions belong locally, centrally, or with human supervision? | Relate coordination architecture to latency, resilience, and learning. | Compare scheduling, control, intervention, and model-update timescales; specify failure modes. | W1 competing designs after FD-01. Deeper testing requires observed workloads and communications constraints. |
| RQ-FD-03: When do shared supervision and coordination become bottlenecks? | Test whether apparent fleet economies survive correlated exceptions. | Model queues, intervention duration, common failures, communications, and escalation capacity. | Deeper after FD-02 and HC-03. Complete with workload sensitivity and correlated-failure stress cases. |
| RQ-FD-04: Which workflows become possible only through joint physical-digital redesign? | Examine new productive arrangements beyond separate automation tools. | Compare integrated and fragmented process designs, control boundaries, costs, and adoption requirements. | Deeper after PL-04 and FD-01/02. Advance when a falsifiable comparison can be specified. |

## 6. Ownership and competitive structures

| ID and question | Decision relevance | Evidence and method | Boundary, dependencies, and completion trigger |
| --- | --- | --- | --- |
| RQ-OS-01: How do incumbent adoption, an acquisition-led holdco, and a native newco compare? | Separate installed customer access from redesign freedom and integration costs. | Compare equal-output scenarios, capital needs, organizational constraints, and learning access. | W1 structural comparison after PL-03/04 scope definition. Unknown advantages remain hypotheses. |
| RQ-OS-02: Which ownership boundaries determine who captures learning gains? | Distinguish hardware ownership from control, customer relationships, and data rights. | Map asset, software, workflow, financing, and data contracts; examine bargaining alternatives. | W1 rights-and-value map after DL-01 and FD-02. Deeper upon disclosed terms or authorized evidence. |
| RQ-OS-03: When does owning operations create an advantage over selling robots or software? | Test integration benefits against capital intensity and organizational burden. | Compare deployment feedback, distribution, margins, learning access, and opportunity costs. | Deeper after OS-01/02 and DL-04. Complete with explicit counterexamples and break-even conditions. |
| RQ-OS-04: What supports coexistence among integrated firms, platforms, operators, and specialists? | Avoid assuming one ownership model dominates every market. | Examine heterogeneity, interoperability, multi-homing, specialization, and competitive responses. | W1 competing hypotheses after OS-01/02. Deeper scenarios follow observed switching and partnership evidence. |

## Recommended follow-on campaigns

1. **Comparative production and penetration.** Combine PL, HC, and SP across contrasting value chains. Graduate from maps to quantitative cohorts when labor denominators, capability requirements, and shared constraints can be reconciled. Produce conditional penetration scenarios and identify their strongest disconfirming observations.
2. **Learning and coordinated fleets.** Combine DL and FD. Begin with access and evaluation feasibility; then compare aggregation, deployment selection, and supervision policies. Graduate to experiments only with authorized data, compatible measurements, and a credible baseline. Simulation remains labeled synthetic evidence.
3. **Ownership, organization, and competition.** Combine OS with the first two campaigns. Compare incumbents, holdcos, native newcos, and mixed structures under common production assumptions. Graduate when differences follow from explicit rights, costs, and capabilities rather than narrative preference; retain market-specific coexistence outcomes.

## Question lifecycle and refresh

Maintain a question ledger containing ID, status, scope, owner, evidence snapshot, dependencies, findings, competing explanations, artifacts, and next trigger. Use OPEN, ACTIVE, BOUNDED ANSWER, BLOCKED ON EVIDENCE, and RETIRED/SUPERSEDED. Preserve earlier conclusions and explain revisions.

Pending access questions include intervention logs, deployment exposure, maintenance records, controlled transfer evaluations, pricing, data rights, and workflow observations. Record the required population, measurement, access route, and consequence of absence. Do not infer missing values from silence or treat vendor claims as independent observations.

Refresh during authorized sessions after relevant provider versions, datasets, papers, deployment results, contracts, or contradictory observations arrive. Check applicability before changing assumptions. Recompute affected scenarios, preserve historical versions, and record changed rankings, penetration stages, or ownership comparisons. Announcements alone do not validate extrapolations.

Reprioritize after the first-week review and each campaign using the criteria above. Expand with comparable evidence; retire questions lacking decision relevance. This roadmap authorizes no periodic polling, background execution, data access, hardware activity, or implementation-repository changes.
