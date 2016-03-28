#! /usr/bin/env python

import os

from flask.ext.script import Manager

from app import create_app, db


app = create_app(os.getenv('APP_CONFIG', 'default'))
manager = Manager(app)


@manager.shell
def make_shell_context():
    return dict(app=app, db=db)


if __name__ == '__main__':
    manager.run()
