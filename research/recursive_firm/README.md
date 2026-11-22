# Recursive Firm Theory

## How production changes what the firm learns

RoboEcon research branch · opened 20 November 2026, US Eastern

**When Capabilities Become Production** asks when a capability, buyer demand, qualification, resources and rights combine to deliver economically accepted work. **Recursive Firm Theory** asks how the organization that performs those conversions comes to exist and changes. A firm can invest in who sees a failure, who may propose an experiment, who bears its loss, and who can revise the operating rule when the result arrives. The latter question applies to a physical fleet, an LLM service business or a federation of independent operators. A single project can supply evidence to both inquiries. Each needs its own outcome and competing explanation. [Foundation and the earlier Q-learning benchmark](../theory/recursive_firm.md) · [Connected production research](https://github.com/amarmurray/robotics-economics/blob/4c39ae66b5e2d8014676dd493550e882ddc48e36/research/theory_integration_2026_11_17/data_value/QUALIFICATION_GATE_AND_DATA_VALUE.md)

## When does a better robot earn less for its fleet?

The [adapter repair study](transfer_validation/ADAPTER_REPAIR.md) prices a second annotation of a robot incident against the opportunity to train the shared digital policy. Across 256 held-out simulated fleets, a correction raised mobile capability by 12.9 percentage points while reducing fleet contribution. Buying a verified donor label beat fixed live sharing when several case families shared a correction and lost to it when the same number of faults were scattered. The next test is learning which cases belong together.

## When should a fleet validate a transfer link?

The [priced validation study](transfer_validation/README.md) compares selective and rotating audits, local heads and tuned fixed sharing across simultaneous model and demand changes. Redirecting the next correction into a disconnected local head added 23.84 contribution units in the ordinary drift simulation. Selective inspection earned only 0.96 more than a matched rotation, with an interval spanning zero. The strongest next comparison is learning a replacement adapter against staying local under unannounced drift.

## Fleet learning dynamics

A production policy changes which situations generate a labeled case. A learned transfer rule determines which downstream agents use it. The resulting competence changes both the next corpus and the work the fleet qualifies to take. This is the branch's primary question across autonomous digital agents and physical robot embodiments. Economic value is measured on complete work alongside fixed-panel capabilities, the diversity of usable evidence, and genuine operating and post-training costs.

The [fleet learning study](learning_dynamics/README.md) derives the scaling of error in deployment time when evidence arrives through exceptions. It reanalyzes 42 published robot scores and runs 96 paired digital and physical fleet worlds. A digital fix increased routing accuracy from 84.47% to 97.35% while slowing mobile learning by 8.69 percentage points under incident-only review. It also increased operating contribution in this comparison. An independent review sample largely removed the lost mobile improvement. A second mechanism shows how qualifying a new task opens its own source of data. An exact model prices the interval between revisions of the firm's learning objective against how stale validation will be. [Trajectory figure](learning_dynamics/learning_paths.svg) · [Fleet accounts](learning_dynamics/fleet_results.json) · [Scaling and independent benchmarks](learning_dynamics/scaling_results.json)

Our working distinction between **design** and **Hayekian emergence** concerns who picks the rule and what that actor knows. A designer can define enforceable messages and legitimate outcomes, while the prices and partnerships that people discover inside that institution are decentralized. Local discovery can in turn reveal a reason to change the institution. Owners with continuing authority to adopt that change constitute one possible firm boundary. Independent parties that achieve the same result through a contingent contract form a second, genuinely competitive explanation.

## How much of a teleoperation hour's buying power does the firm create?

A digital service and two installed robot embodiments share operator time and compute. The firm can buy hardware, seek permission to learn, or negotiate authority to act before the next order. With identical demand, a retrofit raises the first-hour value from 16.62 to 20.76 and changes its best source. A dedicated fixture then lowers that value to 16.47 while improving total contribution. A deployment at which no data are ultimately acquired can still reduce the price of the preferred license by 3.02. A separate nested learning environment compares training on the worst task with training for paid complete orders and with a tuned fixed schedule. [The buying power of a teleoperation hour](stack/README.md) · [Full-stack settlement results](stack/results.json) · [Held-out economic RL comparisons](stack/nested_results.json)

## Experiment 1. Why a successful supplier might stop looking for its next market

A supplier sells a specialist work period. Think of a teleoperator qualifying a robot at a packaging line or an expert reviewer qualifying a digital service for a new customer. Each accepted, productive use yields a gross 10 to the buyer and costs the supplier 3. A mature site can use the service in each of three periods. An untried site's underlying match is good with probability $p$. A first paid engagement reveals the match. A good site continues twice, an unsuccessful site exits. A customer knows what its own work is worth, and the supplier collects only agreed fees. The comparison holds resources and the opportunity set fixed within each cohort. Extra working capital supplies no mechanical benefit in this example.

Let $x$ be the first fee and $y$ the committed repeat fee, capped at 8 by assumption. The untried buyer enters when $p[10+2(10-y)]\ge x$. If a pilot is tried, its joint contribution over three dates is $J(p)=24p-3$. All fees are transfers between seller and buyer. At $p=1/4$ the first attempt loses 0.5 in expected current output but the whole opportunity is worth 3. Paid first attempts and nonparticipation are distinct observations.

**A larger installed base can eliminate experimentation.** With one price, the highest fee admitting the new customer is 5. Write $N$ for the number of mature three-period relationships per prospect. At 5, expected supplier contribution is $6N+3$. At 8, the prospect declines and supplier contribution is $15N$. These are the only candidates for the optimum over continuous uniform fees up to 8, since supplier proceeds rise with price between participation thresholds. The supplier drops profitable discovery when $N>1/3$. Without a mature customer the supplier funds entry. With one mature customer it prefers to protect the price on existing work. This is a mechanism through bargaining and incidence, despite identical physical transfer.

**An institution can change who pays for discovery.** For one unit of real cost per cohort the parties can verify genuine first use. A supplier can post $x=3.25,y=8$, and a new site can obtain the pilot terms once. This cost covers the cohort even if no offer is accepted, whenever the parties use different fees. At $p=1/4$ the prospective buyer earns 0.25, so adoption is a strict choice. The schedule respects the same incumbent price and increases supplier earnings. The following comparison has one mature site.

| Institution | Prospective site buys a trial | Supplier contribution | All buyers' surplus | Joint contribution |
| --- | --- | ---: | ---: | ---: |
| Supplier-optimal uniform fee of 8 | No | 15.00 | 6.00 | 21.00 |
| Uniform fee of 5, best uniform fee that admits a pilot | Yes, at indifference | 9.00 | 15.00 | 24.00 |
| Verified pilot fee of 3.25, repeat fee of 8 | Yes | 16.75 | 6.25 | 23.00 |

The low uniform price produces the highest joint surplus in this table. The verified schedule is a privately attractive route to some of that surplus. At these terms both sides can realize it through a contract. Ownership would require a further friction such as failure to commit to a renewal price, unverifiable identity or a dispute over the transferred skill. If a mature client can continually reclaim pilot status, the calculation must include cannibalization. The units are artificial and the contract does not represent an observed deployment.

**What actually emerged in the simulation.** A supplier uses an upper-confidence-bound bandit on its own settled cash flows. The buyer uses posterior sampling and sees outcomes only from purchased trials. It updates once per tested site, and learns no transfer outcome from a refusal. Both use private observations. The untagged institution permits one of four fees. A registry permits any of their 16 ordered pairs, including flat fees and expensive introductory fees. Nobody tells the agents which schedule to use. The ability to authenticate a first trial is supplied by the experimenter. The buyer's incumbent and post-qualification renewal decisions are solved analytically. This is economic learning in a repeated three-period institutional environment, not a deep RL training result.

Each of eight training runs sampled 12,000 independent cohorts. Policies were then frozen and scored on 3,000 fresh, matched cohorts per seed. The baseline grid excludes the continuous indifference price of 5.

| Training and evaluation condition | Frozen policy across eight runs | Pilot rate | Held-out mean joint contribution |
| --- | --- | ---: | ---: |
| Uniform fees, no mature site | All eight chose 4.50 | 100% | 3.018 |
| Uniform fees, one mature site | All eight chose 8 | 0% | 21.000 |
| Registry available, one mature site | Seven chose 3.25 then 8, one chose flat 8 | 87.5% | 22.708 |
| Same frozen registry policies, transfer falls from 25% to 5% unannounced | Same policies | 87.5% | 18.583 |

A known, well-designed contingent contract at 25% yields exactly 23 in expectation. The learned agents recovered it in seven seeds and fell short of that comparator on average. Freezing the rule under a change in transfer costs money. The fourth row evaluates persistence before adaptation at the new sites. Site-level outcomes and a separate record of refusals would be needed to take this claim to field data. Neither a positive return on a hand-designed menu nor the fact that local agents chose a discount establishes that they invented the institution. [Code](pilot_market.py) · [Results by seed](results.json)

## Experiment 2. How much inquiry can the firm authorize?

Under the incumbent-only fee of 8, two competing theories of transfer, $p=0.05$ and $p=0.25$, generate identical incumbent work, receipts and refusals. Their implications for a new site's economic value have opposite signs. A passive analyst can observe the incumbent ledger forever without separating those worlds. A research agent can instead pay for an independently qualified probe at an untried site.

Give the two theories equal prior probability. The downstream decision is whether to fund ten independent sites from that same population, scored at their risk-neutral **joint** value $10J(p)$. This is a different mandate from the seller's private cash in Experiment 1. A probe costs 0.2 and produces one independent success or failure conditional on the shared regime. The 0.2 is an assumed net cost of a diagnostic service, separate from the 3 cost of a productive engagement. It earns no separate production credit. After $s$ successes and $f$ failures let $\bar p$ denote the posterior predictive success rate. Stopping yields $\max(0,10[24\bar p-3])$. With $n$ probes left, the agent compares stopping with

$$
-0.2+\bar p V(s+1,f,n-1)+(1-\bar p)V(s,f+1,n-1).
$$

Exact fractional enumeration gives the following results before the agent sees any evidence.

| Research authority | Expected net value for ten future sites |
| --- | ---: |
| Act on existing evidence | 6.00000 |
| Approve each test only for what it can change by itself | 6.00000 |
| Commit in advance to the best fixed batch of up to three tests | 6.78825 |
| Authorize up to three, with discretion to stop | 6.87175 |

Even two failures leave $\bar p$ above the 1/8 investment cutoff. Any one or two tests can change beliefs while leaving the decision to fund the ten sites unchanged. Three failures cross the threshold. The optimal research agent probes until the first success or third failure. The three-test program with early stopping earns **0.87175** in additional expected value. Of that, **0.78825** is attainable by a fixed funded batch, and **0.08350** is attributable to the option to stop early.

**Candidate theoretical object.** For a given prior, feasible evidence and downstream action, define the *minimum experimental depth* as the smallest number of observations for which some positive-probability history changes the optimal downstream action. It is three here. With a positive test fee and no intermediate payoff, a manager requiring each isolated next test to pay for itself rejects a program with positive attainable value. A standing budget allowing the sequence can capture most of that value without a sophisticated agent. A stronger test asks which portfolios require delegated stopping, reallocation or hypothesis revision even against an optimized batch program. Correlated demonstrations, heterogeneous sites, an uncertain experimental technology and a longer cash horizon will change the result. [Exact decision program](evidence_budget.py) · [Independent checks](test_experiments.py)

## A ladder from acting to producing economic theories

| What the agent can change | Approach and evidence | Fair comparison |
| --- | --- | --- |
| An operating action | The original tabular Q agent chooses speed and reinvestment on paid orders | Enumerate both dates with the same rights and cash |
| What it learns and funds | Belief-state control chooses where to experiment or when to stop | Myopic experimentation, best fixed batch, and the exact dynamic program |
| The terms on which private parties coordinate | Local payoff learners choose prices, eligibility, consent and contracts | Optimized posted terms, non-learning traders and a planner paying information costs |
| The organization and the space of possible rules | Agents propose contracts in a bounded language, form coalitions, revise authority or exit | A designer with the same vocabulary, rights, latency, costs and opportunity to revise |
| Which economic explanation deserves capital | A proposer supplies rival generative models with matching historical implications. An experimenter chooses the cheapest decision-relevant intervention, and an independent evaluator scores preregistered predictions and later decisions | Equal research and compute budgets, counterexamples, alternative generators, new counterparties and held-out regimes |

The first three levels now have working examples. The fourth is the next experiment. The fifth has an exact experiment-selection example with two *given* hypotheses. Generating new hypotheses and refuting other agents' theories are open problems. Rule-based agents, auctions, dynamic programming, evolutionary populations, network formation, economic RL and language-model agents answer different questions. Compare mechanisms using the simplest agent that could produce the claimed behavior. The economic unit of scientific output is a credible change in what decision can profitably be made with the next dollar of research.

Hayek connects dispersed local knowledge to coordination through prices. Gode and Sunder show in double auctions that an institution can organize substantial gains even with minimally intelligent traders. Bolton and Harris analyze incentives for experimentation when others can learn. Bagnoli and Lipman treat collective provision through private contributions. These are priors and useful null models for the proposed market for research. The AI Economist supplies a two-level RL design precedent, while Melting Pot motivates withholding counterparties and social configurations during evaluation. The unidentified-transfer examples above are conditional constructions. Historical priority and external validity are open.

[Hayek](https://www.econlib.org/library/Essays/hykKnw.html) · [Gode and Sunder](https://doi.org/10.1086/261868) · [Bolton and Harris](https://doi.org/10.1111/1468-0262.00022) · [Bagnoli and Lipman](https://academic.oup.com/restud/article-abstract/56/4/583/1593696) · [The AI Economist](https://pmc.ncbi.nlm.nih.gov/articles/PMC9067926/) · [Melting Pot](https://proceedings.mlr.press/v139/leibo21a.html)

## Counterworld and reproduction

The [hosted runner](counterworld.mjs) implements a separate digital study of delegated pricing discretion. It builds a synthetic Shopify/Stripe commerce world and forks the same checkpoint into three arms. One holds promotion policy fixed at zero, one always offers a seven-day 10% promotion, and one authorizes it only with at most eight unfinished orders in the observed sample of up to 50 open orders. All arms read through the native scoped interface. After 30 simulated days the evaluator inspects gross margin, repeat purchase, refunds and invariants. The seven-day promotion and 30-day settlement horizon are independent of the three-date contracting example. On one checkpoint the conditional arm will coincide with one fixed arm. A credible comparison needs several registered seeds and both capacity regimes, priced intervention effort and comparable buyers.

A server-side project key is required. The local execution environment did not have one. Interface, cleanup and common-checkpoint tests pass against a fixture. The hosted SDK, catalog coverage of the chosen native mutation, invariants and business outcomes have yet to be verified in a live world. A rejected mutation or missing metric fails the run. Every disposable world is created by the harness. Scoped agent credentials never enter the economic report. [Counterworld quickstart](https://counterworld.dev/docs/quickstart.html) · [Evaluation](https://counterworld.dev/docs/evaluation.html) · [Native discount operation](https://shopify.dev/docs/api/admin-graphql/2026-01/mutations/discountAutomaticBasicCreate)

From this directory run the local experiment and its checks.

~~~sh
python pilot_market.py
python -m unittest -v test_experiments
node --test test_counterworld.mjs
~~~

With Node 20+, the installed Counterworld SDK and existing project credentials, a hosted run uses the following entry point. Supply one synthetic seed per run. Output records the checkpoint, policy actions, metrics and invariant status.

~~~sh
node counterworld.mjs roboecon-retention-01
~~~

**Opening research decision.** Start with agents that can propose, accept and copy conditional terms, then vary verification cost and whether either party can authorize a revision unilaterally. Compare the resulting organization against an equally informed external contract. Record who bears the cost of a failed experiment, who can end it, and whether the rule survives replacement of the agent who proposed it. Research depth, rule selection and persistent authority are separate outcomes.

**Earlier commercial extension.** Let customers choose among high-margin sealed and cheaper licensed deployments, and let competing deployers offer the service and its data terms. Give independent parties, a jointly empowered coalition and an integrated owner matched information, physical options and scope to respond when an unforeseen contingency arrives. Measure entry, who finances the useful experiment, the cost of amendment, the operator-hour bid and the complete orders the fleet can deliver.

**Earlier learning experiment brief.** Give the firm a scarce budget for testing transfer links when several digital and physical policies change. Allow it to commission an independent evaluation, open or close sharing, repair an action adapter, revisit an existing corpus or change its sampling allocation. Compare with strong fixed rules as well as separate task heads. Measure the downstream capability, the next stream of informative cases and the net value of changing the rule.
