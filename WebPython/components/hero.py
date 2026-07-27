import reflex as rx

from WebPython.components.ui import COLORS, primary_button, secondary_button
from WebPython.data import PROFILE


def hero() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.box(width="28px", height="1px", background=COLORS["accent"]),
            rx.text(
                PROFILE["role"],
                font_size="11px",
                letter_spacing="0.18em",
                text_transform="uppercase",
                color=COLORS["accent"],
                font_weight="600",
            ),
            align="center",
            spacing="3",
        ),
        rx.heading(
            "María ",
            rx.text.span("Camila", color=COLORS["accent"], font_style="italic"),
            font_family="'Playfair Display', serif",
            font_size="clamp(3.2rem, 8vw, 5.6rem)",
            font_weight="700",
            line_height="1",
            letter_spacing="-0.035em",
            color=COLORS["text"],
            text_align="center",
        ),
        rx.text(
            PROFILE["headline"],
            color=COLORS["muted"],
            font_size=rx.breakpoints(initial="16px", sm="18px"),
            font_weight="300",
            text_align="center",
            max_width="560px",
            line_height="1.6",
        ),
        rx.hstack(
            rx.box(width="7px", height="7px", border_radius="50%", background="#4ade80"),
            rx.text("Disponible para nuevas oportunidades", color=COLORS["muted"], font_size="12px"),
            align="center",
            spacing="2",
            padding="6px 10px",
            border=f"1px solid {COLORS['line']}",
            border_radius="999px",
        ),
        rx.hstack(
            rx.link(primary_button("Ver proyectos"), href="#proyectos", text_decoration="none"),
            rx.link(secondary_button("LinkedIn ↗"), href=PROFILE["linkedin"], is_external=True, text_decoration="none"),
            spacing="3",
            wrap="wrap",
            justify="center",
        ),
        spacing="6",
        align="center",
        padding=rx.breakpoints(initial="5.5rem 1.5rem 4.5rem", sm="7.5rem 2.5rem 6.5rem"),
        width="100%",
        max_width="980px",
        margin="0 auto",
    )
