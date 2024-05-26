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
    

async def hola(user:str) -> str:
    if user == "juli":
        return "hello juli "
    elif user == "cami":
        return "hello cami"
    elif user == "theo":
        return "hello theo"
    elif user == "viejo":
        return "hello viejo"
    elif user == "vieja":
        return "hello vieja"

async def hola():
    return "hello manu"
    
    
    
app = rx.App()
app.add_page(index)

app.api.add_api_route("/hola/{user}", hola)
app.api.add_api_route("/hola", hola)
