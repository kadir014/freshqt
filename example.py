import os

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget, QSlider, QVBoxLayout, QCheckBox, QLabel, QPushButton
from PyQt6.QtGui import QColor, QFontDatabase, QFont, QPainter, QPen, QIcon

from src.freshqt.widgets import Slider, Code


def fill_background(
        widget: QWidget,
        color: tuple[int, int, int] | list[int] | QColor
        ):
    """
    Set background color role of a widget.
    
    Parameters
    ----------
    widget
        Widget to change background role of
    color
        RGB color
    """

    if isinstance(color, (tuple, list)):
        color = QColor(*color, alpha=255)

    widget.setAutoFillBackground(True)
    p = widget.palette()
    p.setColor(widget.backgroundRole(), color)
    widget.setPalette(p)


class CheckBox(QCheckBox):
    def __init__(self,
            text: str = "",
            parent: QWidget | None = None
            ) -> None:
        super().__init__(text=text, parent=parent)

        self._indicator_size = 14

        self._update_style()

        self.setCursor(Qt.CursorShape.PointingHandCursor)

    def _update_style(self) -> None:
        self.setStyleSheet(f"""
            QCheckBox {{
                font-family: Poppins;
                font-size: 14px;
                color: #ffffff;
            }}
            QCheckBox::indicator {{
                width: {self._indicator_size}px;
                height: {self._indicator_size}px;
                background-color: #44475A;
                border-radius: 4px;
                border: 1px solid #797d99;
            }}
            QCheckBox::indicator:unchecked:hover {{
                background-color: #6272A4;
            }}

            QCheckBox::indicator:checked {{
                border: 1px solid #BD93F9;
                background-color: #BD93F9;
            }}
        """)

    def paintEvent(self, e) -> None:
        super().paintEvent(e)

        pt = QPainter(self)
        pt.setRenderHint(QPainter.RenderHint.Antialiasing, on=True)

        if self.isChecked():
            w = 1
            icons["check"].paint(pt, w, 3, self._indicator_size, self._indicator_size)

class MainWindow(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("pyqt-fresh-kit Demo")
        fill_background(self, QColor("#282a36"))

        lyt = QVBoxLayout()
        self.setLayout(lyt)

        self.slider = Slider(orientation=Qt.Orientation.Horizontal)
        lyt.addWidget(self.slider)

        self.code = Code()
        lyt.addWidget(self.code)

        code_str = """
import pygame
pygame.init()
# This is a comment
clock = pygame.Clock()
del clock
        """

        self.code.editor.setPlainText(code_str.strip())

        self.cb = CheckBox("Accept Terms")
        lyt.addWidget(self.cb)

        typo_text = "The quick brown fox jumps over the lazy dog"

        weights = (
            "Black", "ExtraBold", "Bold", "SemiBold",
            "Medium", "Regular",
            "Light", "ExtraLight", "Thin"
        )
        for i in range(10):
            lb = QLabel(typo_text)
            lyt.addWidget(lb)
            lb.setStyleSheet(f"font-family: Outfit; font-weight: {i * 100}; font-size: 14px; color: #ffffff;")


icons: dict[str, QIcon] = dict()

if __name__ == "__main__":
    app = QApplication([])

    # SVG icons have to be loaded before any raster icons so Qt can select proper icon engine
    for root, _, files in os.walk("data/heroicons"):
        for file in files:
            icon_name = file.replace(".svg", "")
            iconpath = os.path.join(root, file)
            icon = QIcon(iconpath)
            icons[icon_name] = icon

            print(f"Icon '{iconpath}' loaded with key: {icon_name}")

    for root, _, files in os.walk("data/fonts"):
        for file in files:
            fontpath = os.path.join(root, file)
            font_id = QFontDatabase.addApplicationFont(fontpath)
            if font_id < 0:
                print(f"Font {file} couldn't load.")
            else:
                font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
                print(f"Font '{file}' loaded with ID: {font_id} Families: {font_family}")

    # https://stackoverflow.com/a/67219364
    # PreferNoHinting solves fonts looking weird on Windows
    font = QFont("Poppins")
    font.setHintingPreference(QFont.HintingPreference.PreferNoHinting)
    app.setFont(font)

    main_window = MainWindow()
    main_window.show()

    app.exec()