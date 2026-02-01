from dataclasses import dataclass


@dataclass
class BasePalette:
    """
    Terminal color palettes for syntax highlighting.
    """

    background: str
    foreground: str
    selection: str
    comment: str
    red: str
    orange: str
    yellow: str
    green: str
    cyan: str
    purple: str
    pink: str

@dataclass
class SyntaxPalette:
    """
    Colors for each syntactic element of a language.
    """

    identifier: str
    operator: str
    brace: str
    string: str
    comment: str
    keyword: str
    numeric: str
    this: str
    function: str
    preprocessor: str


# https://draculatheme.com/
DRACULA = BasePalette(
    background = "#282A36",
    foreground = "#F8F8F2",
    selection = "#44475A",
    comment = "#6272A4",
    red = "#FF5555",
    orange = "#FFB86C",
    yellow = "#F1FA8C",
    green = "#50FA7B",
    cyan = "#8BE9FD",
    purple = "#BD93F9",
    pink = "#FF79C6"
)

DRACULA_SYNTAX = SyntaxPalette(
    identifier = DRACULA.foreground,
    operator = DRACULA.orange,
    brace = DRACULA.comment,
    string = DRACULA.green,
    comment = DRACULA.comment,
    keyword = DRACULA.pink,
    numeric = DRACULA.cyan,
    this = DRACULA.red,
    function = DRACULA.purple,
    preprocessor = DRACULA.purple
)