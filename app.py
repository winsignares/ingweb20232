from flask import Flask, redirect, jsonify, render_template
from config.db import app

from api.Clientes import ruta_cliente

app.register_blueprint(ruta_cliente, url_prefix="/api")

@app.route("/")
def index():
    return "Hola mundo"

if __name__ == "__main__":
    app.run(debug=True, port=5000, host='0.0.0.0')