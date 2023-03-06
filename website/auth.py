from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User, Note
from werkzeug.security import generate_password_hash, check_password_hash
from . import db

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
        first_name = request.form.get('firstName')
        password = request.form.get('password')
        stocksymbol = request.form.get('stocksymbol')
        if len(email) < 2:
            flash('Email invalid', category = 'error')
        elif len(first_name) < 2:
            flash('Name invalid', category = 'error')
        #elif len(stocksymbol) <2:
            #flash('Stock invalid', category = 'error')
        else:
            new_user = User(email = email, first_name = first_name, password = generate_password_hash(password, method = 'sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash('Account created!', category = 'success')
            #return redirect(url_for('views.home'))
    return render_template("sign_up.html")
    