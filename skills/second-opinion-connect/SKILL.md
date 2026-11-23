---
name: second-opinion-connect
description: Inspect the current environment for real internal subagent and external agent/model communication capabilities. Verify paths, versions, schemas, authentication and reachability without installing, changing settings or sending messages unless authorized.
---

# /second-opinion-connect — Capability and Integration Discovery

## Purpose

Establish what the active environment can actually do. This command discovers and tests permitted capabilities; it does not create them.

## Workflow

1. Identify active host, exact version and current workspace.
2. Inspect documented skill, subagent, tool, permission and connection interfaces.
3. Discover installed agents, CLIs, plugins, APIs, MCP servers, A2A endpoints and browser integrations where visible.
4. Inspect authentication and permission state without revealing credentials.
5. Distinguish capability discovered from authentication, reachability, invocation and successful test.
6. Run only harmless, read-only tests within existing permissions.
7. Ask before installing dependencies, plugins, servers, changing configuration or contacting an external party.
8. Produce an integration matrix with evidence and limitations.

## Required distinctions

- Installed is not necessarily enabled.
- Discovered is not necessarily authenticated.
- Authenticated is not necessarily reachable.
- Reachable is not necessarily permitted for this task.
- A tool is not necessarily an agent.
- MCP access is not automatically model-to-model chat.
- A2A requires a compatible reachable agent endpoint.
- Browser access does not guarantee safe/unique conversation addressing.

## Output

Use `../second-opinion/templates/integration-matrix.md`. Report capability, evidence, authentication/reachability, permissions, tests performed, unsupported features and changes that would require approval.
