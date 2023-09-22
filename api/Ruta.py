from flask import Blueprint, jsonify

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
<<<<<<< HEAD

@ruta_ruta.route("/updateruta", methods=["PUT"])
def updatecliente():
    id = request.json['id']
    latitud = latitud.json['latitud']
    longitud = longitud.json['latitud']
    ncliente = ruta.query.get(id) #Select * from ruta where id = id
    
    db.session.commit()
    return "Datos Actualizado con exitos"
=======
#Ellery save rutas










#Hector actualizar Ruta










#Cammpo Eliminar








>>>>>>> 756de472d77f8bc9e2fac12da76c8e585356df60

