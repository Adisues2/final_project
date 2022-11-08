from flask import request, redirect, render_template, flash, url_for, current_app, session
# from flask_login import login_required, logout
from werkzeug.utils import secure_filename
from app import app
from app import db
from app.forms import RegisterForm, LoginForm, ProductForm
from app.models import Register, Login, Product, CartItem, Brand, Category
import os
import secrets
import psycopg2

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLD = '/Users/lenovo/virtual/python_final_project/app/static/image'
UPLOAD_FOLDER = os.path.join(APP_ROOT, UPLOAD_FOLD)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


# def save_images(pic):
#     gallery = pic.filename
#     UPLOAD_FOLD = os.path.join(app.root_path, 'static/image',gallery)

@app.route('/')
def body_page():
    return render_template('home.html')


# @app.route('/cart/<int:id>', methods=['POST'])
# def add_to_cart(id):
#     try:
#         product_id = request.form.get('id')
#         cart = Product.query.filter_by(id=id).first()
#         if product_id and product_price and product_description and request.method == 'P0ST':
#             dict_items = {product_id: {"product_name": product.product_name, 'product_price': product.product_price,
#                                        'product_img': product.product_img}}
#         if 'cart_items' in session:
#             print(session['cart_items'])
#         else:
#             session['cart_items'] == dict_items
#             return redirect(request.referrer)
#     except   Exception as e:
#         print(e)
#     return render_template("body.html")


@app.route('/addProduct', methods=['GET', 'POST'])
def page():
    products = Product.query.all()
    form = ProductForm(request.form)
    if request.method == 'POST':
        if request.files:
            pic = request.files.get('pic')
            pic.save(os.path.join(app.root_path, 'static/image', secure_filename(pic.filename)))

            # name = request.form['name']
            # price = request.form['price']
            # description = request.form['description']
            # img = request.form['product_img']
            added = Product(name=form.name.data, price=form.price.data, description=form.description.data,
                            img=pic)
            if added:
                return 'saved image'
            db.session.add(added)
            db.session.commit()
        else:
            flash('file uploaded successfully')
        return redirect(url_for('login'))
    return render_template('addProduct.html', form=form, products=products)


@app.route('/product')
def index():
    products = Product.query.all()
    return render_template('box.html', products=products)


@app.route('/cart/<int:product_id>', methods=['POST'])
def add_to_cart(product_id):
    product = Product.query.filter(Product.id == product_id)
    cart_item = CartItem(product=product)
    db.session.add(cart_item)
    db.session.commit()

    return render_tempate('cart.html', product=products)


@app.route('/cart', methods=['POST', 'GET'])
def cart():
    if 'cart' not in session:
        session['cart'] = []
    if request.method == 'POST':
        cart_prod_name = request.form['cart_prod_name']
        session['cart'] += cart_prod_name
        return redirect('/cart')
    if request.method == 'GET':
        cart_products = session['cart']
        return render_template('/cart.html', cart_products=cart_products)


@app.route('/register', methods=['GET', 'POST'])
def customer_page():
    form = RegisterForm(request.form)
    if request.method == 'POST':
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']
            email = request.form['email']
            Address = request.form['Address']
            City = request.form['City']
            Country = request.form['Country']
            Zip = request.form['Zip']
            phone = request.form['phone']
            users = Register.query.filter_by(username=username).first()
            if users:
                return 'login successfully'
            new_object = Register(username=username, email=email, password=password, Address=Address, City=City,
                                  Country=Country, Zip=Zip, phone=phone)
            db.session.add(new_object)
            db.session.commit()
        return 'register successfully'
    return render_template('register.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login_page():
    form = LoginForm()
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        users = Login.query.filter_by(username=username).first()
        if users:
            return redirect(url_for('customer_page'))
        new_object = Login(username=username, password=password)
        db.session.add(new_object)
        db.session.commit()
        flash(' new user created', 'success')
        return redirect(url_for('customer_page'))
    return render_template('login.html', form=form)


@app.route('/logout')
# @login_required
def logout():
    logout()
    flash('you are logout', 'success')
    return redirect(url_for('login'))


@app.route('/addProduct')
def abs():
    return render_template('addProduct.html')


# @app.route('/home')
# def marginalized():
#     return render_template('index.html')


@app.route('/addbrand', methods=['GET', 'POST'])
def addbrand():
    if request.method == 'POST':
        getbrand = request.form.get('brand')
        brand = Brand(name=getbrand)
        db.session.add(brand)
        db.session.commit()
        flash(f'the brand{getbrand} was aded to your database', 'success')

        redirect(url_for('addbrand'))
    return render_template('addbrand.html', brands='brands')


@app.route('/addcat', methods=['GET', 'POST'])
def addcat():
    if request.method == 'POST':
        getbrand = request.form.get('category')
        cat = Category(name=getbrand)
        db.session.add(cat)
        flash(f'the category{getbrand} was added to your database', 'success')
        db.session.commit()
        redirect(url_for('addcat'))
    return render_template('addbrand.html')


