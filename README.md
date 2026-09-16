# gjc-quest

> A GJC skill that turns defects you hit while using [gajae-code](https://github.com/Yeachan-Heo/gajae-code) (gjc) into **quests** — and lets only the ones a human accepted become upstream contributions.

*English · [한국어](README.ko.md)*

**Site: https://yazzang-homelab.github.io/gjc-quest/**

Tell an agent "find gjc bugs and open PRs" and you get a pile of draft PRs and
diagnostic-logging cleanups that pollute the maintainer's queue. This skill enforces the
opposite: **detection is automated, judgement and transmission are entirely human.**

```
detect → validity check (is it alive on current dev?) → grade → exclusion view
       → quest card (human accepts / rejects / holds) → three gates in order
       → human transmits → ledger row → observation notes
```

## What makes it different

- **Two human gates**, independent of each other. ① *intake* — is this worth being a quest?
  ② *transmission* — do we actually push it to the remote? Passing ① does not authorize ②.
- **Exactly one in-flight slot.** A second `accepted` row cannot exist. No numeric WIP
  budget — the structure blocks it instead.
- **Three gates evaluated in order**, short-circuiting on the first failure:
  `maintainer_prohibition` → `freeze` → contract/state validity.
- **Pre-intake validity.** Your local install is always older than upstream `dev`. Before
  grading: has it already landed / is the faulty path still present on current `dev` / does it
  reproduce with a clean HOME / (HIGH only) is the crash signature actually in the journal.
  Fail any of these and no card is raised.
- **Minimality gate.** One PR fixes exactly one defect with the minimal change. If more than
  one answer is defensible, it is not a defect but a product decision — it goes out as a
  separate issue, not as code. If blockers survive two independent reviews, stop; a third
  redesign is borrowing the owner's design authority.
- **Decision block.** A card that only lists options is not a valid card. Every option gets
  "what happens if you pick it / upside / downside", plus one recommendation with its basis.
- **Five-field ledger.** `quest_id · source · state · pr · closure_cause`. No sixth column,
  no pseudo-states like `candidate`. Remote state is never copied into markdown; it is derived
  from read-only `gh` (no double bookkeeping).
- **Freeze detection.** Batch closes without review, `do not open`-style wording, or several
  of my items closed within 24 hours — any one of them drops PR/issue transmission to zero and
  raises a local card. It clears only when the owner reviews or merges again, never by elapsed
  time.

## What it will not do

- No periodic batches, no continuous polling, no background timers (`cron` dies with the
  session). The single exception is a one-shot status report at a time the human specified.
- No auto-submission. Push, PR creation and issue creation happen only after human approval,
  and only for that head sha.
- No asking the maintainer for permission. The sole exception is an evidence-carrying
  out-of-scope defect issue, and even that is never chased for an answer.
- No reimplementation of `gjc crash report` — it wraps it.
- No config edits. No hook installation.

## Install

**A skill file is a prompt.** Dropping one into `~/.gjc/agent/skills/` puts text on your
agent's execution path, so treat it like any other supply-chain artifact: pin a revision,
verify the bytes, and read the diff before you install it. `curl | main` is not good enough,
and this repository does not ask you to do it.

```sh
# 1. pin a revision — a tag or a commit sha, never a moving branch
REV=v0.1.0

# 2. fetch to a staging path, not into the skills directory
curl -fsSL "https://raw.githubusercontent.com/yazzang-homelab/gjc-quest/$REV/SKILL.md" \
  -o /tmp/gjc-quest.SKILL.md
curl -fsSL "https://raw.githubusercontent.com/yazzang-homelab/gjc-quest/$REV/SHA256SUMS" \
  -o /tmp/gjc-quest.SHA256SUMS

# 3. verify the bytes, and only then install
(cd /tmp && sed 's| SKILL.md$| gjc-quest.SKILL.md|' gjc-quest.SHA256SUMS | sha256sum -c -)
install -Dm644 /tmp/gjc-quest.SKILL.md ~/.gjc/agent/skills/gjc-quest/SKILL.md
```

**Provenance.** Every push that touches `SKILL.md` publishes a Sigstore build-provenance
attestation, so the file can be tied to this repository and workflow rather than to a checksum
you got from the same place as the file:

```sh
gh attestation verify /tmp/gjc-quest.SKILL.md --repo yazzang-homelab/gjc-quest
```

CI also refuses any commit where `SHA256SUMS` does not match `SKILL.md`
([`skill.yml`](.github/workflows/skill.yml)) — a stale checksum is worse than none, because it
teaches people to skip the check. There is **no PGP signature**; the attestation and the commit
history are the provenance on offer, and 830-odd lines of Korean prose is a readable diff.

`skills.enabled` and `skills.enablePiUser` must be true in `config.yml` for it to load.
**Turning them on does not affect the current session** — invoke it from a new one. The skill
never changes your configuration.

Invoke with `/skill:gjc-quest`. Aliases: `gjc quest`, `quest scan`, `scan gjc defects`,
`gjc 퀘스트`, `결함 퀘스트`.

## Local state

The ledger and the observation notes attach to a single file,
`~/.gjc/agent/state/gjc-quest-ledger.md` by default. This installation's export instead uses
the gjc-quest ledger section of `~/.gjc/agent/state/gajae-code-pr-status.md`.
No new JSONL is created. Damaged or duplicated
sections are held, never rewritten in place.

**The observation notes are local-only.** Observations (direct events) and inferences
(interpretation) are recorded in physically separate tables, and neither is ever sent to a
remote. This repository ships none of that content either — the four exclusion classes are an
empty view that each user fills from their own observations.

## Scope

This targets `Yeachan-Heo/gajae-code` specifically. The base branch is always `dev`, and it
assumes gjc-only surfaces such as `gjc crash report`, `gjc notify` and the PR verdict block.
Using it against another repository means rewriting those parts.

Unofficial third-party skill, not affiliated with upstream.

## Does anyone actually follow this?

Fair question — a dense procedure document proves nothing about whether a human holds the line
every time. [**`LEDGER.md`**](LEDGER.md) is a **2026-09-16 (+09:00) snapshot of 38 quests**,
not an immutable cumulative history. Read-only `gh` checks give **14 landed rows** (13 merged
PRs plus the verified #4956 commit-succession exception), **8 closed, 12 locally held open,
4 rejected and 0 accepted**. There are **22 locators (15 PRs, 7 issues)** and **16 rows without
a locator in this snapshot**. #5290 remains closed/unmerged despite successor #5294 merging.
Locator-free holds were not reproduction-tested again. The older export had 25 rows; its
rejected `di-ask-freetext-missing` is absent and `di-other-empty-input-reask` is present, without
assuming they are the same event. These counts do not prove compliance, honest selection or
a success rate. Only the five-field rows are published; private observation notes are excluded.

## License

MIT. See [`LICENSE`](LICENSE).
