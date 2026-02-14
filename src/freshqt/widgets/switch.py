"""

    freshqt  -  A modern, refreshed take on PyQt user interfaces

    This file is a part of the freshqt
    project and distributed under MIT license.
    https://github.com/kadir014/freshqt

"""

from PyQt6.QtCore import Qt, pyqtSignal, QPointF, QRectF
from PyQt6.QtWidgets import QWidget
from PyQt6.QtGui import QPainter, QPen, QBrush, QColor, QIcon

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

        self.off_icon: QIcon = None
        self.on_icon: QIcon = None

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

        # TODO: animation doesn't play if widget is hidden
        # if changed:
        #     if self.__on:
        #         self.__tween.play(0.15, reverse=True, easing=Easing.EASE_OUT_SINE)
        #     else:
        #         self.__tween.play(0.15, easing=Easing.EASE_OUT_SINE)

        #     self.update()

        self.__tween.value = 1.0 * float(self.__on)
        self.__tween.value_normalized = self.__tween.value
        self.__tween._alpha = 1.0 # BU OLMAK ZORUNDA
        self.update()

        self.toggled.emit()

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

        self.on_color = theme.qcolor(theme.palette.brand_primary)
        self.off_color = theme.qcolor(theme.palette.text_secondary)
        self.handle_color = theme.qcolor(theme.palette.background_primary)
        self.icon_color = theme.qcolor(theme.palette.text_primary)

    def paintEvent(self, e) -> None:
        if self.__theme is None: return

        pt = QPainter(self)
        pt.setRenderHint(QPainter.RenderHint.Antialiasing, on=True)

        #radius = 50# self.radius
        radius = self.height()
        on_color = self.on_color
        off_color = self.off_color
        handle_color = self.handle_color

        # Border thickness
        th = 1.25
        thh = th * 0.5

        # Weird overlapping with antialiased arcs
        aa_radius_offset = 1

        r = radius
        rh = r * 0.5
        w = self.width() - radius * 2.0

        # why the hell would you require 1/16 of a degree ...
        semi_start = 90 * 16
        semi_end = 180 * 16

        # Inside knob radius
        in_r = r * 0.27

        if self.on:
            border_color = on_color
            back_color = on_color
            knob_border = QColor(0, 0, 0, 0)
            knob_fill = QColor(handle_color)
        else:
            border_color = off_color
            back_color = QColor(0, 0, 0, 0)
            knob_border = QColor(0, 0, 0, 0)
            knob_fill = QColor(off_color)

        pen = QPen(border_color, th, Qt.PenStyle.SolidLine, Qt.PenCapStyle.RoundCap, Qt.PenJoinStyle.RoundJoin)
        pt.setPen(pen)
        brush = QBrush(back_color)
        pt.setBrush(brush)

        # Draw capsule borders
        # TODO: As thickness increases, the arc goes from semi-circle to ellipse
        if self.on:
            pt.drawChord(
                QRectF(thh, thh, r, r - th),
                semi_start, semi_end
            )
            pt.drawChord(
                QRectF(r + w - thh, thh, r, r - th),
                -semi_start, semi_end
            )
            pt.drawRect(QRectF(rh + aa_radius_offset, thh, self.width() - r, r - th))
        else:
            pt.drawArc(
                QRectF(thh, thh, r, r - th),
                semi_start, semi_end
            )
            pt.drawArc(
                QRectF(r + w - thh, thh, r, r - th),
                -semi_start, semi_end
            )
            pt.drawLine(
                QPointF(rh + aa_radius_offset, thh),
                QPointF(r + w + rh - aa_radius_offset, thh)
            )
            pt.drawLine(
                QPointF(rh + aa_radius_offset, r - thh),
                QPointF(r + w + rh - aa_radius_offset, r - thh)
            )

        # Draw knob
        pen = QPen(knob_border, th, Qt.PenStyle.SolidLine, Qt.PenCapStyle.RoundCap, Qt.PenJoinStyle.RoundJoin)
        pt.setPen(pen)

        brush = QBrush(knob_fill)
        pt.setBrush(brush)
        pt.drawEllipse(QPointF(rh + self.__tween.value * (self.width() - r), rh), in_r, in_r)

        # Draw icons
        pen = QPen(self.icon_color, 1.0)
        pt.setPen(pen)
        icon_margin = 4
        icon_s = radius - icon_margin * 2
        if self.__on:
            if self.on_icon is not None:
                self.on_icon.paint(
                    pt,
                    icon_margin, icon_margin,
                    icon_s, icon_s,
                    alignment=Qt.AlignmentFlag.AlignCenter
                )
        else:
            if self.off_icon is not None:
                self.off_icon.paint(
                    pt,
                    self.width() - icon_s - icon_margin, icon_margin,
                    icon_s, icon_s,
                    alignment=Qt.AlignmentFlag.AlignCenter
                )

        # Force repaint & update if animation is not done
        if self.__tween.is_started:
            self.update()