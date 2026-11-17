# Aggregate production topology cannot identify task-level robot value

**Research continuation, 17 November 2026, Q2.** Input branch \`60e0dfe9ed23123e6870c5aeff65a17d833e87fe\`. Status: exact synthetic identification result, primary-source accounting interpretation, and a field-level measurement design. **Not an observed BEA dataset, calibrated industrial result, or selected novel paper claim.** The associated exact code is \`sector_bridge.py\` with eight scoped tests.

## Economic question and source distinction

BEA supply/use accounts are a defensible economic **backbone** because they describe commodity production, use by industries, and demand by final purchasers. Official BEA documentation distinguishes supply valued at basic prices from use valued at purchasers' prices; its make/use framework and import/requirements accounts have different accounting meanings. BEA's annual program covers 71 industry summary categories and detailed benchmark tables (roughly 402 industries). BEA's Input-Output interactive page states a late-September annual update cadence. These are economic classifications and money flows—not direct observations of tasks, robot-hours, service-acceptance standards, or individual payer cash. [S1–S3]

BLS's historical nominal input-output compilation covers 1997–2025, separately from a 2035 projection, and BLS explicitly says it is **derived from BEA**, not itself a raw BEA supply/use table. [S4] A secondary BEA-derived 2024 matrix catalog exists [S5] but is not an authoritative primary release.

**Acquisition audit:** BEA's current interactive tables and official guide were read, but no authoritative numeric use/supply table could be materialized in this run. The available container could not resolve BEA/BLS hosts for binary download; web extraction rejected the BLS ZIP; the BEA API requires a user identifier; and the secondary CSV host returned HTTP 530. Therefore **verified observed numeric sector edges obtained = 0**. We will not fabricate an empirical matrix or turn cached sample figures into U.S. values. Q2's observed-backbone acceptance gate remains OPEN. Do not retry unchanged download routes without a different access method. The analytical tranche below is independently useful.

## An exact identification failure

A statistical Use table records purchases at the commodity×industry level. The distinct deployment graph must resolve end-market/value-chain position, productive process, qualified task bundle, embodiment, software policy, service/verification, contract, and customer demand, with payment and learning edges separately identified.

The executable synthetic **industry-by-industry** example has three sectors—materials, manufacturing and health services—each with normalized gross output 100. Rows are suppliers and columns are purchasing industries. The transaction matrix Z is

| Supplier / purchaser | Materials | Manufacturing | Health |
|---|---:|---:|---:|
| Materials | 5 | 30 | 10 |
| Manufacturing | 10 | 10 | 10 |
| Health services | 5 | 5 | 15 |

Final demand is (55,70,75); sector value added is (80,55,65); and **total labor value added is 40 within each sector's value added**, not additional to it. Both row sales plus final demand and column intermediate inputs plus value added reconcile to gross output of 100 in every sector. This fixture is **not BEA data**. Its square representation requires a one-to-one industry/commodity assumption that is not implicit in actual BEA supply-use tables.

Suppose a qualified RaaS provider charges fee f=15 for a complete task bundle and incurs provider operating cost k=12. Under fixed accepted output, a customer accepts iff its truly **avoidable** cost of that complete task bundle exceeds 15, with all retained work and alternative service obligations accounted for. In economy E1 the manufacturing/health eligible labor costs are (30,10); in economy E2 they are (10,30). Each industry's remaining labor equals 40 minus eligible cost. Every macro input, output and industry labor number is identical. Yet E1 only supports the manufacturing deployment, while E2 only supports health. The accepted customer gains 30−15=15 and the provider earns 15−12=3. The rejected opportunity would destroy customer value at that price.

**Non-identification proposition.** If two sectors have aggregate labor totals \`L_i,L_j>f\`, and their accounts do not reveal eligible/retained task partitions, there can exist allocations within those totals such that the same observed use, output, value-added and labor accounts yield opposite adoption rankings at price \`f\`. Take eligible costs above f in one sector and below f in the other; reverse them and allocate residual labor so sector totals stay fixed. Adoption flips while every aggregate observable remains unchanged. If provider cost k<f, the positive-profit opportunity also flips. This is a proof by construction, not a novel theorem. It shows why a sector centrality metric cannot serve as an estimate of robot-addressable, profitable service.

Under **labor-only fixed-output substitution**, where all other costs/benefits are known to be zero, sector labor total L and fee f provide only a possible customer benefit interval \`[0,max(0,L-f)]\`. Here it is [0,25] for each candidate sector: the accounts do not rank them. The interval is NOT a bound on broader robotic production value when output, capacity, quality, risk, integration or support also change.

## What BEA-style network information can contribute

For a **reconciled symmetric** constant-coefficient economy with \`A_ij=Z_ij/x_j\`, \`rho(A)<1\` and fixed account prices, an exogenous final demand perturbation satisfies

\`Δx=(I−A)^{-1}Δy.\`

This is a conditional accounting/technology response, not a measured causal effect. A raw BEA commodity-by-industry use table is not itself a symmetric A; conversion requires explicit supply/make and technology assumptions.

Let a qualified robot lower a customer's per-output cost by g, let the customer pass through fraction \`θ∈[0,1]\` and let local demand respond at slope \`β≥0\`. **Only conditional on those additional behavioral assumptions** does \`Δy_j=βθg\` imply \`Δx=(I−A)^{-1}e_jβθg\`. The accounts identify neither g nor θ nor β, and Leontief gross-output propagation is not provider revenue, consumer surplus or welfare.

Our exact synthetic demonstration sets g=(30−15)/100, θ=1, β=10, giving the same destination-specific final-demand shock 3/2 in both economies. In E1 it enters manufacturing and \`Δx=(13/23,321/184,25/184)\`; in E2 it enters health and \`Δx=(6/23,21/92,165/92)\`. The starting macro network is identical; the underlying service opportunity determines which sector can create the demand perturbation. The exact program verifies both responses. No observed U.S. numerical inference follows.

## What the next empirical atlas must actually observe

**Three resolutions, never silently joined:** (1) authoritative BEA commodity×industry monetary use/supply with year, vintage, currency/valuation, industry concordance, imports, value-added and final-demand rows; (2) named workflow with complete accepted service, feasible incumbent alternative, retained work, qualification standard, site/configuration and task-specific physical time; and (3) customer ability/willingness to pay, price/contract, collections, payer assets/finance, and legal learning-transfer rights.

A meaningful opportunity row needs \`target accepted service → matched baseline → robot configuration and adaptation → verified site output and complementary work → customer's incremental operating value → capturable provider cash → reinvestment/learning path\`. Unknown links remain unknown. The strongest test would compare a high monetary input-output exposure with little measured avoidable task work against a less central but economically attractive task, with both cases actually evidenced. No such case contrast is claimed measured here.

**Measurement priority:** acquire an accessible BEA table in raw export format, reconcile industry and commodity codes/totals, extract a bounded manufacturing/transport/health subgraph, and test whether measured task economics reorder its aggregate-exposure ranking. Do not map a policy benchmark gain or a financing press release to the same physical deployment without a joined observation.

## Verification, limits, continuation

Executable code: \`python sector_bridge.py\`; \`python -m unittest -v test_sector_bridge\`. **Eight new exact tests passed in this session**. No external dependencies. This is a synthetic model and exact arithmetic, not historical repository CI, causal identification, or a new empirical estimate. Source-oriented notes are used to discipline future measured topology, not to claim a completed atlas.

Because the official numeric access routes above were boundedly exhausted, the next useful independent research tranche is **Q3: demand and contracts**, bridging the earlier RaaS hourly-receipt model with the new qualification and embodiment-delay results. Revisit source acquisition only when an actual compatible export route becomes available. Preserve the Christmas deadline and the original empirical gate as open.

## Sources and read boundaries

[S1] BEA, *Guide to Interactive Industry Input-Output Accounts Tables*, read 2026-11-17: https://www.bea.gov/resources/guide-interactive-industry-input-output-accounts-tables. [S2] BEA, *Input-Output Accounts Data*, read 2026-11-17: https://www.bea.gov/data/industries/input-output-accounts-data. [S3] BEA, *Input-Output* interactive release page, read 2026-11-17: https://www.bea.gov/itable/input-output. [S4] BLS, *Inter-industry relationships*, published page last modified 2026-08-27: https://www.bls.gov/emp/data/input-output-matrix.htm. [S5] Leontief/Arcanum research catalog (secondary BEA-derived source, retrieval blocked): https://inputoutput.heterodata.org/data.
