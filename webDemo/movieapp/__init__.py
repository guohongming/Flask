__author__ = 'Guo'
from flask import Flask
from movieapp.models.models import db_user
from movieapp.models import myjinjafilter
from movieapp.controllers.main import main_blueprint
from movieapp.extensions import bcrypt, login_manager

def create_app(object_name):
    """
    An flask application factory, as explained here:
    http://flask.pocoo.org/docs/patterns/appfactories/

    Arguments:
        object_name: the python path of the config object,
                     e.g. project.config.ProdConfig
    """

    app = Flask(__name__)
    app.config.from_object(object_name)
    app.jinja_env.filters['make_name_to_one'] = myjinjafilter.make_name_to_one
    db_user.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)

    app.register_blueprint(main_blueprint)

    return app

if __name__ == '__main__':
    app = app = create_app('config')
    app.run()
