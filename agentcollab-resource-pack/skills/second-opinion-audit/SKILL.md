---
name: second-opinion-audit
description: Perform an evidence-based acceptance audit of an actual artifact, implementation, research pack or deliverable against authoritative requirements. Use when the user needs proof of what passes, fails or remains unverified.
---

# /second-opinion-audit — Acceptance and Evidence Audit

## Purpose

Determine whether an actual deliverable satisfies explicit requirements. This is not a general opinion or a plan review.

## Workflow

1. Identify the exact artifact/version/revision to audit.
2. Obtain authoritative requirements and source-of-truth hierarchy.
3. Convert each requirement into observable acceptance criteria.
4. Inspect the actual files, implementation, outputs or environment.
5. Perform appropriate safe tests or reproducible checks when authorized.
6. Map every requirement to evidence.
7. Classify each item as PASS, PARTIAL, FAIL, NOT VERIFIED, BLOCKED or NOT APPLICABLE.
8. Identify contradictions, evidence gaps and scope limits.
9. Produce an overall verdict only if the criteria justify it.

## Rules

- A proposal, checklist, assertion or implementation plan is not evidence of completion.
- Do not claim files were inspected or tests were run if they were not.
- Do not treat an untested assumption as PASS.
- Keep defects separate from evidence gaps.
- Preserve exact artifact version and source-of-truth references.
- Do not modify the artifact during an audit unless separately authorized.

## Report

Use `../second-opinion/templates/audit-matrix.md` and report overall verdict, requirement-level evidence, failures, partials, not-verified items, blockers and scope limitations.
