from flask import Flask
from models import create_table


app = Flask(__name__)

create_table()

@app.route('/')
def home():
    return {"message": "API funcionando"}


if __name__ == '__main__':
    app.run(debug=True)
