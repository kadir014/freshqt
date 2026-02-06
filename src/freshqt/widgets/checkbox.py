"""

    freshqt  -  A modern, refreshed take on PyQt user interfaces

    This file is a part of the freshqt
    project and distributed under MIT license.
    https://github.com/kadir014/freshqt

"""

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QCheckBox
from PyQt6.QtGui import QPainter, QIcon

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
        self.__indicator_icon: QIcon | None = None

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

    @property
    def indicator_size(self) -> int:
        return self.__indicator_size
    
    @indicator_size.setter
    def indicator_size(self, value: int) -> None:
        self.__indicator_size = int(value)
        self.update()

    @property
    def indicator_icon(self) -> QIcon | None:
        return self.__indicator_icon
    
    @indicator_icon.setter
    def indicator_icon(self, value: QIcon | None) -> None:
        self.__indicator_icon = value
        self.update()

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
                background-color: {theme.qss(theme.palette.background_secondary)};
                border-radius: 4px;
                border: 1px solid {theme.qss(theme.palette.text_tertiary)};
            }}
            QCheckBox::indicator:unchecked:hover {{
                background-color: {theme.qss(theme.palette.background_tertiary)};
            }}

            QCheckBox::indicator:checked {{
                border: 1px solid {theme.qss(theme.palette.brand_primary)};
                background-color: {theme.qss(theme.palette.brand_primary)};
            }}
        """)

    def paintEvent(self, e) -> None:
        super().paintEvent(e)

        pt = QPainter(self)
        pt.setRenderHint(QPainter.RenderHint.Antialiasing, on=True)

        if self.__indicator_icon is not None and self.isChecked():
            self.__indicator_icon.paint(
                pt,
                1, round(self.height() * 0.5 - self.__indicator_size * 0.5),
                self.__indicator_size, self.__indicator_size
            )