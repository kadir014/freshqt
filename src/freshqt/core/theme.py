"""

    freshqt  -  A modern, refreshed take on PyQt user interfaces

    This file is a part of the freshqt
    project and distributed under MIT license.
    https://github.com/kadir014/freshqt

"""

import platform
from pathlib import Path

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget
from PyQt6.QtGui import QColor

from freshqt.core.typing import ColorLike
from freshqt.core.models import UIPalette, TypographyRamp, TypographyType
from freshqt.core.base_icon_manager import BaseIconManager
from freshqt.palettes.catppuccin import UI_CATPPUCCIN_FRAPPE


class Theme:
    """
    Universal theme manager.
    """

    def __init__(self) -> None:
        self.__widgets: list["QWidget | Themeable"] = []
        self.__recent_widgets: list["QWidget | Themeable"] = []
        self.__palette: UIPalette
        self.__typo_ramp: TypographyRamp

        self.update_palette(UI_CATPPUCCIN_FRAPPE)

        self.__font_family = "Arial"
        self.__font_scale = 1.0

        self.update_typo_ramp(TypographyRamp(
            10,
            14,
            19,
            24,
            28,
            32,
            40
        ))

        self.icons: BaseIconManager | None = None
    
    @property
    def palette(self) -> UIPalette:
        """ Loaded & processed UI palette. """
        return self.__palette
    
    @property
    def typo_ramp(self) -> TypographyRamp:
        """ Loaded typography ramp. """
        return self.__typo_ramp
    
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

    def update_palette(self, palette: UIPalette) -> None:
        """
        Update theme palette data.
        
        Parameters
        ----------
        palette
            UI palette
        """

        self.__palette = palette

        for field in self.__palette.__dataclass_fields__:
            if field in ("name", "is_dark"): continue
            
            c = getattr(self.__palette, field)
            if isinstance(c, tuple):
                setattr(self.__palette, field, QColor(*c))
            else:
                setattr(self.__palette, field, QColor(c))

        self.update_widgets()

    def update_typo_ramp(self, typo_ramp: TypographyRamp) -> None:
        """
        Update theme typography ramp.

        Parameters
        ----------
        typo_ramp
            Typography ramp
        """

        self.__typo_ramp = typo_ramp
        self.update_widgets()

    def update_widget(self, widget: QWidget) -> None:
        """ Update single widget's style. """

        widget.update_theme(self)
        widget.update_theme_role(self)
        widget.update()

    def update_widgets(self) -> None:
        """ Update all widgets' styles. """

        for widget in self.__widgets:
            widget.update_theme(self)

        for widget in self.__widgets:
            widget.update_theme_role(self)
        
        for widget in self.__widgets:
            widget.update()

        self.__recent_widgets.clear()

    def update_last_widgets(self) -> None:
        """ Update recently added widgets since last update. """

        for widget in self.__recent_widgets:
            widget.update_theme(self)

        for widget in self.__recent_widgets:
            widget.update_theme_role(self)
        
        for widget in self.__recent_widgets:
            widget.update()

        self.__recent_widgets.clear()

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
        self.__recent_widgets.append(widget)
        
        if update:
            self.update_widget(widget)
            #self.update_widgets()

    def remove_widget(self,
            widget: "QWidget | Themeable",
            update: bool = True,
            no_error: bool = True
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

        if widget in self.__recent_widgets:
            self.__recent_widgets.remove(widget)

        if update:
            self.update_widgets()

    def remove_widgets_by_type(self, type_: type, update: bool = True) -> None:
        """
        Remove widgets by type.
        
        Parameters
        ----------
        type_
            Instance type to check against
        update
            Update all widgets after removal is done
        """

        to_be_removed = []
        for widget in self.__widgets:
            if isinstance(widget, type_):
                to_be_removed.append(widget)

                if widget in self.__recent_widgets:
                    self.__recent_widgets.remove(widget)

        for widget in to_be_removed:
            self.remove_widget(widget, update=False)
            if hasattr(widget, "theme_removed"):
                widget.theme_removed()

        if update:
            self.update_widgets()

    def get_typo_size(self, type: TypographyType) -> None:
        return getattr(self.__typo_ramp, type.name.lower())

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
        
        if isinstance(color, (tuple, list)):
            return QColor(*color)
        
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


def win32_change_titlebar_theme(
        widget: QWidget,
        dark: bool,
        force_update: bool = True
        ) -> int:
    import ctypes
    import ctypes.wintypes

    hwnd = int(widget.winId())

    # https://learn.microsoft.com/en-us/windows/win32/api/dwmapi/ne-dwmapi-dwmwindowattribute
    DWMWA_USE_IMMERSIVE_DARK_MODE = 20

    dark_mode = ctypes.wintypes.BOOL(int(dark))

    dwmapi = ctypes.windll.dwmapi

    ret = dwmapi.DwmSetWindowAttribute(
        hwnd,
        DWMWA_USE_IMMERSIVE_DARK_MODE,
        ctypes.byref(dark_mode),
        ctypes.sizeof(dark_mode)
    )

    if force_update and ret == 0:
        """
        I went with this resizing approach, because none of the win32 API
        calls repainted the DWM area. Only this seems to work the most stable.

        Solutions failed:
        - widget.hide() & widget.show()
           - Too unstable, breaks geometry and layouts
        - dwmapi.DwmFlush
        - user32.UpdateWindow
        - user32.RedrawWindow
           - None of the flags work
        - user32.SetWindowPos
           - With NOMOVE and NORESIZE flags, it doesn't work
        """

        was_maximized = widget.isMaximized()
        
        if not was_maximized:
            rect = widget.geometry()
            w, h = rect.width(), rect.height()
        else:
            normal_rect = widget.normalGeometry()
            w, h = normal_rect.width(), normal_rect.height()

        if was_maximized:
            widget.showNormal()

        widget.resize(w - 1, h)
        widget.resize(w, h)

        if was_maximized:
            widget.showMaximized()

    return ret


def change_titlebar_theme(widget: QWidget, dark: bool) -> int:
    """
    Change theme of the titlebar.

    Parameters
    ----------
    widget
        Widget with visible window titlebar
    dark
        Whether to enable dark or light theme

    Returns
    -------
        Returns 0 if success, otherwise the return code of the OS API call
    """

    if platform.system() == "Windows":
        return win32_change_titlebar_theme(widget, dark, force_update=True)

    else:
        return 1