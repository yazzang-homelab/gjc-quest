# 실제 기여 전수 감사

## 범위와 완전성

공개 작성자 `yazzang-homelab`의 GitHub PR·issue를 조사하였다. [증거 JSON](evidence/2026-09-16-contributions.json)의 수집 시각은 **2026-09-16T15:20:59.269491+09:00–2026-09-16T15:23:02.928174+09:00**이다. API 관측은 원자적 스냅샷이 아니므로 수집 중 상태 변화 가능성이 있다.

공개 PR 검색은 `total_count=collected_count=69`, issue 검색은 `total_count=collected_count=25`이며, 양쪽 모두 `incomplete_results=false`, `duplicate_count=0`이었다. 실제 metadata를 다시 집계하여 **94개 고유 객체**를 확인하였다. 독립적으로 객체가 속한 **8개 저장소**의 REST `issues?creator=yazzang-homelab&state=all`을 pagination하여 94개 key의 완전 일치를 확인하였다. JSON의 `repositories` 14개는 PR head 저장소 등을 포함하므로 작성 객체의 저장소 수와 혼동하지 않는다.

초기 인증 계정의 전체 PR 검색 83건 중 14건은 private였다. 별도 private 검색도 `total_count=14`, `incomplete_results=false`였으며, 그 이름·번호·본문은 이 공개 보고서에 포함하지 않는다. 삭제된 항목, 비공개 항목, 다른 계정의 작성물, 댓글, 직접 push한 commit 및 검색에 노출되지 않는 항목은 이 전수조사의 범위 밖이다. 따라서 GitHub 전체 기여의 절대적 완전성을 주장하지 않는다.

본문과 commit message 원문은 증거에 공개하지 않고 SHA-256으로 대체하였다. metadata·timeline·공개 URL을 보존하며 사적 관측 노트와 Decision block은 사용하지 않았다.

[독립 검증 receipt](evidence/2026-09-16-verification.json)는 원본 JSON SHA-256 결속, 8개 저장소·94개 key의 REST 대조, 21개 원장 직접 일치, 대표 3개 merge commit의 ancestry와 2개 테스트 patch 판독을 기록한다. 추가로 코드 승계 4건, 후속 PR 9건, 미머지 PR 11건의 inline 댓글 0건, 이슈의 17/3/4/1 판독을 기록한다. 이 receipt는 서명이 아니다. ancestry는 commit 포함 관계를 증명하지만 이후 변경이 되돌려지지 않았음을 증명하지 않는다.

## 집계와 평가 기준

| 공개 작성 범위 | PR | merged | closed/unmerged | open | issue (closed) |
|---|---:|---:|---:|---:|---:|
| 스킬 대상 upstream `Yeachan-Heo/gajae-code` | 49 | 38 | 11 | 0 | 23 |
| 자기 저장소 `yazzang-homelab/*` | 17 | 5 | 3 | 9 | 0 |
| 다른 외부 저장소 | 3 | 0 | 2 | 1 | 2 |
| 합계 | **69** | **43** | **16** | **10** | **25** |

PR 43/69 (62.32%)라는 비율은 관측 시점 **기여 객체의 처분 비율**이며 스킬의 인과적 성공률이 아니다. open 10건은 실패로 단정하지 않는다. 자기 저장소의 merge와 upstream 관리자의 채택도 구별한다. 이슈 25건의 closed는 API 상태이며 실제 해결·중복·범위 제외 여부는 공개 근거를 따로 판독해야 한다.

[현행 로컬 원장](LEDGER.md)은 **38개 quest의 현재 스냅샷**으로 이 보고서의 94개 작성 객체와 분모가 다르다. 22개 locator 중 직접 일치하는 것은 **21개(PR 14: 실제 merged 12, closed/unmerged 2; issue 7: closed)**이다. 유일한 비작성자 locator인 [#5154](https://github.com/Yeachan-Heo/gajae-code/pull/5154)는 원장에 있지만 작성자 분모에 추가하지 않는다. 원장 #4956의 `merged`는 commit 승계 예외이며 PR 자체의 merge가 아니다. #5290은 원장에서 `closed`를 유지한다. 작성 PR #5152의 후속 관계는 직접 locator 일치와 별개다.

다음 네 판단을 혼합하지 않는다.

1. **PR merge:** 해당 PR의 `merged_at` 및 merge commit에 근거한다.
2. **코드 승계:** 별도 후속 PR·commit의 연결과 채택 근거가 필요하다. 원 PR의 merge 상태를 바꾸지 않는다.
3. **이슈 해결:** closed 상태만으로 확정하지 않는다. 수정 PR·commit, 중복 관계, 재현 결과의 증거 수준을 표시한다.
4. **스킬 귀속:** 원장 직접 일치 여부를 별도로 기록한다. 일치는 절차 준수나 인과적 효과까지 증명하지 않으며 원장 밖 기여를 자동으로 실적에 넣지 않는다.

공개본 `SKILL.md`의 첫 git commit은 `2026-08-26T14:52:28+09:00`이나 실제 최초 사용일의 증거는 아니다. 따라서 그 날짜 전후의 인과율을 비교하지 않는다. 설치본 `~/.gjc/agent/skills/gjc-quest/SKILL.md`는 이번 확인에서 없었고 새로 설치하지 않았다. 본 조사는 읽기 전용 일회 수집이며 절차 검사기·폴링·자동 제출을 도입하지 않는다. 목적은 기여의 재미와 성취이며 PR 건수 목표가 아니다.

## 구체적 채택과 증거 수준

- [#5440](https://github.com/Yeachan-Heo/gajae-code/pull/5440): [merge commit `884a0ee127c4b943ea4fd5286b27194645a440d1`](https://github.com/Yeachan-Heo/gajae-code/commit/884a0ee127c4b943ea4fd5286b27194645a440d1). `test/tools/image-gen.test.ts`의 실제 patch에서 Google/Antigravity/OpenRouter/Alibaba 네 provider의 요청·결과 `model.id` 보존 및 conversation model이 override하지 못한다는 단언을 확인하였다.
- [#5197](https://github.com/Yeachan-Heo/gajae-code/pull/5197): [merge commit `38513c614349127de4e039bc67c9cb6c7c963af2`](https://github.com/Yeachan-Heo/gajae-code/commit/38513c614349127de4e039bc67c9cb6c7c963af2). `model-selector-profiles.test.ts`의 실제 patch에서 반복 selector가 catalog/auth refresh당 1회 resolve하고 `credentialSessionId`를 보존한다는 단언을 확인하였다.
- [#3527](https://github.com/Yeachan-Heo/gajae-code/pull/3527): [merge commit `a28310bd06ef203137ad7b26adf74854cd32f969`](https://github.com/Yeachan-Heo/gajae-code/commit/a28310bd06ef203137ad7b26adf74854cd32f969). OAuth refresh 실패 루프의 upstream 수정 commit을 확인하였다. 원장 직접 일치가 없으므로 자동으로 스킬 실적으로 귀속하지 않는다.

세 commit 모두 GitHub compare `<sha>...dev`의 `behind_by=0`을 확인하였다. 이는 merge·현재 `dev` 포함 관계의 증거다. 앞 두 사례의 테스트 파일·단언 존재를 확인한 것이며 **이번에 해당 테스트를 실행한 것은 아니다**. #3527 역시 장애 실행 재현 결과가 아니다.

## upstream 미머지 PR 11건의 처분과 후속 경로

아래 11개 원 PR은 모두 `closed`, `merged_at=null`이다. 후속 채택을 원 PR의 merge로 바꾸거나 작성자 분모에 추가하지 않는다. 공개 연결 및 원격 merge·ancestry 확인은 실행 재현과 다른 증거다.

| 원 PR | 판독 | 공개 근거·후속 경로 |
|---|---|---|
| [#3514](https://github.com/Yeachan-Heo/gajae-code/pull/3514) | 제품 계약 부재로 폐기, 반영 경로 미확인 | [`product_direction`](https://github.com/Yeachan-Heo/gajae-code/pull/3514#issuecomment-5125765744) |
| [#3521](https://github.com/Yeachan-Heo/gajae-code/pull/3521) | 오너의 후속 PR로 코드 승계 | [오너 연결 댓글](https://github.com/Yeachan-Heo/gajae-code/pull/3521#issuecomment-5122405290)의 `implementation is preserved verbatim`, [#3523](https://github.com/Yeachan-Heo/gajae-code/pull/3523), `dev` merge 및 `behind_by=0` 확인 |
| [#3756](https://github.com/Yeachan-Heo/gajae-code/pull/3756) | 동일 작성자 재제출 채택 | [연결 댓글](https://github.com/Yeachan-Heo/gajae-code/pull/3756#issuecomment-5160150594), [#3759](https://github.com/Yeachan-Heo/gajae-code/pull/3759), `dev` merge 및 `behind_by=0` 확인 |
| [#3844](https://github.com/Yeachan-Heo/gajae-code/pull/3844) | 관리자 방향에 따른 폐기, 반영 경로 미확인 | [방향 댓글](https://github.com/Yeachan-Heo/gajae-code/pull/3844#issuecomment-5204510008), 이후 `tier3_defer` |
| [#3910](https://github.com/Yeachan-Heo/gajae-code/pull/3910) | 혼합·부분 후속, 원 PR 전체 채택으로 단정하지 않음 | writer 결함은 오너 [#4054](https://github.com/Yeachan-Heo/gajae-code/pull/4054), 기존 poisoned registry parser는 동일 작성자 [#4249](https://github.com/Yeachan-Heo/gajae-code/pull/4249)로 후속; #4249 merge metadata 확인 |
| [#3931](https://github.com/Yeachan-Heo/gajae-code/pull/3931) | 관리자 방향에 따른 폐기, 반영 경로 미확인 | [방향 댓글](https://github.com/Yeachan-Heo/gajae-code/pull/3931#issuecomment-5204509164), 이후 `tier3_defer` |
| [#4309](https://github.com/Yeachan-Heo/gajae-code/pull/4309) | 오너의 후속 PR로 코드 승계 | [오너 연결 댓글](https://github.com/Yeachan-Heo/gajae-code/pull/4309#issuecomment-5261326016)의 `preserves the contributor commit with -x attribution`, [#4312](https://github.com/Yeachan-Heo/gajae-code/pull/4312), `dev` merge 및 `behind_by=0` 확인 |
| [#4466](https://github.com/Yeachan-Heo/gajae-code/pull/4466) | 원안 폐기, 혼합·부분 후속 | [종료 설명](https://github.com/Yeachan-Heo/gajae-code/pull/4466#issuecomment-5281081277)은 identity-loss·legacy replay·lifecycle-resurrection·cap-semantics 문제를 명시. self-quarantine은 동일 작성자 [#4470](https://github.com/Yeachan-Heo/gajae-code/pull/4470), log-only recovery는 [#4478](https://github.com/Yeachan-Heo/gajae-code/issues/4478)→오너 [#4495](https://github.com/Yeachan-Heo/gajae-code/pull/4495). 후자는 reporter attribution이지 원 코드 승계가 아님 |
| [#4956](https://github.com/Yeachan-Heo/gajae-code/pull/4956) | 직접 commit 승계, 원장의 기존 예외 유지 | [공개 설명](https://github.com/Yeachan-Heo/gajae-code/pull/4956#issuecomment-5416955880), [`a9ed03ba2073fda4ed8b0d9c556a104e45df3476`](https://github.com/Yeachan-Heo/gajae-code/commit/a9ed03ba2073fda4ed8b0d9c556a104e45df3476) 등 3개 commit의 작성자·anchor/test patch 및 `behind_by=0` 확인 |
| [#5152](https://github.com/Yeachan-Heo/gajae-code/pull/5152) | 오너의 후속 PR로 코드 승계 | [오너 연결 댓글](https://github.com/Yeachan-Heo/gajae-code/pull/5152#issuecomment-5489968077)의 `preserving the original commit attribution`, [#5154](https://github.com/Yeachan-Heo/gajae-code/pull/5154), `dev` merge 및 `behind_by=0` 확인. 원장 locator는 후속이므로 #5152의 직접 일치는 없음 |
| [#5290](https://github.com/Yeachan-Heo/gajae-code/pull/5290) | 다른 작성자의 구현 채택, 원 코드 승계로 집계하지 않음 | [공개 설명](https://github.com/Yeachan-Heo/gajae-code/pull/5290#issuecomment-5548924781), `lee98www`의 [#5294](https://github.com/Yeachan-Heo/gajae-code/pull/5294) merge 및 `behind_by=0`. generator ownership 및 가격 경계 test 증거가 더 강한 구현을 선택. 원 작성자의 역할은 corroborating evidence |

#5290의 공개 종료 결정은 같은 Astra 요구의 **single-winner** 채택이다. 그러므로 이전 로컬 분류 `product_direction`을 제품 방향 거절로 재사용하지 않고 공개 `LEDGER.md`의 원격 파생 cause만 `other`로 정정하였다. 로컬 상태 원장은 수정하지 않았다.

명확한 코드 승계는 **4건(#3521·#4309·#4956·#5152)**으로 구분한다. #3756의 재제출 #3759 및 부분 후속 #4249·#4470은 이미 작성자의 merged PR 38건에 포함되어 있으므로 다시 가산하지 않는다. #3910·#4466의 전체 코드 승계는 확정하지 않는다. 타인 작성 #3523·#4054·#4312·#4495·#5154·#5294도 작성자 94건에 추가하지 않는다.

11개 원 PR의 inline review comments endpoint는 모두 0개였다. 후속 #3523·#3759·#4054·#4249·#4312·#4470·#4495·#5154·#5294는 모두 `merged`, `base=dev`, 현재 `dev`에 대한 merge commit `behind_by=0`을 추가 확인하였다. 이는 각 후속의 채택 확인이지 원 PR 전체의 코드 동일성 증명이 아니다.

## 이슈 25건: 종료와 해결 근거 구분

25건 모두 원격에서 `closed/completed`이며 open 0, `not_planned` 0이다. 이번 판독에서 중복으로 확인한 항목은 0건이다. **명시적 해결 연결과 반영을 확인한 17건, 일부 계약만 해결한 3건, 해결 미확인 4건, 작성자 철회 1건**으로 구분한다. 여기서 해결 확인은 공개 수정 관계·반영 증거의 확인이며 모든 요구사항의 완전 충족·현재 버전 실행 재현·배포 확인이 아니다. `completed`는 fix와 동의어가 아니다.

아래 번호는 별도 저장소 표기가 없으면 `Yeachan-Heo/gajae-code`다.

해결·부분 해결 분류는 후속 PR 18개의 현재 `merged_at`과 본문의 `Fixes`/`Closes`·부분 범위 선언, 별도 앱 commit의 `Resolves #13`·종료 연결을 직접 대조하였다. 남은 8개 이슈(#3723·#3761·#3871·#3936·#3940·#3942·#3945 및 외부 #76241)의 댓글은 추가로 전부 조회하여 종료·보류·철회 사유를 판독하였다. 이는 25개 이슈의 모든 댓글 원문을 전부 읽었다는 주장이 아니다.

| issue | 판독 | 공개 근거와 한계 |
|---|---|---|
| [#3722](https://github.com/Yeachan-Heo/gajae-code/issues/3722) | 해결 관계·반영 확인 | merged [#3734](https://github.com/Yeachan-Heo/gajae-code/pull/3734)의 `Fixes #3722` |
| [#3723](https://github.com/Yeachan-Heo/gajae-code/issues/3723) | 부분 해결 | merged [#3724](https://github.com/Yeachan-Heo/gajae-code/pull/3724)는 item 3의 403 처리만 구현. `credential_switched`/401 parity는 명시 제외 |
| [#3761](https://github.com/Yeachan-Heo/gajae-code/issues/3761) | 부분 해결 | merged [#3763](https://github.com/Yeachan-Heo/gajae-code/pull/3763)는 reporting half만 수정. daemon activation 자체는 명시 제외 |
| [#3762](https://github.com/Yeachan-Heo/gajae-code/issues/3762) | 해결 관계·반영 확인 | merged [#3768](https://github.com/Yeachan-Heo/gajae-code/pull/3768)의 `Fixes #3762`: 죽은 소유자 복구 진단·identity-bound 재시도 |
| [#3871](https://github.com/Yeachan-Heo/gajae-code/issues/3871) | 부분 해결 | merged [#3872](https://github.com/Yeachan-Heo/gajae-code/pull/3872)의 `Fixes the first half of #3871`: NFC 정규화. escaped Hangul 허용 범위는 해결 미확인 |
| [#3928](https://github.com/Yeachan-Heo/gajae-code/issues/3928) | 해결 관계·반영 확인 | merged [#3932](https://github.com/Yeachan-Heo/gajae-code/pull/3932)의 `Closes #3928`: 생성 docs index 추적 제거 |
| [#3929](https://github.com/Yeachan-Heo/gajae-code/issues/3929) | 해결 관계·반영 확인 | merged [#3932](https://github.com/Yeachan-Heo/gajae-code/pull/3932)의 `Closes #3929`: CHANGELOG `merge=union` 제거. 기존 손실 복원은 별도 범위 |
| [#3936](https://github.com/Yeachan-Heo/gajae-code/issues/3936) | 해결 미확인 | [관리자 방향 종료](https://github.com/Yeachan-Heo/gajae-code/issues/3936#issuecomment-5204511587) 후 [Tier 3 보류](https://github.com/Yeachan-Heo/gajae-code/issues/3936#issuecomment-5210410890). 해결 PR/commit 확인 없음 |
| [#3940](https://github.com/Yeachan-Heo/gajae-code/issues/3940) | 해결 미확인 | [관리자 방향 종료](https://github.com/Yeachan-Heo/gajae-code/issues/3940#issuecomment-5204511172) 후 [Tier 3 보류](https://github.com/Yeachan-Heo/gajae-code/issues/3940#issuecomment-5210411065). 관련 PR merge를 workflow 승인 문제 해결로 세지 않음 |
| [#3942](https://github.com/Yeachan-Heo/gajae-code/issues/3942) | 해결 미확인 | merged [#3941](https://github.com/Yeachan-Heo/gajae-code/pull/3941)·[#3946](https://github.com/Yeachan-Heo/gajae-code/pull/3946)은 방지 가드. [관리자 종료](https://github.com/Yeachan-Heo/gajae-code/issues/3942#issuecomment-5204510780) 후 [Tier 3 보류](https://github.com/Yeachan-Heo/gajae-code/issues/3942#issuecomment-5210411377). [9/12 복구 자기 보고](https://github.com/Yeachan-Heo/gajae-code/issues/3942#issuecomment-5204519941)는 목록 숫자도 불일치하여 전체 복구로 확정하지 않음 |
| [#3945](https://github.com/Yeachan-Heo/gajae-code/issues/3945) | 해결 미확인 | [관리자 방향 종료](https://github.com/Yeachan-Heo/gajae-code/issues/3945#issuecomment-5204510410) 후 [Tier 3 보류](https://github.com/Yeachan-Heo/gajae-code/issues/3945#issuecomment-5210411562). test 환경 격리 해결 확인 없음 |
| [#3975](https://github.com/Yeachan-Heo/gajae-code/issues/3975) | 해결 관계·반영 확인 | merged [#4017](https://github.com/Yeachan-Heo/gajae-code/pull/4017)의 제목 `fixes #3975` |
| [#4259](https://github.com/Yeachan-Heo/gajae-code/issues/4259) | 해결 관계·반영 확인 | merged [#4271](https://github.com/Yeachan-Heo/gajae-code/pull/4271)의 `Closes #4259`: crash fingerprint·journal/index·동의 기반 report |
| [#4478](https://github.com/Yeachan-Heo/gajae-code/issues/4478) | 해결 관계·반영 확인 | merged [#4495](https://github.com/Yeachan-Heo/gajae-code/pull/4495)의 `Fixes #4478`: journal 없이 남은 crash record 복구. reporter attribution은 원 코드 승계와 구별 |
| [#4481](https://github.com/Yeachan-Heo/gajae-code/issues/4481) | 해결 관계·반영 확인 | merged [#4509](https://github.com/Yeachan-Heo/gajae-code/pull/4509)의 `Closes #4481`: non-finite overlay geometry의 무한 padding 경로 수정 |
| [#4764](https://github.com/Yeachan-Heo/gajae-code/issues/4764) | 해결 관계·반영 확인 | merged [#4776](https://github.com/Yeachan-Heo/gajae-code/pull/4776)의 `Closes #4764`: retained-publication 실패 단계·errno 진단 |
| [#4855](https://github.com/Yeachan-Heo/gajae-code/issues/4855) | 해결 관계·반영 확인 | merged [#4874](https://github.com/Yeachan-Heo/gajae-code/pull/4874)의 `Closes #4855`: idle 표시의 세션 태그 |
| [#4867](https://github.com/Yeachan-Heo/gajae-code/issues/4867) | 해결 관계·반영 확인 | merged [#4872](https://github.com/Yeachan-Heo/gajae-code/pull/4872)의 `Fixes #4867`: image protocol 없는 터미널의 text-cell pet renderer |
| [#4908](https://github.com/Yeachan-Heo/gajae-code/issues/4908) | 해결 관계·반영 확인 | merged [#4917](https://github.com/Yeachan-Heo/gajae-code/pull/4917)의 `Closes #4908`: terminal quota 오류의 retryable-at 표시. 자동 대기·재시도 구현은 아님 |
| [#4977](https://github.com/Yeachan-Heo/gajae-code/issues/4977) | 해결 관계·반영 확인 | merged [#4981](https://github.com/Yeachan-Heo/gajae-code/pull/4981)의 `Closes #4977`: OAuth URL 복사 action/shortcut·narrow-pane OSC8 링크 |
| [#5001](https://github.com/Yeachan-Heo/gajae-code/issues/5001) | 해결 관계·반영 확인 | merged [#5004](https://github.com/Yeachan-Heo/gajae-code/pull/5004)의 `Closes #5001` |
| [#5002](https://github.com/Yeachan-Heo/gajae-code/issues/5002) | 해결 관계·반영 확인 | merged [#5005](https://github.com/Yeachan-Heo/gajae-code/pull/5005)의 `Closes #5002` |
| [#5039](https://github.com/Yeachan-Heo/gajae-code/issues/5039) | 해결 관계·반영 확인 | merged [#5041](https://github.com/Yeachan-Heo/gajae-code/pull/5041)의 `Closes #5039`. tmux 자기 pane 입력 차단 범위이며 전체 TTY 신뢰 경계 해결로 확대하지 않음 |
| [anthropics/claude-code#76241](https://github.com/anthropics/claude-code/issues/76241) | 작성자 철회 | [작성자 설명](https://github.com/anthropics/claude-code/issues/76241#issuecomment-4931554191)의 `not a claude-code / Bun bug` 및 `faulty RAM`. 이번 감사에서 현장 하드웨어 검증을 실행하지 않았으며 제품 수정 실적으로 세지 않음 |
| [devswha/gajae-code-app#13](https://github.com/devswha/gajae-code-app/issues/13) | 해결 관계·반영 확인 | [commit `816b03f201143c76bd756fa3bc6502db35b40bd2`](https://github.com/devswha/gajae-code-app/commit/816b03f201143c76bd756fa3bc6502db35b40bd2)의 `Resolves #13` 및 [closed event](https://api.github.com/repos/devswha/gajae-code-app/issues/events/30522059768), GraphQL closer의 동일 commit 직접 지정 확인. native image 전달이 아니라 `<images_input>` 경로 블록 전달 구현 |

부분 해결 3건 역시 관리자 방향 종료 후 Tier 3 보류 이력이 있다: #3723 [종료](https://github.com/Yeachan-Heo/gajae-code/issues/3723#issuecomment-5204513557)·[보류](https://github.com/Yeachan-Heo/gajae-code/issues/3723#issuecomment-5210406654), #3761 [종료](https://github.com/Yeachan-Heo/gajae-code/issues/3761#issuecomment-5204513181)·[보류](https://github.com/Yeachan-Heo/gajae-code/issues/3761#issuecomment-5210407935), #3871 [종료](https://github.com/Yeachan-Heo/gajae-code/issues/3871#issuecomment-5204512827)·[보류](https://github.com/Yeachan-Heo/gajae-code/issues/3871#issuecomment-5210408692). 이 종료 이력으로 제외된 계약까지 해결됐다고 추론하지 않는다.

## 재현 방법

[읽기 전용 수집기](tools/audit_contributions.py)는 다음 명령으로 공개 metadata·hash·timeline을 수집한다. 아래 명령은 재현 안내이며 게이트·포매터·테스트 실행 기록이 아니다.

```sh
python3 tools/audit_contributions.py --author yazzang-homelab --output /tmp/gjc-contributions-recheck.json
gh api --method GET search/issues -f q='is:public author:yazzang-homelab is:pr' -f per_page=100
gh api --method GET search/issues -f q='is:public author:yazzang-homelab is:issue' -f per_page=100
gh api --method GET --paginate 'repos/<owner>/<repo>/issues?creator=yazzang-homelab&state=all&per_page=100'
gh api repos/<owner>/<repo>/pulls/<number> --jq '{state,merged,merged_at,merge_commit_sha}'
gh api --paginate repos/<owner>/<repo>/issues/<number>/timeline
gh api repos/Yeachan-Heo/gajae-code/compare/<sha>...dev --jq .behind_by
```

REST 대조에서는 `pull_request` 존재 여부로 PR/issue를 구분하고 `(repo, kind, number)` key를 비교한다. 제목이나 후속 참조를 작성자 분모의 추가 객체로 세지 않는다. 현재 로컬 원장 이외의 상태 원장은 읽거나 수정하지 않았다.

## 공개 작성 실적 전수표

이 표는 **GitHub 공개 작성 실적 표**이며 quest의 `quest_id · source · state · pr · closure_cause` 5열 schema를 변경하지 않는다. 제목은 원문을 유지하였다. 시간은 모두 **Asia/Seoul, `+09:00`**으로 변환하였다. `—`는 merge 시각이 없음을 뜻한다. issue에는 merge 개념이 없다. 직접 일치는 `LEDGER.md` 38행의 locator만 비교한 결과이며 후속 관계는 포함하지 않는다.

### `Nikolaibibo/uconsole-buddy`

| link | title | kind | state | merged_at (+09:00) | 원장 직접 일치 |
|---|---|---|---|---|---|
| [#1](https://github.com/Nikolaibibo/uconsole-buddy/pull/1) | Add GJC (Gajae Code)/pi support, configurable socket path, and remote TCP transport | pr | open | — | 없음 |

### `Yeachan-Heo/gajae-code`

| link | title | kind | state | merged_at (+09:00) | 원장 직접 일치 |
|---|---|---|---|---|---|
| [#3722](https://github.com/Yeachan-Heo/gajae-code/issues/3722) | AGENTS.md discovery loads every ancestor file in full with no count, depth, or byte bound | issue | closed | — | 없음 |
| [#3723](https://github.com/Yeachan-Heo/gajae-code/issues/3723) | Complete and observe mid-session credential rotation: credential_switched event, 401 rotate-retry parity, terminal 403 | issue | closed | — | 없음 |
| [#3761](https://github.com/Yeachan-Heo/gajae-code/issues/3761) | notifications: non-interactive `notify setup` always fails to activate the daemon, persists the settings anyway, and reports "Unable to persist" | issue | closed | — | 없음 |
| [#3762](https://github.com/Yeachan-Heo/gajae-code/issues/3762) | notifications: `notify recovery` reports `left-contended` forever for a provably dead owner while `notify health` keeps advising "run recovery" — no diagnostic, no escape hatch, manual `rm` only | issue | closed | — | 없음 |
| [#3871](https://github.com/Yeachan-Heo/gajae-code/issues/3871) | Deep Interview corrupts Korean state after #3716: round identity is not Unicode-canonical and escaped Hangul is still accepted | issue | closed | — | 없음 |
| [#3928](https://github.com/Yeachan-Heo/gajae-code/issues/3928) | docs-index.generated.ts is a committed one-line-per-doc artifact that conflicts on every rebase — 6 of 10 real PR conflicts, 4 blocked by it alone | issue | closed | — | 없음 |
| [#3929](https://github.com/Yeachan-Heo/gajae-code/issues/3929) | CHANGELOG merge=union은 GitHub에 적용되지 않는다 — 유령 충돌 15건 + 릴리스된 섹션 조용한 오염(재현됨) | issue | closed | — | 없음 |
| [#3936](https://github.com/Yeachan-Heo/gajae-code/issues/3936) | PR verdict 블록이 강제되지 않는다 — 열린 PR 7건이 규칙 위반 merge-approved 보유 (자체 승인 포함) | issue | closed | — | 없음 |
| [#3940](https://github.com/Yeachan-Heo/gajae-code/issues/3940) | 외부 기여자 PR 6건이 워크플로 승인 대기(action_required)로 CI 0건 — 정책상 머지 불가 상태로 방치 | issue | closed | — | 없음 |
| [#3942](https://github.com/Yeachan-Heo/gajae-code/issues/3942) | 긴급: union 제거 여파로 열린 PR 10건의 CHANGELOG가 비워짐 — 가드 #3941 필요 | issue | closed | — | 없음 |
| [#3945](https://github.com/Yeachan-Heo/gajae-code/issues/3945) | model-registry.test.ts가 호스트 API 키 환경변수를 읽어 로컬에서만 실패 — 리뷰어가 유령 실패를 PR 탓으로 오인한다 | issue | closed | — | 없음 |
| [#3975](https://github.com/Yeachan-Heo/gajae-code/issues/3975) | auth-broker / auth-gateway commands are unreachable: documented verbs fall through to the chat prompt and are billed as a turn | issue | closed | — | 없음 |
| [#4259](https://github.com/Yeachan-Heo/gajae-code/issues/4259) | feat(postmortem): crash fingerprinting and assisted issue reporting (gjc crash report) | issue | closed | — | 없음 |
| [#4478](https://github.com/Yeachan-Heo/gajae-code/issues/4478) | Crash whose journal event was lost is unreportable although its log record survives | issue | closed | — | `GQ-20260813-crash-index-log-orphan` |
| [#4481](https://github.com/Yeachan-Heo/gajae-code/issues/4481) | Session main thread spins a full core with the event loop stopped, survives its terminal as a ppid=1 orphan | issue | closed | — | `GQ-20260813-session-loop-spin` |
| [#4764](https://github.com/Yeachan-Heo/gajae-code/issues/4764) | fix(sdk): retained-publication diagnostic names the wrong stage and drops actionable errnos | issue | closed | — | 없음 |
| [#4855](https://github.com/Yeachan-Heo/gajae-code/issues/4855) | Idle notifications discard the computed display sessionTag; flat-fallback idle bodies carry no session identity | issue | closed | — | `GQ-20260823-idle-session-identity` |
| [#4867](https://github.com/Yeachan-Heo/gajae-code/issues/4867) | Gajae Pet is unreachable in tmux and on every iOS SSH client — both suggested remedies are impossible there | issue | closed | — | 없음 |
| [#4908](https://github.com/Yeachan-Heo/gajae-code/issues/4908) | Quota exhaustion discards the unblock instant it already computed: the turn dies with a raw provider error and no "retryable at" signal | issue | closed | — | `GQ-20260824-usage-limit-auto-resume` |
| [#4977](https://github.com/Yeachan-Heo/gajae-code/issues/4977) | OAuth URLs cannot be copied intact from a pane narrower than the URL | issue | closed | — | `GQ-20260825-login-url-copy-integrity` |
| [#5001](https://github.com/Yeachan-Heo/gajae-code/issues/5001) | ask: empty free-text answer re-asks the identical question in an unbounded loop (deep-interview free-text option looks like it does nothing) | issue | closed | — | 없음 |
| [#5002](https://github.com/Yeachan-Heo/gajae-code/issues/5002) | ask: placeholder deep-interview question bodies are accepted and rendered verbatim (users see a question whose content is literally "unused") | issue | closed | — | 없음 |
| [#5039](https://github.com/Yeachan-Heo/gajae-code/issues/5039) | bug(tools): agent bash can write into its own tmux pane, and the injected text is recorded as a `user` turn | issue | closed | — | `GQ-20260828-self-pane-turn-forgery` |
| [#3514](https://github.com/Yeachan-Heo/gajae-code/pull/3514) | feat(ai): add Kiro as a first-class provider | pr | closed / unmerged | — | 없음 |
| [#3521](https://github.com/Yeachan-Heo/gajae-code/pull/3521) | fix(coding-agent): stop a second resume from crashing the session picker | pr | closed / unmerged | — | 없음 |
| [#3527](https://github.com/Yeachan-Heo/gajae-code/pull/3527) | fix(ai): stop a failed OAuth refresh from looping instead of disabling the credential | pr | closed / merged | 2026-07-30T07:10:54+09:00 | 없음 |
| [#3528](https://github.com/Yeachan-Heo/gajae-code/pull/3528) | fix(utils): honour deletion of an inherited credential env var | pr | closed / merged | 2026-07-30T07:11:20+09:00 | 없음 |
| [#3716](https://github.com/Yeachan-Heo/gajae-code/pull/3716) | fix(prompt): require literal UTF-8 in tool inputs | pr | closed / merged | 2026-08-03T03:10:37+09:00 | 없음 |
| [#3718](https://github.com/Yeachan-Heo/gajae-code/pull/3718) | fix(coding-agent): show current role bindings in the model assignment menu | pr | closed / merged | 2026-08-02T08:25:41+09:00 | 없음 |
| [#3724](https://github.com/Yeachan-Heo/gajae-code/pull/3724) | fix(ai): stop a generic 403 from mutating credential state | pr | closed / merged | 2026-08-03T08:10:37+09:00 | 없음 |
| [#3756](https://github.com/Yeachan-Heo/gajae-code/pull/3756) | feat(auth): pair Anthropic OAuth by pasting the displayed code | pr | closed / unmerged | — | 없음 |
| [#3757](https://github.com/Yeachan-Heo/gajae-code/pull/3757) | fix(models): explain the missing credential source in custom-provider validation | pr | closed / merged | 2026-08-03T04:50:43+09:00 | 없음 |
| [#3758](https://github.com/Yeachan-Heo/gajae-code/pull/3758) | fix(tui): survive a stdin EIO when the controlling terminal disappears | pr | closed / merged | 2026-08-03T08:10:34+09:00 | 없음 |
| [#3759](https://github.com/Yeachan-Heo/gajae-code/pull/3759) | feat(auth): pair Anthropic OAuth by pasting the displayed code | pr | closed / merged | 2026-08-03T05:15:51+09:00 | 없음 |
| [#3763](https://github.com/Yeachan-Heo/gajae-code/pull/3763) | fix(notify): report a failed Telegram setup by durable state, not code path | pr | closed / merged | 2026-08-03T23:11:04+09:00 | 없음 |
| [#3844](https://github.com/Yeachan-Heo/gajae-code/pull/3844) | fix(notifications): report why the Telegram daemon child exits before readiness (#3761) | pr | closed / unmerged | — | 없음 |
| [#3872](https://github.com/Yeachan-Heo/gajae-code/pull/3872) | fix(deep-interview): canonicalize Hangul before hashing and capping prose | pr | closed / merged | 2026-08-06T12:32:56+09:00 | 없음 |
| [#3880](https://github.com/Yeachan-Heo/gajae-code/pull/3880) | fix(coding-agent): hint marketplace-qualified spec when bare plugin install fails | pr | closed / merged | 2026-08-06T11:28:51+09:00 | 없음 |
| [#3897](https://github.com/Yeachan-Heo/gajae-code/pull/3897) | fix(notifications): deliver Telegram frames when the paired chat is not a forum | pr | closed / merged | 2026-08-06T12:13:22+09:00 | 없음 |
| [#3898](https://github.com/Yeachan-Heo/gajae-code/pull/3898) | fix(coding-agent): expand slash commands in non-interactive runs | pr | closed / merged | 2026-08-06T11:57:51+09:00 | 없음 |
| [#3899](https://github.com/Yeachan-Heo/gajae-code/pull/3899) | fix(ask): show multi-select state on remote asks | pr | closed / merged | 2026-08-06T10:26:02+09:00 | 없음 |
| [#3907](https://github.com/Yeachan-Heo/gajae-code/pull/3907) | fix(notifications): stop a failed reconciliation pass from exiting the Telegram daemon | pr | closed / merged | 2026-08-06T10:25:58+09:00 | 없음 |
| [#3910](https://github.com/Yeachan-Heo/gajae-code/pull/3910) | fix(notifications): clear the disconnect-grace deadline when a topic is archived | pr | closed / unmerged | — | 없음 |
| [#3931](https://github.com/Yeachan-Heo/gajae-code/pull/3931) | fix(coding-agent): name the condition that rejects a resident-cache root | pr | closed / unmerged | — | 없음 |
| [#3932](https://github.com/Yeachan-Heo/gajae-code/pull/3932) | fix(repo): remove the two files that conflict on every rebase | pr | closed / merged | 2026-08-06T20:25:32+09:00 | 없음 |
| [#3941](https://github.com/Yeachan-Heo/gajae-code/pull/3941) | fix(ci): block pull requests that delete released CHANGELOG history | pr | closed / merged | 2026-08-06T21:06:08+09:00 | 없음 |
| [#3965](https://github.com/Yeachan-Heo/gajae-code/pull/3965) | fix(notifications): stop a dead Telegram daemon from claiming it is ready | pr | closed / merged | 2026-08-07T09:05:10+09:00 | 없음 |
| [#4118](https://github.com/Yeachan-Heo/gajae-code/pull/4118) | fix(ai): stop stale OAuth refresh-token replay from revoking live grants | pr | closed / merged | 2026-08-10T07:41:47+09:00 | 없음 |
| [#4249](https://github.com/Yeachan-Heo/gajae-code/pull/4249) | fix(telegram): accept archive fences that retained a stray grace deadline | pr | closed / merged | 2026-08-12T01:33:33+09:00 | 없음 |
| [#4309](https://github.com/Yeachan-Heo/gajae-code/pull/4309) | fix(tui): emit a coalesced multi-Esc chunk as individual Escape presses | pr | closed / unmerged | — | 없음 |
| [#4327](https://github.com/Yeachan-Heo/gajae-code/pull/4327) | fix(notifications): settle Telegram topic archives in private chats | pr | closed / merged | 2026-08-12T20:36:07+09:00 | 없음 |
| [#4352](https://github.com/Yeachan-Heo/gajae-code/pull/4352) | fix(ai): reject tool arguments that spell non-ASCII text as \uXXXX escapes | pr | closed / merged | 2026-08-12T20:52:30+09:00 | 없음 |
| [#4415](https://github.com/Yeachan-Heo/gajae-code/pull/4415) | fix(ai): reload the credential snapshot when an OAuth row vanishes | pr | closed / merged | 2026-08-13T13:06:35+09:00 | 없음 |
| [#4466](https://github.com/Yeachan-Heo/gajae-code/pull/4466) | fix(crash): recover reportable signatures from crash-log records, and bound their dismissal by the log | pr | closed / unmerged | — | 없음 |
| [#4470](https://github.com/Yeachan-Heo/gajae-code/pull/4470) | fix(crash): stop compaction writing an index its own reader quarantines | pr | closed / merged | 2026-08-13T23:44:32+09:00 | `GQ-20260813-crash-index-self-quarantine` |
| [#4732](https://github.com/Yeachan-Heo/gajae-code/pull/4732) | fix(sdk): diagnose retained broker publication refusal | pr | closed / merged | 2026-08-20T20:06:14+09:00 | `GQ-20260819-broker-publication-obstruction` |
| [#4736](https://github.com/Yeachan-Heo/gajae-code/pull/4736) | fix(session): retry a content-free Anthropic capacity overload under bare defaults | pr | closed / merged | 2026-08-20T19:45:33+09:00 | `GQ-20260819-anthropic-overload-retry` |
| [#4737](https://github.com/Yeachan-Heo/gajae-code/pull/4737) | fix(auth): reload rotating agent env credentials | pr | closed / merged | 2026-08-20T07:52:41+09:00 | `GQ-20260820-rotating-agent-env-credential` |
| [#4906](https://github.com/Yeachan-Heo/gajae-code/pull/4906) | feat(ai): add Ox Alpha and recover empty streams | pr | closed / merged | 2026-08-24T19:37:06+09:00 | `GQ-20260824-ox-alpha-empty-stream` |
| [#4923](https://github.com/Yeachan-Heo/gajae-code/pull/4923) | feat(agent): log escaped-non-ASCII tool-argument discards and rejections | pr | closed / merged | 2026-08-24T21:57:22+09:00 | `GQ-20260824-escaped-nonascii-observability` |
| [#4956](https://github.com/Yeachan-Heo/gajae-code/pull/4956) | fix(tui): anchor the /login URL so narrow-pane fragments stay clickable | pr | closed / unmerged | — | `GQ-20260825-login-url-unlinked-wrap` |
| [#4985](https://github.com/Yeachan-Heo/gajae-code/pull/4985) | fix(deep-interview): report nested envelope-reserved keys instead of discarding them silently | pr | closed / merged | 2026-08-26T19:13:23+09:00 | `GQ-20260826-di-nested-phase-write-silent` |
| [#5101](https://github.com/Yeachan-Heo/gajae-code/pull/5101) | fix(ai): make pi-native transport work for custom providers | pr | closed / merged | 2026-09-01T08:17:28+09:00 | `GQ-20260831-pi-native-custom-provider-transport` |
| [#5152](https://github.com/Yeachan-Heo/gajae-code/pull/5152) | fix(tui): let a queued steer own the first Esc on a streaming turn | pr | closed / unmerged | — | 없음 |
| [#5184](https://github.com/Yeachan-Heo/gajae-code/pull/5184) | fix(ai): warn glm-zcode users about the desktop app consuming the login code | pr | closed / merged | 2026-09-02T13:21:07+09:00 | 없음 |
| [#5197](https://github.com/Yeachan-Heo/gajae-code/pull/5197) | perf(models): memoize repeated preset auth selectors | pr | closed / merged | 2026-09-03T03:37:35+09:00 | `GQ-20260902-preset-auth-sync-freeze` |
| [#5265](https://github.com/Yeachan-Heo/gajae-code/pull/5265) | perf(models): cache preset availability between refreshes | pr | closed / merged | 2026-09-04T19:47:54+09:00 | `GQ-20260904-preset-cursor-rerender-freeze` |
| [#5290](https://github.com/Yeachan-Heo/gajae-code/pull/5290) | feat(ai): bundle Codex GPT-6-Astra in the model catalog | pr | closed / unmerged | — | `GQ-20260905-codex-astra-catalog` |
| [#5389](https://github.com/Yeachan-Heo/gajae-code/pull/5389) | fix(auth-gateway): emit plain call_id for compound Codex tool ids | pr | closed / merged | 2026-09-07T21:29:48+09:00 | `GQ-20260907-gateway-compound-tool-id` |
| [#5419](https://github.com/Yeachan-Heo/gajae-code/pull/5419) | fix(session): await local migration after cwd moves | pr | closed / merged | 2026-09-11T18:56:30+09:00 | 없음 |
| [#5423](https://github.com/Yeachan-Heo/gajae-code/pull/5423) | fix(web-search): support streaming-only OpenAI-compatible servers | pr | closed / merged | 2026-09-12T03:59:25+09:00 | 없음 |
| [#5440](https://github.com/Yeachan-Heo/gajae-code/pull/5440) | fix(image): preserve the selected image-role model | pr | closed / merged | 2026-09-11T16:27:45+09:00 | `GQ-20260909-image-role-selected-model` |

### `anthropics/claude-code`

| link | title | kind | state | merged_at (+09:00) | 원장 직접 일치 |
|---|---|---|---|---|---|
| [#76241](https://github.com/anthropics/claude-code/issues/76241) | 2.1.206 linux-x64 ships a Bun baseline build that segfaults on startup (glibc 2.41) | issue | closed | — | 없음 |

### `devswha/gajae-code-app`

| link | title | kind | state | merged_at (+09:00) | 원장 직접 일치 |
|---|---|---|---|---|---|
| [#13](https://github.com/devswha/gajae-code-app/issues/13) | [Feature] Attached images never reach the model — adapter drops options.images before session.prompt() | issue | closed | — | `GQ-20260901-app-image-native-vision` |

### `mcpads/create-kr-patch-template`

| link | title | kind | state | merged_at (+09:00) | 원장 직접 일치 |
|---|---|---|---|---|---|
| [#1](https://github.com/mcpads/create-kr-patch-template/pull/1) | feat: patch-guard 판정을 MCP 도구로 노출하는 stdio 서버 추가 | pr | closed / unmerged | — | 없음 |

### `mcpads/create-retro-game-kr-patch`

| link | title | kind | state | merged_at (+09:00) | 원장 직접 일치 |
|---|---|---|---|---|---|
| [#3](https://github.com/mcpads/create-retro-game-kr-patch/pull/3) | feat: 핵심 불변식을 실행 판정하는 patch-guard MCP 서버를 플러그인에 통합 (1.1.0) | pr | closed / unmerged | — | 없음 |

### `yazzang-homelab/hancharacter`

| link | title | kind | state | merged_at (+09:00) | 원장 직접 일치 |
|---|---|---|---|---|---|
| [#1](https://github.com/yazzang-homelab/hancharacter/pull/1) | docs(skill): make the description findable from a ROM-localisation query | pr | open | — | 없음 |

### `yazzang-homelab/hanpatch`

| link | title | kind | state | merged_at (+09:00) | 원장 직접 일치 |
|---|---|---|---|---|---|
| [#1](https://github.com/yazzang-homelab/hanpatch/pull/1) | smoke: agent-approval-check end to end | pr | closed / unmerged | — | 없음 |
| [#2](https://github.com/yazzang-homelab/hanpatch/pull/2) | proof: protected main refuses an unapproved agent commit | pr | closed / unmerged | — | 없음 |
| [#3](https://github.com/yazzang-homelab/hanpatch/pull/3) | smoke: 개죽이 알림에 PR 요약이 실리는지 확인 | pr | closed / unmerged | — | 없음 |
| [#4](https://github.com/yazzang-homelab/hanpatch/pull/4) | harvest: 계획의 근거 숫자를 다시 계산해서 파일로 남김 | pr | closed / merged | 2026-08-07T09:00:48+09:00 | 없음 |
| [#5](https://github.com/yazzang-homelab/hanpatch/pull/5) | recipe: 컨테이너에서 스키마를 귀납 (단계 0) | pr | closed / merged | 2026-08-12T10:17:42+09:00 | 없음 |
| [#6](https://github.com/yazzang-homelab/hanpatch/pull/6) | Leave PSP firmware-owned dialogs untranslated | pr | closed / merged | 2026-08-20T20:19:07+09:00 | 없음 |
| [#7](https://github.com/yazzang-homelab/hanpatch/pull/7) | Record runtime-owned slots and waiver discipline in the skill | pr | closed / merged | 2026-08-20T20:47:17+09:00 | 없음 |
| [#8](https://github.com/yazzang-homelab/hanpatch/pull/8) | fix(cdx2): D2 glyph cell drift and D3 retargeted cells | pr | open | — | 없음 |
| [#9](https://github.com/yazzang-homelab/hanpatch/pull/9) | fix(cdx2): protect creation operands and extract prologue | pr | open | — | 없음 |
| [#10](https://github.com/yazzang-homelab/hanpatch/pull/10) | fix(josa): a particle after a run-time placeholder was never checked | pr | closed / merged | 2026-08-26T18:32:22+09:00 | 없음 |
| [#11](https://github.com/yazzang-homelab/hanpatch/pull/11) | test: run the josa runtime-token regression in the check suite | pr | open | — | 없음 |
| [#12](https://github.com/yazzang-homelab/hanpatch/pull/12) | Integrate PR8+PR9: D2/D3 font cells with opening operands | pr | open | — | 없음 |
| [#13](https://github.com/yazzang-homelab/hanpatch/pull/13) | feat(psp): read the .DMD container, and correct D4's premise | pr | open | — | 없음 |
| [#14](https://github.com/yazzang-homelab/hanpatch/pull/14) | docs(skill): name the voice gate, and the three companions the skill never pointed at | pr | open | — | 없음 |
| [#15](https://github.com/yazzang-homelab/hanpatch/pull/15) | feat(psp): gzip image surfaces in .LDT, and the prologue reinjection path | pr | open | — | 없음 |
| [#16](https://github.com/yazzang-homelab/hanpatch/pull/16) | feat(psp): read PARAM.SFO and replace the title in place | pr | open | — | 없음 |
