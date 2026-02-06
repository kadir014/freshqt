"""

    freshqt  -  A modern, refreshed take on PyQt user interfaces

    This file is a part of the freshqt
    project and distributed under MIT license.
    https://github.com/kadir014/freshqt

"""

from PyQt6.QtCore import Qt, QRectF
from PyQt6.QtWidgets import QWidget, QAbstractButton
from PyQt6.QtGui import QPainter, QIcon, QColor, QPainterPath, QFont, QPen

from freshqt.core.theme import Theme, Themeable
from freshqt.core.models import TypographyType


class Button(QAbstractButton, Themeable):
    def __init__(self,
            text: str = "",
            type: TypographyType = TypographyType.BODY,
            icon: QIcon | None = None,
            parent: QWidget | None = None
            ) -> None:
        super().__init__(parent=parent)

        self.__text = text
        self.__type = type
        self.__icon = icon

        self.__theme: Theme = None

    def update_theme(self, theme: Theme) -> None:
        self.__theme = theme       

    def paintEvent(self, e) -> None:
        if self.__theme is None: return

        pt = QPainter(self)
        pt.setRenderHint(QPainter.RenderHint.Antialiasing, on=True)

        w, h = self.width(), self.height()

        bg_color = self.__theme.qcolor(self.__theme.palette.brand_primary)
        text_color = self.__theme.qcolor(self.__theme.palette.text_primary)
        border_color = QColor(0, 0, 0, 0)

        clippath = QPainterPath()
        clippath.addRoundedRect(0, 0, w, h, 7, 7)
        pt.setClipPath(clippath)

        pt.fillRect(0, 0, w, h, bg_color)

        # Render text
        font_size = int(round(self.__theme.get_typo_size(self.__type) * self.__theme.font_scale))
        if font_size <= 0:
            font_size = 1

        f = QFont()
        f.setFamily(self.__theme.font_family)
        f.setPixelSize(font_size)
        pt.setFont(f)
        pt.setPen(QPen(text_color))
        pt.drawText(QRectF(0, 0, w, h), Qt.AlignmentFlag.AlignCenter, self.__text)
        

        # c = QColor(*self.hover_color, round(self.hover_anim.value))
        # pt.fillRect(0, 0, w, h, c)

        # if isinstance(self.image, (Icon, QLabel)):
        #     pixmap = self.image.pixmap()

        # elif isinstance(self.image, QPixmap):
        #     pixmap = self.image

        # pw, ph = pixmap.width(), pixmap.height()

        # pt.drawPixmap(round(w / 2 - pw / 2), round(h / 2 - ph / 2), pixmap)

        # if not self.hover_anim.is_done(): self.update()