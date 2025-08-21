# frontend/Dockerfile

# --- Estágio 1: Builder ---
FROM node:18-alpine AS builder

WORKDIR /app

# Otimização: Copia ambos os ficheiros de uma só vez.
# O '?' torna o package-lock.json opcional, evitando erros se ele não existir.
COPY package*.json ./

RUN npm install

# --- ERRO CORRIGIDO ---
# Esta linha estava em falta. Ela copia todo o código-fonte.
COPY . .

RUN npm run build


# --- Estágio 2: Final ---
FROM nginx:1.25-alpine

COPY --from=builder /app/build /usr/share/nginx/html

EXPOSE 80
