"""

    freshqt  -  A modern, refreshed take on PyQt user interfaces

    This file is a part of the freshqt
    project and distributed under MIT license.
    https://github.com/kadir014/freshqt

"""

from dataclasses import dataclass
from enum import Enum, auto

from freshqt.core.typing import ColorLike


class TweenRepeatMode(Enum):
    """
    Repeating mode for tweening animations.

    Fields
    ------
    NONE
        Do not repeat.
    LOOP
        Repeat by looping to start.
    BOUNCE
        Repeat and reverse at each loop.
    """
    
    NONE = auto()
    LOOP = auto()
    BOUNCE = auto()


@dataclass
class SyntaxPalette:
    """
    Colors for each syntactic element of a language.
    """

    identifier: ColorLike
    operator: ColorLike
    brace: ColorLike
    string: ColorLike
    comment: ColorLike
    keyword: ColorLike
    numeric: ColorLike
    this: ColorLike
    function: ColorLike
    preprocessor: ColorLike


@dataclass
class UIPalette:
    """
    Colors for primary elements of the user interface.
    """

    is_dark: bool

    background_primary: ColorLike
    background_secondary: ColorLike
    background_tertiary: ColorLike

    text_primary: ColorLike
    text_secondary: ColorLike
    text_tertiary: ColorLike

    brand_primary: ColorLike
    brand_secondary: ColorLike
    brand_tertiary: ColorLike

    text_selection: ColorLike

    state_success: ColorLike
    state_warning: ColorLike
    state_error: ColorLike