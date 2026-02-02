"""

    freshqt  -  A modern, refreshed take on PyQt user interfaces

    This file is a part of the freshqt
    project and distributed under MIT license.
    https://github.com/kadir014/freshqt

"""

from math import ceil, floor

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QSlider

from freshqt.core.theme import Theme, Themeable


class Slider(QSlider, Themeable):
    def __init__(self,
            orientation: Qt.Orientation = Qt.Orientation.Horizontal,
            parent: QWidget | None = None
            ) -> None:
        super().__init__(orientation=orientation, parent=parent)

        self.setCursor(Qt.CursorShape.PointingHandCursor)

    def update_theme(self, theme: Theme) -> None:
        handle_height = 15
        groove_height = 6
        self.setFixedHeight(handle_height + 1)
        margin = -ceil((handle_height - groove_height) / 2.0)
        groove_radius = floor(groove_height * 0.5)
        handle_radius = floor(handle_height * 0.5)

        self.setStyleSheet(f"""
            QSlider::groove:horizontal {{
                border: none;
                height: {groove_height}px;

                background: {theme.qss(theme.palette.background_secondary)};
                border-radius: {groove_radius}px;
            }}

            QSlider::sub-page:horizontal {{
                background: {theme.qss(theme.palette.brand_primary)};
                border: none;
                border-radius: {groove_radius}px;
            }}

            QSlider::handle:horizontal {{
                background: {theme.qss(theme.palette.text_primary)};
                border: none;
                width: {handle_height}px;
                height: {handle_height}px;
                margin: {margin}px 0px;
                border-radius: {handle_radius}px;
            }}
        """)