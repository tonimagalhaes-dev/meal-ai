# Contexto do Projeto MealIA

Este documento serve como um ponto de partida para contextualizar o assistente de IA sobre o estado atual, objetivos e stack tecnológico do projeto MealIA. **Última atualização: 14/09/2025.**

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
    * **Logs e Monitorização:** Cloud Logging e Cloud Monitoring.
    * **Container Registry:** Artifact Registry (us-central1).
    * **Nota de Custo:** O projeto é desenvolvido priorizando o uso do **Free Tier do GCP** para limitar o consumo e os custos. É crucial configurar alertas de orçamento e monitorizar o uso para evitar cobranças inesperadas.
* **Containerização:** **Docker** para o ambiente de desenvolvimento local e para a imagem de produção.

## 4. Estrutura do Projeto (Backlog)

O projeto está organizado em 4 Épicos principais, geridos como Issues no GitHub Projects:

1.  **Epic 1: Foundation & Cloud Infrastructure:** Construir a base da aplicação, infraestrutura na GCP, CI/CD e base de dados.
2.  **Epic 2: AI-Powered Features:** Integrar a IA do Google (Vertex AI) para a geração de cardápios e outras funcionalidades inteligentes.
3.  **Epic 3: Production Scale & Security:** Implementar autenticação, segurança e garantir que a aplicação está pronta para produção.
4.  **Epic 4: Advanced Analytics & Optimization:** Focar em monitorização avançada, performance e análise de dados.

## 5. Progresso e Próximos Passos do Épico 1

### Progresso Atual
* **21/08/2025:** A **User Story 1.1 foi concluída com sucesso!** O ambiente de desenvolvimento local está 100% funcional, com backend, frontend e banco de dados a correr de forma orquestrada pelo Docker Compose.
* **14/09/2025:** **Progresso significativo na User Story 1.2!**
    * ✅ O problema com o Artifact Registry foi **resolvido**.
    * 🚧 O pipeline de CI/CD agora falha no deploy do frontend devido a permissões.

---
### **✅ Story 1.1: Configuração do Ambiente de Desenvolvimento Local (CONCLUÍDA)**

**Como** desenvolvedor, **eu quero** um ambiente de desenvolvimento local totalmente containerizado com Docker, **para que** eu possa desenvolver o back-end (FastAPI) e o front-end (React) de forma isolada e consistente.

**Critérios de Aceitação:**

* [x] O comando `docker-compose up` inicia os contêineres do back-end, front-end e base de dados.
* [x] O back-end em FastAPI reinicia automaticamente ao salvar alterações no código (`hot reload`).
* [x] O front-end em React reinicia automaticamente ao salvar alterações no código (`hot reload`).

---
### **🚧 Story 1.2: Setup do Projeto GCP e Deploy Contínuo no Cloud Run (95% COMPLETA)**

**Como** desenvolvedor, **Eu quero** configurar o projeto na Google Cloud e um pipeline de CI/CD, **Para que** cada *push* para a branch principal (`main`) seja automaticamente testado e implantado, disponibilizando a aplicação na nuvem.

**Critérios de Aceitação:**

* [x] O projeto no GCP está configurado com as APIs necessárias e Service Accounts seguras.
* [x] O pipeline de CI/CD (Cloud Build) é acionado a cada `push` na branch `main`.
* [ ] O pipeline executa os testes, constrói a imagem do back-end e a implanta no Cloud Run.
* [ ] O pipeline faz o build dos arquivos estáticos do front-end (React) e os implanta no Firebase Hosting.

**Progresso Detalhado:**

**✅ Fase 1-4: GCP, Service Accounts, Código e Firebase - CONCLUÍDAS**

**🚧 Fase 5: Cloud Build Pipeline - EM PROGRESSO**
- Trigger criado: `meal-ai-production-trigger`
- Repositório GitHub conectado: `tonimagalhaes-dev/meal-ai`
- **Problema atual:** O deploy do frontend no Firebase Hosting está falhando. A causa provável é a falta de permissão `roles/firebase.admin` para a Service Account `cloudrun-deployer`.

**Próximos Passos para Completar:**
1.  Adicionar a permissão `Firebase Admin` à Service Account:
    ```bash
    gcloud projects add-iam-policy-binding meal-ai-development \
        --member="serviceAccount:cloudrun-deployer@meal-ai-development.iam.gserviceaccount.com" \
        --role="roles/firebase.admin"
    ```
2.  Acionar a pipeline novamente com um novo commit na branch `main`.
3.  Descomentar e testar os steps de build e deploy do backend no `cloudbuild.yaml`.
4.  Validar o deploy end-to-end (frontend e backend).

---
### **Story 1.3: Conectividade com o Banco de Dados Cloud SQL**

**Como** desenvolvedor, **Eu quero** que a aplicação no Cloud Run se conecte de forma segura a uma instância do Cloud SQL (PostgreSQL), **Para que** os dados da aplicação tenham persistência confiável e escalável.

**Critérios de Aceitação:**

* [ ] A instância do Cloud SQL (PostgreSQL) está criada e configurada com boas práticas de segurança.
* [ ] As migrações da base de dados (schema) são geridas via Alembic.
* [ ] As credenciais da base de dados de produção são armazenadas de forma segura no Google Secret Manager.

---

## 6. Configuração Atual do Projeto GCP

### Informações do Projeto:
* **Nome:** Meal-AI Development
* **Project ID:** meal-ai-development
* **Firebase Project ID:** meal-ai-development
* **Email da conta:** tonimagalhaes.dev@gmail.com
* **Orçamento:** R$50,00/mês com alertas configurados

### APIs Ativadas:
* Cloud Run API
* Cloud Build API
* Firebase Hosting API
* Cloud SQL Admin API
* Secret Manager API
* Artifact Registry API

### Service Accounts:
* **cloudrun-deployer@meal-ai-development.iam.gserviceaccount.com**
    * `roles/run.admin`
    * `roles/storage.admin`
    * `roles/secretmanager.secretAccessor`
    * `roles/logging.logWriter`
    * `roles/artifactregistry.admin`
    * **Pendente Adicionar:** `roles/firebase.admin`

### Repositório GitHub:
* **URL:** https://github.com/tonimagalhaes-dev/meal-ai
* **Branches:**
    * `develop` (desenvolvimento ativo)
    * `main` (produção com deploy automático)
* **Trigger Cloud Build:** meal-ai-production-trigger (monitora branch main)

## 7. Problemas Conhecidos e Soluções Pendentes

### Problema Anterior - Build Failure:
* **Erro:** `denied: gcr.io repo does not exist...`
* **Status:** **RESOLVIDO**. O problema foi corrigido com a criação de um repositório no Artifact Registry e a atualização do `cloudbuild.yaml`.

### Problema Atual - Deploy do Frontend:
* **Erro:** Falha no passo de deploy do Firebase Hosting.
* **Causa Provável:** A Service Account não possui a permissão `roles/firebase.admin`.
* **Solução Identificada:** Conceder a permissão necessária via comando `gcloud`.

## 8. Ferramentas de Desenvolvimento e Gestão

| Categoria          | Ferramenta                                     | Status      |
| ------------------ | ---------------------------------------------- | ----------- |
| IDE                | VS Code                                        | Configurado |
| Controlo de Versão | Git + GitHub                                   | Ativo       |
| Gestão de Projeto  | GitHub Projects (Issues para Épicos/Stories)   | Em uso      |
| Ferramenta de BD   | DBeaver                                        | Disponível  |
| Containerização    | Docker Desktop                                 | Funcionando |
| Testes Unitários   | pytest                                         | A implementar|
| CI/CD              | Google Cloud Build                             | 95% completo|
| Cloud CLI          | Google Cloud CLI (Windows)                     | Configurado |
| Firebase CLI       | firebase-tools                                 | Configurado |
| Container Registry | Google Artifact Registry (us-central1)         | Configurado |

## 9. Estratégia de Qualidade e Métricas

* **Testes:** Cobertura de testes unitários > 80% com `pytest`. Testes de integração automatizados em cada Pull Request.
* **Métricas Chave:** API response time < 200ms, Uptime > 99.9%.
* **Monitorização:** Cloud Logging e Cloud Monitoring configurados no pipeline.