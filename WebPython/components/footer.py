import reflex as rx

from WebPython.components.ui import COLORS, primary_button, secondary_button
from WebPython.data import PROFILE


def footer() -> rx.Component:
    return rx.vstack(
        rx.vstack(
            rx.text("Contacto", color=COLORS["accent"], font_size="10px", font_weight="600", letter_spacing="0.2em", text_transform="uppercase"),
            rx.heading("¿Hablamos?", font_family="'Playfair Display', serif", font_size=rx.breakpoints(initial="2.2rem", sm="3rem"), color=COLORS["text"], text_align="center"),
            rx.text("Estoy abierta a oportunidades, colaboraciones y proyectos interesantes.", color=COLORS["muted"], font_size="15px", font_weight="300", text_align="center", max_width="500px", line_height="1.6"),
            rx.hstack(
                rx.link(primary_button("Enviar mensaje"), href=f"mailto:{PROFILE['email']}", text_decoration="none"),
                rx.link(secondary_button("GitHub ↗"), href=PROFILE["github"], is_external=True, text_decoration="none"),
                spacing="3",
                wrap="wrap",
                justify="center",
            ),
            background=COLORS["surface"],
            border=f"1px solid {COLORS['line']}",
            border_radius="10px",
            padding=rx.breakpoints(initial="2.5rem 1.5rem", sm="3.5rem"),
            width="100%",
            max_width="980px",
            margin="0 auto",
            align="center",
            spacing="5",
            id="contacto",
        ),
        rx.hstack(
            rx.text("© 2026 María Camila", font_size="12px", color=COLORS["muted"]),
            rx.hstack(
                rx.link("GitHub", href=PROFILE["github"], is_external=True, color=COLORS["muted"], font_size="12px", text_decoration="none", _hover={"color": COLORS["accent"]}),
                rx.link("LinkedIn", href=PROFILE["linkedin"], is_external=True, color=COLORS["muted"], font_size="12px", text_decoration="none", _hover={"color": COLORS["accent"]}),
                spacing="4",
            ),
            justify="between",
            width="100%",
            max_width="980px",
            margin="0 auto",
            padding=rx.breakpoints(initial="1.5rem 0", sm="2rem 0"),
            flex_direction=rx.breakpoints(initial="column", sm="row"),
            align=rx.breakpoints(initial="start", sm="center"),
            spacing="3",
        ),
        width="100%",
        spacing="0",
        padding=rx.breakpoints(initial="4.5rem 1.5rem 0", sm="6rem 2.5rem 0"),
    )
