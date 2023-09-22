from config.db import app, db, ma

class Ruta(db.Model):
    __tablename__ = "tblrutas"

    id = db.Column(db.Integer, primary_key = True)
    idcliente = db.Column(db.Integer, db.ForeignKey('tblCliente.id'))

    latitud = db.Column(db.Integer)
    longitud = db.Column(db.Integer)

    def __init__(self, idcliente):
        self.idcliente = idcliente

    def __init__(self, latitud):
        self.latitud = latitud

    def __init__(self, longitud):
        self.longitud = longitud


with app.app_context():
    db.create_all()

class RutaSchema(ma.Schema):
    class Meta:
        fields = ('id', 'idcliente')