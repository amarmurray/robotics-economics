# Conditional model-layer architecture economics

Model 0.3.0 adds `model.engine.run_architecture_comparison`. It uses the existing `matched_economics` equations for accepted service, human fallback, robot operating work, configured hardware, manufacturing yield and process integration. `model/architectures.py` adds an explicit cost and transfer ledger. API, exports, dashboard and report use this same calculation. No company benchmark score, revenue figure or observed license label supplies a numerical coefficient.

## Scope and qualification

One selected market-stage cell and year define the reference. The default export uses manufacturing material presentation in 2030, with the existing synthetic annual workload. A supported configured robot and sufficient human fallback complete the same accepted service. Current-year human efficiency, capability, coordination and reference inference expense are held over the assumed robot life. This is not forward-looking valuation under the entire annual path, an installed-fleet allocation, a company treasury or a claim that any named vendor qualifies.

Each profile separately assumes compatible configuration, available rights and adequate service quality. A false premise produces no economic ranking or cost point for that architecture. These assumptions do not resolve the actual compatibility, price or rights gaps retained in the source packet. Human fallback availability is assumed; labor rationing and a newco's possible capacity advantage are not modeled here.

The asset contract is an outright purchase by the logical operator. In the first three default structures that operator is the customer; in the model-led case it is a separate provider. The legacy sale/lease/RaaS selector continues to govern the separate lifetime reference tables. This extension does not add a financier or claim leased and purchased capital are equivalent.

## Four structures, with explicit rather than label-based differences

| Structure | Default legal-entity grouping | What can change the result |
| --- | --- | --- |
| Integrated OEM | OEM, model supplier and integrator combined; customer and operator combined | Declared adaptation, validation, integration, inference and support inputs; hardware/model/integration payments remain distinct logical flows |
| Independent licensed model | Separate OEM, model supplier and integrator; customer operates the site | Model payment, adaptation and serving costs, interface/validation expense and intervention burden |
| Open adaptation | Customer/operator also performs the model-supplier role; separate OEM and integrator | Internal engineering, training, maintenance, rights and qualification work remain costs; an internal model payment creates no surplus |
| Model-led operating provider | Operator, model supplier and integrator combined; external customer and OEM | Provider-owned asset, residual human work, support and service payment; internal model charges cancel |

The input catalog is [architecture_assumptions.json](architecture_assumptions.json). It includes complete units and four explicitly invented profiles. It is not a price sheet for Pi, Skild, Figure or OpenVLA. Role consolidation alone does not change the work, cost or consolidated gain. The default profiles also differ in declared resource assumptions; every such difference is visible and editable through the API or saved-input replay.

Incumbent and newco labels have no productivity multiplier. The same architecture is evaluated for both with identical technology and service assumptions. Only the separately specified incumbent or newco setup charge changes this comparison. The existing monthly entrant model's timing, customer acquisition, demand and funding remain separate.

## Resource costs, transfers and cash interpretation

One-time charges include accepted-robot manufacturing, physical process integration, task demonstration collection, model-adaptation engineering/compute, qualification/validation, an allocated model-development charge and any explicit customer-path setup. Annual charges include remaining human work and site software, required robot operation and support, network-resilience infrastructure, inference resources and model maintenance/support. These work categories are declared disjoint: network infrastructure excludes human recovery labor, and model adaptation is separate from the process-integration hours already priced by the common engine.

The inherited scalar robot digital-service bundle is removed from the physical operating-cost call. Its current `digital_cost_usd` level becomes the reference inference-resource expense, multiplied by each profile's explicit assumption. Additional model fees are transfers, not a second charge for the same resource. Hardware purchase price and integration payments are also transfers inside the chosen five-role boundary; manufacturing and integration resource expenditure are counted once with the party bearing them.

The allocated model-development input is charged at period zero for the constructed full-cost case. Its timing is an analytical assumption, not a reconstruction of a lab's historical training expenditure or marginal cost. Outside supplier bills and labor inputs are valued at declared amounts; this is not a decomposition of every upstream supplier's rents or a national welfare estimate.

All transfers are recorded by logical role, then combined by legal entity. Transfers within one entity are eliminated. Scheduled money is integer cents; derived line items round once with half-up rounding. Annual equivalents divide complete lifetime amounts without intermediate rounding. Resource cost uses the upfront charges spread over service life plus annual costs; the cash schedule charges upfront amounts once at period zero and does not subtract capital consumption again.

Let `B` be the digital-human baseline cost and `H` the remaining human/service-software cost from the common engine. The hypothetical value of displaced human work is `D = B − H`. With labor-avoidability assumption `a`, unavoidable payroll cash is `U = D × (1 − a)`. `U` stays with the customer and reduces cash benefit, while the resource comparison retains the labor-opportunity boundary. Observed payroll removal remains unknown.

The customer receives an avoided-baseline-cost **credit** in the incremental comparison, not an actual revenue receipt. For life `L`:

```text
sum of entity lifetime incremental amounts
  = L × baseline-cost credit − all allocated case expenses

resource benefit − allocated cash benefit
  = unavoidable released-payroll cash
```

No opening cash balance, credit facility, default, customer cancellation, tax, discount rate, within-year working capital or terminal value is simulated. Positive annual-equivalent amounts do not establish liquidity or financing. Contracts are assumed to continue through the full service life. These boundaries preserve the remaining need for a monthly commercial/physical model.

## Conditional fee intervals

For an external annual payment `F`, the recipient's lifetime amount rises by `L × F`, while the payer's falls by the same amount. Other payments and resource assumptions stay fixed. The interval's lower bound covers the recipient's declared annual-equivalent surplus requirement; the upper bound preserves the payer's. Bounds are rounded inward to admissible integer-cent prices: ceiling for the minimum and floor for the maximum. A nonnegative fee interval exists only when the upper bound is at least the lower bound.

The result separately reports whether other counterparties have nonnegative amounts under the fixed payments. A bilateral interval cannot repair an OEM loss caused by an assumed underpriced hardware sale. For combined entities there is no external model/service fee to solve for; the result states that the internal transfer was eliminated. The default surplus requirements are zero and do not represent an investor's actual return hurdle.

## Reproduction and interface

```bash
python3 scripts/export_architectures.py --experiments-output model/results/architecture_experiments.json
python3 scripts/export_architectures.py --scenario saved-architecture.json --output replay.json
```

The first command exports a complete reference comparison and eight separate witnesses. They test fees, adaptation, support, setup costs, an unadmitted configuration, leaner open adaptation and a stronger digital-human alternative. Counterfactual outputs are not added as simultaneously feasible production.

In **Business models**, choose cell/year, edit the architecture inputs and select **Apply architecture assumptions**. Results and exports retain the last applied inputs while edits are pending. The all-cell filter uses an explicitly labeled manufacturing reference rather than adding unlike services. **Export architecture comparison** preserves full effective parameters, source hashes and cell/year scope; reload restores them. The ordinary scenario export also preserves architecture parameters. Invalid combinations, including effective physical inputs outside the shared engine's bounds, fail visibly rather than being clipped or replaced by zero.

Model, resolver and architecture-helper source hashes, both assumption catalogs, effective inputs and selected scope identify the calculation. Legacy scalar inputs acquire explicit default architecture parameters under the new version; their prior numerical fields remain unchanged, while historical hashes require their original checkout. [The implementation audit](../reviews/architecture_economics_review.md) records the exact checks and their limits.
