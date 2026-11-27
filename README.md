# Robotics Economics

When a robot completes a job, the customer receives the service, another site may be able to use the lesson, and a third party may have to pay to qualify the next deployment. Which job should a firm take first when those parties differ? A second question arises when rivals can see what the robot has qualified to do. [Production, learning and payment networks](papers/learning_and_capital/README.md)

## Two propositions for the paper

**Where the saving lands.** A one-unit saving on operator commissioning can unlock a second site. An equal saving on supplier adaptation leaves the operator one unit short. An advance closes that gap in the original model. In a second case, human fallback can fill the same order and only the operator can validate the controller on the target fixture. An advance funds the test, yet the operator can keep the money and skip it. An auditable target test makes a performance payment possible. [Funding proof](research/theory/qualification_finance.md) · [Directed learning threshold](research/theory/learning_funding_alignment.md) · [Contracting comparison](research/theory/qualification_observability.md)

**Who sees qualification.** In a two-price tender, public qualification cuts the firm's profit from 12 to 10 when the rival lowers its quote. If the outcome and procedure are both private, a higher chance of qualifying pays. A credibly disclosed procedure can still change bids. With the same demand and continuous quantity choices, qualifying raises profit. The funded integrated quantity game also gives no strict loss across matched procedures under either published selector. The paper's strict reversal is a bid-pricing result. [Payoffs and quantity check](research/theory/qualification_observability.md) · [Funded action quotient](papers/integrated_firm/FUNDED_EMBODIED.md) · [Milestones](research/theory/milestones.md)

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
