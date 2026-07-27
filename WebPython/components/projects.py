import reflex as rx

from WebPython.components.ui import COLORS, section_heading
from WebPython.data import PROJECTS


def project_tag(name: str) -> rx.Component:
    return rx.box(
        rx.text(name, font_size="11px", letter_spacing="0.03em", color=COLORS["blue"]),
        padding="4px 8px",
        border_radius="3px",
        background="rgba(119, 183, 255, 0.10)",
    )


def project_item(project: dict) -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.text(project["name"], font_family="'Playfair Display', serif", font_size="20px", color=COLORS["text"]),
            rx.spacer(),
            rx.link("Repositorio ↗", href=project["repository"], is_external=True, color=COLORS["accent"], font_size="12px", text_decoration="none"),
            width="100%",
            align="center",
        ),
        rx.text(project["description"], font_size="14px", color=COLORS["muted"], font_weight="300", line_height="1.6"),
        rx.flex(*[project_tag(tag) for tag in project["tags"]], wrap="wrap", gap="7px", width="100%"),
        rx.cond(
            project["demo"] != "",
            rx.link("Ver demo en vivo ↗", href=project["demo"], is_external=True, color=COLORS["text"], font_size="13px", text_decoration="underline"),
        ),
        spacing="4",
        align_items="flex-start",
        padding=rx.breakpoints(initial="1.5rem", sm="1.8rem"),
        background=COLORS["surface"],
        border=f"1px solid {COLORS['line']}",
        border_radius="8px",
        width="100%",
        _hover={"border_color": "rgba(214, 194, 157, 0.48)", "transform": "translateY(-3px)"},
        transition="all 180ms ease",
    )


def projects() -> rx.Component:
    return rx.vstack(
        rx.vstack(
            section_heading("Proyectos seleccionados"),
            rx.text("Una selección de trabajos que refleja mi enfoque técnico y de producto.", color=COLORS["muted"], font_size="15px"),
            rx.grid(*[project_item(project) for project in PROJECTS], columns=rx.breakpoints(initial="1", sm="2"), spacing="5", width="100%"),
            spacing="6",
            width="100%",
            max_width="980px",
            margin="0 auto",
            padding=rx.breakpoints(initial="4.5rem 1.5rem", sm="5.5rem 2.5rem"),
            id="proyectos",
        ),
        border_top=f"1px solid {COLORS['line']}",
        width="100%",
    )
