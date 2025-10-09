# backend/app/services/menu_generator.py

from langchain_google_vertexai import VertexAI
#from app.core.config import settings

# O 'temperature' controla a criatividade (0 = mais determinístico, 1 = mais criativo).
model = VertexAI(model_name="gemini-1.0-pro", temperature=0.7)

def generate_test_message(input_text: str) -> str:
    """
    Função simples para invocar o modelo de IA com uma mensagem de teste.
    """
    try:
        # O método .invoke envia o prompt para a IA e aguarda a resposta.
        response = model.invoke(input_text)
        return response
    except Exception as e:
        # Tratamento básico de erros  
        print(f"Erro ao invocar o modelo de IA: {e}")
        return "Desculpe, ocorreu um erro ao contatar a IA."