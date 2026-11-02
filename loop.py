#!/usr/bin/env python3
"""Read-only check and render of a version 1 lessons ledger (maximum 1 MiB)."""
import datetime
import json
import re
import sys
import unicodedata

MAX_BYTES = 1024 * 1024
STATES = {"candidate", "active", "dormant", "rejected"}


class Invalid(ValueError):
    pass


def fail(path, message):
    raise Invalid(f"{path}: {message}")


def pairs(items):
    result = {}
    for key, value in items:
        if key in result:
            fail("JSON", "duplicate object key")
        result[key] = value
    return result


def fields(obj, required, optional, path):
    if not isinstance(obj, dict):
        fail(path, "expected object")
    if set(obj) - required - optional:
        fail(path, "unknown field")
    if required - set(obj):
        fail(path, "missing required field")


def string(value, path):
    if (
        not isinstance(value, str)
        or not value.strip()
        or any(
            unicodedata.category(c) in {"Cc", "Cf", "Cs", "Zl", "Zp"}
            for c in value
        )
    ):
        fail(path, "expected nonempty single-line text without prohibited characters")


def date(value, path):
    string(value, path)
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", value):
        fail(path, "expected ISO date YYYY-MM-DD")
    try:
        datetime.date.fromisoformat(value)
    except ValueError:
        fail(path, "invalid date")


def evidence(items, path):
    """Check supplied excerpts and return distinct declared session labels."""
    if not isinstance(items, list):
        fail(path, "expected list")
    sessions = set()
    for i, item in enumerate(items):
        p = f"{path}[{i}]"
        fields(item, {"session", "date", "source", "quote", "excerpt"}, set(), p)
        for key in ("session", "source", "quote", "excerpt"):
            string(item[key], f"{p}.{key}")
        date(item["date"], f"{p}.date")
        if item["quote"] not in item["excerpt"]:
            fail(f"{p}.quote", "not found in excerpt")
        sessions.add(item["session"].strip())
    return sessions


def validate(data):
    """Return (entry, eligible, review_required, rule) tuples after policy checks."""
    fields(data, {"schema_version", "entries"}, set(), "ledger")
    if type(data["schema_version"]) is not int or data["schema_version"] != 1:
        fail("ledger.schema_version", "expected integer 1")
    if not isinstance(data["entries"], list):
        fail("ledger.entries", "expected list")
    seen, results = set(), []
    for i, entry in enumerate(data["entries"]):
        p = f"ledger.entries[{i}]"
        fields(
            entry,
            {"id", "state", "trigger", "action", "scope", "evidence", "admission"},
            {"approval", "violations"},
            p,
        )
        for key in ("id", "state", "trigger", "action", "scope"):
            string(entry[key], f"{p}.{key}")
        if not re.fullmatch(r"[A-Za-z][A-Za-z0-9_-]{0,63}", entry["id"]):
            fail(f"{p}.id", "expected safe identifier")
        if entry["id"] in seen:
            fail(f"{p}.id", "duplicate ID")
        seen.add(entry["id"])
        if entry["state"] not in STATES:
            fail(f"{p}.state", "invalid state")
        sessions = evidence(entry["evidence"], f"{p}.evidence")
        violations = evidence(entry.get("violations", []), f"{p}.violations")
        admission = entry["admission"]
        keys = {"own_mistake", "recurring", "preventable", "covered_by_rule"}
        fields(admission, keys, set(), f"{p}.admission")
        for key in keys:
            if type(admission[key]) is not bool:
                fail(f"{p}.admission.{key}", "expected boolean")
        eligible = (
            bool(sessions)
            and all(
                admission[key]
                for key in ("own_mistake", "recurring", "preventable")
            )
            and not admission["covered_by_rule"]
        )
        approved = False
        if "approval" in entry:
            approval = entry["approval"]
            fields(approval, {"decision", "by", "date"}, set(), f"{p}.approval")
            for key in ("decision", "by"):
                string(approval[key], f"{p}.approval.{key}")
            date(approval["date"], f"{p}.approval.date")
            approved = approval["decision"] == "approve"
        rule = f"When {entry['trigger']}, {entry['action']}."
        if entry["state"] == "active":
            if not eligible:
                fail(f"{p}.admission", "active entry fails admission")
            if len(sessions) < 2:
                fail(f"{p}.evidence", "active entry requires two distinct sessions")
            if not approved:
                fail(f"{p}.approval", "active entry requires explicit approval")
            if len(rule.split()) > 30:
                fail(p, "active rule exceeds 30 words")
        results.append((entry, eligible, len(violations) >= 2, rule))
    return results


def load(path):
    try:
        with open(path, "rb") as f:
            raw = f.read(MAX_BYTES + 1)
        if len(raw) > MAX_BYTES:
            fail("file", "exceeds 1 MiB")
        data = json.loads(
            raw.decode("utf-8"),
            object_pairs_hook=pairs,
            parse_constant=lambda _: fail("JSON", "nonfinite number"),
        )
    except Invalid:
        raise
    except (OSError, UnicodeError, ValueError, RecursionError):
        fail("file", "cannot read valid UTF-8 JSON")
    return validate(data)


def main(argv):
    if len(argv) != 3 or argv[1] not in {"check", "render"}:
        print("usage: python3 loop.py {check|render} LEDGER.json", file=sys.stderr)
        return 2
    try:
        results = load(argv[2])
        for entry, eligible, review, rule in results:
            if argv[1] == "render" and entry["state"] == "active":
                print(f"{rule} [Scope: {entry['scope']}]")
            elif argv[1] == "check":
                status = "eligible" if eligible else "ineligible"
                suffix = (
                    "; review enforcement recommended"
                    if entry["state"] == "active" and review
                    else ""
                )
                print(f"Entry {entry['id']}: {entry['state']}; {status}{suffix}")
        return 0
    except Invalid as exc:
        print(f"Invalid ledger: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
