"""

    freshqt  -  A modern, refreshed take on PyQt user interfaces

    This file is a part of the freshqt
    project and distributed under MIT license.
    https://github.com/kadir014/freshqt

"""

from freshqt.core.models import SyntaxPalette, UIPalette


# See the licenses in NOTICE file at root for third party licenses

# https://draculatheme.com
DRACULA = {
    "background": "#282A36",
    "foreground": "#F8F8F2",
    "selection":  "#44475A",
    "comment":    "#6272A4",
    "red":        "#FF5555",
    "orange":     "#FFB86C",
    "yellow":     "#F1FA8C",
    "green":      "#50FA7B",
    "cyan":       "#8BE9FD",
    "purple":     "#BD93F9",
    "pink":       "#FF79C6"
}

SYNTAX_DRACULA = SyntaxPalette(
    identifier   = DRACULA["foreground"],
    operator     = DRACULA["orange"],
    brace        = DRACULA["comment"],
    string       = DRACULA["green"],
    comment      = DRACULA["comment"],
    keyword      = DRACULA["pink"],
    numeric      = DRACULA["cyan"],
    this         = DRACULA["red"],
    function     = DRACULA["purple"],
    preprocessor = DRACULA["purple"]
)

UI_DRACULA = UIPalette(
    is_dark              = True,
    background_primary   = DRACULA["background"],
    background_secondary = DRACULA["selection"],
    background_tertiary  = "#4f5369",
    text_primary         = DRACULA["foreground"],
    text_secondary       = "#ebebe1",
    text_tertiary        = "#cfcfc4",
    brand_primary        = DRACULA["purple"],
    brand_secondary      = DRACULA["pink"],
    brand_tertiary       = DRACULA["cyan"],
    text_selection       = DRACULA["purple"],
    state_success        = DRACULA["green"],
    state_warning        = DRACULA["orange"],
    state_error          = DRACULA["red"]
)