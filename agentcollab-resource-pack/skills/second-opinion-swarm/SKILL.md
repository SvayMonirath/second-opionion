---
name: second-opinion-swarm
description: Run internal peer-review collaboration using separately spawned sessions of the current AI model. Every participant examines the same assignment independently, then challenges claims, verifies evidence and reassesses. Use only when the host supports genuine separate sessions and private first submissions.
---

# /second-opinion-swarm — Internal Independent Collaboration

## Purpose

Create a small panel of actual, separately spawned sessions of the current AI/model by default. All participants examine the same central assignment. The purpose is independent initial reasoning, challenge, verification and reassessment—not splitting a project into separate workstreams and not contacting external providers.

## Required reading

Read `../second-opinion/references/internal-swarm-protocol.md`, `collaboration-contract.md`, `evidence-and-verification.md` and `privacy-and-permissions.md`. Use templates under `../second-opinion/templates/`.

## Preflight gate

Before launching, confirm the host can genuinely spawn separate executions and provide fresh contexts. Determine whether initial submissions can remain private until all first passes are collected. Inspect the actual host's supported tool/API and limits.

If the runtime cannot spawn separate sessions, do not role-play a swarm. Explain the limitation and offer `/second-opinion-perspectives` as a different mode. If the runtime cannot protect first-pass privacy, mark the execution degraded and disclose it; do not claim full protocol compliance.

## Default design

- One primary coordinator/adjudicator (not an extra vote).
- Three worker participants by default: Independent Analyst, Alternative Analyst and Falsification Analyst.
- Optional fourth Evidence Examiner only when claim verification load justifies it.
- Same model as the primary agent by default; report model identity only if observable.
- Same neutral task brief, source material, requirements and constraints.
- Fresh separate contexts; tools read-only and minimally scoped by default.

## Required phases

1. Prepare a neutral task brief without revealing the primary's preferred conclusion.
2. Spawn all participants independently and concurrently when supported.
3. Keep submissions hidden from peers until all successful/failed/timeout states are recorded.
4. Preserve original submissions unchanged.
5. Compare claims and identify material disagreements.
6. Send targeted challenge packets; do not create unrestricted debate.
7. Verify high-impact disputed claims using actual sources, calculations, inspection or tests.
8. Ask each participant to reassess and explain ACCEPTED / PARTLY ACCEPTED / REJECTED / UNRESOLVED challenges.
9. Adjudicate claim-by-claim without majority voting or forced consensus.
10. Produce the final report with limitations and unresolved minority findings.

Default to one independent pass, one challenge pass, one reassessment pass and at most one targeted extra verification cycle. Stop when further work has low expected value or the task limits are reached.

## Non-negotiable rules

- All participants investigate the same core assignment.
- Roles change analytical focus, not task ownership.
- Do not expose the coordinator's own conclusion before first submissions.
- Do not treat same-model contexts as independent providers or statistical independence.
- Do not count repeated use of one source as corroboration.
- Do not force a challenge, a changed mind, a winning option or unanimous agreement.
- Do not use confidence averaging or majority voting.
- Do not fabricate spawned agents, model IDs, sources, tool results or tests.
- Do not modify files, commit, deploy or contact external services unless separately authorized.
- Report context, tool, workspace and process isolation separately.

## Report

Use `../second-opinion/templates/final-report.md`. Include actual participant count, roles, first-pass positions, material challenges, actual verification, reassessment, final adjudication, minority views and limitations.
