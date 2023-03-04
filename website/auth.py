from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)

@auth.route('/login', methods = ['GET', 'POST'])
def login():
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
        stockSymbol = request.form.get('stockSymbol')

        if len(email) < 2:
            flash('Email invalid', category = 'error')
        elif len(firstName) < 2:
            flash('Name invalid', category = 'error')
        elif len(stockSymbol) < 3:
            flash('Invalid', category = 'error')
        else:
            #add user to database 
            flash('Account created!', category = 'success')
    else:
        pass

    return render_template("sign_up.html") 