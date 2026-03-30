from flask import Flask
from models import create_table
from routes import register_routes

app = Flask(__name__)
register_routes(app)

create_table()

@app.route('/')
def home():
    return {"message": "API funcionando"}

if __name__ == '__main__':
    app.run(debug=True)