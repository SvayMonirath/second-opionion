# Collaboration Contract

## Purpose

Improve the reliability, completeness or usefulness of an answer through independent analysis, targeted challenge, evidence checking and disciplined synthesis. Collaboration is a means, not an objective in itself.

## Shared task contract

Every substantial collaboration begins with a neutral task brief. Record:

- original question and requested output;
- objective and scope;
- requirements and constraints;
- authoritative inputs and source precedence;
- assumptions and unknowns;
- acceptance criteria;
- privacy classification and permissions;
- allowed tools and side effects;
- resource/iteration limits;
- required report format.

Do not bias the brief by inserting the primary agent's preferred answer. If the user provided a candidate proposal, include it as the object of evaluation, not as an endorsed conclusion.

## Collaboration roles

Roles are temporary analytical responsibilities. They are not permanent model/provider identities.

- **Coordinator/adjudicator:** prepares the task, controls phases, preserves records, resolves issues and synthesizes. It does not receive an extra vote.
- **Independent analyst:** forms an initial view based on the assignment.
- **Alternative analyst:** looks for materially different interpretations or options without inventing disagreement.
- **Falsification analyst:** searches for counterexamples, contradictions and failure conditions without being required to reject the proposal.
- **Evidence examiner:** checks disputed/high-impact claims against primary sources, data, calculations or tests when needed.
- **External reviewer:** an actually connected model/agent outside the current host/model runtime.

Do not appoint implementers, source-silo researchers or separate domain teams unless the task separately requires those workflows. SecondOpinion is a review/collaboration layer, not a replacement for the user's domain-specific skill system.

## Independence and influence

For a meaningful independent review:

1. Give participants the same neutral task brief and comparable relevant source material.
2. Keep their initial conclusions private until submitted.
3. Avoid exposing the primary agent's preferred conclusion before the first pass.
4. Record initial submissions before distributing challenges.
5. Where practical, anonymize submissions or remove author identity during the comparison stage to reduce status/authority anchoring.
6. Record common sources, shared model, shared tools and any information leakage.

Different role prompts and context windows do not guarantee statistically independent reasoning. State the limit accurately.

## Evidence and disagreement

- Treat agreement as a reason to check important common assumptions, not proof.
- Treat challenges as claims requiring evidence too.
- Distinguish source-supported, inferred, assumed, tested and unresolved statements.
- Preserve minority positions when material.
- Do not force participants to change position or force consensus.
- Do not use majority voting as a truth mechanism.
- Prefer primary sources and reproducible verification where available.
- Record when sources share an underlying origin.

## Bounded iteration

Default substantive review: one independent pass, one cross-challenge pass, one reassessment pass, and at most one targeted extra verification cycle. Add further work only if a material issue remains, the expected value is clear and resources/permissions allow it.

## Completion conditions

A collaboration is complete when the requested acceptance criteria are met or remaining blockers/uncertainties are explicitly reported. Completion does not require agreement. If the host could not perform a required operation, report the limitation rather than silently substituting a weaker method.

## Deliverable integrity

Keep original submissions, challenges, claim statuses and verification records available for audit where the host supports it. The user-facing report should summarize evidence and rationale; do not expose hidden chain-of-thought.
