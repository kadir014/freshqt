"""

    freshqt  -  A modern, refreshed take on PyQt user interfaces

    This file is a part of the freshqt
    project and distributed under MIT license.
    https://github.com/kadir014/freshqt

"""

from freshqt.core.theme import Theme, Themeable, change_titlebar_theme
from freshqt.core.models import (
    TweenRepeatMode,
    SyntaxPalette,
    UIPalette,
    SyntaxLanguage,
    TypographyRamp,
    TypographyType
)

__version__ = "0.0.1"


__all__ = (
    "__version__",
    "Theme", "Themeable", "change_titlebar_theme",
    "TweenRepeatMode",
    "SyntaxPalette",
    "UIPalette",
    "SyntaxLanguage",
    "TypographyRamp",
    "TypographyType"
)