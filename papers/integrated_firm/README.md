# Formal integration of the robotic and recursive firm

The main result is a solved finite firm in which accepted service, digital/human execution, retained evidence, learning, procedure development, hardware and internal scope compete for one dated resource and cash account. A recipient-cohort restriction solves two generations of procedure improvement with the payoff derived from the same production technology. A two-firm restriction solves product-market competition and first-period research under disclosed continuation-equilibrium selections.

## Read the economic argument

1. [UNIFIED_MODEL.md](UNIFIED_MODEL.md): common primitives, timing, production, learning, digital stocks/flows, cash, value and the source-to-core crosswalk.
2. [RESULTS.md](RESULTS.md): computed decisions and comparisons, with initial cash and equipment salvage separated from newly generated cash.
3. [SUCCESSOR_PROCEDURES.md](SUCCESSOR_PROCEDURES.md): derived recipient value, exact research recursion, target scope and deadlines.
4. [PROPOSITIONS.md](PROPOSITIONS.md): ten statements with proofs and boundaries.
5. [CLAIM_LEDGER.md](CLAIM_LEDGER.md): the seven obligations, completed evidence and unresolved closure.
6. [NEXT_QUESTION.md](NEXT_QUESTION.md): the next cumulative integration problem.

The unit examples are synthetic. The model is not empirically calibrated, and no actual LLM or robot controller is trained by this package. Its ordinary comparator can plan contingently, use old qualified policies, learn from production and buy external research. Organizational labels alone confer no advantage.

## Reproduce

Use Python 3.12 or another compatible Python 3 installation. All code uses the standard library; no paid compute, external data download or package installation is needed. Run from this directory:

~~~bash
python run.py --suite standard
~~~

This reconstructs:

- integrated_results.json: concurrent firm comparisons.
- verification_results.json: independent hidden-regime replay, cost/accounting and observation-channel checks.
- competition_results.json: all reported pure root equilibria under two terminal tie-breaks.
- cohort_results.json: policy enumeration for staged successor procedures.
- cohort_verification.json: independent rational-arithmetic reconstruction.
- marginal_results.json: typed physical-output and private-value finite changes.

The complete suite can take several minutes on a CPU. For the analytical cohort restriction alone:

~~~bash
python run.py --suite cohorts
~~~

Individual entry points are [core.py](core.py), [verify.py](verify.py), [competition.py](competition.py), [cohorts.py](cohorts.py), [verify_cohorts.py](verify_cohorts.py) and [margins.py](margins.py). No randomness is sampled in the published results: finite outcomes are enumerated. The concurrent and competitive programs use floating-point expectations and explicit tolerances; the cohort checker also supplies exact rational values.

The terminal and short-horizon dominance reductions are conditional on the declared technology: models/data/procedures have no terminal salvage, construction costs exceed equipment salvage, and research occupies one period before its result is usable. Competitive root actions retain the full menu because spending can change a later strategic capacity constraint. Identical next-state distributions are collapsed using strict state/probability equality.

## Scientific boundary

This edition solves a concurrent finite firm and two precisely stated extensions. It has not solved many-generation strategic learning with endogenous entry, suppliers, private information and changing representations. General Bellman notation does not establish that larger solution. Positive procedure investment in the prefunded, independent-market cohort restriction is not yet a result for that broader economy.

The common state and resource account provide the integration architecture. The open task is to restore the restrictions removed in the cohort solution and carry the competitive response through enough generations for successor procedures to matter. The current [state](state.json) and [integration contract](INTEGRATION_CONTRACT.md) preserve the existing theory-week and Christmas research obligations.

