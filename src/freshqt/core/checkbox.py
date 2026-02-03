"""

    freshqt  -  A modern, refreshed take on PyQt user interfaces

    This file is a part of the freshqt
    project and distributed under MIT license.
    https://github.com/kadir014/freshqt

"""

from PyQt6.QtWidgets import QWidget, QCheckBox

from freshqt.core.typing import ColorLike
from freshqt.core.theme import Theme, Themeable
from freshqt.core.models import TypographyType


class CheckBox(QCheckBox):
    def __init__(self,
            text: str = "",
            color: ColorLike | None = None,
            parent: QWidget | None = None
            ) -> None:
        super().__init__(text=text, parent=parent)

        self._indicator_size = 14

        self._update_style()

        self.setCursor(Qt.CursorShape.PointingHandCursor)

    def _update_style(self) -> None:
        self.setStyleSheet(f"""
            QCheckBox {{
                font-family: Outfit;
                font-size: 14px;
                color: #ffffff;
            }}
            QCheckBox::indicator {{
                width: {self._indicator_size}px;
                height: {self._indicator_size}px;
                background-color: #44475A;
                border-radius: 4px;
                border: 1px solid #797d99;
            }}
            QCheckBox::indicator:unchecked:hover {{
                background-color: #6272A4;
            }}

            QCheckBox::indicator:checked {{
                border: 1px solid #BD93F9;
                background-color: #BD93F9;
            }}
        """)

    def paintEvent(self, e) -> None:
        super().paintEvent(e)

        pt = QPainter(self)
        pt.setRenderHint(QPainter.RenderHint.Antialiasing, on=True)

        if self.isChecked():
            w = 1
            icons["check"].paint(pt, w, 3, self._indicator_size, self._indicator_size)