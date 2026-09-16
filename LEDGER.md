# Ledger — the real rows

The procedure in [`SKILL.md`](SKILL.md) is dense: three ordered gates, a derived exclusion
view, an eleven-slot report per card. A document cannot prove that a human actually holds that
line every time. This is a current local snapshot, with locator states refreshed from remote
checks, not an immutable cumulative history. Most locators target `Yeachan-Heo/gajae-code`;
one targets `devswha/gajae-code-app`.

- **Schema.** Exactly five fields: `quest_id · source · state · pr · closure_cause`. No sixth
  column, no pseudo-states. The source is the gjc-quest ledger section of
  `~/.gjc/agent/state/gajae-code-pr-status.md`; only its 38 five-field rows are exported.
- **Authority.** The markdown holds local decisions and namespaced route/defer/revival
  provenance only. `state` and terminal causes for anything with a locator are **derived from
  read-only `gh`** (`QTR-08`), never stored as a second authority. The `state` column below was
  re-derived at export time; every locator was checked individually.
- **Exported.** 2026-09-16 (+09:00). Query the locator's repository and object type:

  ```sh
  gh api repos/<owner>/<repo>/pulls/<number> --jq '{state, merged, merged_at}'
  gh api repos/<owner>/<repo>/issues/<number> --jq '{state, state_reason}'
  ```

The earlier export had 25 rows. Its rejected `GQ-20260826-di-ask-freetext-missing` row is
absent from the current source; `GQ-20260826-di-other-empty-input-reask` is present instead.
This does not establish that the two IDs represent the same event. Author PRs absent from
the local ledger are not added as quests.

The [public contribution audit](CONTRIBUTIONS.md) enumerates 94 authored GitHub objects,
not 38 quests. Its 21 direct locator matches comprise 14 authored PRs (12 actually merged,
2 closed/unmerged) and 7 issues. #5154 is a successor authored by someone else: it remains
a ledger locator, never an addition to the audited author's denominator. The 38-row snapshot
is preserved, with only #5290's remote-derived cause corrected below; direct matching does
not establish causal skill attribution.

## Rows

| quest_id | source | state | pr | closure_cause |
|---|---|---|---|---|
| `GQ-20260909-image-role-selected-model` | `session-misbehavior` | `merged` | `pr:Yeachan-Heo/gajae-code#5440` | `pending:pr-proposal;pending:head:371c7cd153782b77dced5f158c651c9b4f609f2d` |
| `GQ-20260907-gateway-compound-tool-id` | `session-misbehavior` | `merged` | `pr:Yeachan-Heo/gajae-code#5389` | `pending:pr-proposal;pending:head:84f4f85e0` |
| `GQ-20260905-codex-astra-catalog` | `static-defect` | `closed` | `pr:Yeachan-Heo/gajae-code#5290` | `other;pending:pr-proposal;pending:succession:5294` |
| `GQ-20260904-preset-cursor-rerender-freeze` | `session-misbehavior` | `merged` | `pr:Yeachan-Heo/gajae-code#5265` | `pending:pr-proposal` |
| `GQ-20260902-preset-auth-sync-freeze` | `session-misbehavior` | `merged` | `pr:Yeachan-Heo/gajae-code#5197` | `pending:pr-proposal` |
| `GQ-20260826-di-nested-phase-write-silent` | `static-defect` | `merged` | `pr:Yeachan-Heo/gajae-code#4985` | `pending:pr-proposal` |
| `GQ-20260826-di-other-empty-input-reask` | `static-defect` | `open` | `—` | `hold:mechanism-unidentified;pending:revival:OBS-062` |
| `GQ-20260826-di-resume-empty-state` | `session-misbehavior` | `open` | `—` | `hold:local-state-only` |
| `GQ-20260826-di-cancel-verb-absent` | `static-defect` | `open` | `—` | `hold:product-decision-required` |
| `GQ-20260826-multiplexer-hyperlink-force-off` | `static-defect` | `rejected` | `—` | `exclusion:not-a-defect-measured` |
| `GQ-20260825-login-url-unlinked-wrap` | `static-defect` | `merged` | `pr:Yeachan-Heo/gajae-code#4956` | `pending:pr-proposal;pending:succession:a9ed03ba20` |
| `GQ-20260825-login-url-copy-integrity` | `static-defect` | `closed` | `issue:Yeachan-Heo/gajae-code#4977` | `pending:scope-out-proposal:GQ-20260825-login-url-unlinked-wrap` |
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
| `GQ-20260828-self-pane-turn-forgery` | `session-misbehavior` | `closed` | `issue:Yeachan-Heo/gajae-code#5039` | `pending:pr-proposal` |
| `GQ-20260828-local-legacy-path-resolution` | `session-misbehavior` | `open` | `—` | `hold:dev-reproduction-unverified` |
| `GQ-20260831-thinking-block-duplication` | `static-defect` | `rejected` | `—` | `exclusion:taste-refactor` |
| `GQ-20260824-escaped-nonascii-observability` | `static-defect` | `merged` | `pr:Yeachan-Heo/gajae-code#4923` | `pending:pr-proposal` |
| `GQ-20260824-ox-alpha-empty-stream` | `static-defect` | `merged` | `pr:Yeachan-Heo/gajae-code#4906` | `pending:pr-proposal` |
| `GQ-20260831-pi-native-custom-provider-transport` | `static-defect` | `merged` | `pr:Yeachan-Heo/gajae-code#5101` | `pending:pr-proposal` |
| `GQ-20260901-app-image-native-vision` | `static-defect` | `closed` | `issue:devswha/gajae-code-app#13` | `pending:pr-proposal` |
| `GQ-20260901-esc-steer-loader-precedence` | `static-defect` | `merged` | `pr:Yeachan-Heo/gajae-code#5154` | `pending:pr-proposal;pending:succession:Yeachan-Heo/gajae-code#5154` |

## What the numbers say

| | count |
|---|---|
| quests in the current snapshot | 38 |
| **landed upstream** (`merged`) — 13 merged PRs + 1 succession exception | **14** |
| closed (`closed`) — 1 unmerged PR + 7 completed issues | 8 |
| open — all held locally, none open at the remote | 12 |
| rejected locally (`rejected`) | 4 |
| in the single implementation slot (`accepted`) | 0 |
| rows with a remote locator | 22 (15 PRs, 7 issues) |
| rows without a locator in this snapshot | 16 |

**16 of 38 rows have no locator in the current snapshot:** 12 local holds and 4 rejections.
This is not evidence that no remote object ever existed. Locator-free rows and their recorded
hold reasons are unchanged; this export did not re-test reproduction or revalidate those holds.

### Landed

| quest | locator | how it landed |
|---|---|---|
| `GQ-20260909-image-role-selected-model` | [#5440](https://github.com/Yeachan-Heo/gajae-code/pull/5440) | merged |
| `GQ-20260907-gateway-compound-tool-id` | [#5389](https://github.com/Yeachan-Heo/gajae-code/pull/5389) | merged |
| `GQ-20260904-preset-cursor-rerender-freeze` | [#5265](https://github.com/Yeachan-Heo/gajae-code/pull/5265) | merged |
| `GQ-20260902-preset-auth-sync-freeze` | [#5197](https://github.com/Yeachan-Heo/gajae-code/pull/5197) | merged |
| `GQ-20260826-di-nested-phase-write-silent` | [#4985](https://github.com/Yeachan-Heo/gajae-code/pull/4985) | merged |
| `GQ-20260825-login-url-unlinked-wrap` | [#4956](https://github.com/Yeachan-Heo/gajae-code/pull/4956) | PR closed unmerged; verified commit succession on `dev` — `QTR-12` exception |
| `GQ-20260819-anthropic-overload-retry` | [#4736](https://github.com/Yeachan-Heo/gajae-code/pull/4736) | merged |
| `GQ-20260819-broker-publication-obstruction` | [#4732](https://github.com/Yeachan-Heo/gajae-code/pull/4732) | merged |
| `GQ-20260820-rotating-agent-env-credential` | [#4737](https://github.com/Yeachan-Heo/gajae-code/pull/4737) | merged |
| `GQ-20260813-crash-index-self-quarantine` | [#4470](https://github.com/Yeachan-Heo/gajae-code/pull/4470) | merged |
| `GQ-20260824-escaped-nonascii-observability` | [#4923](https://github.com/Yeachan-Heo/gajae-code/pull/4923) | merged |
| `GQ-20260824-ox-alpha-empty-stream` | [#4906](https://github.com/Yeachan-Heo/gajae-code/pull/4906) | merged |
| `GQ-20260831-pi-native-custom-provider-transport` | [#5101](https://github.com/Yeachan-Heo/gajae-code/pull/5101) | merged |
| `GQ-20260901-esc-steer-loader-precedence` | [#5154](https://github.com/Yeachan-Heo/gajae-code/pull/5154) | merged |

Merge dates are omitted. #4956 remains `merged` only as the existing verified succession
exception, not as a claim that the PR merged. The full successor commit is
`a9ed03ba2073fda4ed8b0d9c556a104e45df3476`; the read-only comparison below returned
`behind_by=0`, confirming the commit is included in `dev`:

```sh
gh api repos/Yeachan-Heo/gajae-code/compare/a9ed03ba2073fda4ed8b0d9c556a104e45df3476...dev --jq .behind_by
```

#5290 is closed **unmerged**. Its remote-derived cause is corrected from the earlier local
`product_direction` classification to `other`: the [public single-winner decision](https://github.com/Yeachan-Heo/gajae-code/pull/5290#issuecomment-5548924781)
accepted #5294's implementation of the same Astra requirement, retaining #5290 only as
corroborating evidence. This is not rejection of the feature's product direction or code
succession preserving this author's implementation. #5294 being merged does not mean #5290
merged, and does not promote this row to `merged`. The local source ledger was not modified.
All seven issue locators are closed/completed. Their recorded provenance, including the
succession references on #4478 and #4481, is retained without adding quests for successor PRs.

### What this export does not contain

Only the five-field ledger rows are exported. Observation notes, Decision blocks and
eleven-slot card reports were not read for this refresh and are not published. References
inside the permitted rows are preserved without retrieving their private targets.

### Honest limits

The `state` column and remote-derived terminal causes for locators are independently
verifiable through `gh`; `quest_id`, `source`, local provenance within `closure_cause`,
and every row without a locator are **self-reported**.
The #4956 succession exception additionally relies on the previously verified succession and
the current commit comparison, not PR merge state alone. These counts prove neither process
compliance nor the honesty of holds or selection. They describe only the current snapshot,
not cumulative activity, a success rate, or fresh reproduction results.

---

## 한국어

절차가 촘촘한 것과 그 규율을 매번 지켰다는 것은 다른 문제고, 문서로는 후자를 증명할 수 없다.
이 공개본은 **2026-09-16 (+09:00) 현재 스냅샷**이며 누적 불변 기록이 아니다.

- 실제 소스는 `~/.gjc/agent/state/gajae-code-pr-status.md`의 gjc-quest 원장 섹션이다.
  다섯 필드 38행만 공개하고, locator 상태는 읽기 전용 `gh`로 각각 확인했다.
  대부분 `Yeachan-Heo/gajae-code`이며 `devswha/gajae-code-app` 이슈가 1건 있다.
- **38건: `merged` 14, `closed` 8, `open` 12, `rejected` 4, `accepted` 0.**
  착륙 14건은 PR merge 13건과 #4956 승계 예외 1건이다. `closed`는 미머지 PR #5290
  1건과 closed/completed 이슈 7건이다. 원격에 열린 locator는 없다.
- locator는 **22건(PR 15, issue 7)**이고 **16건은 현재 스냅샷에 locator가 없다**
  (로컬 보류 12, 거절 4). 과거에도 원격 객체가 없었다는 뜻은 아니다. locator 없는 행과
  보류 사유는 그대로 두었으며 이번에 재현하거나 보류 타당성을 재검증하지 않았다.
- #4956 PR은 closed/unmerged다. 기존에 검증한 승계 commit
  `a9ed03ba2073fda4ed8b0d9c556a104e45df3476`과 `dev`의 위 비교에서 `behind_by=0`을
  확인해 기존 `merged` 예외를 유지했다. PR 자체가 merge됐다는 뜻은 아니다.
  #5290은 `closed`를 유지하되 위 공개 single-winner 결정에 따라 원격 파생 cause만
  `product_direction`에서 `other`로 정정했다. 동일 Astra 요구에서 다른 작성자의 #5294를
  채택하고 #5290은 corroborating evidence로 남긴 것이므로 제품 방향 거절이 아니다.
  후속 #5294의 merge가 #5290의 merge나 원 코드 승계를 뜻하지 않는다. 로컬 소스 원장은
  수정하지 않았다. Landed 표는 날짜를 생략했다.
- 과거 공개본은 25건이었다. 당시 rejected인 `GQ-20260826-di-ask-freetext-missing`은
  현행 원장에 없고 `GQ-20260826-di-other-empty-input-reask`가 있다. 두 ID가 같은
  사건이라고 추정하지 않는다. 로컬 원장에 없는 작성자 PR이나 후속 PR을 quest로 추가하지 않았다.
- 허용된 행의 참조는 보존하되 비공개 참조 대상을 조회하지 않았다. 관측 노트·Decision block·
  11슬롯 보고는 이번 갱신에서 읽지 않았고 공개하지 않는다.
- [공개 작성 기여 전수조사](CONTRIBUTIONS.md)는 GitHub 객체 94건이며 이 원장의 quest
  38건과 분모가 다르다. 직접 locator 일치는 21건(PR 14, issue 7)이다. 타인 작성 후속
  #5154는 원장 locator일 뿐 작성자 분모에 추가하지 않는다. 38행의 구성과 상태는 유지하고
  #5290의 원격 파생 cause만 위 근거로 정정했다.
- locator의 원격 상태·원격 파생 종료 원인 이외 필드와 로컬 provenance, locator 없는 행은
  **자기 보고**다. #4956은 PR 상태만이
  아니라 기존 승계 검증과 현재 commit 비교에 근거한다. 이 집계는 절차 준수·보류의 정직성·
  표본 선택의 공정성을 증명하지 않으며 누적 활동·성공률·새 재현 결과도 아니다.
