# 아이콘 생성/수정

SVG 아이콘을 추가하거나 수정합니다.

## 요청
$ARGUMENTS

## 아이콘 구조

Kiwipet의 아이콘은 kiwipet.py 파일 상단에 SVG 문자열로 정의되어 있습니다.

### 기존 아이콘 목록 (Line ~21-178)
```python
PLACEHOLDER_SVG      # 이미지 없는 캐릭터용 플레이스홀더
SVG_INFO             # i 버튼 (크레딧)
SVG_QUESTION         # ? 버튼 (튜토리얼)
SVG_KIWIPET_TITLE    # Kiwipet 타이틀 로고
SVG_MONITOR          # 모니터 아이콘
SVG_KEY              # 열쇠 아이콘 (API KEY)
SVG_BACKUP           # 백업 아이콘
SVG_TRASH            # 쓰레기통 (기본 초록)
SVG_TRASH_RED        # 쓰레기통 (호버용 빨강)
SVG_PEN              # 펜 아이콘 (이름 수정)
SVG_PALETTE          # 말풍선 팔레트
SVG_SCALE            # 돋보기+ (크기 조절)
SVG_DELETE           # 삭제 아이콘
SVG_CAMERA           # 카메라 (이미지 변경)
SVG_IMAGE_CHANGE     # 이미지 변경 버튼
SVG_BUBBLE_SETTING   # 말풍선 설정 (하트)
SVG_LOGO             # Kiwipet 로고
```

## 아이콘 추가 방법

1. SVG 코드를 문자열로 정의
```python
SVG_NEW_ICON = '''<svg width="16" height="16" viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="..." fill="#349971"/>
</svg>'''
```

2. 코드에서 사용
```python
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtSvg import QSvgRenderer
from PyQt5.QtCore import QByteArray

def load_svg_icon(svg_str, size=16):
    renderer = QSvgRenderer(QByteArray(svg_str.encode()))
    pixmap = QPixmap(size, size)
    pixmap.fill(Qt.transparent)
    painter = QPainter(pixmap)
    renderer.render(painter)
    painter.end()
    return QIcon(pixmap)
```

## 색상 가이드
- 기본 초록: #349971, #4FB98F
- 진한 초록: #317C75
- 연한 초록: #8ECFB5, #9DD4BA
- 배경 초록: #D5E8DF
- 빨강 (호버): #E57373
