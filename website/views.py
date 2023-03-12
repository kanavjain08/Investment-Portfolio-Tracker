from flask import Blueprint, render_template, request, jsonify
from flask_login import login_required, current_user
from getprice import *
from .models import Stock
from . import db
import json

views = Blueprint('views', __name__)

@views.route('/home', methods = ['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        symbol = request.form.get('stocksymbol')
        stock_info = getData(symbol)
        new_stock = Stock(data = str(stock_info), user_id = current_user.id)
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

@views.route('/delete-stock', methods = ['POST'])
def delete_item():
    stock = json.loads(request.data)
    stockId = stock['stockId'] 
    stock = Stock.query.get(stockId)
    if stock:
        if stock.user_id == current_user.id:
            db.session.delete(stock)
            db.session.commit()
            
    return jsonify({})
