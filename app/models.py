from wtforms import FileField

from app import db, login_manager
from flask_login import UserMixin
from datetime import datetime


@login_manager.user_loader
def user_loader(user_id):
    return Register.query.get(user_id)


class Register(db.Model, UserMixin):
    __tablename__ = "users"
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(50), unique=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(50), unique=True)
    Address = db.Column(db.String(50), unique=True)
    City = db.Column(db.String(50), unique=True)
    Country = db.Column(db.String(50), unique=True)
    Zip = db.Column(db.String(50), unique=True)
    phone = db.Column(db.String(50), unique=True)


def __repr__(self, firstname, lastname):
    self.firstname = firstname
    self.lastname = lastname


class Login(db.Model):
    __tablename__ = "login"

    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(20), unique=True)
    password = db.Column(db.String(10), unique=True)


class Product(db.Model):
    __tablename__ = 'product'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    description = db.Column(db.Text, unique=True, nullable=True)
    price = db.Column(db.Float, nullable=False)
    img = db.Column(db.String(64), unique=True)
    cartitems = db.relationship('CartItem', backref='Product')


def __repr__(self):
    return '<ProductName %r>' % self.name


class CartItem(db.Model):
    __tablename__ = 'cartitems'
    id = db.Column(db.Integer, primary_key=True)
    # adding the foreign key
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'))


class Brand(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False, unique=True)


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False, unique=True)
