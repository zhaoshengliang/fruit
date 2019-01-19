from App.models import db
from App.models.modelUtil import ModelUtil

class Indexpic(db.Model,ModelUtil):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(62),unique=True)
    src = db.Column(db.String(256),unique=True)
