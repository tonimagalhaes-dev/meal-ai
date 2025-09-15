# backend/Dockerfile
# --- Estágio 1: Builder ---
FROM python:3.11-slim AS builder
WORKDIR /app
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# --- Estágio 2: Final ---
FROM python:3.11-slim
WORKDIR /app
COPY --from=builder /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

RUN useradd --create-home appuser
USER appuser

# Copia todo o código do backend, incluindo o start.sh
COPY . .

EXPOSE 8000

# Variável de ambiente para controlar o modo (development/production)
ENV ENVIRONMENT=development

# --- CORREÇÃO AQUI ---
# Torna o script de inicialização executável e define-o como o ponto de entrada.
RUN chmod +x ./start.sh
ENTRYPOINT ["./start.sh"]