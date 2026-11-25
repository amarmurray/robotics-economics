# RoboEcon papers and replications

The links to research branches open the current manuscripts, code and numerical results. The PDFs below preserve the dated reading editions.

## Learning and capital in robotic production

What makes one deployment induce another, possibly at a different firm or in a different industry? The common model links the production decisions in *When Capabilities Become Production* to the choices over learning and reinvestment in *Recursive Firm Theory*. It derives the response of robot-capital productivity as the fleet adjusts and a condition under which two markets can sustain additional adoption together. [Working paper](learning_and_capital/README.md) · [PDF](learning_and_capital/Learning_and_Capital_in_Robotic_Production.pdf) · [Replication](learning_and_capital/replication.py)

From the repository root, run `python3 papers/learning_and_capital/replication.py` with NumPy installed.

[How deployment changes the productivity of robot capital](How_Deployment_Changes_Robot_Productivity.md) develops the premises of the two working papers through parcel handling and power inspection. It includes proposed openings, a model of the marginal product of robot hours, and tests of execution, learning and authority.

## Recursive Firm Theory

How does a firm change what it will learn from its next deployment? The research follows a digital agent and physical fleets through incident selection, training allocation, transfer and the release decision. [Live research index](https://github.com/amarmurray/robotics-economics/blob/research/recursive-firm-theory/research/recursive_firm/README.md)

| Reading edition | Question |
| --- | --- |
| [Recursive Firm Theory](recursive_firm/Recursive_Firm_Theory.pdf) · Nov 20 | How can a firm invest in the way it produces, learns and delegates future decisions? |
| [Intervention as a Production Input](recursive_firm/Intervention_Economics_Research_Note.pdf) · Nov 22 | How do simultaneous requests, operator attention and recovery time affect the cost of intervention? |

The [learning dynamics study](https://github.com/amarmurray/robotics-economics/blob/research/recursive-firm-theory/research/recursive_firm/learning_dynamics/README.md) connects deployment exposure to useful evidence. Subsequent experiments cover [priced transfer validation](https://github.com/amarmurray/robotics-economics/blob/research/recursive-firm-theory/research/recursive_firm/transfer_validation/README.md), [repairing a shared policy](https://github.com/amarmurray/robotics-economics/blob/research/recursive-firm-theory/research/recursive_firm/transfer_validation/ADAPTER_REPAIR.md), [learning which corrections generalize](https://github.com/amarmurray/robotics-economics/blob/research/recursive-firm-theory/research/recursive_firm/partition_discovery/README.md) and [learning from paid orders](https://github.com/amarmurray/robotics-economics/blob/research/recursive-firm-theory/research/recursive_firm/settlement_learning/README.md).

## The Autonomous Firm

| Reading edition | Question |
| --- | --- |
| [The full-stack robotic firm](autonomous_firm/FULL_STACK_FIRM.md) · [PDF](autonomous_firm/The_Full_Stack_Robotic_Firm.pdf) · Nov 25 | How does a firm choose its next customer, model update and hardware generation when each changes what the fleet can learn? |
| [When Faster Learning Pays](autonomous_firm/When_Faster_Learning_Pays.md) · [PDF](autonomous_firm/When_Faster_Learning_Pays.pdf) · Nov 25 | How much is a temporary learning lead worth, and how does a rival’s response change its return? |
| [The Production of Capability](autonomous_firm/The_Production_of_Capability.md) · [PDF](autonomous_firm/The_Production_of_Capability.pdf) · Nov 25 | How does paid work teach a fleet what to try next, and how does the obligation to support existing sites change which discoveries it pursues? |
| [Deployment portfolios and the next robot](autonomous_firm/DEPLOYMENT_PORTFOLIOS_AND_DESIGN.md) · Nov 25 | How can one deployment make another's data useful, changing the next hardware design and manufacturing quantity? |
| [The Autonomous Firm](autonomous_firm/The_Autonomous_Firm.pdf) · Nov 20 | How do shared capacity and deadlines change the opportunity cost of learning across machines and people? |
| [Choosing the First Deployment](autonomous_firm/Choosing_the_First_Deployment.md) · [PDF](autonomous_firm/Choosing_the_First_Deployment.pdf) · Nov 22 | Which feasible use of capacity should the firm choose when today's work changes tomorrow's alternatives? |

Run `python run_all.py` from the replication directory to reproduce the six numerical modules. [Browse the source and reference output](autonomous_firm/replication/README.md) · [Download the original package](autonomous_firm/Autonomous_Firm_Replication.zip)

[Both manuscripts in Markdown, the deployment and competition checks, figures, and original typesetting sources](autonomous_firm/README.md)

## When Capabilities Become Production

How do qualification, demand and dated capacity determine which technical gains become accepted output? [Current compact paper](https://github.com/amarmurray/robotics-economics/blob/research/assistant-led-expansion-20261117/research/theory_integration_2026_11_17/data_value/WHEN_CAPABILITIES_COMPACT_DRAFT.md) · [Broader manuscript and supporting work](https://github.com/amarmurray/robotics-economics/blob/research/assistant-led-expansion-20261117/research/theory_integration_2026_11_17/THEORY_MANUSCRIPT.md)

| Reading edition | Subject |
| --- | --- |
| [When Capabilities Become Production](production/When_Capabilities_Become_Production.pdf) · Nov 17 | The earlier integrated argument on qualification networks and learning complementarities. |
| [Teleoperation and Economic Data Value](production/Teleoperation_and_Economic_Data_Value_2026-11-17.pdf) · Nov 17 | How information acquired during service can change the firm's next investment. |

The November 17 replication outputs include [deployment expansion](production/results_2026_11_17/deployment_expansion_results.json), [qualification](production/results_2026_11_17/qualification_results.json) and their [joint calculation](production/results_2026_11_17/bridge_results.json). [Expansion source](https://github.com/amarmurray/robotics-economics/blob/0bde43c00cceda1fcb258c51468955c94d4834e8/research/takeover_2026_11_17/expansion.py) · [Qualification and bridge source](https://github.com/amarmurray/robotics-economics/tree/bee49a9d66bf09f5bee50692f7cb44c17147e029/research/qualification_bridge_2026_11_17)

## Program briefs

The original November 15 brief and its expanded Christmas edition document the research questions and milestones at the start of the theory phase. [Original brief](program_briefs/Codex_Robotics_Economics_Theory_Research_Brief.md) · [Through-Christmas edition](program_briefs/Codex_Robotics_Economics_Theory_Research_Brief_Through_Christmas_2026.md)
