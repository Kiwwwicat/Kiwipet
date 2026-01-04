# 버그 수정

Kiwipet의 버그를 조사하고 수정합니다.

## 버그 설명
$ARGUMENTS

## 작업 순서

1. 관련 코드 영역 탐색
2. 문제 원인 분석
3. 수정 방안 제시
4. 코드 수정
5. 빌드 및 테스트

## 자주 발생하는 문제 패턴

### 키 타입 불일치
- AI 캐시 interaction 키: `int` (예: `0`, `1`)
- 대사 dialogues 키: `str` (예: `'char_0'`)
- JSON 저장 시 int 키가 string으로 변환됨
```python
# 로드 시 int 변환 필요
for k, v in raw_interaction.items():
    try:
        converted[int(k)] = v
    except (ValueError, TypeError):
        converted[k] = v
```

### 캐시 손실
- `save_characters()`에서 빈 캐시 시 기존 파일 캐시 유지 확인
- AI 대사 생성 OFF 시 기존 캐시 보존 필요

### 캐릭터 사라짐
- 파일 탐색기 등 다른 창 닫힐 때 캐릭터 숨겨짐
- `check_characters_visibility` 타이머로 복구

### 중복 이름 처리
- `make_unique_names()` 함수가 `(2)`, `(3)` 접미사 추가
- AI 응답 파싱 시 접미사 제거 필요
