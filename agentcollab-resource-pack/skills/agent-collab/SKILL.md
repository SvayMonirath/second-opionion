---
name: agent-collab
description: Universal evidence-led collaboration router. Use when a task may benefit from independent analysis, internal peer review, external model collaboration, critical challenge, alternative paths, research, engineering, security, product evaluation, decisions or acceptance audits. Select the simplest adequate method and verify actual runtime capabilities.
---

# AgentCollab — Universal Router

## Purpose

Be the single entry point for AgentCollab. Understand the task, select the simplest adequate collaboration method, invoke the relevant method and domain guidance, and deliver one evidence-led result. The user should normally need only `/agent-collab`.

AgentCollab is a methodology layer, not an agent runtime or integration. It must discover host capabilities and must never pretend to spawn agents, contact models, access files or verify results when it has not done so.

## Read shared guidance

Read the relevant files under this skill's `references/` directory:

- `routing-and-command-model.md` for mode selection and command semantics.
- `collaboration-contract.md` for common collaboration standards.
- `internal-swarm-protocol.md` for internal same-model peer review.
- `external-collaboration-protocol.md` for real external participants.
- `evidence-and-verification.md` for claim and evidence handling.
- `domain-methods.md` for research, engineering, security, product and decision shortcuts.
- `runtime-adapters.md` for host capability inspection.
- `privacy-and-permissions.md` for information sharing and approvals.

Templates are under `templates/` in this skill. Variant skills are sibling directories under the shared skill root; if the host makes them available, read the relevant variant's `SKILL.md` rather than recreating its instructions.

## Universal workflow

### 1. Understand the request

Extract objective, requested deliverable, scope, constraints, authoritative inputs, acceptance criteria, risk and permissions. Use context already provided. Ask only for a detail that is genuinely blocking.

### 2. Select the domain method

Recognize whether the task is research, engineering, security, product, decision-making, audit or a combination. Domain methods define evaluation criteria and checks; they do not dictate a separate agent team. Reuse existing user skills, agents, tools and workflows. Do not duplicate them.

### 3. Select the collaboration topology

Choose the smallest method likely to improve the result:

- **Direct/solo:** simple, low-risk tasks where collaboration adds little.
- **Perspectives:** one current agent makes multiple structured analytical passes; no new participants.
- **Internal swarm:** `/agent-collab-swarm` only when actual separate subagent executions are supported and the value of same-model independent peer review justifies the cost.
- **External:** `/agent-collab-external` when provider/model diversity or an explicitly requested external participant is valuable and a real authorized transport exists.
- **Hybrid:** internal swarm plus external participation only when the added diversity materially helps and the user has authorized external disclosure.

Do not automatically swarm every task. Do not call single-agent role-play an independent swarm. Do not assume an external API, browser, CLI, MCP server or A2A endpoint exists.

### 4. Route to optional shortcuts

Use the same prefixed command family:

- `/agent-collab-swarm`
- `/agent-collab-external`
- `/agent-collab-perspectives`
- `/agent-collab-challenge`
- `/agent-collab-paths`
- `/agent-collab-audit`
- `/agent-collab-connect`
- `/agent-collab-research`
- `/agent-collab-engineering`
- `/agent-collab-security`
- `/agent-collab-product`
- `/agent-collab-decision`

These are optional direct entry points. The universal router should invoke their relevant method internally where host skill invocation permits; otherwise follow the corresponding skill instructions directly. Never create unprefixed aliases.

### 5. Set the evidence and permission contract

Use read-only access by default. Decide what sources, tools, files and data are necessary. Minimize disclosure. Obtain explicit authorization before sending data externally or performing consequential side effects. See `privacy-and-permissions.md`.

### 6. Collaborate and verify

Use the selected protocol. Preserve independent initial opinions where applicable. Track claims separately from opinions. Verify material claims using suitable sources, code inspection, calculations, experiments or tests. Never use participant count or agreement as proof.

### 7. Synthesize

Present the conclusion, reasons, evidence, disagreements, changes of position, limitations and unresolved questions. Do not hide minority findings. Do not claim certainty beyond the evidence.

### 8. Stop appropriately

Avoid needless loops. For a substantive review, default to one independent pass, one challenge pass, one reassessment pass and at most one targeted extra cycle unless new evidence or user authorization justifies more. Stop when criteria are met, marginal value is low, a capability limit is reached or human input is needed.

## Output expectations

For a short task, answer directly. For a substantial collaboration, include:

1. task and method;
2. actual participants and runtime capabilities;
3. important findings and their evidence status;
4. material disagreements and their resolution;
5. verification performed and not performed;
6. conclusion/recommendation;
7. uncertainty, limitations and next action.

Do not expose private chain-of-thought. Provide concise reasons, evidence and decision records instead.

## Non-negotiable honesty rules

- A skill file is not proof of an available subagent runtime.
- A separate context is not necessarily a process, workspace or security sandbox.
- Same-model subagents do not provide provider/model diversity.
- MCP is not automatically a model-to-model chat bridge; A2A requires compatible reachable agents.
- A prepared handoff is not a sent message; a sent message is not a received answer.
- A recommendation is not verification; describe the actual check and its scope.
- No hallucination-free guarantees, fabricated citations, synthetic tool results or invented model identities.
- Do not imply unanimous agreement or use majority voting as the adjudication method.
