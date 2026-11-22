# AgentCollab

**Resource pack:** 2.0.0  
**Prepared:** 2026-11-22  
**Brand:** AgentCollab  
**Canonical skill namespace:** `agent-collab`

AgentCollab is a reusable, host-adaptable collaboration and verification skill system. It helps an AI agent decide when collaboration is useful, coordinate internal or external participants, preserve independent assessments, challenge claims, verify evidence and deliver an auditable synthesis.

It is a skill and methodology pack. It is **not** an agent runtime, MCP server, A2A server, API client, browser automation system, credential store or guarantee of correctness.

## Naming convention

The product is called **AgentCollab**. Skill identifiers and slash commands use lowercase kebab-case because the Agent Skills format requires names made from lowercase letters, digits and hyphens, and the skill directory must match the frontmatter `name`.

Every command in this pack uses the same prefix:

`/agent-collab...`

No unprefixed AgentCollab command aliases are part of this design. A host may have its own built-in commands with similar names; do not confuse those with AgentCollab commands.

## Command set

| Command | Purpose | Typical use |
|---|---|---|
| `/agent-collab` | Universal entry point and router | Almost any task requiring analysis, collaboration or verification |
| `/agent-collab-swarm` | Internal peer-review collaboration using separate sessions of the current AI model | Independent first opinions, cross-examination, evidence verification and reassessment without contacting external models |
| `/agent-collab-external` | Collaboration with real external models or agents | Bring in Claude, ChatGPT, another provider or a reachable agent when model/provider diversity is useful |
| `/agent-collab-perspectives` | One agent performs multiple structured analytical passes | Fast multi-lens analysis without spawning participants |
| `/agent-collab-challenge` | Focused critical review | Try to falsify a proposal, answer, claim or design |
| `/agent-collab-paths` | Explore materially different solution paths | Generate and compare genuine alternatives before choosing |
| `/agent-collab-audit` | Evidence-based acceptance audit | Check an actual deliverable against its authoritative requirements |
| `/agent-collab-connect` | Discover and test collaboration capabilities | Inspect available agents, tools, transports, permissions and connection status |
| `/agent-collab-research` | Research methodology shortcut | Deep investigation, source quality, claim tracing and counter-evidence |
| `/agent-collab-engineering` | Engineering methodology shortcut | Architecture, codebase, design and implementation review; reuses existing engineering workflows |
| `/agent-collab-security` | Security methodology shortcut | Scoped threat analysis and authorized validation |
| `/agent-collab-product` | Product methodology shortcut | User problem, product direction, UX and feasibility analysis |
| `/agent-collab-decision` | Decision methodology shortcut | Compare options against explicit criteria and trade-offs |

**You only need to remember `/agent-collab`.** The other commands are optional shortcuts. The universal command should automatically load the relevant methods and choose an appropriate collaboration mode.

## Core distinction between modes

- **Internal swarm:** Multiple actual, separately invoked sessions of the same current AI/model by default. They independently investigate the same assignment, then challenge and reassess. It is not a task-splitting implementation team.
- **External collaboration:** Real communication with other models or agents. It requires an available and authorized transport. A prepared handoff is not a sent request; a sent request is not a received answer.
- **Perspectives:** One agent performing separate analytical passes in one execution. Useful, but not independent agents.
- **Challenge:** Focused adversarial examination of a specified target.
- **Paths:** Development and comparison of distinct viable alternatives.
- **Audit:** Checks actual work against requirements using observable evidence. It is not merely a critical opinion.

## Design principles

1. Use the simplest method likely to meet the task's quality needs.
2. Preserve independent first-pass conclusions before sharing opinions.
3. Treat agreement as a signal to inspect, never as proof.
4. Evaluate claims using evidence, logic, constraints and reproducible checks.
5. Preserve material disagreement and uncertainty; do not manufacture consensus.
6. Do not claim independent model diversity when sessions share the same model.
7. Do not claim isolation beyond what the host runtime actually provides.
8. Keep work read-only by default. Obtain authorization before consequential side effects.
9. Reuse the user's existing skills, agents and tools; do not duplicate specialist workflows.
10. Measure whether collaboration improves outcomes enough to justify cost and latency.

## Contents

- `skills/`: 13 Agent Skills-compatible skill directories.
- `skills/agent-collab/references/`: shared methodology, routing, protocols, evidence, safety and adapter guidance.
- `skills/agent-collab/templates/`: reusable task, participant, challenge, evidence and report templates.
- `evaluation/`: acceptance tests, representative test cases and an evaluation scorecard.
- `DESIGN_AUDIT.md`: final design audit and known limitations.
- `INSTALL_AGENTCOLLAB.md`: standalone installation and environment-audit prompt.
- `MANIFEST.md`, `FILE_INVENTORY.md`, `CHANGELOG.md`: package records.

## Installation

Give `INSTALL_AGENTCOLLAB.md` and this resource pack to your local agent. The installer must inspect the actual host, version, existing skill locations, commands, agents and integrations before changing anything. It must avoid overwrites and report installation, discovery, invocation and operational testing as separate states.

Do not assume that a skill being present means that subagent spawning, external communication or the full workflow is operational.
