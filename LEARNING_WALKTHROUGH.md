# First guided walkthrough: from evidence to a deployment decision

This is an entry point for Amar's comprehension and critical review, following [the accepted staging plan](POST_RESEARCH_STAGING.md). It can begin now with the verified early edition; the continuing research campaign and its gaps remain open. Use a weekend session if convenient, or split the exercises across shorter sessions. There is no required calendar delay.

Start with [the concise continuation findings](CONTINUATION_FINDINGS.md), then launch the dashboard using [REPRODUCE.md](REPRODUCE.md). Keep [the thesis register](THESIS_REGISTER.md) and [model methods](model/METHODS.md) nearby. The aim is to explain a decision and its uncertainty in your own words, not memorize company names or model outputs.

## 1. Define the opportunity before counting robots

Open **Economic atlas**. Compare manufacturing, hospital logistics and utility inspection. For each, name the buyer, operating organization, value-chain stage and accepted service. Then identify the strongest current alternative: a person, digital-improved process, specialized machine or another embodiment.

Explain why the national employment figure, the selected occupation groups and the six constructed model cells are different populations. The occupation view overlaps the industry view; it cannot be added to it. Physical-work hours remain unknown. The model's sites are synthetic and are excluded from observed totals.

Write a three-sentence answer for one cell:

1. The customer needs this accepted outcome, under this quality and timing standard.
2. The relevant alternatives and retained human tasks are these.
3. These missing observations prevent a defensible market-size or ROI conclusion.

**Check your understanding:** a humanoid can successfully move a tote, yet the economically relevant service may still fail at the handoff, deadline, exception or customer-contract boundary. Explain a specific example without calling the whole job automated.

## 2. Trace capability into supported output

Open **Market deployment** and **Fleet & bottlenecks**. Begin with the saved reference scenario, then compare delayed supply and service stress in **Scenarios & evidence**. Inspect the full time path and cumulative baseline-equivalent hours as well as final active stock.

The delayed-supply example can end with more active robots while producing less cumulative output because later cohorts have not yet retired. Explain that result using commissioning, retirement and exposure. It is a constructed counterexample to terminal-stock ranking, not evidence that real supply delays help deployment.

Now reduce shared support capacity and inspect commissioning, active stock, supported fraction and output. The control recalculates the entire scenario history: it can reduce admissions and commissioning rather than remove support from a previously fixed installed fleet. A time-specific support shock is not implemented. Distinguish installed capacity from supported work without assuming this slider isolates that shock. Then restore the reference and set the cash-avoidability assumption to zero. Explain why released labor time and removed payroll lead to different economic eligibility.

Use this accounting identity to check the physical story:

`closing active stock = opening active stock + commissions − retirements`

A replacement consumes production and commissioning resources without necessarily increasing net stock. A faster robot cannot silently work at a site where it has not been installed. These are population constraints, not opinions about technological progress.

**Check your understanding:** choose the next scarce resource you would investigate before ordering more hardware. State the observation that could overturn your choice.

## 3. Move the human comparator too

Open **Analogies & contributions** and inspect the four-way cost comparison: human baseline, additional digital improvement, robotics with its required embedded software, and the combined system. Note that this is a fixed-horizon reference; the calendar-year selector does not change that table.

Select **Trace inputs and costs** for one cell. Reconcile each total from human/site digital cost, robot operating cost and annual capital consumption. Inspect accepted robot output and retained human hours, then open the exact inputs and engine equations. Identify which values would require target-site evidence before this comparison could support a deployment decision; every coefficient here is synthetic.

Explain these two quantities:

- Robotics value against an improved human baseline: `C01 − C11`.
- Cost interaction: `C11 − C10 − C01 + C00`.

A negative interaction means complementary cost reduction within the scenario's definitions. It does not establish causality in a real workplace. A positive interaction can arise when two changes remove overlapping work or introduce additional costs. Total joint savings must not be added again to both separate savings.

Start from the reference and change only **Human time reduction**, keeping **Robot scheduling change** fixed. Trace its effect on the human-led comparator and the human work retained alongside robots. Then inspect the saved digital-first preset: it changes both human time reduction and robot coordination, so its difference from the reference cannot isolate one channel. Fewer robots need not mean a worse production system if the alternative improved. Digital systems can also improve robot capability or coordination; target-side evidence must determine those channels.

Open a benchmark record. Identify its task population, model/harness version, human involvement, budget and clock. Explain why a paused simulation or successful-episode-only cost cannot directly price a hospital or factory service.

## 4. Separate the customer's organization from the robot's owner

Open **Customer adoption** and **Business models**. Hold technical controls fixed while changing a customer profile. Trace the mechanism through approval, authority, implementation capacity or funding criteria. The profile label is not a productivity multiplier.

Then compare sale, lease and service arrangements. Identify who owns the robot, who controls the workflow, who funds the asset and who retains software/data rights. Internal payments move cash between parties; they do not automatically create consolidated economic value.

Compare the saved RaaS entrant and prompt-incumbent-response cases. The entrant and incumbent have the same robot technology and terms. Explain how demand, price, ramp and receivables can change the entrant's funding requirement without changing the robot. These are synthetic comparisons, not evidence of available financing or attainable market share.

The current monthly entrant is separate from the annual shared-resource model. Do not add their outputs or assume both fleets can claim the same components. The [treasury proposal](model/treasury_extension_design.md) describes the full accounting extension. Its [isolated financial core](model/TREASURY_CORE.md) now tests payments, reservations, deposits and explicit credit, but does not yet integrate physical supply or the entrant. Explain why a passed cash-settlement witness cannot establish delivered service.

**Check your understanding:** give one case where the deployment is economically attractive but temporarily unfundable, and another where funding exists but the physical service cannot be delivered.

## 5. Challenge a real source at the operating boundary

Choose either the hospital or TenneT follow-up. Open its evidence from the relevant dashboard view, then read the source locator and limitations.

For hospital logistics, distinguish transport-phase duration, loading/unloading, safety accompaniment, interventions and paid staffing. Preserve the inconsistent success counts rather than selecting the more favorable percentage. For inspection, distinguish reaching a point, obtaining an accepted measurement, interpreting it, taking action and eliminating a required human visit. Selected robot-suitable points are not the complete mandatory inspection inventory.

Write the minimum operating ledger you would need: eligible and excluded work; attempts and accepted output; deadlines and quality; all human support; retained fleet exposure; complete costs; and the customer's retain, expand, redesign or stop decision. Do not invent a missing denominator.

## 6. Turn understanding into one falsifiable decision

Pick one thesis from [THESIS_REGISTER.md](THESIS_REGISTER.md). Explain its mechanism, strongest evidence, strongest objection and next disconfirming observation. Choose the smallest next research action that could change a deployment choice. A new company list is not automatically more useful than one matched support-cost denominator.

A useful session ends with three artifacts: your own explanation of one cell, one corrected or challenged thesis, and one prioritized question with an explicit stopping condition. Record misunderstandings as learning targets. If an equation or control remains unclear, work that example before broadening the research.

This walkthrough prepares interpretation and thesis refinement. It does not initiate practitioner outreach, publish private work, select an employer or commit to a startup. Those later stages remain contingent on evidence and Amar's direction, as the accepted plan specifies.
