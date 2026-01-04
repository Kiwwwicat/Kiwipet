# 캐릭터 이펙트/애니메이션 추가

캐릭터에 새로운 시각 효과나 애니메이션을 추가합니다.

## 효과 정보
$ARGUMENTS

## 작업 순서

1. `CharacterWidget` 클래스 분석 (~1464줄)
2. 기존 애니메이션 패턴 파악
3. 효과 구현
4. 테스트

## CharacterWidget 주요 구조

```python
class CharacterWidget(QWidget):
    def __init__(self):
        # 물리 시뮬레이션 변수
        self.velocity_y = 0          # 수직 속도
        self.on_ground = False       # 착지 상태
        self.is_jumping = False      # 점프 중

        # 위치 업데이트 타이머 (30ms)
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_position)

    def update_position(self):
        # 중력 적용
        # 바닥/창 경계 감지
        # 위치 이동

    def show_dialogue(self, text, duration=180):
        # 말풍선 표시
```

## 참고: 기존 효과들
- 점프 애니메이션 (물리 시뮬레이션)
- 좌우 이동 (랜덤 방향 전환)
- 말풍선 표시/숨김
- 캐릭터 뒤집기 (이동 방향에 따라)

## 주의사항
- QTimer 사용하여 애니메이션 구현
- 30ms 간격의 기존 타이머 활용 권장
- 캐릭터 이미지는 QLabel에 QPixmap으로 표시
- GIF 지원: QMovie 사용
