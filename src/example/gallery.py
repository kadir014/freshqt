"""

    freshqt  -  A modern, refreshed take on PyQt user interfaces

    This file is a part of the freshqt
    project and distributed under MIT license.
    https://github.com/kadir014/freshqt

"""

import platform

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout
from PyQt6.QtGui import QFont, QIcon

from freshqt.widgets import (
    Slider,
    Code,
    TypoLabel,
    KbdLabel,
    BadgeLabel,
    CheckBox,
    Switch,
    Button
)
from freshqt.core import Theme, Themeable, change_titlebar_theme
from freshqt.assets import HEROICONS

from freshqt.palettes.dracula import UI_DRACULA
from freshqt.palettes.alucard import UI_ALUCARD
from freshqt.palettes.catpuccin import UI_CATPUCCIN_FRAPPE


# You would probably have a smarter way to handle these global
# states, but for this example, they're enough.
theme = Theme()
icons: dict[str, QIcon] = {}


class MainWindow(QWidget, Themeable):
    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("FreshQT Design System - Gallery Demo")

        lyt = QVBoxLayout()
        self.setLayout(lyt)

        self.slider = Slider()
        theme.add_widget(self.slider)
        lyt.addWidget(self.slider)
        self.slider.setFixedHeight(15)
        self.slider.groove_height = 6

        self.slider.setMinimum(0)
        self.slider.setMaximum(200)
        self.slider.setValue(100)
        self.slider.valueChanged.connect(self.slider_change)

        lb0 = TypoLabel("Hello")
        theme.add_widget(lb0)
        lyt.addWidget(lb0)

        kbdlyt = QHBoxLayout()
        kbdlyt.setAlignment(Qt.AlignmentFlag.AlignLeft)
        lyt.addLayout(kbdlyt)
        keys = ("ESC", "Right", "Return", "cmd", "Ctrl + B")
        for key in keys:
            kbdlbl = KbdLabel(key)
            theme.add_widget(kbdlbl)
            kbdlyt.addWidget(kbdlbl)

        bdglbl = BadgeLabel("Badge", color=theme.palette.brand_primary)
        theme.add_widget(bdglbl)
        kbdlyt.addWidget(bdglbl)

        bdglbl = BadgeLabel("Success", color=theme.palette.state_success)
        theme.add_widget(bdglbl)
        kbdlyt.addWidget(bdglbl)

        bdglbl = BadgeLabel("Warning", color=theme.palette.state_warning)
        theme.add_widget(bdglbl)
        kbdlyt.addWidget(bdglbl)

        bdglbl = BadgeLabel("Failed", color=theme.palette.state_error)
        theme.add_widget(bdglbl)
        kbdlyt.addWidget(bdglbl)

        self.checkbox = CheckBox("Accept terms")
        theme.add_widget(self.checkbox)
        lyt.addWidget(self.checkbox)
        self.checkbox.indicator_icon = icons["check"]
        self.checkbox.toggle()

        self.switch = Switch()
        theme.add_widget(self.switch)
        lyt.addWidget(self.switch)

        b0 = Button("Accept terms")
        theme.add_widget(b0)
        lyt.addWidget(b0)
        b0.setMinimumSize(75, 40)

        #self.switch.setMinimumSize(100, 50)
        #self.switch.setFixedSize(100, 50)
        self.switch.setFixedSize(int(25 + 25 * 1.3), 25)

        self.code = Code()
        theme.add_widget(self.code)
        lyt.addWidget(self.code)

        code_str = """
import pygame
pygame.init()
# This is a comment
clock = pygame.Clock()
del clock

@property
def font_family(self) -> str:
    ...
        """

        self.code.editor.setPlainText(code_str.strip())

        if platform.system() == "Windows":
            change_titlebar_theme(self, True)

    def update_theme(self, theme: Theme) -> None:
        self.setStyleSheet(f"background-color: {theme.qss(theme.palette.background_primary)};")

    def slider_change(self):
        v = self.slider.value()

        theme.font_scale = v / 100


def main() -> None:
    app = QApplication([])

    if platform.system() == "Windows":
        # https://stackoverflow.com/a/67219364
        # PreferNoHinting solves fonts looking weird on Windows
        font = app.font()
        font.setHintingPreference(QFont.HintingPreference.PreferNoHinting)
        app.setFont(font)

    # SVG icons have to be loaded before any raster icons so Qt can select proper icon engine
    for iconname in HEROICONS:
        iconpath = HEROICONS[iconname]
        icon = QIcon(str(iconpath.absolute()))
        icons[iconname] = icon

        print(f"Icon '{iconpath}' loaded with key: {iconname}")

    #theme.update_palette(UI_CATPUCCIN_FRAPPE)
    theme.font_family = "Outfit"
    theme.update_widgets()

    main_window = MainWindow()
    theme.add_widget(main_window)
    main_window.show()

    app.exec()