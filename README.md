# 디스코드 메이플 봇

디스코드 메이플 봇입니다.

## 봇 서버 세팅 방법

- `.env` 파일을 다음과 같이 설정합니다.

```text
DISCORD_TOKEN="<your_discord_server_token>"
```

- 봇 실행
  - 실행 전에 현재 폴더에 캐릭터 사진 저장을 위한 `char_img` 폴더를 생성합니다.

```bash
$ pip3 install -r requirements.txt
$ mkdir char_img
$ python3 bot.py
```

## 디스코드 서버에 추가
- 아래 링크를 눌러 추가하면 됩니다.
- 서버의 관리자 권한이 있어야 합니다.
- https://discord.com/oauth2/authorize?client_id=417300457048768512&scope=bot&permissions=

## 명령어 목록

해당 명령어를 클릭하면 명령어의 설명으로 이동할 수 있습니다.

- [도움말](#도움말)

- 캐릭터 정보 관련 명령어
  - [정보](#정보)
  - [경험치](#경험치)

- 기타
  - [주사위](#주사위)

## 도움말
- 사용법: `!도움말` 혹은 `!도움말 [명령어]`

지원하는 모든 명령어 목록을 출력합니다. `[명령어]` 옵션이 주어지면 해당 명령어의 자세한 정보를 출력합니다.

## 정보
- 사용법: `!정보 [닉네임]`

해당 캐릭터의 정보를 출력합니다. 이 정보는 maple.gg 에서 가져오기 때문에 갱신에 시간이 조금 걸릴 수도 있습니다.

### 확인 가능한 정보
- 캐릭터가 속한 월드
- 캐릭터 이미지
- 직업
- 레벨
- 종합 랭킹, 월드 랭킹, 직업 랭킹 (월드), 직업 랭킹 (전체)
- 길드
- 인기도
- 무릉도장, 더 시드 기록
- 메이플 유니온 레벨, 유니온 전투력
- 업적, 업적 점수
- 마지막 활동일

## 경험치
- 사용법: `!경험치 [닉네임]`

해당 캐릭터의 경험치 정보를 출력합니다. 이 정보는 메이플 공식 홈페이지 랭킹에서 가져옵니다. 공식 홈페이지 랭킹은 실시간 반영되지 않으므로 오차가 있을 수 있습니다.

### 확인 가능한 정보
- 캐릭터가 속한 월드
- 캐릭터 이미지
- 직업
- 레벨
- 현재 경험치량 및 퍼센트
- Lv.250, Lv.275 까지 각각 필요한 경험치량 및 달성률

## 주사위
- 사용법: `!주사위` 또는 `!데굴데굴`

주사위를 굴립니다. 1 부터 100 까지의 결과가 나오고, 인벤의 주사위 결과와 동일한 메시지가 출력됩니다.
