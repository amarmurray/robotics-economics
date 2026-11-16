# Internal capital markets: the prior-art objection is substantive

Jeremy C. Stein, *Internal Capital Markets and the Competition for Corporate Resources*, **Journal of Finance 52(1), March 1997, pp. 111–133**, DOI [10.1111/j.1540-6261.1997.tb03810.x](https://doi.org/10.1111/j.1540-6261.1997.tb03810.x). Bibliographic identity checked against the [author's publication page](https://stein.scholars.harvard.edu/publications/internal-capital-markets-and-competition-corporate-resources) and journal discovery entry. The journal webpage's later online-hosting date is not the article's publication year.

[Author-hosted published PDF](https://stein.scholars.harvard.edu/sites/g/files/omnuum5951/files/stein/files/internal-capital-markets-jf-march-97.pdf), retrieved November 16 UTC, 2026. SHA-256 `c2d7f3c4ab055db7f1c8a91ccde0506c471213b197f717e7ab9235de1e2ecbf4`. The PDF is scanned; text extraction alone returned no substantive text. Pages 114–118 were visually inspected from rendered pages, with OCR used as a reading aid. The reconstruction below is limited to the standalone-project rationing comparison and headquarters' stated authority/incentive assumptions; it does not replicate the complete multiproject or optimal-scope results.

## Mechanism card

**Question.** Can reallocating a fixed amount of scarce corporate finance create value, and when does assigning control to headquarters help or hurt?

**Primitives, agents and information.** A founder owns a project idea but has neither wealth nor managerial ability; a professional manager and outside financiers are needed. A project can receive investment one or two. In bad state B its verifiable cash returns are y1 and y2, with `1<y1<y2<2`; in good state G they are theta*y1 and theta*y2, where theta>1 and `theta*(y2-y1)>1`. The manager observes the state; the founder and financiers do not. Managers obtain unverifiable private benefits proportional to project cash flow, motivating overoptimistic reports. The required return on finance and the manager's reservation wage are normalized to zero.

**Objective and restriction.** The founder maximizes expected proceeds net of financier/manager payments. Without an effective revelation scheme, investment cannot depend on the state. The paper explains that inducing truthful revelation is costly and focuses subsequently on cases where private benefits make such schemes unattractive. This is an agency/information origin for rationing, not our assumption of known project payoffs and an exogenous transfer cap.

## Reconstructing the rationing comparison

Let p be the good-state probability and `Delta=y2-y1`. Expected net cash at investment n is `(1+p*(theta-1))*y_n-n`. Increasing investment from one to two changes expected net cash by

`(1+p*(theta-1))*Delta-1`.

Thus, conditional on the no-revelation restriction, one unit is preferred iff

`p < [1/Delta-1]/(theta-1)`,

with a tie at equality. The assumptions `Delta<1<theta*Delta` put this threshold strictly between zero and one. This derives the comparison underlying §I.B, pp. 115–116; it is not a new financing theorem. Knowing the state would instead allocate one in B and two in G. The underinvestment in G is therefore an information/agency problem, not a lack of productive opportunity.

## Headquarters adds authority and an incentive cost

At pp. 117–118, headquarters has monitoring skills, no own financial resources, control rights that let it capture a share of private benefits, and authority to redistribute resources across projects. Assigning those rights dilutes managers' effort incentives; the model represents this with a factor k<1 on project cash flows. Headquarters can allocate two units to some projects and zero to others rather than spreading one to each. Its authority to exclude project managers from seeking independent financing is central to the contrast with a nonowner intermediary.

Consequently the source already motivates value from reallocating scarce funds **without an increase in total financing**. Our checkpoint-2 aggregate-cash counterexample cannot be claimed as a new general insight. Conversely, our costless separate-firm transfer agreement is not a refutation of Stein's model: it assumes away the very authority, exclusivity and incentive restrictions that his ownership comparison studies.

## Implication for the robotics claim

The robotics extension must specify what experience changes—qualification cost, eligibility, uncertainty, or bargaining/commitment—and how that change interacts with the actual payer. The [directed-experience extension](learning_funding_alignment.md) isolates cost reductions at particular obligations. It remains a conditional application of the funding-cut result, with no new agency solution or claim of novelty.

Next literature need: distinguish exogenous payment permission from endogenous control/commitment and audit related internal-capital-market distortions before drawing an organizational conclusion. No interview or external outreach is needed to perform this theoretical audit.
