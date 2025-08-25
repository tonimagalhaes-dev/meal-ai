# Contexto do Projeto MealIA

Este documento serve como um ponto de partida para contextualizar o assistente de IA sobre o estado atual, objetivos e stack tecnológico do projeto MealIA. **Última atualização: 25/08/2025.**

## 1. Resumo do Projeto (O Quê e Por Quê)

O MealIA é um projeto para desenvolver uma aplicação web que gera cardápios semanais personalizados para famílias, utilizando IA para as sugestões. O objetivo principal é o aprendizado prático de tecnologias modernas de desenvolvimento de software, cloud e IA, seguindo um plano de desenvolvimento estruturado.

## 2. Objetivos de Negócio (OKRs)

Os objetivos principais do projeto são:
* **Modernizar a Arquitetura Técnica:** Migrar 100% da aplicação para GCP, implementar CI/CD e atingir 99.9% de uptime.
* **Potencializar com IA:** Integrar o Vertex AI para geração inteligente de cardápios e implementar busca semântica.
* **Escalar para Produção:** Suportar mais de 1000 usuários simultâneos e implementar monitoramento completo.

## 3. Arquitetura e Stack de Tecnologia

Decidimos começar o projeto do zero com o seguinte stack:

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

* **25/08/2025:** **Progresso significativo na User Story 1.2!** Pipeline de CI/CD quase completo:
  - ✅ Projeto GCP configurado: `meal-ai-development`
  - ✅ Todas as APIs necessárias ativadas
  - ✅ Orçamento configurado (R$50/mês com alertas)
  - ✅ Google Cloud CLI instalado e configurado
  - ✅ Service Account criado: `cloudrun-deployer@meal-ai-development.iam.gserviceaccount.com`
  - ✅ Controle de ambiente implementado (dev/prod) no Dockerfile
  - ✅ Firebase Hosting configurado
  - ✅ Trigger do Cloud Build criado: `meal-ai-production-trigger`
  - ✅ Repositório GitHub conectado: `tonimagalhaes-dev/meal-ai`
  - 🚧 **Problema atual:** Build falhando por erro de repositório no Artifact Registry

---
### **✅ Story 1.1: Configuração do Ambiente de Desenvolvimento Local (CONCLUÍDA)**

**Como** desenvolvedor, **eu quero** um ambiente de desenvolvimento local totalmente containerizado com Docker, **para que** eu possa desenvolver o back-end (FastAPI) e o front-end (React) de forma isolada e consistente.

**Critérios de Aceitação:**

* [x] O comando `docker-compose up` inicia os contêineres do back-end, front-end e base de dados.
* [x] O back-end em FastAPI reinicia automaticamente ao salvar alterações no código (`hot reload`).
* [x] O front-end em React reinicia automaticamente ao salvar alterações no código (`hot reload`).

**Implementação finalizada:**
- Dockerfile com controle de ambiente via variável `ENVIRONMENT`
- docker-compose.yml configurado para modo development
- Hot reload funcionando perfeitamente em ambos os ambientes

---
### **🚧 Story 1.2: Setup do Projeto GCP e Deploy Contínuo no Cloud Run (90% COMPLETA)**

**Como** desenvolvedor, **Eu quero** configurar o projeto na Google Cloud e um pipeline de CI/CD, **Para que** cada *push* para a branch principal (`main`) seja automaticamente testado e implantado, disponibilizando a aplicação na nuvem.

**Critérios de Aceitação:**

* [x] O projeto no GCP está configurado com as APIs necessárias e Service Accounts seguras.
* [x] O pipeline de CI/CD (Cloud Build) é acionado a cada `push` na branch `main`.
* [ ] O pipeline executa os testes, constrói a imagem do back-end e a implanta no Cloud Run.
* [ ] O pipeline faz o build dos arquivos estáticos do front-end (React) e os implanta no Firebase Hosting.

**Progresso Detalhado:**

**✅ Fase 1: Configuração Inicial do GCP - CONCLUÍDA**
- Projeto GCP criado: `meal-ai-development`
- APIs ativadas: Cloud Run, Cloud Build, Firebase Hosting, Cloud SQL, Secret Manager, Artifact Registry
- Orçamento configurado: R$50/mês com alertas em 50%, 90% e 100%
- Google Cloud CLI instalado e autenticado no Windows

**✅ Fase 2: Service Accounts e Permissões - CONCLUÍDA**
- Service Account criado: `cloudrun-deployer@meal-ai-development.iam.gserviceaccount.com`
- Permissões concedidas:
  - `roles/run.admin` (Cloud Run)
  - `roles/storage.admin` (Container Registry)
  - `roles/secretmanager.secretAccessor` (Secret Manager)
  - `roles/logging.logWriter` (Cloud Logging)
  - `roles/artifactregistry.admin` (Artifact Registry)

**✅ Fase 3: Preparação do Código - CONCLUÍDA**
- Dockerfile otimizado para produção com controle de ambiente
- docker-compose.yml configurado com `ENVIRONMENT=development`
- cloudbuild.yaml criado com pipeline completo
- Configuração otimizada para Free Tier do GCP

**✅ Fase 4: Firebase Hosting - CONCLUÍDA**
- Firebase CLI instalado e configurado
- Projeto Firebase habilitado: `meal-ai-development-c160u`
- Arquivos firebase.json e .firebaserc criados
- Configuração para deploy do frontend (pasta frontend/build)

**🚧 Fase 5: Cloud Build Pipeline - EM PROGRESSO**
- Trigger criado: `meal-ai-production-trigger`
- Repositório GitHub conectado: `tonimagalhaes-dev/meal-ai`
- **Problema atual:** Build falhando devido a repositório inexistente no Artifact Registry

**Próximos Passos para Completar:**
1. Criar repositório no Artifact Registry:
   ```cmd
   gcloud artifacts repositories create mealia-backend --repository-format=docker --location=us-central1
   ```

2. Atualizar cloudbuild.yaml para usar Artifact Registry em vez de gcr.io

3. Testar build completo do backend no Cloud Run

4. Adicionar step do Firebase Hosting ao pipeline

5. Validar deploy end-to-end

**Arquivos de Configuração Atual:**
- `backend/Dockerfile`: Com controle dev/prod via ENVIRONMENT
- `docker-compose.yml`: Configurado para desenvolvimento
- `cloudbuild.yaml`: Pipeline CI/CD (precisa ajuste para Artifact Registry)
- `firebase.json`: Configuração do hosting
- `.firebaserc`: Projeto padrão configurado

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
* **Firebase Project ID:** meal-ai-development-c160u
* **Email da conta:** tonimagalhaes.dev@gmail.com
* **Orçamento:** R$50,00/mês com alertas configurados

### APIs Ativadas:
* Cloud Run API
* Cloud Build API
* Firebase Hosting API
* Cloud SQL Admin API
* Secret Manager API
* Artifact Registry API
* Container Registry API (gcr.io - sendo migrado para Artifact Registry)

### Service Accounts:
* **cloudrun-deployer@meal-ai-development.iam.gserviceaccount.com**
  - roles/run.admin
  - roles/storage.admin
  - roles/secretmanager.secretAccessor
  - roles/logging.logWriter
  - roles/artifactregistry.admin

### Repositório GitHub:
* **URL:** https://github.com/tonimagalhaes-dev/meal-ai
* **Branches:** 
  - `develop` (desenvolvimento ativo)
  - `main` (produção com deploy automático)
* **Trigger Cloud Build:** meal-ai-production-trigger (monitora branch main)

### Ambiente de Desenvolvimento:
* **Sistema Operacional:** Windows
* **Google Cloud CLI:** Instalado e configurado
* **Projeto padrão configurado:** meal-ai-development
* **Docker:** Ambiente local funcionando com hot reload
* **Firebase CLI:** Configurado

## 7. Problemas Conhecidos e Soluções Pendentes

### Problema Atual - Build Failure:
**Erro:** `denied: gcr.io repo does not exist. Creating on push requires the artifactregistry.repositories.createOnPush permission`

**Causa:** O pipeline está tentando usar gcr.io (Container Registry) que está sendo descontinuado, mas o repositório não existe.

**Solução Identificada:** 
1. Criar repositório no Artifact Registry
2. Migrar cloudbuild.yaml para usar `us-central1-docker.pkg.dev` em vez de `gcr.io`

### Estratégia de Branches:
- **develop:** Para desenvolvimento e testes
- **main:** Para deploy automático em produção
- Hot reload configurado apenas em ambiente de desenvolvimento

## 8. Ferramentas de Desenvolvimento e Gestão

| Categoria             | Ferramenta                                     | Status        |
| --------------------- | ---------------------------------------------- | ------------- |
| IDE                   | VS Code                                        | Configurado   |
| Controlo de Versão    | Git + GitHub                                   | Ativo         |
| Gestão de Projeto     | GitHub Projects (Issues para Épicos/Stories)  | Em uso        |
| Ferramenta de BD      | DBeaver                                        | Disponível    |
| Containerização       | Docker Desktop                                 | Funcionando   |
| Testes Unitários      | pytest                                         | A implementar |
| CI/CD                 | Google Cloud Build                             | 90% completo  |
| Cloud CLI             | Google Cloud CLI (Windows)                     | Configurado   |
| Firebase CLI          | firebase-tools                                 | Configurado   |
| Container Registry    | Google Artifact Registry (us-central1)        | A configurar  |

## 9. Estratégia de Qualidade e Métricas

* **Testes:** Cobertura de testes unitários > 80% com `pytest`. Testes de integração automatizados em cada Pull Request.
* **Métricas Chave:** API response time < 200ms, Uptime > 99.9%.
* **Monitorização:** Cloud Logging e Cloud Monitoring configurados no pipeline.

## 10. Papel da IA no Desenvolvimento

* **Chat do Gemini:** Utilizado como assistente de programação ("pair programmer") para ajudar no desenvolvimento do código, resolução de erros e aprendizagem de conceitos durante User-Storie 1.1

* **Claude (Anthropic):** Utilizado como assistente principal de desenvolvimento e arquitetura, ajudando na resolução de problemas complexos de infraestrutura e implementação usado na User-storie 1.2.

* **Google AI Studio:** Utilizado como laboratório para desenhar, testar e refinar os prompts que serão usados na funcionalidade de geração de cardápios.

## 11. Configuração de Custos e Free Tier

### Recursos Configurados para Free Tier:
- **Cloud Run:** 2M requests/mês, 400K GB-segundos/mês, 200K CPU-segundos/mês
- **Cloud Build:** 120 build-minutes/dia
- **Firebase Hosting:** 10GB storage, 10GB transfer/mês
- **Artifact Registry:** 0.5GB storage gratuito
- **Região otimizada:** us-central1 (melhor custo-benefício)

### Alertas de Orçamento:
- R$25,00 (50%) - Email alert
- R$45,00 (90%) - Email alert  
- R$50,00 (100%) - Email alert

**Próxima Sessão:** Resolver o problema do Artifact Registry e completar o deploy automático do backend no Cloud Run.

