import contextlib
import copy
import io
import json
import pathlib
import subprocess
import sys
import tempfile
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
import loop


class LedgerTests(unittest.TestCase):
    def setUp(self):
        self.data = json.loads((ROOT / "examples/ledger.json").read_text())

    def test_example_and_candidate(self):
        results = loop.validate(self.data)
        self.assertEqual([(x[0]["state"], x[1]) for x in results], [("active", True), ("candidate", True)])
        self.data["entries"][1]["admission"]["preventable"] = False
        self.assertFalse(loop.validate(self.data)[1][1])

    def test_approval_and_recurrence_required(self):
        for change in (lambda e: e.pop("approval"),
                       lambda e: e["approval"].update(decision="reject"),
                       lambda e: e["evidence"][1].update(session="example-1")):
            data = copy.deepcopy(self.data)
            change(data["entries"][0])
            with self.assertRaises(loop.Invalid):
                loop.validate(data)

    def test_quote_unknown_field_and_admission_type(self):
        changes = (lambda e: e["evidence"][0].update(quote="not present"),
                   lambda e: e.update(private_metadata="secret"),
                   lambda e: e["admission"].update(recurring=1))
        for change in changes:
            data = copy.deepcopy(self.data)
            change(data["entries"][0])
            with self.assertRaises(loop.Invalid):
                loop.validate(data)

    def test_violations_and_retirement(self):
        entry = self.data["entries"][0]
        entry["violations"] = copy.deepcopy(entry["evidence"])
        self.assertTrue(loop.validate(self.data)[0][2])
        entry["state"] = "dormant"
        with tempfile.TemporaryDirectory() as folder:
            path = pathlib.Path(folder) / "ledger.json"
            path.write_text(json.dumps(self.data))
            out = io.StringIO()
            with contextlib.redirect_stdout(out):
                self.assertEqual(loop.main(["loop.py", "render", str(path)]), 0)
            self.assertEqual(out.getvalue(), "")

    def test_invalid_json_and_duplicate_keys(self):
        for raw in ('{"schema_version":1,"schema_version":1,"entries":[]}',
                    '{"schema_version":1,"entries": [}',
                    '{"schema_version":1,"entries":[],"extra":NaN}'):
            with tempfile.TemporaryDirectory() as folder:
                path = pathlib.Path(folder) / "ledger.json"
                path.write_text(raw)
                with self.assertRaises(loop.Invalid):
                    loop.load(path)

    def test_duplicate_ids_and_rule_length(self):
        self.data["entries"][1]["id"] = "R1"
        with self.assertRaises(loop.Invalid):
            loop.validate(self.data)
        self.data["entries"][1]["id"] = "C1"
        self.data["entries"][0]["action"] = "word " * 31
        with self.assertRaises(loop.Invalid):
            loop.validate(self.data)

    def test_control_characters_and_identifier(self):
        for key, value in (("id", "R\x1b[31m"), ("id", "bad name"),
                           ("action", "check \u202etext"), ("action", "check\x00text"),
                           ("action", "secret\ud800"), ("action", "check\u2028text"),
                           ("action", "check\u2029text")):
            data = copy.deepcopy(self.data)
            data["entries"][0][key] = value
            with self.assertRaises(loop.Invalid):
                loop.validate(data)

    def test_empty_candidate_evidence_and_boolean_version(self):
        self.data["entries"][1]["evidence"] = []
        self.assertFalse(loop.validate(self.data)[1][1])
        self.data["schema_version"] = True
        with self.assertRaises(loop.Invalid):
            loop.validate(self.data)

    def test_cli_errors_do_not_echo_and_size_limit(self):
        with tempfile.TemporaryDirectory() as folder:
            path = pathlib.Path(folder) / "ledger.json"
            self.data["entries"][0]["action"] = "secret\x1b[31m"
            path.write_text(json.dumps(self.data))
            result = subprocess.run([sys.executable, "-B", str(ROOT / "loop.py"), "render", str(path)],
                                    capture_output=True, text=True)
            self.assertEqual(result.returncode, 1)
            self.assertNotIn("secret", result.stderr)
            self.assertNotIn("\x1b", result.stderr)
            self.assertEqual(result.stdout, "")
            self.data["entries"][0]["action"] = "secret\ud800"
            path.write_text(json.dumps(self.data))
            result = subprocess.run([sys.executable, "-B", str(ROOT / "loop.py"), "render", str(path)],
                                    capture_output=True, text=True)
            self.assertEqual(result.returncode, 1)
            self.assertNotIn("secret", result.stderr)
            self.assertNotIn("Traceback", result.stderr)
            self.assertEqual(result.stdout, "")
            path.write_bytes(b" " * (loop.MAX_BYTES + 1))
            result = subprocess.run([sys.executable, "-B", str(ROOT / "loop.py"), "check", str(path)],
                                    capture_output=True, text=True)
            self.assertEqual(result.returncode, 1)
            self.assertIn("exceeds 1 MiB", result.stderr)


if __name__ == "__main__":
    unittest.main()
