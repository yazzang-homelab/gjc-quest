import importlib.util
import unittest
from pathlib import Path
from unittest.mock import patch


SPEC = importlib.util.spec_from_file_location(
    "audit_contributions", Path(__file__).resolve().parents[1] / "tools/audit_contributions.py"
)
audit = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(audit)


def item(number=1, kind="pr"):
    value = {"number": number, "repository_url": "https://api.github.com/repos/owner/repo",
             "user": {"login": "example"}}
    if kind == "pr":
        value["pull_request"] = {}
    return value


def response(items, total=None, incomplete=False):
    return {"items": items, "total_count": len(items) if total is None else total,
            "incomplete_results": incomplete}


class SearchTests(unittest.TestCase):
    def test_public_query_and_pagination(self):
        calls = []
        def fetch(endpoint, **params):
            calls.append((endpoint, params))
            return response([item(i) for i in range(1, 101)], 101) if params["page"] == 1 else response([item(101)], 101)
        items, meta = audit.search("example", "pr", fetch)
        self.assertEqual(len(items), 101)
        self.assertEqual(meta["pages"], 2)
        self.assertEqual(calls[0][1]["q"], "is:public author:example is:pr")

    def test_invalid_search_responses_fail(self):
        cases = [response([], incomplete=True), response([], 1001), response([], 1),
                 response([item(), item()]), response([item(kind="issue")]),
                 response([], -1), response([], True)]
        for payload in cases:
            with self.subTest(payload=payload), self.assertRaises(audit.AuditError):
                audit.search("example", "pr", lambda *a, **kw: payload)

    def test_changed_total_fails(self):
        def fetch(endpoint, **params):
            return response([item(i) for i in range(1, 101)], 101) if params["page"] == 1 else response([item(101)], 102)
        with self.assertRaises(audit.AuditError):
            audit.search("example", "pr", fetch)

    def test_duplicate_across_pages_fails(self):
        def fetch(endpoint, **params):
            return response([item(i) for i in range(1, 101)], 101) if params["page"] == 1 else response([item(1)], 101)
        with self.assertRaises(audit.AuditError):
            audit.search("example", "pr", fetch)

    def test_author_mismatch_fails(self):
        with self.assertRaises(audit.AuditError):
            audit.search("other", "pr", lambda *a, **kw: response([item()]))

    def test_issue_classification(self):
        self.assertEqual(audit.kind_of(item()), "pr")
        self.assertEqual(audit.kind_of(item(kind="issue")), "issue")
        with self.assertRaises(audit.AuditError):
            audit.search("example", "issue", lambda *a, **kw: response([item()]))

    def test_api_error_propagates(self):
        def fail(*args, **kwargs):
            raise audit.AuditError("unavailable")
        with self.assertRaisesRegex(audit.AuditError, "unavailable"):
            audit.collect("example", fail)


class HelpersTests(unittest.TestCase):
    def test_identity_rejects_non_github_or_invalid_numbers(self):
        self.assertEqual(audit.identity(item(42)), ("owner/repo", 42))
        for value in ({**item(), "repository_url": "https://elsewhere/repos/a/b"},
                      {**item(), "number": True}, {**item(), "number": 0}):
            with self.assertRaises(audit.AuditError):
                audit.identity(value)

    def test_hash_body_and_minimize_event(self):
        value = audit.event({"body": "abc", "id": 4, "event": "commented",
                             "user": {"login": "example", "email": "omit", "avatar_url": "omit"},
                             "source": {"type": "issue", "issue": {"number": 2, "title": "연결",
                                        "body": "never publish", "html_url": "https://github.com/a/b/issues/2"}}})
        self.assertEqual(value["body_sha256"], "ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad")
        self.assertNotIn("body", value)
        self.assertNotIn("email", value["user"])
        self.assertNotIn("body", value["source"]["issue"])
        self.assertEqual(value["source"]["issue"]["title"], "연결")

    def test_redaction(self):
        for text in ("ghp_abcdefghijk", "github_pat_abcdef", "/root/private/file", "C:\\Users\\name\\secret", "token=secret", "Bearer abc.def"):
            self.assertEqual(audit.redact(text), "[REDACTED]")

    def test_paginated_events(self):
        def fetch(endpoint, **params):
            return [{"id": i} for i in range(100)] if params["page"] == 1 else [{"id": 100}]
        entries, meta = audit.pages("events", fetch)
        self.assertEqual(len(entries), 101)
        self.assertEqual(meta["pages"], 2)
        with self.assertRaises(audit.AuditError):
            audit.pages("events", lambda *a, **kw: [{"id": 1}, {"id": 1}])
        with self.assertRaises(audit.AuditError):
            audit.pages("events", lambda *a, **kw: {})

    def test_repository_visibility_fails_closed(self):
        for repo in ({"private": True, "visibility": "private"}, {"private": False}):
            with self.assertRaises(audit.AuditError):
                audit.repository("a/b", lambda *a: repo, {})

    def test_detail_author_mismatch(self):
        def fetch(endpoint):
            if endpoint == "repos/owner/repo":
                return {"private": False, "visibility": "public", "full_name": "owner/repo"}
            return {"number": 1, "user": {"login": "other"}}
        with self.assertRaises(audit.AuditError):
            audit.detail(item(), "example", fetch, {})

    def test_gh_read_only_failure_and_invalid_json(self):
        from types import SimpleNamespace
        for result in (SimpleNamespace(returncode=1, stdout="", stderr="secret"),
                       SimpleNamespace(returncode=0, stdout="not json", stderr="")):
            with patch.object(audit.subprocess, "run", return_value=result) as run:
                with self.assertRaises(audit.AuditError):
                    audit.api("search/issues", q="is:public")
                self.assertEqual(run.call_args.args[0][:4], ["gh", "api", "--method", "GET"])


if __name__ == "__main__":
    unittest.main()
