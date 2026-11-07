# Funded share acquisition and separate growth

[This extension](entry_transitions.py) runs on the unchanged monthly physical, commercial, enterprise, finance and calendar bridge. It uses the bridge's explicit synthetic cleaning-zone contract. The [fifteen saved worlds](results/entry_transitions.json) compare status quo, organic build, share acquisition and hybrid entry. No company is bought, no third party is contacted, and no real transaction terms are inferred.

## What transfers

The supported acquisition is a 100% beneficial equity transfer in the existing incumbent operating company. Before closing its recorded owner is `selling_owner`; after a successful closing it is `platform_buyer`. Its legal actor/account stays `incumbent`. Customer assignments, unique physical unit IDs, leases, title, custody, workflow authority, receivables and liabilities stay with their existing legal counterparties. In the reference the lessor continues to own the robots. The separate ultimate-owner register must not be mistaken for robot title or a grant of model/data rights.

Closing requires an explicit assumed-consent/operating-rights premise and actual buyer funds. Consideration goes to the selling owner. It does not arrive in the target's operating account. Separate target equity, if specified, requires a separate settled payment from buyer to company. No target-cash sweep, dividend, target-funded purchase, asset novation, debt forgiveness or share liquidation is modeled. Share price and terminal value are assumptions/unknowns, respectively; this is not a valuation, legal or tax analysis.

## Dated funding and atomic closing

At the declared month before closing (month zero if closing is zero), the buyer incurs a diligence bill to a distinct resource supplier. The committed bill remains even if closing fails. Each due collection uses actual available buyer cash. In the closing month's phase 1, conditional invoices are issued for share consideration, transition resources and optional target working equity; phase 2 follows actual operating receipts and scheduled growth equity.

The three conditional payments are evaluated on an immutable candidate Treasury. All must settle before any candidate payment or ownership change is accepted. Otherwise the candidate is discarded and the conditional invoices are cancelled. Prior paid diligence and its unpaid obligation remain. The failed closing is not silently rescheduled. A one-cent boundary is tested against the full group, including the target-equity leg. A funded closing never implies that all the target's operating obligations can subsequently be paid.

A declared whole-target interruption begins only after successful closing. During its explicit months the target cannot provide service; its paid fixed obligations continue and its physical units remain. No customer reassignment, free fallback or restoration of already missed service occurs. Interruption is a synthetic sensitivity, not an estimated acquisition effect.

## Build and hybrid

All four routes start with the same $200,000 in the buyer account. The target has a separate $25,000 reference opening balance and two existing leased robots. Technology, annual digital/capability levels, support/integration budgets and supplier terms are common; the former floor-bundle case is not converted or added to this market.

Build and hybrid commit $60,000 of buyer equity to a separate entrant company at month zero and request two new robots through the existing funded manufacture, shipping, integration and support process. Building captures 70 units of existing baseline business and assigns 100 unmet plus 50 already specified new recurring zones in month three. Hybrid leaves the target's 500 baseline zones assigned to the target and assigns only those 150 growth zones to the entrant. The market remains 650 zones per month; acquisition adds no demand or robot stock.

The hybrid growth leg is separately committed and may continue even when the share acquisition fails. This is an explicit contract choice, not an assertion that a real buyer should proceed. No integration synergy, automatic headcount change or automatic transfer of idle parent cash is assumed. Alternative prompt/delayed incumbent customer-return attempts use the same technology access and actual acquisition-resource charges; their timing is a fixed policy, not an optimized competitive equilibrium.

## Accounting and replay boundary

The existing enterprise perimeter reports its actual operating sales, paid costs and received equity. A second, fixed wider perimeter includes buyer, seller and all robot-commercial/operating parties. Share consideration and internal equity cancel inside this wider boundary; externally paid operating and transaction bills remain. The seller's cash receipt is not new physical output. A deliberately supplied opening target payable stays owed by the target; its settlement is reported separately from current-period resource creation. All actors conserve cash and every month's demand assignment conserves the same market inventory.

The wider cash change reconciles to actual end-market collections plus external equity/net financing minus external operating and transaction cash. It is not accounting profit. Uncollected sales, existing/future obligations, assets, unpaid claims and unknown terminal share value remain visible. The reference adds no new term loan; inherited outside-lender facilities can be replayed, while parent/seller loans and unrelated opening invoice contracts are rejected rather than silently misclassified.

`python3 scripts/export_entry_transitions.py --check` verifies deterministic exports. `--case downloaded.json --output replay.json` restores complete opening Treasury, physical plan, contracts, enterprise, finance, bridge and transition inputs and recomputes all outcomes. Saved owners, cash totals and hashes are ignored. Integral JSON numbers are canonicalized and rational numerator/denominator strings preserve exact browser replay. The API `/api/entry-transitions` accepts exactly shortcut `inputs` or a complete `saved_case`. Customer adoption shows terms, operating versus buyer cash, ultimate ownership, unchanged leases, obligations, controls and export/import.
