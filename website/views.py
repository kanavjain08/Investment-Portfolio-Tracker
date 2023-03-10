from flask import Blueprint, render_template, request
from flask_login import login_required, current_user
from getprice import *
from .models import Stock
from . import db

views = Blueprint('views', __name__)

@views.route('/home', methods = ['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        symbol = request.form.get('stocksymbol')
        stock_info = getData(symbol)
        stock = request.form.get('stock')
        new_stock = Stock(data = stock, user_id = current_user.id)
        db.session.add(new_stock)
        db.session.commit()
        return render_template("home.html", user = current_user, name = symbol, _data = stock_info)
    else:
        return render_template("home.html", user = current_user)


@views.route('/', methods = ['GET', 'POST'])
@login_required
def home_def(): 
    if request.method == 'POST':
        symbol = request.form.get('stocksymbol')
        stock_info = getData(symbol)
        new_stock = Stock(data = str(stock_info), user_id = current_user.id)
        db.session.add(new_stock)
        db.session.commit()
        return render_template("home.html", user = current_user, name = symbol, _data = stock_info)
    else:
        return render_template("home.html", user = current_user)

