#!/bin/bash
# Script inteligente que adapta a inicialização conforme o ambiente

# Define a porta padrão para 8000 se a variável PORT não estiver definida
# Em produção, Cloud Run irá definir esta variável.
PORT=${PORT:-8000}

echo "ENVIRONMENT: $ENVIRONMENT"
echo "PORT: $PORT"

if [ "$ENVIRONMENT" = "development" ]; then
    echo "🚀 Iniciando em modo DESENVOLVIMENTO com hot reload na porta $PORT..."
    exec uvicorn app.main:app --host 0.0.0.0 --port "$PORT" --reload
else
    echo "🏭 Iniciando em modo PRODUÇÃO otimizado na porta $PORT..."
    exec uvicorn app.main:app --host 0.0.0.0 --port "$PORT" --workers 1
fi