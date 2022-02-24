import os
from dotenv import load_dotenv
load_dotenv()


basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = '1111'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    FLASK_APP = os.environ.get('FLASK_APP')
    FLASK_ENV = os.environ.get('FLASK_ENV')
