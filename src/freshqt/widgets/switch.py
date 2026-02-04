"""

    freshqt  -  A modern, refreshed take on PyQt user interfaces

    This file is a part of the freshqt
    project and distributed under MIT license.
    https://github.com/kadir014/freshqt

"""

from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtWidgets import QWidget
from PyQt6.QtGui import QPainter, QPen, QBrush, QColor

from freshqt.core.typing import ColorLike
from freshqt.core.theme import Theme, Themeable
from freshqt.core.models import TypographyType
from freshqt.animation import Tween, Easing


class Switch(QWidget, Themeable):
    """
    Animated toggle switch widget.

    Signals
    -------
    toggled
        Switch is toggled
    """

    toggled = pyqtSignal()

    def __init__(self,
            on: bool = False,
            parent: QWidget | None = None
            ) -> None:
        super().__init__(parent=parent)

        self.__on = on

        self.__tween = Tween(
            start_value=0.0,
            end_value=1.0,
            value=1.0 * float(self.__on)
        )

        self.setCursor(Qt.CursorShape.PointingHandCursor)

        self.__theme: Theme = None

    @property
    def on(self) -> bool:
        """ Whether the switch is toggled or not. """
        return self.__on
    
    @on.setter
    def on(self, value: bool) -> None:
        changed =  value != self.__on

        self.__on = value

        if changed:
            if self.__on:
                self.__tween.play(0.15, reverse=True, easing=Easing.EASE_OUT_SINE)
            else:
                self.__tween.play(0.15, easing=Easing.EASE_OUT_SINE)

            self.update()

    def mousePressEvent(self, e) -> None:
        if self.__on:
            self.__on = False
            self.__tween.play(0.15, reverse=True, easing=Easing.EASE_OUT_SINE)
        else:
            self.__on = True
            self.__tween.play(0.15, easing=Easing.EASE_OUT_SINE)

        self.update()

        self.toggled.emit()

        super().mousePressEvent(e)

    def enterEvent(self, e) -> None:
        self.on_color = self.__theme.qcolor(self.__theme.palette.brand_primary)
        self.off_color = self.__theme.qcolor(self.__theme.palette.text_primary)
        self.handle_color = self.__theme.qcolor(self.__theme.palette.background_secondary)

        self.update()

        super().enterEvent(e)

    def leaveEvent(self, e) -> None:
        self.on_color = self.__theme.qcolor(self.__theme.palette.brand_primary)
        self.off_color = self.__theme.qcolor(self.__theme.palette.text_secondary)
        self.handle_color = self.__theme.qcolor(self.__theme.palette.background_primary)

        self.update()

        super().leaveEvent(e)

    def update(self) -> None:
        self.__tween.update()
        super().update()

    def update_theme(self, theme: Theme) -> None:
        self.__theme = theme

        self.on_color = self.__theme.qcolor(self.__theme.palette.brand_primary)
        self.off_color = self.__theme.qcolor(self.__theme.palette.text_secondary)
        self.handle_color = self.__theme.qcolor(self.__theme.palette.background_primary)

    def paintEvent(self, e) -> None:
        if self.__theme is None: return

        pt = QPainter()
        pt.begin(self)
        pt.setRenderHint(QPainter.RenderHint.Antialiasing, on=True)

        radius = 20# self.radius
        on_color = self.on_color
        off_color = self.off_color
        handle_color = self.handle_color

        w = round(self.width() - radius * 2) - 2

        # TODO: Rewrite drawing logic

        pt.fillRect(0, 0, self.width(), self.height(), QColor(255, 0, 0))

        if self.on:
            pen = QPen(on_color, 1.5, Qt.PenStyle.SolidLine, Qt.PenCapStyle.RoundCap, Qt.PenJoinStyle.RoundJoin)
            pt.setPen(pen)
            brush = QBrush(on_color)
            pt.setBrush(brush)

            r = radius

            pt.drawChord(r, 1, r, r, 90*16, 180*16)
            pt.drawChord(r+w, 1, r, r, -90*16, 180*16)
            pt.drawRect(r+r//2, 1, w, r)

            pt.setBrush(QBrush(handle_color))
            offset = r*0.4
            pt.drawEllipse(round(r+offset/2+self.__tween.value*w), round(1+offset/2), round(r-offset) , round(r-offset))

        else:
            pen = QPen(off_color, 1.5, Qt.PenStyle.SolidLine, Qt.PenCapStyle.RoundCap, Qt.PenJoinStyle.RoundJoin)
            pt.setPen(pen)

            r = radius

            pt.drawArc(r, 1, r, r, 90*16, 180*16)
            pt.drawArc(r+w, 1, r, r, -90*16, 180*16)
            pt.drawLine(r+r//2, 1, r+w+r//2, 1)
            pt.drawLine(r+r//2, r+1, r+w+r//2, r+1)

            brush = QBrush(off_color)
            pt.setBrush(brush)
            offset = r*0.4
            pt.drawEllipse(round(r+offset/2+self.__tween.value*w), round(offset/2+1), round(r-offset), round(r-offset))

        pt.end()

        # Force repaint & update if animation is not done
        if self.__tween.is_started:
            self.update()