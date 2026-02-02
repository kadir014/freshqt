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

from freshqt.core.models import SyntaxPalette
from freshqt.core.theme import Theme, Themeable
from freshqt.palettes.dracula import SYNTAX_DRACULA


class HighlighterLanguage(Enum):
    PLAIN = auto()
    PYTHON = auto()


class Highlighter(QSyntaxHighlighter):
    def __init__(self,
            parent: QTextDocument | None = None,
            language: HighlighterLanguage = HighlighterLanguage.PYTHON,
            syntax_palette: SyntaxPalette = SYNTAX_DRACULA
            ) -> None:
        super().__init__(parent)

        self.set_language(language)

        self.syntax_palette = syntax_palette
        self.set_rules()

    @property
    def language(self) -> HighlighterLanguage:
        return self.__language

    def set_language(self, language: HighlighterLanguage) -> None:
        self.__language = language

        self.__elements = {
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

    def set_rules(self) -> None:
        if self.__language == "Plain":
            return

        syntax_theme = dict()
        for key in self.syntax_palette.__dataclass_fields__:
            c = QTextCharFormat()
            c.setForeground(QBrush(QColor(getattr(self.syntax_palette, key))))
            syntax_theme[key] = c

        self.tri_single = (QRegularExpression("'''"), 1, syntax_theme["string"])
        self.tri_double = (QRegularExpression("\"\"\""), 2, syntax_theme["string"])

        rules = []

        rules += [(r"\b%s\b" % w, 0, syntax_theme["keyword"]) for w in self.__elements["keywords"]]

        rules += [(r"%s" % o, 0, syntax_theme["operator"]) for o in self.__elements["operators"]]

        rules += [(r"%s" % b, 0, syntax_theme["brace"]) for b in self.__elements["braces"]]

        # if self.lang in ("cpp", "c"):
        #     rules.append( (r'\#[^\n]*', 0, self.theme["preprocessor"]) )

        rules += [
            (r"\b[A-Za-z0-9_]+(?=\()",  0, syntax_theme["function"]),

            (r"\b%s\b" % self.__elements["this"], 0, syntax_theme["this"]),

            (r"\"[^\"\\]*(\\.[^\"\\]*)*\"", 0, syntax_theme["string"]),

            (r"'[^'\\]*(\\.[^'\\]*)*'", 0, syntax_theme["string"]),

            (r"%s[^\n]*" % self.__elements["comment"], 0, syntax_theme["comment"]),

            (r"\b[+-]?[0-9]+[lL]?\b", 0, syntax_theme["numeric"]),
            (r"\b[+-]?0[xX][0-9A-Fa-f]+[lL]?\b", 0, syntax_theme["numeric"]),
            (r"\b[+-]?[0-9]+(?:\.[0-9]+)?(?:[eE][+-]?[0-9]+)?\b", 0, syntax_theme["numeric"])
        ]

        self.rules = [(QRegularExpression(pat), index, fmt) for (pat, index, fmt) in rules]

    def highlightBlock(self, text: str) -> None:
        if self.__language == HighlighterLanguage.PLAIN:
            return

        for expression, nth, format in self.rules:
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
        if self.__language == HighlighterLanguage.PLAIN:
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

        self.editor_lyt = QVBoxLayout()
        self.editor_lyt.setSpacing(0)
        self.editor_lyt.setContentsMargins(0, 0, 0, 0)
        lyt.addLayout(self.editor_lyt)

        self.editor = QPlainTextEdit()
        self.editor.setLineWrapMode(QPlainTextEdit.LineWrapMode.NoWrap)
        self.editor_lyt.addWidget(self.editor)

        self.highlighter = Highlighter(self.editor.document())

        self.statusbar = QWidget()
        self.statusbar.setFixedHeight(26)
        self.statusbarlyt = QHBoxLayout()
        self.statusbarlyt.setContentsMargins(10, 0, 30, 0)
        self.statusbar.setLayout(self.statusbarlyt)
        self.editor_lyt.addWidget(self.statusbar)

        self.cursor_lbl = QLabel("0:0")
        self.cursor_lbl.setStyleSheet("font-size: 14px;")
        self.statusbarlyt.addWidget(self.cursor_lbl, alignment=Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)

        self.lang_lbl = QLabel(self.highlighter.language.name.lower().capitalize())
        self.lang_lbl.setStyleSheet("font-size: 14px;")
        self.statusbarlyt.addWidget(self.lang_lbl, alignment=Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)

        self.statusbar.hide()

        self.editor.cursorPositionChanged.connect(self._editor_cursor_position_changed)

        self.__theme: Theme = None

    def update_theme(self, theme: Theme) -> None:
        self.__theme = theme

        border_color = theme.qss(theme.palette.text_tertiary)

        self.statusbar.setStyleSheet("background-color: transparent;")

        self.setStyleSheet(f"""
            QPlainTextEdit {{
                font-family: "Cascadia Code";
                font-size: 14px;
                color: {theme.qss(theme.palette.text_primary)};
                background-color: {theme.qss(theme.palette.background_primary)};
                border-top: 1px solid {border_color};
                border-right: 1px solid {border_color};
                border-top-right-radius: 7px;
                border-bottom: 1px solid {border_color};
                border-bottom-right-radius: 7px;
            }}

            QLabel {{
                font-family: "Cascadia Code";
                font-size: 14px;
                color: {border_color};
            }}
        """)

    def _editor_cursor_position_changed(self) -> None:
        pos_str = f"{self.editor.textCursor().blockNumber()}:{self.editor.textCursor().positionInBlock()}"
        self.cursor_lbl.setText(pos_str)

    def paintEvent(self, e) -> None:
        if self.__theme is None:
            # TODO: warning
            return

        pt = QPainter(self)
        pt.setRenderHint(QPainter.RenderHint.Antialiasing, on=True)

        outline_pen = QPen(self.__theme.qcolor(self.__theme.palette.text_tertiary))
        # TODO: need testing, 1.5 works as close as to native Qt rendering
        outline_pen.setWidthF(1.5)

        slider_value = self.editor.verticalScrollBar().value()

        pt.setPen(outline_pen)
        pt.setBrush(QBrush(self.__theme.qcolor(self.__theme.palette.background_secondary)))
        pt.drawRoundedRect(0, 0, self.width(), self.height(), 7, 7)

        pt.setBrush(QBrush())

        font = self.editor.font()
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