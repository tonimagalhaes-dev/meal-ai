# backend/app/main.py

from fastapi import FastAPI

app = FastAPI(
    title="MealIA API",
    description="API para geração de cardápios semanais com IA.",
    version="0.1.0",
)

@app.get("/", tags=["Root"])
def read_root():
    return {"message": "Bem-vindo à API do Meal-AI! - com hot reload 25/08/2025"}