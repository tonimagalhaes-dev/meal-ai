# frontend/Dockerfile

# Usamos a imagem Node.js como base
FROM node:18-alpine

# Define o diretório de trabalho
WORKDIR /app

# Copia os ficheiros de manifesto de dependências para aproveitar o cache
COPY package*.json ./

# Instala as dependências
RUN npm install

# Copia o resto do código da aplicação
COPY . .

# Expõe a porta 3000, que é a porta padrão do servidor de desenvolvimento do React
EXPOSE 3000

# Comando para iniciar o servidor de desenvolvimento quando o container arrancar
CMD ["npm", "start"]

