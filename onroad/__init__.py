from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_wtf import FlaskForm,CSRFProtect

from werkzeug.utils import secure_filename
from flask_restful import Api





app = Flask(__name__)
api=Api(app)

app.config['SECRET_KEY'] = '8ea2a86e42689205dde0ba81f31138b6'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///road.db'

db = SQLAlchemy(app)

login_manager = LoginManager(app) 



from onroad import routes