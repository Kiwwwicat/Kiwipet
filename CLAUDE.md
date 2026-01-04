# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Build Commands

```bash
# Install dependencies
pip install PyQt5 Pillow pywin32 pyinstaller

# Build executable (using spec file)
py -m PyInstaller --clean Kiwipet.spec

# Or build directly
py -m PyInstaller --onefile --windowed --hidden-import=PyQt5.QtSvg --add-data "Pretendard-Medium.otf;." --add-data "Pretendard-Bold.otf;." --icon=kiwipet.ico --name "Kiwipet" kiwipet.py

# Run directly without building
py kiwipet.py
```

Build output: `dist/Kiwipet.exe`

---

## Architecture

**Single-file PyQt5 application** (`kiwipet.py`, ~13,500 lines) - A Windows desktop pet that walks on screen/window edges.

### Core Features
- User-uploaded images as character sprites
- Characters walk on screen bottom/window edges
- Character interactions and events
- Google Gemini API for AI dialogue generation
- Per-character personality, relationships, nicknames
- App window size scaling (100%~200%)

### 모듈 파일

| 파일 | 설명 |
|------|------|
| `kiwipet.py` | 메인 애플리케이션 |
| `app_scale.py` | 앱 크기 조절 기능 모듈 (kiwipet.py에서 import) |

> **빌드 시 모듈 처리**: PyInstaller가 kiwipet.py의 import문을 분석하여 app_scale.py를 자동으로 exe에 포함시킵니다.

### app_scale.py 모듈

앱 창 크기를 조절하는 기능 모듈입니다. `kiwipet.py`에서 import하여 사용합니다.

```python
# kiwipet.py에서의 import
from app_scale import (
    create_app_scale_section,
    calculate_scaled_size,
    apply_scale_to_window,
    DEFAULT_APP_SCALE,
    BASE_WIDTH,
    BASE_HEIGHT
)
```

**상수:**
- `DEFAULT_APP_SCALE = 100` - 기본 스케일
- `MIN_APP_SCALE = 100` - 최소 스케일
- `MAX_APP_SCALE = 200` - 최대 스케일
- `BASE_WIDTH = 650` - 기본 창 너비
- `BASE_HEIGHT = 750` - 기본 창 높이
- `PRESET_VALUES = [100, 125, 150, 200]` - 프리셋 버튼 값

**함수:**
- `create_app_scale_section(parent, current_scale, callback)` - UI 섹션 생성, (widget, slider) 튜플 반환
- `calculate_scaled_size(scale)` - 스케일에 따른 창 크기 계산, (width, height) 튜플 반환
- `apply_scale_to_window(window, scale, save_callback)` - 윈도우에 스케일 적용

---

## 🏗️ 코드 구조

### 전역 변수 (Line 1~430)
```python
_gemini_api_key = ""           # Gemini API 키
_ai_enabled = False            # AI 기능 활성화
_ai_dialogues_cache = {}       # AI 생성 대사 캐시
_temp_dialogues_cache = {}     # 시간/날씨 기반 임시 대사
_ssl_context                   # SSL 컨텍스트
_win32_available               # win32gui 사용 가능 여부
```

### 주요 클래스

| 클래스 | 라인 | 설명 |
|--------|------|------|
| `ToggleSwitch` | ~291 | 토글 스위치 위젯 |
| `IconButton` | ~357 | 아이콘 버튼 위젯 |
| `CharacterWidget` | ~1464 | **핵심** - 화면에 표시되는 캐릭터 |
| `CharacterCard` | ~3662 | 메인 윈도우의 캐릭터 카드 UI |
| `AIDialogueViewDialog` | ~4141 | AI 대사 열람/편집 다이얼로그 |
| `PersonalityDialog` | ~4671 | 캐릭터 성격 설정 다이얼로그 |
| `DialogueDialog` | ~5373 | 대사 편집 다이얼로그 |
| `RelationshipDialog` | ~5785 | 관계 설정 다이얼로그 |
| `BubbleColorDialog` | ~6100 | 말풍선 색상 다이얼로그 |
| `ScaleDialog` | ~6432 | 크기 조절 다이얼로그 |
| `MainWindow` | ~7124 | **핵심** - 메인 윈도우 |

### 주요 함수

| 함수 | 라인 | 설명 |
|------|------|------|
| `sync_dialogues_to_ai_cache` | ~464 | 수동 대사 → AI 캐시 동기화 |
| `clean_api_key` | ~567 | API 키에서 특수문자 제거 |
| `get_cached_dialogue` | ~717 | 캐시에서 대사 가져오기 |
| `make_unique_names` | ~760 | 중복 이름에 (2), (3) 접미사 추가 |
| `generate_dialogues_batch` | ~805 | AI 대사 일괄 생성 요청 |

---

## 📊 데이터 구조

### AI 대사 캐시 (`_ai_dialogues_cache`)
```python
_ai_dialogues_cache = {
    char_id: {                    # int 키
        'solo': ["혼잣말1", ...],
        'interaction': {
            other_char_id: ["대사1", ...],  # int 키
            'default': ["일반 대사", ...]
        },
        'fallback': ["폴백 대사", ...],
        'generated_at': timestamp
    }
}
```

### 수동 대사 (`self.dialogues`)
```python
self.dialogues = {
    char_id: {                    # int 키
        '기본': ["수동 대사1", ...],
        'char_0': ["캐릭터0에게", ...],  # 문자열 키!
        'char_1': ["캐릭터1에게", ...]
    }
}
```

### 관계 (`self.relationships`)
```python
self.relationships = {
    (min_id, max_id): {           # 튜플 키, 작은 ID가 앞
        char_id_a: "좋아함",       # A→B 감정
        char_id_b: "존경함"        # B→A 감정
    }
}
```

### 캐릭터 데이터 (`self.character_data`)
```python
self.character_data = {
    char_id: {
        'name': "캐릭터명",
        'image_path': "/path/to/image.png",
        'scale': 100,
        'bubble_color': "#81C784",
        'bubble_size': 100,
        'personality': "성격 설명",
        'background_story': "배경 스토리",
        'catchphrase': "캐치프레이즈",
        'nicknames': {other_id: "별명", ...},
        'stories': {other_id: "관계 스토리", ...},
        'ai_auto_generate': True
    }
}
```

---

## ⚠️ 중요 주의사항

### 1. 키 타입 불일치 문제
- **AI 캐시 interaction 키**: `int` (예: `0`, `1`)
- **대사 dialogues 키**: `str` (예: `'char_0'`, `'char_1'`)
- **JSON 저장 시**: 모든 int 키가 string으로 변환됨
- **로드 시**: 반드시 int로 다시 변환 필요

```python
# 올바른 로드 예시
for k, v in raw_interaction.items():
    try:
        converted[int(k)] = v
    except (ValueError, TypeError):
        converted[k] = v  # 'default' 등 문자열 키 유지
```

### 2. 중복 이름 처리
`make_unique_names()` 함수가 동일 이름에 `(2)`, `(3)` 접미사 추가
- AI 응답 파싱 시 이 패턴 제거 필요:
```python
def strip_number_suffix(name):
    return re.sub(r'\(\d+\)$', '', name).strip()
```

### 3. 저장 시 캐시 보존
`save_characters()`에서 메모리 캐시가 비어있으면 기존 파일의 캐시 유지:
```python
if not ai_cache_to_save and os.path.exists(self.config_file):
    # 기존 캐시 로드하여 사용
```

---

## 🔄 자동 백업 시스템

- **위치**: `{앱 폴더}/backups/`
- **주기**: 1시간마다 (시작 5분 후 첫 백업)
- **보관**: 최근 24개 유지
- **파일명**: `kiwipet_backup_YYYYMMDD_HHMMSS.json`

관련 함수:
- `create_auto_backup()` - 백업 생성
- `cleanup_old_backups()` - 오래된 백업 삭제
- `get_backup_list()` - 백업 목록 조회
- `show_backup_restore_dialog()` - 복원 UI

---

## 🖼️ UI 구조

### 메인 윈도우 (`MainWindow`)
```
┌─────────────────────────────────────┐
│ 헤더: 로고 + 타이틀                  │
├─────────────────────────────────────┤
│ 버튼 영역:                          │
│ [캐릭터 추가] [일괄표시] [환경설정]   │
│ [전체백업] [API설정] [크레딧]        │
├─────────────────────────────────────┤
│ 캐릭터 카드 목록 (스크롤)            │
│ ┌─────────────────────────────────┐ │
│ │ CharacterCard                   │ │
│ │ [이미지] [이름] [ON/OFF]        │ │
│ │ [캐치프레이즈]                  │ │
│ │ [크기/색상/관계/대사/성격 버튼]  │ │
│ └─────────────────────────────────┘ │
└─────────────────────────────────────┘
```

### 캐릭터 위젯 (`CharacterWidget`)
- 투명 배경의 프레임리스 윈도우
- 항상 위 (`Qt.WindowStaysOnTopHint`)
- 물리 시뮬레이션 (중력, 점프, 착지)
- 30ms 타이머로 위치 업데이트

---

## 📍 주요 함수 위치 (빠른 참조)

| 기능 | 함수 | 라인 |
|------|------|------|
| API 키 정리 | `clean_api_key` | ~567 |
| 대사 캐시 조회 | `get_cached_dialogue` | ~717 |
| AI 대사 생성 | `generate_dialogues_batch` | ~805 |
| AI 응답 처리 | `_process_ai_complete_queue` | ~9712 |
| 설정 저장 | `save_characters` | ~10240 |
| 자동 백업 | `create_auto_backup` | ~10390 |
| 설정 로드 | `load_characters` | ~10623 |
| 환경설정 UI | `show_settings` | ~10956 |
| 전체 백업 | `_export_all_characters` | ~11449 |
| 전체 복원 | `_import_all_characters` | ~11571 |
| API 설정 UI | `show_api_settings` | ~12070 |

---

## 📝 문서 업데이트 가이드

### 코드 수정 시 이 문서도 업데이트해야 하는 경우:

1. **새 클래스/함수 추가**: "주요 클래스" 또는 "주요 함수" 테이블에 추가
2. **데이터 구조 변경**: "데이터 구조" 섹션 업데이트
3. **새로운 주의사항 발견**: "중요 주의사항" 섹션에 추가
4. **UI 변경**: "UI 구조" 섹션 업데이트
5. **빌드 방법 변경**: "빌드 방법" 섹션 업데이트

### 라인 번호 업데이트
코드 수정으로 라인 번호가 변경되면, "주요 함수 위치" 테이블의 라인 번호도 업데이트해주세요.
(대략적인 위치 `~` 표기 사용 권장)

---

## 🐛 알려진 이슈 및 해결된 버그

### 해결됨
- [x] AI 대사 생성 끄면 기존 대사 사라짐 → `save_characters`에서 빈 캐시 시 기존 캐시 유지
- [x] 파일 탐색기 닫으면 캐릭터 사라짐 → `check_characters_visibility` 타이머로 복구
- [x] 백업 복원 후 상호작용 대사 키 불일치 → int 키 변환 로직 추가
- [x] API 키 테스트 시 InvalidURL → URL 인코딩 및 에러 처리 개선

### 미해결/알려진 이슈
- macOS 지원 안 됨 (win32gui 의존)

---

## Slash Commands

Available in `.claude/commands/`:

| Command | Description |
|---------|-------------|
| `/build` | 빌드 및 실행 (프로세스 종료 → 빌드 → 실행) |
| `/add-feature [desc]` | 새 기능 추가 가이드 |
| `/fix-bug [desc]` | 버그 조사 및 수정 가이드 |
| `/add-dialog [desc]` | 새 다이얼로그 추가 템플릿 |
| `/add-effect [desc]` | 캐릭터 이펙트/애니메이션 추가 |
| `/gen-icons [desc]` | SVG 아이콘 추가/수정 가이드 |

---

*마지막 업데이트: 2025-12-20*
*코드 라인 수: 약 13,800줄*
