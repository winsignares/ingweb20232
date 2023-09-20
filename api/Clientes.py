from flask import Blueprint, jsonify

from models.Clientes import Clientes, ClienteSchema

ruta_cliente = Blueprint("ruta_cliente",__name__)
#routes_cliente = Blueprint("routes_cliente", __name__)

cliente_schema = ClienteSchema()
clientes_schema = ClienteSchema(many=True)

@ruta_cliente.route("/clientes", methods=["GET"])
def clientes():
    resultall = Clientes.query.all()
    result = clientes_schema.dump(resultall)
    return jsonify(result)
