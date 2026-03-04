"""

    freshqt  -  A modern, refreshed take on PyQt user interfaces

    This file is a part of the freshqt
    project and distributed under MIT license.
    https://github.com/kadir014/freshqt

"""

from PyQt6.QtCore import Qt, QPoint
from PyQt6.QtWidgets import QWidget, QGraphicsColorizeEffect, QLabel
from PyQt6.QtGui import QPixmap, QColor, QPainter, QPainterPath

from freshqt.core.theme import Theme, Themeable
from freshqt.assets import IMAGES


class Avatar(QWidget, Themeable):
    def __init__(self,
            pixmap: QPixmap | None = None,
            parent: QWidget | None = None
            ) -> None:
        super().__init__(parent=parent)

        self.__theme: Theme | None = None

        self.__pixmap0: QPixmap | None # Initial source pixmap
        self.__pixmap0_scaled: QPixmap # Scaled version of source pixmap (or fallback)
        self.__pixmap_fallback: QPixmap # Fallback pixmap
        self.__pixmap: QPixmap # Final rendered pixmap

        self.setFixedSize(32, 32)

        self.__pixmap0 = pixmap
        
        self.__update_pixmaps()

        self.__colorize = True
        self.__radius = -1

    def __load_fallback_pixmap(self) -> None:
        w, h = self.width(), self.height()

        #self.__pixmap_fallback = QPixmap(str(IMAGES["avatar"].absolute()))
        self.__pixmap_fallback = QPixmap(64, 64)
        self.__pixmap_fallback.fill(QColor(255, 255, 255))

        self.__pixmap_fallback = self.__pixmap_fallback.scaled(
            w, h,
            transformMode=Qt.TransformationMode.SmoothTransformation
        )

    def __update_pixmaps(self) -> None:
        w, h = self.width(), self.height()

        self.__load_fallback_pixmap()

        if self.__pixmap0 is None or self.__pixmap0.isNull():
            self.__pixmap0_scaled = self.__pixmap_fallback.copy()

        else:
            self.__pixmap0_scaled = self.__pixmap0.scaled(
                w, h,
                transformMode=Qt.TransformationMode.SmoothTransformation
            )

        self.__pixmap = self.__pixmap0_scaled.copy()

        # Update the final pixmap using last theme
        if self.__theme is not None:
            self.update_theme(self.__theme)

    @property
    def pixmap(self) -> QPixmap:
        """ Unscaled source pixmap. """
        return self.__pixmap0
    
    @pixmap.setter
    def pixmap(self, value: QPixmap | None) -> None:
        self.__pixmap0 = value

        self.__update_pixmaps()
        self.update()

    @property
    def colorize(self) -> bool:
        """ Colorize the pixmap. """
        return self.__colorize
    
    @colorize.setter
    def colorize(self, value: bool) -> None:
        self.__colorize = value

        if self.__theme is not None:
            self.__update_pixmaps()
            self.update_theme(self.__theme)
            self.update()

    @property
    def radius(self) -> int:
        """ Border radius. Circle if -1. """
        return self.__radius
    
    @radius.setter
    def radius(self, value: int) -> None:
        self.__radius = value
        self.update()

    def recolor_pixmap(self, color: QColor) -> None:
        if self.__pixmap0_scaled is None or self.__pixmap0_scaled.isNull():
            return

        g = QGraphicsColorizeEffect()
        g.setEnabled(True)
        g.setColor(color)
        g.setStrength(1.0)
        
        lbl = QLabel()
        lbl.setFixedSize(self.size())
        lbl.setPixmap(self.__pixmap0_scaled)
        lbl.setGraphicsEffect(g)

        self.__pixmap = lbl.grab()

    def update_theme(self, theme: Theme) -> None:
        self.__theme = theme

        if self.__colorize:
            self.recolor_pixmap(theme.qcolor(theme.palette.brand_primary))

    def resizeEvent(self, e) -> None:
        super().resizeEvent(e)
        self.__update_pixmaps()

    def paintEvent(self, e) -> None:
        if self.__pixmap is None or self.__pixmap.isNull():
            return

        pt = QPainter(self)
        pt.setRenderHint(QPainter.RenderHint.Antialiasing, on=True)

        w, h = self.width(), self.height()

        clippath = QPainterPath()
        if self.__radius == -1:
            clippath.addEllipse(0, 0, w, h)
        else:
            clippath.addRoundedRect(0, 0, w, h, self.__radius, self.__radius)
        pt.setClipPath(clippath)

        pt.drawPixmap(0, 0, self.__pixmap)