"""

    freshqt  -  A modern, refreshed take on PyQt user interfaces

    This file is a part of the freshqt
    project and distributed under MIT license.
    https://github.com/kadir014/freshqt

"""

import json
from pathlib import Path

from PyQt6.QtWidgets import QWidget
from PyQt6.QtGui import QColor

from freshqt.core.typing import PathLike, ColorLike
from freshqt.core.models import UIPalette


class Theme:
    """
    Universal theme manager.
    """

    def __init__(self) -> None:
        self.__widgets: list["QWidget | Themeable"] = []
        self.__palette: UIPalette
        self.__name = ""

        self.__font_family = "Arial"
        self.__font_scale = 1.0
    
    @property
    def name(self) -> str:
        """ Loaded theme name. """
        return self.__name
    
    @property
    def palette(self) -> UIPalette:
        """ Loaded & processed UI palette. """
        return self.__palette
    
    @property
    def font_family(self) -> str:
        return self.__font_family
    
    @font_family.setter
    def font_family(self, value: str) -> None:
        self.__font_family = value
        self.update_widgets()

    @property
    def font_scale(self) -> float:
        return self.__font_scale
    
    @font_scale.setter
    def font_scale(self, value: float) -> None:
        self.__font_scale = value
        self.update_widgets()

    def update(self, palette: UIPalette) -> None:
        """
        Update theme data.
        
        Parameters
        ----------
        palette
            UI palette
        """

        self.__palette = palette

        for field in self.__palette.__dataclass_fields__:
            c = getattr(self.__palette, field)
            if isinstance(c, tuple):
                setattr(self.__palette, field, QColor(*c))
            else:
                setattr(self.__palette, field, QColor(c))

        self.update_widgets()

    def update_widgets(self) -> None:
        """ Update all widgets' styles. """

        for widget in self.__widgets:
            widget.update_theme(self)

        for widget in self.__widgets:
            widget.update_theme_role(self)
        
        for widget in self.__widgets:
            widget.update()

    def add_widget(self,
            widget: "QWidget | Themeable",
            update: bool = True
        ) -> None:
        """
        Add a new widget.

        Parameters
        ----------
        widget
            Themeable widget
        update
            Whether to update all widgets after this operation
        """

        self.__widgets.append(widget)
        if update: self.update_widgets()

    def remove_widget(self,
            widget: "QWidget | Themeable",
            update: bool = True,
            no_error: bool = False
        ) -> None:
        """
        Remove a widget.
        
        Parameters
        ----------
        widget
            Themeable widget
        update
            Whether to update all widgets after this operation
        no_error
            Suppress error if widget is not a child
        """
        
        if no_error:
            if widget in self.__widgets:
                self.__widgets.remove(widget)
        else:
            self.__widgets.remove(widget)

        if update:
            self.update_widgets()

    @staticmethod
    def qss(color: ColorLike) -> str:
        """ Convert color to QSS-compatible color string. """

        if isinstance(color, str):
            return color
        
        elif isinstance(color, (tuple, list)):
            return f"rgb({color[0]}, {color[1]}, {color[1]})"
        
        elif isinstance(color, QColor):
            return f"rgb({color.red()}, {color.green()}, {color.blue()})"
        
        # Just hope the color is already in correct format
        return str(color)
    
    @staticmethod
    def qcolor(color: ColorLike) -> QColor:
        """ Convert color to QColor. """

        if isinstance(color, str):
            return QColor(color)
        
        elif isinstance(color, (tuple, list)):
            return QColor(*color)
        
        elif isinstance(color, QColor):
            return color
        
        # Just hope the QColor constructor supports it
        return QColor(color)


class Themeable:
    """
    Themable widget interface.
    """

    def update_theme(self, theme: Theme) -> None:
        """ Update the style of the widget according to theme. """
        ...

    def update_theme_role(self, theme: Theme) -> None:
        """ Update background role of the widget according to theme. """
        ...


def change_titlebar_theme(widget: QWidget, dark: bool) -> int:
    """
    Change theme of the titlebar.

    Warning: Only for Windows 10 and above.

    Parameters
    ----------
    widget
        Widget with visible window titlebar
    dark
        Whether to enable dark or light theme

    Returns
    -------
        Returns 0 if success, otherwise the return code of the Windows API call
    """
    import ctypes
    import ctypes.wintypes

    hwnd = int(widget.winId())

    S_OK = 0x00000000

    # https://learn.microsoft.com/en-us/windows/win32/api/dwmapi/ne-dwmapi-dwmwindowattribute
    DWMWA_USE_IMMERSIVE_DARK_MODE = 20
    dwmapi = ctypes.windll.dwmapi

    dark_mode = ctypes.wintypes.BOOL(int(dark))

    return dwmapi.DwmSetWindowAttribute(
        hwnd,
        DWMWA_USE_IMMERSIVE_DARK_MODE,
        ctypes.byref(dark_mode),
        ctypes.sizeof(dark_mode)
    )