---
name: agent-collab-challenge
description: Critically examine a specified claim, answer, plan, design or implementation for material weaknesses, counterexamples, missing assumptions and failure conditions. Use when the user wants to know what may be wrong.
---

# /agent-collab-challenge — Focused Critical Review

## Purpose

Test a defined target. Do not redesign the entire project unless requested.

## Workflow

1. Identify the exact target and criteria for judging it.
2. Extract its key claims and assumptions.
3. Search for material logical gaps, counterexamples, unsupported claims, requirement conflicts, edge cases, failure paths and hidden costs.
4. Prioritize issues by consequence and evidence, not count.
5. Verify important criticisms using relevant sources, calculations, code inspection or tests.
6. Distinguish confirmed defects from plausible risks and speculative questions.
7. Recommend specific corrections or checks.

## Challenge record

For each finding state: target claim, issue, evidence, impact, severity rationale, verification status and recommended next action.

## Rules

- Do not manufacture objections.
- Do not confuse style preferences with defects.
- A criticism is itself a claim and requires support.
- Do not report a test as performed unless it was actually run.
- Preserve parts of the target that are sound.

## Report

Lead with the most consequential findings, then uncertainties and checks not performed. If no material defect is established, say what was checked and what remains outside scope.
