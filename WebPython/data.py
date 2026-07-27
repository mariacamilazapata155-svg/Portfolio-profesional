"""Contenido público del portfolio.

Actualiza los enlaces de PROFILE y los proyectos antes de publicar el sitio.
Mantener estos datos aquí evita que información personal y enlaces queden
repartidos entre los componentes visuales.
"""

PROFILE = {
    "name": "María Camila",
    "role": "Ingeniera de software",
    "headline": "Construyo experiencias web claras, accesibles y escalables.",
    "summary": (
        "Me especializo en Python y desarrollo web, combinando una base técnica "
        "sólida con atención al detalle en la experiencia de usuario."
    ),
    # Reemplaza estos valores por tus enlaces públicos antes del despliegue.
    "email": "mariacamilazapata155@gmail.com",
    "github": "https://github.com/mariacamilazapata155-svg",
    "linkedin": "https://www.linkedin.com/in/maria-camila1785",
}

PROJECTS = [
    {
        "name": "Portfolio profesional",
        "description": (
            "Sitio personal responsive creado con Python y Reflex para presentar "
            "proyectos, tecnologías y canales de contacto."
        ),
        "tags": ["Python", "Reflex", "Responsive UI"],
        "repository": "https://github.com/mariacamilazapata155-svg",
        "demo": "",  # Añade la URL de despliegue cuando esté disponible.
    },
    {
        "name": "Plataforma de gestión de proyectos",
        "description": (
            "Aplicación similar a Trello que permite gestionar tareas, tableros y equipos, "
            "cuenta con una base de datos en PostgreSQL, contenedorización con Docker, backend construido con FastAPI."
        ),
        "tags": ["FastAPI", "Docker", "PostgreSQL"],
        "repository": "https://github.com/mariacamilazapata155-svg",
        "demo": "",
    },
]

SKILLS = {
    "principal": ["Python", "FastAPI", "Reflex"],
    "complementarias": ["JavaScript", "React", "Docker", "PostgreSQL", "Git", "REST APIs", "Linux"],
}
