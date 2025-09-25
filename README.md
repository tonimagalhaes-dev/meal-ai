# MealIA - Planejador de Cardápios com IA

O MealIA é uma aplicação web para o planejamento de cardápios familiares semanais, utilizando Inteligência Artificial para gerar sugestões personalizadas. Este projeto está sendo desenvolvido com um foco em aprender e aplicar tecnologias modernas de desenvolvimento, cloud e IA.

## Status do Projeto

**ÉPICO 1: Foundation & Cloud Infrastructure - CONCLUÍDO!**
* [x] Ambiente de desenvolvimento local 100% containerizado com Docker.
* [x] Pipeline de CI/CD com Google Cloud Build.
* [x] Deploy automatizado do backend (FastAPI) no Google Cloud Run.
* [x] Deploy automatizado do frontend (React) no Firebase Hosting.
* [x] Conexão segura com banco de dados PostgreSQL no Google Cloud SQL.
* [x] Gestão de migrações de banco de dados com Alembic.

**Próximo Passo:** Iniciar o **Épico 2: AI-Powered Features**.

## Stack de Tecnologia

* **Backend:** Python com **FastAPI**
* **Frontend:** **React**
* **Banco de Dados:** **PostgreSQL**
* **Containerização:** **Docker** e **Docker Compose**
* **Plataforma Cloud:** **Google Cloud Platform (GCP)**
    * **Hospedagem Backend:** Cloud Run
    * **Hospedagem Frontend:** Firebase Hosting
    * **CI/CD:** Cloud Build
    * **Banco de Dados Gerenciado:** Cloud SQL
    * **Gestão de Segredos:** Secret Manager

---

## Ambiente de Produção (Implantado na GCP)

Graças ao pipeline de CI/CD, cada `push` para a branch `main` é automaticamente implantado.

* **Frontend (React App):** [https://meal-ai-development-c1604.web.app/](https://meal-ai-development-c1604.web.app/)
* **Backend (FastAPI):** [https://mealia-backend-959470190812.us-central1.run.app/](https://mealia-backend-959470190812.us-central1.run.app/)
    * **Endpoint de Health Check:** [https://mealia-backend-959470190812.us-central1.run.app/db-test](https://mealia-backend-959470190812.us-central1.run.app/db-test)

---

## Ambiente de Desenvolvimento Local

Todo o ambiente de desenvolvimento é orquestrado pelo Docker Compose, garantindo consistência e facilidade de configuração.

### **Pré-requisitos**

* **Docker Desktop:** Certifique-se de que o [Docker Desktop](https://www.docker.com/products/docker-desktop/) está instalado e rodando na sua máquina.

### **Como Iniciar**

Para iniciar todos os serviços (Backend, Frontend e Banco de Dados), navegue até a pasta raiz do projeto no seu terminal e execute o seguinte comando:

docker-compose up --build
  up: Inicia os contêineres.
  --build: Reconstrói as imagens se houver alguma alteração nos Dockerfiles. Use este comando da primeira vez ou sempre que alterar a configuração de um serviço.
Após a execução, os serviços estarão disponíveis nos seguintes endereços:

Frontend (React App): http://localhost:3000
Backend (FastAPI Docs): http://localhost:8000/docs
Banco de Dados (PostgreSQL):
Host: localhost
Porta: 5432
Base de Dados: mealiadb
Usuário: user
Senha: password

### **Como Parar**
Para parar todos os serviços, pressione Ctrl + C no terminal onde o docker-compose está rodando. Depois, para garantir que os contêineres sejam removidos, execute:
docker-compose down

Solução de Problemas (Local)
Se encontrar erros inesperados, pode ser necessário forçar uma limpeza completa do ambiente Docker.
Atenção: Este comando irá apagar todos os dados do seu banco de dados local.
docker-compose down -v