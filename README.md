# Palinode Loop

**Make the next mistake harder to repeat.**

Palinode Loop turns documented agent failures into reviewed, scoped rules, then makes later failures visible against those rules. Its central contribution is the path between evidence, a human policy decision, an active intervention, and feedback.

![Palinode Loop: evidence, candidate, human decision, active rule, feedback](docs/architecture.svg)

The name comes from *palinode*, a poem or statement that revises an earlier position. Palinode Loop treats revision as practical corrigibility: keep the grounds for a decision, let a person choose what should change, and retain a route back to the evidence.

## Quickstart

Requires Python 3.10+ and the standard library. From this directory:

```sh
python3 loop.py check examples/ledger.json
python3 loop.py render examples/ledger.json
```

Example output:

```text
$ python3 loop.py check examples/ledger.json
Entry R1: active; eligible
Entry C1: candidate; eligible
$ python3 loop.py render examples/ledger.json
When a synthetic example contains a date, check the date before presenting it. [Scope: synthetic examples]
```

`check` validates and summarises the entries. `render` prints active rules for human review; it does not update the ledger or install guidance in an agent host. Run the offline suite with `python3 -m unittest discover -s tests -v`.

## Mechanism

The version 1 JSON ledger stores `candidate`, `active`, `dormant`, or `rejected` entries. Each entry has a trigger, action, scope, evidence records, and admission answers. Active entries also need a recorded approval. See [`examples/ledger.json`](examples/ledger.json) for synthetic records and [`ARCHITECTURE.md`](ARCHITECTURE.md) for the validation path and trust boundaries.

| Stage | Implementation |
|---|---|
| Record a failure | An evidence item records session label, date, source label, quote, and excerpt. |
| Check admission | `validate()` requires evidence and the declared mistake, recurrence, preventability, and prior-rule answers. |
| Activate a rule | The ledger must record approval; active entries need two distinct evidence sessions and a generated rule of at most 30 words. |
| Check and render | `main()` reports ledger status or prints active rules with scope. It never promotes candidates. |
| Revisit | Two distinct violation sessions cause `check` to recommend review of an active rule. A person decides whether to revise or retire it. |

## What the research supports

Published studies report gains from related mechanisms in specific tasks. ACE reports 57.2 versus 42.4 across four AppWorld metrics for its evaluated configuration ([Table 1](https://arxiv.org/html/2510.04618v3#S4.SS3)). LongMemEval-V2 reports AgentRunbook-C at 74.9% versus 69.9% on its small tier and 70.1% versus 68.7% on medium ([Table 2](https://arxiv.org/html/2605.12493v1#S5.SS1)). DreamBench-SWE's preregistered successor audit reports 82/180 passes for deterministic event memory and 21/180 for no external memory ([Table 12](https://arxiv.org/html/2608.20664v1#S6.SS6)).

These results support studying feedback, retrieved procedures, and retained events. They do not measure Palinode Loop or establish the effectiveness of its human approval process. [`docs/evidence.md`](docs/evidence.md) records the exact comparisons and study limits.

## Inspect the implementation

- [`loop.py`](loop.py) — standard-library parser, ledger validator, and renderer.
- [`ARCHITECTURE.md`](ARCHITECTURE.md) — schema rules, function path, and trust boundaries.
- [`docs/index.html`](docs/index.html) — interactive walkthrough and study references.
- [`docs/architecture.svg`](docs/architecture.svg) — portable static architecture diagram.
- [`docs/evidence.md`](docs/evidence.md) — linked research and evidence limits.
- [`SECURITY.md`](SECURITY.md) — local-use and data-handling guidance.

This is a version 0.1.0 reference implementation, developed with AI assistance from an earlier lessons-workflow design. The example is synthetic. The proposed MIT licence and publication contents remain subject to final review; font licensing is recorded in [`THIRD_PARTY.md`](THIRD_PARTY.md).
