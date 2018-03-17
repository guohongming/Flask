__author__ = 'Guo'
from flask import Flask,request

from lockerapp.models import myjinjafilter
from lockerapp.controllers.main import main_blueprint
from lockerapp.controllers.device import device_blueprint
from lockerapp.controllers.captcha import captcha_blueprint
from flask_jwt import JWT


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

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Origin', '*')
        if request.method == 'OPTIONS':
            response.headers['Access-Control-Allow-Methods'] = 'DELETE, GET, POST, PUT'
            headers = request.headers.get('Access-Control-Request-Headers')
            if headers:
                response.headers['Access-Control-Allow-Headers'] = headers
        return response
    app.jinja_env.filters['make_name_to_one'] = myjinjafilter.make_name_to_one
    from lockerapp.auth.auths import Auth
    auth = Auth()
    jwt = JWT(app, auth.authenticate, auth.identity)

    from lockerapp.users.model import db
    db.init_app(app)
    from lockerapp.users.api import init_api
    init_api(app)




    app.register_blueprint(main_blueprint, url_prefix='/main')
    app.register_blueprint(device_blueprint, url_prefix='/device')
    app.register_blueprint(captcha_blueprint, url_prefix='/captcha')
    return app

if __name__ == '__main__':
    app = create_app('config')
    app.run()
