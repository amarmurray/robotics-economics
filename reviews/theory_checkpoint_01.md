# Theory checkpoint 1 — scoped verification and self-challenge

Executed November 16 UTC / November 15 Eastern, 2026. Single writer; not independent review. Input accepted main: `654e4ff9dbc1e1eb945a8b2734eaf5e058c6fa9a`. The full Christmas brief arrived during reconciliation and replaced the initially missing attachment dependency. No blocker remains on useful theory work.

## Actual checks

- `python -m unittest tests.test_theory_deployment`: **7 tests pass**, covering exact credit boundary, reconciliation, investment threshold inside its declared regime, demand saturation/participation, rational-grid global quantity comparisons, ablations/failed expansion and selected source worked arithmetic.
- `python -m model.theory_deployment`: result generated; parsed output equals a fresh `build()` exactly. Rational economic results are serialized as fractions; source exponential arithmetic uses floating point and bounded rounding checks.
- `python scripts/build_report.py`: completed. Generated report is byte-identical to its previous content after removing the new current-phase banner. Historical chapter claims are not rewritten or presented as freshly verified.
- All **79 tracked prior files under `model/results/`** are byte-identical to the input commit. New theory output is additive. Prior empirical datasets and acceptance statuses are unchanged.
- New phase and research relative links resolve. Manifest entries and hashes are refreshed only for this checkpoint's accepted files, then all entries are checked before commit.

These checks are not a clean-checkout Christmas release replay, a broad legacy test rerun, equilibrium replication, or empirical validation. PDF extraction emitted font mismatch warnings; the inspected formulas were cross-checked against surrounding definitions and the worked numerical example. No claim relies on parsing an unread theorem proof.

## Material limits and adverse interpretation

**Prior art:** the finance-induced ranking reversal is standard constrained investment, and directed data accumulation already appears in Farboodi–Koh–Xia. These results begin the model audit; they do not establish an original contribution. Chen–Elliott–Koh remains an important uninspected seed.

**Objective distinction:** the source's productivity-maximizing firm size is not our customer's profit-maximizing output or a robot fleet optimum. Its replacement-stable equilibrium differs from our single-provider finite decision. We do not transfer its concentration conclusion into robotics.

**Financing:** the one-unit lender is a disclosed scenario, riskless and interest-free with feasible repayment. A lender's principal is not profit or a resource benefit. Customer intraperiod collections/cost reimbursement are assumed contemporaneous. Missing customer working capital, costly credit or unenforceable transfers could remove the example's implementation.

**Demand and technology:** linear inverse demand, deterministic known transitions, a fixed surplus share and no terminal obligations are restrictive. The customer outside option is explicit but zero in the illustration. Physical learning, rights and qualification are not estimated from papers. The binary expansion is neither a manufacturing-learning model nor an endogenous embodiment result.

**Empirics:** historical inspection, municipal contract and manipulation-learning records are distinct populations. They motivate discrimination and negative controls, not a joined site/provider panel or calibration. Public source mapping cannot identify a causal transfer effect without matched target evaluation and controls.

**Strongest next challenge:** can a minimal joint capability/qualification constraint combined with a distinct payment network yield a substantive result beyond existing capability accumulation and dynamic-finance models? Inspect the closest source first, then try to defeat that claim with a simpler model and competent alternative deployment.

## Reproduce this checkpoint

Use the repository's existing Python environment; this small kernel uses only the standard library. From repository root:

```sh
python -m unittest tests.test_theory_deployment
python -m model.theory_deployment
python scripts/build_report.py
```

The source cards specify public PDF URLs, inspected dates, relevant sections and SHA-256 fingerprints. Ignored local downloads are convenience copies. If a URL later serves a different hash, record the new version and compare before using it as the same source. No source PDF is republished in the repository.
