# Robotics supply chains, embodiments, and open ecosystems

Version 1.0 · 25 October 2026 · Workstream I

## 1. Purpose and place in the program

Explain which physical systems can serve each end market, what it takes to manufacture and support them, and how the availability, cost, performance, and control of key inputs constrain deployment over time. This is a substantial continuing module covering humanoids and quadrupeds directly, with other embodiments and drones included where they change a comparison or illuminate a mechanism.

The organizing unit remains **end market × value-chain stage × operating archetype × geography × time**. A component map, company roster, or embodiment taxonomy is a supporting view of that economic map. The career objective remains strategy and staged deployment at a humanoid company; understanding when another system is preferable is part of that competence.

Read this module with [RESEARCH_PROGRAM_DESIGN.md](RESEARCH_PROGRAM_DESIGN.md), [QUADRUPED_AND_DRONE_RESEARCH_MODULE.md](QUADRUPED_AND_DRONE_RESEARCH_MODULE.md), and [LLM_ECOSYSTEM_RESEARCH_MODULE.md](LLM_ECOSYSTEM_RESEARCH_MODULE.md). I owns component, production, architecture, openness, and physical supply mechanisms; J owns quadruped deployment dossiers and drone comparisons. A–H retain their existing responsibilities. Use common actor, system, activity, resource, rights, and evidence IDs across them.

The central question is: **For a specified productive outcome and deployment scale, which combinations of embodiment, autonomy, components, manufacturing, capital, and field operations are feasible, by when, and who can capture value along the resulting chain?**

## 2. Distinguish the forms of scale

Maintain separate explanations for:

1. **Capability improvement:** what a configured system can accomplish at a given quality, reliability, assistance, and resource budget.
2. **Production learning and cost:** how repeat manufacture, design changes, sourcing, and process learning affect qualified unit cost and quality.
3. **Manufacturing capacity:** how many qualified units and compatible spares can actually be delivered per period.
4. **Operational scale:** how much installed capacity can be commissioned, maintained, supervised, and productively used.
5. **Economic penetration:** how much demand is served and how labor, output, customer surplus, revenues, and returns change.

These interact but are not interchangeable scaling laws. A more capable policy need not reduce actuator cost; a lower robot price need not relieve support congestion; a larger factory announcement need not create qualified supply. Define every proposed scale target: cumulative production, annual shipments, active installed fleet, accepted output, or share of a specified economic denominator. Do not use one number as all five.

Investigate empirical response relationships where comparable evidence exists. Separate cumulative output from calendar time, product generation, input prices, utilization, purchasing discounts, subsidized pricing, and quality changes. Manufacturing learning curves, software/data response surfaces, and adoption trajectories need different evidence and parameters. A declining quoted selling price does not identify a decline in cost, and a cost decrease does not establish sustainable provider margins.

## 3. Full physical and economic value chain

Map upstream materials and process equipment through qualified components, robot integration, software/model provision, delivery, field service, and customer output. Preserve material, data, cash, contractual, and control relationships separately. Trace the deepest upstream dependencies for consequential bottlenecks rather than attempting an unsupported complete bill of materials for every robot.

| Layer | Required coverage | Connection to capability, scale, and economics |
| --- | --- | --- |
| Materials and basic processing | Magnetic materials, copper, aluminum/steel, polymers/composites, battery materials; processing and substitution routes where relevant | Material qualification, conversion capacity, geography, lead times, alternative uses, and exposure to price or access changes |
| Actuation and transmission | Motors, windings/magnets, drives, strain-wave/planetary/other reducers, direct or quasi-direct drives, ball/roller screws, bearings, brakes, encoders, force/torque sensing | Torque–speed envelope, backdrivability, efficiency, thermal limits, shock loads, lifetime, precision, yield, maintainability, and supplier qualification |
| Manipulation and end effectors | Hands, grippers, tendons/cables, fingertip/tactile sensing, tool interfaces, consumables | Fit to work, contact robustness, changeover, repair burden, replacement inventory, and additional control/data requirements |
| Compute and memory | Onboard processors/accelerators, microcontrollers, memory type/capacity/bandwidth, storage, interconnect; remote inference and training as separate resources | Model footprint, latency, concurrent workloads, bandwidth, power/heat, software compatibility, sourcing, and recurring compute cost |
| Perception and state estimation | Cameras, depth sensors, lidar, IMUs, position/force sensors, GNSS where applicable, calibration | Environmental fit, sensor fusion, failure recovery, cost, calibration labor, and configuration-specific autonomy |
| Energy and thermal systems | Cells, packs, BMS, charging/swapping infrastructure, power conversion, cooling and thermal design | Duty cycle, peak/continuous load, degradation, charging queues, fire/environmental qualification where relevant, and fleet availability |
| Structures, interfaces, and connectivity | Frames, seals, housings, feet/wheels, connectors/cabling, field buses, radios, networking, docks and payload mounts | Weight, durability, ingress/temperature limits, payload, repair time, connectivity dependence, and ecosystem compatibility |
| Production and quality | Tooling, machining/forming, winding, electronics assembly, metrology, test rigs, calibration, burn-in, system assembly and acceptance | Capital, labor/process skills, throughput, yield, rework, supplier switching, validation, and ramp delays |
| Models and software | Simulation, training/data tools, firmware, middleware, policies, orchestration, monitoring, updates | Development effort, reproducibility, interoperability, dependency/control, version compatibility, and lifetime support |
| Deployment and support | Integrators, site preparation, workflow/enterprise interfaces, supervision, maintenance, spares, repair/refurbishment, transport and training | Time to useful output, staffing, service density, uptime, recurring costs, working capital, and scalable delivery capacity |
| Commercial and customer layers | OEMs, distributors, operators, lessors, financiers, insurers where material, customers and productive businesses | Pricing, risk, asset/data rights, cash timing, bargaining power, entry pathways, and value capture |

Do not assume every robot uses every component architecture. Record joint-level rotary/linear, geared/direct, electric/other configurations when material. A nominally similar actuator is not necessarily interchangeable across torque, shock, thermal, precision, packaging, control, or lifetime requirements. An open CAD file or an off-the-shelf part does not by itself establish production yield or field qualification.

Memory must be a first-class input. Distinguish onboard memory and bandwidth from training/remote-inference memory and from software context/state. NVIDIA's published Orin and Thor families provide useful configuration-specific examples of compute, memory, power, and interface tradeoffs; their specifications are not measured robot productivity. For example, Orin configurations specify LPDDR5, while the datacenter H200 specifies HBM3e. Do not pool these into a fungible memory constraint or presume that a data-center bottleneck applies identically to embedded modules. Training and inference can both use datacenter resources. [Orin specifications](https://www.nvidia.com/en-us/autonomous-machines/embedded-systems/jetson-orin/); [Thor specifications](https://www.nvidia.com/en-us/autonomous-machines/embedded-systems/jetson-thor/); [H200 specifications](https://www.nvidia.com/en-us/data-center/h200/).

## 4. Embodiment is an economic design variable

Represent embodiment as attributes and configuration choices, not a ranking from primitive to advanced. Distinguish bipedal humanoids, wheeled humanoid/mobile manipulators, sensor-carrying quadrupeds, quadrupeds with manipulators, wheel-legged hybrids, AMRs/AGVs, fixed arms and automation, specialized machines, drones, and human–machine combinations. Treat these as candidate families; document the actual system, payload, policy, and integration.

Compare reach, access/terrain, manipulation, payload at working posture, energy/duty cycle, speed, footprint, noise, environmental suitability, supervision, durability, serviceability, and the surrounding process. Simpler grippers, tools, or altered workstations may outperform anthropomorphic hands for a particular outcome. More degrees of freedom can expand reachable work while increasing cost and operational burden; the net effect is a research question.

For each selected market-stage cell ask:

- Which outcome and service level must be delivered, and which physical requirements are indispensable?
- Which alternatives satisfy them today, including digitally improved human operations and process redesign?
- Where does the embodiment create economic value, and where does it add capabilities the customer does not need?
- How do mobility, manipulation, sensors, compute, and software choices change one another's requirements?
- Which mixed fleet or shared infrastructure arrangement beats a single universal machine, if any?
- What must change for the preferred configuration to change, and what retrofit or stranded-asset consequences follow?

Assess the whole configured system and workflow: purchase/manufacturing cost, payloads, software, integration, site changes, human work, energy, consumables, charging, downtime, maintenance, spares, replacements, financing, and decommissioning. Use matched accepted output and quality; disclose unmatched capabilities. A cheap research platform and an industrial service package should not be compared by headline sticker price.

Where systems compete for the same underlying activity, allocate that activity once. Where they perform complementary stages, preserve the handoffs and shared costs. A drone inspection, a quadruped inspection, and subsequent human maintenance may be one coordinated workflow; the same avoided visit or information benefit cannot be booked three times. Cross-embodiment learning remains a directed, tested transfer hypothesis.

## 5. Time-indexed production and deployment feasibility

Build a versioned dependency network linking qualified input classes and facilities to system configurations, assembly/test capacity, finished goods, shipping, commissioning, service resources, and active fleets. Track named supplier relationships separately from hypothesized alternatives. An announced partnership, order, preferred-supplier status, planned plant, nameplate capacity, qualified capacity, shipments, and observed productive operation are distinct states.

For a bounded model, let `A[p,t]` denote assembly starts of system configuration `p`; `b[k,p,t]` the compatible component units required per start; `D[k,t]` qualified component deliveries; `I[k,t]` available inventory; `S[k,t]` parts consumed by installed-fleet service; and `R[k,t]` separately modeled rework/test consumption. Then enforce:

```text
I[k,t] = I[k,t−1] + D[k,t]
         − sum_p(b[k,p,t] × A[p,t]) − S[k,t] − R[k,t] − other_allocations[k,t]
I[k,t] ≥ 0
```

State whether scrap is included in `b`, component qualification, or `R`; count it once. Model robot assembly/test yield and lead time separately to turn starts into accepted finished systems. Conserve finished-goods stocks as systems are shipped and commissioned. Upstream manufacturing yield affects qualified deliveries; it must not be applied again if deliveries are already measured after acceptance. Production capacity also has process, equipment, labor, funding, and time constraints.

Use **qualified receipts actually accessible to the modeled inventory pool**, rather than worldwide commodity supply assumed accessible to every provider. State whether `D` is gross or net of commitments to customers outside the explicitly modeled system set. Deduct each commitment once: if it is already removed from net `D`, exclude it from `other_allocations`; otherwise show it in `other_allocations`. Product grades, packaging, geography, lead times, contracts, inventory, and qualification prevent automatic substitution. Map shared upstream capacity across humanoids, quadrupeds, drones, digital AI, industrial automation, and other customers only where there is evidence of an actual shared resource; common supplier names alone do not establish a common bottleneck.

Installed cohorts consume maintenance and support resources before expansion. Replacement units, retired robots, refurbished units, spare assemblies, and net additions need separate stock flows. Do not count a replacement as net fleet growth or a spare actuator as a new robot. Capacity remaining after support and replacement can constrain new deployments even when new-unit production is increasing.

Model expansion through announced → financed/ordered → installed → qualified → ramping → sustained capacity states where evidence permits. Include tooling, equipment delivery, supplier validation, customer validation, ramp yield, working capital, and field-service coverage. Capital-expenditure announcements do not set those lags to zero. Different providers can have different access to the same nominal supply pool.

Connect this model to Workstream C's commissioning and active-stock identities and B's capability thresholds. For each defined scale target, show both a forward trajectory and a **backcast of necessary conditions**: required annual qualified components, production lines, yields, investment and orders by date, integration/service staffing, retained fleet, and demand. A feasible resource path is necessary but not proof of adoption; do not turn a backcast into a forecast. Unsupported inputs remain ranges or named gaps.

At minimum test slower component qualification, delayed expansion, and greater service/spares requirements; include a case where component supply is ample and customer readiness or economics binds instead. Show bottleneck migration, not a permanent claim that one component will always be scarce. Avoid using correlated best cases for every input as a central forecast.

## 6. Key players, competition, and value capture

Map companies by actual roles, product generations, geography, production relationships, customer channels, capital commitments, and evidence status. Cover component suppliers, semiconductor/memory providers, contract manufacturers, OEMs, autonomy/model developers, open-project maintainers, integrators, payload providers, operators, and financiers. Record ultimate ownership and contracting entities where relevant; an entity can occupy several layers.

The current humanoid seed roster in the charter remains a starting point to refresh. Quadruped and drone coverage belongs to J's sector-driven registry, and must extend beyond familiar US brands. Supplier coverage follows consequential component dependencies, including regional manufacturers and alternatives. Do not label a firm a leader based on publicity, GitHub activity, a financing announcement, or a single order.

Investigate make/buy/partner decisions, custom versus standardized components, vertical integration, contract manufacturing, modular interfaces, multivendor sourcing, and service networks. Ask which layers become more standardized as volumes grow, which remain differentiated by reliability or integration, and where an OEM's cost reduction changes supplier bargaining power. Model margins and entry barriers as conditional findings, not as automatic implications of a long component list.

Schaeffler describes roles spanning components, customer use, industrialization, and lifetime service; Boston Dynamics and Hyundai Mobis announced an actuator collaboration. These are useful examples of overlapping roles and contractual dependencies to investigate. They do not establish realized supply volumes, exclusivity beyond disclosed terms, comparable unit economics, or an industry-wide actuator cost share. [Schaeffler](https://www.schaeffler.com/en/technology-innovation/technology/humanoid-robots/); [Boston Dynamics–Hyundai Mobis announcement](https://bostondynamics.com/news/hyundai-mobis-forms-strategic-collaboration-framework-with-boston-dynamics/).

Trace how availability and standardization could enable customer-side AI-native newcos, independent deployers, or component/service specialists, and how incumbents can obtain the same inputs. Preserve the separation between customer formation in F and provider/commercial allocation in G. Supplier investment may depend on credible customer commitments; customer adoption may depend on reliable supply and service. Study this coordination problem and the risk of both underinvestment and excess capacity.

## 7. What counts as open robotics?

There is no single robot-company equivalent of digital open source. Construct a layered, dated rights and reproducibility matrix. Public availability, low purchase price, research popularity, interoperability, and open-source licensing are separate properties.

| Layer | Questions to verify per artifact/version |
| --- | --- |
| Hardware | Are design files, schematics, tolerances, BOM, tooling, assembly/calibration instructions, and necessary manufacturing rights available? Which purchased subsystems remain closed? |
| Firmware and control | Is source available, buildable, modifiable, and deployable on the relevant device? What bootloader, driver, binary, or calibration dependencies remain? |
| SDKs, middleware, and interfaces | What can a developer inspect or command? Are interfaces documented and stable, and can the system operate independently of a vendor service? |
| Models and policies | Are weights, inference/training code, recipes, evaluation harnesses, and needed base-model rights available? Which embodiments and actions are supported? |
| Data and simulation | What can be accessed, redistributed, reused, and trained on? Are assets, real-world data, provenance, and simulator dependencies sufficient for reproduction? |
| Commercial operation and support | Which rights, warranties, service conditions, telemetry requirements, repair options, and version restrictions affect actual deployment or independent manufacture? |
| Project governance | Who maintains releases, accepts contributions, controls interfaces, funds support, and can change future access or roadmap? |

Record the license text and scope, release/commit, dependencies, distribution conditions, and unresolved conflicts. Do not infer that one permissive repository license covers a complete robot, model lineage, dataset, or commercial service. A numerical openness score must not conceal decisive missing rights; show the matrix first.

**Unitree is a useful platform-ecosystem case, not a blanket open-source classification.** Its SDK2 has a BSD-3-Clause license, while the UniFoLM-WMA repository specifies CC BY-NC-SA 4.0, including a noncommercial restriction. Check each checkpoint and dataset separately; a repository announcement does not verify every download or dependency. Product variants and developer access must also be checked separately. An SDK license alone does not demonstrate an open hardware manufacturing package, fully open firmware, or training-data/policy rights. [SDK2 license](https://github.com/unitreerobotics/unitree_sdk2/blob/main/LICENSE); [UniFoLM-WMA repository license](https://github.com/unitreerobotics/unifolm-world-model-action/blob/main/LICENSE); [G1 product](https://www.unitree.com/g1/); [Go2 product](https://www.unitree.com/go2/).

Use genuinely different layers as comparators. The Open Dynamic Robot Initiative publishes mechanical/electronic designs and assembly information for platforms including Solo, with licenses attached to the relevant repositories. ROS, drone autopilot projects, and released robotics policies/data supply different kinds of openness. Assess each artifact and its dependencies before drawing commercial implications. [ODRI hardware repository](https://github.com/open-dynamic-robot-initiative/open_robot_actuator_hardware); [ODRI board and firmware repository](https://github.com/open-dynamic-robot-initiative/master-board).

Include Octo as a released-policy example: the project code and Octo Base 1.5 model card specify MIT, while upstream datasets and practical adaptation remain separate checks. PX4 provides a drone flight-control software ecosystem with hardware and commercial-system interfaces, rather than a single entirely open aircraft. These examples make the layered comparison concrete; they do not establish production readiness or commercial success. [Octo code](https://github.com/octo-models/octo); [Octo model card](https://huggingface.co/rail-berkeley/octo-base-1.5/raw/main/README.md); [PX4](https://px4.io/).

## 8. Economic differences from digital open models

Test mechanisms in both directions. Shared code, weights, interfaces, data, and hardware designs might reduce duplicated R&D, lower entry costs, support specialization, improve reproducibility, enlarge a developer ecosystem, or reduce vendor dependence. They might also shift differentiation to reliable manufacture, distribution, service, proprietary data, integration, or capital. Those are hypotheses whose size and incidence require evidence.

Digital weights can be copied while inference still consumes hardware, energy, engineering, and sometimes adaptation. In robotics, copying software or a design also leaves the need to manufacture, assemble, calibrate, deploy, validate, maintain, and finance physical units. Additional embodiments and operating conditions can require new data or adaptation. Avoid the false comparison of free digital deployment with costly physical deployment; specify both production functions and their complements.

Compare access to a common robot platform against permission and practical ability to reproduce the robot. Ask whether openness primarily expands research participation, lowers commercial adoption cost, improves repair, enables new hardware suppliers, strengthens an incumbent platform's sales, or changes the distribution of rents. GitHub stars and robot sales are neither commercial autonomy nor productivity measures. A platform may benefit commercially from open complements while retaining control over critical hardware or services.

Investigate interoperability versus integration, compatibility across revisions, maintainer funding, fork costs, and deployment responsibility. Join H's evidence on digital open models and lab complements to I's artifact-level rights and J's field evidence. Keep source and target effects separate; an open-model adoption rate cannot directly calibrate robot adoption.

## 9. Data and dashboard additions

Extend existing schemas rather than creating a separate supplier universe:

- **Component/configuration:** component and grade IDs; units per assembly start; role; specification envelope; hardware revision; supplier/facility links; qualification and substitution; unit cost/price basis; evidence and unknowns.
- **Supply capacity:** resource/facility/geography/time; nameplate and qualified output; yields and their boundaries; existing commitments; allocations; inventory; expansion stage, funding, lead time and confidence.
- **Production/service flow:** starts, accepted completions, work in progress, finished goods, shipments, commissioning, spare/replacement demand, repair/refurbishment and retirement by compatible cohort.
- **Embodiment comparison:** matched work/output/quality; configurations and alternatives; capability requirements; resource and cash differences; complements; exclusions; break-even conditions; evidence/scenario links.
- **Openness artifact:** artifact/layer/version/license/source; reproducibility; dependency and rights chain; interfaces; modification/operation/manufacture restrictions; practical switching/repair; evidence gaps.

Add a **robotics supply and production explorer** with a component/facility/system graph, bottleneck timeline, scale-target backcast, shared allocations, and cost/capability sensitivities. Add a linked **embodiment and deployment comparator**, shared with J, for matched outcomes, mixed fleets, market fit, openness layers, and evidence maturity. Qualitative relationships must not appear as measured flows. Users can select configuration, input class, region, year, qualification/yield/expansion assumptions and service burden where modeled; overrides do not rewrite observed facts.

## 10. First-week deliverables and continuing research

The authoritative first-week contract is [WEEK_ONE_RESEARCH_SPEC.md](WEEK_ONE_RESEARCH_SPEC.md). Reuse its existing six deeper market-stage cells and shared data/model; do not create an extra economy-wide denominator for each embodiment. Preserve H's substantial approximately one-third research-attention default, counting shared work once. I/J have substantial dedicated outputs without a second fixed time quota or a promise to complete their entire multimonth agenda.

Produce a connected supply/value-chain map across the layers above; two sourced system/component configurations, one humanoid and one quadruped; at least two matched embodiment comparisons; one time-indexed production-to-deployment scenario with a scale-target backcast and sensitivity cases; and at least five layered openness cards spanning a commercial platform, open hardware, middleware, policy/data, and drone software. Unknown proprietary BOM, costs, yield, and capacity remain explicit. Include key-player coverage and a substantive report section with the two linked dashboard views.

These are connected evidence/model packages, not independent large studies. Requirements can share one well-supported case, but each promised perspective must be visible. Use literature and public evidence; no manufacturing, hardware, or GPU experiments are implied. Preserve unanswered sourcing, rights, cost, qualification, capacity, service-life, transfer, and economic questions as bounded roadmap items.

Acceptance requires traceable sources, consistent units and stock flows, no duplicated resource allocation or yields, matched outcome comparisons, layer-specific openness, explicit unknowns, and an explanation of how supply or embodiment findings change deployment sequence. Preparation of this module does not activate the seven-day campaign.

## 11. Source status

The linked primary sources were checked during design preparation on 25 October 2026. Product pages and repositories are live references; the campaign must pin the versions actually used, verify license scope and lineage, and preserve observation/publication/retrieval dates. They are seeds for investigation, not a completed player census, BOM audit, capacity estimate, or validated commercial forecast. J supplies deployment/drone anchors; H supplies digital-development and infrastructure anchors.
