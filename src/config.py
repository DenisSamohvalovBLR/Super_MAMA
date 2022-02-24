import os
from dotenv import load_dotenv
load_dotenv()


basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = '6bedff746725f60c9cfa704b0730f7e41ffb78e5a5a2e9e65b5abe468484cf97d87892'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    FLASK_APP = os.environ.get('FLASK_APP')
    FLASK_ENV = os.environ.get('FLASK_ENV')
