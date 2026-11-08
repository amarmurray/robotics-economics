# Compatible components and discrete replacements

Edition 0.31 is a bounded synthetic component contract on the existing physical, commercial, calendar, annual-resource and competition loop. It preserves the generic monthly contract for earlier cases. It does not convert an abstract module or an annual average spare rate into a real component.

## Explicit replacement of the generic inventory

`TypedComponentSystem` requires zero generic components per start and per service booking. Its plan must have zero generic opening inventory and receipts. An explicit `ComponentInventory` must accompany it. Generic `System` retains its original positive manufacturing-component guard and requires no typed ledger. Complete imports reconstruct the declared system class; a typed case cannot run without its material contract.

Old generic result fields remain structurally unchanged in old cases. In typed cases, the zero generic balance is explicitly marked inactive, and `compatible_parts` carries the actual stock ledger. These are alternative accounting contracts, not two additive supplies or expenses.

The synthetic annual catalog supplies compatible manufacturing requirements: 24 `actuator_h` units for SYN-H, or 12 `actuator_q` units for SYN-Q, plus the hypothetical compatible onboard-board requirement. The selected cleaning bridge uses SYN-H. Standard configuration requires one board; the existing high-memory assumption requires two. These identifiers are not vendor products, tested hardware equivalence or a real bill of materials. A Q actuator cannot satisfy an H requirement.

Every funded whole-unit start issues the complete vector. Partial stock cannot create a fractional robot. Rejection later retains the consumed parts and bundled manufacturing payment. No salvage, part return or refund is inferred. The existing synthetic manufacturing price is held fixed to isolate availability; it does not identify the incremental price or performance of an extra board.

## Delivery and qualification are distinct states

Each identified receipt records its pool, whole quantity, announcement month, physical receipt month and qualification month. A null receipt or qualification remains unrealized. Announcements add no inventory. Physical arrivals enter quarantine in phase 4; only an explicitly dated qualification release makes them usable. Qualification cannot precede receipt, and receipt cannot precede the recorded announcement.

For each compatible pool and month:

```
qualified_close = qualified_open + qualification_release - manufacturing_issue - replacement_issue
quarantine_close = quarantine_open + actual_receipt - qualification_release
```

All terms are exact nonnegative integers. Qualified opening stock is explicitly assumed already usable; its historical funding is outside the window. Receipt timing is declared independently of the annual model's aggregate supply path. The annual six-cell supply and outside allocations are not imported or jointly executed.

Existing service remains phase 3. A phase-4 arrival or release cannot retroactively enable that booking. Available parts needed by unsupported installed units are protected, and the existing strict installed-service priority still blocks new commissioning, shipping and manufacture when an installed unit is unsupported. Later qualification does not automatically retry a missed manufacturing order; a later start must be explicitly scheduled.

## Maintenance, paid admission and resource conservation

The bounded maintenance contract allows one named replacement requirement per physical unit: due month and compatible whole-part vector. The vector must fit the system/configuration. The unit ID must belong to opening stock or an explicitly scheduled start. If manufacture never occurs, the requirement remains conditional on an uncreated unit; rejected stock does not acquire operating service. A delayed requirement remains due until successfully fulfilled. It is not consumed before its date or repeatedly as an average spare rate.

Ordinary paid support remains necessary even when no replacement is due. Replacement labor is explicitly assumed within that support booking and its existing hour allocation. This is not an empirical repair-time claim. Separate target labor, repair pricing, hazards, technician availability and qualification evidence remain unknown.

Part availability is checked before the existing contingent payment group. Only a fully admitted booking issues parts and completes the requirement. A failed support, software, upgrade or manufacturing payment leaves candidate parts unconsumed. Annual support/integration ceilings continue to apply; an annual refusal cannot consume a replacement or advance its completion date. This is serial simulation atomicity, not a claim about production databases or real robot transactions.

The existing cash perimeter is retained: components are consigned/supplier-funded until issue, and their consumed cost is included once in the paid manufacturing or support bundle. This tranche adds no supplier payment, debt, new account or duplicate part expense. It does not establish that a real supplier would extend such financing or that the quoted bundle covers these requirements.

## Replay and interface

```sh
python3 scripts/export_component_execution.py
python3 scripts/export_component_execution.py --check
python3 scripts/export_component_execution.py --case saved-components.json --output replay.json
python3 -m unittest tests.test_component_inventory tests.test_component_execution -v
node --check dashboard/component_execution.js
```

[component_execution.json](results/component_execution.json) contains eight full executions. The Customer adoption and Supply & production panels share the same selected case. Controls edit pools, quantities, receipt/qualification dates, opening qualified inventory, replacements, manufacturing timing and provider cash. Blank receipt/qualification dates preserve unrealized states. Pending, invalid and obsolete requests retain the last applied display/export. Full import ignores saved output totals and reconstructs complete inputs. Ordinary annual cell controls remain separate.

`GET /api/component-execution` supplies the catalog and control; `POST` accepts exactly one `inputs` or `saved_case`. Five metric-lineage entries, dated part and physical events, unit states, annual resources and closing Treasury are inspectable/exportable. See [decision findings](../research/component_execution.md) and [self-review](../reviews/component_execution_review.md).
