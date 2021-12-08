from flask import Flask, render_template, request
from forex_python.converter import CurrencyRates, CurrencyCodes
from decimal import *

c = CurrencyRates(force_decimal=True)
codes = CurrencyCodes()

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/convert')
def convert():
    currency1 = request.args.get('currency1')
    currency2 = request.args.get('currency2')
    amount = request.args.get('amount')
    result = c.convert(base_cur=currency1, dest_cur=currency2, amount=Decimal(amount))

    return render_template('results.html',
                            symbol=codes.get_symbol(currency2),
                            result=round(result, 2)
                            )
