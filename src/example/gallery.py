"""

    freshqt  -  A modern, refreshed take on PyQt user interfaces

    This file is a part of the freshqt
    project and distributed under MIT license.
    https://github.com/kadir014/freshqt

"""

import platform

from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout
from PyQt6.QtGui import QFont

from freshqt.widgets import Slider, Code
from freshqt.core import Theme, Themeable, change_titlebar_theme
from freshqt.palettes.dracula import UI_DRACULA
from freshqt.palettes.alucard import UI_ALUCARD


# Global theme manager
theme = Theme()


class MainWindow(QWidget, Themeable):
    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("FreshQT Demo")

        lyt = QVBoxLayout()
        self.setLayout(lyt)

        self.slider = Slider()
        theme.add_widget(self.slider)
        lyt.addWidget(self.slider)

        self.code = Code()
        theme.add_widget(self.code)
        lyt.addWidget(self.code)

        code_str = """
import pygame
pygame.init()
# This is a comment
clock = pygame.Clock()
del clock
        """

        self.code.editor.setPlainText(code_str.strip())

        if platform.system() == "Windows":
            change_titlebar_theme(self, True)

    def update_theme(self, theme: Theme) -> None:
        self.setStyleSheet(f"background-color: {theme.qss(theme.palette.background_primary)};")


def main() -> None:
    app = QApplication([])

    theme.update(UI_DRACULA)

    main_window = MainWindow()
    theme.add_widget(main_window)
    main_window.show()

    if platform.system() == "Windows":
        # https://stackoverflow.com/a/67219364
        # PreferNoHinting solves fonts looking weird on Windows
        font = app.font()
        font.setHintingPreference(QFont.HintingPreference.PreferNoHinting)
        app.setFont(font)

    app.exec()