# From operating continuation to a financeable deployment

Edition 0.23 extends the existing F/G customer package through FG-E019–FG-E023 and FG-AUDIT-01. It changes the evidence supporting deployment gates, without changing synthetic coefficients. The inference is that operating continuation, customer value and provider survival require three different demonstrations. None can substitute for the others.

## What the new sources establish

[GXO's 26 October announcement](https://gxo.com/news_article/gxo-and-agility-robotics-expand-partnership-to-accelerate-deployment-of-humanoids-in-u-s-operations/) describes continued Flowery Branch operation and planned additional sites. Its site tote count and Agility's broader operating-hour count have different populations. Their quotient would not measure a site's rate. Additional deployments begin on Digit 4, with later Digit 5 migration planned. This strengthens the existing prompt-incumbent counterexample in FG-CMP-01; it does not establish completed migration or matched payroll savings.

The [6 October investor presentation](https://www.sec.gov/Archives/edgar/data/2074973/000121390026107259/ea030784201ex99-1.htm), visually checked at slides 45, 57 and 66, separates customer illustrations, generation-specific BOM and provider product economics. Its BOM-recovery definition of provider payback omits costs that still need funding. The [13 October prospectus](https://www.sec.gov/Archives/edgar/data/2074973/000121390026109058/ea0297114-07.htm) supplies explicit planning components and historical company statements. They support a reproducible boundary audit, not an executed price quote or measured site return. The generated report and dashboard show the arithmetic from those saved records.

The [5 November closing update](https://investors.agilityrobotics.com/news-releases/news-release-details/agility-becomes-first-us-publicly-listed-pure-play-humanoid) changes financing status from expected to completed. Its aggregate includes earlier funding and is stated before transaction expenses. Subtracting the earlier component prevents one obvious double count but does not reconstruct the closing bank balance. Historical operating cash use remains informative about the earlier business; it is not a forecast of future burn or a post-close liquidity verdict.

The [22 October compute announcement](https://investors.agilityrobotics.com/news-releases/news-release-details/agility-robotics-expands-nvidia-collaboration-it-prepares-digit) concerns the planned general-availability Digit 5 configuration and evaluation before final certification. It identifies a dependency for qualification, not a measured improvement in accepted service. It must not be retroactively assigned to the operating Digit 4 cohort.

## Three gates, with different failure modes

**Operating gate.** A buyer needs unique accepted handoffs on time, matched demand and exposure, a specified configuration, and all retained work. Aggregate counts can show that a deployment persisted while remaining insufficient to price a unit of service. A new location also requires its own layout, systems integration, staff procedure and safety acceptance. Expansion therefore increases the importance of a repeatable qualification process; it does not eliminate it.

**Commercial gate.** The relevant contract must allocate acceptance, payment start, service interruption, upgrade costs, termination and residual equipment responsibility. A paid evaluation program can be valuable engineering work without becoming a recurring productive deployment. Its fee, a per-robot deployment charge and a service subscription represent different obligations. No program charge should be silently assigned to the earlier GXO contract. The source's five-year illustration also cannot turn a conditional three-year order into five years of assured collections.

**Provider funding gate.** Hardware construction, deployment work, service delivery, software development and corporate operations require cash on different dates. A subscription can be attractive over a hypothetical life yet fail to finance its initial hardware or a support surge. Conversely, a company's development-stage losses do not by themselves prove that one mature site has unfavorable incremental economics. A fair assessment keeps both levels visible and asks what share of shared development/support is avoidable, recurrent or required for the next qualified cohort.

The reproducible payment-component totals deliberately omit unpriced customer work and financing. The provider product-cost subtotal deliberately excludes corporate costs, consistent with the source boundary. They are not consolidated resource totals: the customer fee is a transfer to the provider, while provider labor and hardware are uses of resources. Add the underlying resources once when consolidating; keep the fee in each actor's cash account. Neither a product margin nor a whole-company loss divided by a missing robot denominator resolves the full-service cost.

## Substantial H: software is an operating and qualification obligation

This case links digital work to deployment through three distinct layers: onboard policy and safety computation, fleet/site orchestration and diagnostics, and R&D that produces a candidate update. The prospectus's Arc discussion provides context for the operating layer, including local sensory processing and diagnostic transmission. It does not establish that every observation is exported as reusable training data or that customer data rights permit cross-site training.

The decision question is whether an update improves the constrained accepted service after qualification and ongoing support. In the [funded learning worlds](learning_execution.md), hypothetical candidates must earn their place through paid tests and retained-cohort checks. The present source audit adds a real reason to maintain that separation: commercial generations and compute configurations are changing while an existing cohort continues to operate. The synthetic worlds do not forecast Agility's update success, migration time or costs.

A buyer should be able to specify the supported version, update approval and rollback, the operating envelope during network loss, incident responsibility and the data needed to reconcile a failed task. These are proposed contract/qualification questions, not findings that the product lacks those capabilities. A provider should separately budget ongoing software and support from the research program that may unlock new tasks. Combining them into an inference-token price would conceal the engineering and service obligations that determine scale.

## Consequences for the existing deployment and entry decisions

| Decision | Proceed gate | Wait or reject trigger |
| --- | --- | --- |
| Existing tote workflow | Continue a bounded site evaluation once acceptance, retained work, exposure and funded support are observable. | Wait on expansion valuation when hours, schedules or contract terms cannot be matched; reject a cost-per-tote calculation using fleet hours from another population. |
| Hospital logistics | Apply the same service, interruption and funded-support questions to the hospital's complete request and handoff workflow. | Do not transfer warehouse rates, generation readiness, labor assumptions or prices to hospital service. |
| Utility inspection | Price complete accepted measurements, residual visits and response obligations for the chosen configuration. | A mobile-platform financing headline cannot remove physical duties or replace inspection qualification. |
| Automotive workcells | Qualify the actual generation, end effector, presentation and retained task mix before scaling. | Wait when a future compute/safety configuration is required for the proposed workflow; retain the qualified conventional comparator. |

For a standalone operating entrant, supplier funding is helpful context but does not provide the entrant's working capital, customer demand or implementation authority. An acquisition can bring those relationships while also importing obligations. A hybrid can pool specialist integration and service capacity, but its fees and incident authority need an explicit allocation. GXO's continuation means prompt incumbent adoption is a live competitive possibility; the entrant cannot claim a durable technology-access advantage from a public robot offering alone.

These findings reinforce staged deployment and actor-specific funding rather than a market-wide humanoid ranking. The three principal campaign recommendations remain provisional. No new empirical whole-system-cost requirement is closed.

## Reproduction and stopping rule

`commercial_disclosure_summary` in [research_calculations.py](../model/research_calculations.py) reads typed quantities in [customer_evidence.json](../data/customer_evidence.json). The normal scenario exporter refreshes [observed_research_summary.json](../model/results/observed_research_summary.json). Exact equations and source identifiers accompany each calculation. Null customer ROI/payback, paid labor removal, site rate, net closing cash and runway remain null. Historical periods are not annualized.

Reopen this source branch when a public executed service agreement, matched site operating/staffing record, qualified Digit 5 release or post-close financial statement changes a gate. Repeated announcements are not new independent cohorts. Further public searching without such a trigger has low decision value; advance the remaining cross-cell execution challenges instead. No outreach or commercial transaction was undertaken. See the [sole-writer review](../reviews/commercial_disclosures_review.md).
