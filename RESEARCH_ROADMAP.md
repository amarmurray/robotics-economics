# Robotics economics research roadmap

Version 1.2 · Prepared 25 October 2026. **All 31 questions below are OPEN.** This document specifies investigations; it does not claim completed research or execution.

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

## 6. Customer ownership, organization, and adoption

| ID and question | Decision relevance | Evidence and method | Boundary, dependencies, and completion trigger |
| --- | --- | --- | --- |
| RQ-OS-01: How do customer ownership and governance affect adoption within a market-stage cell? | Explain capital access/allocation, investment criteria and automation appetite, rather than assigning an effect to a label. | Build adopter profiles; compare financeability, willingness, operating authority and implementation capacity under matched technical conditions; retain opposing mechanisms and selection limits. | W1 structural comparison alongside PL-03 and SP-01. Complete when relevant actor levels, mechanisms, unknowns, and alternative explanations are explicit. |
| RQ-OS-02: Who can authorize process changes and retain adoption and learning benefits? | Identify parent, operator, site, buyer and beneficiary constraints that change readiness and rollout. | Map governance, procurement, premises/workflow control, investment responsibility, data access and gain retention; join BM-02's rights map. | W1 customer-decision map after PL-03 and DL-01 scope definition. Deepen with disclosed operating/governance evidence. |
| RQ-OS-03: How do incumbent adoption, acquisition/holdco transformation, and AI-native entry change customer value-chain position? | Test ownership and organization as both causes and consequences of automation. | Compare acquisition, organic expansion, outsourcing and entry under common output assumptions; include capital, transition and customer-acquisition costs; conserve activity under reclassification. | W1 pathway hypotheses after OS-01 and PL-04 scope definition. Deeper alongside BM-03; complete a bounded case when transition mechanisms and costs are inspectable. |
| RQ-OS-04: Which customer structures coexist, consolidate, specialize, or gain share as automation improves? | Connect customer heterogeneity to market penetration and competitive structure. | Model activity-weighted customer cohorts, entry/exit and role transitions; test fixed composition against changed composition without double-counting labor. | W1 conditional hypotheses after OS-01/03 and SP-01. Deeper with observed adoption, financing, acquisition and entry evidence. |
| RQ-OS-05: Where can a customer-side AI-native operating newco win through production design, adoption timing, or capacity availability? | Test entrepreneurial entry by market/stage, including ordinary robots available to incumbents on the same terms. | Compare useful-output economics and customer propositions against legacy and robot-adopting incumbents; model demand won, delivered output, competitive response, and persistence of any advantage. | W1 bounded entrant case after OS-01/03, HC-02 and SP-01 scope definition. Deeper when customer access, operating exposure and response timing can be bounded. |
| RQ-OS-06: What capital and milestones can support formation and scaling of a humanoid-enabled operating newco? | Separate economic attractiveness, financeability, actual capital access, and survival through ramp. | Model enterprise and robot-asset funding, working capital, ramp losses, runway, customer acquisition and expansion; test delay and funding-gap scenarios with BM-01/02. | W1 conditional financing case alongside OS-05. Financing terms remain assumptions until evidenced; deepen with disclosed comparable terms or authorized operating data. |
| RQ-OS-07: When should an industrial AI operating platform create new businesses, acquire incumbents, or combine routes? | Evaluate a physical/industrial Thrive-like model without conflating a new holdco with new operating capacity. | Compare capital, time to customers, inherited constraints, shared engineering/procurement/learning, overhead and competition; distinguish standalone, newco-builder, acquisition and hybrid forms. | W1 structural comparison after OS-03 and OS-05/06 scope definition, linked to BM-03. Primary-source analogies frame hypotheses; deeper work requires demonstrated cross-business effects. |

## 7. Robotics business models, asset ownership, and value capture

| ID and question | Decision relevance | Evidence and method | Boundary, dependencies, and completion trigger |
| --- | --- | --- | --- |
| RQ-BM-01: Which commercial arrangements fit different customer structures and adoption constraints? | Compare equipment sales, leases, services, usage/outcome pricing, software, managed operations and partnerships. | Join adopter profiles to matched-output economics; trace capital, support, utilization, cash timing and risk across parties. | W1 cross-comparison alongside OS-01/02 and SP-02. Deepen when commercial terms and performance exposure are observable. |
| RQ-BM-02: How do asset ownership, operational control and model/data rights allocate costs, risks and gains? | Preserve the prior asset/control/learning-value inquiry and explain bargaining positions. | Use one actor/role and rights map for customer, provider, operator, integrator and financier; distinguish business ownership from robot ownership and access rights. | W1 rights-and-value map after DL-01 and FD-02 scope definition; joins OS-02. Disclosed terms or authorized evidence trigger deeper comparison. |
| RQ-BM-03: When does a robotics provider benefit from owning or operating a productive business rather than supplying it? | Preserve the prior provider-integration question; test feedback and control benefits against capital and organizational burden. | Compare sell, partner, managed-operation and integration routes; include acquisition/greenfield capital, customer access, learning rights, transition time and opportunity costs. | Deeper after BM-01/02, OS-03 and DL-04 scope definition. Complete with counterexamples and explicit break-even conditions. |
| RQ-BM-04: Where can durable value be captured across robotics provision, operation, integration, software and finance? | Explain conditional investment outcomes and coexistence among integrated firms and specialists. | Reconcile value creation and participant cash flows; examine specialization, interoperability, switching, competition and alternatives; distinguish transfers from additional value. | W1 competing hypotheses after BM-01/02. Deeper with terms, utilization, operating costs and competitive evidence. |

### Scope clarification and continuity

On 25 October 2026 Amar clarified that customer ownership/organization affects adoption and value-chain position, and explicitly retained the previous ownership analysis under a separate category. OS-01 through OS-04 now address customer structures and their transitions. The prior asset/control/learning-rights inquiry continues in BM-02; the prior provider-owning-operations question continues in BM-03; commercial structures and supplier/operator coexistence continue in BM-01/04. Earlier wording remains in repository history. These scope changes do not mark any question answered.

The subsequent AI-native-entry clarification adds OS-05/06/07. It preserves standalone customer newcos, newco-building platforms, acquisition and hybrid routes; explicitly tests equal access to robots, incumbent adoption delays, differentiated production, labor-capacity conditions, financing, and competitive response. These additions remain OPEN.

Use common actor and cohort IDs across OS and BM. A provider can also be an operator or adopter; several roles do not imply several independent labor pools, revenue opportunities or sources of finance.

## Recommended follow-on campaigns

1. **Comparative production and penetration.** Combine PL, HC, and SP across contrasting value chains. Graduate from maps to quantitative cohorts when labor denominators, capability requirements, and shared constraints can be reconciled. Produce conditional penetration scenarios and identify their strongest disconfirming observations.
2. **Learning and coordinated fleets.** Combine DL and FD. Begin with access and evaluation feasibility; then compare aggregation, deployment selection, and supervision policies. Graduate to experiments only with authorized data, compatible measurements, and a credible baseline. Simulation remains labeled synthetic evidence.
3. **Customer structures, robotics business models, and competition.** Combine OS and BM with the first two campaigns. Compare customer ownership/governance, incumbent/acquisition/newco pathways, explicit entrant financing and competition, and commercial/asset/control arrangements as linked dimensions. Test standalone newco and platform formation, acquisition and hybrid routes with the Thrive analogy labeled as a comparator. Graduate when adoption and value-capture differences follow from explicit mechanisms, rights, costs, and capabilities; retain market-specific coexistence outcomes.

## Question lifecycle and refresh

Maintain a question ledger containing ID, status, scope, owner, evidence snapshot, dependencies, findings, competing explanations, artifacts, and next trigger. Use OPEN, ACTIVE, BOUNDED ANSWER, BLOCKED ON EVIDENCE, and RETIRED/SUPERSEDED. Preserve earlier conclusions and explain revisions.

Pending access questions include intervention logs, deployment exposure, maintenance records, controlled transfer evaluations, pricing, data rights, and workflow observations. Record the required population, measurement, access route, and consequence of absence. Do not infer missing values from silence or treat vendor claims as independent observations.

Refresh during authorized sessions after relevant provider versions, datasets, papers, deployment results, contracts, or contradictory observations arrive. Check applicability before changing assumptions. Recompute affected scenarios, preserve historical versions, and record changed rankings, penetration stages, or ownership comparisons. Announcements alone do not validate extrapolations.

Reprioritize after the first-week review and each campaign using the criteria above. Expand with comparable evidence; retire questions lacking decision relevance. This roadmap authorizes no periodic polling, background execution, data access, hardware activity, or implementation-repository changes.
