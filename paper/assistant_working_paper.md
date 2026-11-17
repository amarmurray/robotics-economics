# Deploying to Learn, Learning to Deploy
## Capital Allocation and the Expansion of Robotic Production

Working manuscript segment, 17 November 2026. This is an early argument and analytical section, not a complete draft, selected novel contribution or submitted paper. Core model sources: `research/takeover_2026_11_17/RESEARCH_NOTE.md` and `research/qualification_bridge_2026_11_17/RESEARCH_NOTE.md`. Preserve the wider theory program and historical source reconstructions.

### Provisional abstract

Robotic deployments can generate current cash, transferable capability and access to future customers, but these outputs are neither equivalent nor necessarily aligned. We study a provider choosing between deepening an existing activity and qualifying a different configuration. Customer demand determines the surplus available from service, adaptation translates a multidimensional capability profile into a qualification cost, and a finite budget makes investments compete. In a tractable benchmark, a higher average capability score can require more spending to meet the same service criterion because its remaining weakness is more expensive to improve. Joining that cost to an exact portfolio problem can reverse current-cash deployment rankings. The reversal disappears under weak destination demand, scarce finance or sufficiently high verification cost. These are conditional analytical and computational results; public technical evaluations motivate measurements but do not calibrate industrial costs. The prospective contribution remains subject to comparison with existing investment and reliability-allocation theory.

### 1. The economic problem

The economically relevant question is not simply which robot is most capable. An enterprise must choose which combination of systems, workflows and customers to develop with finite resources. One deployment can produce cash with little useful experience for its next application. Another can create a profile of capabilities that is inexpensive to adapt, yet have weak immediate economics. Manufacturing investment may make repeated configurations less costly, while an embodiment change may alter the work the enterprise can perform at all.

These decisions belong to overlapping networks. A material production link connects one activity's output to another's input. A learning link connects source experience to a target configuration's performance. A payment link determines who can finance the next investment. They need not coincide. The working paper studies a focused choice inside this larger system rather than claiming to solve its entire equilibrium.

Our current benchmark holds most contracting and strategic competition fixed. It first derives customer output and capturable operating surplus, then values the feasible investment menu. The role of theory is to identify which relationship can reverse a choice and what observation would distinguish that mechanism. A synthetic reversal is a diagnostic, not by itself evidence of novelty or a strategy for an actual company.

### 2. Customer value and the alternative use of capital

Let a customer maximize revenue minus full service resources, subject to qualified capacity. Under the maintained quadratic revenue and two-part tariff, its chosen quantity responds to capacity and demand. Provider profit is a declared share of incremental surplus over the best feasible alternative; customer value and provider receipts are not interchangeable. Gross downstream revenue is not attributed wholesale to the robot.

Write H(B) for the provider's best incremental value from investment in its established application with cash B. For a new application requiring cost I(y,e), let J(y,e) be its standalone net value at scale y after source experience e. Entry dominates staying with the established activity precisely when some feasible y satisfies

    J(y,e) > H(B)-H(B-I(y,e)).

The right side is the value of displaced incumbent investment. This standard opportunity-cost comparison clarifies why positive standalone returns do not suffice. It also explains why additional capital can deepen existing operations before broadening the set of markets served when investment is indivisible.

### 3. From performance to adaptation expenditure

A scalar data stock cannot reveal which service requirement remains difficult. Let a candidate configuration have failure-event probabilities f_r(x)=l_r+a_r exp(-alpha_r x_r) after adaptation effort x_r. Minimize adaptation expenditure subject to sum f_r<=epsilon. This is a conservative whole-service rule under a union bound; its assumptions are explicitly different from an empirical certification protocol.

Transforming to reducible failures delta_r gives the convex program in the accompanying note. Its optimum has delta_r=min(a_r,(w_r/alpha_r)/lambda). The multiplier prices a tighter service requirement. Componentwise learning lowers cost when it improves the feasible profile, but a mean score cannot rank two crossing profiles: the cost vector and service requirements matter.

The synthetic example demonstrates the distinction. Initial mean component success is .939 for one profile and .935 for another. Yet adaptation costs are approximately 15.18 and 11.86, respectively, because the first profile's remaining weakness is expensive to improve. A separate verification bill remains in both cases. None of these probabilities, costs or response parameters is fitted from a published benchmark.

### 4. Joining the mechanisms

The empirical object we ultimately need is cost to meet a fixed, complete target service after alternative sources of experience. The model maps that object into the investment menu rather than adding an arbitrary strategic bonus to data. Using the preserved customer-demand kernel, the lower-current-cash source produces greater optimized portfolio value in the base example. Destination demand, available cash and verification cost each supply a counterexample to the unrestricted recommendation to prioritize learning.

The current computation assumes that qualifying a unit delivers the capacity defined by the kernel, and omits qualification duration and uncertain trial outcomes. These assumptions now determine the next extension: compare more learning on the existing embodiment with an embodiment change that alters an irreducible limitation, while customer demand evolves during development. This should be a small time-to-build model with terminal assets and obligations, not a general simulator before its economic mechanism is clear.

### 5. Measurement and evidence

The current evidence atlas separates reported technical comparisons, hypothetical task-to-market mappings and unknown economic coefficients. Its source locators cover Open X-Embodiment and Lin et al.'s data-scaling paper; the qualification note records exactly what was inspected. Those evaluations do not establish a customer profitability curve, qualification expenditure or commercial availability. The atlas therefore identifies what must be measured rather than inventing numbers to complete the model.

A discriminating design holds target service, configuration, evaluation distribution and acceptance standard fixed, varies source experience, and records complete adaptation and verification effort. It then joins those observations to customer output, incumbent alternatives, actual prices, payment timing and retained human work. Rejected and failed trials matter as much as successful demonstrations. Cross-market task similarity is a candidate transfer edge, not an observed coefficient.

### 6. Contribution discipline and remaining work

The allocation solution, union bound and investment comparison use established mathematical ideas. The candidate contribution must arise from a consequential production/learning/investment relationship and a credible measurement implication, not from relabeling known methods with robotics language. Existing financing-identification and contracting results remain useful but should not displace constructive expansion analysis.

Before a complete first draft, the work must settle the main claim, compare relevant prior art, test alternative response curves and contracts, incorporate development time, and build an actual sector/workflow backbone. The broader program retains competence versus coordination, manufacturing economics, organizational boundaries, demand feedback and alternative embodiments even when the first paper omits some of them.
