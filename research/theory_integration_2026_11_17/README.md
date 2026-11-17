# When Capabilities Become Production

An integrated theoretical investigation for Amar's Robotics Economics program, November 17, 2026. The central manuscript links production-network qualification, learning investment, and customer value rather than introducing another isolated numerical model.

Read `THEORY_MANUSCRIPT.md` (or its rendered PDF), then `RESEARCH_PROGRAM.md`. `STUDY_GUIDE.md` and `SOLUTIONS.md` separate exercises from answers. `CLAIMS_AND_SOURCES.md` distinguishes proofs, computational checks, prior art and empirical unknowns.

## Reproduce

The core uses Python, NumPy and SciPy; no training, GPU, robot, private customer data, or paid API is required. Tested environment is recorded in `VALIDATION.json`.

```sh
python -m pip install -r requirements.txt
python -m unittest -v test_theory
python theory.py --output results.json
```

The first command requires an environment where package installation is permitted; the completed run used preinstalled dependencies. Exact rational checks and floating-point LP/ODE checks have different scopes. No global historical repository test suite or independent peer review is claimed.

To render the manuscript, use Pandoc and XeLaTeX with an installed Unicode font:

```sh
pandoc THEORY_MANUSCRIPT.md --from=markdown+tex_math_single_backslash \
  --pdf-engine=xelatex -V documentclass=article -V fontsize=11pt \
  -V geometry:margin=0.9in -V mainfont='DejaVu Serif' \
  -V colorlinks=false -H header.tex -o When_Capabilities_Become_Production.pdf
```

The distributed PDF additionally starts its bibliography on a new page. Font files are not included. Source papers are referenced, not redistributed.

## Scope and status

Conditional theory and synthetic checks; not calibrated deployment economics or a claim of publication novelty. The source boundary is accepted service and a competent alternative, not raw robot motion. All monetary/capacity examples are normalized and hypothetical. The adaptive homogeneous-chain policy is solved; the general dynamic multi-payer production-network problem is not claimed solved.

The complete pre-refocus Q1–Q13 queue is preserved in the repository at `research/theory_integration_2026_11_17/PREVIOUS_RESEARCH_STATE.json`. The December 25, 2026 deadline and all broader roadmap topics remain active.
