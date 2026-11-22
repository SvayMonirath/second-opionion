# Internal Swarm Protocol

## Definition

The internal swarm is a structured peer-review collaboration among multiple **separately spawned executions of the same current AI/model by default**. Every participant examines the same central assignment. The purpose is to create independent initial assessments, serious challenges, claim verification and reassessment without contacting external models.

This is not a task-splitting team. Participants do not each own a different project workstream. This is not one model role-playing several people. The runtime must actually create separate agent executions.

## Required runtime capability

Before starting, verify that the host can:

1. spawn at least two genuine, separate agent executions;
2. give each a fresh context not containing the coordinator's private conversation history by default;
3. give all participants the same neutral task brief and relevant source material;
4. inherit or explicitly select the same current model/model tier for every participant when the host supports it;
5. keep initial submissions from other participants until the first pass is complete, either via separate private return channels or coordinator-held submissions;
6. receive and preserve each participant's structured result;
7. distribute challenges and verification results in a controlled second phase.

Three participants are the default target. At least two successfully spawned and separately submitting participants are required to call an execution a swarm. If the host cannot protect the first-pass phase, clearly mark the swarm protocol as degraded and explain the exact limitation. Do not claim full protocol compliance.

## Roles and default size

The coordinator is the primary agent and is not an extra vote. Verify that each worker inherits the primary model configuration or can be explicitly assigned the same model. If the host silently substitutes a different model or the identity cannot be confirmed, disclose that limitation; do not claim confirmed same-model identity.

Default three participants:

- **Participant A — Independent analyst:** answer the same original question and build a reasoned initial conclusion.
- **Participant B — Alternative analyst:** test a different interpretation or develop a materially different candidate answer; do not manufacture difference.
- **Participant C — Falsification analyst:** actively look for counterexamples, contradictions, hidden assumptions and evidence that would overturn the leading conclusion; do not force a negative finding.

Optional fourth participant:

- **Participant D — Evidence examiner:** independently check high-impact disputed claims against primary sources, relevant data, reproducible calculations or tests.

Keep role instructions analytical, not domain-specialist. All participants still examine the same central question. Do not assign one participant only research, another only engineering and another only security unless the user explicitly requests task decomposition as a separate activity.

## Phase 0 — Preflight

The coordinator:

1. identifies the objective, requirements, authoritative materials, constraints and permission boundary;
2. assesses whether a swarm offers sufficient value over one-agent perspectives;
3. confirms actual subagent spawning, context isolation, submission privacy, allowed tools, concurrency and limits;
4. chooses participant count and roles;
5. creates a neutral task brief;
6. records what isolation is and is not guaranteed.

If spawning or required first-pass privacy is unavailable, do not simulate participants. Explain that the requested swarm cannot be performed under the current host capability and offer `/agent-collab-perspectives` as a different fallback. Do not silently switch modes.

## Phase 1 — Independent first pass

Spawn all selected participants concurrently when the runtime supports it. Every participant receives:

- the same task brief;
- the same relevant source material and source-authority rules;
- the same constraints and acceptance criteria;
- its role-specific analytical focus;
- the same tool/permission boundary;
- a request not to infer or claim access to other participants' work.

Do not give any participant:

- another participant's output;
- the coordinator's preferred answer or private reasoning;
- an assessment of which participant is senior or expected to be correct;
- hidden context that would bias the analysis but is not part of the task evidence.

Require a compact structured submission:

1. interpretation of the question;
2. initial conclusion or candidate answer;
3. key claims and supporting evidence;
4. assumptions and uncertainty;
5. strongest alternative explanation;
6. plausible failure modes/counterexamples;
7. what evidence would change the conclusion;
8. what was not investigated.

The coordinator stores each first submission unchanged with participant ID, role, available model/runtime identity and source/tool access actually known. Do not invent model identifiers.

**Gate:** Do not distribute peer conclusions until every successfully launched participant has either submitted or timed out/failed and that failure is recorded. If one participant fails, proceed only if at least two valid independent submissions remain; disclose the reduced participation.

## Phase 2 — Comparison and issue selection

The coordinator compares initial submissions and creates an issue/claim list. Identify:

- agreements on material claims;
- material disagreements;
- distinct interpretations or candidate solutions;
- unsupported or circular claims;
- assumptions that differ;
- important questions all participants missed;
- claims whose resolution could change the answer.

Do not equate agreement with verification. Do not suppress outlier conclusions. When practical, distribute anonymized claims without author labels to reduce anchoring.

## Phase 3 — Controlled cross-examination

Each participant receives the relevant competing claims and is asked to challenge material points, not to argue endlessly. The challenge packet should identify:

- target claim/conclusion;
- reason it may be wrong or incomplete;
- evidence, counterexample or logical defect;
- impact if the challenge is correct;
- specific check that could resolve it.

Participants may also state that no material objection was found, but must state what they examined and what remains outside scope.

The coordinator controls message flow. No unrestricted participant-to-participant chat is needed. Do not let one participant's confident language substitute for evidence.

## Phase 4 — Claim-level verification

Build a ledger of material claims. Prioritize by:

- impact on the final conclusion;
- uncertainty;
- plausibility of being wrong;
- ease and cost of checking.

Use appropriate verification: original/primary sources, official documentation, source-code inspection, calculations, data analysis, safe experiments or tests. An additional model opinion alone is not verification.

Record source provenance. Copies or summaries of the same original source are not independent corroboration. Record execution conditions and limits for tests. If the required tool/source is unavailable, mark the claim unverified rather than imply it was checked.

## Phase 5 — Reassessment

Send the verified issue packet to the participants. Each responds to its own initial position and material challenges.

For each challenged claim, mark:

- **ACCEPTED** — challenge is valid;
- **PARTLY ACCEPTED** — part is valid or requires qualification;
- **REJECTED** — challenge is not supported, with reason;
- **UNRESOLVED** — available evidence cannot settle it.

Every participant records:

1. original position;
2. current position;
3. what changed or did not change;
4. what evidence/argument affected it;
5. remaining disagreement;
6. outstanding uncertainty.

Do not reward stubbornness or agreement. A position change needs a reason; retaining a position also needs a reason.

## Phase 6 — Coordinator adjudication

The coordinator evaluates claim by claim using evidence quality, source reliability, logical validity, task requirements, feasibility, risks and test results. It does not count votes, average confidence or defer to the most senior-sounding participant.

It may conclude:

- one answer is best supported;
- several options remain viable under different conditions;
- the initial proposal is only conditionally supported;
- all proposed answers are inadequate;
- evidence is insufficient to decide.

Preserve a minority position when it raises a material unresolved issue. Separate participant agreement from evidence status.

## Phase 7 — Optional targeted extra cycle

Allow at most one additional focused cycle by default, only for a material issue that could alter the outcome. Give a narrow, testable assignment and the relevant evidence. Do not restart the entire swarm just to obtain more opinions.

Further cycles require a clear reason and must remain within the user's resource/permission limits.

## Stop conditions

Stop when:

- acceptance criteria are satisfied to the available evidence level;
- no material new evidence or challenge is emerging;
- unresolved issues cannot be settled with available tools;
- the agreed participant/time/token/tool budget is reached;
- additional work has low expected value;
- human input or approval is needed.

No unanimity requirement.

## Permissions and isolation

Default to read-only. Do not modify files, commit, push, deploy, make purchases, send external messages or alter system configuration. If the task later requires implementation, use a separately authorized workflow and explicit resource ownership.

Report separately:

- **context isolation:** separate conversation history/context;
- **tool isolation:** per-participant tool availability/permissions;
- **workspace isolation:** shared filesystem vs isolated workspace/worktree;
- **process/security isolation:** only if actual host guarantees are known.

Never infer OS/process isolation from a fresh context. Prevent participants from spawning nested agents unless explicitly required and authorized. Never share credentials or unrelated sensitive context.

## Failure handling

- **Spawn failed:** record exact failure; do not invent a participant.
- **Only one participant returned:** this is not a completed swarm; offer perspectives or report partial execution.
- **First-pass privacy unsupported:** mark protocol degraded; do not claim full independence.
- **Tool unavailable:** mark affected claim unverified.
- **Participant timeout:** preserve completed submissions and report missing contribution; continue only if minimum valid participants remain.
- **Conflicting source access:** record differences and resolve with authoritative sources where possible.
- **Shared-board leakage:** do not use a board that reveals first opinions before submissions are locked unless the host can provide private partitions.

## Final swarm report

Include:

1. assignment and task brief summary;
2. participants actually spawned, roles and model/runtime identity only if observable;
3. isolation level and limitations;
4. preserved initial conclusions;
5. key agreements and disagreements;
6. material challenges and verification actions;
7. participant reassessment and changed positions;
8. evidence status for important claims;
9. adjudicated conclusion and rationale;
10. minority findings and unresolved uncertainty;
11. resource use and execution failures, if known.

Do not include private chain-of-thought. Provide concise reasoning summaries and auditable evidence.
