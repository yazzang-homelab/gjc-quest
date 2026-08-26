# gjc-quest

> [gajae-code](https://github.com/Yeachan-Heo/gajae-code)(gjc)를 쓰다 마주친 결함을 **퀘스트**로 띄워, 사람이 수락한 것만 upstream 기여로 바꾸는 GJC 스킬.

*[English](README.md) · 한국어*

**소개 사이트: https://yazzang-homelab.github.io/gjc-quest/**

에이전트에게 "gjc 버그 찾아서 PR 내"라고 시키면 십중팔구 draft PR 더미와 진단 로그 개선
PR이 쌓여 메인테이너 큐를 오염시킨다. 이 스킬은 그 반대를 강제한다 — **탐지는 자동,
판단과 전송은 전부 사람.**

```
탐지 → 유효성 확인(현행 dev에 살아 있나) → 등급 판정 → 배제 뷰 통과
     → 퀘스트 카드(사람이 수락/거절/보류) → 세 게이트 순차 통과
     → 사람이 직접 전송 → 원장 기록 → 관측 노트 누적
```

## 무엇이 다른가

- **사람 게이트가 두 개**, 서로 독립이다. ① 수락(intake) — 이걸 퀘스트로 삼을지.
  ② 전송(transmission) — 실제로 원격에 낼지. ①이 ②를 허락하지 않는다.
- **동시 진행 슬롯은 하나.** 두 번째 `accepted` 행을 만들 수 없다. WIP 개수 상한 같은
  숫자 예산은 쓰지 않고 구조로 막는다.
- **전송 전 세 게이트를 순서대로** 평가하고 첫 실패에서 단락한다 —
  `maintainer_prohibition` → `freeze` → contract/state validity.
- **Pre-intake validity.** 로컬 설치본은 upstream `dev`보다 늘 낡다. 등급 판정 전에
  "이미 착륙했나 / 현행 dev에 경로가 살아 있나 / 깨끗한 HOME에서도 재현되나 /
  (HIGH 전용) 크래시 지문이 저널에 있나"를 확인한다. 여기서 떨어지면 카드를 안 올린다.
- **Minimality gate.** 한 PR은 결함 하나, 최소 수정. 정답이 둘 이상이면 그건 결함이
  아니라 제품 결정이므로 코드가 아니라 별도 이슈로 내려간다. 독립 리뷰 두 번에 blocker가
  남으면 멈춘다 — 세 번째 재설계는 설계 권한을 빌리는 것이다.
- **Decision block.** 선택지를 나열만 하는 카드는 유효한 카드가 아니다. 선택지마다
  "고르면 벌어지는 일 / 유리한 점 / 불리한 점"을 채우고 권장 하나와 근거를 단다.
- **다섯 필드 원장.** `quest_id · source · state · pr · closure_cause`. 여섯 번째 열도,
  `candidate` 같은 유사 상태도 없다. 원격 현재 상태는 마크다운에 복사하지 않고 읽기 전용
  `gh`로 파생한다(이중 기장 금지).
- **freeze 감지.** 리뷰 없는 일괄 close, `do not open` 류 문구, 내 항목이 24시간 안에
  여럿 close됨 — 하나라도 관측되면 PR·이슈 전송이 0이 되고 로컬 카드로 통보한다.
  해제는 경과 시간이 아니라 오너가 다시 리뷰·머지하는 이벤트로만 한다.

## 하지 않는 것

- 정기 배치·상시 폴링·백그라운드 타이머를 만들지 않는다(`cron`은 세션과 함께 소멸한다).
  사람이 시각을 지정한 1회 현황 보고만 예외다.
- 자동 제출을 하지 않는다. push·PR 생성·이슈 생성은 사람 승인 뒤에만, 그 head sha에만.
- 메인테이너에게 허가를 묻지 않는다. 증거를 담은 범위 밖 결함 이슈만 예외이며 그것도
  독촉하지 않는다.
- `gjc crash report`를 재구현하지 않는다 — 감싼다.
- 설정 파일을 바꾸지 않는다. 훅을 설치하지 않는다.

## 설치

**스킬 파일은 곧 프롬프트다.** `~/.gjc/agent/skills/`에 넣는 순간 에이전트 실행 경로에
텍스트가 꽂히므로 다른 공급망 산출물과 똑같이 다뤄야 한다 — 리비전을 고정하고, 바이트를
검증하고, 설치 전에 diff를 읽는다. `curl | main`은 충분하지 않고, 이 저장소는 그걸 권하지
않는다.

```sh
# 1. 리비전 고정 — 태그나 커밋 sha. 움직이는 브랜치는 쓰지 않는다
REV=v0.1.0

# 2. 스킬 디렉터리가 아니라 스테이징 경로로 받는다
curl -fsSL "https://raw.githubusercontent.com/yazzang-homelab/gjc-quest/$REV/SKILL.md" \
  -o /tmp/gjc-quest.SKILL.md
curl -fsSL "https://raw.githubusercontent.com/yazzang-homelab/gjc-quest/$REV/SHA256SUMS" \
  -o /tmp/gjc-quest.SHA256SUMS

# 3. 바이트를 검증하고, 통과한 뒤에만 설치한다
(cd /tmp && sed 's| SKILL.md$| gjc-quest.SKILL.md|' gjc-quest.SHA256SUMS | sha256sum -c -)
install -Dm644 /tmp/gjc-quest.SKILL.md ~/.gjc/agent/skills/gjc-quest/SKILL.md
```

**출처 증명.** `SKILL.md`를 건드리는 모든 푸시가 Sigstore 빌드 출처 증명을 발행한다. 파일과
같은 곳에서 받은 체크섬이 아니라, 이 저장소와 이 워크플로에 파일을 결속해 확인할 수 있다.

```sh
gh attestation verify /tmp/gjc-quest.SKILL.md --repo yazzang-homelab/gjc-quest
```

CI는 `SHA256SUMS`가 `SKILL.md`와 어긋나는 커밋을 거부한다
([`skill.yml`](.github/workflows/skill.yml)) — 낡은 체크섬은 없는 것보다 나쁘다. 검증을
건너뛰는 습관을 가르치기 때문이다. **PGP 서명은 없다.** 제공되는 출처 증명은 attestation과
커밋 히스토리이고, 830줄 한국어 산문은 사람이 읽을 수 있는 diff다.

`config.yml`의 `skills.enabled`와 `skills.enablePiUser`가 참이어야 로드된다. **설정을 켠
직후 세션에는 반영되지 않는다** — 새 세션에서 호출한다. 스킬은 설정을 바꾸지 않는다.

호출: `/skill:gjc-quest`. 별칭 — `gjc quest`, `quest scan`, `gjc 퀘스트`, `결함 퀘스트`,
`퀘스트 스캔`, `기여할 거 있나`, `이거 PR 낼까`.

## 로컬 상태

원장과 관측 노트는 `~/.gjc/agent/state/gjc-quest-ledger.md` 한 파일에 붙는다.
새 JSONL을 만들지 않는다. 손상·중복 섹션을 발견하면 고쳐 쓰지 않고 보류한다.

**관측 노트는 로컬 전용이다.** 관측(직접 사건)과 추단(해석)을 물리적으로 분리해 적고,
어느 쪽도 원격으로 내보내지 않는다. 이 저장소도 노트 내용을 담지 않는다 — 배제 뷰 네
부류는 고정 목록이 아니라 각자가 자기 관측에서 채우는 빈 뷰다.

## 범위

`Yeachan-Heo/gajae-code` 전용이다. 대상 브랜치는 항상 `dev`이고, `gjc crash report`·
`gjc notify`·PR verdict 블록처럼 gjc에만 있는 표면을 전제한다. 다른 저장소에 그대로
쓰려면 그 부분을 다시 써야 한다.

비공식 서드파티 스킬이며 upstream과 제휴 관계가 없다.

## 이 규율을 실제로 지키는가

타당한 의문이다 — 절차가 촘촘하다는 것이 매번 지켰다는 증명은 아니고, 문서로는 증명할 수
없다. [**`LEDGER.md`**](LEDGER.md)가 이 스킬이 실제로 써 온 원장이다. 25건 전부, 로케이터는
export 시점에 읽기 전용 `gh`로 하나씩 재파생했다 — **착륙 5건, 원격 객체를 아예 만들지 않은
것 15건.** 거절과 로컬 보류 쪽이 읽을 값이 있는 부분이다.

## License

MIT. [`LICENSE`](LICENSE) 참조.
