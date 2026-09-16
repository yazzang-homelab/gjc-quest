#!/usr/bin/env python3
"""Collect a public-only GitHub contribution audit using read-only gh API calls."""
import argparse
import datetime as dt
import hashlib
import json
import re
import subprocess
from pathlib import Path


class AuditError(RuntimeError):
    pass


def utc_now():
    return dt.datetime.now(dt.timezone.utc).isoformat()


def redact(text):
    if text is None:
        return None
    if not isinstance(text, str):
        raise AuditError("Expected text")
    patterns = [
        r"\b(?:gh[pousr]_[A-Za-z0-9_]+|github_pat_[A-Za-z0-9_]+)\b",
        r"\b(?:sk|xox[baprs])-[A-Za-z0-9_-]{10,}\b",
        r"(?i)\b(?:bearer\s+)[A-Za-z0-9._~+/-]+=*",
        r"(?i)\b(?:token|password|secret|api[_-]?key)\s*[:=]\s*[\"']?[^\s\"'`,;]+",
        r"/(?:root|home|Users)/[^\s\"'`<>]+",
        r"[A-Za-z]:\\Users\\[^\s\"'`<>]+",
    ]
    for pattern in patterns:
        text = re.sub(pattern, "[REDACTED]", text)
    return text


def api(endpoint, **params):
    command = ["gh", "api", "--method", "GET", endpoint]
    for key, value in params.items():
        command.extend(["-f", f"{key}={value}"])
    result = subprocess.run(command, capture_output=True, text=True, check=False)
    if result.returncode:
        # Do not echo provider errors: they may contain credentials or local paths.
        raise AuditError(f"GitHub GET failed for {endpoint}: exit {result.returncode}")
    try:
        return json.loads(result.stdout)
    except json.JSONDecodeError as exc:
        raise AuditError(f"Invalid JSON from {endpoint}") from exc


def kind_of(item):
    return "pr" if "pull_request" in item else "issue"


def identity(item):
    url = item.get("repository_url", "")
    match = re.fullmatch(r"https://api\.github\.com/repos/([^/]+/[^/]+)", url)
    number = item.get("number")
    if not match or not isinstance(number, int) or isinstance(number, bool) or number <= 0:
        raise AuditError("Invalid search object identity")
    return match.group(1), number


def search(author, kind, fetch=api):
    query = f"is:public author:{author} is:{kind}"
    items, seen = [], set()
    page, total = 1, None
    while True:
        data = fetch("search/issues", q=query, per_page=100, page=page, sort="created", order="asc")
        count = data.get("total_count")
        if data.get("incomplete_results") is not False:
            raise AuditError(f"Incomplete search: {query}")
        if not isinstance(count, int) or isinstance(count, bool) or count < 0 or count > 1000:
            raise AuditError(f"Invalid total or 1000-result cap exceeded: {query}")
        if total is not None and count != total:
            raise AuditError(f"Search total changed: {query}")
        total = count
        batch = data.get("items")
        if not isinstance(batch, list) or len(batch) > 100:
            raise AuditError("Invalid search page")
        for item in batch:
            key = identity(item)
            if kind_of(item) != kind:
                raise AuditError("PR/issue search classification mismatch")
            if item.get("user", {}).get("login", "").casefold() != author.casefold():
                raise AuditError("Search author mismatch")
            if key in seen:
                raise AuditError("Duplicate search object")
            seen.add(key)
            items.append(item)
        if len(batch) < 100 or len(items) >= total:
            break
        page += 1
    if len(items) != total:
        raise AuditError(f"Search count mismatch: expected {total}, collected {len(items)}")
    return items, {"query": query, "total_count": total, "incomplete_results": False,
                   "pages": page, "collected_count": len(items), "duplicate_count": 0}


def pages(endpoint, fetch=api):
    result, page = [], 1
    while True:
        batch = fetch(endpoint, per_page=100, page=page)
        if not isinstance(batch, list) or len(batch) > 100:
            raise AuditError(f"Invalid list page: {endpoint}")
        result.extend(batch)
        if len(batch) < 100:
            break
        page += 1
    ids = [entry["id"] for entry in result if "id" in entry]
    if len(ids) != len(set(ids)):
        raise AuditError(f"Duplicate paginated event: {endpoint}")
    return result, {"pages": page, "collected_count": len(result)}


def pick(item, fields):
    out = {}
    for key in fields:
        if key not in item:
            continue
        if key == "body":
            out["body_sha256"] = hashlib.sha256((item[key] or "").encode("utf-8")).hexdigest()
        else:
            out[key] = redact(item[key]) if isinstance(item[key], str) else item[key]
    return out


def user(item):
    return pick(item or {}, ("login", "html_url"))


def event(item, fetch=None, repos=None):
    out = pick(item, ("id", "event", "state", "body", "html_url", "url", "created_at",
                      "submitted_at", "commit_id", "commit_url", "dismissed_review"))
    # Keep only purpose-specific fields rather than nested profiles/payloads.
    out.pop("dismissed_review", None)
    for key in ("user", "actor"):
        if item.get(key):
            out[key] = user(item[key])
    if item.get("source"):
        source = item["source"]
        linked = source.get("issue", {})
        if linked and fetch is not None:
            locator = re.fullmatch(r"https://github\.com/([^/]+/[^/]+)/(?:issues|pull)/[0-9]+", linked.get("html_url", ""))
            if not locator:
                raise AuditError("Invalid timeline source locator")
            repository(locator.group(1), fetch, repos)
        out["source"] = {"type": source.get("type"), "issue": pick(linked, (
            "number", "html_url", "title", "state"))}
        if "pull_request" in linked:
            out["source"]["issue"]["pull_request"] = pick(linked["pull_request"], (
                "html_url", "merged_at"))
    return out


def repository(name, fetch, cache):
    if name not in cache:
        data = fetch(f"repos/{name}")
        if data.get("private") is not False or data.get("visibility") != "public":
            raise AuditError(f"Repository is not confirmed public: {name}")
        cache[name] = pick(data, ("full_name", "html_url", "private", "visibility"))
        cache[name]["owner"] = user(data.get("owner"))
    return cache[name]


def detail(item, author, fetch, repos):
    name, number = identity(item)
    repo = repository(name, fetch, repos)
    kind = kind_of(item)
    endpoint = f"repos/{name}/{'pulls' if kind == 'pr' else 'issues'}/{number}"
    data = fetch(endpoint)
    if data.get("user", {}).get("login", "").casefold() != author.casefold():
        raise AuditError(f"Detail author mismatch: {endpoint}")
    if data.get("number") != number:
        raise AuditError(f"Detail number mismatch: {endpoint}")
    if kind == "issue" and "pull_request" in data:
        raise AuditError("Issue detail is a PR")
    out = pick(data, ("number", "title", "body", "html_url", "url", "state", "state_reason",
                      "created_at", "closed_at", "merged_at", "merge_commit_sha"))
    out.update(kind=kind, user=user(data["user"]), repo=repo, pagination={})
    if kind == "pr":
        out["merged_by"] = user(data.get("merged_by"))
        for key in ("base", "head"):
            branch = data.get(key) or {}
            out[key] = pick(branch, ("label", "ref", "sha"))
            linked_repo = branch.get("repo")
            if linked_repo:
                # Never publish metadata of a private head repository.
                if linked_repo.get("private") is not False:
                    raise AuditError("PR branch repository is not public")
                out[key]["repo"] = repository(linked_repo["full_name"], fetch, repos)
        if data.get("merged_at"):
            sha = data.get("merge_commit_sha")
            if not sha:
                raise AuditError("Merged PR missing merge commit SHA")
            commit = fetch(f"repos/{name}/commits/{sha}")
            out["merge_commit"] = pick(commit, ("sha", "html_url"))
            out["merge_commit"]["message_sha256"] = hashlib.sha256(commit["commit"]["message"].encode("utf-8")).hexdigest()
            out["merge_commit"]["author"] = user(commit.get("author"))
            out["merge_commit"]["committer"] = user(commit.get("committer"))
            # Email addresses and author names are unnecessary for account attribution.
            out["merge_commit"]["author_date"] = commit["commit"]["author"].get("date")
        elif data.get("state") == "closed":
            for key, path in (("comments", f"issues/{number}/comments"),
                              ("reviews", f"pulls/{number}/reviews"),
                              ("timeline", f"issues/{number}/timeline")):
                entries, meta = pages(f"repos/{name}/{path}", fetch)
                out[key] = [event(entry, fetch, repos) for entry in entries]
                out["pagination"][key] = meta
    else:
        entries, meta = pages(f"repos/{name}/issues/{number}/timeline", fetch)
        out["timeline"] = [event(entry, fetch, repos) for entry in entries]
        out["pagination"]["timeline"] = meta
    return out


def collect(author, fetch=api):
    if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9-]{0,38}", author):
        raise AuditError("Invalid GitHub login")
    started = utc_now()
    repos, searches, objects = {}, {}, []
    for kind in ("pr", "issue"):
        items, searches[kind] = search(author, kind, fetch)
        for item in items:
            objects.append(detail(item, author, fetch, repos))
    return {"schema_version": 1, "author": author, "started_at_utc": started,
            "finished_at_utc": utc_now(), "complete": True,
            "scope": "Public GitHub PRs and issues authored by this account; API observations are not an atomic snapshot.",
            "redaction": "Bodies and commit messages are replaced by SHA-256 of the original UTF-8 text (null body hashes as empty text). Known token/credential and personal local-path patterns in remaining text are replaced with [REDACTED]; nested profiles and commit emails omitted. Pattern redaction is not a guarantee against arbitrary secrets.",
            "searches": searches, "repositories": sorted(repos.values(), key=lambda x: x["full_name"]),
            "objects": objects}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--author", required=True)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    try:
        evidence = collect(args.author)
    except (AuditError, KeyError, TypeError, OSError) as exc:
        parser.exit(1, f"Audit failed; output not written: {redact(str(exc))}\n")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(evidence, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"output": str(args.output), "searches": evidence["searches"]}, ensure_ascii=False))


if __name__ == "__main__":
    main()
