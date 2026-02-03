"""

    freshqt  -  A modern, refreshed take on PyQt user interfaces

    This file is a part of the freshqt
    project and distributed under MIT license.
    https://github.com/kadir014/freshqt

"""

from PyQt6.QtWidgets import QWidget
from PyQt6.QtGui import QPainter, QPainterPath

from freshqt.core.theme import Theme, Themeable
from freshqt.core.models import TypographyType
from freshqt.widgets.typolabel import TypoLabel


SPECIAL_CHARS = {
    "command": "⌘",
    "cmd": "⌘",
    "option": "⌥",
    "alt": "⌥",
    "shift": "⇧",
    "capslock": "⇪",

    "enter": "⏎",
    "return": "⏎",

    "left": "←",
    "up": "↑",
    "down": "↓",
    "right": "→",
    "backspace": "⌫",
    "delete": "⌦"
}


class KbdLabel(TypoLabel):
    def __init__(self,
            text: str | None = None,
            convert_special: bool = True,
            type: TypographyType = TypographyType.BODY,
            parent: QWidget | None = None
            ) -> None:
        super().__init__(text=None, type=type, parent=parent)

        self.setText(text, convert_special)

        self.setMargin(2)

        self.__theme: Theme | None = None

    def update_theme(self, theme: Theme) -> None:
        self.__theme = theme

        super().update_theme(theme)

    def setText(self, text: str | None, convert_special: bool = True) -> None:
        """
        Set text property of label.

        Parameters
        ----------
        text
            Text content
        convert_special
            Convert key names to special characters (e.g Command -> ⌘)
        """
        if text is None: return

        if convert_special:
            for key in SPECIAL_CHARS:
                char = SPECIAL_CHARS[key]
                text = text.replace(key, char)
                text = text.replace(key.upper(), char)
                text = text.replace(key.capitalize(), char)

        super().setText(text)

    def paintEvent(self, a0) -> None:
        if self.__theme is None: return

        pt = QPainter(self)
        pt.setRenderHint(QPainter.RenderHint.Antialiasing, on=True)

        size = self.sizeHint()

        clippath = QPainterPath()
        clippath.addRoundedRect(0, 0, size.width(), size.height(), 6, 6)
        pt.setClipPath(clippath)

        bg_color = self.__theme.qcolor(self.__theme.palette.background_tertiary)
        pt.fillRect(0, 0, size.width(), size.height(), bg_color)

        super().paintEvent(a0)