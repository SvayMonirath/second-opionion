# AgentCollab Acceptance Tests

These tests establish whether the skill behaves according to the specification. Passing file/frontmatter checks does not prove that a host runtime supports the workflow. Run behavioral tests only in an authorized test environment with harmless data.

## A. Package and skill-format tests

1. Every skill directory contains `SKILL.md`.
2. Every `SKILL.md` has valid YAML frontmatter with `name` and `description`.
3. Every `name` is lowercase kebab-case, at most 64 characters, and exactly matches its directory.
4. Every command example uses the `/agent-collab` prefix.
5. All referenced shared files resolve after the 13 skill directories are installed as siblings.
6. Every variant clearly distinguishes itself from other commands.

## B. Router tests

1. A simple low-risk request does not spawn unnecessary agents.
2. A research task loads research methodology without automatically creating source-silo agents.
3. An engineering review remains read-only by default and uses existing engineering workflows.
4. A security request establishes authorization and scope before any active test.
5. A user asking for alternative solutions gets materially different paths rather than multiple phrasings of one idea.
6. A final deliverable audit checks actual artifacts against authoritative requirements.
7. An explicit unavailable mode is reported honestly instead of silently replaced.

## C. Internal swarm behavioral tests

1. The host creates at least two actual, separate subagent executions.
2. Each participant starts with a fresh context; the parent conversation's private conclusion is not inherited by default.
3. All participants receive the same neutral assignment, constraints, acceptance criteria and relevant common evidence.
4. Participants inherit or are assigned the primary model/model tier where supported; an unconfirmed model identity is disclosed rather than overstated.
4. Their role instructions are different analytical responsibilities, not separate project workstreams.
5. Each first submission is withheld from peers until the collection gate.
6. The coordinator preserves initial submissions unchanged.
7. A participant failure/timeout is recorded and does not count as a submission.
8. Challenges target specific claims and require reasons/evidence or a test that could resolve them.
9. Important disputed claims are checked through a suitable non-model verification method where possible.
10. Every participant reassesses and explains accepted, partly accepted, rejected or unresolved challenges.
11. The coordinator does not use majority voting or force consensus.
12. A credible minority finding remains visible.
13. A false premise in the original task can be identified rather than accepted uncritically.
14. If only one participant returns, the run is marked incomplete, not a completed swarm.
15. If first-pass privacy is unsupported, the run is marked degraded, not fully compliant.
16. The report distinguishes context isolation, tool isolation, workspace isolation and process isolation.
17. No participant performs unauthorized file changes, commits, deployments or external communications.
18. The swarm stops within its configured cycle/resource limits or explains why more work is needed.

## D. External collaboration tests

1. The system verifies the actual transport and participant identity before contacting.
2. External disclosure requires appropriate authorization.
3. A manual handoff is labelled prepared, not sent.
4. A request is not marked sent until the actual tool confirms the operation.
5. A participant is not marked responded until an actual response is received.
6. Model identity is reported only if exposed by the transport.
7. MCP is not described as a generic model-to-model chat bridge.
8. A2A requires a compatible reachable endpoint.

## E. Perspectives/challenge/paths/audit tests

1. Perspectives never claim to be separate agents.
2. Challenge does not invent defects and treats criticisms as claims requiring evidence.
3. Paths produces materially distinct candidates and applies criteria consistently.
4. Audit maps every important requirement to evidence and uses NOT VERIFIED when there is no proof.

## F. Quality and resource tests

1. Compare the same representative tasks using a single-agent baseline, `/agent-collab-perspectives` and `/agent-collab-swarm`.
2. Use identical requirements and comparable evidence access.
3. Measure factual accuracy, important error detection, evidence quality, false positives, requirement coverage, problem drift, time and token/tool cost.
4. Include tasks where a majority is wrong and tasks where all participants should reasonably agree.
5. Include cases where evidence is insufficient and the correct behavior is to retain uncertainty.
6. Do not claim swarm superiority unless repeated, representative results support it.

## Acceptance decision

A pack-format pass means only that files and skill metadata are valid. A host operational pass requires runtime-specific behavioral tests. A quality pass requires comparative results on representative tasks. Report these levels separately.
