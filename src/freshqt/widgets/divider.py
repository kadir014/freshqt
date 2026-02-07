"""

    freshqt  -  A modern, refreshed take on PyQt user interfaces

    This file is a part of the freshqt
    project and distributed under MIT license.
    https://github.com/kadir014/freshqt

"""

from PyQt6.QtCore import Qt, QPointF
from PyQt6.QtWidgets import QWidget, QAbstractButton, QSizePolicy
from PyQt6.QtGui import QPainter, QIcon, QColor, QPainterPath, QFont, QPen

from freshqt.core.theme import Theme, Themeable
from freshqt.core.models import TypographyType


class Divider(QAbstractButton, Themeable):
    def __init__(self,
            margin: int = 15,
            orientation: Qt.Orientation = Qt.Orientation.Horizontal,
            parent: QWidget | None = None
            ) -> None:
        super().__init__(parent=parent)

        self.__orientation = orientation

        if self.__orientation == Qt.Orientation.Horizontal:
            self.setSizePolicy(
                QSizePolicy.Policy.Expanding,
                QSizePolicy.Policy.Minimum
            )
        else:
            self.setSizePolicy(
                QSizePolicy.Policy.Minimum,
                QSizePolicy.Policy.Expanding
            )

        self.setMinimumSize(margin, margin)

        self.__theme: Theme = None

    def update_theme(self, theme: Theme) -> None:
        self.__theme = theme

    def paintEvent(self, e) -> None:
        if self.__theme is None: return

        pt = QPainter(self)
        # IMPORTANT: Only dividers need antialiasing false, since 1-pixel
        #            completely straight lines break with antialiasing.
        pt.setRenderHint(QPainter.RenderHint.Antialiasing, on=False)

        w, h = self.width(), self.height()
        wh, hh = w * 0.5, h * 0.5

        color = self.__theme.qcolor(self.__theme.palette.text_primary)
        color.setAlphaF(0.35)
        p = QPen(color, 1.0)
        pt.setPen(p)

        if self.__orientation == Qt.Orientation.Vertical:
            pt.drawLine(
                QPointF(wh, 0.0),
                QPointF(wh, h)
            )
        else:
            pt.drawLine(
                QPointF(0.0, hh),
                QPointF(w, hh)
            )