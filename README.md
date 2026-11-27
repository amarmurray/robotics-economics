# Robotics Economics

When a robot completes a job, the customer receives the service, another site may be able to use the lesson, and a third party may have to pay to qualify the next deployment. Which job should a firm take first when those parties differ? A second question arises when rivals can see what the robot has qualified to do. [Production, learning and payment networks](papers/learning_and_capital/README.md)

## Two propositions for the paper

**Where the saving lands.** Every group of payers must cover its share of a site's qualification bills from available cash and permitted incoming payments. In the two-payer proof, a one-unit saving on operator commissioning unlocks service. The same saving on supplier adaptation leaves the operator one unit short. An enforceable one-unit prepayment erases the difference. The proposed paper uses this condition to rank first deployments by where their validated learning can be used. [Funding and deployment-order proof](research/theory/qualification_finance.md) · [Directed learning threshold](research/theory/learning_funding_alignment.md)

**Who sees qualification.** With a fixed rival action, a firm can ignore a newly qualified recipe and use the old one. A public certificate can also change what the rival offers. The funded solver can prune a more expensive recipe with identical quantities and successor law. A change in success probability falls outside that argument. The proposed test prices the same service before and after the rival responds to certified capacity. [Optional-capability theorem](papers/integrated_firm/PROPOSITIONS.md) · [Action quotient](papers/integrated_firm/FUNDED_EMBODIED.md) · [Proposed milestones](research/theory/milestones.md)

## Preparing inputs for an automotive fixture

Both sides of the saved `prepared_vs_human` comparison deliver the same 12 kits by their original deadlines and pay all due bills. Liebherr’s Dingolfing account documents fixed, vision-guided handling with intermediate buffering. It supplies a reason to include a capable fixed alternative. The preparation requirement, 12-kit obligation, locally qualified configurations ($K,M$) and dollars are inputs to the illustrative replay. [Source audit](research/automotive_workcell_decision.md) · [Replay contract](model/WORKCELL_COMPARISON.md)

| Formal quantity | Human | Prepared fixed cell | Interpretation |
| --- | ---: | ---: | --- |
| Accepted service $y$, kits | 12 | 12 | The same parts and deadlines constrain both recipes |
| Station / upstream preparation in $A^Y y$, person-seconds | 360 / 0 | 60 / 360 | Separate resource requirements for the same service |
| Outlays charged to customer cash $B$ | $572 | $908 | Both include the same $500 station-staff commitment |

The cell uses 60 more modeled person-seconds overall. Its extra $336 comprises $200 for station resources and $136 for preparation. In the two-period model, a customer choosing the fixture needs at least $336 of additional net cash value it can capture after omitted costs. If only the station invoice can change, it must fall to $164 or less while still funding timely service. Reuse rights, target qualification probability and supplier margins remain unknown. Six incomplete comparisons receive no economic bound. [Matched bounds](research/workcell_cash_decision.md) · [Formal state and dated cash account](papers/integrated_firm/UNIFIED_MODEL.md) · [Acceptance audit](ACCEPTANCE_AUDIT.md)

## What the exact games establish

At initial cash 120, the four-date, from-zero comparison yields the same wealth and zero successor attempts across procedure caps 0, 1 and 2. The cash-16 run stopped at profile 300,001 without a solved equilibrium. In the separate 8-, 9- and 10-shift comparisons, early use of qualification at committed quantities leaves all six selected initial outcomes intact and changes some off-path play. [Funded comparison](papers/integrated_firm/FUNDED_EMBODIED.md) · [Event clock](papers/integrated_firm/EVENT_RELEASE.md) · [Claim ledger](papers/integrated_firm/CLAIM_LEDGER.md) · [Referee report](reviews/integrated_firm_referee.md)

## Papers, evidence and replication

The wider program follows hardware and model suppliers, fleet operators and customers across end markets. [When Capabilities Become Production](https://github.com/amarmurray/robotics-economics/blob/research/assistant-led-expansion-20261117/research/theory_integration_2026_11_17/data_value/WHEN_CAPABILITIES_COMPACT_DRAFT.md) · [The Autonomous Firm](papers/autonomous_firm/The_Autonomous_Firm.md) · [Choosing the First Deployment](papers/autonomous_firm/Choosing_the_First_Deployment.md) · [When Faster Learning Pays](papers/autonomous_firm/When_Faster_Learning_Pays.md) · [Recursive Firm Theory](https://github.com/amarmurray/robotics-economics/blob/research/recursive-firm-theory/research/recursive_firm/README.md) · [The Production of Capability](papers/autonomous_firm/The_Production_of_Capability.md)

[Working papers and replication code](papers/README.md) · [Integrated research report](REPORT.md) · [Research design](RESEARCH_PROGRAM_DESIGN.md) · [Reproduction guide](REPRODUCE.md) · [Theory-week proposition register](papers/theory_week_20261125/PROPOSITION_REGISTER.md)

From the repository root, run `python3 scripts/serve.py` to explore the local dashboard at `http://127.0.0.1:8765`.
