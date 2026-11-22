---
name: agent-collab-external
description: Coordinate real external AI model, agent or human review using an available and authorized transport. Use when provider diversity is valuable or the user explicitly requests an external participant. Never simulate contact.
---

# /agent-collab-external — External Collaboration

## Purpose

Obtain independent assessments from real external providers, agents or reviewers. This is distinct from `/agent-collab-swarm`, which uses separate sessions of the current model.

## Required reading

Read `../agent-collab/references/external-collaboration-protocol.md`, `collaboration-contract.md`, `evidence-and-verification.md` and `privacy-and-permissions.md`.

## Workflow

1. Identify the requested provider/participant and why provider diversity adds value.
2. Inspect actual integrations and tool contracts. Confirm authentication, reachability, identity and permissions.
3. Confirm user authorization to disclose the necessary task material externally.
4. Prepare a neutral task brief with only relevant information.
5. Obtain independent initial responses before sharing competing opinions, where supported.
6. Preserve exact provenance: who was contacted, how, when and what response was received.
7. Distribute material competing claims for targeted challenge.
8. Independently verify important factual claims where possible.
9. Ask external participants for reassessment when the transport supports another round.
10. Synthesize evidence and disagreements without majority voting.

## Transport honesty

Possible transports include API, agent CLI, browser automation, supported application connector, A2A-compatible endpoint or manual handoff. Discover actual capability. MCP is not automatically a model-chat bridge. A2A requires compatible reachable endpoints. Browser thread titles are locator hints, not unique identity proof.

A manual handoff is **prepared, not sent**. A request is **sent** only after a real tool action succeeds. A participant is **responded** only after its actual response is received.

## Privacy and side effects

Do not upload entire conversations, repositories, secrets or private project files by default. Minimize data and obtain approval before external disclosure of sensitive/confidential content. Do not perform changes or external actions not authorized.

## Report

State actual participants, provider/model identity only if observable, transport, sent/received status, evidence quality, disagreements, verification, privacy scope and limitations. If no real external response was received, say so.
