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

## Dated physical manufacturing and rival response

[Embodied competitive game](EMBODIED_GAME.md) · [Code](embodied_game.js) · [Results](embodied_game_results.json). Reproduce: `node embodied_game.js > embodied_game_results.json`. Concurrent embodied competitive game: paid kits, delayed assembly, installed arm/mobile, local qualified recipes, cash, ordinary learning and successor menu in one exact dated two-market account. 32/32 matched cases; inherited-procedure manufacturing increases accepted jobs 7.5→10 and customer surplus 10.5→20 while combined terminal wealth falls 58→56 (higher-total pure selection); cheaper kits induce actual order→assembly→service and change rival research; matched cap-2 null. Positive active-rival cap-2, endogenous retention/scope, longer horizons and general mixed solver open.


## Four-date funded embodied game

[Proof and results](FUNDED_EMBODIED.md) · [Solver](funded_embodied.js) · [Results](funded_embodied_results.json). Run `node funded_embodied.js`. Four-date embodied cap-0/1/2 from zero solved under guaranteed funding and two pure selections via a cash-independent continuation quotient; all six yield wealth (160.5,159), 12.5 accepted jobs and customer surplus 22.5, with ordinary training and actual mobile-kit orders/assembly but no successor attempts. Binding-cash cap-2 diagnostic stopped at 300,001 profiles (33,480 solved states), not an equilibrium nonexistence result. Positive active-rival cap-2, larger recipient sets, rights/scope and binding finance remain open.

## November 26: terminal economic irrelevance and solved four-date cohort game

Four-date from-zero three-recipient embodied cap-0/1/2 now all solved under both continuation selections: wealth (166,166) or (166,164), no successor attempts in any case. Terminal projection and funded penultimate successor dominance reduce cap-2 from 6,689,725 to 3,239,595 profiles and 17,538 to 3,754 memo states; unprojected higher-budget solve matches exact selected wealth and successor counts. Five-date batch exceeded execution limit; positive active-rival second-generation return, endogenous retention/scope and longer binding finance remain open.

[Proof, exact results and falsifiers](COHORT_SCALE.md) · [Reproduction](cohort_scale.js) · [Results](cohort_scale_results.json). The projection is conditional on the selected terminal game and funding bound; binding penultimate actions remain intact. No learned-policy, empirical calibration or universal superiority claim.

## November 26: evidence rights and endogenous lab scope

Endogenous archive retention, paid outside training/data and dated lab entry/exit now enter the same three-recipient competitive technology. 24/24 primary pure-game cases and 12 projection-off comparisons solved. With an inherited procedure 2, installed mobile and costly outside research, retention rights induce one ordinary-service archive→internal physical qualification→extra accepted job: combined wealth 347→348, jobs 12→13, customer surplus 18→21. At cheap outside research or binding B=9, rights add zero selected private value. With inherited physical archives, open rather than closed initial lab scope raises wealth 349→362 and jobs 13→16; without enough useful opportunity the lab exits. This is a matched rights/scope comparison, not an endogenous second-generation acquisition result. Three-date positive cases fix hardware, while two-date cash/scope cases allow assembly.

[Derivation, exact competitive results and falsifiers](COHORT_RIGHTS.md). The terminal projection preserves inherited scope when it changes the current bill, and the funded penultimate closure result is conditional on cash-independent payoff selection. No empirical or general-equilibrium claim.
