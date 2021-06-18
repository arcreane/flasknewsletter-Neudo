from flask import Flask
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect



app = Flask(__name__)
app.config['SECRET_KEY'] = '436ab96a7efdc88c90f2c81e5a5bba9e'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/photo_blog'
db = SQLAlchemy(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'Bienvenue au login de l application !!'

csrf = CSRFProtect()

bcrypt = Bcrypt(app)

from OurApp import routes
