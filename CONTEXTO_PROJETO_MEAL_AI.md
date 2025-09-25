# Contexto do Projeto MealIA

Este documento serve como um ponto de partida para contextualizar o assistente de IA sobre o estado atual, objetivos e stack tecnológico do projeto MealIA, com base no backlog oficial. **Última atualização: 18/09/2025.**

## 1. Visão Geral do Projeto

O MealIA é uma aplicação web para o planejamento de cardápios familiares semanais, utilizando Inteligência Artificial para gerar sugestões personalizadas. O objetivo principal é o aprendizado prático de tecnologias modernas de desenvolvimento de software, cloud e IA.

## 2. Stack de Tecnologia

* **Backend:** Python com **FastAPI**
* **Frontend:** **React**
* **Banco de Dados:** **PostgreSQL** (gerido pelo **Cloud SQL** no GCP)
* **Cloud:** **Google Cloud Platform (GCP)**
    * **Hospedagem Backend:** Cloud Run
    * **Hospedagem Frontend:** Firebase Hosting
    * **CI/CD:** Cloud Build
    * **Container Registry:** Artifact Registry
* **Containerização:** **Docker** e **Docker Compose**

---

# Epic 1: Foundation & Cloud Infrastructure (CONCLUÍDO)

### ✅ Story 1.1: Containerização da Aplicação

**Como** desenvolvedor, **Eu quero** containerizar o MealIA com Docker, **Para que** possa deployar de forma consistente em qualquer ambiente.
* **Status:** Concluída.

### ✅ Story 1.2: Setup GCP Project e Cloud Run Deploy

**Como** desenvolvedor, **Eu quero** deployar o MealIA no Cloud Run, **Para que** tenha uma versão rodando na nuvem.
* **Status:** Concluída. O deploy do backend está funcional.

### ✅ Story 1.3: Conectividade com Cloud SQL PostgreSQL

**Como** desenvolvedor, **Eu quero** que a aplicação se conecte a um banco de dados PostgreSQL, **Para que** tenha persistência confiável e queries eficientes.
* **Status:** Concluída. A conexão com o Cloud SQL está funcional e o schema inicial foi migrado com Alembic.

### ✅ Story 1.4: Implementar CI/CD com Cloud Build

**Como** desenvolvedor, **Eu quero** um pipeline automatizado de CI/CD, **Para que** deployments sejam rápidos e confiáveis.
* **Status:** Concluída. O pipeline básico de build e deploy para backend e frontend está implementado e funcional.

---

# Epic 2: AI-Powered Features (Próximo Épico)

### 🚧 Story 2.1: Integração com Vertex AI

**Como** usuário, **Eu quero** que o sistema use IA para gerar cardápios, **Para que** tenha sugestões mais inteligentes e personalizadas.
* **Status:** A Fazer.
* **Prioridade:** Muito Alta.

### 🔧 Tasks para a Story 2.1:

* [ ]  **Task 2.1.1:** Setup Vertex AI no projeto
* [ ]  **Task 2.1.2:** Implementar integração com LangChain
* [ ]  **Task 2.1.3:** Desenvolver prompts para cardápios
* [ ]  **Task 2.1.4:** Implementar *tools* para o agent (ex: buscar receitas no banco)
* [ ]  **Task 2.1.5:** Implementar tratamento de erros e fallbacks

---

## Informações Técnicas Atuais

### Configuração do Projeto GCP:
* **Project ID:** `meal-ai-development`
* **Firebase Project ID:** `meal-ai-development-c1604`
* **Região Principal:** `us-central1`

### Service Account Principal:
* **Nome:** `cloudrun-deployer@meal-ai-development.iam.gserviceaccount.com`
* **Funções Ativas:** `Cloud Run Admin`, `Storage Admin`, `Secret Manager Secret Accessor`, `Logs Writer`, `Artifact Registry Admin`, `Firebase Admin`, `Cloud SQL Client`, `Service Account User`.

### Endpoints Ativos:
* **Backend (Cloud Run):** `https://mealia-backend-959470190812.us-central1.run.app`
* **Frontend (Firebase):** `https://meal-ai-development-c1604.web.app`

### Débitos Técnicos e Melhorias Futuras:
* **CI/CD:** Adicionar um passo para executar as migrações do Alembic automaticamente no deploy.
* **Cloud SQL:** Configurar IP privado e otimizar a política de backups.
* **Frontend:** Implementar o código da aplicação React e ajustar o deploy no CI/CD.