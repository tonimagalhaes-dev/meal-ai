# backend/Dockerfile

# --- Estágio 1: Builder ---
# Usamos uma imagem Python completa para instalar as dependências.
FROM python:3.11-slim AS builder

# Define o diretório de trabalho dentro do container
WORKDIR /app


# Cria um ambiente virtual para isolar as dependências
RUN python -m venv /opt/venv
# Ativa o ambiente virtual para os comandos seguintes NESTE ESTÁGIO
ENV PATH="/opt/venv/bin:$PATH"

# Copia o ficheiro de dependências primeiro para aproveitar o cache do Docker
COPY requirements.txt .

# Instala as dependências no ambiente virtual
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt


# --- Estágio 2: Final ---
# Usamos uma imagem "slim" que é mais leve para a imagem final
FROM python:3.11-slim

# Define o diretório de trabalho
WORKDIR /app

# Copia o ambiente virtual com as dependências já instaladas do estágio 'builder'
COPY --from=builder /opt/venv /opt/venv

# --- LINHA CRÍTICA ---
# Ativa o ambiente virtual para o ambiente final do container.
# Isto garante que o comando 'uvicorn' seja encontrado.
ENV PATH="/opt/venv/bin:$PATH"

# Cria um utilizador não-root para correr a aplicação por razões de segurança
RUN useradd --create-home appuser
USER appuser

# Copia o código da aplicação para o container
COPY ./app /app/app

# Expõe a porta em que a aplicação vai correr
EXPOSE 8000

# Comando para iniciar a aplicação quando o container arrancar
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
