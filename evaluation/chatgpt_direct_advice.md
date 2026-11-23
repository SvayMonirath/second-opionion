My honest opinion: SecondOpinion should not try to prove that it makes AI smarter. It should prove that it catches expensive engineering mistakes before they become code.
That distinction should drive your testing strategy, README, examples, and marketing.
Your current result (66/100 vs. 74/100) is a useful starting point. But I would not make it the centerpiece of the project yet. Ten tasks are too few to establish that SecondOpinion consistently improves engineering decisions.
I would approach this in three parts.
1. How to test SecondOpinion credibly
1.1 Test the actual problem, not general AI intelligence
Your product has a specific job:
Given an engineering proposal, identify dangerous assumptions, explain the consequences, challenge the proposed design, and recommend a better direction before implementation.
Therefore, your benchmark should evaluate those abilities.
I would divide the test suite into five categories.
Category
What to test
Example
Architecture decisions
Detect unnecessary or inappropriate architecture
GraphQL Federation for a small monolith
Security decisions
Detect security weaknesses
Long-lived JWTs in localStorage
Data integrity
Detect designs that risk incorrect or inconsistent data
MongoDB as a financial ledger
Scalability decisions
Detect premature or inadequate design choices
Microservices before meaningful scaling needs
Correct decisions
Avoid criticizing perfectly reasonable engineering decisions
PostgreSQL for a conventional transactional application
That last category is extremely important.
A good red-team reviewer must know when NOT to object.
If SecondOpinion criticizes everything, it isn't a senior engineer. It's just another AI that disagrees with everything.
1.2 Build a benchmark with three types of cases
I recommend three distinct test groups.
A. Dangerous proposals
Must detect
Proposals containing significant security, architectural, or data-integrity problems.
Example: "Store seven-day JWT access tokens in localStorage and use them for every API request." Expected behavior:
Identify the actual security risks.
Explain realistic attack scenarios.
Identify missing revocation controls.
Recommend a safer alternative.
B. Reasonable proposals
Must recognize
Proposals that are already reasonable, even if alternatives exist.
Example: "Use PostgreSQL and a modular monolith for a small SaaS application." Expected behavior:
Recognize that the proposal is reasonable.
Avoid inventing architectural problems.
Identify only meaningful trade-offs.
C. Context-dependent proposals
Must investigate
Proposals that cannot be evaluated correctly without additional information.
Example: "We want to introduce microservices." Expected behavior:
Ask about team size, deployment constraints, scaling requirements, and operational capabilities.
Explain which assumptions determine whether the decision makes sense.
Avoid immediately approving or rejecting it.
This gives you a much better evaluation than simply feeding AI ten bad architectural decisions.
1.3 Use a consistent evaluation rubric
Do not score whether the response sounds intelligent.
Score whether it actually performs useful engineering review.
I recommend this rubric:
Evaluation dimension
Weight
Detects genuine problems
25
Technical correctness
25
Explains consequences with evidence
15
Provides actionable alternatives
15
Prioritizes severity correctly
10
Handles uncertainty and avoids false alarms
10
Total
100
For example:
A response that says:
MongoDB is not suitable. Use PostgreSQL.
Should not receive a high score just because it identified a potential issue.
A stronger response would explain:
Which financial invariants need to be maintained.
Why atomic transactions, constraints, and consistency guarantees matter.
Which specific MongoDB capabilities could address some requirements.
Why a relational database may be a better fit.
Under what circumstances the original choice could still be justified.
The difference is engineering reasoning, not response length.
Important: Use independent reviewers
Do not let SecondOpinion score itself.
A better evaluation process:
Prepare engineering scenarios.
Have experienced engineers independently establish acceptable findings and alternatives.
Run Baseline AI and SecondOpinion under identical conditions.
Remove identifying information from the responses.
Have reviewers score the responses without knowing which system produced them.
Resolve scoring disagreements and retain the evidence.
For context-dependent decisions, allow multiple technically valid answers. You should not require one predetermined architecture.
1.4 Measure the things that matter to actual developers
I would report these metrics separately rather than compressing everything into one score.
Metric
Why it matters
Critical issue detection
Does it catch genuinely dangerous decisions?
False-positive rate
Does it unnecessarily criticize good decisions?
Technical correctness
Are its objections actually valid?
Actionability
Can developers do something useful with its findings?
Missed critical issues
What dangerous problems escaped detection?
Token overhead
How much additional AI usage does it require?
Review latency
How much time does it add?
One particularly important metric:
Critical issue miss rate.
Imagine a test contains 20 genuinely dangerous proposals.
Baseline catches 12.
SecondOpinion catches 17.
That is a much more meaningful result than saying one model produced longer, more sophisticated answers.
You should also measure false positives. Otherwise, a tool that flags every architectural decision could look artificially successful.
1.5 Improve your existing 10-task benchmark
Your existing result:
Current benchmark result
Baseline AI
66/100
SecondOpinion
74/100
Absolute improvement +8 percentage points
Relative improvement +12.1%
Token usage 1.4×
Based on your reported 10-task evaluation. These are preliminary results, not evidence of general performance across all engineering tasks.
I would preserve this result, not discard it.
But I would do the following next:
Expand to approximately 40–60 carefully designed scenarios.
Include both dangerous and reasonable proposals.
Run each scenario multiple times to account for model variability.
Keep model versions, system prompts, settings, and tool configurations fixed.
Use identical evaluation conditions.
Have independent engineers score the results blindly.
Publish the complete methodology and individual case results.
Do not claim statistical significance unless your study actually supports it.
Also, keep token usage visible. Your 1.4× token consumption is a legitimate trade-off, not something to hide.
The message should be: SecondOpinion adds review cost in exchange for potentially preventing much more expensive engineering mistakes.
You still need evidence that the trade-off is worthwhile.
2. How I would structure the README
I think your current problem is primarily a communication problem.
A developer opens your README and sees charts, tables, and benchmark scores.
But they haven't understood one fundamental thing:
"What does this tool actually do to my AI coding workflow?"
Your README should answer that before showing any benchmarks.
I would structure it like this.
Section 1: Hero — Explain the product immediately
SecondOpinion
Your AI coding assistant needs someone who can disagree.
An independent engineering review layer that challenges risky assumptions before your AI writes the code.
You: "Let's use MongoDB for our financial ledger."
SecondOpinion challenges the decision
"Before implementing this, let's examine transaction guarantees, financial invariants, auditability, and concurrent updates.
A relational database may be a better fit for these requirements."
Illustrative interaction, not a measured benchmark result.
Open source
Architecture review
Security review
Pre-implementation
I particularly like this positioning:
"Your AI coding assistant needs someone who can disagree."
It communicates the personality and purpose of your product.
Alternative tagline:
"Challenge the architecture before you commit to the code."
Either is stronger than a generic description such as "AI-powered architectural analysis framework."
Section 2: Show the problem with one concrete example
Do not explain the problem in five paragraphs.
Show the interaction.
Without SecondOpinion
Developer
"Let's store seven-day JWT access tokens in localStorage. This will simplify authentication."
AI coding assistant
"Great idea! JWT authentication is a scalable and stateless approach. Let's implement it."
Illustrative baseline response.
With SecondOpinion
Developer
"Let's store seven-day JWT access tokens in localStorage."
SecondOpinion: Review required
Potential problems
XSS exposure: JavaScript executing in your application can potentially steal tokens from localStorage.
Revocation: A self-contained seven-day access token remains usable until expiration unless additional server-side controls exist.
Token lifetime: Seven days may be unnecessarily long for an access token.
Recommended direction
Consider short-lived access tokens with a properly secured refresh-token mechanism, rotation, and revocation.
Before implementation: Establish your threat model and session requirements.
Illustrative interaction. The actual recommendation depends on the application's authentication architecture and threat model.
This communicates the value of your product in seconds.
No benchmark chart needed.
Section 3: Explain how it works
Keep this extremely simple.
Propose
Tell your coding assistant what you want to build or which technical decision you want to make.
Challenge
SecondOpinion examines the assumptions, technical trade-offs, security implications, and architectural risks.
Review
It produces prioritized findings, supporting reasoning, and alternative approaches.
Decide
You decide whether to proceed, revise the design, or reject the proposal.
Important: Do not present SecondOpinion as an autonomous authority that always knows the correct architecture.
It is an independent reviewer that helps developers make better decisions.
Section 4: Show real proof
This is where your benchmark belongs.
But don't lead with a 10-bar chart.
Instead, use three elements:
A. One headline result
"74 vs. 66 in our initial 10-task evaluation."
B. Three observations
SecondOpinion performed better on complex architectural decisions.
Both systems performed similarly on straightforward textbook bugs.
SecondOpinion used approximately 1.4× the tokens.
C. Link to the evidence
Benchmark methodology
Complete task set
Raw model responses
Scoring rubric
Individual scoring results
Reproduction instructions
The README should contain the summary. A separate BENCHMARK.md should contain the detailed evidence.
Do not make people understand ten individual test cases just to understand why the product exists.
Section 5: When should developers use it?
This is extremely important because SecondOpinion should not be used for every single coding request.
Use it when
Choosing a database.
Designing authentication.
Planning a new architecture.
Making security-sensitive decisions.
Introducing major infrastructure.
Evaluating a complex refactor.
Probably unnecessary for
Renaming variables.
Fixing simple syntax errors.
Writing basic utility functions.
Small UI adjustments.
Straightforward CRUD implementation.
This communicates that you understand the cost of additional AI review.
It also makes the product feel more credible.
Section 6: Installation and usage
After developers understand the product, show them how to use it.
Keep installation instructions short, provide one working example, and link to detailed configuration documentation.
Don't force developers to read your architecture explanation before they can try the tool.
3. What concrete proof should appear in the README?
This is probably the most important part.
My recommendation is to create three representative engineering case studies, not ten benchmark cards.
Each should demonstrate a different reason to use SecondOpinion.
Example 1: Security — Seven-day JWT in localStorage



medium.com
Developer proposal:
"Use seven-day JWT access tokens stored in localStorage."
What the baseline AI does:
Approves the proposal and begins implementing authentication.
What SecondOpinion identifies:
JavaScript-accessible token storage creates an XSS-related token theft risk.
Long-lived access tokens increase the exposure window.
Revocation requires additional mechanisms if tokens are otherwise valid until expiration.
What changes:
The design moves toward short-lived access tokens, refresh-token rotation, and explicit revocation requirements.
Why this case matters: It demonstrates that SecondOpinion can challenge a security-sensitive implementation decision before code exists.
Example 2: Data integrity — MongoDB financial ledger



syncfusion.com
Developer proposal:
"Let's use MongoDB for our warehouse billing and financial ledger."
What SecondOpinion investigates:
Transaction boundaries.
Concurrent financial updates.
Double-entry accounting invariants, if applicable.
Audit history.
Referential integrity.
Reconciliation requirements.
What changes:
The team evaluates PostgreSQL or another relational database as the primary financial ledger store, while considering whether MongoDB has a justified role elsewhere.
Why this case matters: It demonstrates that SecondOpinion understands the difference between choosing a database for convenience and choosing one based on data-integrity requirements.
Importantly, MongoDB is not inherently incapable of financial workloads. Your example should demonstrate why a particular design is unsuitable, not make technically absolute claims.
Example 3: Architecture — Premature GraphQL Federation



medium.com
Developer proposal:
"We should implement GraphQL Federation for our new application."
What SecondOpinion investigates:
Number of independently owned services.
Team boundaries.
Deployment independence.
Actual scaling requirements.
Operational complexity.
Whether a single GraphQL service is sufficient.
What changes:
The team starts with a modular monolith or simpler GraphQL architecture and introduces federation only when independent service ownership and other requirements justify it.
Why this case matters: It demonstrates that SecondOpinion can recognize unnecessary complexity, not just security vulnerabilities.
4. One thing I would add: An actual end-to-end case study
The three examples above demonstrate different capabilities.
But I would go one step further.
Publish one complete, reproducible case study showing:
A real engineering decision, from proposal to revised design
Original proposal
The exact developer prompt, including its original assumptions.
Baseline response
What the original AI coding assistant recommended.
SecondOpinion response
Its complete findings, severity levels, and supporting reasoning.
Independent verification
An engineer evaluates whether each finding is correct and relevant.
Revised engineering decision
Show the original design beside the revised design, explaining what changed and why.
Most important proof
Show an engineering decision that changed because SecondOpinion identified a problem.
This is much more persuasive than a benchmark score.
It shows the entire value chain:
Proposal → Risk detection → Verification → Better decision.
One caution: do not claim that SecondOpinion prevented a production incident unless you have evidence of that. Say it identified a risk before implementation if that is what actually happened.
5. My recommended repository structure
I would keep the README focused and move supporting evidence into separate documents.
Plain text


SecondOpinion/
│
├── README.md
│
├── docs/
│   ├── HOW_IT_WORKS.md
│   ├── USE_CASES.md
│   ├── REVIEW_METHODOLOGY.md
│   └── LIMITATIONS.md
│
├── benchmarks/
│   ├── README.md
│   ├── METHODOLOGY.md
│   ├── SCORING_RUBRIC.md
│   ├── TASKS.md
│   ├── RESULTS.md
│   ├── raw/
│   └── reproducibility/
│
└── examples/
    ├── jwt-authentication/
    ├── financial-ledger/
    └── premature-federation/
The important separation:
README.md: Why should I care?
HOW_IT_WORKS.md: What happens internally?
USE_CASES.md: When should I use it?
BENCHMARKS: Does it actually work?
LIMITATIONS.md: Where can it fail?
Don't turn the README into a complete technical specification.
6. What I would prioritize
If I were responsible for SecondOpinion, this would be my execution order.
Priority 1 — Fix the proof
Critical
Expand the benchmark beyond ten tasks.
Include correct and context-dependent proposals.
Establish independent expert scoring.
Measure false positives and missed critical issues.
Publish reproducible evidence.
Priority 2 — Fix the README
Critical
Rewrite the opening around the problem.
Show one before-and-after interaction immediately.
Explain the four-step workflow.
Present the benchmark as supporting evidence, not the main attraction.
Priority 3 — Build three case studies
High
Security decision.
Data-integrity decision.
Architectural complexity decision.
Priority 4 — Validate actual developer value
High
Let developers use it in real projects.
Record how often findings are accepted, rejected, or modified.
Ask whether it changed a decision.
Measure review time and token overhead.
7. My final recommendation: Change what you are trying to sell
There are two ways to position this product.
Position A:
"SecondOpinion improves AI coding performance by 12%."
This makes developers ask:
How was it measured?
Why only ten tasks?
Does it work with my model?
Is 1.4× more tokens worth it?
You're forced to defend a benchmark.
Position B:
"Your AI coding assistant can write 5,000 lines of code around a bad architectural decision. SecondOpinion challenges that decision before implementation."
This makes developers immediately understand the problem.
You're selling a different kind of value.
The product's core promise
Don't let your AI coding assistant blindly agree with expensive engineering decisions.
SecondOpinion independently reviews your assumptions, challenges risky designs, and helps you identify problems before implementation.
A skeptical engineering perspective for AI-assisted development.
One final thought: Your strongest differentiator is not that SecondOpinion finds more problems. It's that it knows which problems are worth challenging, explains why, and knows when the original decision is already good.
Build your benchmark around proving that. Build your README around demonstrating it.
If you get those two things right, you won't need a complicated chart to explain why SecondOpinion exists.