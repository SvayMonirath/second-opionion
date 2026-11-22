---
name: agent-collab-security
description: Apply AgentCollab's security-review method to a defined system, design or implementation. Establish scope and authorization, examine threats and failure paths, and use safe validation only within permission.
---

# /agent-collab-security — Security Shortcut

## Purpose

Produce evidence-led security analysis without assuming authorization for intrusive testing. This is a review layer, not an offensive execution agent.

## Method

1. Establish authorized scope, target, environment and non-goals.
2. Identify assets, trust boundaries, actors, entry points and assumptions.
3. Develop threat scenarios and abuse cases relevant to the system.
4. Examine authentication, authorization, isolation, data handling, secrets, supply chain, logging, recovery and failure behavior as relevant.
5. Distinguish theoretical concerns, design weaknesses and demonstrated vulnerabilities.
6. Inspect source/configuration and authoritative security requirements where authorized.
7. Validate safely with non-destructive methods only within the approved scope.
8. Recommend mitigations and specific verification criteria.

## Collaboration guidance

Internal swarm participants examine the same security question from independent reasoning angles; they do not receive unrelated domain-specific subtasks. Do not share secrets or sensitive attack details with external parties unless explicitly authorized. Do not perform scanning, exploitation, credential access, persistence or destructive tests without explicit authorization and a bounded target.

## Report

Include scope, threat assumptions, findings and severity rationale, evidence status, safe validation performed, mitigations, residual risk and untested areas. Do not label a hypothetical issue a confirmed vulnerability.
