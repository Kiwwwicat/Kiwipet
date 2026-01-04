# -*- coding: utf-8 -*-
"""
모니터 해상도 기반 자동 스케일링 모듈
- v1.2.1 빌드 시에만 사용
- 모니터 크기에 따라 앱 창 크기 자동 조절
"""

from PyQt5.QtWidgets import QApplication

# 기본 창 크기
BASE_WIDTH = 650
BASE_HEIGHT = 750


def get_auto_scale():
    """
    모니터 해상도에 따른 스케일 값 계산

    Returns:
        float: 스케일 값 (1.0, 1.25, 1.5)
    """
    screen = QApplication.primaryScreen().geometry()
    screen_height = screen.height()

    # 기준: 1080p = 100%, 1440p = 125%, 4K = 150%
    if screen_height >= 2160:  # 4K
        return 1.5
    elif screen_height >= 1440:  # QHD
        return 1.25
    else:  # FHD 이하
        return 1.0


def get_scaled_size():
    """
    스케일링된 창 크기 반환

    Returns:
        tuple: (width, height)
    """
    scale = get_auto_scale()
    width = int(BASE_WIDTH * scale)
    height = int(BASE_HEIGHT * scale)

    screen = QApplication.primaryScreen().geometry()
    print(f"[자동 스케일] 모니터 높이: {screen.height()}px, 스케일: {int(scale*100)}%, 창 크기: {width}x{height}")

    return width, height
