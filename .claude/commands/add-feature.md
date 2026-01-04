# 새 기능 추가

Kiwipet에 새로운 기능을 추가합니다.

## 요청된 기능
$ARGUMENTS

## 작업 가이드

1. kiwipet.py 파일 분석 (단일 파일, ~13,500줄)
2. 관련 클래스 파악:
   - `CharacterWidget` (~1464줄): 캐릭터 표시/이동
   - `CharacterCard` (~3662줄): 메인 윈도우 캐릭터 카드 UI
   - `MainWindow` (~7124줄): 메인 윈도우
3. 기능 구현
4. 필요시 설정 저장 로직 추가 (`save_characters`/`load_characters`)
5. 빌드 및 테스트

## 주의사항
- UI 텍스트는 한국어로 작성
- PyQt5 사용 (QWidget, QDialog 등)
- 다이얼로그는 QDialog 상속, `Qt.WindowStaysOnTopHint` 설정
- 캐릭터 ID는 항상 int 타입으로 처리
- JSON 저장/로드 시 키 타입 변환 주의 (int ↔ str)
