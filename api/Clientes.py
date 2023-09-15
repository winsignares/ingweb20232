from flask import blueprints, jsonify

from models.Clientes import Clientes, ClienteSchema

routes_cliente = blueprints("routes_cliente", __name__)

cliente_schema = ClienteSchema()
clientes_schema = ClienteSchema(many=True)

@routes_cliente.route("/clientes", methods=["GET"])
def clientes():
    resultall = Clientes.query.all()
    result = clientes_schema.dump(resultall)
    return jsonify(result)
