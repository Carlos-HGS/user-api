from flask import request, jsonify
from database import connect

def register_routes(app):

    @app.route('/users', methods=['POST'])
    def create_user():
        data = request.json

        conn = connect()
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO users (name, email) VALUES (?, ?)",
            (data['name'], data['email'])
        )

        conn.commit()
        conn.close()

        return {"message": "Usuário criado com sucesso"}

    @app.route('/users', methods=['GET'])
    def get_users():
        conn = connect()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM users")
        users = cursor.fetchall()

        conn.close()

        return jsonify(users)