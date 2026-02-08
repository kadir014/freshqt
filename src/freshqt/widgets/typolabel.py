"""

    freshqt  -  A modern, refreshed take on PyQt user interfaces

    This file is a part of the freshqt
    project and distributed under MIT license.
    https://github.com/kadir014/freshqt

"""

from PyQt6.QtWidgets import QWidget, QLabel
from PyQt6.QtGui import QColor

from freshqt.core.typing import ColorLike
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

        self.__color0 = None
        self.__color = None

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

    @property
    def color(self) -> QColor:
        """
        Converted text color.
        """
        return self.__color
    
    @color.setter
    def color(self, value: ColorLike) -> None:
        self.__color0 = value

        self.update()

    def update_theme(self, theme: Theme, force_text_color: QColor | None = None) -> None:
        font_size = int(round(theme.get_typo_size(self.__type) * theme.font_scale))
        if font_size <= 0:
            font_size = 1

        if self.__color0 is None:
            self.__color = theme.qcolor(theme.palette.text_primary)

        elif isinstance(self.__color0, str) and hasattr(theme.palette, self.__color0):
            self.__color = theme.qcolor(getattr(theme.palette, self.__color0))

        else:
            self.__color = theme.qcolor(self.__color0)

        if force_text_color is not None:
            self.__color = theme.qcolor(force_text_color)

        self.setStyleSheet(f"""
            font-family: {theme.font_family};
            font-size: {font_size}px;
            color: {theme.qss(self.__color)};
        """)