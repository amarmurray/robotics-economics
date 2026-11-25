# Robotics Economics

Robotics Economics studies how physical robots and autonomous digital agents change the organization of production. When does a technical capability become work a customer will accept and pay for? How does doing that work change what a firm can learn, produce and invest in next?

[Working papers and replication code](papers/README.md) · [Integrated research report](REPORT.md)

## Research scope

The program compares human, assisted and autonomous work across industries such as manufacturing and infrastructure inspection. It follows the value chain from hardware and model suppliers through fleet operators to the firms adopting the technology. The comparisons span industrial arms, mobile robots, humanoids, quadrupeds and drones, as well as LLM-based agents that deliver digital services or coordinate physical fleets.

Consider a teleoperator who recovers a failed pick. That hour can finish an order and generate a demonstration. Its value to the rest of the fleet depends on who may retain the record, which robots can learn from it and whether the correction can be validated in time. The fleet operator may pay for the recovery while a model provider earns the return from training on it.

## Papers and studies

- **Production and adoption.** Which combinations of robot capability, human support and shared capacity turn a better task score into more completed orders? [When Capabilities Become Production](https://github.com/amarmurray/robotics-economics/blob/research/assistant-led-expansion-20261117/research/theory_integration_2026_11_17/data_value/WHEN_CAPABILITIES_COMPACT_DRAFT.md)
- **Allocation and competition.** How should a firm allocate scarce labor, machines and compute across sites when winning a deployment changes what it or a rival can learn? [The Autonomous Firm](papers/autonomous_firm/The_Autonomous_Firm.md) · [Choosing the First Deployment](papers/autonomous_firm/Choosing_the_First_Deployment.md) · [When Faster Learning Pays](papers/autonomous_firm/When_Faster_Learning_Pays.md)
- **Organizational learning.** A better routing agent can prevent the failures that supplied a robot's training data. When should the firm revise its rules for sampling cases, sharing corrections across embodiments and authorizing the next release? [Recursive Firm Theory](https://github.com/amarmurray/robotics-economics/blob/research/recursive-firm-theory/research/recursive_firm/README.md)

## Evidence and replication

The empirical work draws on labor statistics, deployment case studies and published evaluations of robots and digital agents. The economic models and agent-based simulations use stated assumptions about demand, costs and learning to trace their effects on paid output and investment returns. [Research design](RESEARCH_PROGRAM_DESIGN.md) · [Reproduction guide](REPRODUCE.md)

From the repository root, run `python3 scripts/serve.py` to explore the local dashboard at `http://127.0.0.1:8765`.
