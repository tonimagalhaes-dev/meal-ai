# Contexto do Projeto MealIA

Este documento serve como um ponto de partida para contextualizar o assistente de IA sobre o estado atual, objetivos e stack tecnológico do projeto MealIA. **Última atualização: 22/08/2025.**

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
    * **Nota de Custo:** O projeto será desenvolvido priorizando o uso do **Free Tier do GCP** para limitar o consumo e os custos. É crucial configurar alertas de orçamento e monitorizar o uso para evitar cobranças inesperadas.
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

* **22/08/2025:** **Progresso significativo na User Story 1.2!** A configuração inicial do GCP foi concluída com sucesso:
  - ✅ Projeto GCP criado: `meal-ai-development`
  - ✅ Todas as APIs necessárias ativadas (Cloud Run, Cloud Build, Firebase Hosting, Cloud SQL, Secret Manager)
  - ✅ Orçamento configurado (R$50/mês com alertas em 50%, 90% e 100%)
  - ✅ Google Cloud CLI instalado e configurado no ambiente Windows

---
### **✅ Story 1.1: Configuração do Ambiente de Desenvolvimento Local (CONCLUÍDA)**

**Como** desenvolvedor, **eu quero** um ambiente de desenvolvimento local totalmente containerizado com Docker, **para que** eu possa desenvolver o back-end (FastAPI) e o front-end (React) de forma isolada e consistente.

**Critérios de Aceitação:**

* [x] O comando `docker-compose up` inicia os contêineres do back-end, front-end e base de dados.
* [x] O back-end em FastAPI reinicia automaticamente ao salvar alterações no código (`hot reload`).
* [x] O front-end em React reinicia automaticamente ao salvar alterações no código (`hot reload`).

---
### **🚧 Story 1.2: Setup do Projeto GCP e Deploy Contínuo no Cloud Run (EM PROGRESSO)**

**Como** desenvolvedor, **Eu quero** configurar o projeto na Google Cloud e um pipeline de CI/CD, **Para que** cada *push* para a branch principal (`main`) seja automaticamente testado e implantado, disponibilizando a aplicação na nuvem.

**Critérios de Aceitação:**

* [x] O projeto no GCP está configurado com as APIs necessárias e Service Accounts seguras.
* [ ] O pipeline de CI/CD (Cloud Build) é acionado a cada `push` na branch `main`.
* [ ] O pipeline executa os testes, constrói a imagem do back-end e a implanta no Cloud Run.
* [ ] O pipeline faz o build dos arquivos estáticos do front-end (React) e os implanta no Firebase Hosting.

**Progresso Atual:**
- ✅ **Fase 1: Configuração Inicial do GCP** - CONCLUÍDA
  - Projeto GCP criado com sucesso
  - Todas as APIs necessárias ativadas
  - Orçamento e alertas configurados
  - Google Cloud CLI instalado e autenticado

**Próximos Passos:**
- 📋 **Fase 2: Service Accounts e Permissões**
  - Criar Service Account para deploy automático
  - Configurar IAM roles necessárias
  - Gerar e configurar chaves de autenticação

- 📋 **Fase 3: Preparação do Código para Deploy**
  - Ajustar Dockerfiles para produção
  - Configurar variáveis de ambiente
  - Preparar frontend para build estático

- 📋 **Fase 4: Pipeline CI/CD**
  - Criar arquivo cloudbuild.yaml
  - Configurar triggers automáticos
  - Setup do Firebase Hosting
  - Testar deploy completo

---
### **Story 1.3: Conectividade com o Banco de Dados Cloud SQL**

**Como** desenvolvedor, **Eu quero** que a aplicação no Cloud Run se conecte de forma segura a uma instância do Cloud SQL (PostgreSQL), **Para que** os dados da aplicação tenham persistência confiável e escalável.

**Critérios de Aceitação:**

* [ ] A instância do Cloud SQL (PostgreSQL) está criada e configurada com boas práticas de segurança.
* [ ] As migrações da base de dados (schema) são geridas via Alembic.
* [ ] As credenciais da base de dados de produção são armazenadas de forma segura no Google Secret Manager.

---

## 6. Configuração do Projeto GCP

### Informações do Projeto:
* **Nome:** Meal-AI Development
* **Project ID:** meal-ai-development
* **Email da conta:** tonimagalhaes.dev@gmail.com
* **Orçamento:** R$50,00/mês com alertas configurados

### APIs Ativadas:
* Cloud Run API
* Cloud Build API
* Firebase Hosting API
* Cloud SQL Admin API
* Secret Manager API

### Ambiente de Desenvolvimento:
* **Sistema Operacional:** Windows
* **Google Cloud CLI:** Instalado e configurado
* **Projeto padrão configurado:** meal-ai-development

## 7. Ferramentas de Desenvolvimento e Gestão

| Categoria             | Ferramenta                                     |
| --------------------- | ---------------------------------------------- |
| IDE                   | VS Code                                        |
| Controlo de Versão    | Git + GitHub                                   |
| Gestão de Projeto     | GitHub Projects (Issues para Épicos/Stories) |
| Ferramenta de BD      | DBeaver                                        |
| Containerização       | Docker Desktop                                 |
| Testes Unitários      | pytest                                         |
| CI/CD                 | Google Cloud Build                             |
| Plataforma de IA      | Google Vertex AI                               |
| Cloud CLI             | Google Cloud CLI (Windows)                     |

## 8. Estratégia de Qualidade e Métricas

* **Testes:** Cobertura de testes unitários > 80% com `pytest`. Testes de integração automatizados em cada Pull Request.
* **Métricas Chave:** API response time < 200ms, Uptime > 99.9%.

## 9. Papel da IA no Desenvolvimento

* **Chat do Gemini:** Utilizado como assistente de programação ("pair programmer") para ajudar no desenvolvimento do código, resolução de erros e aprendizagem de conceitos.
* **Google AI Studio:** Utilizado como um laboratório para desenhar, testar e refinar os prompts que serão usados na funcionalidade de geração de cardápios, antes de os implementar no código.