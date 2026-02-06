"""

    freshqt  -  A modern, refreshed take on PyQt user interfaces

    This file is a part of the freshqt
    project and distributed under MIT license.
    https://github.com/kadir014/freshqt

"""

from PyQt6.QtGui import QColor


def luminance(color: QColor) -> float:
    """ Calculate relative luminance of the color. """

    # https://en.wikipedia.org/wiki/Relative_luminance
    Y = (0.2125, 0.7154, 0.0721)
    return color.redF() * Y[0] + color.greenF() * Y[1] + color.blueF() * Y[2]


def sRGB_to_linear_cheap(color: QColor) -> QColor:
    """
    Convert from non-linear sRGB space to linear RGB space using approximation.
    """

    r = color.redF() ** 2.2
    g = color.greenF() ** 2.2
    b = color.blueF() ** 2.2

    return QColor(int(r * 255.0), int(g * 255.0), int(b * 255.0))


def WCAG(a: QColor, b: QColor) -> float:
    """
    Calculate WCAG contrast ratio of two colors.
    """

    # https://www.w3.org/TR/WCAG20/#contrast-ratiodef

    La = luminance(sRGB_to_linear_cheap(a))
    Lb = luminance(sRGB_to_linear_cheap(b))

    L1 = max(La, Lb)
    L2 = min(La, Lb)

    return (L1 + 0.05) / (L2 + 0.05)


WCAG_NORMAL_TEXT = 4.5