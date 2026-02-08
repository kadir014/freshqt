"""

    freshqt  -  A modern, refreshed take on PyQt user interfaces

    This file is a part of the freshqt
    project and distributed under MIT license.
    https://github.com/kadir014/freshqt

"""

from freshqt.core.models import SyntaxPalette, UIPalette


# Third-party licenses are listed in the NOTICE file at the project root

# Dracula official home: https://draculatheme.com


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
    name                 = "Dracula",
    is_dark              = True,
    background_primary   = DRACULA["background"],
    background_secondary = DRACULA["selection"],
    background_tertiary  = "#4f5369",
    text_primary         = DRACULA["foreground"],
    text_secondary       = "#ebebe1",
    text_tertiary        = "#cfcfc4",
    text_fallback        = "#1f1f1f",
    brand_primary        = DRACULA["purple"],
    brand_secondary      = DRACULA["pink"],
    brand_tertiary       = DRACULA["cyan"],
    text_selection       = DRACULA["purple"],
    state_success        = DRACULA["green"],
    state_warning        = DRACULA["orange"],
    state_error          = DRACULA["red"]
)


ALUCARD = {
    "background": "#fffbeb",
    "foreground": "#1f1f1f",
    "selection":  "#cfcfde",
    "comment":    "#6c664b",
    "red":        "#cb3a2a",
    "orange":     "#a34d14",
    "yellow":     "#846e15",
    "green":      "#14710a",
    "cyan":       "#036a96",
    "purple":     "#644ac9",
    "pink":       "#a3144d"
}

SYNTAX_ALUCARD = SyntaxPalette(
    identifier   = ALUCARD["foreground"],
    operator     = ALUCARD["orange"],
    brace        = ALUCARD["comment"],
    string       = ALUCARD["green"],
    comment      = ALUCARD["comment"],
    keyword      = ALUCARD["pink"],
    numeric      = ALUCARD["cyan"],
    this         = ALUCARD["red"],
    function     = ALUCARD["purple"],
    preprocessor = ALUCARD["purple"]
)

UI_ALUCARD = UIPalette(
    name                 = "Alucard",
    is_dark              = False,
    background_primary   = ALUCARD["background"],
    background_secondary = ALUCARD["selection"],
    background_tertiary  = ALUCARD["comment"],
    text_primary         = ALUCARD["foreground"],
    text_secondary       = "#2b2a2a",
    text_tertiary        = "#3b3939",
    text_fallback        = "#F8F8F2",
    brand_primary        = ALUCARD["purple"],
    brand_secondary      = ALUCARD["pink"],
    brand_tertiary       = ALUCARD["cyan"],
    text_selection       = ALUCARD["purple"],
    state_success        = ALUCARD["green"],
    state_warning        = ALUCARD["orange"],
    state_error          = ALUCARD["red"]
)