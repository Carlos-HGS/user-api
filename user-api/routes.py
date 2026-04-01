from flask import request, jsonify
from database import connect


def register_routes(app):

    @app.route('/users', methods=['POST'])
    def create_user():
        data = request.json

        # verifica se veio JSON
        if not data:
            return {"error": "JSON inválido"}, 400

        # valida campos obrigatórios
        if 'name' not in data or 'email' not in data:
            return {"error": "Campos 'name' e 'email' são obrigatórios"}, 400

        conn = connect()
        cursor = conn.cursor()

        # verifica email duplicado
        cursor.execute("SELECT * FROM users WHERE email=?", (data['email'],))
        user = cursor.fetchone()

        if user:
            conn.close()
            return {"error": "Email já cadastrado"}, 400

        cursor.execute(
            "INSERT INTO users (name, email) VALUES (?, ?)",
            (data['name'], data['email'])
        )

        conn.commit()
        conn.close()

        return {
            "message": "Usuário criado",
            "user": {
                "name": data["name"],
                "email": data["email"]
            }
        }, 201

    @app.route('/users', methods=['GET'])
    def get_users():
        conn = connect()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM users")
        users = cursor.fetchall()

        formatted = []
        for user in users:
            formatted.append({
                "id": user[0],
                "name": user[1],
                "email": user[2]
            })

        conn.close()

        return jsonify(formatted)

    @app.route('/users/<int:user_id>', methods=['PUT'])
    def update_user(user_id):
        data = request.json

        if not data:
            return {"error": "JSON inválido"}, 400

        if 'name' not in data or 'email' not in data:
            return {"error": "Campos obrigatórios faltando"}, 400

        conn = connect()
        cursor = conn.cursor()

        # verifica se usuário existe
        cursor.execute("SELECT * FROM users WHERE id=?", (user_id,))
        user = cursor.fetchone()

        if not user:
            conn.close()
            return {"error": "Usuário não encontrado"}, 404

        cursor.execute(
            "UPDATE users SET name=?, email=? WHERE id=?",
            (data['name'], data['email'], user_id)
        )

        conn.commit()
        conn.close()

        return {"message": "Usuário atualizado"}

    @app.route('/users/<int:user_id>', methods=['DELETE'])
    def delete_user(user_id):
        conn = connect()
        cursor = conn.cursor()

        # verifica se existe
        cursor.execute("SELECT * FROM users WHERE id=?", (user_id,))
        user = cursor.fetchone()

        if not user:
            conn.close()
            return {"error": "Usuário não encontrado"}, 404

        cursor.execute("DELETE FROM users WHERE id=?", (user_id,))

        conn.commit()
        conn.close()

        return {"message": "Usuário deletado"}
