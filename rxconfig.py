import reflex as rx

config = rx.Config(
    app_name="prueba_5000",
    api_url="https://api.baackend.com",
    cors_allowed_origins=[
        "http://localhost:3000",
        "http://localhost:3001",
        "https://baackend.com"
    ]
)