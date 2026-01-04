# 새 다이얼로그 추가

Kiwipet에 새로운 설정 다이얼로그를 추가합니다.

## 다이얼로그 정보
$ARGUMENTS

## 기본 다이얼로그 템플릿

```python
class NewDialog(QDialog):
    """새 다이얼로그"""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("다이얼로그 제목")
        self.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint)
        self.setFixedSize(400, 300)
        self.setStyleSheet("background-color: white;")

        layout = QVBoxLayout(self)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(15)

        # 섹션 라벨
        title_label = QLabel("섹션명")
        title_label.setFont(QFont("Pretendard", 14, QFont.Bold))
        title_label.setStyleSheet("color: #333;")
        layout.addWidget(title_label)

        # 컨텐츠 영역
        content_frame = QFrame()
        content_frame.setStyleSheet("background-color: #f5f5f5; border-radius: 8px;")
        content_layout = QVBoxLayout(content_frame)
        layout.addWidget(content_frame)

        # 버튼 영역
        btn_layout = QHBoxLayout()
        btn_layout.addStretch()

        cancel_btn = QPushButton("취소")
        cancel_btn.clicked.connect(self.reject)
        btn_layout.addWidget(cancel_btn)

        ok_btn = QPushButton("확인")
        ok_btn.setStyleSheet("background-color: #4FB98F; color: white;")
        ok_btn.clicked.connect(self.accept)
        btn_layout.addWidget(ok_btn)

        layout.addLayout(btn_layout)
```

## 기존 다이얼로그 참고
- `PersonalityDialog` (~4671줄): 캐릭터 성격 설정
- `DialogueDialog` (~5373줄): 대사 편집
- `RelationshipDialog` (~5785줄): 관계 설정
- `BubbleColorDialog` (~6100줄): 말풍선 색상
- `ScaleDialog` (~6432줄): 크기 조절

## 주의사항
- 폰트: "Pretendard" 사용
- 배경색: white, 테두리: #e0e0e0
- 강조색: #4FB98F (초록), #317C75 (진한 초록)
- `Qt.WindowStaysOnTopHint` 필수
