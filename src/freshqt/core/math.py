"""

    freshqt  -  A modern, refreshed take on PyQt user interfaces

    This file is a part of the freshqt
    project and distributed under MIT license.
    https://github.com/kadir014/freshqt

"""


def clamp(x: float, low: float, high: float) -> float:
    return max(low, min(x, high))