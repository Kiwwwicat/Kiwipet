# -*- coding: utf-8 -*-
"""
앱 크기 조절 기능 모듈
- 창 크기를 100%~200% 범위로 조절
- 기본 창 크기: 650x750
"""

from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel,
    QSlider, QPushButton
)
from PyQt5.QtCore import Qt


# 기본 설정값
DEFAULT_APP_SCALE = 100
MIN_APP_SCALE = 100
MAX_APP_SCALE = 200
BASE_WIDTH = 650
BASE_HEIGHT = 750
PRESET_VALUES = [100, 125, 150, 200]


def create_app_scale_section(parent, current_scale, on_scale_changed_callback):
    """
    앱 크기 조절 UI 섹션 생성

    Args:
        parent: 부모 위젯
        current_scale: 현재 스케일 값 (100-200)
        on_scale_changed_callback: 스케일 변경 시 호출할 콜백 함수

    Returns:
        tuple: (section_widget, slider_widget)
    """
    section = QWidget()
    layout = QVBoxLayout(section)
    layout.setSpacing(8)

    # 섹션 제목
    title = QLabel("앱 크기")
    title.setStyleSheet("font-family: 'Pretendard', sans-serif; font-size: 15px; font-weight: 700;")
    layout.addWidget(title)

    # 슬라이더 행
    slider_row = QHBoxLayout()
    slider_row.setSpacing(10)

    # 슬라이더
    slider = QSlider(Qt.Horizontal)
    slider.setMinimum(MIN_APP_SCALE)
    slider.setMaximum(MAX_APP_SCALE)
    slider.setValue(current_scale)
    slider.setStyleSheet("""
        QSlider::groove:horizontal {
            height: 8px;
            background: #E8F5E9;
            border-radius: 4px;
        }
        QSlider::handle:horizontal {
            width: 18px;
            height: 18px;
            margin: -5px 0;
            background: #8ECFB5;
            border-radius: 9px;
        }
        QSlider::sub-page:horizontal {
            background: #8ECFB5;
            border-radius: 4px;
        }
    """)

    # 값 표시 라벨
    value_label = QLabel(f"{current_scale}%")
    value_label.setFixedWidth(50)
    value_label.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
    value_label.setStyleSheet("font-size: 14px; font-weight: 700; color: #5A9C85;")

    # 슬라이더 값 변경 핸들러
    def on_slider_changed(value):
        value_label.setText(f"{value}%")
        if on_scale_changed_callback:
            on_scale_changed_callback(value)

    slider.valueChanged.connect(on_slider_changed)

    slider_row.addWidget(slider)
    slider_row.addWidget(value_label)
    slider_row.addStretch()

    layout.addLayout(slider_row)

    # 프리셋 버튼 행
    preset_row = QHBoxLayout()
    preset_row.setSpacing(8)

    for preset in PRESET_VALUES:
        btn = QPushButton(f" {preset}% ")
        btn.setCursor(Qt.PointingHandCursor)
        btn.setStyleSheet("""
            QPushButton {
                background-color: #C5E8D8;
                color: #5A9C85;
                border: none;
                border-radius: 6px;
                padding: 5px 8px;
            }
            QPushButton:hover {
                background-color: #8ECFB5;
                color: white;
            }
        """)
        btn.clicked.connect(
            lambda checked, v=preset: (slider.setValue(v), on_slider_changed(v))
        )
        preset_row.addWidget(btn)

    preset_row.addStretch()
    layout.addLayout(preset_row)

    # 설명
    info = QLabel("창 크기를 조절합니다.")
    info.setStyleSheet("font-family: 'Pretendard', sans-serif; font-size: 12px; font-weight: 700; color: #888;")
    layout.addWidget(info)

    return section, slider


def calculate_scaled_size(scale):
    """
    스케일 값에 따른 창 크기 계산

    Args:
        scale: 스케일 값 (100-200)

    Returns:
        tuple: (width, height)
    """
    width = int(BASE_WIDTH * scale / 100)
    height = int(BASE_HEIGHT * scale / 100)
    return width, height


def apply_scale_to_window(window, scale, save_callback=None):
    """
    윈도우에 스케일 적용

    Args:
        window: 대상 윈도우
        scale: 스케일 값 (100-200)
        save_callback: 저장 콜백 함수 (optional)
    """
    width, height = calculate_scaled_size(scale)
    window.resize(width, height)

    if save_callback:
        save_callback()

    print(f"[앱 크기] {scale}% 적용 ({width}x{height})")
