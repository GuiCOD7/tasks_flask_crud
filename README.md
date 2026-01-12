# To-Do List API — Aprendendo Flask

Esse projeto é parte do meu processo de aprendizado com Python, Flask e APIs REST. É meu primeiro repositório no GitHub, feito para entender na prática como funciona um CRUD, requisições HTTP e testes automatizados.

A ideia principal é simples: uma API de tarefas (to-do list) onde é possível criar, listar, atualizar e deletar tarefas (CREATE, READ, UPDATE, DELETE).
## Pontos importantes do projeto

* API REST simples usando Flask

* Implementação completa de CRUD

* Uso de JSON para envio e retorno de dados

* Rotas dinâmicas com parâmetros (/tasks/<id>)

* Organização básica do projeto em arquivos

* Testes automatizados usando pytest

* Consumo da API via Postman e requests
## Tecnologias usadas

Python 3.12 — linguagem principal do projeto

Flask — framework web para criação da API REST

Pytest — criação de testes automatizados

Requests — consumo da API nos testes

Postman — testes manuais das rotas da API

Git — controle de versão do projeto

GitHub — hospedagem e versionamento do repositório

Virtual Environment (venv) — isolamento do ambiente de desenvolvimento
Funcionalidades da API

Swagger (OpenAPI)
Utilizado para documentar a API de forma visual e interativa.

Com o Swagger é possível:

- Visualizar todas as rotas disponíveis

- Testar requisições (GET, POST, PUT, DELETE) diretamente pelo navegador

- Entender melhor como a API funciona sem precisar ler o código

## Rodando os testes dentro do POSTMAN

### Criar uma tarefa

```bash
POST /tasks
```
#### Body (JSON):
```
{
  "title": "Estudar inglês",
  "description": "Estudar inglês por 1 hora",
  "completed": True
}
```
### Listar todas as tarefas
```bash
GET /tasks
```
#### Resposta:
```
{
  "tasks": [
    {
      "id": 1,
      "title": "Estudar inglês",
      "description": "Estudar inglês por 1 hora",
      "completed": True
    }
  ],
  "total_tasks": 1
}
```
### Buscar uma tarefa por ID
```
GET /tasks/{id}

para pegar tarefa ESPECÍFICA por /{id}
```
#### Parâmetros

| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `id`      | `int` | O ID do item que você quer (**Tarefa**) |

### Atualizar uma tarefa
```
PUT /tasks/{id}
```
#### Resposta

```
{
  "title": "Tarefa atualizad",
  "description": ""Nova descrição",
  "completed": true
}
```
## Testes automatizados
##### O projeto possui testes automatizados usando pytest, cobrindo:

* Criação de tarefas
* Listagem de tarefas
* Busca por ID
* Atualização
* Remoção

## Como rodar o projeto
```
# Clonar o repositório
git clone https://github.com/seu-usuario/seu-repositorio.git

# Entrar no projeto
cd tasks_flask_crud

# Criar ambiente virtual
python -m venv venv

# Ativar o ambiente virtual
venv\Scripts\activate

# Instalar dependências
pip install -r requirements.txt

# Rodar a aplicação
python app.py

```

***Observações** *

Esse projeto não utiliza banco de dados.
As tarefas ficam armazenadas em memória, com foco total em aprendizado e prática.


## Autor

Projeto desenvolvido por Guilherme Braga

- Estudante de Python e desenvolvimento backend

-   Aprensentação do repositório feito em  - [Readme.so](https://readme.so/pt/editor)