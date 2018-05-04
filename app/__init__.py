#!usr/bin/python
#Flask Imports
from flask import Flask
from flask_login import LoginManager, login_required
import config
from functools import wraps
from mongoengine import connect
from mongoengine import *
from mongoengine import errors  as mgengErrors
from mongoengine.queryset.visitor import Q
from mongoengine.connection import MongoEngineConnectionError
import sys

class CustomFlask(Flask):
    jinja_options = Flask.jinja_options.copy()
    jinja_options.update(dict(
        block_start_string='{%',
        block_end_string='%}',
        variable_start_string='%%',
        variable_end_string='%%',
        comment_start_string='<#',
        comment_end_string='#>',
    ))

#flask App
app = CustomFlask(__name__,static_url_path='')

#login manager for handling user logins    
login_manager = LoginManager()


login_manager.init_app(app)
login_manager.login_message = "You must be logged in to access this page."
login_manager.login_view = "auth.login"


try:
    conn = connect(config.MONGO_DATABASE_DB, host = config.MONGO_HOST, port = config.MONGO_PORT, username = config.MONGO_USERNAME, password =config.MONGO_USER_PASSWORD)
    #conn = connect(config.MONGO_DATABASE_DB, host ="localhost", port =27017)
except MongoEngineConnectionError as e:
    print(e)
    print("Connection to given mongodb Settings Failed. Please check for connection parameters")
    sys.exit(0)


app.config.from_object('config')



#Import all the DB Models
from app.auth import models
from app.main import models

from app.auth.models import User
#Load user to load user from ID upon new request.. Commented out now for testing 
@login_manager.user_loader
def load_user(user_id):
    return User.objects(emailId = user_id).first()





#login_required() overriden inorder to accomodate next params
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if (not current_user.is_authenticated):
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function


from .auth import auth as auth_blueprint
app.register_blueprint(auth_blueprint)

from .main import main as main_blueprint
app.register_blueprint(main_blueprint)

from .api import api as api_blueprint
app.register_blueprint(api_blueprint, url_prefix="/api")
