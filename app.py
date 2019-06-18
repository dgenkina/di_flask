from flask import Flask, render_template, request

from wtforms import Form
from wtforms import fields, validators
from wtforms.ext.sqlalchemy.fields import QuerySelectField
import pandas as pd
import re

from get_data_and_plot import plot_closing_prices
app = Flask(__name__)


ticker_list = pd.read_csv('WIKI_metadata.csv')['code'].tolist()
stock_list = pd.read_csv('WIKI_metadata.csv')['name'].tolist()
tick_list = []
for ind,tick in enumerate(ticker_list):
    name = re.split('\(',stock_list[ind])[0]
    tick_list.append((tick,name))
    
class SetDataParamsForm(Form):
    ticker = fields.SelectField('ticker', choices = tick_list)
    year = fields.IntegerField('Year', [validators.NumberRange(min=2005, max=2019)])
    month = fields.IntegerField('Month', [validators.NumberRange(min=1, max=12)])

  #  site = QuerySelectField(query_factory=Site.query.all)

@app.route('/tickers', methods=['GET', 'POST'])
def tickers():
    set_data_params_form = SetDataParamsForm()
    if request.method == 'GET':
        plot = None
    elif request.method == 'POST':
        ticker = str(request.form.get('ticker'))
        year = int(request.form.get('year'))
        month = int(request.form.get('month'))
        plot = plot_closing_prices(ticker_name=ticker,year=year,month=month)

    return render_template('tickers.html', form=set_data_params_form, plot=plot)


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(port=33507)
