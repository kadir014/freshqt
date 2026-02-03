"""

    freshqt  -  A modern, refreshed take on PyQt user interfaces

    This file is a part of the freshqt
    project and distributed under MIT license.
    https://github.com/kadir014/freshqt

"""

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QCheckBox
from PyQt6.QtGui import QPainter

from freshqt.core.typing import ColorLike
from freshqt.core.theme import Theme, Themeable
from freshqt.core.models import TypographyType


class CheckBox(QCheckBox, Themeable):
    def __init__(self,
            text: str = "",
            type: TypographyType = TypographyType.BODY,
            parent: QWidget | None = None
            ) -> None:
        super().__init__(text=text, parent=parent)

        self.__indicator_size = 14

        self.__type = type

        self.setCursor(Qt.CursorShape.PointingHandCursor)

    @property
    def type(self) -> TypographyType:
        """ Typography type of the label. """
        return self.__type
    
    @type.setter
    def type(self, value: TypographyType) -> None:
        self.__type = value
        self.update_theme()
        self.update_theme_role()

    def update_theme(self, theme: Theme) -> None:
        font_size = int(round(theme.get_typo_size(self.__type) * theme.font_scale))
        if font_size <= 0:
            font_size = 1

        self.setStyleSheet(f"""
            QCheckBox {{
                font-family: {theme.font_family};
                font-size: {font_size}px;
                color: {theme.qss(theme.palette.text_primary)};
            }}
            QCheckBox::indicator {{
                width: {self.__indicator_size}px;
                height: {self.__indicator_size}px;
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
            #icons["check"].paint(pt, w, 3, self._indicator_size, self._indicator_size)