# AgentCollab Evaluation Scorecard

## Purpose

Determine whether collaboration improves outcomes enough to justify additional inference, coordination, latency and disclosure risk. Do not assume that more participants improve quality.

## Compare methods

For the same representative task set, compare:

- **Baseline:** one normal agent response with comparable tools/evidence.
- **Perspectives:** one agent, separate analytical passes.
- **Internal swarm:** separate sessions of the same current model, following the AgentCollab protocol.
- **External collaboration:** only when a real second provider is connected and the same disclosure/scope is acceptable.

Use the same task brief, source access and acceptance criteria. Run more than one trial where feasible. Avoid changing multiple variables at once.

## Measures

Score each dimension 0–4 and record evidence. Do not collapse the whole evaluation into a single score without showing the dimensions.

| Dimension | 0 | 2 | 4 |
|---|---|---|---|
| Factual accuracy | Materially wrong | Mixed accuracy | Important facts correct and well-qualified |
| Error detection | Misses known material error | Detects some | Detects important planted/real errors |
| Evidence quality | Unsupported | Mixed source quality | Relevant, traceable and independent where claimed |
| Challenge quality | Empty/false objections | Some useful challenges | Specific, material and evidence-backed challenges |
| False positives | Many invented defects | Some noise | Few unsupported findings |
| Requirement coverage | Major omissions | Partial coverage | All material criteria addressed |
| Reassessment | No meaningful response | Mixed | Evidence-linked changes/retentions |
| Uncertainty calibration | Overclaims | Some caveats | Accurate limits and unresolved status |
| Problem focus | Drifts | Some drift | Stays on task |

Also record raw metrics:

- elapsed wall-clock time;
- model calls and participant count;
- token or usage cost where observable;
- tool calls;
- verification actions actually executed;
- failures/timeouts;
- privacy/data disclosure scope.

## Interpretation

- A higher answer length is not a quality improvement.
- Consensus is not an outcome metric by itself.
- A swarm finding a valid error that the baseline missed is valuable; a swarm inventing multiple false objections is not.
- A swarm that uses much more cost for no measurable improvement should not be the default.
- Provider diversity is different from multiple contexts of the same model.
- Report uncertainty and sample-size limitations; do not generalize from a tiny test set.

## Evaluation record

| Task | Method | Accuracy | Error detection | Evidence | False positives | Coverage | Time | Cost | Notes |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| | Baseline | | | | | | | | |
| | Perspectives | | | | | | | | |
| | Swarm | | | | | | | | |
