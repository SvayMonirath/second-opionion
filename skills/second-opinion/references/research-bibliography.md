# Research Bibliography and Design Basis

The links below informed this pack's design. Product documentation changes; verify the current version installed in the target environment. The research evidence informs design choices but does not establish that SecondOpinion will improve every task.

## Agent Skills and host documentation

1. Agent Skills specification. https://agentskills.io/specification — skill directory and `SKILL.md` requirements; lowercase kebab-case names and matching directory name.
2. Google Antigravity, Agent Skills. https://antigravity.google/docs/skills — skill discovery and CLI invocation behavior.
3. Google Antigravity, Custom subagents. https://antigravity.google/docs/subagents — spawning, context and workspace modes; verify installed version.
4. Google Antigravity, Swarm. https://antigravity.google/docs/swarm — native task coordination/shared-board behavior; not automatically equivalent to SecondOpinion's private-first-pass swarm.
5. Gemini CLI, Agent Skills. https://github.com/google-gemini/gemini-cli/blob/main/docs/cli/using-agent-skills.md — skill discovery and locations.
6. Gemini CLI, Subagents. https://github.com/google-gemini/gemini-cli/blob/main/docs/core/subagents.md — context/tool behavior for subagents.
7. Claude Code, Agent Skills. https://code.claude.com/docs/en/skills — skill directories and invocation.
8. Claude Code, Subagents. https://code.claude.com/docs/en/sub-agents — separate context windows and tool/permission configuration.
9. OpenAI, Orchestration. https://developers.openai.com/api/docs/guides/agents/orchestration — manager-style orchestration and handoff patterns.
10. OpenAI, Multi-agent systems. https://developers.openai.com/api/docs/guides/agents-api/multi-agent — agent collaboration and concurrency considerations.

## Agent design and empirical cautions

11. Anthropic, “Building effective agents” (19 Dec 2024). https://www.anthropic.com/research/building-effective-agents — simple composable workflow patterns; do not add complexity without a task-specific reason. The page notes that tools evolve.
12. Anthropic, “How we built our multi-agent research system” (13 Jun 2025). https://www.anthropic.com/engineering/multi-agent-research-system — one orchestrator coordinating parallel subagents for a particular internal research evaluation. Its reported improvement is specific to that system/evaluation and is not a universal expected gain.
13. Smit et al., “Should we be going MAD? A Look at Multi-Agent Debate Strategies for LLMs” (ICML 2024 / PMLR). https://proceedings.mlr.press/v235/smit24a.html — debate did not uniformly outperform other methods in the tested settings; configuration matters.
14. He, Treude and Lo, “Large Language Models for Software Engineering: A Systematic Literature Review” (ACM TOSEM, 2025). Search/index record: https://dl.acm.org/doi/10.1145/3695988 — broader review of LLM-based multi-agent systems for software engineering.

## Communication protocols

15. Model Context Protocol, architecture. https://modelcontextprotocol.io/docs/learn/architecture — host/client/server model for tools and resources.
16. Agent2Agent protocol. https://a2a-protocol.org/latest/ — compatible agent-to-agent discovery, messaging and task lifecycle.

## How to interpret this evidence

- Official host documentation supports capability claims only for the documented product/version. It does not prove the same feature is available in another host.
- Research findings are specific to their methods, models, tasks and evaluations. Do not turn one benchmark result into a general promise.
- Multi-agent debate and multiple calls to one model can be wasteful or reinforce shared errors. Preserve independent first passes and use evidence checks; measure quality, latency and cost on representative tasks.
- SecondOpinion uses a conservative composition: route simply, spawn only when valuable, challenge important claims and stop when further work has low expected value.
