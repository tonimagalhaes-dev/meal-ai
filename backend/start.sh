#!/bin/bash

# Script inteligente que adapta a inicialização conforme o ambiente

if [ "$ENVIRONMENT" = "development" ]; then
    echo "🚀 Iniciando em modo DESENVOLVIMENTO com hot reload..."
    exec uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
else
    echo "🏭 Iniciando em modo PRODUÇÃO otimizado..."
    exec uvicorn app.main:app --host 0.0.0.0 --port 8000 --workers 1
fi