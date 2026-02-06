"""

    freshqt  -  A modern, refreshed take on PyQt user interfaces

    This file is a part of the freshqt
    project and distributed under MIT license.
    https://github.com/kadir014/freshqt

"""

from PyQt6.QtWidgets import QWidget
from PyQt6.QtGui import QPainter, QPainterPath, QColor

from freshqt.core.typing import ColorLike
from freshqt.core.theme import Theme
from freshqt.core.models import TypographyType
from freshqt.widgets.typolabel import TypoLabel
from freshqt.core.color import WCAG, WCAG_NORMAL_TEXT


class BadgeLabel(TypoLabel):
    def __init__(self,
            text: str | None = None,
            type: TypographyType = TypographyType.BODY,
            color: ColorLike | None = None,
            parent: QWidget | None = None
            ) -> None:
        super().__init__(text=None, type=type, parent=parent)
        
        self.setText(text)
        self.setMargin(2)

        self.__border_radius = -1.0
        self.__color0 = color
        self.__color = None

        self.__theme: Theme | None = None

    @property
    def border_radius(self) -> float:
        """
        Border radius for the background.

        If -1, the radius is 100%
        """
        return self.__border_radius
    
    @border_radius.setter
    def border_radius(self, value: float) -> None:
        self.__border_radius = value
        self.update()

    @property
    def color(self) -> QColor:
        """
        Badge color.
        """
        return self.__color
    
    @color.setter
    def color(self, value: ColorLike) -> None:
        self.__color0 = value

        self.update()

    def setText(self, text: str | None) -> None:
        if text is None: return

        # For background badge to look correctly, we need padding
        # So spaces on sides and also setMargin is neeeded
        text = f" {text} "

        super().setText(text)

    def update_theme(self, theme: Theme) -> None:
        self.__theme = theme

        if self.__color0 is None:
            self.__color = theme.qcolor(theme.palette.brand_primary)

        elif isinstance(self.__color0, str) and hasattr(theme.palette, self.__color0):
            self.__color = theme.qcolor(getattr(theme.palette, self.__color0))

        else:
            self.__color = theme.qcolor(self.__color0)

        text_color = theme.qcolor(theme.palette.text_primary)
        if WCAG(text_color, self.__color) < WCAG_NORMAL_TEXT:
            text_color = theme.qcolor(theme.palette.text_fallback)

        super().update_theme(theme, text_color=text_color)

    def paintEvent(self, a0) -> None:
        if self.__theme is None: return

        pt = QPainter(self)
        pt.setRenderHint(QPainter.RenderHint.Antialiasing, on=True)

        # Usual widget geometry and label's text size is not the same
        #size = self.sizeHint()
        w = self.width()
        h = self.height()

        border_radius = self.__border_radius
        if border_radius < 0.0:
            border_radius = min(w, h) * 0.5

        clippath = QPainterPath()
        clippath.addRoundedRect(0, 0, w, h, border_radius, border_radius)
        pt.setClipPath(clippath)

        pt.fillRect(0, 0, w, h, self.__color)

        super().paintEvent(a0)