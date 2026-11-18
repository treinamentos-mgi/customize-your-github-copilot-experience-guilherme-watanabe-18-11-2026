# 📘 Atividade: Building REST APIs com FastAPI

## 🎯 Objetivo

Construa uma API REST para gerenciar livros usando o framework FastAPI. Pratique criação de rotas, métodos HTTP, validação de dados com modelos Pydantic e respostas HTTP.

## 📝 Tarefas

### 🛠️ Criar a Aplicação e Listar Livros

#### Descrição
Prepare o ambiente, execute o código inicial e implemente a rota que retorna todos os livros cadastrados.

#### Requisitos
O programa concluído deve:

- Instalar FastAPI e Uvicorn com `python -m pip install fastapi uvicorn`.
- Expor a aplicação FastAPI pela variável `app` no arquivo `main.py`.
- Implementar `GET /books` para retornar a lista de livros.
- Permitir iniciar o servidor com `uvicorn main:app --reload` e visualizar a documentação interativa em `/docs`.

### 🛠️ Cadastrar e Consultar Livros

#### Descrição
Use um modelo Pydantic para validar os dados recebidos e implemente rotas para cadastrar um livro e consultar um livro pelo seu identificador.

#### Requisitos
O programa concluído deve:

- Definir os campos `title`, `author` e `year` para os dados de um livro.
- Implementar `POST /books` e retornar o livro criado com um identificador e status HTTP `201`.
- Implementar `GET /books/{book_id}` para retornar um livro específico.
- Retornar status HTTP `404` quando o identificador não corresponder a um livro cadastrado.

### 🛠️ Atualizar e Remover Livros

#### Descrição
Complete as operações de gerenciamento implementando a atualização e a remoção de livros existentes.

#### Requisitos
O programa concluído deve:

- Implementar `PUT /books/{book_id}` para atualizar os dados de um livro existente.
- Implementar `DELETE /books/{book_id}` para remover um livro existente e retornar status HTTP `204`.
- Retornar status HTTP `404` ao tentar atualizar ou remover um livro inexistente.