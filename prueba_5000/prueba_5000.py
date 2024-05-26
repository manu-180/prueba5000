import reflex as rx

class Colores(rx.State):
    color:str = "green"
    
    def change_color(self):
        if self.color == "green":
            self.color = "red"
        else:
            self.color = "green"


def index() -> rx.Component:
    return rx.center(
        rx.link(
            rx.button(
            rx.text("linkedIn"),
            color_scheme=Colores.color,
            on_click=Colores.change_color()
            ),
        href="https://www.linkedin.com/feed/",
        is_external=True
        ),
        rx.button(
            rx.text("linkedIn"),
            disabled=True
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

    
    
    
app = rx.App()
app.add_page(index)

app.api.add_api_route("/hola/{user}", hola)
