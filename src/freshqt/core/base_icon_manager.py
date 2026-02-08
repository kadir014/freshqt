"""

    freshqt  -  A modern, refreshed take on PyQt user interfaces

    This file is a part of the freshqt
    project and distributed under MIT license.
    https://github.com/kadir014/freshqt

"""

from abc import ABC, abstractmethod

from PyQt6.QtGui import QIcon, QColor


class BaseIconManager(ABC):
    """
    Icon manager base class.

    You would want to implement a fast way to handle icons
    with multiple colors so the themed widgets can use them.

    For example loading colored ones or coloring the default ones
    in runtime and then caching them.
    """

    @abstractmethod
    def get(self, name: str, color: QColor) -> QIcon:
        ...