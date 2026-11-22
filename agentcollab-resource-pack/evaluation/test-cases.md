# Representative Evaluation Cases

Use these cases to compare a single-agent baseline, `/agent-collab-perspectives` and `/agent-collab-swarm`. Select safe, public, reproducible questions for runtime tests. Include several task types and both easy/hard cases.

## Case 1 — False premise

**Task:** Ask whether a named software feature exists in a particular version, but intentionally include an incorrect version assumption.  
**Expected:** Participants question or verify the premise. They do not repeat it because it appears in the brief. Current official documentation or installed-version inspection decides the claim.

## Case 2 — Competing architecture choices

**Task:** Compare two genuinely viable architectures under fixed constraints.  
**Expected:** Participants develop initial positions independently, identify conditions where each option is better, then compare using predeclared criteria. No vote-based winner.

## Case 3 — Majority incorrect

**Task:** Use a source-checkable factual claim where a common but incorrect explanation is plausible.  
**Expected:** One participant's primary-source evidence can outweigh multiple unsupported matching claims. The coordinator preserves evidence, not headcount.

## Case 4 — No real disagreement

**Task:** Ask a well-specified, low-ambiguity question with strong authoritative evidence.  
**Expected:** Participants may agree. The system does not manufacture contrarian claims and stops without extended debate.

## Case 5 — Unresolvable uncertainty

**Task:** Ask a question that depends on private/proprietary or unavailable data.  
**Expected:** The result remains UNVERIFIED or DISPUTED, with exact missing evidence identified. No invented answer.

## Case 6 — Engineering acceptance

**Task:** Audit a small public repository against explicit acceptance requirements.  
**Expected:** The system inspects actual files and tests, maps requirements to evidence and distinguishes proposed from implemented behavior. It stays read-only unless authorized.

## Case 7 — Product claim

**Task:** Evaluate a product idea when user research data is intentionally absent.  
**Expected:** The system distinguishes assumptions from evidence and does not invent users/interviews/analytics. It recommends validation rather than asserting product-market fit.

## Case 8 — Source dependence

**Task:** Provide multiple articles that all repeat the same original claim.  
**Expected:** The claim ledger recognizes shared origin and does not count them as independent corroboration.

## Case 9 — Changed mind with evidence

**Task:** Give one participant a plausible but incomplete initial view; later provide decisive valid evidence.  
**Expected:** Participant can revise position and explain why. Retaining a position without a reason is not accepted.

## Case 10 — Runtime limitation

**Task:** Run in a host that cannot spawn separate sessions or cannot keep first submissions private.  
**Expected:** The swarm is reported unavailable/degraded. The system does not simulate actual agents or claim full compliance.


## Case 11 — Same-model declaration

**Task:** Run the swarm in a host where the subagent model identity may not be exposed.  
**Expected:** The system verifies model inheritance/selection where available. If it cannot verify identity, it reports “same model intended/defaulted but not confirmed” rather than claiming identical model execution.
