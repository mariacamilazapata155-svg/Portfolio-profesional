"""Primitivas visuales reutilizables para mantener el diseño consistente."""

import reflex as rx

COLORS = {
    "background": "#0a0d14",
    "surface": "#111520",
    "text": "#f1ede5",
    "muted": "#9aa4b5",
    "accent": "#d6c29d",
    "line": "rgba(255, 255, 255, 0.12)",
    "blue": "#77b7ff",
}


def section_heading(label: str) -> rx.Component:
    return rx.hstack(
        rx.text(
            label,
            font_size="10px",
            letter_spacing="0.2em",
            text_transform="uppercase",
            color=COLORS["accent"],
            font_weight="600",
        ),
        rx.divider(flex="1", border_color=COLORS["line"]),
        width="100%",
        align="center",
        spacing="3",
    )


def primary_button(label: str) -> rx.Component:
    return rx.button(
        label,
        background=COLORS["accent"],
        color=COLORS["background"],
        border="1px solid transparent",
        border_radius="6px",
        padding="10px 18px",
        font_size="13px",
        font_weight="600",
        cursor="pointer",
        _hover={"background": "#ead7b2", "transform": "translateY(-1px)"},
        transition="all 160ms ease",
    )


def secondary_button(label: str) -> rx.Component:
    return rx.button(
        label,
        background="transparent",
        color=COLORS["text"],
        border=f"1px solid {COLORS['line']}",
        border_radius="6px",
        padding="10px 18px",
        font_size="13px",
        font_weight="500",
        cursor="pointer",
        _hover={"border_color": COLORS["accent"], "color": COLORS["accent"]},
        transition="all 160ms ease",
    )
