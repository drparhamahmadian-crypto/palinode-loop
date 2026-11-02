# Security and privacy

Palinode Loop is a local checker and renderer for a user-supplied JSON ledger. It uses Python's standard library, reads one named file (up to 1 MiB), and makes no network or model calls. It does not load rules into a host or modify settings. Treat ledger content and rendered rules as untrusted until a person reviews them.

## Threats and limits

- **Malicious instructions in data:** triggers, actions, excerpts, and rendered rules are text. The checker does not detect prompt injection, judge whether a rule is safe, or prevent a host from misusing copied text. Review the exact rule and its scope before use.
- **Fabricated or incomplete evidence:** the checker verifies that a quoted string appears in a supplied excerpt and that session labels are distinct. It cannot authenticate sources or sessions, verify context or recurrence, or establish that all relevant events were recorded.
- **Approval spoofing:** approval names and decisions are ledger fields, not signatures or authenticated identities. Control write access to the ledger and keep approval evidence in your normal review system.
- **Overbroad or stale rules:** structural validity does not make a rule appropriate or current. Keep conditions and scope narrow; use later violations as a prompt for human review, and retire rules when needed. The two-session minimum and 30-word cap are policy heuristics, not validated safety thresholds.
- **Sensitive data:** ledgers can contain private conversation material. Keep them access-controlled and use synthetic or appropriately de-identified examples. Do not publish patient information, credentials, personal data, private conversations, or raw logs.
- **Input handling:** the implementation bounds file size, rejects malformed JSON and duplicate keys, restricts IDs, and rejects Unicode control/format characters. These checks validate input shape; they do not sandbox the operating system or make arbitrary files safe to open.

## Safe use

Keep ledgers local and access-controlled. Inspect the exact rendered rules and scope before manually adding any to host instructions. Do not configure automatic promotion, retrieval, or loading based on a successful check alone. Review changes before sharing or publishing a ledger.

## Reporting a vulnerability

If GitHub private vulnerability reporting is enabled for the repository, use that channel. If it is unavailable, open an issue asking for a private reporting route without including exploit details, secrets, or sensitive data. Do not publish credentials or personal records in a report.
