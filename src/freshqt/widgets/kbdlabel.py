"""

    freshqt  -  A modern, refreshed take on PyQt user interfaces

    This file is a part of the freshqt
    project and distributed under MIT license.
    https://github.com/kadir014/freshqt

"""

from PyQt6.QtWidgets import QWidget
from PyQt6.QtGui import QPainter, QPainterPath

from freshqt.core.theme import Theme
from freshqt.core.models import TypographyType
from freshqt.widgets.badgelabel import BadgeLabel


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


class KbdLabel(BadgeLabel):
    def __init__(self,
            text: str | None = None,
            convert_special: bool = True,
            type: TypographyType = TypographyType.BODY,
            parent: QWidget | None = None
            ) -> None:
        super().__init__(text=None, type=type, parent=parent)

        self.setText(text, convert_special)

        self.border_radius = 3.5

    def update_theme(self, theme: Theme) -> None:
        self.color = theme.qcolor(theme.palette.background_tertiary)

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