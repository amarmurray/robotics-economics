# Independent review: onboard workload qualification

Review date: 25 October 2026. Disposition: **accept the bounded source packet and its source-arithmetic helper; no required correction found.** This is acceptance of the evidence boundaries and calculations, not certification of GR00T, TensorRT, Jetson deployment compatibility, physical competence, sustained throughput or control deadlines.

## Reviewed snapshot and method

| Artifact | SHA-256 |
| --- | --- |
| `research/onboard_workload_qualification.md` | `ce6a6a7a6d067eb78b55760efcf45c92fa2d349734b9bab91f33d3ce9eaace32` |
| `data/onboard_workload_qualification.json` | `e2348e8320889a2f44ee6678ddac6d18d314ef4d046c705015f3f4095d6adf9a` |
| `model/research_calculations.py` | `a7d6f7e4ca03fc9e8b89e736a6fccdbaceafe4dc85b86ae338002cb68eb28710` |
| `tests/test_research_calculations.py` | `4a3151a8bae1f4fb5d78382c72f046cb9c9ce6e4f4a92fcf6ee0ff7dd53c9e85` |

The review covers four claims, one same-board comparison card, 27 source quantities and three arithmetic records. It inspected the narrative, JSON and helper, then independently retrieved the consequential primary source text at 2026-10-25T17:49:29Z rather than relying on the author's cached copies. Source commits and publication-date kinds were checked against GitHub's commit API; the ROS release date was checked against the release table. No model weights, datasets or containers were downloaded, and no source workload was imported or run.

Primary sources independently retrieved:

- [Pinned tutorial](https://github.com/NVIDIA-AI-IOT/jetson-ai-lab/blob/2fcbe216dbaf6301103e03a177a1980a426c6ae7/src/content/tutorials/vla/groot_n17_on_thor.md), source-file commit 13 August 2026. Full text SHA-256 `a57f61e51d158e9f829a6b12c9022fc84bc6a3f8802c036b851dc370d62f6d52` matches OWQ-E01.
- [Pinned optimization patch](https://github.com/NVIDIA-AI-IOT/jetson-ai-lab/blob/522b964711d2a02cd880f0a2f2cea7ef313d14fc/public/code-samples/groot_n17_on_thor/groot-n17-trt-optimization.patch), commit 31 July 2026. Full text SHA-256 `6a818bfcbb149c0f0efa8567ecc0fd6909613bc53e00e08f66bb81c8c601d5a3` matches OWQ-E03.
- [Timing harness](https://github.com/NVIDIA/Isaac-GR00T/blob/9c7e746b2cd37a810070a98ef41d290a07e806c2/scripts/deployment/benchmark_inference.py) and [pipeline driver](https://github.com/NVIDIA/Isaac-GR00T/blob/9c7e746b2cd37a810070a98ef41d290a07e806c2/scripts/deployment/build_trt_pipeline.py), pinned upstream revision dated 8 July 2026. Base harness SHA-256 `2cd4051a145cd2ce37a8cdf98244ce35a33f768dd8b15643b5705597eb4a29c0` matches OWQ-E02. The date describes the upstream revision, not the experiment date or a claim that every file changed that day.
- [Isaac ROS 5.0 methodology](https://nvidia-isaac-ros.github.io/v/release-5.0/performance/index.html#methodology) and [benchmark release history](https://nvidia-isaac-ros.github.io/repositories_and_packages/isaac_ros_benchmark/index.html), release update 21 September 2026. Retrieved HTML SHA-256 values are `5330353dca395792a09649065ed72d544255b1e9e9e8d1aee26464f16d98c3e3` and `04b793cca4b57060319a1a68b9560dd6c82cfddd865e85e0a8545f76c4c1dbf8`, respectively. The versioned web path is not immutable experiment provenance.

## Findings and denominator checks

**OWQ-E01/02: the timing boundary is correctly restricted.** The tutorial reports approximately 81 ms baseline TensorRT and 39.9 ms optimized median on the same Thor developer-kit recipe. The baseline/treatment precision settings, batch one, one camera, four denoising steps, twenty timing iterations and ten calibration samples are supported by the pinned text. These remain vendor-reported results. Graph restructuring and mixed precision change together; neither a pure quantization effect nor a cross-board speedup is identified.

The harness's `compute_e2e_from_components` returns `data_processing + backbone + action_head`. Preprocessing is measured separately and the same array is reused across backend comparisons. GPU stages are separately bracketed by synchronization and timers. `prepare_model_inputs` includes input processing/collation/dtype conversion; the timed action-head call returns a prediction that is discarded. Live sensing, observation age, final action denormalization/transport, actuator motion and accepted service are not measured. A median of component sums is not necessarily the sum of component medians, and neither it nor its reciprocal identifies sustained request throughput.

The pipeline driver does not set `use_trajectory`; `BenchmarkConfig` defaults it to false. The harness consequently selects episode zero, step zero. The source supports the packet's distinction between default recipe semantics and undisclosed actual-run arguments. Code warm-ups are ten for preprocessing, five eager, seven compiled and at least ten TensorRT under default arguments; the tutorial's blanket five-warm-up statement is correctly retained as a discrepancy.

**OWQ-E03: conflicting timing tables and the separate success population remain separate.** The patch explicitly labels its table JetPack 7.2 and reports 93.8/38.9 ms baseline/optimized results. The tutorial's 81/39.9 ms table and explanation of a prior 2.41× comparison as JetPack 7.1 do not resolve that mismatch. The packet correctly avoids a cross-table ratio. The patch's 97.3% versus 97.5% claim is averaged over three rounds of a 200-episode LIBERO Spatial benchmark. It is not a trial-level noninferiority result or the `libero_10` timing cohort. The output cosine similarity is also correctly separated from task success.

**Memory, deployment and economic scope are appropriately bounded.** The 60 GB recommendation concerns storage, while 8192 MB is a builder workspace default. Neither is runtime occupancy or concurrent-workload headroom. The tutorial's unpinned model/dataset downloads and absent measured-run container/engine hashes remain explicit gaps. Its PyTorch-only bundled server and requirement for a separate TensorRT-serving wrapper are retained as integration limitations. Nothing in this packet establishes that the catalog's Unitree configurations run this pipeline, or converts simulated policy timing into accepted assemblies, totes, removed labor, OEM availability or a scenario coefficient.

**OWQ-E04: ROS metric definitions are accurately quoted in substance.** The documentation says throughput targets less than 5% frame loss while admitting some runs above target; it averages five runs after discarding the minimum and maximum. Its latency is first-sent-frame to first-received-frame in a separate 30 Hz trial, omitted without a valid measurement. These quantities do not supply a tail-latency distribution or deadline qualification. No Orin/Thor performance ratio is imported.

## Independent static and arithmetic checks

Freshly downloaded pinned base source files accepted the patch in an isolated temporary directory: `git apply --check` and application succeeded for thirteen files, and all twelve resulting Python files parsed using `ast.parse` without imports. The raw-source executable-bit warning reproduced the author's documented mode warning. The patched harness SHA-256 is `31e4fcf562d256257269c5c4d943cfb503ec831e34126b2da6847694f171ba33`, matching the packet. This verifies patch applicability and syntax only; it does not establish dependency installation, engine compilation or runtime behavior.

`onboard_timing_summary` reconstructs the source arithmetic with Decimal inputs: `1000/25 = 40 ms`, `40−39.9 = 0.1 ms`, and `41−40 = 1 ms`. It correctly uses the introductory rounded **25 Hz** claim rather than silently substituting the separate 25.1 Hz reciprocal-median display. The two small differences are arithmetic on rounded statistics, not measured timing margins or missed-deadline fractions.

All six existing source-helper tests passed. Ten additional independent adverse probes rejected booleans, NaN, infinity, zero, wrong units, changed population, changed period, duplicate metric IDs, stale stored arithmetic and an incorrect calculation-ID set. Separate inclusion probes confirmed that `research_summary` omits OWQ when absent from the explicit acceptance registry, includes it when accepted, and records the actual package content hash. Deadline-miss rate and sustained policy throughput remain null. The helper executes no source formula strings and supplies no scenario calibration. These guards validate the specified arithmetic inputs; they are not a universal validator of arbitrary source claims or runtime artifacts.

## Acceptance limits and next evidence

No blocking or required precision correction remains in the reviewed snapshot. Keep OWQ-X01–03 unresolved, the missing execution/qualification fields null, and the static-source checks distinct from benchmark reproduction. The useful next artifact is the original immutable run manifest and raw timings linked to checkpoint, dataset, engine, board and actual arguments, followed by sustained concurrent-load/power/memory traces and matched closed-loop target outcomes. A new unrelated platform benchmark would not close those gaps. No external service action or hardware execution was authorized or initiated by this review.
