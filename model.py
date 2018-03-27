from flask import Flask
from flask_mongoengine import MongoEngine
db = MongoEngine()

app = Flask(__name__)
app.config.from_json('config.json')
db.init_app(app)

class Contato(db.Document):
    nome = db.StringField(required=True, max_length=100)
    sobrenome = db.StringField(required=True, max_length=100)
    canal = db.StringField(max_length=50)
    valor =db.StringField(max_length=100)
    obs = db.StringField(max_length=500)