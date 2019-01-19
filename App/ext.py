from flask_bootstrap import Bootstrap
from flask_debugtoolbar import DebugToolbarExtension
from flask_migrate import Migrate
from flask_session import Session
from App.models import db
from App.views import blue

def init_ext(app,name):
    app.register_blueprint(blueprint=blue)
    # de = DebugToolbarExtension()
    # de.init_app(app=app)
    Session(app=app)
    db.init_app(app=app)
    Migrate(db=db, app=app)
    Bootstrap(app=app)

