from App.models import db
from App.models.modelUtil import ModelUtil

class Function(db.Model,ModelUtil):
    id = db.Column(db.Integer,primary_key=True)
    tittle = db.Column(db.String(128),nullable=False)
    desc = db.Column(db.Text,nullable=False)
    ftoken = db.Column(db.String(256),nullable=False)
    ishow = db.Column(db.Boolean,default=False)
    showpic = db.Column(db.String(256),nullable=False)
    desctitle1 =  db.Column(db.String(64),nullable=False)
    descontext1 = db.Column(db.Text, nullable=False)
    desctitle2 = db.Column(db.String(64), nullable=True)
    descontext2 = db.Column(db.Text, nullable=True)
    desctitle3 = db.Column(db.String(64), nullable=True)
    descontex3 = db.Column(db.Text, nullable=True)
    desctitle4 = db.Column(db.String(64), nullable=True)
    descontex4 = db.Column(db.Text, nullable=True)
