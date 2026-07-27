import reflex as rx

from WebPython.components.ui import COLORS


NAV_ITEMS = [("Sobre mí", "#sobre-mi"), ("Tecnologías", "#skills"), ("Proyectos", "#proyectos"), ("Contacto", "#contacto")]


def navbar() -> rx.Component:
    return rx.hstack(
        rx.link(
            "MC.",
            href="#inicio",
            color=COLORS["accent"],
            font_family="'Playfair Display', serif",
            font_size="20px",
            font_weight="700",
            text_decoration="none",
            flex_shrink="0",
        ),
        rx.spacer(),
        rx.hstack(
            *[
                rx.link(
                    label,
                    href=target,
                    color=COLORS["muted"],
                    font_size="11px",
                    letter_spacing="0.08em",
                    text_transform="uppercase",
                    white_space="nowrap",
                    _hover={"color": COLORS["accent"]},
                    _focus_visible={"outline": f"2px solid {COLORS['accent']}", "outline_offset": "4px"},
                    text_decoration="none",
                )
                for label, target in NAV_ITEMS
            ],
            spacing=rx.breakpoints(initial="3", sm="6"),
            overflow_x="auto",
            max_width="80%",
        ),
        width="100%",
        padding=rx.breakpoints(initial="1rem 1.5rem", sm="1.25rem 2.5rem"),
        border_bottom=f"1px solid {COLORS['line']}",
        background="rgba(10, 13, 20, 0.86)",
        position="sticky",
        top="0",
        z_index="10",
        backdrop_filter="blur(14px)",
    )
