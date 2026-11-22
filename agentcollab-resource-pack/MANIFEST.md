# Package Manifest

- Product: AgentCollab
- Version: 2.0.0
- Canonical skill namespace: `agent-collab`
- Format: Agent Skills-compatible skill directories with host-adaptation guidance
- Target environments: Antigravity CLI, Gemini CLI, Claude Code and other hosts that support compatible skills/subagents; capability varies by host/version.
- Contains: 13 skills, shared references, templates, evaluation suite, installation prompt and design audit.
- Does not contain: executable subagent runtime, MCP/A2A service, API credentials, provider integrations, browser automation, scripts that modify host configuration, or proof of local installation.

## Required safety and honesty posture

- All file operations during installation are subject to user authorization and host permissions.
- No existing skill or configuration may be overwritten without explicit approval.
- No external participant may be contacted without an available integration and appropriate authorization.
- No subagent may be represented as independent if it has not been spawned as a separate execution context.
- No work may be reported as verified without an actual, described verification action.

See `FILE_INVENTORY.md` for the complete contents and `DESIGN_AUDIT.md` for the design review.
