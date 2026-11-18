# 📘 Atividade: Integrando FastAPI e SQLite

## 🎯 Objetivo

Evolua a API de livros feita com FastAPI para armazenar dados em um banco SQLite. Pratique persistência, consultas SQL parametrizadas e operações CRUD sem mudar o contrato dos endpoints.

## 📝 Tarefas

### 🛠️ Preparar o Banco e Listar Livros

#### Descrição
Execute o código inicial e explore como a aplicação cria o banco `books.db`, define a tabela `books` e lista os registros existentes.

#### Requisitos
O programa concluído deve:

- Instalar FastAPI e Uvicorn com `python -m pip install fastapi uvicorn`.
- Criar a tabela `books` com `id`, `title`, `author` e `year`.
- Implementar ou completar `GET /books` para consultar os livros no SQLite.
- Iniciar com `uvicorn main:app --reload` e exibir uma lista vazia quando o banco ainda não tiver livros.

### 🛠️ Cadastrar e Consultar Livros

#### Descrição
Implemente a criação de livros no banco e a consulta de um livro pelo identificador, usando as rotas da API anterior.

#### Requisitos
O programa concluído deve:

- Implementar `POST /books` para cadastrar `title`, `author` e `year` e responder com o identificador criado e status HTTP `201`.
- Implementar `GET /books/{book_id}` para consultar um livro específico.
- Usar parâmetros SQL (`?`) em vez de concatenar valores recebidos do usuário nas consultas.
- Retornar status HTTP `404` quando o livro solicitado não existir.

### 🛠️ Atualizar e Remover Livros Persistidos

#### Descrição
Complete as operações de atualização e remoção, confirmando que os dados continuam corretos depois de reiniciar o servidor.

#### Requisitos
O programa concluído deve:

- Implementar `PUT /books/{book_id}` para atualizar os campos de um livro existente.
- Implementar `DELETE /books/{book_id}` para remover um livro existente e responder com status HTTP `204`.
- Retornar status HTTP `404` ao tentar atualizar ou remover um livro inexistente.
- Preservar os dados cadastrados após encerrar e iniciar o servidor novamente.