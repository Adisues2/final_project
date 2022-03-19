from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, IntegerField, FileField, PasswordField, BooleanField, SubmitField, \
    validators, TextAreaField
from wtforms.validators import data_required

from app.models import Register


class LoginForm(FlaskForm):
    username = StringField('Username', [validators.Length(min=6, max=35)])
    password = PasswordField('Password', [validators.Length(min=6, max=35)])
    submit = SubmitField('Sign In')


class RegisterForm(FlaskForm):
    username = StringField('Username', [validators.data_required()])
    first_name = StringField('first_name', [validators.data_required()])
    last_name = StringField('last_name', [validators.data_required()])
    Email = StringField('Email Address', [validators.data_required()])
    password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    Address1 = StringField("Address1", [validators.data_required()])
    City = StringField('City', [validators.data_required()])
    country = StringField('country', [validators.data_required()])
    State = StringField('State', [validators.data_required()])
    Zip = StringField('zip', [validators.data_required()])
    phone = StringField('phone', [validators.data_required()])
    submit = SubmitField('Register')


def validate_username(self, username):
    if Register.query.filter_by(username=username.data).first():
        raise validationError("the username already exist")


def validate_email(self, email):
    if Register.query.filter_by(email=email.data).first():
        raise validationError('the email is already exist')


class ProductForm(FlaskForm):
    name = StringField('product_name', [validators.data_required()])
    price = IntegerField('product_price', [validators.data_required()])
    img = TextAreaField('product_img', [validators.data_required()])
    description = IntegerField('product_description', [validators.data_required()])
