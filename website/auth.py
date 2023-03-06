from flask import Blueprint, render_template, request, flash
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash

auth = Blueprint('auth', __name__)

@auth.route('/login', methods = ['GET', 'POST'])
def login():
    data = request.form
    print(data)
    return render_template("login.html", boolean = True)

@auth.route('/logout')
def logout():
    return "hello"

@auth.route('/sign-up', methods = ['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password = request.form.get('password')
        stocksymbol = request.form.get('stocksymbol')
        if len(email) < 2:
            flash('Email invalid', category = 'error')
        elif len(firstName) < 2:
            flash('Name invalid', category = 'error')
        elif len(stocksymbol) <2:
            flash('Stock invalid', category = 'error')
        else:
            new_user = User(email = email, firstName = firstName)
            flash('Account created!', category = 'success')
    return render_template("sign_up.html")
    