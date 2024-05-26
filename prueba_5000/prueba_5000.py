import reflex as rx

class Colores(rx.State):
    color:str = "pink"
    
    def change_color(self):
        if self.color == "pink":
            self.color = "red"
        else:
            self.color = "pink"


def index() -> rx.Component:
    return rx.center(
            rx.button(
            rx.text("linkedIn"),
            color_scheme=Colores.color,
            on_click=Colores.change_color()
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