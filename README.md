# SecondOpinion (`second-opinion`)

> Evidence-led adversarial peer review, falsification, and multi-agent reality checks for AI coding agents.

`SecondOpinion` is a modular skill pack for Google Antigravity, Gemini CLI, Claude Code, and compatible agent runtimes. It replaces single-agent guesswork and sycophancy with structured peer review, isolated blind subagent swarms, falsification challenges, and acceptance audits.

---

## The Core Problem It Solves

- **The "Yes-Man" Flaw**: Single AI agents often validate flawed architectures because they default to agreeable, cooperative responses.
- **Tunnel Vision**: Once an agent starts down a sub-optimal technical path in its first paragraph, it rarely re-evaluates its assumptions.
- **Unverified Claims**: Without structured challenge, marketing metrics and superficial research are frequently accepted at face value.

---

## How It Works

Instead of asking one model to "think carefully", `SecondOpinion` orchestrates a structured review protocol:

1. **Neutral Task Framing**: The coordinator presents the problem without tipping off its preferred answer.
2. **Blind First-Pass Submissions**: Subagents analyze the assignment in separate, isolated memory spaces without seeing peer responses.
3. **Cross-Examination**: Once initial submissions are locked, targeted challenge packets are distributed to probe edge cases and failure modes.
4. **Evidence-Based Adjudication**: Claims are verified against source code, documentation, or calculations. Truth is never determined by majority vote.

---

## Slash Command Catalog

You only need to remember `/second-opinion`. It routes tasks automatically. You can also invoke direct shortcuts:

### Core Analysis
- `/second-opinion` — Universal router for any architectural question, proposal, or dilemma.
- `/second-opinion-challenge` — Red-team an idea: hunts for fatal flaws, edge cases, and hidden assumptions.
- `/second-opinion-paths` — Explores 2–3 materially different technical architectures before writing code.
- `/second-opinion-audit` — Audits files, PRs, or deliverables against strict acceptance requirements.
- `/second-opinion-swarm` — Coordinates an internal panel of subagents with withheld first passes.
- `/second-opinion-perspectives` — Single-agent multi-lens review across maintainability, performance, security, and UX.

### Domain Shortcuts
- `/second-opinion-engineering` — Architecture review, code smells, refactoring risks, and concurrency pitfalls.
- `/second-opinion-security` — Threat modeling, permission boundary audits, and security vulnerability reviews.
- `/second-opinion-research` — Fact-checking, claim-evidence matrices, and primary source verification.
- `/second-opinion-product` — Problem framing, user experience, and feature necessity audits.
- `/second-opinion-decision` — Multi-criteria trade-off matrices for major technology choices.
- `/second-opinion-connect` — Discovers available local CLIs, MCP servers, and external agent bridges.

---

## Repository Structure

```text
.
├── README.md
├── .gitignore
└── agentcollab-resource-pack/
    ├── README.md
    ├── CHANGELOG.md
    ├── FILE_INVENTORY.md
    ├── evaluation/
    └── skills/
        ├── second-opinion/             # Universal router, shared references & templates
        ├── second-opinion-swarm/       # Blind subagent review protocol
        ├── second-opinion-challenge/   # Falsification & red-teaming
        ├── second-opinion-paths/       # Architectural alternatives
        ├── second-opinion-audit/       # Acceptance criteria auditing
        ├── second-opinion-perspectives/# Single-agent multi-lens analysis
        ├── second-opinion-engineering/ # Code & architecture shortcut
        ├── second-opinion-security/    # Threat modeling shortcut
        ├── second-opinion-research/    # Evidence & fact-checking shortcut
        ├── second-opinion-product/     # Product & UX shortcut
        ├── second-opinion-decision/    # Trade-off evaluation shortcut
        ├── second-opinion-connect/     # Local/remote tool discovery
        └── second-opinion-external/    # Cross-model external collaboration
```

---

## Local Installation in Antigravity / Gemini

Skills are registered via symlinks into:
- `~/.gemini/config/skills/`
- `~/.gemini/antigravity-cli/skills/`
- `~/.agents/skills/`

Because the installation uses symlinks to this repository, running `git pull` in this folder immediately updates all skills in your AI runtime.
