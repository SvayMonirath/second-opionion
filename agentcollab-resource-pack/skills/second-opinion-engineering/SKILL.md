---
name: second-opinion-engineering
description: Apply SecondOpinion's engineering review methodology to software architecture, codebases, technical designs, debugging or implementation acceptance. Reuse the user's existing engineering skills and avoid unauthorized edits.
---

# /second-opinion-engineering — Engineering Shortcut

## Purpose

Provide independent examination and verification of an engineering question. This skill does not replace the user's implementation, architecture or software-development workflows.

## Method

1. Identify the actual repository, branch, commit and environment where relevant.
2. Read authoritative requirements, architecture decisions and source-of-truth documents.
3. Inspect actual code and configuration before making implementation claims.
4. Evaluate interfaces, state/data flow, concurrency, error handling, persistence, security boundaries, testability, observability, performance, maintainability and deployment constraints as relevant.
5. Identify competing design options and their requirements fit.
6. Verify framework/tool behavior with current official documentation and actual environment where possible.
7. Inspect tests, run safe tests only when authorized and record exact results.
8. Separate proposed design, implemented behavior and verified runtime behavior.

## Collaboration guidance

All internal swarm participants examine the same engineering question; they do not become separate implementation workers. Keep repository access read-only by default. Reuse existing engineering/repository skills for deeper implementation tasks. If the user asks for changes, clarify the authorized scope and use the established implementation workflow separately.

## Report

State inspected commit/environment, requirements, important findings, evidence, reproducible checks, risks, unverified claims and recommended changes. Never state that code passes without actual test evidence.
