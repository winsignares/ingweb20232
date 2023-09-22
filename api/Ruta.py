from flask import Blueprint, jsonify, request
from config.db import db, app, ma
from models.Ruta import Ruta, RutaSchema

ruta_ruta = Blueprint("ruta_ruta",__name__)
#routes_cliente = Blueprint("routes_cliente", __name__)

ruta_schema = RutaSchema()
rutas_schema = RutaSchema(many=True)

@ruta_ruta.route("/rutas", methods=["GET"])
def ruta():
    resultall = Ruta.query.all()# Select * from Ruta;
    result = rutas_schema.dump(resultall)
    return jsonify(result)
#Ellery save rutas
@ruta_ruta.route("/saveruta", methods=["POST"])
def saveruta():
    data = request.get_json()
    new_ruta = Ruta(data)
    db.session.add(new_ruta)
    db.session.commit()
    return "Ruta guardada con éxito"
#Hector actualizar Ruta










#Cammpo Eliminar









