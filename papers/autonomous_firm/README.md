# Autonomous Firm Theory

How should a firm allocate a teleoperator hour, a robot, or a compute slot when delivering work today changes what its fleet can learn tomorrow?

| Paper | Read on GitHub | PDF edition |
| --- | --- | --- |
| **Choosing the First Deployment** · November 22, 2026 · 17 pages | [Allocation, site selection, learning, and competition](Choosing_the_First_Deployment.md) | [Download](Choosing_the_First_Deployment.pdf) |
| **The Autonomous Firm** · November 20, 2026 · 15 pages | [The opportunity cost of learning across digital agents, physical fleets, and human operators](The_Autonomous_Firm.md) | [Download](The_Autonomous_Firm.pdf) |

A useful starting point is the [timing example](Choosing_the_First_Deployment.md#when-the-timing-of-scarcity-changes-the-answer). Keeping average compute load and the chance of a useful demonstration fixed, changing which jobs coincide with a trace reverses the value of collecting it. The [linked procurement example](Choosing_the_First_Deployment.md#when-the-weaker-learner-wins-the-site) asks how that valuation changes when a rival can learn from winning. The papers distinguish conditional model results, motivating observations, and tests that could reject the proposed mechanisms. The numerical examples use illustrative parameters.

## Replication

From the repository root, with Python 3.10 or newer:

```sh
python -m pip install -r papers/autonomous_firm/replication/requirements.txt
python papers/autonomous_firm/replication/run.py
```

The runner checks the two papers and regenerates the figures. The first paper’s six model checks can also run with the Python standard library alone.

| Material | Location |
| --- | --- |
| First paper’s calculations and recorded output | [Six model checks](replication/README.md) · [Reference output](replication/reference_output.txt) · [Original downloadable replication package](Autonomous_Firm_Replication.zip) |
| First deployment and learning over repeated orders | [Site and price choice](replication/deployment/first_site.py) · [Learning dynamics](replication/deployment/learning_state.py) · [Independent policy enumeration](replication/deployment/check_stationary_policy.py) |
| Conditional allocation and competitive effects | [Allocation and two linked auctions](replication/deployment/allocation_and_bids.py) · [Adoption, capacity, and market shares](replication/deployment/competition.py) |

## Related research

[When Capabilities Become Production](https://github.com/amarmurray/robotics-economics/blob/research/assistant-led-expansion-20261117/research/theory_integration_2026_11_17/data_value/WHEN_CAPABILITIES_COMPACT_DRAFT.md) develops the production and qualification argument. [Recursive Firm Theory](https://github.com/amarmurray/robotics-economics/blob/research/recursive-firm-theory/research/recursive_firm/README.md) develops the organization and learning experiments. The links follow the respective working branches. [Dated PDF editions](../README.md) provide a fixed reading copy.

[Original typesetting sources and PDF rebuild instructions](replication/Typesetting_sources.zip)
