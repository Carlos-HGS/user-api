# User API

API simples de gerenciamento de usuários desenvolvida com Flask e SQLite.

-----
## Funcionalidades

* Criar usuário (POST /users)
* Listar usuários (GET /users)
* Atualizar usuário (PUT /users/<id>)
* Deletar usuário (DELETE /users/<id>)
-----
## Tecnologias utilizadas

* Python
* Flask
* SQLite
-----
## Como rodar o projeto

```bash
git clone https://github.com/Carlos-HGS/user-api.git
cd user-api

python -m venv venv
venv\Scripts\activate

pip install flask

python app.py
```
-----
## Endpoints

### Criar usuário

POST /users

```json
{
  "name": "Carlos",
  "email": "carlos@email.com"
}
```
-----
### Listar usuários

GET /users

------
### Atualizar usuário

PUT /users/<id>

```json
{
  "name": "Novo Nome",
  "email": "novo@email.com"
}
```
-----
### Deletar usuário

DELETE /users/<id>

-----
## Status do projeto

Projeto funcional com operações CRUD completas e validações básicas.

-----
## Autor

Carlos Henrique Gouveia de Souza