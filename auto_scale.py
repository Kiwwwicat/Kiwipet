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

# 현재 스케일 값 저장 (글씨 크기 계산용)
_current_scale = 1.0


def get_auto_scale():
    """
    모니터 해상도에 따른 스케일 값 계산

    Returns:
        float: 스케일 값 (1.0, 1.25, 1.5)
    """
    global _current_scale
    screen = QApplication.primaryScreen().geometry()
    screen_height = screen.height()

    # 기준: 1080p = 100%, 1440p = 125%, 4K = 150%
    if screen_height >= 2160:  # 4K
        _current_scale = 1.5
    elif screen_height >= 1440:  # QHD
        _current_scale = 1.25
    else:  # FHD 이하
        _current_scale = 1.0

    return _current_scale


def get_current_scale():
    """현재 스케일 값 반환"""
    return _current_scale


def scale_font_size(base_size):
    """
    기본 폰트 크기를 스케일에 맞게 조절

    Args:
        base_size: 기본 폰트 크기 (px)

    Returns:
        int: 스케일링된 폰트 크기
    """
    return int(base_size * _current_scale)


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
