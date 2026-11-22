# Evidence and Verification

## Core rule

A claim is not true because an agent said it, because several agents repeated it, or because the group agrees. The final synthesis must distinguish evidence from reasoning and belief.

## Claim ledger

For each material claim, record:

- unique claim ID;
- exact claim (atomic where possible);
- importance to the decision;
- who raised it;
- evidence/source references;
- source provenance and independence;
- method of verification;
- conditions and scope;
- status;
- remaining caveats.

## Claim statuses

Use one of the following and explain why:

- **VERIFIED:** a specific direct check (test, reproduction, inspection or calculation) confirmed the claim within stated conditions and scope. Record the procedure and result.
- **SUPPORTED:** reliable evidence supports the claim, but it has not been directly reproduced or tested in the target environment.
- **INFERRED:** the conclusion follows reasonably from available evidence but is not directly established.
- **ASSUMPTION:** accepted provisionally for analysis; not checked.
- **UNVERIFIED:** evidence or capability is insufficient to establish the claim.
- **DISPUTED:** credible evidence or reasoning materially conflicts and is not resolved.
- **REFUTED:** adequate evidence or a reproducible check contradicts the claim as stated.

Do not label an answer VERIFIED merely because sources seem reputable. Use SUPPORTED when source evidence exists but no direct test was done.

## Evidence quality checks

Evaluate:

1. **Authority:** Is the source primary, official, peer-reviewed, expert, first-hand or secondary?
2. **Relevance:** Does it address this exact claim, version, environment and date?
3. **Method:** Is the source's method transparent and appropriate?
4. **Recency:** Could the fact have changed?
5. **Independence:** Does this source derive from another source already counted?
6. **Scope:** Does evidence support the exact breadth of the claim or only a narrower case?
7. **Contradiction:** Is there credible counter-evidence?
8. **Reproducibility:** Can the result be repeated under stated conditions?

Prefer primary sources for specifications and current behavior. Use secondary sources for context, interpretation and triangulation. For a current software feature, inspect current official documentation and actual installed version rather than relying on old memory.

## Verification methods

Select based on claim type:

- documentation or standards inspection;
- original research and source triangulation;
- repository/source inspection;
- static analysis or linting;
- unit/integration/system tests;
- controlled reproduction or experiment;
- calculations or independent recomputation;
- dataset inspection and statistical analysis;
- authorized security validation;
- user research or actual product observations.

An additional language-model opinion alone is not a verification method.

## Independence of sources

Two URLs are not two independent sources if both quote the same press release, paper, dataset or origin. Track original publisher/author and derivation. Participants who rely on the same source are not independent evidence corroborators.

## Confidence

Avoid made-up numerical confidence scores. Use qualitative confidence only when the basis is explained. Do not average model confidence values. Explain the specific evidence and uncertainty that support the assessment.

## Challenge claims are claims too

A criticism must identify what is wrong, what evidence supports the criticism and what impact it would have. Speculative issues may be listed as hypotheses, not findings. Do not reward a reviewer for finding a large number of low-quality objections.

## Verification report

For each check record:

- what was tested/inspected;
- tool, version, source or environment if known;
- command/procedure or reproducible method, where safe and useful;
- result;
- scope/conditions;
- limitations;
- related claim IDs.

Never fabricate test execution, source inspection, citations or observed results. If no actual check was performed, say so.
