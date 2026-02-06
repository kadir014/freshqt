"""

    freshqt  -  A modern, refreshed take on PyQt user interfaces

    This file is a part of the freshqt
    project and distributed under MIT license.
    https://github.com/kadir014/freshqt

"""

from enum import Enum, auto

from PyQt6.QtCore import Qt, QRegularExpression, QRect
from PyQt6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QPlainTextEdit, QLabel
from PyQt6.QtGui import QColor, QSyntaxHighlighter, QPainter, QBrush, QPen, QTextDocument, QTextCharFormat

from freshqt.core.models import SyntaxPalette, SyntaxLanguage
from freshqt.core.theme import Theme, Themeable
from freshqt.palettes.dracula import SYNTAX_DRACULA
from freshqt.palettes.catpuccin import SYNTAX_CATPUCCIN_LATTE


_RULESETS = {
    SyntaxLanguage.PLAIN: {},

    SyntaxLanguage.JSON: {
        "keywords": ("null", "true", "false"),
        "braces": (
            r"\{", r"\}", r"\(", r"\)", r"\[", r"\]",
        )
    },

    SyntaxLanguage.PYTHON: {
        "this": "self",
        "comment": "#",
        "keywords": (
            "and", "assert", "break", "class", "continue", "def",
            "del", "elif", "else", "except", "exec", "finally",
            "for", "from", "global", "if", "import", "in",
            "is", "lambda", "not", "or", "pass",
            "raise", "return", "try", "while", "yield",
            "None", "True", "False"
        ),
        "operators": (
            r"=",
            r"==", r"!=", r"<", r"<=", r">", r">=",
            r"\+", r"-", r"\*", r"/", r"//", r"\%", r"\*\*",
            r"\+=", r"-=", r"\*=", r"/=", r"\%=",
            r"\^", r"\|", r"\&", r"\~", r">>", r"<<",
            r"\+\+", r"--", r"\&\&", r"\|\|"
        ),
        "braces": (
            r"\{", r"\}", r"\(", r"\)", r"\[", r"\]",
        )
    }
}


class Highlighter(QSyntaxHighlighter):
    def __init__(self,
            parent: QTextDocument | None = None,
            language: SyntaxLanguage = SyntaxLanguage.PLAIN,
            syntax_palette: SyntaxPalette = SYNTAX_CATPUCCIN_LATTE
            ) -> None:
        super().__init__(parent)

        self.__elements = {}
        self.__language = language
        self.__syntax_palette = syntax_palette
        self.__rules: list[tuple[QRegularExpression, int, QTextCharFormat]] = []

        self.load_rules()
        self.apply_rules()

    @property
    def language(self) -> SyntaxLanguage:
        return self.__language
    
    @language.setter
    def language(self, value: SyntaxLanguage) -> None:
        self.__language = value
        self.load_rules()
        self.apply_rules()

    @property
    def syntax_palette(self) -> SyntaxPalette:
        return self.__syntax_palette
    
    @syntax_palette.setter
    def syntax_palette(self, value: SyntaxPalette) -> None:
        self.__syntax_palette = value
        self.apply_rules()

    def load_rules(self) -> None:
        self.__elements = _RULESETS[self.__language]

    def apply_rules(self) -> None:
        if self.__language == SyntaxLanguage.PLAIN:
            return

        syntax_theme = dict()
        for key in self.__syntax_palette.__dataclass_fields__:
            c = QTextCharFormat()
            c.setForeground(QBrush(QColor(getattr(self.__syntax_palette, key))))
            syntax_theme[key] = c

        self.tri_single = (QRegularExpression("'''"), 1, syntax_theme["string"])
        self.tri_double = (QRegularExpression("\"\"\""), 2, syntax_theme["string"])

        rules = []

        if "keywords" in self.__elements:
            rules += [(r"\b%s\b" % w, 0, syntax_theme["keyword"]) for w in self.__elements["keywords"]]

        if "operators" in self.__elements:
            rules += [(r"%s" % o, 0, syntax_theme["operator"]) for o in self.__elements["operators"]]

        if "braces" in self.__elements:
            rules += [(r"%s" % b, 0, syntax_theme["brace"]) for b in self.__elements["braces"]]

        # if self.lang in ("cpp", "c"):
        #     rules.append( (r'\#[^\n]*', 0, self.theme["preprocessor"]) )

        rules += [(r"\b[A-Za-z0-9_]+(?=\()",  0, syntax_theme["function"])]

        if "this" in self.__elements:
            rules += [(r"\b%s\b" % self.__elements["this"], 0, syntax_theme["this"])]

        rules += [(r"\"[^\"\\]*(\\.[^\"\\]*)*\"", 0, syntax_theme["string"])]
        rules += [(r"'[^'\\]*(\\.[^'\\]*)*'", 0, syntax_theme["string"])]

        if "comment" in self.__elements:
            rules += [(r"%s[^\n]*" % self.__elements["comment"], 0, syntax_theme["comment"])]

        rules += [(r"\b[+-]?[0-9]+[lL]?\b", 0, syntax_theme["numeric"])]
        rules += [(r"\b[+-]?0[xX][0-9A-Fa-f]+[lL]?\b", 0, syntax_theme["numeric"])]
        rules += [(r"\b[+-]?[0-9]+(?:\.[0-9]+)?(?:[eE][+-]?[0-9]+)?\b", 0, syntax_theme["numeric"])]

        self.__rules = [(QRegularExpression(pat), index, fmt) for (pat, index, fmt) in rules]

    def highlightBlock(self, text: str) -> None:
        if self.__language == SyntaxLanguage.PLAIN:
            return

        for expression, nth, format in self.__rules:
            it = expression.globalMatch(text)

            while it.hasNext():
                match = it.next()
                start = match.capturedStart(nth)
                length = match.capturedLength(nth)

                if start >= 0:
                    self.setFormat(start, length, format)

        self.setCurrentBlockState(0)

        in_multiline = self.match_multiline(text, *self.tri_single)
        if not in_multiline:
            in_multiline = self.match_multiline(text, *self.tri_double)

    def match_multiline(self,
            text: str,
            delimiter: QRegularExpression,
            in_state: int,
            style: str
            ) -> None:
        if self.__language == SyntaxLanguage.PLAIN:
            return

        if self.previousBlockState() == in_state:
            start = 0
            add = 0

        else:
            m = delimiter.match(text)
            start = m.capturedStart()
            add = m.capturedLength()

        while start >= 0:
            m2 = delimiter.match(text, start + add)
            end = m2.capturedStart()

            if end >= 0:
                length = end - start + m2.capturedLength() + add
                self.setCurrentBlockState(0)

            else:
                self.setCurrentBlockState(in_state)
                length = len(text) - start + add

            self.setFormat(start, length, style)

            m3 = delimiter.match(text, start + length)
            start = m3.capturedStart()
            add = m3.capturedLength()

        return self.currentBlockState() == in_state


class Code(QWidget, Themeable):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)

        lyt = QHBoxLayout()
        lyt.setContentsMargins(0, 0, 0, 0)
        self.setLayout(lyt)

        # TODO: Make these properties
        self.line_col_width = 37
        self.line_no_alignment = Qt.AlignmentFlag.AlignRight
        lyt.addSpacing(self.line_col_width)

        self.__editor_lyt = QVBoxLayout()
        self.__editor_lyt.setSpacing(0)
        self.__editor_lyt.setContentsMargins(0, 0, 0, 0)
        lyt.addLayout(self.__editor_lyt)

        self.__editor = QPlainTextEdit()
        self.__editor.setLineWrapMode(QPlainTextEdit.LineWrapMode.NoWrap)
        self.__editor_lyt.addWidget(self.__editor)

        self.__highlighter = Highlighter(self.__editor.document())

        self.__statusbar = QWidget()
        self.__statusbar.setFixedHeight(26)
        self.__statusbarlyt = QHBoxLayout()
        self.__statusbarlyt.setContentsMargins(10, 0, 30, 0)
        self.__statusbar.setLayout(self.__statusbarlyt)
        self.__editor_lyt.addWidget(self.__statusbar)

        self.__cursor_lbl = QLabel("0:0")
        self.__statusbarlyt.addWidget(self.__cursor_lbl, alignment=Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)

        self.__lang_lbl = QLabel(self.__highlighter.language.name.lower().capitalize())
        self.__statusbarlyt.addWidget(self.__lang_lbl, alignment=Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)

        self.__editor.cursorPositionChanged.connect(self.__editor_cursor_position_changed)

        self.__theme: Theme | None = None

    @property
    def text(self) -> str:
        """ Plain text content of the editor. """
        return self.__editor.toPlainText()
    
    @text.setter
    def text(self, value: str) -> None:
        self.__editor.setPlainText(value)

    @property
    def language(self) -> SyntaxLanguage:
        """ Language of the syntax highlighter. """
        return self.__highlighter.language
    
    @language.setter
    def language(self, value: SyntaxLanguage) -> None:
        self.__highlighter.language = value
        self.__lang_lbl.setText(self.__highlighter.language.name.lower().capitalize())

        # Update rich text engine
        self.text = self.text

    @property
    def syntax_palette(self) -> SyntaxPalette:
        """ Color palette of the syntax highlighter. """
        return self.__highlighter.syntax_palette
    
    @syntax_palette.setter
    def syntax_palette(self, value: SyntaxPalette) -> None:
        self.__highlighter.syntax_palette = value

        # Update rich text engine
        self.text = self.text

    def update_theme(self, theme: Theme) -> None:
        self.__theme = theme

        font_size = int(round(14.0 * theme.font_scale))
        if font_size <= 0:
            font_size = 1

        border_color = theme.qss(theme.palette.text_tertiary)

        self.__statusbar.setStyleSheet("background-color: transparent;")

        self.setStyleSheet(f"""
            QPlainTextEdit {{
                font-family: "Cascadia Code";
                font-size: {font_size}px;
                color: {theme.qss(theme.palette.text_primary)};
                selection-background-color: {theme.qss(theme.palette.text_selection)};
                background-color: {theme.qss(theme.palette.background_primary)};
                border-top: 1px solid {border_color};
                border-right: 1px solid {border_color};
                border-top-right-radius: 7px;
                border-bottom: 1px solid {border_color};
                border-bottom-right-radius: 7px;
            }}

            QLabel {{
                font-family: "Cascadia Code";
                font-size: {font_size}px;
                color: {border_color};
            }}
        """)

    def __editor_cursor_position_changed(self) -> None:
        pos_str = f"{self.__editor.textCursor().blockNumber()}:{self.__editor.textCursor().positionInBlock()}"
        self.__cursor_lbl.setText(pos_str)

    def paintEvent(self, e) -> None:
        if self.__theme is None: return

        pt = QPainter(self)
        pt.setRenderHint(QPainter.RenderHint.Antialiasing, on=True)

        outline_pen = QPen(self.__theme.qcolor(self.__theme.palette.text_tertiary))
        # TODO: need testing, 1.5 works as close as to native Qt rendering
        outline_pen.setWidthF(1.5)

        slider_value = self.__editor.verticalScrollBar().value()

        pt.setPen(outline_pen)
        pt.setBrush(QBrush(self.__theme.qcolor(self.__theme.palette.background_secondary)))
        pt.drawRoundedRect(0, 0, self.width(), self.height(), 7, 7)

        pt.setBrush(QBrush())

        font = self.__editor.font()
        pt.setFont(font)
        pt.setPen(outline_pen)

        gap = font.pixelSize() + 3
        for i in range(self.height() // gap + 2):
            line_no = i + slider_value
            digits = len(str(line_no)) - 1
            y = i * gap + 6

            col_margin = 5
            pt.drawText(
                QRect(0, y, self.line_col_width - col_margin, 50),
                self.line_no_alignment,
                str(line_no)
            )