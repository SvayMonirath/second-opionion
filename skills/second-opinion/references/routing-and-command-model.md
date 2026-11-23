# Routing and Command Model

## Product and skill naming

- Product brand: **SecondOpinion**.
- Canonical skill namespace: `second-opinion`.
- Every slash command begins `/second-opinion`.
- Agent Skills skill identifiers use lowercase kebab-case and match their directory names. Do not use CamelCase in the technical `name` field.

## Main command

`/second-opinion` is the default entry point. The user should not need to understand orchestration topology, provider adapters or domain methods to use it.

## Command catalog

| Skill/command | Core distinction |
|---|---|
| `second-opinion` | Chooses and coordinates the overall method. |
| `second-opinion-swarm` | Multiple separate sessions of the same current model examine the same assignment and challenge/verify one another. |
| `second-opinion-external` | Real external model/agent interaction across providers or runtimes. |
| `second-opinion-perspectives` | One session performs several analytical passes. |
| `second-opinion-challenge` | Examines one specified proposal/claim for defects. |
| `second-opinion-paths` | Generates and compares materially different solutions. |
| `second-opinion-audit` | Checks a real artifact against authoritative requirements. |
| `second-opinion-connect` | Inspects available communication capabilities and their status. |
| `second-opinion-research` | Adds research-specific evidence and source methodology. |
| `second-opinion-engineering` | Adds engineering-specific review criteria and reuses existing engineering workflow. |
| `second-opinion-security` | Adds threat/risk and authorized validation criteria. |
| `second-opinion-product` | Adds user/problem/product/UX evidence criteria. |
| `second-opinion-decision` | Establishes criteria and compares choices/trade-offs. |

## Routing procedure

1. Parse what the user wants, not merely which nouns appear in the prompt.
2. Determine whether the task requires a direct answer, generation, independent review, comparison, research, implementation inspection or formal acceptance.
3. Select domain methodology separately from collaboration topology.
4. Assess consequence of error, uncertainty, complexity, value of independent assessment, availability of evidence, privacy, cost and latency.
5. Choose the least complex adequate method.
6. Tell the user briefly when a requested mode is unavailable or would not add value.

## Practical mode-selection matrix

| Task condition | Preferred mode | Reason / guardrail |
|---|---|---|
| Low consequence, clear request, little uncertainty | Direct/solo | More participants are unlikely to add value. |
| User wants several analytical angles quickly | Perspectives | One execution; explicitly not independent agents. |
| Important conclusion, multiple plausible interpretations, and true separate sessions available | Internal swarm | Independent first opinions followed by targeted verification. |
| User explicitly asks for another provider, or provider/model diversity is important | External | Requires a real authorized connection. |
| Both internal peer review and provider diversity materially add value | Hybrid | Use only when privacy, cost and latency justify both. |
| Existing answer/proposal needs adversarial testing | Challenge | Focuses on falsifying a target rather than generating a fresh project plan. |
| Solution space is unclear and multiple viable approaches may exist | Paths | Develop distinct options before selecting. |
| Actual artifact must meet formal requirements | Audit | Requirement-to-evidence mapping and observable checks. |

Do not use arbitrary fixed complexity scores or a fixed swarm threshold as if they were empirically universal. Explain the reason for a mode choice briefly when the choice affects cost, latency, privacy or the user's expectations.

## Decision rules

- A simple factual/transformative task normally needs no swarm.
- A proposal needing more than one plausible assessment may use perspectives or challenge.
- A complex, consequential conclusion may justify internal swarm if separate sessions and first-pass privacy are supported.
- A task requiring diverse provider perspectives may justify external collaboration if the real channel exists and sharing is authorized.
- A final deliverable that must meet requirements may need an audit, regardless of whether it was produced with a swarm.
- A request for several possible solutions should use paths before prematurely selecting one.
- A user explicitly naming a mode should normally be honored, but capability and safety limitations must be stated.

## Avoiding command overlap

- **Perspectives vs swarm:** one session with multiple lenses vs multiple actual sessions with independent contexts.
- **Swarm vs external:** same current model in separate sessions vs other provider/model/agent endpoints.
- **Challenge vs audit:** critique a target vs verify a deliverable against explicit criteria.
- **Paths vs perspectives:** distinct solution candidates vs different ways to analyze a question.
- **Research shortcut vs research team:** domain method applies to the whole collaboration; it does not mean each participant receives a different subtopic by default.
- **Domain methods vs topology:** research/security/engineering/product describe how to judge the subject, not who must be spawned.

## User invocation language

Natural language after the slash command is the task. Examples:

```text
/second-opinion Review my proposed architecture and verify the important assumptions.
/second-opinion-swarm Independently examine whether this approach is justified; challenge and verify it.
/second-opinion-external Ask Claude to independently review this proposal, if a supported connection is available.
/second-opinion-perspectives Evaluate this question from several distinct analytical lenses.
/second-opinion-challenge Find material reasons this plan could fail.
/second-opinion-paths Develop three genuinely different ways to solve this problem.
/second-opinion-audit Check this deliverable against the attached acceptance criteria.
/second-opinion-connect Inspect which collaboration transports are installed and authenticated.
```

Any `--with`, `--model`, `--conversation`, `--session`, `--rounds` or `--read-only` text is a user hint, not guaranteed parser syntax. Interpret only when supported by the host and never imply that optional flags are implemented by every CLI.
