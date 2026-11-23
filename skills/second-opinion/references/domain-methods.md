# Domain Methods

Domain methods define what to examine and how to judge the result. They do not require a specific collaboration topology. The universal router may combine methods. Reuse the user's existing specialist skills and agents; do not recreate or replace them.

## Research

- Convert the question into explicit claims and subquestions.
- Establish source hierarchy appropriate to the subject.
- Search authoritative and primary sources first.
- Check dates, versions, original publication and method.
- Track source provenance and duplicate sourcing.
- Seek disconfirming evidence and competing interpretations.
- Distinguish documented facts, interpretations, assumptions and unknowns.
- Verify important claims with primary sources where possible.
- Do not present search snippets as full-source verification.

The same central question is given to independent swarm participants. Do not automatically silo one participant into one source category; use targeted source checks after the first pass where needed.

## Engineering and architecture

- Inspect the actual repository and authoritative requirements before making claims about implementation.
- Distinguish proposed design from implemented behavior.
- Check interfaces, data flow, state ownership, concurrency, failure handling, migrations, observability, performance, maintainability and deployment constraints as relevant.
- Compare alternatives using the user's requirements and environment.
- Prefer official current docs and reproducible proof for framework/runtime claims.
- In review mode, remain read-only. Do not modify code unless explicitly authorized.
- When implementation is requested, route execution through the user's existing engineering/workflow skills. SecondOpinion itself remains the independent review/verification layer.
- Verify implementation by inspecting diffs and running appropriate tests; do not accept an implementer's completion statement as proof.

## Security

- Establish scope, assets, trust boundaries and authorization before testing.
- Identify threats, attack surfaces, abuse cases, failure paths and security assumptions.
- Distinguish theoretical concern from observed vulnerability.
- Prefer safe source inspection and controlled validation.
- Do not exploit systems, access data, perform scans or modify controls without explicit authorization and a clearly bounded scope.
- Avoid exposing secrets or security-sensitive details to external participants.
- Recommend mitigations and verification criteria; do not claim a fix is effective until validated.

## Product and UX

- Start from user problem, target users, context and observed evidence.
- Distinguish user-provided facts, research evidence, assumptions and product hypotheses.
- Examine desirability, usability, accessibility, feasibility, viability, scope and differentiation as relevant.
- Do not invent analytics, user interviews, conversion data or market facts.
- Challenge complexity and distinguish core product value from optional features.
- Use actual usability evidence when available; otherwise identify what requires validation.

## Decision analysis

- Define the decision and decision owner.
- Establish criteria and constraints before scoring options.
- Separate must-haves from preferences.
- Generate materially different viable options before evaluating.
- Compare evidence, costs, benefits, reversibility, dependencies, risk and uncertainty.
- Avoid false precision in weighted scores; explain judgments and sensitivity.
- Identify what new evidence could change the decision.
- Preserve conditional recommendations when no option dominates.

## Acceptance audit

- Obtain the actual artifact and authoritative requirements.
- Translate each requirement into an observable acceptance condition.
- Inspect and test the actual result.
- Map each requirement to evidence.
- Report pass, partial, fail, not verified, blocked or not applicable.
- Separate defects from evidence gaps.
- Do not accept plans, intentions or self-reported completion as proof of implementation.
