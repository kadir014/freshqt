"""

    freshqt  -  A modern, refreshed take on PyQt user interfaces

    This file is a part of the freshqt
    project and distributed under MIT license.
    https://github.com/kadir014/freshqt

"""

from PyQt6.QtWidgets import QWidget, QLineEdit
from PyQt6.QtGui import QColor

from freshqt.core.typing import ColorLike
from freshqt.core.theme import Theme, Themeable
from freshqt.core.models import TypographyType


class LineEdit(QLineEdit, Themeable):
    def __init__(self,
            text: str | None = None,
            parent: QWidget | None = None
            ) -> None:
        super().__init__(text=text, parent=parent)

        self.setTextMargins(5, 5, 5, 5)

    def update_theme(self, theme: Theme) -> None:
        font_size = int(round(theme.get_typo_size(TypographyType.BODY) * theme.font_scale))
        if font_size <= 0:
            font_size = 1

        self.setStyleSheet(f"""
            font-family: {theme.font_family};
            font-size: {font_size}px;
            color: {theme.qss(theme.palette.text_primary)};
            background-color: {theme.qss(theme.palette.background_secondary)};
            border: 1px solid {theme.qss(theme.palette.text_tertiary)};
            border-radius: 10px;
            selection-background-color: {theme.qss(theme.palette.text_selection)};
        """)