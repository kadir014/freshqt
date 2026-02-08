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


CATPPUCCIN_LATTE = {
    "crust": "#dce0e8",
    "mantle": "#e6e9ef",
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

SYNTAX_CATPPUCCIN_LATTE = SyntaxPalette(
    identifier   = CATPPUCCIN_LATTE["text"],
    operator     = CATPPUCCIN_LATTE["sky"],
    brace        = CATPPUCCIN_LATTE["overlay2"],
    string       = CATPPUCCIN_LATTE["green"],
    comment      = CATPPUCCIN_LATTE["overlay2"],
    keyword      = CATPPUCCIN_LATTE["mauve"],
    numeric      = CATPPUCCIN_LATTE["peach"],
    this         = CATPPUCCIN_LATTE["red"],
    function     = CATPPUCCIN_LATTE["blue"],
    preprocessor = CATPPUCCIN_LATTE["rosewater"]
)

UI_CATPPUCCIN_LATTE = UIPalette(
    name                 = "Catppuccin Latte",
    is_dark              = False,
    background_primary   = CATPPUCCIN_LATTE["base"],
    background_secondary = CATPPUCCIN_LATTE["mantle"],
    background_tertiary  = CATPPUCCIN_LATTE["crust"],
    text_primary         = CATPPUCCIN_LATTE["text"],
    text_secondary       = CATPPUCCIN_LATTE["subtext1"],
    text_tertiary        = CATPPUCCIN_LATTE["subtext0"],
    text_fallback        = CATPPUCCIN_LATTE["crust"],
    brand_primary        = CATPPUCCIN_LATTE["mauve"],
    brand_secondary      = CATPPUCCIN_LATTE["maroon"],
    brand_tertiary       = CATPPUCCIN_LATTE["sapphire"],
    text_selection       = CATPPUCCIN_LATTE["teal"],
    state_success        = CATPPUCCIN_LATTE["green"],
    state_warning        = CATPPUCCIN_LATTE["peach"],
    state_error          = CATPPUCCIN_LATTE["red"]
)


CATPPUCCIN_FRAPPE = {
    "crust": "#232634",
    "mantle": "#292c3c",
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

SYNTAX_CATPPUCCIN_FRAPPE = SyntaxPalette(
    identifier   = CATPPUCCIN_FRAPPE["text"],
    operator     = CATPPUCCIN_FRAPPE["sky"],
    brace        = CATPPUCCIN_FRAPPE["overlay2"],
    string       = CATPPUCCIN_FRAPPE["green"],
    comment      = CATPPUCCIN_FRAPPE["overlay2"],
    keyword      = CATPPUCCIN_FRAPPE["mauve"],
    numeric      = CATPPUCCIN_FRAPPE["peach"],
    this         = CATPPUCCIN_FRAPPE["red"],
    function     = CATPPUCCIN_FRAPPE["blue"],
    preprocessor = CATPPUCCIN_FRAPPE["rosewater"]
)

UI_CATPPUCCIN_FRAPPE = UIPalette(
    name                 = "Catppuccin Frappé",
    is_dark              = True,
    background_primary   = CATPPUCCIN_FRAPPE["base"],
    background_secondary = CATPPUCCIN_FRAPPE["mantle"],
    background_tertiary  = CATPPUCCIN_FRAPPE["crust"],
    text_primary         = CATPPUCCIN_FRAPPE["text"],
    text_secondary       = CATPPUCCIN_FRAPPE["subtext1"],
    text_tertiary        = CATPPUCCIN_FRAPPE["subtext0"],
    text_fallback        = CATPPUCCIN_FRAPPE["crust"],
    brand_primary        = CATPPUCCIN_FRAPPE["mauve"],
    brand_secondary      = CATPPUCCIN_FRAPPE["maroon"],
    brand_tertiary       = CATPPUCCIN_FRAPPE["sapphire"],
    text_selection       = CATPPUCCIN_FRAPPE["teal"],
    state_success        = CATPPUCCIN_FRAPPE["green"],
    state_warning        = CATPPUCCIN_FRAPPE["peach"],
    state_error          = CATPPUCCIN_FRAPPE["red"]
)


CATPPUCCIN_MOCHA = {
    "crust": "#11111b",
    "mantle": "#181825",
    "base": "#1e1e2e",
    "surface0": "#313244",
    "surface1": "#45475a",
    "text": "#cdd6f4",
    "subtext1": "#bac2de",
    "subtext0": "#a6adc8",
    "overlay2": "#9399b2",
    "red": "#f38ba8",
    "maroon": "#eba0ac",
    "peach": "#fab387",
    "yellow": "#f9e2af",
    "green": "#a6e3a1",
    "teal": "#94e2d5",
    "sky": "#89dceb",
    "sapphire": "#74c7ec",
    "blue": "#89b4fa",
    "lavender": "#b4befe",
    "mauve": "#cba6f7",
    "pink": "#f5c2e7",
    "flamingo": "#f2cdcd",
    "rosewater": "#f5e0dc"
}

SYNTAX_CATPPUCCIN_MOCHA = SyntaxPalette(
    identifier   = CATPPUCCIN_MOCHA["text"],
    operator     = CATPPUCCIN_MOCHA["sky"],
    brace        = CATPPUCCIN_MOCHA["overlay2"],
    string       = CATPPUCCIN_MOCHA["green"],
    comment      = CATPPUCCIN_MOCHA["overlay2"],
    keyword      = CATPPUCCIN_MOCHA["mauve"],
    numeric      = CATPPUCCIN_MOCHA["peach"],
    this         = CATPPUCCIN_MOCHA["red"],
    function     = CATPPUCCIN_MOCHA["blue"],
    preprocessor = CATPPUCCIN_MOCHA["rosewater"]
)

UI_CATPPUCCIN_MOCHA = UIPalette(
    name                 = "Catppuccin Mocha",
    is_dark              = True,
    background_primary   = CATPPUCCIN_MOCHA["base"],
    background_secondary = CATPPUCCIN_MOCHA["mantle"],
    background_tertiary  = CATPPUCCIN_MOCHA["crust"],
    text_primary         = CATPPUCCIN_MOCHA["text"],
    text_secondary       = CATPPUCCIN_MOCHA["subtext1"],
    text_tertiary        = CATPPUCCIN_MOCHA["subtext0"],
    text_fallback        = CATPPUCCIN_MOCHA["crust"],
    brand_primary        = CATPPUCCIN_MOCHA["mauve"],
    brand_secondary      = CATPPUCCIN_MOCHA["maroon"],
    brand_tertiary       = CATPPUCCIN_MOCHA["sapphire"],
    text_selection       = CATPPUCCIN_MOCHA["teal"],
    state_success        = CATPPUCCIN_MOCHA["green"],
    state_warning        = CATPPUCCIN_MOCHA["peach"],
    state_error          = CATPPUCCIN_MOCHA["red"]
)