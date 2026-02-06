"""

    freshqt  -  A modern, refreshed take on PyQt user interfaces

    This file is a part of the freshqt
    project and distributed under MIT license.
    https://github.com/kadir014/freshqt

"""

from freshqt.core.models import SyntaxPalette, UIPalette


# Third-party licenses are listed in the NOTICE file at the project root

# https://draculatheme.com
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
    is_dark              = False,
    background_primary   = ALUCARD["background"],
    background_secondary = ALUCARD["selection"],
    background_tertiary  = ALUCARD["comment"],
    text_primary         = ALUCARD["foreground"],
    text_secondary       = "#2b2a2a",
    text_tertiary        = "#3b3939",
    brand_primary        = ALUCARD["purple"],
    brand_secondary      = ALUCARD["pink"],
    brand_tertiary       = ALUCARD["cyan"],
    text_selection       = ALUCARD["purple"],
    state_success        = ALUCARD["green"],
    state_warning        = ALUCARD["orange"],
    state_error          = ALUCARD["red"]
)