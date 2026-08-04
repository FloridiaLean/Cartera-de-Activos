from flask import Flask
from routes import registrar_blueprints

app = Flask(__name__)
app.secret_key = "cartera_activos"

registrar_blueprints(app)

if __name__ == "__main__":
    app.run(debug=True)