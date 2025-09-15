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

# --- CORREÇÃO DE ORDEM ---
# 1. Copia os ficheiros da aplicação como root
COPY . .

# 2. Cria o utilizador não-root
RUN useradd --create-home appuser

# 3. Dá a permissão de execução ao script e muda o dono de todos os ficheiros para o novo utilizador
RUN chmod +x ./start.sh && chown -R appuser:appuser /app

# 4. Muda para o utilizador não-root
USER appuser

# Expõe a porta em que a aplicação vai correr
EXPOSE 8000

# Variável de ambiente para controlar o modo
ENV ENVIRONMENT=production

# Define o ponto de entrada para o nosso script
ENTRYPOINT ["./start.sh"]