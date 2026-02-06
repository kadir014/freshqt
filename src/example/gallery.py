"""

    freshqt  -  A modern, refreshed take on PyQt user interfaces

    This file is a part of the freshqt
    project and distributed under MIT license.
    https://github.com/kadir014/freshqt

"""

import platform

from PyQt6.QtCore import Qt, QT_VERSION_STR, PYQT_VERSION_STR
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
    Button,
    Divider
)
from freshqt.core import Theme, Themeable, change_titlebar_theme, SyntaxLanguage
from freshqt.core import __version__ as freshqt_version
from freshqt.assets import HEROICONS

from freshqt.palettes.dracula import UI_DRACULA
from freshqt.palettes.alucard import UI_ALUCARD
from freshqt.palettes.catpuccin import UI_CATPUCCIN_FRAPPE, UI_CATPUCCIN_LATTE, SYNTAX_CATPUCCIN_FRAPPE, SYNTAX_CATPUCCIN_LATTE


# You would probably have a smarter way to handle these global
# states, but for this example, they're enough.
theme = Theme()
icons: dict[str, QIcon] = {}


class MainWindow(QWidget, Themeable):
    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("FreshQT Design System - Gallery Demo")

        if platform.system() == "Windows":
            change_titlebar_theme(self, theme.palette.is_dark)

        mainlyt = QHBoxLayout()
        mainlyt.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.setLayout(mainlyt)

        self.plyt = QVBoxLayout()
        self.plyt.setAlignment(Qt.AlignmentFlag.AlignTop)
        mainlyt.addLayout(self.plyt)

        self.add_badge_pair("Python", platform.python_version())
        self.add_badge_pair("Qt", QT_VERSION_STR)
        self.add_badge_pair("PyQt", PYQT_VERSION_STR)
        self.add_badge_pair("FreshQt", freshqt_version)

        divider = Divider(orientation=Qt.Orientation.Horizontal)
        theme.add_widget(divider)
        self.plyt.addWidget(divider)


        divider = Divider(orientation=Qt.Orientation.Vertical)
        theme.add_widget(divider)
        mainlyt.addWidget(divider)


        lyt = QVBoxLayout()
        mainlyt.addLayout(lyt)

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

        bdglbl = BadgeLabel("Badge", color="brand_primary")
        theme.add_widget(bdglbl)
        kbdlyt.addWidget(bdglbl)

        bdglbl = BadgeLabel("Success", color="state_success")
        theme.add_widget(bdglbl)
        kbdlyt.addWidget(bdglbl)

        bdglbl = BadgeLabel("Warning", color="state_warning")
        theme.add_widget(bdglbl)
        kbdlyt.addWidget(bdglbl)

        bdglbl = BadgeLabel("Failed", color="state_error")
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
        self.switch.setFixedSize(int(25 + 25 * 1.3), 25)
        self.switch.toggled.connect(self.switch_toggled)
        self.switch.off_icon = icons["moon"]
        self.switch.on_icon = icons["sun"]

        btn_lyt = QHBoxLayout()
        btn_lyt.setAlignment(Qt.AlignmentFlag.AlignLeft)
        lyt.addLayout(btn_lyt)
        variants = (
            Button.Variant.BRAND,
            Button.Variant.SECONDARY,
            Button.Variant.OUTLINE,
            Button.Variant.GHOST
        )
        for variant in variants:
            btn = Button(variant.name.lower().capitalize(), variant=variant)
            theme.add_widget(btn)
            btn_lyt.addWidget(btn)
            btn.setFixedSize(90, 32)

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

        self.code.text = code_str.strip()
        self.code.language = SyntaxLanguage.PYTHON

    def update_theme(self, theme: Theme) -> None:
        self.setStyleSheet(f"background-color: {theme.qss(theme.palette.background_primary)};")

    def add_badge_pair(self, left: str, right: str) -> None:
        pair_lyt = QHBoxLayout()
        self.plyt.addLayout(pair_lyt)

        left_lbl = TypoLabel(left)
        theme.add_widget(left_lbl)
        pair_lyt.addWidget(left_lbl)

        right_lbl = BadgeLabel(right, color="background_secondary")
        theme.add_widget(right_lbl)
        pair_lyt.addWidget(right_lbl)

    def slider_change(self) -> None:
        v = self.slider.value()
        theme.font_scale = v / 100

    def switch_toggled(self) -> None:
        if self.switch.on:
            theme.update_palette(UI_CATPUCCIN_LATTE)
            self.code.syntax_palette = SYNTAX_CATPUCCIN_LATTE
        else:
            theme.update_palette(UI_CATPUCCIN_FRAPPE)
            self.code.syntax_palette = SYNTAX_CATPUCCIN_FRAPPE

        if platform.system() == "Windows":
            change_titlebar_theme(self, theme.palette.is_dark)


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

    theme.update_palette(UI_CATPUCCIN_FRAPPE)
    theme.font_family = "Outfit"

    main_window = MainWindow()
    theme.add_widget(main_window)
    main_window.show()

    app.exec()