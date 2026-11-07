# Funded monthly intelligence architectures

Edition 0.16 adds [monthly_architectures.py](monthly_architectures.py) as a policy on the existing calendar, physical, commercial, enterprise, financing and Treasury loop. It resolves the existing [architecture catalog](architecture_assumptions.json) into dated obligations and actual legal accounts. Twelve source/catalog hashes identify execution. The earlier annual architecture comparison, monthly worlds and assumptions remain unchanged.

The four labels are alternative synthetic contracts, not qualified products or estimates for named firms. Every profile separately assumes configuration compatibility, rights availability and service quality. A false gate blocks robot support, starts and shipment; the paid human alternative remains visible. It does not turn a missing rights record into a license opinion.

## Matched service and scope

One active cleaning-service business delivers the same recurring 500 accepted zones per month over July 2026–February 2027. The existing two-business engine retains an explicitly inactive second business with no robots or customer assignments. There is no new demand, demand capture or inferred conversion from the historical floor bundle. Zone quantities retain the inherited rational expected-output approximation; this is not a discrete request/deadline simulator or observed service count. The new comparison is separate from the earlier two-business calendar worlds.

Two opening installed robots and two requested new robots form the standard physical plan. Opening hardware predates the cash window. Manufacturing expense applies only to actual new starts; hardware payment occurs only on actual shipment. The one declared start date is month zero. An unsuccessful start is not automatically rescheduled. Each architecture must qualify its opening hardware as well as new units before operating it under this contract. Previously integrated opening hardware does not incur a second physical integration charge.

The existing fixed staffing commitment is $4,000 per month, plus its existing overhead, materials and site software. The operator pays it even when robots release all of its service task hours. No paid shift is removed and no avoided-baseline-cost credit enters cash. Actual service bills and paid resource invoices are the only operating cash flows. Opening assets, unused stock, unsettled receivables and different qualification paths make a short-window outlay table unsuitable as a lifetime ranking.

## Roles, capital and ownership

The five logical roles are customer, operator, OEM, model supplier and integrator. The existing catalog specifies their legal-entity grouping:

| Profile | Grouping in this execution |
| --- | --- |
| Integrated OEM | Customer/operator together; OEM/model supplier/integrator together |
| Independent licensed policy | Customer/operator together; separate OEM, model supplier and integrator |
| Open adaptation | Customer/operator/model supplier together; separate OEM and integrator |
| Model-led operating provider | Customer separate; operator/model supplier/integrator together; separate OEM |

Each role receives a declared opening capital allocation. Standard allocations are $200,000 customer, $100,000 operator, $200,000 OEM, $50,000 model supplier and $50,000 integrator: $600,000 total. Allocations are **summed**, never replicated, when roles share one account. These amounts are arbitrary scenario inputs. Equal aggregate capital does not imply that an independent actor can use another actor's cash. No automatic rescue, cash pooling or new financial claim is invented.

The operator buys and owns new hardware from the independent OEM. Physical custody and workflow authority follow that operator after commissioning. The market business's customer account receives actual end-market sale receipts. In the model-led case the separate operator pays staff, overhead, materials and site software, and bills the customer the explicit contract rate per **total accepted zone**, including its paid human fallback. The standard rate is $6 per zone, due one month after delivery. Internal customer/operator service bills are eliminated. This rate replaces the separate annual reference's hypothetical baseline-cost fraction; that fraction and its bilateral surplus hurdles are not used or editable here.

## Resources and transfers counted once

Per successful first unit admission, the profile charges demonstration collection, adaptation engineering and compute, qualification/validation resources, allocated model development and any explicit customer-path setup. These source quantities came from a one-robot annual reference. Applying them **per actual unit** is an explicit constructed contract, not evidence that adaptation scales linearly or cannot be shared. Allocated model-development cash is a scenario expense at qualification, not a reconstruction of a model lab's actual training spend.

The customer pays dedicated demonstration/setup resources; the model supplier pays adaptation, compute, allocated development, inference and maintenance; the integrator pays qualification/validation and physical commissioning; the operator pays ongoing physical operation, network resilience, staffing and site software. The demonstration and engineering work are explicitly additional resource purchases, separate from the fixed service staff's hours. Shared adaptation economies and reassignment of paid employees require another declared contract.

Physical integration hours equal the annual reference hours times the selected profile's multiplier. Intervention minutes include the profile's declared support delta. These effective parameters are validated against the saved reference mapping, not independently editable after the profile is applied. A label alone has no performance multiplier. The same annual operation and cohort/ramp functions determine output.

The opaque robot digital-service bundle is replaced by itemized inference, maintenance and network bills. Inference uses the admitted software vintage's annual digital price times the profile multiplier, divided by twelve. Maintenance, network and model license fees use one twelfth of their annual amounts per supported robot-month. Site software and changed-version qualification retain the earlier calendar contract. They are separately traced and never added a second time to consolidated outlay.

Model fees and upfront model payments transfer money from operator to model supplier. An integration/validation price transfers their declared resource cost plus the catalog markup from operator to integrator. For a new commission, the integrator also prepays that month's physical support; an equal operator-to-integrator passthrough funds it. All these fees cancel within the complete role perimeter. When payer and payee are the same entity, no self-payment, invoice or cash posting is created. The nominal quoted amount remains visible as an eliminated internal transfer; quotes for blocked admissions are not realized savings or receipts.

## Admission, time and resources

Initial adaptation and validation share a declared monthly engineering pool; dedicated demonstrations have their own pool. These are additional specified resources alongside the existing physical integration and support/upgrade pools. They are not silently allocated from the same annual pool twice. Standard capacities are 400 engineering hours and 100 demonstration hours each month. Actual work is consumed only by successful qualification. The default open profile needs 300 engineering hours per unit; two opening units therefore need 600 hours.

For each supported or commissioned unit, the policy evaluates qualification gates, resource capacity, operator fee payments, physical booking and model/resource bills on an immutable Treasury candidate. Successful fee receipts may fund the corresponding supplier resource purchase within this explicitly atomic booking. If any obligation cannot settle, the whole contingent group is canceled: no partial fee receipt, resource purchase, qualification, software vintage or resource-hour consumption survives. Previously paid fixed staffing/site costs and completed hardware shipment remain real. This cooperative atomic-booking assumption requires a real contractual/transaction mechanism before implementation; it is not a claim about ordinary supplier payment terms.

Existing installed support has priority over expansion under the inherited physical policy. A month-zero support shortfall can cancel the declared month-zero start. More engineering capacity may therefore enable later physical stock without changing manufacturing productivity. Separately, a funded hardware purchase does not pay for the subsequent qualification of that asset.

Customer-to-operator service invoices are earned after observed delivery, with the declared collection lag. They are mandatory obligations, not cancellable qualification quotes. Unpaid due operating obligations suspend service under the existing readiness rule; receivables beyond the horizon remain claims. Standard architecture cases use no loans. The inherited finance path remains available for its supported borrower roles, but this tranche does not solve optimal financing for every new role, restructuring or insolvency.

## Reproduction and interface

```bash
python3 scripts/export_monthly_architectures.py
python3 scripts/export_monthly_architectures.py --check
python3 scripts/export_monthly_architectures.py --case saved-case.json --output /tmp/architecture-replay.json
python3 -m unittest tests.test_monthly_architectures -v
```

The ten worlds cover the four profiles, a higher external fee, an unfunded model supplier, scarce/additional engineering, a capital reallocation with unchanged total funds, and a false rights premise. Fully resolved profile/reference/capital inputs, actual opening Treasury, physical plan and complete contracts are saved. Replay recomputes from inputs and ignores saved outcomes. Rational components retain the lossless decimal-string format; unsafe non-rational integers fail. Equivalent integral JSON spellings such as `3` and `3.0` are canonicalized before hashing, so browser export preserves the case identity. Historical reproduction requires the matching source checkout.

The **Business models** view exposes witness selection, role capital, model/service fees, qualification capacity, rights premises, legal-account balances, source/obligation traces and complete export/reload. Invalid or stale requests preserve the last valid result. Imported complete cases are read-only in the shortcut controls until a witness is selected. `GET /api/monthly-architectures` returns the bundle; `POST` accepts exactly one `inputs` or `saved_case` object. The earlier annual architecture controls retain their separate lifetime scope.

The bridge is bounded to one synthetic service business. It does not establish real whole-system costs, rights, qualification, model/data premiums, a preferred architecture, the strongest conventional scheduling alternative, endogenous learning or acquisition/hybrid economics. See [findings](../research/monthly_intelligence_execution.md) and [sole-writer review](../reviews/monthly_architectures_review.md).
