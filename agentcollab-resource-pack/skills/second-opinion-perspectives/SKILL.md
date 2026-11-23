---
name: second-opinion-perspectives
description: Use one AI execution to examine a question through several structured analytical perspectives without spawning subagents or contacting external models. Use for quick multi-lens reasoning when true independence is not required.
---

# /second-opinion-perspectives — Single-Agent Multi-Perspective Analysis

## Purpose

Have one current agent make several deliberate analytical passes over the same question. This is faster and simpler than spawning participants, but it is not an independent swarm.

## Workflow

1. Restate the question and evaluation criteria.
2. Identify the few analytical lenses that materially fit the task (usually 3–5, not an exhaustive persona list).
3. Perform distinct passes, each focusing on a different source of insight: for example, direct analysis, alternative explanation, skeptical review, practical feasibility and evidence check.
4. Separate conclusions, assumptions, facts and uncertainty.
5. Compare the passes and identify contradictions or blind spots.
6. Verify material facts using actual sources or tests where available.
7. Produce a synthesis and state what was not independently verified.

## Rules

- Do not claim these passes are separate agents or independent model opinions.
- Do not invent disagreement to make the answer look balanced.
- Do not rely on role labels as proof.
- Do not reveal hidden chain-of-thought; provide concise reasoning, evidence and conclusions.
- If the task requires genuine independent contexts, use `/second-opinion-swarm` only if supported.

## Report

Summarize the lenses used, conclusions each surfaced, important tensions, evidence checks, final synthesis and remaining uncertainty.
