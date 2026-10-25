# Robotics Economics: Research Charter

Version 0.9 · 25 October 2026 · Amar Murray

This charter governs the paired Codex and ChatGPT research program in physical labor, humanoid deployment, learning/control, physical-digital coordination, and the organization of production. Version 0.9 retains and extends Amar's 25 October 2026 correction: begin with end markets and value chains, develop qualitative views and staged penetration models, and investigate how capability improvements, data aggregation, bottlenecks, and ownership change deployment pathways. It supersedes the warehouse-first case, mandatory Excel-first sequence, and delayed dashboard. The detailed design is `RESEARCH_PROGRAM_DESIGN.md`; first-week deliverables and acceptance are in `WEEK_ONE_RESEARCH_SPEC.md`; launch text is `CODEX_GOAL.md`; open questions are in `RESEARCH_ROADMAP.md`.

This is the accepted program design and a prepared research campaign, not a completed market study or an activated seven-day run. Models, datasets, report, and dashboard remain campaign outputs to be produced. Existing historical source notes are retained as dated research seeds. They must be refreshed before they support current claims.

## Purpose and decisions

Develop the understanding, evidence base, and working models needed to shape strategy and staged deployment at a humanoid robotics company.

The central question is: **Where, how, and in what sequence can humanoids and digital agents transform physical production and services; what must improve for each stage to become viable; and which deployment and ownership arrangements create and capture value?**

The program connects eight research decisions:

1. Map physical labor, productive processes, and operating heterogeneity across end markets and value-chain stages.
2. Relate current provider/system capabilities and research progress to conditional improvement and scaling pathways.
3. Develop staged penetration waterfalls and deployment portfolios under shared supply, integration, service, supervision, and financing constraints.
4. Examine data aggregation, transfer, learning, evidence acquisition, and control, including how deployments affect subsequent capability.
5. Study productive coordination among physical robots, digital agents, people, and infrastructure.
6. Investigate customer ownership, governance, capital allocation, automation appetite, operating authority, and implementation capacity as determinants of adoption and value-chain position; compare incumbent, acquisition/holdco, and AI-native development pathways.
7. Preserve the distinct inquiry into robotics business models, provider/operator/integrator/financier roles, asset ownership, commercial/control/data rights, integration, and value capture, including coexistence.
8. Study the full digital-AI ecosystem as substantial comparative evidence and a direct contributor to embodied capability, fleet/site/enterprise coordination, and humanoid R&D. Cover physical inputs/model development, scaling and deployment/overhang, economic effects, benchmarks, multi-agent systems, lab/input/capital/customer competition, deploycos and complementary businesses; test analogies and joint capability paths explicitly.

Customer-side AI-native entry is an explicit research thesis: can capital fund a new operating business or platform that competes through differentiated humanoid/digital-agent deployment, earlier adoption of broadly available technology, or conditional labor-capacity advantages? Examine financing through ramp, demand capture, incumbent response, and build/acquire/hybrid choices by end market and value-chain stage. Use Thrive Holdings as an organizational comparator, with the physical/industrial extension and greenfield cases treated as hypotheses. Keep customer formation separate from robotics-provider business models while linking their economics.

The detailed digital-AI workstream is `LLM_ECOSYSTEM_RESEARCH_MODULE.md`. It receives substantial first-week research attention and reporting, with explicit evidence on both sides of each analogy, direct-contribution/interface maps, and digital-improved human-led baselines. Enterprise/site coordination includes ERP, inventory, production systems, routing/scheduling, maintenance, and exception workflows; robotics R&D is a separate contribution channel. Shared improvements and resource budgets are counted once.

Tasks and task bundles enter as explanatory detail. The organizing research and presentation level is end markets and value-chain stages. The first milestone is a broad, evidence-grounded research edition with a written report and functioning interactive dashboard; the program continues through a prioritized multi-month roadmap.

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
| Excel, when useful | Optional transparent review/export surface reconciled to the authoritative calculation engine |
| Interactive dashboard in the first research campaign | Explore end markets, value chains, capabilities, staged penetration, physical-digital coordination, data/transfer, and ownership scenarios from the same evidence and model |

Use one transparent, versioned calculation engine for report figures, dashboard views, and exports. Select a lightweight CPU implementation appropriate to the question. A workbook is optional and must reconcile to the same engine if produced. Multiple agents work from explicit versions and handoffs, with one writer per file at a time.

Use public sources and clearly labeled scenarios for this personal program. Evidence-led research, CPU models, and a local interactive dashboard are in scope. New hardware or GPU training is not required to investigate broader deployment and learning questions.

### Repository exchange and dialogue

Maintain `HANDOFF.md` as the current coordination record and `artifact_manifest.json` as the index of repository-relative paths, local working paths, artifact versions, and content hashes. Commit these records with accepted changes. Keep publication receipts, check timestamps, logs, and incoming-proposal bookkeeping outside the shared research state. Repository commits identify shared versions; no file should try to contain the SHA of its own containing commit.

1. **Start from a known commit.** At the start of each Work session, resolve remote `main` HEAD and read the charter, handoff, manifest, and required files at that exact SHA. Report the SHA used. Re-fetch deliberately if the task needs later changes; do not mix revisions silently. If the repository or a required file is inaccessible, state the failure and missing input rather than treating an old upload or remembered text as current.
2. **Exchange a concrete question and evidence.** Either side prepares a bounded question, findings, source links and dates, assumptions, relevant artifacts, and a requested review or next action. Work returns proposals in its task output, with the input commit SHA. Writing a proposal to `proposals/` requires authorization to write to the repository; a task output does not itself authorize a commit, issue, comment, or other external post. Keep decision-relevant reasoning in the returned artifact or output rather than assuming access to another transcript.
3. **Review and reconcile.** The receiving side checks evidence, units, model behavior, and implications, then returns agreement, a correction, a competing explanation, or a testable next step. Preserve unresolved disagreements. A new proposal remains a proposal until incorporated and verified in the canonical files; it does not silently overwrite an earlier decision.
4. **Publish the accepted state.** Finish each substantive authorized Codex task with appropriate validation, updated accepted artifacts, handoff and manifest, a scoped commit, and a normal push to `main`. Include only the task's accepted changes; unrelated or unaccepted working edits remain untouched. Check remote state before pushing. Preserve divergence or conflicts for explicit reconciliation; do not force-push or auto-merge them. Work-generated changes return for reconciliation before becoming accepted state.
5. **Record publication and consumption separately.** The local operational receipt records actual push verification and any observed Work read, with commit SHA and time. A successful push proves repository publication, not that a Work session has consumed it. Each Work session records the SHA it actually read. Preserve pending publication, unavailable access, and conflicts explicitly. One writer owns each file during an exchange.

The earlier hourly Sync robotics economics automation is PAUSED. There is no periodic polling or source-upload refresh in this workflow. Work reviews the repository when a session begins, and accepted changes are shared through normal commits and pushes at task completion. See `SYNC_AUTOMATION.md`, retained as the migration guide, for session-start retrieval and publication details. This arrangement does not provide automatic shared transcripts or refresh a running task's existing context.

## Relationship to existing Ixion work

The separately scoped Ixion repository's June 2026 deployment-economics reorientation describes a deterministic, typed, additive, CPU-only implementation posture with reproducible receipts and explicit unavailable states. Its hardware calendar is a dated project-planning assumption, not a robotics-market forecast or a restriction on this research program's intellectual scope. This research may analyze hardware, training economics, and fleet architectures without authorizing their execution or purchases.

A limited read at the cited June 2026 implementation snapshot found:

- `src/deployment/task_economics.py`: normalized task and resource-pressure inputs for evidence-source routing. These scores are distinct from currency-denominated commercial cash flows.
- `src/economics/pricing.py`: pricing functions that impose a human-wage benchmark cap. The new research should treat that cap as an explicit contract assumption and examine when its denominator and outside option are appropriate.
- `src/economics/data_value.py`: an estimator relating novelty features to productivity changes. Its existence does not establish empirical learning value or transfer between real deployments. The current near-term program does not call for training it.

These are reuse candidates and conceptual antecedents. A full implementation audit has not been performed. Research models should make their units, evidence, and accounting boundaries explicit and may compare alternative control and coordination arrangements. Any later separately authorized integration into Ixion must review and preserve its applicable frozen control/reward boundaries unless that task explicitly authorizes a change.

## Unit of analysis: end markets and value chains

The principal analytical cell is **end market × value-chain stage × operating archetype × geography × time**. Begin with the distribution and organization of physical labor and its supporting digital processes. Investigate which configurations of humanoids, other machines, software agents, people, and infrastructure can change those processes over successive deployment stages.

Use the hierarchy economy → end market → value chain → productive process/operating archetype → work and capability requirements → candidate systems and organizational arrangements. Tasks and task bundles supply supporting mechanisms; a single task is not the program's entry gate.

Detailed deployment records may additionally identify task bundles, site cohorts, providers, robot configurations, software/autonomy versions, integration arrangements, and contracts. Preserve a stable identity for the underlying activity when several systems or organizational routes compete to serve it.

Keep labor headcounts, annual hours, physical-work shares, compensation, accepted output, robot-hours, and removed payroll distinct. Show evidence and assumptions for conversions. Task descriptions or importance/frequency ratings do not establish time shares. Keep measured employment coverage separate from scenario estimates of physical-work hours.

Allocate outsourced and shared work consistently. A facility's operating industry and its customer's served end market are different views of the same activity, not independent labor pools. Preserve workflow dependencies, complementary tasks, and the demand constraints that determine whether improved capability increases useful output.

## The connected analytical map

| Layer | Questions and records | Main output |
| --- | --- | --- |
| Physical labor, end markets, and value chains | Where is physical work organized, who performs it, which outputs and digital processes matter, and where do operating archetypes differ? | Economic atlas, labor crosswalks, and process maps |
| Providers, products, and competitive position | Which companies and specific systems can serve each task, on what evidence, economics, commercial terms, and delivery capacity? | Versioned provider map and task-specific competitive comparisons |
| Deployment economics | What are the customer and provider cash flows at equal output and service quality? | Price feasibility, contribution, payback and NPV by scenario |
| Adoption and penetration | Which technically possible deployments become economical, operationally ready, funded, and actually installed? | Dated penetration waterfall and installed-base scenarios |
| Learning and task transfer | Which capabilities could improve, where could they transfer, and who captures the resulting gains? | Directed transfer hypotheses and incremental cash-flow effects |
| Robot supply chain | Which components, manufacturing capacity, integration crews, service resources, and financing constrain expansion? | Supply relationships, bottleneck scenarios and value-capture map |
| Physical-digital fleets and control | How do robots, software agents, people, and infrastructure allocate work and shared resources? | Coordination archetypes and mechanism models |
| Customer ownership, organization, and adoption | How do the adopting business's governance, capital allocation, appetite, authority, capacity, and value-chain position change deployment? | Customer profiles, adoption mechanisms, pathway and coexistence comparisons |
| Robotics business models, asset ownership, and value capture | How should robots be supplied, operated, financed and controlled; which participants capture gains? | Commercial and actor/rights maps; customer/provider/operator/financier economics; integration strategies |
| Digital AI ecosystem and direct contributions | What transfers conditionally from model development, supply, deployment, economics, evaluation and competition; how do digital systems directly change robotics and the organization? | Ecosystem dossiers, analogy tests, benchmark cards, role/interface and R&D maps, joint digital/physical scenarios |
| Interpretation | What changed, which conclusions follow, which are uncertain, and what deployment decision should change? | Integrated report, interactive dashboard, and decision memos |

Maintain connected maps of **physical labor/end markets**, **productive value chains**, and **providers and their ecosystems**, with ownership, data, and coordination relationships. End markets and value-chain stages organize the synthesis; provider and task detail explain the mechanisms. Link them through common activity and cohort identities. Each map must support factual description and traceable changes to model inputs and conclusions.

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

### Historical seed provider and robot reference set

The following references were assembled for charter v0.5 and reviewed on 5 September 2026. They are retained as a historical seed set, not a required provider shortlist, current capability census, or committed personal hardware choice. Refresh each claim, expand provider coverage from the market map, and preserve superseded versions before using these sources in the first campaign.

| Provider | Initial reference and role | Deployment and capability evidence | Modeling treatment |
| --- | --- | --- | --- |
| Unitree | **G1 EDU**, with exact configuration still to be selected, as the initial platform reference for personal research | Unitree distinguishes G1 and G1 EDU, including development access and optional hands, joints, and compute. It warns that some showcased functions remain under development. [G1 product specifications](https://www.unitree.com/g1/) | Keep hardware specifications and proposed task performance separate. Pin configuration and autonomy before assigning operational capability. A base G1 advertised price is not a G1 EDU quotation or a complete deployed system cost. |
| Agility Robotics | **Digit at GXO's SPANX operation**, using the 2024 commercial cohort as a task reference; add subsequent hardware/software evidence separately | GXO's June 2024 announcement describes a multiyear RaaS arrangement and totes moved from mobile robots to conveyors through Agility Arc. [Customer announcement](https://investors.gxo.com/news-releases/news-release-details/gxo-signs-industry-first-multi-year-agreement-agility-robotics/) | Starting commercial reference for this specific warehouse handoff. Public deployment evidence does not supply all inputs for throughput, support staffing, price, or ROI. Exact hardware revision and software release remain unpinned. |
| Boston Dynamics | **2026 production version of electric Atlas** as the industrial comparison; keep the earlier electric prototype in a separate historical record | The January 2026 launch describes planned shipments to Hyundai's RMAC and Google DeepMind. The product page separately describes Hyundai sequencing field tests. [Production-version announcement](https://bostondynamics.com/blog/boston-dynamics-unveils-new-atlas-robot-to-revolutionize-industry/); [Atlas product and deployment history](https://bostondynamics.com/products/atlas/) | Automotive sequencing/material handling is an initial research focus. Preserve pilot evidence and announced production-version shipments as distinct events; do not automatically attribute earlier test results to the new configuration. |
| Apptronik | **Apollo used in reported 2025 pilots**, plus separate **Apollo 2 bipedal** and **Apollo 2 wheeled** references for later detailed coverage | Mercedes-Benz describes intralogistics testing and teleoperated data collection. Apptronik describes a Jabil manufacturing/pilot relationship. Its current Apollo 2 page identifies both mobility configurations. [Mercedes-Benz testing](https://group.mercedes-benz.com/company/production/production-network/mbdfc-humanoid-robots.html); [Jabil collaboration](https://apptronik.com/news-collection/apptronik-and-jabil-collaborate-to-scale-production); [Apollo 2](https://apptronik.com/apollo/apollo-2) | Track automotive and manufacturing tasks, production learning, and manufacturing scale-up. Do not carry Apollo pilot results into Apollo 2 by default. Apollo 2 introduction date and task-specific performance require further evidence. |

No personal platform is selected by the revised research design. Add provider/system records when they matter to end-market deployment pathways or capability research, including relevant non-humanoid alternatives. The historical references above do not limit coverage.

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

The first-campaign dashboard starts with **end markets → value-chain stages → operating configurations and deployment pathways**, with drill-down into tasks, provider/system versions, evidence, coordination, and ownership. Reverse views connect providers to deployments, markets, suppliers, and learning opportunities. As-of-date and scenario controls show the evidence and modeled consequences. The complete interaction and validation specification is in `WEEK_ONE_RESEARCH_SPEC.md`.

## Staged penetration and deployment capacity

Model penetration by end-market/value-chain cohort, operating configuration, system version, geography, and period. Develop qualitative stage views before supplying unsupported numbers. The first framework links relevant physical work → capability-compatible work → feasible production configurations → economically attractive configurations → ready demand → deliverable capacity → installed and retained productive capacity → realized useful output and labor effects.

Maintain one denominator within each waterfall panel. Link hours, sites, robots, output, and currency through explicit conversion tables rather than subtracting unlike units. Gates are conditional on preceding eligibility, and dependence among physical difficulty, reliability, integration, and economics must remain visible.

Pair the waterfall with deployment-stage scenarios ranging from bounded assisted operation to integrated fleets and coordinated physical-digital processes. These stages are not a universal mandatory ladder. Explain the capability, organizational, and resource conditions needed for each transition, including possible delays or regressions.

Keep active capacity as a stock with new deployment, ramp, retirement, replacement, and retention flows. Allocate shared hardware, integration teams, service headroom, supervision, and financing across markets. Track useful output separately from machines shipped or installed. Model demand expansion and new services separately from substitution of the baseline labor pool.

Capability-improvement relationships, learning transfer, coordination effectiveness, customer ownership/governance and readiness, customer development pathways, and commercial/asset/control arrangements are separate scenario inputs. Ownership primarily describes the adopting business in the customer workstream; robot ownership and supplier business models remain a distinct linked inquiry. Customer structures affect funding, investment appetite, process authority, implementation capacity, and value-chain position through specified mechanisms, not a universal label-based adoption multiplier. Use activity-weighted customer cohorts and conserve underlying activity when ownership or value-chain roles change. An improvement affects only the populations and compatible system versions justified by evidence or an explicitly labeled assumption. See `RESEARCH_PROGRAM_DESIGN.md` and `WEEK_ONE_RESEARCH_SPEC.md` for the detailed contracts.

## Cash generation and learning value

Present-day productivity and future learning act through different channels.

**Customer adoption:** the customer responds to the price, performance, risk, and workflow consequences it experiences. A provider's expected future data value does not directly increase the customer's savings. It may influence adoption if it funds a lower price, more support, or later performance improvement.

**Provider cash generation:** include hardware and integration outlays, ramp losses, support costs, collection timing, and working capital. Operating cash generated by existing deployments can fund later expansion under an explicit reinvestment policy. Accounting profit alone does not establish financing capacity.

**Capability learning:** model possible changes in success rate, cycle time, intervention demand, or deployment effort. Map those changes to additional cash flows. Transfer is directed and conditional on the task, embodiment, environment, data rights, and training process.

**Information value:** a deployment may also reveal which market or design to pursue. That value comes from improving a later decision. Keep it conceptually distinct from improved robot capability.

Use three scenario families: no transfer, limited transfer within related tasks, and broader transfer. Treat these as assumptions until suitable evidence supports calibration. Include the possibility that improvements are small, do not transfer, arrive late, or fail to remain exclusive.

The clean overall comparison is the discounted value of a deployment policy with the proposed learning opportunity versus an otherwise comparable policy without it, including all incremental costs. If learning already changes future cash flows in that comparison, do not add a separate data-value premium to the same result. Do not count the same learning benefit separately for every contributing deployment.

## Deployment-level economic module

Use this module when it explains an end-market deployment conclusion. It is not a prerequisite for economy-wide mapping, learning/control research, or the first dashboard. Specify the relevant cohort or site, process configuration, horizon, and comparable output/service quality under the baseline and robot-assisted operation.

For each period:

- `B_t`: customer's full baseline operating cost for the specified output.
- `A_t`: customer's retained operating cost after deployment, excluding the robot-provider payment.
- `P_t`: payment to the robot provider.
- `O_t`: provider operating cash costs, including human support and service resources within the chosen boundary.

Customer operating savings are `B_t - A_t - P_t`. Provider operating cash contribution is `P_t - O_t`. Place one-time integration and hardware investments at their actual dates, then calculate each party's NPV with separately stated required returns, taxes or other included cash-flow items, and residual-value assumptions. Avoid subtracting depreciation as a cash outflow after already counting capex.

For a specified commercial configuration, test whether a price interval exists that satisfies both parties' requirements. Use actually avoidable customer costs; redeployed time and removed payroll are distinct outcomes. Demand and utilization should be consistent with the modeled process bottleneck. Added capacity creates value only under an explicit demand and monetization assumption.

The economic module should show sensitivities to technical availability, useful throughput, intervention demand, integration cost, useful life, price, and actually avoided human staffing. All numerical inputs begin as unfilled or explicitly illustrative until sourced.

## Minimum research records

Start with inspectable tables. Add a database only when relationships and update volume justify it.

| Record | Required content |
| --- | --- |
| Market-stage cell | Stable ID; end market; value-chain stage; operating archetype; geography; time; denominator and coverage status |
| Labor/activity allocation | Source industry/occupation identity and vintage; employment, hours, physical-work-share assumptions, weights, units, uncertainty, and unallocated share |
| Opportunity | Stable ID linked to the market-stage cell; detailed process/task bundle where needed; system/organization configuration; site cohort; base period |
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
| Coordination configuration | Physical/digital agents; human support; process dependencies; decision authority; shared resources; control assumptions; measured versus proposed effects |
| Customer/adopter profile | Parent/operator/site/buyer/beneficiary actors; ownership/governance attributes; capital allocation; investment criteria and appetite evidence; authority; implementation capacity; value-chain role |
| Customer pathway | Incumbent expansion, acquisition/holdco transformation, new entry and repositioning; transition timing/costs; cohort identity and reclassification; coexistence links |
| Robotics commercial/asset/control arrangement | Provider/operator/integrator/financier roles; robot/model/data/workflow rights; sale/lease/service/partnership/integration terms; funding, risks, cash and value allocation |
| Research question | Stable ID; decision relevance; current state; evidence/method; dependencies; disconfirming evidence; next action and completion criterion |
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

The learning method is active: Amar predicts important directions and tradeoffs before inspecting a scenario, explains why the results follow, and defends the conclusions in a short memo. Mathematical concepts enter as the decisions require them: accounting, constrained optimization, queueing, learning response models, causal inference, and value of information. There is no fixed requirement that a cash-flow exercise precede learning, control, or coordination questions.

## First seven-day research campaign

Execute the program-level first edition defined in `WEEK_ONE_RESEARCH_SPEC.md` when Amar activates `CODEX_GOAL.md` in the Codex project. Record the actual start, a deadline 168 hours later, resource/runtime interruptions, and input repository revision. The goal has not been started merely because these documents exist.

The first edition contains:

1. A broad end-market and value-chain map of physical labor, with coverage and accounting boundaries explicit.
2. A current provider/system capability map and evidence-contingent progress/scaling scenarios.
3. Qualitative deployment theses and staged penetration models for a contrasting set of market-stage cohorts.
4. Substantive analyses of data aggregation, learning/control, physical-digital fleet coordination, and shared rollout constraints.
5. Market-stage comparisons of customer ownership/organization and adoption, including incumbent/acquisition/newco pathways, plus distinct robotics business-model, asset/control, and value-capture comparisons.
6. An integrated written report and functional interactive dashboard drawing on the same versioned evidence and model, with a substantial digital-AI ecosystem chapter and dedicated linked workspaces for ecosystem evidence, tested analogies and direct contributions.
7. Reproduction instructions, an acceptance audit, and a ranked roadmap of unresolved questions and follow-on research.

Continue substantive work through the research window, using checkpoints and priority questions to deepen the edition. Do not confuse seven named stages with a week of elapsed execution, invent research performed during a pause, or manufacture inputs to complete a visual. At the deadline publish the strongest verified edition and clearly identify incomplete requirements.

The warehouse/carton-handling case is no longer the required starting point. Specific cases are selected later according to how they explain important market-stage mechanisms. The broader program can continue for months as capabilities, evidence, and data access evolve; the first campaign does not exhaust it.

## Completion standards

The program-level first-week acceptance criteria are authoritative in `WEEK_ONE_RESEARCH_SPEC.md`. They require substantive breadth, traceable evidence, coherent scenarios, functioning dashboard controls, matched report outputs, and an explicit continuing roadmap. A missing parameter may limit a quantitative conclusion; it does not justify silently narrowing the program to a single task.

For later detailed deployment cases:

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

- **0.9 — 25 October 2026:** Added substantial Workstream H and a dedicated digital-AI ecosystem module: full physical/digital value chain, deployment/overhang, economic evidence, benchmarking, multi-agent coordination, lab competition/deploycos and complementary businesses. Distinguished multivariate analogies from direct robot/site/enterprise/R&D contributions; added evolving digital baselines, joint scenarios, source/target records, two dashboard workspaces and ten roadmap questions (41 total). Preserved all prior workstreams and prepared-only campaign status.

- **0.8 — 25 October 2026:** Made capital-funded customer-side AI-native entry explicit, including operating-design, equal-technology adoption-timing, and capacity/availability hypotheses. Added funding/runway, customer acquisition, competitive response, and standalone/platform/build/acquire/hybrid comparisons; sourced the Thrive Holdings analogy. Expanded the roadmap to 31 open questions while preserving seven workstreams and the separate provider/asset/control inquiry.

- **0.7 — 25 October 2026:** Clarified customer ownership and organization as determinants of adoption, capital allocation, automation appetite, implementation capacity, and value-chain position. Retained the previous provider/asset/control/value-capture research as a distinct seventh workstream. Added separate adopter/commercial records and dashboard views; expanded the roadmap to 28 questions with prior provider questions preserved.

- **0.6 — 25 October 2026:** Adopted Amar's end-market/value-chain organizing level and strategy/deployment objective. Replaced warehouse-first, mandatory Excel-first, and delayed-dashboard sequencing with a prepared seven-day research campaign and continuing roadmap. Added capability/scaling, learning/control/data aggregation, physical-digital fleet coordination, and competing ownership/coexistence pathways. Preserved evidence, accounting, versioning, and separate Ixion scope.

- **0.5 — 6 September 2026:** Adopted the private amarmurray/robotics-economics repository and main branch as the shared accepted source. Replaced hourly uploads with repository review at each Work session's start, commit-pinned reads, and scoped commit/push publication after substantive authorized Codex tasks. Paused the earlier hourly automation; preserved explicit proposal review, access verification, and the separate Ixion implementation boundary.

- **0.4 — 5 September 2026:** Installed an hourly synchronization automation for changed canonical sources and incoming ChatGPT Work findings. Added an operating guide, content-based change detection, conflict preservation, and quiet unchanged runs. Future scheduled execution remains subject to available local files, browser access, and app runtime.

- **0.3.1 — 5 September 2026:** Confirmed both projects exist, recorded their displayed names, and adopted the user-created Robotics Economics folder as the canonical local workspace. Research content and the versioned handoff protocol are unchanged.

- **0.3 — 5 September 2026:** Defined the paired Codex and ChatGPT Work arrangement for robotics economics. Added shared artifact ownership, versioned source snapshots, reciprocal review, explicit handoffs and receipt checks, conflict handling, and truthful synchronization status. Preserved the separately scoped review before adopting work into the existing repository.
- **0.2 — 5 September 2026:** Promoted provider mapping to an equal analytical workstream alongside end markets and customer deployment value chains. Added initial sourced robot references, version and evidence rules, provider economics and competition, ecosystem relationships, dynamic update logic, and links to the first economic case.
- **0.1 — 5 September 2026:** Established the research purpose, workspace, accounting boundaries, penetration waterfall, learning framework, and first-case plan.
