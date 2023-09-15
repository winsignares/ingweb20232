from flask import Flask, redirect, jsonify, render_template
from config.db import app

from api.Clientes import routes_cliente

app.register_blueprint(routes_cliente, uri_prefix="/api")

@app.route("/")
def index():
    return "Hola mundo"

if __name__ == "__main__":
    app.run(debug=True, port=5000, host='0.0.0.0')