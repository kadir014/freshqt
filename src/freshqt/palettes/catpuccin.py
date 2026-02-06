"""

    freshqt  -  A modern, refreshed take on PyQt user interfaces

    This file is a part of the freshqt
    project and distributed under MIT license.
    https://github.com/kadir014/freshqt

"""

from freshqt.core.models import SyntaxPalette, UIPalette


# Third-party licenses are listed in the NOTICE file at the project root

# https://catppuccin.com
CATPUCCIN_FRAPPE = {
    "base": "#303446",
    "surface0": "#414559",
    "surface1": "#51576d",
    "text": "#c6d0f5",
    "subtext1": "#b5bfe2",
    "subtext0": "#a5adce",
    "overlay2": "#949cbb",
    "red": "#e78284",
    "maroon": "#ea999c",
    "peach": "#ef9f76",
    "yellow": "#e5c890",
    "green": "#a6d189",
    "teal": "#81c8be",
    "sky": "#99d1db",
    "sapphire": "#85c1dc",
    "blue": "#8caaee",
    "lavender": "#babbf1",
    "mauve": "#ca9ee6",
    "pink": "#f4b8e4",
    "flamingo": "#eebebe",
    "rosewater": "#f2d5cf"
}

# https://github.com/catppuccin/catppuccin/blob/main/docs/style-guide.md
SYNTAX_CATPUCCIN_FRAPPE = SyntaxPalette(
    identifier   = CATPUCCIN_FRAPPE["text"],
    operator     = CATPUCCIN_FRAPPE["sky"],
    brace        = CATPUCCIN_FRAPPE["overlay2"],
    string       = CATPUCCIN_FRAPPE["green"],
    comment      = CATPUCCIN_FRAPPE["overlay2"],
    keyword      = CATPUCCIN_FRAPPE["mauve"],
    numeric      = CATPUCCIN_FRAPPE["peach"],
    this         = CATPUCCIN_FRAPPE["red"],
    function     = CATPUCCIN_FRAPPE["blue"],
    preprocessor = CATPUCCIN_FRAPPE["rosewater"]
)

UI_CATPUCCIN_FRAPPE = UIPalette(
    is_dark              = True,
    background_primary   = CATPUCCIN_FRAPPE["base"],
    background_secondary = CATPUCCIN_FRAPPE["surface0"],
    background_tertiary  = CATPUCCIN_FRAPPE["surface1"],
    text_primary         = CATPUCCIN_FRAPPE["text"],
    text_secondary       = CATPUCCIN_FRAPPE["subtext1"],
    text_tertiary        = CATPUCCIN_FRAPPE["subtext0"],
    brand_primary        = CATPUCCIN_FRAPPE["lavender"],
    brand_secondary      = CATPUCCIN_FRAPPE["mauve"],
    brand_tertiary       = CATPUCCIN_FRAPPE["sapphire"],
    text_selection       = CATPUCCIN_FRAPPE["teal"],
    state_success        = CATPUCCIN_FRAPPE["green"],
    state_warning        = CATPUCCIN_FRAPPE["peach"],
    state_error          = CATPUCCIN_FRAPPE["red"]
)