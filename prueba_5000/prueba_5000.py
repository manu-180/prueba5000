import reflex as rx


def index() -> rx.Component:
    return rx.center(
        rx.link(
            rx.button(
            rx.text("linkin"),
            ),
        href="https://www.linkedin.com/feed/",
        is_external=True
        )
    )
    
    
app = rx.App()
app.add_page(index)