import reflex as rx
import os
import dotenv
from supabase import create_client, Client


url: str = "https://gcjyhrlcftbkeaiqlzlm.supabase.co"
key: str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImdjanlocmxjZnRia2VhaXFsemxtIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MTU3MjQ3NzAsImV4cCI6MjAzMTMwMDc3MH0.MFsm9DJ9XnVnsTUK-N2SsCBf8wnhW03mGp5d2Z2Jf9Q"

class Horarios(rx.Base):
    id = int
    horario = int
    cant_users = int
    

class Supabase:
    
    dotenv.load_dotenv()
    
    SUPABASE_URL = os.environ.get("SUPABASE_URL")
    SUPABASE_KEY = os.environ.get("SUPABASE_KEY")
    
    supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
    
    supabase: Client = create_client(url, key)
    
    def data(self):
        
        data_list = []
        
        response = self.supabase.table('Horarios').select("*").execute()
        if len(response.data) > 0:
            for i in response.data:
                data_list.append(Horarios(id=i["id"], horario= i["horario"], cant_users=i["cant_users"]))
        return data_list
    
    def horarios(self):
        horarios=[]
        data = self.data()
        for i in data:
            horarios.append(i.horario)
        horarios.sort()
        return horarios
                
    def unico_horario(self, id):
        data = self.data()
        for i in data:
            if i.id == id:
                return i.horario


supabase = Supabase()
    

class Colores(rx.State):
    color: str = "pink"
    data_info: list = []
    
    async def data(self):
        self.data_info = await supabase.data()
        print(self.data_info)

    def change_color(self):
        if self.color == "green":
            self.color = "red"
        else:
            self.color = "green"

@rx.page(
    title="turnos",
    description="Taller de ceramica",
    on_load=Colores.data
)
def index() -> rx.Component:
    return rx.center(
            rx.vstack(
                button(1),
                button(2),
                button(3),
                button(4),
                button(5),
                button(1),
                button(2),
                button(3),
                button(4),
                button(5),
            )
        )
    

def button(id):
    return rx.button(
        rx.text(supabase.unico_horario(id)),
        color_scheme=Colores.color,
        on_click=Colores.change_color  # Sin paréntesis, pasar como referencia
    )

async def hola(user: str) -> str:
    if user == "juli":
        return "hello juli"
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

# if __name__ == "__main__":
#     print("Current working directory:", os.getcwd())
#     app._compile()