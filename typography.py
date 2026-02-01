import os

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget, QSlider, QVBoxLayout, QHBoxLayout, QCheckBox, QLabel
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

class MainWindow(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("pyqt-fresh-kit Demo")
        fill_background(self, QColor("#282a36"))

        lyt = QVBoxLayout()
        self.setLayout(lyt)

        sliderlyt = QHBoxLayout()
        lyt.addLayout(sliderlyt)

        self.slider_title_lbl = QLabel("Font Size")
        self.slider_val_lbl = QLabel("4px")
        self.slider_title_lbl.setStyleSheet(f"font-family: Outfit; font-size: 16px; color: #ffffff;")
        self.slider_val_lbl.setStyleSheet(f"font-family: Outfit; font-size: 16px; color: #ffffff;")
        sliderlyt.addWidget(self.slider_title_lbl)
        sliderlyt.addWidget(self.slider_val_lbl, alignment=Qt.AlignmentFlag.AlignRight)

        self.slider = Slider(orientation=Qt.Orientation.Horizontal)
        self.slider.setMinimum(4)
        self.slider.setMaximum(48)
        lyt.addWidget(self.slider)
        self.slider.valueChanged.connect(self.slider_value_change)

        lyt.addSpacing(15)

        typo_text = "The quick brown fox jumps over the lazy dog"

        # Weight is [100, 900]
        # https://doc.qt.io/qt-6/qfont.html#Weight-enum
        self.weight_labels: list[QLabel] = []
        for i in range(1, 10):
            lbl = QLabel(typo_text)
            lyt.addWidget(lbl)
            #lbl.setStyleSheet(f"font-family: Outfit; font-weight: {i * 100}; font-size: 14px; color: #ffffff;")
            self.weight_labels.append(lbl)

    def slider_value_change(self) -> None:
        val = self.slider.value()

        self.slider_val_lbl.setText(f"{val}px")

        for i, lbl in enumerate(self.weight_labels):
            weight = (i + 1) * 100
            lbl.setStyleSheet(f"font-family: Outfit; font-weight: {weight}; font-size: {val}px; color: #ffffff;")

            #lbl.setStyleSheet(f"font-size: {val}px;")


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
    font = QFont()
    font.setHintingPreference(QFont.HintingPreference.PreferNoHinting)
    app.setFont(font)

    main_window = MainWindow()
    main_window.show()

    app.exec()