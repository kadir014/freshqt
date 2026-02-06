"""

    freshqt  -  A modern, refreshed take on PyQt user interfaces

    This file is a part of the freshqt
    project and distributed under MIT license.
    https://github.com/kadir014/freshqt

"""

from freshqt.core.models import SyntaxPalette, UIPalette


# Third-party licenses are listed in the NOTICE file at the project root

# Catpuccin official home: https://catppuccin.com
# Catpuccin styling guide: https://github.com/catppuccin/catppuccin/blob/main/docs/style-guide.md


CATPUCCIN_FRAPPE = {
    "crust": "#232634",
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
    text_fallback        = CATPUCCIN_FRAPPE["crust"],
    brand_primary        = CATPUCCIN_FRAPPE["mauve"],
    brand_secondary      = CATPUCCIN_FRAPPE["maroon"],
    brand_tertiary       = CATPUCCIN_FRAPPE["sapphire"],
    text_selection       = CATPUCCIN_FRAPPE["teal"],
    state_success        = CATPUCCIN_FRAPPE["green"],
    state_warning        = CATPUCCIN_FRAPPE["peach"],
    state_error          = CATPUCCIN_FRAPPE["red"]
)


CATPUCCIN_LATTE = {
    "crust": "#dce0e8",
    "base": "#eff1f5",
    "surface0": "#ccd0da",
    "surface1": "#bcc0cc",
    "text": "#4c4f69",
    "subtext1": "#5c5f77",
    "subtext0": "#6c6f85",
    "overlay2": "#7c7f93",
    "red": "#d20f39",
    "maroon": "#e64553",
    "peach": "#fe640b",
    "yellow": "#df8e1d",
    "green": "#40a02b",
    "teal": "#179299",
    "sky": "#04a5e5",
    "sapphire": "#209fb5",
    "blue": "#1e66f5",
    "lavender": "#7287fd",
    "mauve": "#8839ef",
    "pink": "#ea76cb",
    "flamingo": "#dd7878",
    "rosewater": "#dc8a78"
}

SYNTAX_CATPUCCIN_LATTE = SyntaxPalette(
    identifier   = CATPUCCIN_LATTE["text"],
    operator     = CATPUCCIN_LATTE["sky"],
    brace        = CATPUCCIN_LATTE["overlay2"],
    string       = CATPUCCIN_LATTE["green"],
    comment      = CATPUCCIN_LATTE["overlay2"],
    keyword      = CATPUCCIN_LATTE["mauve"],
    numeric      = CATPUCCIN_LATTE["peach"],
    this         = CATPUCCIN_LATTE["red"],
    function     = CATPUCCIN_LATTE["blue"],
    preprocessor = CATPUCCIN_LATTE["rosewater"]
)

UI_CATPUCCIN_LATTE = UIPalette(
    is_dark              = True,
    background_primary   = CATPUCCIN_LATTE["base"],
    background_secondary = CATPUCCIN_LATTE["surface0"],
    background_tertiary  = CATPUCCIN_LATTE["surface1"],
    text_primary         = CATPUCCIN_LATTE["text"],
    text_secondary       = CATPUCCIN_LATTE["subtext1"],
    text_tertiary        = CATPUCCIN_LATTE["subtext0"],
    text_fallback        = CATPUCCIN_LATTE["crust"],
    brand_primary        = CATPUCCIN_LATTE["mauve"],
    brand_secondary      = CATPUCCIN_LATTE["maroon"],
    brand_tertiary       = CATPUCCIN_LATTE["sapphire"],
    text_selection       = CATPUCCIN_LATTE["teal"],
    state_success        = CATPUCCIN_LATTE["green"],
    state_warning        = CATPUCCIN_LATTE["peach"],
    state_error          = CATPUCCIN_LATTE["red"]
)