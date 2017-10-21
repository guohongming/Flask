__author__ = 'Guo'

from flask_script import Manager, Server
from lockerapp import create_app
from lockerapp.models import models

app = create_app('lockerapp.config.DevConfig')
manager = Manager(app)
manager.add_command("runserver", Server())


@manager.shell
def make_shell_context():
    return dict(app=app, db=models.db_user, User=models.User)


if __name__ == '__main__':
    manager.run()