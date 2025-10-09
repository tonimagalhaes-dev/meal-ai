# backend/app/services/menu_generator.py

from langchain_google_vertexai import VertexAI

# Variável para guardar o modelo, mas não o inicialize ainda.
_model = None

def get_model():
    """
    Função que inicializa o modelo na primeira vez que for chamado
    e o reutiliza nas chamadas seguintes (padrão singleton).
    """
    global _model
    if _model is None:
        # O 'project' não é necessário aqui, pois o vertexai.init() no main.py já o configurou.
        _model = VertexAI(model_name="gemini-1.0-pro", temperature=0.7)
    return _model

def generate_test_message(input_text: str) -> str:
    """
    Função simples para invocar o modelo de IA com uma mensagem de teste.
    """
    try:
        # Pega o modelo através da função, garantindo que ele já foi inicializado
        model = get_model()
        response = model.invoke(input_text)
        return response
    except Exception as e:
        # Tratamento básico de erros
        print(f"Erro ao invocar o modelo de IA: {e}")
        return "Desculpe, ocorreu um erro ao contatar a IA."