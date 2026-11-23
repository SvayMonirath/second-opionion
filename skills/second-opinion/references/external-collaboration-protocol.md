# External Collaboration Protocol

## Purpose

Coordinate real independent assessments from external models, agents or human reviewers when provider/model diversity or a particular external capability is valuable. External collaboration is distinct from same-model internal swarm.

## Preflight

Before contacting anyone, confirm:

- the user requested or authorized external collaboration;
- an actual reachable transport exists;
- the target provider/agent and endpoint are identified;
- authentication and permissions are valid;
- the information to be shared is appropriate for that destination;
- the task brief can be sent without unnecessary private context;
- the expected benefit justifies delay, cost and disclosure.

Do not infer integration from a product name or a URL. Discover the actual available tools and schemas.

## Supported transport categories

Possible categories, depending on the host:

- provider API/client;
- installed agent CLI;
- compatible A2A endpoint;
- browser automation that can reliably address the intended account and conversation;
- connected application/plugin action;
- manual handoff prepared for the user to send.

MCP commonly exposes tools, resources or prompts to a host; it does not automatically turn any MCP server into a chat bridge to an external model. A2A is for compatible agent-to-agent interaction and requires a reachable compatible endpoint. A CLI/API/browser mechanism must be checked against its actual contract.

## Participant record

For every external participant, record what is actually known:

- provider/agent/product;
- model/version only if exposed by the integration;
- transport and endpoint/account;
- authentication/connection status;
- request sent status;
- response received status;
- timestamp if available;
- tool/data scope and limitations.

Never claim a provider/model identity based only on the user's label if the actual connection cannot be verified.

## Independent first pass

Send the same neutral brief to each external reviewer when independent first opinions are needed. Do not include other participants' conclusions or the primary's preferred answer. Request a structured response with conclusion, key claims, evidence, assumptions, counterarguments, uncertainty and what could change its position.

A visible browser conversation title is only a locator hint, not proof of a unique conversation. Verify the signed-in account, product, intended conversation and active context before sending. A pre-existing conversation may contain prior anchoring; describe that limitation and prefer a clean context when available.

## Challenge and reassessment

After initial responses are received, share relevant competing claims and invite targeted challenges. Verify disputed claims independently where practical. Ask participants to reassess after seeing the evidence. Retain the distinction between independent first responses and later influenced responses.

## Manual handoff

If no transport exists, prepare a concise handoff message for the user. Label it **prepared, not sent**. Do not describe manual handoff as external collaboration completed. When the user later supplies the response, treat it as an external submission but record that the transport was manual and its provenance is user-supplied.

## Privacy and authority

Send only information necessary for the assignment. Do not disclose secrets, credentials, personal data, private repository contents or proprietary material without explicit authorization. Respect the tool's data handling and permission scope.

## Final report

Clearly state which participants were contacted, which messages were sent, which responses were received, actual model identity if known, and what was not verified. If no external participant was reached, say so plainly. Never fabricate a response, citation, connection or model identity.
