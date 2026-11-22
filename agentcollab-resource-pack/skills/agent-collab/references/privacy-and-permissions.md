# Privacy, Permissions and Side Effects

## Default posture

- Read-only unless the user authorizes a specific change or action.
- Minimum necessary context for every participant.
- No credentials, API keys, secrets or unrelated personal/project information in task briefs.
- No external disclosure without authorization.
- No destructive or consequential action merely because a participant recommends it.

## Internal participants

Separate context does not automatically provide operating-system security isolation. Confirm actual tool permissions and workspace behavior. Do not give internal subagents broader access than the task requires. Prevent nested spawning unless explicitly needed. Prefer read-only source inspection and tests that do not alter user data.

## External participants

Before sending, identify what information will leave the local host, where it will go, and the relevant provider/account/endpoint. Ask for explicit approval when confidential, private, proprietary or otherwise sensitive content is involved or when the user's intent is unclear.

Never silently upload an entire repository or conversation. Redact or minimize context where feasible.

## Side effects requiring explicit approval

Unless the user has specifically authorized the relevant operation, do not:

- edit, delete, move or overwrite files;
- commit, push, merge or create a release;
- deploy or change production systems;
- purchase, subscribe, send or publish;
- alter permissions, credentials, environment variables or hooks;
- install packages, plugins, servers or integrations;
- run intrusive security tests or access systems outside scope;
- send messages or data to external models/agents.

## Approval record

Record what was authorized, by whom (in the conversation context), the allowed scope and any limits. If a task expands materially, pause before the new side effect.

## Reports

Disclose missing permissions, shared workspace limitations, actual external data transfers and unperformed checks. Never imply a security boundary that the runtime does not provide.
