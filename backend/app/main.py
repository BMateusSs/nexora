from fastapi import FastAPI
from app.routers.health import router as health_router

app = FastAPI(
    title="Nexora API",
    description="API da plataforma Nexora",
    version="0.1.0",
)

@app.get("/")
def read_root():
    return {"Hello": "World"}

app.include_router(health_router)