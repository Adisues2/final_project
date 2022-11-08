from flask import Flask, request
<<<<<<< HEAD
#from flask import Bcrypt
=======
#from flask_login import Bcrypt
>>>>>>> e5e478a116cf489d28fe293b5e7b83fe9f350fdb
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
import os

# Flask Object
app = Flask(__name__)
app.config['SECRET_KEY'] = "this is a secret"
app.config['DEBUG'] = True
os.system('set FLASK_APP=wsgi.py')
UPLOAD_FOLDER = 'static/image'
ALLOWED_EXTENSIONS = set('*.doc')
# Database Connection

app.config[
    'SQLALCHEMY_DATABASE_URI'] = f'postgresql://postgres:12345@localhost/project'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Database Representation
db = SQLAlchemy(app)
migrate = Migrate(app, db)
db.init_app(app)
<<<<<<< HEAD
# bcrypt = Bcrypt(app)
=======
#bcrypt = Bcrypt(app)
>>>>>>> e5e478a116cf489d28fe293b5e7b83fe9f350fdb
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "customerLogin"
login_manager.needs_refresh_message_category = 'danger'
login_manager.login_message = u"please login first"
from app import forms, models, route
