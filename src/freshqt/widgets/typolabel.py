"""

    freshqt  -  A modern, refreshed take on PyQt user interfaces

    This file is a part of the freshqt
    project and distributed under MIT license.
    https://github.com/kadir014/freshqt

"""

from PyQt6.QtWidgets import QWidget, QLabel
from PyQt6.QtGui import QPainter, QPainterPath, QColor

from freshqt.core.theme import Theme, Themeable


class TypoLabel(QLabel, Themeable):
    """
    Typography styled label.
    """

    def __init__(self,
            text: str | None = None,
            parent: QWidget | None = None
            ) -> None:
        super().__init__(text=text, parent=parent)

    def update_theme(self, theme: Theme) -> None:
        self.__theme = theme

        font_size = int(round(14 * theme.font_scale))
        if font_size <= 0:
            font_size = 1

        self.setStyleSheet(f"""
            font-family: {theme.font_family};
            font-size: {font_size}px;
            color: {theme.qss(theme.palette.text_primary)};
        """)