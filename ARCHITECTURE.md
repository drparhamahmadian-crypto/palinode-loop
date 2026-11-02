# Architecture

Palinode Loop separates **evidence**, **policy decisions**, and **use**. The reference implementation checks a caller-supplied JSON ledger and renders rules that are already marked active and carry an approval attestation.

```text
observed example ──> candidate with evidence ──> human decision
                                                   │
                                                   v
ledger.json ──> check ──> active approved rule ──> render for review
     ^                                                │
     └──────── later violation evidence ──────────────┘
```

This is a governed workflow, not an automated state machine. A person documents evidence, evaluates the candidate, records approval or rejection, and updates the ledger. `loop.py` does not capture sessions, create candidates, change entry states, or enforce rules in an agent host.

## Ledger lifecycle

The version 1 ledger has a `schema_version` and an `entries` array. Entries use one of four states: `candidate`, `active`, `dormant`, or `rejected`. Each entry includes an `id`, `trigger`, `action`, `scope`, evidence, admission answers, and optionally approval and violation records. [`examples/ledger.json`](examples/ledger.json) contains a fabricated active rule and candidate.

An entry is eligible when it has at least one distinct evidence session, records the mistake as the operator's own, recurring, and preventable, and says no existing rule covered it. Eligibility is not approval. To be active, the entry must also have evidence from at least two distinct sessions, an approval record with decision `approve`, and a generated rule no longer than 30 words. The two-session minimum and word cap are policy heuristics, not research-derived thresholds. Approval records an attestation; it does not authenticate a person.

Later violations are kept as evidence records. `check` recommends review for an active rule when violations cover at least two distinct session labels. It does not decide whether to revise, retire, or retain the rule. Unrecorded violations remain invisible.

## Commands

From this directory, using Python 3.10 or newer:

```sh
python3 loop.py check examples/ledger.json
python3 loop.py render examples/ledger.json
```

`check` validates the ledger and reports each entry's state and eligibility. `render` prints active rules as `When <trigger>, <action>. [Scope: <scope>]`. Review the output before copying selected rules into host instructions. Neither command changes the ledger, global instructions, or host settings.

The implementation uses only the Python standard library. It reads at most 1 MiB from the named input, rejects malformed UTF-8/JSON, duplicate JSON keys and entry IDs, unknown fields, invalid dates, unsupported states, unsafe IDs, and Unicode control/format characters in strings. It checks that each evidence quote occurs in its supplied excerpt. That string check does not establish source authenticity, quotation context, or semantic support.

## Source map

- [`loop.py`](loop.py): `validate` checks ledger structure and lifecycle requirements; `evidence` validates supplied evidence and returns distinct session labels; `load` parses bounded JSON input; `main` implements `check` and `render`.
- [`tests/test_loop.py`](tests/test_loop.py): fabricated tests for admission, approval, identifiers, evidence, violations, and malformed input.
- [`docs/evidence.md`](docs/evidence.md): cited studies and their limits; none tests Palinode Loop or establishes its effectiveness.
- [`docs/index.html`](docs/index.html) and [`docs/architecture.svg`](docs/architecture.svg): interactive explanation and static diagram.
