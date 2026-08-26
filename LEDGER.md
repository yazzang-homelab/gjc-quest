# Ledger — the real rows

The procedure in [`SKILL.md`](SKILL.md) is dense: three ordered gates, a derived exclusion
view, an eleven-slot report per card. A document cannot prove that a human actually holds that
line every time. So here is the live ledger this skill has been writing against
`Yeachan-Heo/gajae-code`, exported as-is.

- **Schema.** Exactly five fields: `quest_id · source · state · pr · closure_cause`. No sixth
  column, no pseudo-states. This is the same table the skill appends to
  `~/.gjc/agent/state/gjc-quest-ledger.md`.
- **Authority.** The markdown holds local decisions and namespaced route/defer/revival
  provenance only. `state` and terminal causes for anything with a locator are **derived from
  read-only `gh`** (`QTR-08`), never stored as a second authority. The `state` column below was
  re-derived at export time; every locator was checked individually.
- **Exported.** 2026-08-26T08:00Z. Reproduce any row:

  ```sh
  gh api repos/Yeachan-Heo/gajae-code/issues/<number> \
    --jq '"\(if .pull_request then "PR" else "ISSUE" end) \(.state) \(.pull_request.merged_at // "-")"'
  ```

## Rows

| quest_id | source | state | pr | closure_cause |
|---|---|---|---|---|
| `GQ-20260826-di-nested-phase-write-silent` | `static-defect` | `accepted` | `—` | `pending:new` |
| `GQ-20260826-di-ask-freetext-missing` | `static-defect` | `rejected` | `—` | `exclusion:not-a-defect-measured` |
| `GQ-20260826-di-resume-empty-state` | `session-misbehavior` | `open` | `—` | `hold:local-state-only` |
| `GQ-20260826-di-cancel-verb-absent` | `static-defect` | `open` | `—` | `hold:product-decision-required` |
| `GQ-20260826-multiplexer-hyperlink-force-off` | `static-defect` | `rejected` | `—` | `exclusion:not-a-defect-measured` |
| `GQ-20260825-login-url-unlinked-wrap` | `static-defect` | `merged` | `pr:Yeachan-Heo/gajae-code#4956` | `pending:pr-proposal;pending:succession:a9ed03ba20` |
| `GQ-20260825-login-url-copy-integrity` | `static-defect` | `open` | `issue:Yeachan-Heo/gajae-code#4977` | `pending:scope-out-proposal:GQ-20260825-login-url-unlinked-wrap` |
| `GQ-20260823-idle-session-identity` | `static-defect` | `closed` | `issue:Yeachan-Heo/gajae-code#4855` | `pending:pr-proposal` |
| `GQ-20260823-account-env-token-freeze` | `session-misbehavior` | `open` | `—` | `hold:local-state-only` |
| `GQ-20260818-managed-lock-leak` | `static-defect` | `open` | `—` | `hold:independent-review-blocked;hold:local-worktree-missing` |
| `GQ-20260819-anthropic-overload-retry` | `session-misbehavior` | `merged` | `pr:Yeachan-Heo/gajae-code#4736` | `pending:pr-proposal` |
| `GQ-20260819-notify-debris-amplification` | `static-defect` | `rejected` | `—` | `exclusion:already-landed-upstream` |
| `GQ-20260819-broker-publication-obstruction` | `static-defect` | `merged` | `pr:Yeachan-Heo/gajae-code#4732` | `pending:pr-proposal` |
| `GQ-20260820-rotating-agent-env-credential` | `session-misbehavior` | `merged` | `pr:Yeachan-Heo/gajae-code#4737` | `pending:pr-proposal` |
| `GQ-20260818-crash-index-predelete` | `static-defect` | `open` | `—` | `hold:slot-occupied` |
| `GQ-20260813-broker-retained-publication` | `crash` | `open` | `—` | `hold:trigger-unspecified;pending:revalidated-head:7a920df9c1` |
| `GQ-20260813-crash-index-self-quarantine` | `static-defect` | `merged` | `pr:Yeachan-Heo/gajae-code#4470` | `pending:pr-proposal` |
| `GQ-20260813-crash-index-log-orphan` | `static-defect` | `closed` | `issue:Yeachan-Heo/gajae-code#4478` | `pending:succession:Yeachan-Heo/gajae-code#4495` |
| `GQ-20260813-session-loop-spin` | `session-misbehavior` | `closed` | `issue:Yeachan-Heo/gajae-code#4481` | `pending:succession:Yeachan-Heo/gajae-code#4509` |
| `GQ-20260813-shared-topic-authority` | `crash` | `open` | `—` | `hold:dev-reproduction-unverified;exclusion:already-landed-upstream` |
| `GQ-20260812-binding-invalid` | `crash` | `open` | `—` | `hold:local-state-only` |
| `GQ-20260813-pi-natives-load` | `crash` | `open` | `—` | `hold:not-reproducible-on-current-version` |
| `GQ-20260813-clear-context-transition` | `session-misbehavior` | `open` | `—` | `hold:not-reproducible-on-current-version` |
| `GQ-20260824-usage-limit-auto-resume` | `static-defect` | `closed` | `issue:Yeachan-Heo/gajae-code#4908` | `pending:pr-proposal` |
| `GQ-20260824-wsl-drvfs-busy-lock` | `session-misbehavior` | `rejected` | `—` | `exclusion:already-landed-upstream` |

## What the numbers say

| | count |
|---|---|
| quests recorded | 25 |
| **landed upstream** (`merged`) | **5** |
| closed at the remote (`closed`) | 4 |
| open — 1 awaiting review at the remote, 10 held locally | 11 |
| rejected before ever leaving the machine (`rejected`) | 4 |
| in the single implementation slot (`accepted`) | 1 |
| remote objects created, total | 10 (5 PRs, 5 issues) |

**15 of 25 never produced a remote object.** That is the part worth reading. Four were rejected
by the exclusion view or by measurement showing there was no defect
(`exclusion:not-a-defect-measured`, `exclusion:already-landed-upstream`), and ten sit on local
holds — `hold:local-state-only` when a clean HOME would not reproduce it,
`hold:dev-reproduction-unverified` when the path could not be confirmed on current `dev`,
`hold:product-decision-required` when the fix would have invented product semantics,
`hold:slot-occupied` when the one slot was taken.

### Landed

| quest | locator | how it landed |
|---|---|---|
| `GQ-20260813-crash-index-self-quarantine` | [#4470](https://github.com/Yeachan-Heo/gajae-code/pull/4470) | merged 2026-08-13 |
| `GQ-20260820-rotating-agent-env-credential` | [#4737](https://github.com/Yeachan-Heo/gajae-code/pull/4737) | merged 2026-08-19 |
| `GQ-20260819-anthropic-overload-retry` | [#4736](https://github.com/Yeachan-Heo/gajae-code/pull/4736) | merged 2026-08-20 |
| `GQ-20260819-broker-publication-obstruction` | [#4732](https://github.com/Yeachan-Heo/gajae-code/pull/4732) | merged 2026-08-20 |
| `GQ-20260825-login-url-unlinked-wrap` | [#4956](https://github.com/Yeachan-Heo/gajae-code/pull/4956) | PR closed unmerged; the commit landed on `dev` as `a9ed03ba20` with authorship credit — `QTR-12` succession |

Two issues were closed the same way: [#4478](https://github.com/Yeachan-Heo/gajae-code/issues/4478)
and [#4481](https://github.com/Yeachan-Heo/gajae-code/issues/4481) were completed by the
maintainer's own [#4495](https://github.com/Yeachan-Heo/gajae-code/pull/4495) and
[#4509](https://github.com/Yeachan-Heo/gajae-code/pull/4509). The skill records that as
`pending:succession:<ref>` and **does not contest credit** — a landed fix is the outcome that
was wanted.

### What this export does not contain

The observation notes, the Decision blocks and the eleven-slot card reports stay local by
design. They contain interpretation of a specific maintainer's behaviour, and publishing that
would be a dossier, not evidence. What is publishable is what can be checked independently: the
five fields and the locators.

### Honest limits

The `state` column for locators is independently verifiable through `gh`; the rest —
`quest_id`, `source`, `closure_cause`, and every row without a locator — is **self-reported**.
Nothing in this repository can prove a hold was honest rather than convenient. What it can show
is that the ratio is not flattering-by-construction: five landed against fifteen that were
never sent.

---

## 한국어

절차가 촘촘한 것과 그 규율을 매번 지켰다는 것은 다른 문제고, 문서로는 후자를 증명할 수 없다.
그래서 이 스킬이 `Yeachan-Heo/gajae-code`를 상대로 실제로 써 온 원장을 그대로 공개한다.

- 열은 정확히 다섯 개이고, locator가 있는 행의 `state`와 종단 사유는 **읽기 전용 `gh`로
  파생**한다(`QTR-08`). 위 표의 `state`는 export 시점에 로케이터를 하나씩 조회해 다시 파생한
  값이다 — 마크다운에 두 번째 권위 상태를 두지 않는다는 규칙이 그래서 실물로 보인다.
- **25건 중 15건은 원격 객체를 만들지 않았다.** 4건은 배제 뷰 또는 "재보니 결함이 아님"으로
  거절, 10건은 로컬 보류(깨끗한 HOME에서 미재현·현행 dev 확인 불가·제품 결정 선행 필요·
  슬롯 점유), 1건이 구현 슬롯에 있다. 착륙 5건, 원격 종단 4건.
- 관측 노트·Decision block·11슬롯 보고는 공개하지 않는다. 특정 관리자의 행동에 대한 해석이
  들어 있어 그것을 공개하면 증거가 아니라 신상 문서가 된다. 독립 검증이 가능한 다섯 필드와
  로케이터만 낸다.
- locator 행의 상태 외에는 전부 **자기 보고**다. 보류가 정직했는지는 이 저장소가 증명하지
  못한다. 증명되는 것은 비율이 자기 유리하게 조작되지 않았다는 것뿐이다 — 착륙 5 대 미발송 15.
