# **MealIA**

O MealIA é uma aplicação web para o planeamento de cardápios familiares semanais, utilizando Inteligência Artificial para gerar sugestões personalizadas. Este projeto está a ser desenvolvido com um foco em aprender e aplicar tecnologias modernas de desenvolvimento, cloud e IA.

## **🚀 Ambiente de Desenvolvimento Local com Docker**

Todo o ambiente de desenvolvimento é orquestrado pelo Docker Compose, garantindo consistência e facilidade de configuração.

### **Pré-requisitos**

* **Docker Desktop:** Certifique-se de que o [Docker Desktop](https://www.docker.com/products/docker-desktop/) está instalado e a correr na sua máquina.

### **Como Iniciar**

Para iniciar todos os serviços (Backend, Frontend e Banco de Dados), navegue até à pasta raiz do projeto no seu terminal e execute o seguinte comando:

docker-compose up \--build

* up: Inicia os contentores.  
* \--build: Reconstrói as imagens se houver alguma alteração nos Dockerfiles. Use este comando da primeira vez ou sempre que alterar a configuração de um serviço.

Após a execução, os serviços estarão disponíveis nos seguintes endereços:

### **Como Testar**

* **Frontend (React App):**  
  * Aceda a: http://localhost:3000  
  * Deverá ver a página inicial do React. As alterações feitas no código da pasta /frontend serão refletidas automaticamente no navegador (hot-reload).  
* **Backend (FastAPI):**  
  * Aceda a: http://localhost:8000  
  * Deverá ver a mensagem de boas-vindas da API em formato JSON.  
* **Banco de Dados (PostgreSQL):**  
  * Use o seu cliente de base de dados preferido (ex: DBeaver) para se conectar com as seguintes credenciais:  
    * **Host:** localhost  
    * **Porta:** 5432  
    * **Base de Dados:** mealiadb  
    * **Utilizador:** user  
    * **Senha:** password

### **Como Parar**

Para parar todos os serviços, pressione Ctrl \+ C no terminal onde o docker-compose está a correr. Depois, para garantir que os contentores são removidos, execute:

docker-compose down

### **Troubleshooting (Solução de Problemas)**

Se encontrar erros inesperados, especialmente relacionados com o uvicorn ou cache, pode ser necessário forçar uma limpeza completa do ambiente Docker.

**Atenção:** Estes comandos irão apagar todos os dados do seu banco de dados local.

1. **Parar e remover volumes:**  
   docker-compose down \-v

2. **Limpeza profunda do sistema Docker (remove todo o cache):**  
   docker system prune \-a \-f

Depois de executar a limpeza, tente iniciar o ambiente novamente com docker-compose up \--build."# MealIA - Deploy Test" 
"# MealIA - Deploy Test" 
"# MealIA - Deploy Test" 
"# Test Cloud Run API" 
"# Test service account permissions" 
