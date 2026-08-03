from flask import Flask,render_template,request

from persistencia import (
    cargar_operaciones,
    cargar_posiciones,
    guardar_operaciones,
    guardar_posiciones
)
from servicios import (
registrar_compra
)

app = Flask(__name__)

operaciones = cargar_operaciones()
posiciones = cargar_posiciones()

@app.route("/")
def inicio():
    return render_template("index.html")

@app.route("/compras", methods=["GET","POST"])
def compras():
    
    if request.method == "POST":
        
        activo = request.form["activo"]
        monto = float(request.form["monto"])
        precio = float(request.form["precio"])

        exito = registrar_compra(operaciones,posiciones,None,activo,monto,precio)
    
        if exito:
            guardar_operaciones(operaciones)
            guardar_posiciones(posiciones)
        
    return render_template("compras.html")

if __name__ == "__main__":
    app.run(debug=True)