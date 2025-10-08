# backend/app/main.py

# backend/app/main.py
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app.db.database import engine, get_db, Base
from app.services.menu_generator import generate_test_message

app = FastAPI(
    title="MealIA API",
    description="API para geração de cardápios semanais com IA.",
    version="0.1.0",
)

@app.get("/", tags=["Root"])
def read_root():
    return {"message": "Bem-vindo à API do Meal-AI! Conectado e pronto para servir."}

@app.get("/db-test", tags=["Database"])
def test_db_connection(db: Session = Depends(get_db)):
    try:
        # Tenta executar uma consulta simples
        db.execute('SELECT 1')
        return {"status": "success", "message": "Conexão com o banco de dados bem-sucedida!"}
    except Exception as e:
        return {"status": "error", "message": f"Falha na conexão com o banco de dados: {e}"}
    
@app.get("/ai-test", tags=["AI"])
def test_ai_connection():
    """
    Envia uma mensagem de teste para o Vertex AI para verificar a conectividade.
    """
    prompt = "Olá, IA! Me diga em uma única frase por que cozinhar é incrível."
    ai_response = generate_test_message(prompt)
    return {"prompt_enviado": prompt, "resposta_da_ia": ai_response}