from flask import Flask
from App import setting
from App.ext import init_ext
from App.models.uploadpictures import Indexpic


def create_app(name):
    app = Flask(__name__)
    app.config.from_object(setting.ENV_NAME.get(name))
    app.debug = True
    init_ext(app, name)
    app.config.update(RESTFUL_JSON=dict(ensure_ascii=False))
    add = Indexpic()
    return app