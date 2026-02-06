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
    Colors for each almost-language-agnostic syntactic element.

    Fields
    ------
    identifier
        Default color for all identifiers and unclassified symbols
    operator
        Operators and symbolic expressions
    brace
        Braces, brackets, and structural punctuation
    string
        String and character literals
    comment
        Line and block comments
    keyword
        Language keywords and reserved words
    numeric
        Numeric literals
    this
        Contextual self-referencing keywords (e.g. `this`, `self`, `cls`, ...)
    function
        Function and method names
    preprocessor
        Preprocessor directives, annotations, or decorators
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

    Fields
    ------
    is_dark
        Whether this palette is light text on dark surface (dark theme) or
        dark text on light surface (light theme)
    background_primary
        Primary background surface color
    background_secondary
        Secondary background surface color
    background_tertiary
        Tertiary background surface color
    text_primary
        Primary foreground color for text content and UI glyphs
    text_secondary
        Secondary foreground color for text content and UI glyphs
    text_tertiary
        Tertiary foreground color for text content and UI glyphs
    text_fallback
        Foreground color used when the primary text color fails contrast
        requirements on the current surface
    brand_primary
        Primary branding accent color
    brand_secondary
        Secondary branding accent color
    brand_tertiary
        Tertiary branding accent color
    text_selection
        Background color for text selection
    state_success
        Success state color
    state_warning
        Warning state color
    state_error
        Error state color
    """

    is_dark: bool

    background_primary: ColorLike
    background_secondary: ColorLike
    background_tertiary: ColorLike

    text_primary: ColorLike
    text_secondary: ColorLike
    text_tertiary: ColorLike
    text_fallback: ColorLike

    brand_primary: ColorLike
    brand_secondary: ColorLike
    brand_tertiary: ColorLike

    text_selection: ColorLike

    state_success: ColorLike
    state_warning: ColorLike
    state_error: ColorLike


class SyntaxLanguage(Enum):
    """
    Supported languages for syntax highlighting.
    """

    PLAIN = auto()
    JSON = auto()
    PYTHON = auto()


@dataclass
class TypographyRamp:
    """
    Typography type sizes in pixels.
    """

    caption: int
    body: int
    subtitle: int
    title3: int
    title2: int
    title1: int
    large_title: int


class TypographyType(Enum):
    """
    Typography types.
    """

    CAPTION = auto()
    BODY = auto()
    SUBTITLE = auto()
    TITLE3 = auto()
    TITLE2 = auto()
    TITLE1 = auto()
    LARGE_TITLE = auto()