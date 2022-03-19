import os

from app import app

basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SECRET_KEY'] = 'you-will-never-guess'

# Other FLASK config varaibles ...
app.config["ALLOWED_EXTENSIONS"] = ["jpg", "png", "mov", "mp4", "mpg"]
app.config["MAX_CONTENT_LENGTH"] = 1000 * 1024 * 1024  # 1000mb

app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://postgres:12345@localhost/project'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
