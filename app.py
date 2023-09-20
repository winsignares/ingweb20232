from flask import Flask, redirect, jsonify, render_template
from config.db import app

from api.Clientes import ruta_cliente
from api.Ruta import  ruta_ruta

app.register_blueprint(ruta_cliente, url_prefix="/api")
app.register_blueprint(ruta_ruta, url_prefix="/api")


@app.route("/")
def index():
    return "Hola mundo"

if __name__ == "__main__":
    app.run(debug=True, port=5000, host='0.0.0.0')