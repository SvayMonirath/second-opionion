# Runtime Adapters and Capability Discovery

## Why an adapter is needed

SecondOpinion defines the collaboration protocol. Each host runtime has its own skill discovery, slash command, subagent, context, tool, concurrency and workspace semantics. The adapter maps the protocol to verified host capabilities. Never assume that two hosts implement the same feature in the same way.

## Capability matrix

Before execution, inspect and record:

- host application and version;
- Agent Skills support and skill search paths;
- how slash commands are derived/registered;
- how separate agent executions are spawned;
- whether subagents receive fresh contexts;
- whether subagents inherit or can be assigned the same model/model tier as the primary agent;
- whether they can run concurrently;
- whether first-pass outputs can remain private;
- tool and permission restrictions;
- workspace/filesystem isolation;
- external model/agent transports;
- resource limits and failure/timeout behavior.

## Host notes (verify against installed version)

### Antigravity CLI

Official docs describe Agent Skills and CLI slash invocation based on skill names. The CLI also documents custom subagents with a dedicated context, and separate workspace modes such as inherited workspace, branch/worktree or shared workspace. It has a native `/swarm` workflow oriented around coordinated task splitting and a shared board. That native `/swarm` must not be presumed equivalent to SecondOpinion's private-first-pass peer-review protocol. Inspect the installed version's current documentation and actual tool signatures before invoking subagents.

### Gemini CLI

Official docs describe Agent Skills in user/workspace locations and subagents with focused contexts and configurable tool access. Search paths and aliases may differ by version. Inspect active `/skills` discovery behavior and the installed CLI's subagent interface.

### Claude Code

Official docs describe Agent Skills in user and project directories and custom subagents with separate context windows and configurable tools/permissions. Confirm actual version and concurrency/agent behavior. A skill folder generally becomes a slash-invocable skill name, but test it in the installed host.

### Other runtimes

Use their current official documentation and tool schemas. Do not infer support from another runtime.

## Important distinctions

- **Skill installed:** files exist at a path.
- **Skill discovered:** host lists or loads it.
- **Command invocable:** slash invocation successfully starts the skill.
- **Subagent spawn supported:** host can create another execution.
- **Context isolated:** subagent lacks parent's private history by default.
- **First-pass private:** peer submissions remain hidden until collection gate.
- **Tool restricted:** subagent's available actions are explicitly bounded.
- **Workspace isolated:** filesystem changes are separated by host-supported mechanisms.
- **Operational:** actual behavior passed a test.
- **External connected:** a real external request/response path was authenticated and tested.

Do not collapse these into one “works” status.

## Native swarm caution

A host's built-in `/swarm` may be an excellent task-delegation tool, but if it uses a shared board or exposes peer updates immediately, it does not satisfy the SecondOpinion requirement that independent first submissions remain private until collected. Use it only if its actual behavior can satisfy the required protocol; otherwise use the lower-level isolated subagent interface if available.

## Adapter failure behavior

If a feature is unavailable, record the missing capability and select a truthful alternative:

- no subagent spawn -> explain and offer single-agent perspectives;
- no private first pass -> mark swarm degraded, do not claim full independence;
- no external transport -> prepare manual handoff, mark not sent;
- no tool access -> mark claims unverified;
- no workspace isolation -> maintain read-only mode or request appropriate approval.
