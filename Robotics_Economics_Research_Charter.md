# Robotics Economics: Research Charter

Version 0.5 · 6 September 2026 · Amar Murray

This charter establishes a paired Codex and ChatGPT Work research workspace and a first sequence of work. It incorporates deployment economics, fleet learning, market penetration, end markets, provider competition, product generations, and supply chains. Version 0.5 makes the private robotics-economics repository the shared accepted source and uses repository review at the start of each Work session. It retains the research framework and sourced provider reference set from earlier versions. It contains research specifications and selected evidence, rather than a calibrated market forecast. Both app projects and the private repository have been created; actual publication and Work access are tracked separately in the handoff and local operational receipt. Standalone datasets, financial models, and the interactive interface remain planned work. The roadmap supplies context; work begins from the user's current request.

## Purpose and decisions

Develop the judgment, evidence base, and working models needed for strategy, strategic finance, deployment economics, and fleet monetization at a robotics company.

The central question is: **Which deployments should happen, in which sequence, on what commercial terms, and how should their cash generation and learning alter subsequent deployment choices?**

The program connects four decisions:

1. Where customer demand and provider economics support deployment today.
2. Which deployments improve capabilities or information relevant to future markets.
3. Which capital, organizational, and supply constraints determine the feasible pace of expansion.
4. Where value accrues across customers, robot providers, integrators, service networks, and suppliers.

## Paired Codex and ChatGPT Work workspace

Maintain two connected projects for **robotics economics**: the local Codex project **Robotics Economics** and the personal ChatGPT project **robotics economics** used with ChatGPT Work. They form one research program with shared decisions, evidence, and model versions. Use Chat for exploratory discussion and Work for research, analysis, and deliverables. Use Codex for local investigation, reproducible calculations, implementation, verification, and maintaining the canonical files. Both sides may frame questions, conduct research, critique assumptions, and interpret results; these responsibilities are complementary defaults.

The ChatGPT project is [robotics economics](https://chatgpt.com/g/g-p-6a9cdcdb891c819190d2ea406ab0a03c/project). Its instructions direct Work to the private [amarmurray/robotics-economics repository](https://github.com/amarmurray/robotics-economics), whose `main` branch holds the shared accepted state. The canonical local working copy is `/Users/amarmurray/Documents/ChatGPT/Robotics Economics`. At each Work session's start, resolve the current remote `main` HEAD, record its commit SHA, and fetch the charter, handoff, manifest, and other required files at that same SHA through the authorized GitHub connection. An unpushed local edit is not part of the published state. Earlier uploaded project sources and Documents copies are historical snapshots; they are not refreshed as the primary exchange method. Repository access and successful reads must be verified rather than inferred from a project name or URL.

Keep this research program in `amarmurray/robotics-economics`. For implementation that belongs with existing Ixion work, review applicable guidance and existing modules in `robotics-vp/robotics-vp-core` before introducing an additive commercial research area there. Creating the research repository does not authorize changes to the Ixion repository. Keep one registered source for each artifact; record any later migration and retire the former editable location. Review workbooks, Work analyses, and an eventual interactive interface must identify the same underlying dataset, calculation, and repository versions.

| Component | Responsibility |
| --- | --- |
| ChatGPT Work project | Research, discussion, source assessment, scenario framing, interpretation, deliverables, and critique using files fetched at one recorded repository commit |
| Codex local project | Canonical working copy, reproducible analysis, implementation and verification, review of Work findings, and publication of accepted changes |
| Shared handoff record and artifact manifest | Current decision, repository paths and artifact versions, evidence dates, changes, open disagreements, and next owner |
| robotics-economics Git repository | Shared accepted charter, guidance, methods, data schemas, model code, scenario inputs, reproducible results, and research notes on main |
| Existing Ixion Git repository, after scoped review | Implementation assigned to it through an explicit artifact migration or integration decision |
| CSV tables initially | Inspectable end-market, provider, robot-version, deployment, capability, evidence, transfer, and supply records |
| Python and notebooks | Scenario calculations, adoption dynamics, sensitivity analysis, and later stochastic models |
| Excel | Transparent first cash-flow model; finance-facing review and presentation of scenarios |
| Interactive interface, after the first case | Explore end markets, customer workflows, provider positioning, robot generations, adoption waterfalls, transfer paths, and supply constraints |

Begin the financial model in Excel for inspection. When dynamic simulation moves into Python, reconcile the two on fixed cases and make one engine authoritative. Changes made in a review workbook must be deliberately incorporated into that engine. Multiple models or agents should work from explicit file versions and handoffs, with one writer per file at a time.

Use public sources and clearly labeled synthetic cases for this personal program. Its first stages fit the existing CPU-only, docs-first plan and do not depend on new hardware or GPU training.

### Repository exchange and dialogue

Maintain `HANDOFF.md` as the current coordination record and `artifact_manifest.json` as the index of repository-relative paths, local working paths, artifact versions, and content hashes. Commit these records with accepted changes. Keep publication receipts, check timestamps, logs, and incoming-proposal bookkeeping outside the shared research state. Repository commits identify shared versions; no file should try to contain the SHA of its own containing commit.

1. **Start from a known commit.** At the start of each Work session, resolve remote `main` HEAD and read the charter, handoff, manifest, and required files at that exact SHA. Report the SHA used. Re-fetch deliberately if the task needs later changes; do not mix revisions silently. If the repository or a required file is inaccessible, state the failure and missing input rather than treating an old upload or remembered text as current.
2. **Exchange a concrete question and evidence.** Either side prepares a bounded question, findings, source links and dates, assumptions, relevant artifacts, and a requested review or next action. Work returns proposals in its task output, with the input commit SHA. Writing a proposal to `proposals/` requires authorization to write to the repository; a task output does not itself authorize a commit, issue, comment, or other external post. Keep decision-relevant reasoning in the returned artifact or output rather than assuming access to another transcript.
3. **Review and reconcile.** The receiving side checks evidence, units, model behavior, and implications, then returns agreement, a correction, a competing explanation, or a testable next step. Preserve unresolved disagreements. A new proposal remains a proposal until incorporated and verified in the canonical files; it does not silently overwrite an earlier decision.
4. **Publish the accepted state.** Finish each substantive authorized Codex task with appropriate validation, updated accepted artifacts, handoff and manifest, a scoped commit, and a normal push to `main`. Include only the task's accepted changes; unrelated or unaccepted working edits remain untouched. Check remote state before pushing. Preserve divergence or conflicts for explicit reconciliation; do not force-push or auto-merge them. Work-generated changes return for reconciliation before becoming accepted state.
5. **Record publication and consumption separately.** The local operational receipt records actual push verification and any observed Work read, with commit SHA and time. A successful push proves repository publication, not that a Work session has consumed it. Each Work session records the SHA it actually read. Preserve pending publication, unavailable access, and conflicts explicitly. One writer owns each file during an exchange.

The earlier hourly Sync robotics economics automation is PAUSED. There is no periodic polling or source-upload refresh in this workflow. Work reviews the repository when a session begins, and accepted changes are shared through normal commits and pushes at task completion. See `SYNC_AUTOMATION.md`, retained as the migration guide, for session-start retrieval and publication details. This arrangement does not provide automatic shared transcripts or refresh a running task's existing context.

## Relationship to existing Ixion work

The repository's June 2026 deployment-economics reorientation specifies deterministic, typed, additive, CPU-only work with reproducible receipts and explicit unavailable states. It places humanoid hardware unlikely before 2028. This is the relevant planning constraint; the older README contains earlier training and hardware dates.

A limited read of current files found:

- `src/deployment/task_economics.py`: normalized task and resource-pressure inputs for evidence-source routing. These scores are distinct from currency-denominated commercial cash flows.
- `src/economics/pricing.py`: pricing functions that impose a human-wage benchmark cap. The new research should treat that cap as an explicit contract assumption and examine when its denominator and outside option are appropriate.
- `src/economics/data_value.py`: an estimator relating novelty features to productivity changes. Its existence does not establish empirical learning value or transfer between real deployments. The current near-term program does not call for training it.

These are reuse candidates and conceptual antecedents. A full implementation audit has not been performed. Commercial modeling should make its units, evidence, and accounting boundaries explicit and preserve the existing frozen control and reward baseline.

## Unit of analysis: a deployment opportunity

The principal demand record is an **end market × value-chain stage × task bundle × site archetype × geography × time period**. A modeled deployment joins that opportunity to a **provider × robot configuration × software/autonomy version × integration arrangement × contract**. This permits the same customer opportunity to be evaluated under multiple competing solutions while preserving its identity and denominator.

An industry label alone is too coarse for the operating decisions. For example, logistics contains receiving, storage, replenishment, picking, packing, and shipping, each containing tasks with different workflow dependencies. A task bundle should include the supporting work required to produce the customer outcome, including loading, recovery, inspection, and handoffs where relevant.

Define output as accepted units of useful work at a stated service level. Distinguish attempted tasks, successful tasks, billed activity, robot-hours, and human-hours actually removed from a roster. Count complementary tasks separately while preventing their simultaneous inclusion as substitute deployments or duplicated labor savings.

## The connected analytical map

| Layer | Questions and records | Main output |
| --- | --- | --- |
| End markets and customer value chains | Who performs each process, who buys, what outcome matters, what is the present alternative? | Market and workflow map |
| Providers, products, and competitive position | Which companies and specific systems can serve each task, on what evidence, economics, commercial terms, and delivery capacity? | Versioned provider map and task-specific competitive comparisons |
| Deployment economics | What are the customer and provider cash flows at equal output and service quality? | Price feasibility, contribution, payback and NPV by scenario |
| Adoption and penetration | Which technically possible deployments become economical, operationally ready, funded, and actually installed? | Dated penetration waterfall and installed-base scenarios |
| Learning and task transfer | Which capabilities could improve, where could they transfer, and who captures the resulting gains? | Directed transfer hypotheses and incremental cash-flow effects |
| Robot supply chain | Which components, manufacturing capacity, integration crews, service resources, and financing constrain expansion? | Supply relationships, bottleneck scenarios and value-capture map |
| Interpretation | What changed, which conclusions follow, which are uncertain, and what decision should change? | Short research and decision memos |

Maintain three equally developed maps: **end markets**, **customer deployment value chains**, and **providers and their ecosystems**. The provider map includes the supply chain that manufactures, integrates, finances, and supports each system. Link all three through the particular task and deployment opportunity. Each map must support both factual description and changes to model inputs and conclusions.

## Provider market map and economic connections

Provider research is a continuing workstream with the same analytical depth as end-market research. A company profile should explain how capabilities, customer access, execution capacity, and capital translate into economic outcomes. Preserve source-backed facts, analytical interpretations, and forward scenarios as separate fields.

| Provider dimension | Research content | Economic connection |
| --- | --- | --- |
| Company and position in the ecosystem | Hardware maker; autonomy developer; integrator; operator; asset owner; partners; make-versus-buy boundaries; customer and data relationships | Which party collects revenue, bears costs and risk, owns assets, and retains learning benefits |
| Product and software lineage | Robot generations; hardware revisions; end effectors; mobility; sensors; compute; autonomy stack and release; upgrade compatibility | Capability coverage, delivered system cost, retrofit spending, obsolescence, and residual value |
| Capability by task and environment | Physical fit; accepted output; quality; recovery; assistance; availability; integration requirements; evidence conditions | Technical eligibility, useful capacity, staffing, support costs, and service commitments |
| Deployment footprint and market entry | End market; workflow; customer; site operator; site; geography; task; pilot/production status; contract; expansions and exits | Demonstrated market access, sales cycles, rollout assumptions, retention, and addressable customer cohorts |
| Business model and operating economics | Hardware sales, leases, RaaS, usage fees, software, integration, and service; pricing and discounts; component costs; maintenance and support | Customer price interval, provider contribution, recurring cash generation, and deployment cohort returns |
| Supply, delivery, and capital | Component dependencies; manufacturing partners; yields; actual and planned output; lead times; integration crews; service coverage; financing | Deployable units per period, working capital, rollout bottlenecks, financing need, and supply-side value capture |
| Learning and expansion | Data access and reuse rights; task diversity; training and validation; software partners; cross-task and cross-generation transfer | Cost or performance improvements, entry into adjacent tasks, learning expenditure, and who captures incremental cash flows |
| Competitive interpretation | Alternatives at the same service level; switching costs; channel access; differentiation; evidence gaps; plausible competitor responses | Win-rate scenarios, realized pricing, market share, margins, and the durability of an advantage |

An organization can have several roles. Represent each relationship separately: a manufacturing partner may also host a pilot; a customer can be an investor; a software company may serve competing hardware providers. A partnership alone does not establish exclusivity, productive deployment, unlimited data rights, or available manufacturing capacity.

Classify the **served end market**, **facility workflow**, **site operator**, **buyer**, and **economic beneficiary** separately. For example, a 3PL operating an apparel fulfillment facility belongs to an operator category and serves an apparel end market. Those labels describe one deployment and must not create two market opportunities.

### Versioned capability baselines

The capability reference is **a configured system performing a defined task in a defined environment at a dated evidence snapshot**. A company name or a headline payload cannot specify that reference.

Record three separate time dimensions:

1. Hardware model, revision, and introduction date, when disclosed.
2. Software/autonomy release, supplier, and deployment or evaluation date.
3. The observation period and source publication/retrieval dates.

A commercial deployment cohort is not necessarily a hardware generation. When a revision or software release is undisclosed, retain an explicit unknown. Proposed future configurations are scenarios. Freeze prior snapshots so improvements can be compared without rewriting historical capability or installed fleets.

For every modeled task, specify the physical envelope and workload: object distribution, payload at the relevant posture, reach, grasp, travel path, surfaces, workstation geometry, handoffs, and quality standard. Then distinguish nominal specifications from accepted throughput, intervention frequency and duration, charging and maintenance downtime, recovery behavior, and deployment effort. State whether performance is autonomous, teleoperated, assisted, or under undisclosed control. Missing performance metrics remain uncalibrated.

### Initial provider and robot reference set

These are research anchors selected for this program. The sources below were reviewed on 5 September 2026. This is a bounded starting set, not a complete survey or a claim that every deployment announcement remains current.

| Provider | Initial reference and role | Deployment and capability evidence | Modeling treatment |
| --- | --- | --- | --- |
| Unitree | **G1 EDU**, with exact configuration still to be selected, as the initial platform reference for personal research | Unitree distinguishes G1 and G1 EDU, including development access and optional hands, joints, and compute. It warns that some showcased functions remain under development. [G1 product specifications](https://www.unitree.com/g1/) | Keep hardware specifications and proposed task performance separate. Pin configuration and autonomy before assigning operational capability. A base G1 advertised price is not a G1 EDU quotation or a complete deployed system cost. |
| Agility Robotics | **Digit at GXO's SPANX operation**, using the 2024 commercial cohort as a task reference; add subsequent hardware/software evidence separately | GXO's June 2024 announcement describes a multiyear RaaS arrangement and totes moved from mobile robots to conveyors through Agility Arc. [Customer announcement](https://investors.gxo.com/news-releases/news-release-details/gxo-signs-industry-first-multi-year-agreement-agility-robotics/) | Starting commercial reference for this specific warehouse handoff. Public deployment evidence does not supply all inputs for throughput, support staffing, price, or ROI. Exact hardware revision and software release remain unpinned. |
| Boston Dynamics | **2026 production version of electric Atlas** as the industrial comparison; keep the earlier electric prototype in a separate historical record | The January 2026 launch describes planned shipments to Hyundai's RMAC and Google DeepMind. The product page separately describes Hyundai sequencing field tests. [Production-version announcement](https://bostondynamics.com/blog/boston-dynamics-unveils-new-atlas-robot-to-revolutionize-industry/); [Atlas product and deployment history](https://bostondynamics.com/products/atlas/) | Automotive sequencing/material handling is an initial research focus. Preserve pilot evidence and announced production-version shipments as distinct events; do not automatically attribute earlier test results to the new configuration. |
| Apptronik | **Apollo used in reported 2025 pilots**, plus separate **Apollo 2 bipedal** and **Apollo 2 wheeled** references for later detailed coverage | Mercedes-Benz describes intralogistics testing and teleoperated data collection. Apptronik describes a Jabil manufacturing/pilot relationship. Its current Apollo 2 page identifies both mobility configurations. [Mercedes-Benz testing](https://group.mercedes-benz.com/company/production/production-network/mbdfc-humanoid-robots.html); [Jabil collaboration](https://apptronik.com/news-collection/apptronik-and-jabil-collaborate-to-scale-production); [Apollo 2](https://apptronik.com/apollo/apollo-2) | Track automotive and manufacturing tasks, production learning, and manufacturing scale-up. Do not carry Apollo pilot results into Apollo 2 by default. Apollo 2 introduction date and task-specific performance require further evidence. |

Unitree remains the initial personal platform reference; the commercial reference is selected separately for each task. The research fits the current docs-first, CPU-only plan. Further Unitree models and other vendors enter as separately identified records when they answer a concrete task or market question.

Agility subsequently reported more than 100,000 totes moved at GXO's Flowery Branch facility. This provides a vendor-reported cumulative activity observation. It does not, on its own, identify robot-hours, fleet size, intervention burden, sustained units per hour, or returns. [Agility's activity update](https://www.agilityrobotics.com/content/digit-moves-over-100k-totes)

Two initial ecosystem relationships deserve separate records. Boston Dynamics' launch announcement identifies Hyundai Mobis as an actuator supplier and a Google DeepMind collaboration. Apptronik's Jabil announcement combines manufacturing and validation-site roles. These relationships motivate supply and learning hypotheses; capacity, exclusivity, and realized economic effects remain to be established. [Atlas launch](https://bostondynamics.com/blog/boston-dynamics-unveils-new-atlas-robot-to-revolutionize-industry/); [Apptronik–Jabil announcement](https://apptronik.com/news-collection/apptronik-and-jabil-collaborate-to-scale-production)

### How the maps enter the models

For each opportunity, create a set of candidate solutions: specified humanoid systems, relevant alternative automation, and the existing process. Compare them at matched accepted output and service requirements. One provider may cover more tasks while another has better economics on a narrower task. Keep capability, economic viability, and delivery capacity as distinct comparisons.

Each provider/system opportunity pairing gets its own technical gate, customer savings, provider costs, price terms, implementation time, and capital requirements. Task capability establishes eligibility; it does not establish that the provider wins the customer. Model selection using explicit assumptions about performance, total cost, procurement access, availability, and switching friction. Leave a share with alternatives and non-adoption where appropriate.

Aggregate demand across providers using the union of eligible opportunities and a consistent allocation of task volume. Overlapping provider addressable markets cannot be summed into total industry demand. A customer may use several systems on complementary tasks; preserve the task boundaries when allocating useful work, spending, and labor savings.

Track deployments by provider, system version, task, site cohort, contract, and installation period. Existing cohorts improve only when a compatible upgrade is actually applied in the scenario, including downtime, validation, and retrofit costs. A new product announcement does not upgrade the installed base. Allocate limited hardware, integration, service, and financing capacity across the provider's competing opportunities.

Learning is similarly specific. Ask whether deployment A supplies useful, accessible data for task B on the same system, another generation, or a partner's stack; what training and validation it requires; and whether the provider keeps, licenses, or shares the gain. A larger fleet is an input to this investigation, not a calibrated measure of data value.

The dynamic model should be able to answer: **If one provider reduces assistance on one task, how do its costs and prices change, which customer cohorts become viable, how much demand can it win and deliver, what cash can fund expansion, and which adjacent capabilities might improve?** The response can include a competitor lowering price, a manufacturing bottleneck, or no transferable learning. Each consequence requires an explicit dependency or scenario assumption.

### Updating and interpreting provider evidence

Store deployment phase and evidence provenance separately. Useful phases include demonstration, pilot, production operation, expansion, and retirement. Record an order or commercial agreement as a contract event, with shipments and operations as separate events. A customer statement can substantiate a pilot; a vendor specification can describe design intent; neither observation automatically establishes the other.

At each update, retain the old view, add the dated evidence, identify the applicable product/task/site population, and propose any changed assumptions. Rerun only affected cases, then record changes to feasibility, price boundaries, adoption, provider share, capital needs, and learning hypotheses. Preserve contradictory observations for review. New announcements trigger review rather than automatically becoming forecast inputs.

The eventual interactive view should allow movement from **end market → workflow → task → competing provider/system versions**, and back from **provider → deployments → customer markets → suppliers and learning opportunities**. An as-of-date selector and scenario comparison should show both the changing evidence and its modeled consequences.

## Penetration waterfall

Start each waterfall with a consistent denominator: eligible sites, task volume, or task-hours in a defined geography and period. Do not mix them or convert total industry revenue directly into robot revenue.

| Stage | Gate to quantify |
| --- | --- |
| Total relevant activity | Distinct sites and task volume; current installed automation and remaining baseline |
| Task-addressable activity | Task bundles and environments covered by the specified solution |
| Technically feasible activity | Throughput, quality, reliability, physical fit and required human assistance |
| Economically attractive activity | Customer benefits and provider returns at explicit prices and terms |
| Operationally and institutionally ready demand | Integration fit, process redesign, procurement, buyer budget, training and acceptance |
| Deliverable deployments | Hardware supply, deployment slots, service headroom and financing available in the period |
| Installed and retained deployments | Actual starts, ramp-up, utilization, failures, exits, replacements and expansions |

Estimate gates for matched cohorts. Sequential percentages are conditional on the previous stage; they are not independent probabilities. Preserve the relationship between difficult environments, low reliability, integration cost, and adoption instead of applying unrelated aggregate haircuts.

Keep an installed-base stock and a flow of new deployments. Incremental installations are bounded by ready unserved demand, hardware availability converted into deployment capacity, integration capacity, support headroom, and deployable capital. Track retirements and replacements separately so cumulative shipments are not mistaken for an active fleet.

## Cash generation and learning value

Present-day productivity and future learning act through different channels.

**Customer adoption:** the customer responds to the price, performance, risk, and workflow consequences it experiences. A provider's expected future data value does not directly increase the customer's savings. It may influence adoption if it funds a lower price, more support, or later performance improvement.

**Provider cash generation:** include hardware and integration outlays, ramp losses, support costs, collection timing, and working capital. Operating cash generated by existing deployments can fund later expansion under an explicit reinvestment policy. Accounting profit alone does not establish financing capacity.

**Capability learning:** model possible changes in success rate, cycle time, intervention demand, or deployment effort. Map those changes to additional cash flows. Transfer is directed and conditional on the task, embodiment, environment, data rights, and training process.

**Information value:** a deployment may also reveal which market or design to pursue. That value comes from improving a later decision. Keep it conceptually distinct from improved robot capability.

Use three scenario families: no transfer, limited transfer within related tasks, and broader transfer. Treat these as assumptions until suitable evidence supports calibration. Include the possibility that improvements are small, do not transfer, arrive late, or fail to remain exclusive.

The clean overall comparison is the discounted value of a deployment policy with the proposed learning opportunity versus an otherwise comparable policy without it, including all incremental costs. If learning already changes future cash flows in that comparison, do not add a separate data-value premium to the same result. Do not count the same learning benefit separately for every contributing deployment.

## First cash-flow model

Specify one site, one task bundle, an operating horizon, and comparable output and service quality under manual and robot-assisted operation.

For each period:

- `B_t`: customer's full baseline operating cost for the specified output.
- `A_t`: customer's retained operating cost after deployment, excluding the robot-provider payment.
- `P_t`: payment to the robot provider.
- `O_t`: provider operating cash costs, including human support and service resources within the chosen boundary.

Customer operating savings are `B_t - A_t - P_t`. Provider operating cash contribution is `P_t - O_t`. Place one-time integration and hardware investments at their actual dates, then calculate each party's NPV with separately stated required returns, taxes or other included cash-flow items, and residual-value assumptions. Avoid subtracting depreciation as a cash outflow after already counting capex.

The first question is whether a price interval exists that satisfies both parties' requirements. Use actually avoidable customer costs; redeployed time and removed payroll are distinct outcomes. Demand and utilization should be consistent with the modeled process bottleneck. Added capacity creates value only under an explicit demand and monetization assumption.

The first model should show sensitivities to technical availability, useful throughput, intervention demand, integration cost, useful life, price, and actually avoided human staffing. All numerical inputs begin as unfilled or explicitly illustrative until sourced.

## Minimum research records

Start with inspectable tables. Add a database only when relationships and update volume justify it.

| Record | Required content |
| --- | --- |
| Opportunity | Stable ID; end market; value-chain stage; task bundle; site archetype; geography; denominator; base period |
| Organization and roles | Stable organization ID; provider, customer, operator, integrator, supplier, software developer, financier, and asset-owner roles; dated relationships |
| System version | Stable system ID; provider ID; model; hardware revision; configuration; end effector; autonomy/software provider and version; dates; predecessor; upgrade compatibility; unknown fields |
| Capability observation | System ID; task ID; environment and workload; control mode; metric; value and unit; measurement window; assistance and setup conditions; linked evidence |
| Deployment and contract event | System and opportunity IDs; customer, buyer, operator, and site; served end market; event date; phase; contract type; counts with units; source; effective period |
| Provider economics and capacity | Provider/system IDs; period; prices and terms; cost assumptions; asset ownership; actual versus planned output; deployment/service capacity; capital; linked evidence |
| Provider opportunity comparison | Opportunity ID; competing system IDs and alternatives; capability gaps; customer and provider economics; allocation assumptions; dependencies; scenario and evidence versions |
| Evidence | Stable ID; metric or claim; value and unit; source and locator; observation date; retrieval date; applicable population; evidence class; uncertainty; superseded record |
| Scenario | Opportunity and system-version IDs; model version; linked evidence IDs; input assumptions; contract; integration arrangement; horizon; capital policy; competitor response |
| Transfer relationship | Source and destination task/system IDs; data access and reuse rights; hypothesized shared capability; training and validation costs; expected operational effect; beneficiary; uncertainty; evidence and validation status |
| Supply relationship | Supplier or resource category; customer/component relationship; substitute options; quantity per deployment; capacity or lead-time assumption; source and date |
| Interpretation and change | Previous view; new evidence; changed assumptions; affected scenarios; resulting ranking or timing changes; unresolved questions |

Use evidence classes such as observed result, vendor-reported claim, sourced estimate, engineering assumption, and synthetic example. Attach evidence to particular claims and parameters. A reported pilot, order, shipment, and production deployment represent different observations.

Preserve time and version identity. A result should identify its model version, scenario inputs, evidence snapshot, units, horizon, and relevant costs. Unknown values remain unknown; an assumption-filled scenario is an exploration of consequences rather than validation.

## How each work session proceeds

1. Choose a decision or claim that would matter to an operator, finance lead, or strategist.
2. Write the mechanism in ordinary language and identify competing explanations.
3. Define the entities, units, boundary, causal dependencies, and time horizon.
4. Find the smallest set of primary evidence needed to constrain the important assumptions.
5. Build or revise a transparent model and run counterfactuals and sensitivities.
6. Interpret the result: what changes the decision, what survives, and what observation would reverse it?
7. Update accepted records and the handoff, validate and publish authorized Codex changes through a scoped commit and normal push, and leave one clear next question and next owner. Work returns its findings with the repository commit it read.

Use focused tasks across both projects for distinct outcomes: end-market and workflow mapping, provider research, model development, learning and transfer, supply-chain analysis, and synthesis. Link related Codex and ChatGPT Work tasks through the handoff record. Each Work task begins by reading the current remote `main` commit and its charter, scenario version, and open-question record. Each task ends by recording decisions, relevant reasoning, changed artifacts or proposals, and the receiving side's review or pending action. Research findings should inform executable models, and model results should return to research for interpretation and challenge.

New evidence should trigger a dependency review. For example, a supported reduction in intervention minutes changes the support-cost assumption, which may change the viable price interval, then eligible customer cohorts, then the adoption scenario, and finally component demand and financing needs. If the evidence only covers one task or environment, propagate it only there.

The learning method is active: Amar predicts important directions and tradeoffs before inspecting a scenario, explains why the results follow, and defends the conclusions in a short memo. Mathematical concepts enter as the decisions require them: cost accounting and cash flows first; constrained optimization, queueing, learning curves, causal inference, and value of information as the corresponding mechanisms enter the model.

## First complete case

Proposed starting scope: a warehouse material-flow value chain, with a narrow carton or tote-handling task selected for the first deployment model. This is a modeling choice, not a claim that it is the most attractive market.

Produce a connected case containing:

1. A value-chain map and five to ten candidate task bundles, with consistent opportunity IDs.
2. A provider-by-task comparison for Unitree G1 EDU, the Digit commercial reference, and electric Atlas; Apollo/Apollo 2 initially enter as separate coverage candidates. Include the current process and relevant alternative automation. Mark missing evidence explicitly; do not invent comparable performance scores.
3. One operating and cash-flow model comparing the current process and specified robot-assisted scenarios, beginning with the best-supported task reference and labeled sensitivity cases.
4. An adoption waterfall for the defined site cohort with sourced inputs, labeled gaps, and explicit provider allocation assumptions.
5. A small transfer map containing two or three explicit hypotheses to adjacent tasks and system versions, including a no-transfer case.
6. A supply and integration constraint scenario showing what could limit provider rollout.
7. A two-page interpretation: deployment conditions, price boundaries, provider positioning, capital needs, highest-value missing evidence, and conditions that would change the recommendation.

Broaden to a second end market after this case can be rerun and explained. Compare which primitives generalize and which assumptions need to change. Build a private interactive view once the underlying definitions and first calculations are stable enough to make its controls meaningful.

An appropriate sustainable default is one substantive session each week, with optional short reading or question-capture sessions. Progress is measured in completed, reproducible cases and improved judgment. Several strong cases over time can become a portfolio demonstrating market interpretation, commercial modeling, and deployment decision-making.

## Completion standard for a research case

- The question, boundary, units, baseline, and decision are explicit.
- Important inputs can be traced to evidence or a labeled assumption.
- The model can be rerun from a saved version.
- The customer and provider perspectives are reconciled.
- Competing systems are identified by configuration and evidence snapshot; supplier, provider, operator, and end-market roles are distinguishable.
- Provider market shares and end-market totals reconcile without duplicated demand or labor savings.
- Adoption constraints, supply constraints, and cash timing are represented where material.
- At least one adverse or competing scenario has been examined.
- Transfer value is conditional and avoids double counting.
- The memo states what is known, what is inferred, and what would change the decision.
- Amar can explain the major dependencies and limitations without relying on the model's prose.

## Source notes for workspace and project continuity

The economic framework above is a proposed research design developed for this discussion. The initial provider reference set links selected public product and deployment claims to their sources; it does not provide calibrated market sizes, adoption rates, comparable operating performance, or company financial forecasts.

- [OpenAI: Projects and chats](https://learn.chatgpt.com/docs/projects) — shared project sources and instructions, local folder access, durable Codex file guidance, and separate chats for distinct outcomes. Reviewed 5 September 2026. The paired-project exchange protocol above is this program's operating convention; it is not a claim of native automatic synchronization.
- [Ixion: deployment-economics reorientation](https://github.com/robotics-vp/robotics-vp-core/blob/c06143ac3e073a3838578aaf2c64eeabab867c30/docs/economic_world_model/deployment_economics_reorientation_2026_2027.md) — current near-term constraints at the repository snapshot inspected.
- [Ixion: task-economics inputs](https://github.com/robotics-vp/robotics-vp-core/blob/c06143ac3e073a3838578aaf2c64eeabab867c30/src/deployment/task_economics.py) — normalized evidence-routing contracts.
- [Ixion: pricing functions](https://github.com/robotics-vp/robotics-vp-core/blob/c06143ac3e073a3838578aaf2c64eeabab867c30/src/economics/pricing.py) — existing accounting and pricing assumptions.
- [Ixion: data-value estimator](https://github.com/robotics-vp/robotics-vp-core/blob/c06143ac3e073a3838578aaf2c64eeabab867c30/src/economics/data_value.py) — existing estimator code inspected, without running or validating it.

## Change record

- **0.5 — 6 September 2026:** Adopted the private amarmurray/robotics-economics repository and main branch as the shared accepted source. Replaced hourly uploads with repository review at each Work session's start, commit-pinned reads, and scoped commit/push publication after substantive authorized Codex tasks. Paused the earlier hourly automation; preserved explicit proposal review, access verification, and the separate Ixion implementation boundary.

- **0.4 — 5 September 2026:** Installed an hourly synchronization automation for changed canonical sources and incoming ChatGPT Work findings. Added an operating guide, content-based change detection, conflict preservation, and quiet unchanged runs. Future scheduled execution remains subject to available local files, browser access, and app runtime.

- **0.3.1 — 5 September 2026:** Confirmed both projects exist, recorded their displayed names, and adopted the user-created Robotics Economics folder as the canonical local workspace. Research content and the versioned handoff protocol are unchanged.

- **0.3 — 5 September 2026:** Defined the paired Codex and ChatGPT Work arrangement for robotics economics. Added shared artifact ownership, versioned source snapshots, reciprocal review, explicit handoffs and receipt checks, conflict handling, and truthful synchronization status. Preserved the separately scoped review before adopting work into the existing repository.
- **0.2 — 5 September 2026:** Promoted provider mapping to an equal analytical workstream alongside end markets and customer deployment value chains. Added initial sourced robot references, version and evidence rules, provider economics and competition, ecosystem relationships, dynamic update logic, and links to the first economic case.
- **0.1 — 5 September 2026:** Established the research purpose, workspace, accounting boundaries, penetration waterfall, learning framework, and first-case plan.
