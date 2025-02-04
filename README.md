# Time App ⏰

Um pipeline CI/CD simples com **Jenkins** e **Docker** para um aplicativo que exibe a hora atual.

## 📌 Tecnologias Utilizadas

- [Jenkins](https://www.jenkins.io/)
- [Docker](https://www.docker.com/)
- [Git](https://git-scm.com/)
- [Python](https://www.python.org/)

## 📜 Requisitos

Antes de começar, certifique-se de ter instalado:

- Docker
- Jenkins (com plugins para Docker e Git)
- Python 3+

## 🚀 Configuração do Jenkins

### 1️⃣ Instalar Plugins Necessários

No Jenkins, vá para:
**Dashboard → Gerenciar Jenkins → Gerenciar Plugins**

Instale os seguintes plugins:
- `git`
- `pipeline`
- `docker-workflow`
- `credentials-binding`

### 2️⃣ Configurar um Novo Pipeline

1. No Jenkins, clique em **Novo Item** → **Pipeline**.
2. No campo **Pipeline Script from SCM**, escolha **Git**.
3. Adicione a URL do repositório:
   ```
   https://github.com/dantas-barreto/time-app.git
   ```
4. Em **Branch Specifier**, use:
   ```
   */main
   ```
5. No campo **Script Path**, certifique-se de que está como:
   ```
   Jenkinsfile
   ```
6. Salve e execute o pipeline.

## 🛠️ Construção e Execução Manual

Caso queira testar sem o Jenkins, use os seguintes comandos:

```sh
# Clonar o repositório
git clone https://github.com/dantas-barreto/time-app.git
cd time-app

# Construir a imagem Docker
docker build -t time-app .

# Rodar o container
docker run --rm time-app
```

## 📌 Estrutura do Projeto

```
📂 time-app/
 ├── 📄 Dockerfile
 ├── 📄 Jenkinsfile
 ├── 📄 README.md
 ├── 📄 requirements.txt
 ├── 📄 app.py
```

## 📜 Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

---

🚀 Desenvolvido por João Pedro Barreto


 
