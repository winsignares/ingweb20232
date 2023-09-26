from config.db import app, db, ma

class Community(db.Model):
    __tablename__ = "tblCommunity"

    id_comunidad = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(250))

    def __init__(self, nombre):
        self.nombre = nombre

with app.app_context():
    db.create_all()

class CommunitySchema(ma.Schema):
    class Meta:
        fields = ('id_comunidad', 'nombre')