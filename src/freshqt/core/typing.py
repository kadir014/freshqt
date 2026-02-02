"""

    freshqt  -  A modern, refreshed take on PyQt user interfaces

    This file is a part of the freshqt
    project and distributed under MIT license.
    https://github.com/kadir014/freshqt

"""

from pathlib import Path

from PyQt6.QtGui import QColor


PathLike = str | Path
ColorLike = str | tuple[int, int, int] | QColor