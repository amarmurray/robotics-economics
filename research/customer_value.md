# Customer organization, entry, and robotics value capture

First-wave F/G findings · 25 October 2026 · Version 0.1.1
Input revision: `campaign launch snapshot (see ignored sync_receipt.json)`
Evidence: [customer_evidence.json](../data/customer_evidence.json). Common numerical assumptions and calculations belong to [model/assumptions.json](../model/assumptions.json) and [model/engine.py](../model/engine.py).

This is a bounded first-wave result, not campaign completion. The requested configuration was GPT-6 Astra with Ultra reasoning; this delegated runtime does not expose a verifiable active model/reasoning identifier. Actual settings therefore remain unverified. Primary documents were retrieved during this session through Exa. Source dates, claim locators, geography, limitations and missing terms are recorded separately from interpretations.

## Decision finding

An AI-native operating newco needs a reason to win after incumbents can buy the same robots. Current evidence already includes incumbent adoption: GXO reports a commercial humanoid RaaS deployment, and ISS describes a substantial specialized-cleaning-robot program. The strongest initial entry thesis is conditional: win a defined service obligation, control enough of the workflow to deliver it, survive commissioning and collections, and preserve an advantage in operating design, customer access or constrained capacity after competitors respond. Neither an AI-native label nor cheaper hypothetical robots establishes this sequence.

Customer organization and provider arrangements change different constraints. On the customer side, ownership can affect capital allocation, approval, process authority, implementation and retention of gains. On the supply side, a sale, subscription, lease or managed operation allocates asset funding, utilization risk, service work, control and rights. A structure can relax one party's constraint by moving it to another party. An investment case therefore needs both maps and consolidated cash accounting.

Three first-wave findings are consequential:

1. **Service contracts can matter more than corporate ownership labels.** The same reduction in physical effort has different cash effects under fixed-price, cost-plus and hourly contracts. Contract termination can precede robot-cost recovery. These are disclosed mechanisms, not conjectures about public versus private management.
2. **Incumbents have evidenced complements to common robot access.** Existing customers, software integration, service networks and site knowledge must be included in the same-technology comparator. An entrant may design a better process, but that is a separate hypothesis requiring costs and evidence.
3. **Asset or data ownership does not establish exclusive control.** A retrieved BrainOS agreement gives the end user operational-data ownership while giving Brain durable nonexclusive improvement-use rights. The robot, software, customer relationship, workflow authority, practical data access and economic learning benefit can belong to different parties.

## What the sources establish

| Evidence | Finding and decision consequence | What remains unknown |
| --- | --- | --- |
| FG-E001: [GXO, 27 June 2024](https://gxo.com/news_article/gxo-signs-industry-first-multi-year-agreement-with-agility-robotics/) | Multi-year Digit RaaS with Arc at a SPANX operation, following a late-2023 pilot; totes move from AMRs to conveyors. An incumbent operator is already a route to deployment and coordinated workflows. | Fees, exact term, legal asset owner, SLA, uptime, intervention exposure, economics and data rights. Commercial announcement is not a controlled performance study. |
| FG-E002/003: [GXO 2025 Form 10-K, filed 25 February 2026](https://www.sec.gov/Archives/edgar/data/1852244/000185224426000007/gxo-20251231.htm), Item 7 and Item 1A | Contracts include fixed-price and cost-plus; some infrastructure investment is recovered across customer relationships. Onboarding requires capital and operational effort; customers can solicit competing bids or insource. | SPANX's particular contract form and the size of each adoption mechanism. Company-wide disclosure cannot fill a site-specific ROI model. |
| FG-E004/005: [ISS, 19 March 2026](https://www.issworld.com/insights/blog/technology-and-innovation-in-cleaning) | ISS describes deploying over 800 sweep/vacuum/scrub robots across 21 countries, site-specific evaluation and privacy checks, digital scheduling, and retained human quality review. | Retained productive count, exposure, costs and causal productivity. Its 30% UK efficiency claim has no disclosed denominator or payroll reconciliation. It is not a US or humanoid coefficient. |
| FG-E007: [ABM 2025 Form 10-K, Note 2, filed 19 December 2025](https://www.sec.gov/Archives/edgar/data/771497/000077149725000031/R10.htm) | Service revenues use several contract forms. Most contracts can be cancelled without substantive penalty; the majority have 30–90 days' notice. Asset redeployability and cancellation terms can determine recoverable investment. | The terms of a particular robot contract or ISS customer agreement. This is sector mechanism evidence, not a claim that all clients cancel quickly. |
| FG-E006: [Tennant–Brain, 22 February 2024](https://investors.tennantco.com/news/news-details/2024/Tennant-Company-and-Brain-Corp-Sign-Exclusive-Technology-Agreement-To-Accelerate-Robotic-Floor-Cleaning-Innovation-and-Adoption/default.aspx) | Equipment and autonomy are bundled through Tennant, with recurring autonomy revenue and a specified next-generation floorcare exclusivity arrangement. Distribution and service are part of the commercial product. | Price, supplier split, margin, end-user rights and achieved ROI. The announcement does not establish blanket exclusivity across all Brain products. |
| FG-E008: [Kärcher-hosted BrainOS agreement](https://s1.kaercher-media.com/media/file/261106/kira-b100-eula-2-2025.pdf), §§2–5, 6 and 10.3 | Software use depends on services, operation remains the end user's responsibility, and operational-data ownership coexists with Brain improvement rights. | Executed customer terms, effective date and actual training gains. Filename `2-2025` conflicts with extracted `v2021_12` metadata; no current universal applicability is assumed. |

Company announcements and filings are primary descriptions of the relevant decisions and terms, but they are not independent evaluations of robot productivity. Two useful counterweights are the retained human work in the ISS description and a [Brain grocery case](https://www.braincorp.com/resources/major-grocery-retailer-enhances-cleaning-operations-and-efficiency-with-tennant-t380-amrs-powered-by-brainos-r) that calls its 2024 hours **reallocated**, while reporting a broader annual-value figure without an auditable methodology. Neither supports treating all released time as cash savings. FG-E012 preserves that distinction.

## Two controlled customer comparisons

### Contract logistics: outsourced operator versus own-account operation

`FG-CMP-01` joins `CELL-M08-3pl-tote-US-2025`. The useful outcome is an accepted tote handoff at required quality and service timing. Hold tote distribution, layout, system/software, throughput, uptime, intervention and robot commercial terms fixed. This is an explanatory counterfactual, not an observed matched experiment.

In the observed GXO configuration, GXO is both the robot customer and logistics operator; SPANX is the served business. Agility supplies the robot and orchestration. The financier and legal robot owner are undisclosed. This single physical activity appears in the logistics and apparel value-chain views but must not become two opportunity totals.

| Mechanism | Multi-site logistics contractor | Integrated brand/retailer doing the same work |
| --- | --- | --- |
| Capital access/allocation | Can incorporate equipment recovery into a service relationship; still needs finance and customer commitment. | Can invest directly, but fulfillment competes with other internal uses of capital. |
| Appetite | Actual GXO pilot-to-contract progression is evidence of willingness for this use case. | Unknown for the counterfactual; legal ownership alone supplies no estimate. |
| Authority | Operational experience and integration control, subject to client requirements, premises and contract. | Potentially fewer organizational interfaces, but site, safety and business-process approval remain. |
| Implementation | Existing integration and customer onboarding capability can support rollout; no universal cross-site transfer assumed. | May need to build or buy these capabilities even when hardware is identical. |
| Gain retention | Fixed-price contract may retain cost improvements until repricing; cost-plus may pass benefits to the shipper or alter the margin base. | Retains avoidable internal cost reduction, subject to workforce and capacity constraints. |
| Opposing mechanism | Unrecovered investment, performance penalties, client loss and price competition. | Higher implementation burden, stranded dedicated assets and competing capital priorities. |

The pivotal issue is **who can change the process and retain a sufficient share of its gains for long enough to recover the investment**. Under a percentage cost-plus arrangement, reducing allowable labor cost can even reduce the contractor's absolute fee unless gain-sharing or another contract provision compensates it. GXO reports a specified margin, not that every contract has this percentage formula; the reduction is a scenario to test. Fixed-price service instead exposes the contractor to both cost savings and cost overruns. These mechanisms can explain different adoption choices with the same robot, without assigning an ownership multiplier.

The provider implication is to qualify the client contract and approval chain before interpreting an enthusiastic site manager as ready demand. A joint customer/operator deployment agreement may improve incentives, but the negotiation, integration expense and allocation of benefits need explicit treatment. A new logistics operator faces the same technical boundary plus customer acquisition, onboarding capital, service credibility and competitive bidding. GXO's own risk disclosures make a frictionless entrant assumption indefensible.

### Facilities services: contractor versus in-house facility operator

`FG-CMP-02` joins `CELL-M11-floor-cleaning-US-2025`. Hold accepted cleaned area or service zones, frequency, cleanliness standard, layout, robot configuration, supplies, setup and human quality review fixed. Compare a specialist contractor with a facility owner operating the same equipment. The source-backed present competitor is a specialized cleaner. A humanoid doing broader cleaning remains a conditional system and must earn its added scope against that alternative.

A contractor may pool procurement, training, service and movable equipment across clients. Its workflow authority remains bounded by the client's premises, access, work specification and data requirements. Under fixed-price or square-foot service it may retain efficiency gains; under hourly billing, fewer billed hours can reduce revenue; cost-plus depends on the exact margin and allowable-cost rules. The facility operator may retain savings directly and align investment with building use, but needs integration and support capability. None of these effects is guaranteed by size or ownership category.

ABM's disclosed cancellation window creates a concrete asset-contract mismatch. A long asset life or noncancellable supplier lease can outlast the service customer's effective commitment. The useful questions are the recoverable setup cost, relocation cost, compatible next site, downtime between contracts and residual value. A robot that is cheap per productive hour can still be a poor investment if it is rarely productive or cannot be redeployed economically. Conversely, actual customer retention may be much longer than legal notice: using notice periods as measured customer lifetime would be equally wrong.

ISS's [three-year European customer expansion](https://www.issworld.com/insights/news-and-press/iss-signs-new-deal-with-global-technology-company) shows how incumbents can grow through existing relationships and cross-country standardization. It does not disclose cancellation options or demonstrate robot-cost recovery. The combination argues for modeling contract commitment and actual retention separately.

Digital-only improvement also belongs in this comparator. ISS describes activity-based scheduling and customer requests independently of floor robots. Better scheduling can reduce unnecessary cleaning or improve timeliness without replacing the worker. Assigning the same avoided work to both digital scheduling and robotics would overstate the combined benefit.

## Where a customer-side newco could enter

These are qualitative screens, not penetration estimates or verified operating advantages. All cells require accepted output, realistic human complements, customer access and supply/support capacity. Market boundaries use the economic atlas; cross-cutting service views do not add extra labor pools.

| End market / stage | Candidate entry proposition | Principal condition or disconfirmation |
| --- | --- | --- |
| M01 Agriculture, forestry, fishing / field and post-harvest services | Seasonal service capacity or standardized post-harvest process. | Outdoor variability, seasonality and travel can overwhelm utilization; specialized machinery remains the comparator. |
| M02 Extraction / inspection and maintenance support | Sell verified inspection coverage or local service availability. | Site qualification, dangerous-environment requirements and incumbent asset relationships; sensing is not completed repair. |
| M03 Utilities / asset inspection | Service company integrating robotic sensing with maintenance decisions. | Customer permissions, geographic density, review/action workflow and incumbent capability; does not require humanoids. |
| M04 Construction / installation support | Local repeatable package, prefabrication or material-handling service. | Changing sites, subcontract boundaries, skilled supervision and project cash timing. Full enterprise redesign must pay for itself. |
| M05 Manufacturing / bounded process supply | Sell accepted parts or subassemblies, using a redesigned production system. | Qualification, scrap, bottleneck equipment and customer programs. Hadrian supports formation as a comparator, not equal-robot economics. |
| M06 Wholesale / distribution services | Shared automation-supported capacity for smaller customers. | Density, integration and customer switching; preserve overlap with M08. |
| M07 Retail / store replenishment and cleaning | Sell reliable service across a store cluster. | Public-space interference and customer access; established chains and cleaning suppliers already automate. |
| M08 Transportation/warehousing / fulfillment handoffs | Contract operator wins work on service or rapid available capacity. | GXO counterexample to passive incumbents; onboarding, volume commitments and cost-plus incentives matter. |
| M09 Hospitality/food service / preparation and back-of-house | Standardized output and extended service availability. | Hygiene, peak demand, customer experience and cheaper fixed/specialized equipment. |
| M10 Healthcare/social assistance / nonclinical logistics | Supply delivery or support service with strict acceptance requirements. | Clinical governance and urgency, integration, quality and retained staff; throughput is not automatically nursing value. |
| M11 Facilities / repeatable cleaning | Contracted local service with digital dispatch, robots and human quality review. | Contract/asset mismatch, commoditized equipment, service density and prompt same-robot competition. |
| M12 Waste/remediation / sorting and handling | Sell accepted material recovery or service capacity. | Contamination, variable inputs, commodity prices and specialized sorting alternatives. |
| M13 Personal/household/repair / route-based service | Capacity for narrowly defined recurring services. | Dispersed travel, trust, heterogeneous sites, insurance and acquisition cost. General household humanoid service is unproven here. |
| M14 Education/public services / support operations | Procurement-qualified cleaning, maintenance or internal logistics. | Budget/procurement cycles, public accountability and operational authority; public ownership is not a causal adoption coefficient. |
| M15 Arts/recreation/visitor services / venue operation | Off-hours preparation, cleaning and logistics. | Highly variable peaks, public interaction and idle capacity. |

For a humanoid company, this screen favors selling a verified incremental workflow to customers with control, demand and implementation resources while separately testing operator entry where that route solves a real coordination or capacity constraint. It does not establish that starting an operating company is necessary to capture physical-AI value, nor that all current service opportunities need a humanoid.

## Same-robot entrant, financing and incumbent response

Current implementation note: [the shared entrant-market follow-up](shared_enterprise_finance.md) now links customer assignments, actual cohorts and funded enterprise obligations. It leads the Customer adoption view. The older example below is retained as a historical separate reference and is not added to that market.

`ENTRY-FG-01` is a deliberately synthetic monthly formation/ramp example linked to the facilities cell. It sells accepted facility-service bundles; these are normalized model units, not measured square metres or observed humanoid capabilities. A present specialized-cleaner competitor remains explicit. The example tests a conditional broadly available robotic configuration and gives the prompt incumbent exactly the same hardware, accepted productivity and robot commercial terms.

The implementation lane owns all numerical values and generated results in the common engine. The scenario distinguishes a three-month commissioning period, phased ramp, robot payments, retained service labor/materials, enterprise overhead, initial setup/customer acquisition, delayed collections and committed funding. No later financing appears automatically. Incumbent response timing changes price and capturable demand, rather than mechanically converting lower costs to market share. A separate operating-redesign override may change retained costs; it is not the equal-technology baseline.

The identities are:

```text
accepted_capacity[t] = commissioned_robots[t] × accepted_units_per_robot[t] × ramp[t]
served_newco[t] = min(accepted_capacity[t], won_and_retained_demand[t])
served_newco = incumbent_share_transfer + existing_unmet_demand_served + new_demand_served
incumbent_output_after_transfer = incumbent_reference_output − incumbent_share_transfer
cash[t] = cash[t−1] + collections[t] + committed_funding[t]
          − setup[t] − customer_acquisition[t] − robot_payments[t]
          − retained_operating_cost[t] − overhead[t] − other_investment[t]
minimum_external_funding = maximum cumulative cash deficit before external funding
```

Accepted capacity is after the workload's quality and downtime allowances; it must not be multiplied by the same loss again. Collections differ from recognized service revenue, and uncollected receivables are not available cash. Acquisition transfers ownership of existing activity; it does not increase market output. A hypothetical shortage of people can support a capacity proposition only if customers will buy the output and robots plus support can reliably supply it.

Three investment hurdles remain distinct: positive repeatable contribution, survival through ramp, and actual capital availability. The first does not establish the second or third. Financeability is strongest when evidence milestones reduce the remaining risk: customer commitment and site permissions before deployment spend; repeated quality with measured intervention/support before fleet expansion; retention, collections and performance under incumbent response before financing the next operating unit.

A delayed incumbent offers a temporary window. A prompt incumbent can cut price, include the same robots within an existing service bundle, improve its digital workflow, retain customers through broader relationships, partner with the entrant, or acquire it. After technical convergence, the newco needs a demonstrated difference in service, integrated process cost, customer reach or execution. Supplier-mediated learning can improve competitors too. Merely owning the first deployed fleet is not evidence of a durable data advantage.

## Pure newco, builder platform, acquisition and hybrid

| Route | What it buys or creates | Main advantage hypothesis | Costs and reversal conditions |
| --- | --- | --- | --- |
| Standalone operating newco | Genuinely new operating capacity and customer relationships. | Coherent process design; no acquisition premium or inherited constraints. | Formation, qualification, CAC, ramp losses and limited reputation. Prompt incumbent adoption may erase the lead before recovery. |
| Platform creating newcos | Shared engineering, financing and support across genuinely new operating subsidiaries. | Reuse reduces deployment burden where environments and rights permit transfer. | Central overhead, correlated funding calls and weak cross-market reuse; a new parent alone creates no output. |
| Acquire and transform | Existing customers, workforce, licenses, domain knowledge, assets and cash flow. | Shorter commercial ramp and established authority. | Acquisition price can already capitalize expected AI gains; legacy contracts, asset mismatch, debt and integration reduce flexibility. |
| Hybrid build/acquire/partner | Anchor operations plus new capacity or specialized partners. | Existing channels and domain skill support greenfield production. | Combines transition and commissioning risk; requires clear governance and opportunity-cost accounting. |

Acquisition should be compared through the value of purchased customer access, earlier cash flow and reusable operating capability against acquisition premium, transition cost, legacy obligations and financing burden. An observed caution is GXO's Wincanton acquisition: its 2025 filing reports April 2024 completion and June 2025 competition approval subject to divestment of certain UK grocery contracts (FG-E014). This does not identify an AI transformation return. It does show that buying an operator can involve control and portfolio constraints beyond installing robots.

The [OpenAI–Thrive announcement of 1 December 2025](https://openai.com/index/thrive-holdings/) describes owned operating businesses and embedded technical teams, initially in accounting and IT. [Thrive's 12 August 2026 update](https://www.thriveholdings.com/thrive-holdings-fundraise) reports more than $2 billion of new capital at a $12 billion valuation, over 70 owned/operated businesses and expansion into built-environment technical and regulatory services. These issuer descriptions support a structural comparator: capital allocation and deployment engineering under an operating ownership architecture. They do not establish returns, causal productivity or humanoid deployment economics. Technical/regulatory services for the built environment are not interchangeable with robotic construction labor.

The physical extension differs in hardware capital, maintenance, site access, liability, qualified supply, residual values and noncopyable productive capacity. A pure operating-newco platform also differs from buying revenue-producing firms. `FG-AN-THRIVE` therefore permits organizational hypotheses only. It supplies no robotics adoption, productivity, valuation or financing coefficient.

[Hadrian's July 2025 announcement](https://www.hadrian.co/blog/series-c) provides a separate physical-production comparator: an operating manufacturing company, proprietary software, new capital, a loan arrangement and planned factory expansion. It supports the existence of capital formation around a physical operator; it does not validate off-the-shelf humanoid economics. The financing description does not cleanly separate all equity and debt components, so the model must not add an assumed loan amount to the headline figure. Planned factory timing is not verified operating exposure. Defense programs and proprietary production technology are material limits to transfer.

## Provider assets, control and value capture

This inquiry remains separate from the customer pathways. The same newco, acquired operator or incumbent can use several supply arrangements. An integrated robot provider can additionally operate a service business, but its internal robot payment is eliminated when calculating consolidated value.

| Arrangement | Funding and operating allocation | Value-capture question |
| --- | --- | --- |
| Equipment sale | Customer or lender funds acquisition; supplier still finances production and receivables. Customer carries utilization and residual risk subject to warranty/support. | Can hardware margin cover product development and service obligations when autonomy, integration and competition constrain price? |
| Asset lease | Lessor funds asset; operator still funds site setup, employees, working capital and losses. | Who can price credit, residual value, redeployment and obsolescence better? Lease availability and cancellation terms are inputs. |
| RaaS | Customer payment may bundle hardware/software/support; actual title and obligations depend on contract. | Does recurring price cover provider capital, upkeep, intervention and idle risk? Lower customer capex does not eliminate system capital. |
| Usage/outcome contract | Provider/operator may carry unused-capacity risk; accepted-output and customer-caused delay rules matter. | Who can control enough of the process to guarantee an outcome and measure it without dispute? |
| Integration/software | Customer or equipment partner pays for setup and recurring autonomy/orchestration. | Reusable integration and a service channel may capture rents, but interoperability and competing suppliers can constrain them. |
| Managed operation, partnership or JV | Adds end-market execution; governance can unify or complicate decisions. | Are control and customer access worth extra operating risk, shared governance and capital? Equity does not itself grant data/model rights. |
| Provider owning the productive business | Provider funds greenfield/acquisition, overhead and demand formation as well as robots. | Are additional operating margin and verified learning/control benefits worth capital and lost focus relative to selling or partnering? |

For matched output, let baseline customer cost be `B`, retained nonprovider customer cost `A`, provider payment `P`, and provider operating cash cost `O`. Customer operating savings are `B − A − P`; provider operating contribution is `P − O`; consolidated operating benefit is `B − A − O`. Price cancels. One-time investments, collections, working capital and replacement are added at their dates; depreciation is not a second cash outlay. Financing payments between modeled participants also cancel in a consolidated resource view, while the cost and availability of external capital remain relevant.

The feasible commercial interval must satisfy both customer and provider cash requirements, with customer savings based on **avoidable** costs. Customer time redeployed to another task is not the same as payroll removed. A provider discount justified by expected learning is a provider investment, not an unexplained increase in customer savings or a second data premium.

The BrainOS artifact is especially informative. Section 5.2 leaves operational-data title with the end user but grants Brain continuing, nonexclusive rights to store, use and copy it for service and improvement purposes; access/export is not automatically assured. Section 5.2 also excludes aggregated data that is not linked to the end user from the defined Operational Data category; personal data is outside that definition. End-user ownership must be read within those boundaries. Sections 4.1–4.3 reserve software rights and link use to service access. This demonstrates the need to record ownership, access, reuse, export, exclusivity and commercial rights separately. It does not establish that any particular data actually improves a model, that those terms govern Digit, or that a customer cannot negotiate another arrangement.

Tennant–Brain illustrates a complementary distribution/software structure rather than inevitable total vertical integration. Its disclosed channel, service and recurring autonomy roles suggest that access to customers and supported deployment can capture value alongside hardware and models. Exact rents remain unquantified. Competing hypotheses stay live: autonomy could commoditize while local service remains scarce; or proprietary orchestration and dependent subscriptions could preserve supplier bargaining power. Observable renewal, switching, service cost and performance evidence would distinguish them.

## Coverage, limitations and next questions

The two cell comparisons provide sourced mechanisms at fixed technical/workload baselines. They do not estimate a causal effect of ownership. The entrant case specifies equal robot access, commissioning, runway, customer acquisition, demand conservation and competitive response as an explicit scenario. The four enterprise formation routes and distinct provider arrangements are preserved. Fifteen market families have a qualitative entry screen, mostly hypotheses rather than investigated field cases.

The highest-value next evidence is a coherent pair of customer and supplier contracts plus measured operating exposure. Exact fees, accepted output, support time, cancellation, collections and redeployment determine whether an attractive unit margin is financeable. Public procurement and regulatory disclosures are the next authorized research route; no outreach is assumed.

Second, seek matched pilot-to-rollout comparisons that observe approval authority, engineering effort and savings retention, instead of treating public/private/holdco labels as causal. Third, obtain authoritative humanoid data and model terms before modeling exclusive learning. Fourth, compare one genuine greenfield operating ramp with one acquired operator, including price paid, retained customers, cash flow and transition costs. Finally, study renewals and prompt same-robot competitors to separate durable operating advantage from a temporary adoption lead.

These gaps are registered as `FG-Q-01` through `FG-Q-05`, linked to the existing OS/BM roadmap. The next bounded question is: **Can a robot-supported service contract recover all commissioning, customer-acquisition and working-capital costs before cancellation or same-technology competition removes its surplus, and who must finance the intervening cash deficit?**
