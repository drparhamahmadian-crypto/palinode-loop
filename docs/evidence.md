# Evidence and limits

Palinode Loop makes a feedback path inspectable: outcomes and source excerpts inform a candidate; a person can approve a short rule with an explicit trigger and scope; later violations prompt review. Research supports parts of this path—learning reusable context from execution feedback, retrieving procedures and events, and retaining evidence that can be revisited. It does **not** test or validate this repository's complete workflow. The human approval gate is a governance choice, not a benchmark-proven performance gain.

## Relevant studies

### [Agentic Context Engineering (ACE), §4.3, Table 1](https://arxiv.org/html/2510.04618v3#S4.SS3)

On AppWorld, offline ReAct with ACE and no ground-truth labels scored 57.2 versus 42.4 for ReAct alone: **+14.8 percentage points** averaged over four task metrics. The base was DeepSeek-V3.1-671B; the same non-thinking DeepSeek-V3.1 served as generator, reflector and curator. This supports refining reusable, inspectable context from execution feedback. It does not evaluate human approval or this loop; the authors warn that weak reflection can create noisy or harmful context. The paper's abstract also reports a separate average across selected baselines; that is not the comparison quoted here.

### [LongMemEval-V2, §5.1, Table 2](https://arxiv.org/html/2605.12493v1#S5.SS1)

In the specialized web-agent memory benchmark, AgentRunbook-C scored 74.9% versus 69.9% for Codex on the small tier (**+5.0 points**) and 70.1% versus 68.7% on medium (**+1.4 points**). The experiment used an agent controller; it did not test Palinode Loop or its approval process. These tier-specific table values avoid an inconsistent aggregate in the paper's abstract, which describes a different RAG comparison than the table's AgentRunbook-R rows. The evidence supports the usefulness of retrieved workflow and event context in that setting, not general effectiveness.

### [DreamBench-SWE, §6.6, Table 12](https://arxiv.org/html/2608.20664v1#S6.SS6)

In the separately preregistered v2.1 audit, no external memory passed 21/180 cases; the deterministic verbatim event-memory baseline passed 82/180. Each condition covered 60 traps with three repeated seeds, clustered by trap. This suggests stored prior events can help on those multi-session software tasks. It is a benchmark result, not a component-level causal test or evidence for a human approval gate; the authors limit inference to registered comparisons and report no superiority claim between memory-bearing conditions.

## Design choices that remain judgements

Keeping excerpts beside derived rules lets a reviewer revisit whether a candidate still follows from its evidence; these studies do not measure that benefit in Palinode Loop. The **two-session minimum** and **30-word limit** are policy heuristics, not research-derived thresholds. Concise rules may be easier to inspect and apply, while ACE cautions that excessive compression can discard useful detail. Schema tests establish that the supplied ledger meets structural checks; they do not establish evidence authenticity, semantic support, or improved agent reliability.
