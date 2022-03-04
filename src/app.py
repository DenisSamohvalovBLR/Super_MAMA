from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

login_manager = LoginManager(app)
login_manager.login_view = 'authorization'
login_manager.login_message = 'Log in to access restricted pages'
login_manager.login_message_category = 'success'

"""don't delete that part"""
from models import db_models