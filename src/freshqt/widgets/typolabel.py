"""

    freshqt  -  A modern, refreshed take on PyQt user interfaces

    This file is a part of the freshqt
    project and distributed under MIT license.
    https://github.com/kadir014/freshqt

"""

from PyQt6.QtWidgets import QWidget, QLabel
from PyQt6.QtGui import QColor

from freshqt.core.theme import Theme, Themeable
from freshqt.core.models import TypographyType


class TypoLabel(QLabel, Themeable):
    """
    Typography styled label.
    """

    def __init__(self,
            text: str | None = None,
            type: TypographyType = TypographyType.BODY,
            parent: QWidget | None = None
            ) -> None:
        super().__init__(text=text, parent=parent)

        self.__type = type

        self.__theme: Theme | None = None

    @property
    def type(self) -> TypographyType:
        """ Typography type of the label. """
        return self.__type
    
    @type.setter
    def type(self, value: TypographyType) -> None:
        self.__type = value
        if self.__theme is not None:
            self.update_theme(self.__theme)
            self.update_theme_role(self.__theme)
        self.update()

    def update_theme(self, theme: Theme, text_color: QColor | None = None) -> None:
        font_size = int(round(theme.get_typo_size(self.__type) * theme.font_scale))
        if font_size <= 0:
            font_size = 1

        if text_color is None:
            text_color = theme.qcolor(theme.palette.text_primary)

        self.setStyleSheet(f"""
            font-family: {theme.font_family};
            font-size: {font_size}px;
            color: {theme.qss(text_color)};
        """)