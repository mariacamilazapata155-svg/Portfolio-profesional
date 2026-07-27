import reflex as rx

from WebPython.components.navbar import navbar
from WebPython.components.hero import hero
from WebPython.components.about import about
from WebPython.components.skills import skills
from WebPython.components.projects import projects
from WebPython.components.footer import footer
from WebPython.components.ui import COLORS
from WebPython.data import PROFILE

def index() -> rx.Component:
    return rx.vstack(
        navbar(),
        hero(),
        about(),
        skills(),
        projects(),
        footer(),
        spacing="0",
        width="100%",
        min_height="100vh",
        background_color=COLORS["background"],
        id="inicio",
    )

app = rx.App(
    style={
        "font_family": "'DM Sans', sans-serif",
        "background_color": COLORS["background"],
        "color": COLORS["text"],
        "scroll_behavior": "smooth",
        "::selection": {"background": "rgba(214, 194, 157, 0.35)"},
        "a:focus-visible": {"outline": f"2px solid {COLORS['accent']}", "outline_offset": "3px"},
    },
    stylesheets=[
        "https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700&family=DM+Sans:wght@300;400;500&display=swap"
    ],
)

app.add_page(
    index,
    title=f"{PROFILE['name']} | {PROFILE['role']}",
    description="Portfolio profesional de María Camila, ingeniera de software enfocada en desarrollo web.",
)
