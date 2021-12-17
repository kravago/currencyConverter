from flask import Flask, render_template, request, flash, redirect
from forex_python.converter import CurrencyRates, CurrencyCodes
from decimal import *
import numbers

c = CurrencyRates(force_decimal=True)
codes = CurrencyCodes()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'LETSCONVERTMONEY'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/convert')
def convert():
    currency1 = request.args.get('currency1')
    currency2 = request.args.get('currency2')
    amount = request.args.get('amount')

    # Check the inputs
    messages=[]
    if codes.get_currency_name(currency1) is None:
        messages.append(f'{currency1} is not a valid currency code')

    if codes.get_currency_name(currency2) is None:
        messages.append(f'{currency2} is not a valid currency code')

    if amount.isnumeric() == False:
        messages.append(f'{amount} is an invalid amount')

    if len(messages) > 0:
        for message in messages:
            flash(message)

        return redirect('/')
    
    result = c.convert(base_cur=currency1, dest_cur=currency2, amount=Decimal(amount))

    return render_template('results.html',
                            symbol=codes.get_symbol(currency2),
                            result=round(result, 2)
                            )
