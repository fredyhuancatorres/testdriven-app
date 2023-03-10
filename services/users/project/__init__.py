# services/users/project/__init__.py


import os

from flask import Flask  # new
from flask_bcrypt import Bcrypt  # new
from flask_cors import CORS  # new
from flask_debugtoolbar import DebugToolbarExtension  # new
from flask_migrate import Migrate  # new
from flask_sqlalchemy import SQLAlchemy

# instantiate the db
db = SQLAlchemy()
toolbar = DebugToolbarExtension()  # new
cors = CORS()  # new
migrate = Migrate()  # new
bcrypt = Bcrypt()  # new


# new
def create_app(script_info=None):

    # instantiate the app
    app = Flask(__name__)

    # set config
    app_settings = os.getenv("APP_SETTINGS")
    app.config.from_object(app_settings)

    # set up extensions
    db.init_app(app)
    toolbar.init_app(app)  # new
    cors.init_app(app)  # new
    migrate.init_app(app, db)  # new
    bcrypt.init_app(app)  # new

    # register blueprints
    from project.api.users import users_blueprint
    app.register_blueprint(users_blueprint)
    from project.api.auth import auth_blueprint  # new
    app.register_blueprint(auth_blueprint)       # new

    # shell context for flask cli
    @app.shell_context_processor
    def ctx():
        return {"app": app, "db": db}

    return app
