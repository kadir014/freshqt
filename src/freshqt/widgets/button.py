"""

    freshqt  -  A modern, refreshed take on PyQt user interfaces

    This file is a part of the freshqt
    project and distributed under MIT license.
    https://github.com/kadir014/freshqt

"""

from enum import Enum, auto

from PyQt6.QtCore import Qt, QRectF
from PyQt6.QtWidgets import QWidget, QAbstractButton
from PyQt6.QtGui import QPainter, QIcon, QColor, QPainterPath, QFont, QPen

from freshqt.core.typing import ColorLike
from freshqt.core.theme import Theme, Themeable
from freshqt.core.models import TypographyType
from freshqt.animation import Tween, Easing
from freshqt.core.color import WCAG, WCAG_NORMAL_TEXT


class Button(QAbstractButton, Themeable):
    """
    Themeable push button widget.
    """

    class Variant(Enum):
        """
        Button variant.
        """
        BRAND = auto()
        SECONDARY = auto()
        OUTLINE = auto()
        GHOST = auto()

    def __init__(self,
            text: str = "",
            type: TypographyType = TypographyType.BODY,
            icon_name: str = "",
            variant: Variant = Variant.BRAND,
            parent: QWidget | None = None
            ) -> None:
        """
        Parameters
        ----------
        text
            Text content of the button
        type
            Typographic type of the text content
        icon_name
            Themed icon displayed with text content
            The regular icon set with setIcon has priority
        variant
            Button variant
        parent
            Parent widget
        """
        super().__init__(parent=parent)

        self.__text = text
        self.__text_alignment = Qt.AlignmentFlag.AlignCenter
        self.__type = type
        self.__icon_name = icon_name
        self.__variant = variant

        self.__background_color: ColorLike | None = None

        self._reset_tween()

        self.__mouse_effect_dark = False
        self.__hover_percent = 0.1
        self.__press_percent = 0.2

        self.__border_width = 1.5
        self.__border_radius = 7.0

        self.setCursor(Qt.CursorShape.PointingHandCursor)

        self.setMinimumSize(16, 16)

        self.__theme: Theme | None = None

    def _reset_tween(self) -> None:
        self.__hover_tween = Tween(
            start_value=0.0,
            end_value=1.0,
            value=0.0
        )

        self.__press_tween = Tween(
            start_value=0.0,
            end_value=1.0,
            value=0.0
        )

    @property
    def text(self) -> str:
        """ Text content of the button. """
        return self.__text
    
    @text.setter
    def text(self, value: str) -> None:
        self.__text = value
        self.update()

    @property
    def text_alignment(self) -> Qt.AlignmentFlag:
        """ Alignment of the text content of the button. """
        return self.__text_alignment
    
    @text_alignment.setter
    def text_alignment(self, value: Qt.AlignmentFlag) -> None:
        self.__text_alignment = value
        self.update()

    @property
    def type(self) -> TypographyType:
        """ Typography type of the label. """
        return self.__type
    
    @type.setter
    def type(self, value: TypographyType) -> None:
        self.__type = value
        if self.__theme is not None:
            self.update_theme(self.__theme)
            self.update_theme_role(self.__theme)
        self.update()

    @property
    def icon_name(self) -> str:
        """ Themed icon name. """
        return self.__icon_name
    
    @icon_name.setter
    def icon_name(self, value: str) -> None:
        self.__icon_name = value
        self.update()

    @property
    def border_radius(self) -> float:
        """ Border radius. If negative, completely round. """
        return self.__border_radius
    
    @border_radius.setter
    def border_radius(self, value: float) -> None:
        self.__border_radius = value
        self.update()

    @property
    def variant(self) -> Variant:
        """ Button variant. """
        return self.__variant
    
    @variant.setter
    def variant(self, value: Variant) -> None:
        self.__variant = value
        self.update()

    @property
    def background_color(self) -> ColorLike | None:
        """ Background color. Uses the variant background if None. """
        return self.__background_color
    
    @background_color.setter
    def background_color(self, value: ColorLike | None):
        self.__background_color = value
        self.update()

    def update_theme(self, theme: Theme) -> None:
        self.__theme = theme
        self.__mouse_effect_dark = not theme.palette.is_dark

    def enterEvent(self, e) -> None:
        super().enterEvent(e)
        self.__hover_tween.play(0.12, easing=Easing.EASE_IN_SINE)
        self.update()

    def leaveEvent(self, e) -> None:
        super().leaveEvent(e)
        self.__hover_tween.play(0.12, easing=Easing.EASE_IN_SINE, reverse=True)
        self.update()

    def mousePressEvent(self, e) -> None:
        super().mousePressEvent(e)
        self.__press_tween.play(0.1, easing=Easing.EASE_IN_SINE)
        self.update()

    def mouseReleaseEvent(self, e) -> None:
        super().mouseReleaseEvent(e)
        self.__press_tween.play(0.1, easing=Easing.EASE_IN_SINE, reverse=True)
        self.update()

    def showEvent(self, e) -> None:
        super().showEvent(e)
        self._reset_tween()
        self.update()

    def hideEvent(self, e) -> None:
        super().hideEvent(e)
        self._reset_tween()
        self.update()

    def update(self) -> None:
        self.__hover_tween.update()
        self.__press_tween.update()
        super().update()

    def paintEvent(self, e) -> None:
        if self.__theme is None: return

        dpi = self.devicePixelRatioF()

        pt = QPainter(self)
        pt.setRenderHint(QPainter.RenderHint.Antialiasing, on=True)

        w, h = self.width(), self.height()
        main_axis = min(w, h)

        border_r = self.__border_radius
        if border_r < 0:
            border_r = main_axis * 0.5

        # Predefined button variants
        if self.__variant == Button.Variant.BRAND:
            bg_color = self.__theme.qcolor(self.__theme.palette.brand_primary)
            text_color = self.__theme.qcolor(self.__theme.palette.text_primary)
            border_color = QColor(0, 0, 0, 0)

        elif self.__variant == Button.Variant.SECONDARY:
            bg_color = self.__theme.qcolor(self.__theme.palette.background_secondary)
            text_color = self.__theme.qcolor(self.__theme.palette.text_primary)
            border_color = QColor(0, 0, 0, 0)

        elif self.__variant == Button.Variant.OUTLINE:
            bg_color = self.__theme.qcolor(self.__theme.palette.background_secondary)
            text_color = self.__theme.qcolor(self.__theme.palette.text_primary)
            border_color = self.__theme.qcolor(self.__theme.palette.text_tertiary)

        elif self.__variant == Button.Variant.GHOST:
            bg_color = self.__theme.qcolor(self.__theme.palette.background_primary)
            bg_color.setAlpha(0)
            text_color = self.__theme.qcolor(self.__theme.palette.text_primary)
            border_color = QColor(0, 0, 0, 0)

        # If background option is given, use it instead of button variant
        if self.__background_color is not None:
            if isinstance(self.__background_color, str) and hasattr(self.__theme.palette, self.__background_color):
                bg_color = self.__theme.qcolor(getattr(self.__theme.palette, self.background_color))

            else:
                bg_color = self.__theme.qcolor(self.__background_color)

        # Test for WCAG contrast ratio
        if WCAG(text_color, bg_color) < WCAG_NORMAL_TEXT:
            text_color = self.__theme.qcolor(self.__theme.palette.text_fallback)

        # Hover & pressed mouse effect colors
        hover_alpha = int(self.__hover_tween.value * 255.0 * self.__hover_percent)
        if self.__mouse_effect_dark:
            hover_color = QColor(0, 0, 0, hover_alpha)
        else:
            hover_color = QColor(255, 255, 255, hover_alpha)

        press_alpha = int(self.__press_tween.value * 255.0 * self.__press_percent)
        if self.__mouse_effect_dark:
            press_color = QColor(0, 0, 0, press_alpha)
        else:
            press_color = QColor(255, 255, 255, press_alpha)

        # Draw button background
        clippath = QPainterPath()
        clippath.addRoundedRect(0, 0, w, h, border_r, border_r)
        pt.setClipPath(clippath)

        pt.fillRect(0, 0, w, h, bg_color)
        pt.fillRect(0, 0, w, h, hover_color)
        pt.fillRect(0, 0, w, h, press_color)

        # Draw button borders
        p = QPen(border_color, self.__border_width)
        pt.setPen(p)
        pt.drawRoundedRect(
            QRectF(0.0, 0.0, w, h),
            border_r, border_r
        )

        # Try to load regular icon, try icon manager if it fails
        icon = self.icon()
        if icon.isNull() and len(self.__icon_name) > 0:
            icon = self.__theme.icons.get(self.__icon_name, text_color)

        icon_size = self.iconSize()
        
        diff = main_axis - icon_size.width()
        if diff < 0: diff = 0

        diff_h = int(round(diff * 0.5))

        # Render text
        font_size = int(round(self.__theme.get_typo_size(self.__type) * self.__theme.font_scale))
        if font_size <= 0:
            font_size = 1

        f = QFont()
        f.setFamily(self.__theme.font_family)
        f.setPixelSize(font_size)
        pt.setFont(f)

        # Expand minimum size according to content
        # TODO: They don't resize down
        bounding = pt.fontMetrics().boundingRect(self.__text)

        padding_w = 8
        expand_w = bounding.width() + icon_size.width() + (padding_w * 3)
        expand_h = bounding.height() + icon_size.height()

        if expand_w > self.width() and expand_w < self.maximumWidth():
            self.setMinimumWidth(expand_w)

        if expand_h > self.height() and expand_h < self.maximumHeight():
            self.setMinimumHeight(expand_h)

        # Push the text content if there is an icon
        text_padding = 0
        if not icon.isNull():
            text_padding = main_axis - diff

            # Increase text padding if text is not center aligned so they don't touch each other
            # TODO: Handle other alignments and better padding calculation
            if self.__text_alignment & Qt.AlignmentFlag.AlignLeft:
                text_padding += padding_w * 2

        # TODO: Other alignmenst & proper content margins
        if text_padding == 0 and self.text_alignment & Qt.AlignmentFlag.AlignLeft:
            text_padding = padding_w

        pt.setPen(QPen(text_color))
        pt.drawText(QRectF(text_padding, 0, w - text_padding, h), self.__text_alignment, self.__text)

        if not icon.isNull():
            # If there is no text content, center the icon
            if len(self.__text) == 0:
                padding_w = diff_h

            icon_w = main_axis - diff
            icon_h = main_axis - diff

            icon_w = int(icon_w * dpi)
            icon_h = int(icon_h * dpi)

            icon.paint(
                pt,
                padding_w, diff_h,
                icon_w, icon_h,
                alignment=Qt.AlignmentFlag.AlignLeft
            )

        # Force repaint & update if animation is not done
        if self.__hover_tween.is_started or self.__press_tween.is_started:
            self.update()