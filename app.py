from flask import (
    Flask,
    render_template
)
from routes.compras import (
    compras_bp
)

app = Flask(__name__)
app.secret_key = "cartera_activos"

app.register_blueprint(compras_bp)

@app.route("/")
def inicio():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)