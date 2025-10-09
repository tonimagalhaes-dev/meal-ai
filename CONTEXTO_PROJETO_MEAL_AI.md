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

<<<<<<< HEAD
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
=======
* **Testes:** Cobertura de testes unitários > 80% com `pytest`. Testes de integração automatizados em cada Pull Request.
* **Métricas Chave:** API response time < 200ms, Uptime > 99.9%.
* **Monitorização:** Cloud Logging e Cloud Monitoring configurados no pipeline.

# Contexto do Projeto MealIA

Este documento serve como um ponto de partida para contextualizar o assistente de IA sobre o estado atual, objetivos e stack tecnológico do projeto MealIA, com base no backlog oficial. **Última atualização: 09/10/2025.**

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

# Contexto do Projeto MealIA

Este documento serve como um ponto de partida para contextualizar o assistente de IA sobre o estado atual, objetivos e stack tecnológico do projeto MealIA. **Última atualização: 10/10/2025.**

## 1. Resumo do Projeto (O Quê e Por Quê)

O MealIA é um projeto para desenvolver uma aplicação web que gera cardápios semanais personalizados para famílias, utilizando IA para as sugestões. O objetivo principal é o aprendizado prático de tecnologias modernas de desenvolvimento de software, cloud e IA, seguindo um plano de desenvolvimento estruturado.

## 2. Objetivos de Negócio (OKRs)

Os objetivos principais do projeto são:
* **Modernizar a Arquitetura Técnica:** Migrar 100% da aplicação para GCP, implementar CI/CD e atingir 99.9% de uptime.
* **Potencializar com IA:** Integrar o Vertex AI para geração inteligente de cardápios e implementar busca semântica.
* **Escalar para Produção:** Suportar mais de 1000 usuários simultâneos e implementar monitoramento completo.

## 3. Arquitetura e Stack de Tecnologia

* **Backend:** Python com o framework **FastAPI**.
* **Frontend:** **React**.
* **Base de Dados:** **PostgreSQL**, gerido pelo **Cloud SQL** no GCP.
* **Plataforma Cloud:** **Google Cloud Platform (GCP)**.
    * **Hospedagem Back-end:** Cloud Run (Serverless).
    * **Hospedagem Front-end:** Firebase Hosting.
    * **CI/CD:** Cloud Build.
    * **Container Registry:** Artifact Registry (us-central1).
* **Containerização:** **Docker** para o ambiente de desenvolvimento local e para a imagem de produção.

---

## 4. Progresso dos Épicos

### ✅ Epic 1: Foundation & Cloud Infrastructure (CONCLUÍDO)

Todas as User Stories (1.1 a 1.4) foram concluídas. A base da aplicação, incluindo ambiente local com Docker, pipeline de CI/CD, deploy na nuvem com Cloud Run e Firebase, e a conexão com o banco de dados Cloud SQL com Alembic, está funcional.

### 🚧 Epic 2: AI-Powered Features (EM PROGRESSO)

#### **🚧 Story 2.1: Integração com Vertex AI**
* **Status:** Em Progresso.
* **Prioridade:** Muito Alta.

**Tasks da Story 2.1:**
* [x] **Task 2.1.1:** Setup Vertex AI no projeto (API habilitada, permissões da Service Account configuradas).
* [🚧] **Task 2.1.2:** Implementar integração com LangChain (Dependências instaladas, código de conexão implementado).
* [ ] **Task 2.1.3:** Desenvolver prompts para cardápios.
* [ ] **Task 2.1.4:** Implementar *tools* para o agent.
* [ ] **Task 2.1.5:** Implementar tratamento de erros e fallbacks.

---

## 5. Ponto Atual e Próximos Passos (10/10/2025)

* **Situação:** Após configurar o ambiente local (Docker, Git, `gcloud`), o teste do endpoint `/ai-test` está a falhar.
* **Erro Observado:** A API retorna a mensagem de erro genérica: `"resposta_da_ia": "Desculpe, ocorreu um erro ao contatar a IA."`.
* **Próximo Passo Imediato:** Analisar os logs do contêiner `mealia_api` no momento em que o teste é executado para identificar a exceção específica (o erro real) que está a ser capturada pelo bloco `try...except` no código.

---

## 6. Configuração Atual do Projeto GCP

# Contexto do Projeto MealIA

Este documento serve como um ponto de partida para contextualizar o assistente de IA sobre o estado atual, objetivos e stack tecnológico do projeto MealIA. **Última atualização: 10/10/2025.**

## 1. Resumo do Projeto (O Quê e Por Quê)

O MealIA é um projeto para desenvolver uma aplicação web que gera cardápios semanais personalizados para famílias, utilizando IA para as sugestões. O objetivo principal é o aprendizado prático de tecnologias modernas de desenvolvimento de software, cloud e IA, seguindo um plano de desenvolvimento estruturado.

## 2. Stack de Tecnologia

- **Backend:** Python com o framework **FastAPI**.
- **Frontend:** **React**.
- **Base de Dados:** **PostgreSQL**, gerido pelo **Cloud SQL** no GCP.
- **Plataforma Cloud:** **Google Cloud Platform (GCP)**.
    - **Hospedagem Back-end:** Cloud Run (Serverless).
    - **Hospedagem Front-end:** Firebase Hosting.
    - **CI/CD:** Cloud Build.
    - **Logs e Monitorização:** Cloud Logging e Cloud Monitoring.
    - **Container Registry:** Artifact Registry (us-central1).
- **Containerização:** **Docker** para o ambiente de desenvolvimento local e para a imagem de produção.

---

## 3. Progresso dos Épicos

### ✅ Epic 1: Foundation & Cloud Infrastructure (CONCLUÍDO)

Todas as User Stories (1.1 a 1.4) foram concluídas. A base da aplicação, incluindo ambiente local com Docker, pipeline de CI/CD, deploy na nuvem com Cloud Run e Firebase, e a conexão com o banco de dados Cloud SQL com Alembic, está funcional.

### 🚧 Epic 2: AI-Powered Features (EM PROGRESSO)

#### 🚧 Story 2.1: Integração com Vertex AI
- **Status:** Em Progresso.
- **Prioridade:** Muito Alta.

**Tasks da Story 2.1:**
- [x] **Task 2.1.1:** Setup Vertex AI no projeto (API habilitada, permissões da Service Account configuradas).
- [🚧] **Task 2.1.2:** Implementar integração com LangChain (Dependências instaladas, código de conexão implementado).
- [ ] **Task 2.1.3:** Desenvolver prompts para cardápios.
- [ ] **Task 2.1.4:** Implementar *tools* para o agent.
- [ ] **Task 2.1.5:** Implementar tratamento de erros e fallbacks.

---

## 4. Ponto Atual e Próximos Passos (10/10/2025)

- **Situação:** Após configurar o ambiente local (Docker, Git, `gcloud`), o teste do endpoint `/ai-test` está a falhar.
- **Erro Observado:** A API retorna a mensagem de erro genérica: `"resposta_da_ia": "Desculpe, ocorreu um erro ao contatar a IA."`.
- **Próximo Passo Imediato:** Analisar os logs do contêiner `mealia_api` no momento em que o teste é executado para identificar a exceção específica (o erro real) que está a ser capturada pelo bloco `try...except` no código.

---

## 5. Configuração Atual do Projeto GCP

### Informações do Projeto:
- **Nome de Exibição:** Meal-AI Development
# Contexto do Projeto MealIA

Este documento serve como um ponto de partida para contextualizar o assistente de IA sobre o estado atual, objetivos e stack tecnológico do projeto MealIA. **Última atualização: 10/10/2025.**

## 1. Resumo do Projeto (O Quê e Por Quê)

O MealIA é um projeto para desenvolver uma aplicação web que gera cardápios semanais personalizados para famílias, utilizando IA para as sugestões. O objetivo principal é o aprendizado prático de tecnologias modernas de desenvolvimento de software, cloud e IA, seguindo um plano de desenvolvimento estruturado.

## 2. Stack de Tecnologia

- **Backend:** Python com o framework **FastAPI**.
- **Frontend:** **React**.
- **Base de Dados:** **PostgreSQL**, gerido pelo **Cloud SQL** no GCP.
- **Plataforma Cloud:** **Google Cloud Platform (GCP)**.
    - **Hospedagem Back-end:** Cloud Run (Serverless).
    - **Hospedagem Front-end:** Firebase Hosting.
    - **CI/CD:** Cloud Build.
    - **Logs e Monitorização:** Cloud Logging e Cloud Monitoring.
    - **Container Registry:** Artifact Registry (us-central1).
- **Containerização:** **Docker** para o ambiente de desenvolvimento local e para a imagem de produção.

---

## 3. Progresso dos Épicos

### ✅ Epic 1: Foundation & Cloud Infrastructure (CONCLUÍDO)

Todas as User Stories (1.1 a 1.4) foram concluídas. A base da aplicação, incluindo ambiente local com Docker, pipeline de CI/CD, deploy na nuvem com Cloud Run e Firebase, e a conexão com o banco de dados Cloud SQL com Alembic, está funcional.

### 🚧 Epic 2: AI-Powered Features (EM PROGRESSO)

#### 🚧 Story 2.1: Integração com Vertex AI
- **Status:** Em Progresso.
- **Prioridade:** Muito Alta.

**Tasks da Story 2.1:**
- [x] **Task 2.1.1:** Setup Vertex AI no projeto (API habilitada, permissões da Service Account configuradas).
- [🚧] **Task 2.1.2:** Implementar integração com LangChain (Dependências instaladas, código de conexão implementado).
- [ ] **Task 2.1.3:** Desenvolver prompts para cardápios.
- [ ] **Task 2.1.4:** Implementar *tools* para o agent.
- [ ] **Task 2.1.5:** Implementar tratamento de erros e fallbacks.

---

## 4. Ponto Atual e Próximos Passos (10/10/2025)

- **Situação:** Após configurar o ambiente local (Docker, Git, `gcloud`), o teste do endpoint `/ai-test` está a falhar.
- **Erro Observado:** A API retorna a mensagem de erro genérica: `"resposta_da_ia": "Desculpe, ocorreu um erro ao contatar a IA."`.
- **Próximo Passo Imediato:** Analisar os logs do contêiner `mealia_api` no momento em que o teste é executado para identificar a exceção específica (o erro real) que está a ser capturada pelo bloco `try...except` no código.

---

## 5. Configuração Atual do Projeto GCP

### Informações do Projeto:
- **Nome de Exibição:** Meal-AI Development
- **Project ID (Principal):** `meal-ai-development`
- **Firebase Project ID (Alias):** `meal-ai-development-c1604`

### APIs Ativadas:
- Cloud Run API, Cloud Build API, Firebase Hosting API, Cloud SQL Admin API, Secret Manager API, Artifact Registry API, Vertex AI API.

### Service Account Principal:
- **Nome:** `cloudrun-deployer@meal-ai-development.iam.gserviceaccount.com`
- **Funções Ativas:** `Cloud Run Admin`, `Storage Admin`, `Secret Manager Secret Accessor`, `Logs Writer`, `Artifact Registry Admin`, `Firebase Admin`, `Cloud SQL Client`, `Service Account User`, `Vertex AI User`.

---

## 6. Informações Adicionais e Histórico

Este arquivo consolida várias versões e atualizações do contexto do projeto. Principais pontos adicionais extraídos das versões anteriores:

- Informações do projeto (nome, project id, firebase id, e-mail de contato) e orçamento estão registrados no repositório e nas configurações do GCP.
- Detalhes operacionais sobre deploys (Cloud Run endpoint, Firebase Hosting URL) e recomendações de melhorias (executar migrações do Alembic no CI/CD, configurar IP privado para Cloud SQL) devem ser mantidos atualizados conforme infraestrutura for modificada.
- Metas de qualidade: testes unitários com pytest, cobertura > 80%, métricas de performance (API <200ms, uptime >99.9%) e monitorização com Cloud Logging/Monitoring.

---

## 7. Próximos Passos Recomendados

1. Corrigir o erro do endpoint `/ai-test` analisando logs do contêiner local (`mealia_api`) e o código no backend que chama a IA.
2. Completar a integração LangChain/Vertex AI (Task 2.1.2 a 2.1.5).
3. Adicionar step no `cloudbuild.yaml` para executar migrações Alembic durante o deploy.
4. Validar permissões da Service Account para deploy do frontend no Firebase (adicionar `roles/firebase.admin` se necessário).

---

## 8. Contatos e Repositório

- Repositório: https://github.com/tonimagalhaes-dev/meal-ai
- Branches principais: `develop`, `main`
- Contato: tonimagalhaes.dev@gmail.com

---

*Arquivo consolidado automaticamente pelo script de resolução de conflitos.*
