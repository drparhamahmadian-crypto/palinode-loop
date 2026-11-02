# Contributing

Contributions should keep the project small, reviewable, and honest about what its checks establish.

## Before proposing a change

- Describe the user-visible problem and the smallest complete fix.
- Keep examples synthetic; do not add private conversations, patient information, credentials, or unredacted logs.
- Preserve the distinction between structural validation, human judgment, and authenticated evidence.
- For schema or CLI changes, update the README and architecture notes so behavior and limits stay aligned.

## Local checks

The implementation uses only the Python standard library. From this directory, run:

```sh
python3 -m unittest discover -s tests -v
python3 loop.py check examples/ledger.json
python3 loop.py render examples/ledger.json
```

Tests and examples use fabricated records. A passing test suite shows only that the exercised cases behave as expected; it does not establish real-world accuracy, adoption, or safety of a proposed rule.

## Review and release

Keep changes focused and explain new validation boundaries or failure cases. Do not claim automatic learning, model-weight updates, or measured reliability gains. Provenance, attribution, and the final licence choice remain release prerequisites; do not add or imply an approved licence without resolving them.
