# 서부전선 1918

브라우저에서 실행하는 3D 전쟁 게임입니다. **V17.7 — 거점수비와 시험병기**를 개발 기준점으로 저장했습니다.

## 실행

Python 3을 설치한 뒤 저장소 폴더에서 실행합니다.

```powershell
python -m http.server 8000
```

브라우저에서 `http://localhost:8000`을 엽니다. 개발본은 음원을 로컬 파일로 읽으므로 HTTP 서버로 실행합니다.

## 단일 HTML 만들기

```powershell
python tools/build.py
```

`dist/1918_V18.1.html`이 만들어집니다. 이 배포 파일은 음원이 내장되어 있어 브라우저에서 직접 열 수 있습니다. `dist/`는 Git 추적 대상에서 제외했습니다.

## 개발 기준

- `index.html`: 현재 게임 소스. 다음 수정은 이 파일을 기준으로 합니다.
- `assets/media/`: 기존 HTML에서 추출한 음원·이미지. 동일한 콘텐츠는 한 번만 저장합니다.
- `assets/manifest.json`: 미디어 경로, MIME, SHA-256 및 V17.7 원본 체크섬.
- `tools/build.py`: 외부 미디어를 내장해 단일 HTML로 재조립하는 도구.
- `tools/check.cjs`: Node.js를 이용한 인라인 JavaScript 구문 검사.
- `THIRD_PARTY_NOTICES.md`: 외부 자료와 음원 출처.

현재 게임은 기존 HTML 구조를 보존해 가져왔습니다. 주요 기능은 작전·대지역 점령, 일곱 주전장, 28개 외곽 배치, 차량·열차, 거점 수비 배치와 시험병기 보급입니다.

## 변경 및 기록

기능별 브랜치와 커밋을 만들고, `CHANGELOG.md`와 `VERSION`을 함께 갱신합니다.

```powershell
git switch -c codex/작업이름
# 수정 후
node tools/check.cjs
python tools/build.py
git add index.html assets tools VERSION CHANGELOG.md
git commit -m "변경 내용"
git push -u origin HEAD
```

브랜치 내용을 검토한 뒤 `main`에 반영합니다. 기준 태그는 `v17.7`입니다.

초기 가져오기를 검증할 때만 다음 명령을 사용합니다. 개발 후에는 원본과 달라지는 것이 정상입니다.

```powershell
python tools/build.py --verify-baseline
```
