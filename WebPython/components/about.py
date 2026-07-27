import reflex as rx

from WebPython.components.ui import COLORS, section_heading
from WebPython.data import PROFILE


def about() -> rx.Component:
    return rx.vstack(
        rx.vstack(
            section_heading("Sobre mí"),
            rx.grid(
                rx.text(
                    PROFILE["summary"],
                    color=COLORS["text"],
                    font_size="17px",
                    font_weight="300",
                    line_height="1.75",
                ),
                rx.text(
                    "Trabajo con APIs, interfaces modernas y buenas prácticas de "
                    "desarrollo. Me interesa transformar necesidades reales en "
                    "productos mantenibles y fáciles de usar.",
                    color=COLORS["muted"],
                    font_size="15px",
                    font_weight="300",
                    line_height="1.75",
                ),
                columns=rx.breakpoints(initial="1", md="2"),
                spacing="9",
                width="100%",
            ),
            spacing="7",
            width="100%",
            max_width="980px",
            margin="0 auto",
            padding=rx.breakpoints(initial="4.5rem 1.5rem", sm="5.5rem 2.5rem"),
            id="sobre-mi",
        ),
        border_top=f"1px solid {COLORS['line']}",
        width="100%",
    )
