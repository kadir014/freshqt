from math import ceil, floor

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QSlider


class Slider(QSlider):
    def __init__(self,
            orientation: Qt.Orientation = Qt.Orientation.Horizontal,
            parent: QWidget | None = None
            ) -> None:
        super().__init__(orientation=orientation, parent=parent)

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

                background: #44475a;
                border-radius: {groove_radius}px;
            }}

            QSlider::sub-page:horizontal {{
                background: #bd93f9;
                border: none;
                border-radius: {groove_radius}px;
            }}

            QSlider::handle:horizontal {{
                background: #ffffff;
                border: none;
                width: {handle_height}px;
                height: {handle_height}px;
                margin: {margin}px 0px;
                border-radius: {handle_radius}px;
            }}
        """)

        self.setCursor(Qt.CursorShape.PointingHandCursor)