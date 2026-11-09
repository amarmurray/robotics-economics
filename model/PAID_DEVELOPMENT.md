# Paid development before service admission

The CPU-only fixture extends one architecture/crew/actual-award history. It does not train a model, simulate a robot acceptance trial or calibrate a learning rate. `model/paid_development.py` replaces the existing first-successful-admission convention for initial work while leaving the old architecture model and its saved numerical results intact.

## Work, identity and sequence

One declared architecture/onboard configuration and at most one manufactured target robot are permitted. Each dated review has a unique attempt ID, physical unit ID, fresh evidence ID and explicit synthetic pass/fail premise. Collection permission and evidence-use rights are separate assumptions. Review requires the robot to have arrived for commissioning; it cannot run on absent hardware or another configuration. No work is performed after a pass, without rights, outside a dated slot or without full funding/capacity. Unperformed attempts are not silently retried.

A month opens with issued prospective invoices. Mandatory payroll/debt settles before review. The phase-3 review books dedicated specialist engineering and demonstration hours in a declared pre-service window; these are the same finite architecture pools used by the old initial qualification contract. They are distinct from site crews, annual provider support and physical commissioning. This coarse calendar does not resolve detailed robot motion, wear, trial parts or a full external laboratory. Review evidence is neither customer service nor training output.

Fees and resource payments must fund atomically. Same-entity fees are eliminated; other transfers remain explicit. If cash or capacity is insufficient, the group is cancelled, no fee receipt remains and no work or hours are recorded. If the work completes and its declared outcome fails, its actual resource payments and hours remain. A declared pass permits a later commissioning attempt; it supplies no parts, support entitlement, physical capacity or service outcome by itself.

## Once-only and repeated costs

The first completed review pays customer-path setup, allocated model development and the model upfront fee once per physical unit. Every completed review pays fresh demonstration, adaptation engineering, adaptation compute, qualification engineering/resources and the declared validation fee. Repeated review is explicitly a full rework premise, not an estimated iterative learning curve. Physical integration and its markup remain payable separately at commissioning. Ordinary inference, maintenance, network resources and service fees retain their existing timing.

The former initial costs and validation payment are replaced, never added again at successful admission. Paid failed work and paid successful work survive later provider-support or physical-admission failure. External resources are already included once in the existing all-payer resource/transaction cash. Fees are transfers, not additional resources. Stopping does not refund earlier work or purchased hardware. The legal title register, retained site crew, inventory duties, customer awards and every account remain the same execution.

## Comparisons and scope

Six complete cases compare first pass, paid failure followed by a pass, stopping after paid failure, unavailable evidence rights, a human-only policy and a passed review awaiting next-year support. All retain the same cleaning and inventory obligations. The human-only policy has no robot purchase or development; it is a competent alternative, not an assertion that all physical tasks admit direct human substitution.

The saved continue-versus-stop comparison first verifies identical opening contracts and realized physical/cash histories through month 2. It then sums actual external-resource settlement events from month 3 onward by legal payer, alongside staffing, accepted zones, inventory jobs and terminal robot state. Earlier costs and internal fees are excluded. A differing past or the unmatched human-only case is rejected.

A single first pass reproduces the old successful case's total cash and service. Failed work and delayed service can change both cash and staffing-notice timing. This does not identify an optimal stopping rule, current commercial product, observed cost or economic return. Terminal hardware, claims and beyond-window staffing commitments remain. Commercial alternative qualification, shared adaptation, configuration/version changes, asset recovery and a true endogenous learning process remain separate gaps. The automotive learning fixture uses incompatible service/time/data units and is not summed into this history.

## Reproduction

Run `python3 scripts/export_paid_development.py`, then `python3 scripts/export_paid_development.py --check`. Replay a complete saved case with `--case FILE --output FILE`. `python3 -m unittest tests.test_paid_development tests.test_architecture_awards -v` covers the new mechanism and the directly affected formatter. The dashboard's Customer and Commercial views add this comparison to the existing paid-crew selector. Funding, engineering, support, crew and rights controls recompute through `/api/paid-development`; pending or rejected edits preserve the last applied export. Imports recompute complete opening contracts and ignore saved derived outcomes.
