import reflex as rx

from WebPython.components.ui import COLORS, section_heading
from WebPython.data import SKILLS


def skill_tag(name: str, highlight: bool = False) -> rx.Component:
    return rx.box(
        rx.text(name, font_size="12px", letter_spacing="0.04em", color=COLORS["accent"] if highlight else COLORS["muted"]),
        padding="7px 12px",
        border=f"1px solid {'rgba(214, 194, 157, 0.42)' if highlight else COLORS['line']}",
        border_radius="4px",
        background="rgba(214, 194, 157, 0.08)" if highlight else "transparent",
        _hover={"border_color": COLORS["accent"], "color": COLORS["accent"]},
        transition="border-color 160ms ease",
    )


def skills() -> rx.Component:
    return rx.vstack(
        rx.vstack(
            section_heading("Tecnologías"),
            rx.text("Herramientas con las que construyo, itero y despliego productos web.", color=COLORS["muted"], font_size="15px"),
            rx.flex(
                *[skill_tag(skill, highlight=True) for skill in SKILLS["principal"]],
                *[skill_tag(skill) for skill in SKILLS["complementarias"]],
                wrap="wrap",
                gap="8px",
                width="100%",
            ),
            spacing="6",
            width="100%",
            max_width="980px",
            margin="0 auto",
            padding=rx.breakpoints(initial="4.5rem 1.5rem", sm="5.5rem 2.5rem"),
            id="skills",
        ),
        border_top=f"1px solid {COLORS['line']}",
        width="100%",
    )
