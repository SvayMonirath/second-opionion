# Installation and Environment-Audit Prompt — AgentCollab 2.0.0

Give this prompt and the complete AgentCollab resource-pack directory to your local AI coding agent (for example, Antigravity CLI, Gemini CLI or Claude Code). The agent must inspect the actual environment before modifying anything.

---

## Role

Act as a senior agent-runtime integrator and cautious configuration auditor. Your task is to inspect the current environment, determine how AgentCollab can be installed safely, install only what is compatible and authorized, and prove what is and is not operational.

## Primary objective

Install the AgentCollab skill system from the supplied resource pack while preserving the user's existing skills, agents, slash commands, frameworks, hooks, permissions, MCP servers, A2A endpoints and configuration.

**Do not begin by copying files. Begin with a read-only audit.**

## Non-negotiable rules

1. Never overwrite, delete, rename, disable or silently replace existing files, commands, skills, agents, hooks, settings or integrations.
2. Never assume a path, host version, CLI capability, integration, model identity or permission. Inspect it.
3. Do not install dependencies, MCP servers, browser tools, plugins or provider clients unless separately authorized.
4. Do not send messages to external models or disclose project material during installation tests.
5. Do not modify global instructions, shell profiles, hooks, permissions, environment variables, MCP/A2A configuration or unrelated repositories without explicit approval.
6. Do not claim that a slash command works until it has been discovered/invoked in the actual host.
7. Do not claim that `/agent-collab-swarm` is operational until separate contexts, locked first-pass submissions and the required coordination behavior have been tested.
8. If a capability is missing, document the limitation. Do not simulate success.
9. Keep all changes reversible. Record exact destination paths and files created.
10. If a name collision exists, stop that item and present a safe resolution. Do not overwrite.

## Phase 1 — Identify the runtime

Read-only inspection:

- Identify the current host application and executable(s): Antigravity CLI (`agy`), Gemini CLI, Claude Code or another runtime.
- Record exact installed versions and the current project/workspace root.
- Identify which host is active in this session and which other hosts are merely installed.
- Inspect the host's current documentation or built-in help for Agent Skills, skill discovery, slash command behavior, subagents, invocation APIs, concurrency, context isolation, tool restrictions and workspace isolation.
- Do not infer support from another product or another version.

Deliver a host capability matrix with evidence (command output, official docs or local config) for:

| Capability | Supported? | How verified | Limitations |
|---|---|---|---|
| Agent Skills-compatible skill discovery | | | |
| Slash invocation from skill name | | | |
| User/global skill location | | | |
| Workspace/project skill location | | | |
| Spawn separate subagent execution | | | |
| Fresh context per subagent | | | |
| Same-model/model-tier inheritance or selection | | | |
| Parallel subagent runs | | | |
| Hide/withhold initial submissions | | | |
| Restrict subagent tools/permissions | | | |
| Isolated workspace/worktree | | | |
| External model/agent transport | | | |

## Phase 2 — Audit existing setup

Inspect relevant locations only after confirming they exist. Potential locations vary by host/version and are discovery candidates, not assumed installation targets:

- Antigravity CLI: `~/.gemini/config/skills/`, workspace `.agents/skills/`, or another version-specific location.
- Gemini CLI: `~/.gemini/skills/`, `~/.agents/skills/`, workspace `.gemini/skills/` or `.agents/skills/`.
- Claude Code: `~/.claude/skills/` and project `.claude/skills/`.
- Other hosts: their documented compatible skill directories.

Also inspect, read-only, existing:

- skills and descriptions;
- slash commands and command registries;
- subagent/agent definitions;
- user and project instruction files;
- installed plugins/extensions;
- MCP servers and configuration;
- A2A agents/endpoints, if any;
- existing orchestration and workflow systems;
- existing frameworks and skill packs such as ECC, Superpowers, Impeccable or user-created systems;
- overlapping capabilities already covering collaboration, research, coding, review, audit or browser work.

The user's environment has historically included a substantial `.gemini` setup and a shared `.agents/skills/` directory, plus existing frameworks and commands. Treat this as a reason to inspect carefully, not as proof of current state. Do not ask the user to repeat information that can be inspected.

Create an inventory with:

- path/name;
- purpose;
- scope (global/user/project);
- enabled/discovered status;
- overlap with AgentCollab;
- whether AgentCollab should reuse, reference, adapt, skip or install alongside it.

Do not change any existing item in this phase.

## Phase 3 — Collision and placement plan

The product brand is **AgentCollab**. The canonical technical skill namespace is `agent-collab`.

The pack contains 13 skill directories. Every directory name must exactly match its YAML frontmatter `name` value:

1. `agent-collab`
2. `agent-collab-swarm`
3. `agent-collab-external`
4. `agent-collab-perspectives`
5. `agent-collab-challenge`
6. `agent-collab-paths`
7. `agent-collab-audit`
8. `agent-collab-connect`
9. `agent-collab-research`
10. `agent-collab-engineering`
11. `agent-collab-security`
12. `agent-collab-product`
13. `agent-collab-decision`

Every user-facing slash command must use the same prefix: `/agent-collab...`. Do not create unprefixed AgentCollab aliases.

Select the best shared/user or project-level skill location for the active host. Prefer a shared user-level location only if that host officially supports it and it does not duplicate a skill already shared across runtimes. If user asks for project-only installation, use the project's skill scope. Explain the scope and trade-off before installing.

Check for collisions by both directory name and command name. If any of the 13 names already exist:

- inspect the existing skill's full contents and purpose;
- compare it with the AgentCollab version;
- do not overwrite or silently merge;
- report the exact collision and propose options (reuse existing, install non-conflicting subset, install under an explicitly approved alternate name, or wait for user decision).

Do not install multiple copies into Antigravity and Gemini if they resolve to the same shared skill directory. Avoid duplicate registration.

## Phase 4 — Installation plan and approval gate

Prepare a concise plan containing:

- chosen host and version;
- chosen skill root and scope;
- all 13 intended skill directories;
- existing overlaps and collisions;
- any host-specific adaptation required;
- any files to be created or modified;
- whether any change outside new skill directories is required.

If installation requires changes to existing files/configuration, global instructions, hooks, agents, permissions, MCP/A2A, plugins or shell settings, stop and request explicit user approval for those specific changes. New, non-conflicting skill directories may be installed if the user has authorized the installation task and the target paths are confirmed safe.

## Phase 5 — Install the skills

- Copy the complete `skills/` contents as sibling directories under the selected skill root.
- Preserve the directory names exactly.
- Preserve each `SKILL.md` frontmatter and all reference/template files.
- Keep `skills/agent-collab/` and the 12 variant directories as siblings; shared material is under `agent-collab/references/` and `agent-collab/templates/`.
- Verify every internal relative path resolves after installation.
- Do not install documentation files into skill roots unless host requires them.
- Do not copy over any existing files.

## Phase 6 — Register and verify commands

The intended command set is:

- `/agent-collab` — universal router; the main command users should remember.
- `/agent-collab-swarm` — isolated internal same-model peer-review collaboration.
- `/agent-collab-external` — actual external model/agent collaboration.
- `/agent-collab-perspectives` — one-agent multi-perspective analysis.
- `/agent-collab-challenge` — focused critical challenge.
- `/agent-collab-paths` — materially different solution paths.
- `/agent-collab-audit` — evidence-based artifact acceptance audit.
- `/agent-collab-connect` — capability and integration discovery.
- `/agent-collab-research` — research shortcut.
- `/agent-collab-engineering` — engineering shortcut.
- `/agent-collab-security` — security shortcut.
- `/agent-collab-product` — product/UX shortcut.
- `/agent-collab-decision` — decision-analysis shortcut.

Use the active host's documented skill invocation mechanism. Do not assume a slash command is registered solely because the folder exists. If the host automatically exposes a skill as a slash command, verify discovery. If it requires a separate command registry, explain the additional step and request authorization before editing that registry.

Test at minimum:

1. list/discover skills;
2. invoke `/agent-collab` with a harmless read-only task;
3. invoke `/agent-collab-swarm` only if the host supports separate subagent sessions and it is safe to test;
4. verify all variant names are discovered or report why not;
5. reload/restart only if the host requires it and the user authorizes it.

## Phase 7 — Operational test for `/agent-collab-swarm`

Do not mark the swarm operational based only on a skill file being installed.

Use a harmless task such as “independently assess whether a 4-day workweek has evidence of productivity effects; report uncertainty” or another low-risk, source-checkable question. Do not use confidential project details.

Verify:

- at least two separate subagent executions were actually created (three preferred);
- each has a fresh context rather than inheriting the parent's conversation;
- each uses the primary model/model tier where the host supports explicit inheritance/selection, and any inability to confirm this is disclosed;
- all receive the same neutral assignment and source material;
- their first submissions are withheld from peers until all initial submissions are recorded;
- the coordinator preserves the first submissions;
- targeted challenges are distributed only after that point;
- participants can reassess and explain changes;
- the final synthesis does not use majority voting;
- the host reports model identity and tool/workspace isolation only to the extent observable.

If the host cannot withhold first submissions, report that limitation and do not describe the implementation as fully compliant with the AgentCollab swarm protocol. If the only available native swarm is a task-splitting shared-board swarm, do not treat it as equivalent.

## Phase 8 — External integration readiness

Inspect possible API, CLI, browser, MCP or A2A capabilities, but do not contact external parties or configure credentials without authorization.

Remember:

- MCP is not automatically a model-to-model communication bridge.
- A2A requires a compatible reachable endpoint.
- Browser conversation titles are hints, not unique identifiers.
- A prepared manual handoff is not an external response.
- Never claim external collaboration until an actual request was sent and an actual response was received.

## Phase 9 — Final report

Provide a precise report with separate statuses:

- **Audited:** what existing environment was inspected.
- **Installed:** exact new skill directories and paths.
- **Discovered:** which skills the host lists.
- **Invocable:** which slash commands were actually invoked.
- **Operational:** which workflows passed behavioral tests.
- **Connected:** which external transports are authenticated and tested.
- **Not available:** unsupported capabilities and reasons.
- **Skipped:** overlapping skills or collisions intentionally left alone.
- **Changed:** all created/modified files, with reversible steps.
- **Needs approval:** any recommended changes not made.

Never collapse these statuses into a single word such as “installed” or “working”.

## Expected result

The user should be able to use `/agent-collab` as the normal entry point. The other prefixed commands are optional. Existing specialist workflows remain intact and are reused rather than replaced. The swarm is only declared functional when true separate sessions and the privacy of initial submissions have been demonstrated.

---
