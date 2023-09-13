#aquì colocamos los comandos para la configuraciòn con la bd de mysql
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

# Realizar la conexiòn

app = Flask(__name__)

app.secret_key = "IngeWeb"
